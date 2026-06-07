---
name: doc-renamer
description: Use when đổi tên file văn bản hành chính Việt Nam theo logic magic-renamer, chuẩn hóa tên file, hoặc xử lý document operations mức cơ bản trong agent RE-Legal.
version: 2.2.0
license: MIT
---

# Doc Renamer

## Overview

Skill này dùng cho 2 nhóm việc trong `RE-Legal`:
- **đặt tên file văn bản hành chính Việt Nam** theo logic `magic-renamer`;
- **document operations mức cơ bản** như inventory, classify, move file có kiểm soát.

Phần logic rename trong skill này được giữ theo **bản source mới nhất Sếp cung cấp** rồi bọc lại theo format Codex để dễ load, dễ bảo trì và không đứt skill graph của `RE-Legal`.

Đây là support skill cho legal workflow, không phải skill điều phối data room đa workstream. Nếu tác vụ biến thành data room orchestration quy mô lớn, request tracking hoặc coordination nhiều team, phải route sang `RE-HQ`.

## When to Use

Dùng skill này khi:
- Sếp muốn đổi tên file văn bản theo chuẩn;
- cần chuẩn hóa tên file quyết định, công văn, tờ trình, nghị định, thông tư, báo cáo;
- người dùng paste tiêu đề, nội dung, hoặc ảnh scan văn bản và hỏi nên đặt tên file là gì;
- cần inventory hồ sơ trước khi legal review;
- cần phân loại tài liệu hoặc move file có kiểm soát ở quy mô nhỏ hoặc vừa.

Do not use for:
- legal analysis nội dung tài liệu;
- approval path / permit / compliance analysis;
- review clause hợp đồng;
- điều phối data room nhiều stream;
- workflow cần nhiều owner hoặc approval chain liên phòng ban.

## Routing

- Dùng cùng `re-legal-intake-router` nếu chưa rõ đây chỉ là document ops nhẹ hay đã thành bài toán coordination.
- Dùng cùng `re-legal-deliverable-templates` nếu cần chốt output bằng `document-ops-report-template`.
- Nếu sau một đợt sync source mới mà logic rename / output shape / related skills thay đổi, rà thêm `re-legal-skill-maintenance` để tránh drift.
- Nếu sau intake thấy tác vụ là data room orchestration, request list management hoặc tài liệu phải chạy qua nhiều team, route sang `RE-HQ`.
- Skill này không thay thế `licensing-expert` hoặc `legal-counsel`; nó chỉ chuẩn bị đầu vào tài liệu hoặc trả lời bài toán naming / filing.

## Workflow

### Phần A — Đặt tên file văn bản theo logic magic-renamer

Khi người dùng cung cấp văn bản (nội dung, tiêu đề, hoặc hình ảnh scan), thực hiện tuần tự 3 bước sau.

### Bước 1 — Trích xuất 6 trường dữ liệu cốt lõi
Đọc kỹ phần Header và Tiêu đề của văn bản, tìm và xác định chính xác 6 thông tin:

#### 1. `isDraft` (Trạng thái dự thảo)
- `True` nếu: văn bản có chữ `DỰ THẢO`, hoặc vừa thiếu Số hiệu và thiếu Ngày tháng cụ thể.
- `False` nếu: văn bản đã chính thức ban hành.

#### 2. `date` (Ngày ban hành)
- Lấy theo format **DD/MM/YYYY**.
- Mẹo: kiểm tra kỹ xung quanh xem có ngày viết tay lệch dòng không.
- Nếu không tìm được ngày cụ thể → để trống.

#### 3. `docNumber` (Số hiệu)
- Lấy toàn bộ số hiệu có dấu `/` hoặc `-`.
- Bỏ qua: số đóng dấu đỏ đơn lẻ, số đến, số biên nhận.

#### 4. `agency` (Cơ quan ban hành)
- **Cấp Quận/Huyện/Thị xã/Phường/Xã**: chỉ lấy tên cơ quan đó, không thêm tên tỉnh/thành phố.
  - Đúng: `UBND huyện Nhà Bè`
  - Sai: `UBND huyện Nhà Bè TPHCM`
- **Sở/Ban/Ngành cấp tỉnh**: lấy tên Sở + tên tỉnh/thành phố.
  - Ví dụ: `Sở Xây dựng TP. Hồ Chí Minh`
- Bỏ qua dòng `CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM`.

#### 5. `docType` (Loại văn bản)
- Lấy từ tiêu đề: `Quyết định`, `Tờ trình`, `Báo cáo`, `Công văn`, `Nghị định`, `Thông tư`, v.v.

#### 6. `summary` (Trích yếu)
- Tóm tắt tối đa 15 từ, chỉ lấy thông tin quan trọng nhất.
- Dừng lại khi gặp: `kính gửi`, hoặc hết dòng in đậm sau `V/v`.

### Bước 2 — Dọn dẹp và chuẩn hóa dữ liệu
Sau khi có đủ 6 trường, tra cứu từ điển và xử lý như sau:

- `[Ngày tháng]` → convert sang `YYYYMMDD`.
- `[Số hiệu ngắn]` → chỉ lấy chuỗi số đầu tiên trước dấu `/` hoặc `-`.
  - Ví dụ: `112/2025/QH15` → `112`; `23-CP` → `23`.
- `[Cơ quan viết tắt]` → tra từ điển `agency_mapping` trong `references/dictionaries.md`.
  - Sau đó ghép thêm viết tắt tỉnh/thành nếu là Sở cấp tỉnh từ `province_mapping`.
- `[Loại văn bản viết tắt]` → tra từ điển `doc_type_mapping`.
- `[Trích yếu]` → thực hiện theo thứ tự:
  1. Bỏ các từ mào đầu: `Về việc`, `Ban hành`, `V/v`.
  2. Bỏ hậu tố: `của Quốc hội`, `của Chính phủ`.
  3. Cắt bỏ phần diễn giải thừa sau khi đã trích đủ ý chính.
  4. Viết hoa chữ cái đầu tiên.
  5. Tra và thay thế từ trong `summary_mapping`.
  6. Loại bỏ dấu tiếng Việt và ký tự đặc biệt `\ / : * ? " < > |`.

> Tra cứu đầy đủ các từ điển tại: `references/dictionaries.md`

### Bước 3 — Ráp tên file theo nhóm
Xác định văn bản thuộc **nhóm nào** rồi áp dụng công thức tương ứng.
Lưu ý chung: khoảng trắng thừa rút về 1, dùng `_` để bọc phần Trích yếu.

#### Nhóm 1 — Quy phạm pháp luật trung ương (Legislative)
Áp dụng khi loại văn bản là: **Luật**, **Nghị định**, **Thông tư**, hoặc **Nghị quyết** do Quốc hội/Chính phủ ban hành.

```text
[Năm ban hành] [Số hiệu ngắn] [CQ ban hành] _[Loại VB] [Trích yếu CÓ DẤU]
```

Ví dụ:
```text
2024 112 CP _ND Sửa đổi bổ sung một số điều Nghị định 43
2023 45 QH _Luat Dat dai
```

#### Nhóm 2 — Dự thảo (Draft)
Áp dụng khi `isDraft = True` (có chữ `Dự thảo` hoặc thiếu cả số hiệu lẫn ngày).

```text
Draft [Ngày nếu có / Năm nếu có] [Cơ quan] _[Loại VB] [Trich_yeu_khong_dau]
```

Ví dụ:
```text
Draft 2025 UBND _QD Phe duyet quy hoach su dung dat
Draft 20250315 SXD HCM _TTr De xuat cai tao he thong thoat nuoc
```

#### Nhóm 3 — Thông thường (Standard)
Áp dụng cho tất cả loại còn lại: Quyết định, Tờ trình, Báo cáo, Công văn...

```text
[YYYYMMDD] [Số hiệu ngắn] [CQ ban hành] _[Loại VB] [Trich_yeu_khong_dau]
```

Lưu ý Công văn:
- theo bản source mới nhất, `doc_type_mapping` có `công văn → CV`;
- khi áp dụng thực tế, bám đúng mapping hiện có trong `references/dictionaries.md` của skill này.

Ví dụ:
```text
20240101 123 BKHDT _CV BSKT du an khu do thi moi
20251215 45 UBND Nha Be _QD Thu hoi dat tai khu vuc phuong Phu Xuan
20240820 67 SXD HCM _TTr Chap thuan dau tu du an can ho thuong mai
```

## Output Format

### 1. Kết quả đặt tên file
```md
📄 KẾT QUẢ ĐẶT TÊN FILE

Thông tin trích xuất:
  • Dự thảo     : [True/False]
  • Ngày        : [DD/MM/YYYY hoặc (trống)]
  • Số hiệu     : [số hiệu hoặc (trống)]
  • Cơ quan     : [tên cơ quan gốc] → [viết tắt]
  • Loại VB     : [loại văn bản] → [viết tắt]
  • Trích yếu   : [trích yếu gốc]

Nhóm áp dụng  : [Nhóm 1 – Legislative / Nhóm 2 – Draft / Nhóm 3 – Standard]

✅ Tên file chuẩn:
[TÊN FILE CUỐI CÙNG]
```

Nếu có điều gì không rõ ràng hoặc thiếu thông tin, nêu rõ phần bị thiếu và đề xuất tên file tạm thời, đồng thời hỏi người dùng để xác nhận.

### 2. Báo cáo document ops
Dùng `references/document-ops-report-template.md` từ `re-legal-deliverable-templates` nếu cần chốt output canonical.

Fallback inline format:
```md
## Kết quả xử lý hồ sơ
| STT | Tên file | Hành động | Thư mục đích / Ghi chú |
|---|---|---|---|
```

## Phần B — Document operations mức cơ bản

### Bước 1 — Chốt phạm vi thao tác
Làm rõ:
- chỉ rename;
- inventory;
- classify;
- move;
- hay tổ hợp các việc trên.

Nếu có thao tác move / xóa / ghi đè trên dữ liệu thật, phải xin xác nhận trước khi chạy.

### Bước 2 — Lấy inventory trước khi move
- Phải có danh sách file nguồn trước khi di chuyển.
- Danh sách này là baseline để làm báo cáo cuối.
- Ưu tiên dùng Codex file tools hoặc terminal có kiểm soát.

### Bước 3 — Thực hiện rename / classify / move
- Chỉ chạy sau khi đã có inventory.
- Nếu có nhiều thư mục đích, phải map rõ từng nhóm tài liệu.
- Nếu phát hiện cấu trúc tài liệu quá lớn hoặc yêu cầu routing nhiều bên, dừng và route `RE-HQ`.

### Bước 4 — Báo cáo
Xuất báo cáo ít nhất gồm:
- STT;
- tên file;
- hành động;
- thư mục đích hoặc trạng thái sau xử lý.

### Bước 5 — So chất lượng tối thiểu
Trước khi chốt, dùng `re-legal-verification-rules` theo logic phù hợp để kiểm tra:
- đã mô tả đúng phạm vi xử lý chưa;
- đã nêu rõ phần nào chỉ là document ops support step chưa;
- có dấu hiệu nào cho thấy task thực chất phải route `RE-HQ` không.

## Xử lý trường hợp đặc biệt

- **Nhiều văn bản cùng lúc**: liệt kê từng văn bản theo thứ tự, mỗi văn bản một khối output riêng.
- **Chỉ có tiêu đề, không có nội dung đầy đủ**: trích xuất hết những gì có, đánh dấu `(?)` cho phần không chắc chắn.
- **Văn bản địa phương không có trong từ điển**: giữ nguyên tên đầy đủ và bỏ dấu.
- **Số hiệu phức tạp**: chỉ lấy phần số đứng trước dấu `/` hoặc `-` đầu tiên.

## Escalation Rule

Phải route `RE-HQ` khi:
- tài liệu trải trên nhiều workstream hoặc nhiều team;
- cần data room coordination thực thụ;
- cần request / response tracking với counterparties;
- document ops không còn là support step mà đã thành chương trình điều phối.

## Reference

- `references/dictionaries.md`

## Common Pitfalls

1. Move file trước khi có inventory.
2. Đổi tên hàng loạt trên dữ liệu thật mà chưa xác nhận.
3. Trộn logic rename theo source mới với assumptions cũ mà không bám `references/dictionaries.md` hiện hành.
4. Biến task document ops nhẹ thành data room coordination nhưng không route `RE-HQ`.
5. Gộp lẫn document ops với legal analysis trong cùng một bước.

## Verification Checklist

- [ ] Đã bám bản source mới nhất cho logic rename
- [ ] Đã tra `references/dictionaries.md` trước khi chốt viết tắt
- [ ] Đã chốt rõ phạm vi: rename / inventory / classify / move
- [ ] Đã có inventory trước khi move
- [ ] Đã xin xác nhận nếu thao tác có rủi ro trên dữ liệu thật
- [ ] Đã xuất báo cáo sau xử lý
- [ ] Đã kiểm tra xem task có vượt scope `RE-Legal` và phải route `RE-HQ` hay không
