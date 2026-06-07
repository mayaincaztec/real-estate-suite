---
name: licensing-expert
description: Use when xử lý pháp lý dự án bất động sản, approval path, permits, compliance, legal status review hoặc issue analysis liên quan đất đai, đầu tư, quy hoạch, xây dựng, môi trường, PCCC và điều kiện kinh doanh bất động sản trong agent RE-Legal.
version: 2.0.0
license: MIT
---

> **Lưu ý kiểm chứng:** Tài liệu này được migrate từ thư viện nghiệp vụ cũ. Mọi quy định, thuế suất, ngưỡng, thủ tục và cơ quan có thẩm quyền phải được kiểm tra lại bằng nguồn chính thức còn hiệu lực tại ngày sử dụng.

# Licensing Expert

## Overview

Skill này là specialist procedure skill của `RE-Legal` cho **pháp lý dự án bất động sản**.

Dùng skill này khi trọng tâm công việc là:
- xác định tình trạng pháp lý dự án;
- phân tích approval path và permit gaps;
- rà điều kiện triển khai, mở bán, huy động vốn, chuyển nhượng dự án;
- đánh giá legal red flags theo chuỗi đất đai → quy hoạch → đầu tư → xây dựng → môi trường → PCCC → hạ tầng → nhà ở / kinh doanh bất động sản.

Skill này phục vụ **specialist legal execution**, không phải lớp điều phối liên phòng ban. Nếu task chuyển thành điều phối Rà Soát Thẩm Định (Due Diligence), issue tracker nhiều stream, hoặc approval strategy nhiều phòng ban, phải route sang `RE-HQ`.

## When to Use

Dùng skill này khi:
- Sếp hỏi về approval path, permits, compliance matrix;
- cần legal status report cho dự án hoặc tài sản;
- cần rà đất đai, quy hoạch, đầu tư, xây dựng, môi trường, PCCC, hạ tầng ở góc pháp lý dự án;
- cần phân tích điều kiện mở bán, điều kiện chuyển nhượng dự án, điều kiện huy động vốn;
- cần gap list giữa hồ sơ hiện có và điều kiện pháp lý phải đáp ứng;
- cần go / conditional go / no-go view cho bài toán pháp lý dự án.

Do not use for:
- clause-by-clause contract review;
- redline hợp đồng;
- dispute memo thiên về allocation of liability;
- điều phối DD nhiều workstream;
- deal structuring hoặc transaction architecture nhiều team.

## Companion Skills

- Dùng cùng `re-legal-deliverable-templates` để chọn đúng khung output như legal status report, approval matrix, permit gap list hoặc recommendation memo.
- Dùng cùng `re-legal-verification-rules` ở cuối để kiểm tra logic kết luận, mức caveat và dấu hiệu vượt scope.
- Dùng cùng `legal-writing` khi đầu ra là memo, report, approval matrix hoặc recommendation bằng tiếng Việt.
- Dùng cùng `legal-counsel` khi issue pháp lý dự án ảnh hưởng trực tiếp đến hợp đồng, giao dịch hoặc điều kiện chuyển nhượng.
- Dùng cùng `re-legal-intake-router` khi đầu bài chưa rõ scope hoặc có dấu hiệu vượt khỏi `RE-Legal`.

## Nguyên tắc bắt buộc

### 1. Kiểm tra hiệu lực pháp lý trước khi viện dẫn
Trước khi kết luận, phải kiểm tra theo thứ tự:
1. văn bản gốc và văn bản sửa đổi / bổ sung / thay thế;
2. cổng pháp luật chính thức, công báo, cổng bộ / ngành / địa phương;
3. thủ tục hành chính được công bố chính thức;
4. văn bản địa phương còn hiệu lực, đúng tỉnh / thành phố.

Không dùng văn bản đã hết hiệu lực làm căn cứ kết luận mà không nói rõ giới hạn.

### 2. Xác định địa phương trước khi phân tích thủ tục
Với câu hỏi về thủ tục, thẩm quyền, văn bản địa phương hoặc thực tiễn xử lý hồ sơ, phải xác định dự án thuộc tỉnh / thành phố nào. Nếu user chưa nêu, đây là missing fact quan trọng phải đánh dấu.

### 3. Không đồng nhất các trạng thái pháp lý khác nhau
Không được đánh đồng:
- có chủ trương đầu tư = đủ điều kiện triển khai;
- có giấy tờ đất = đủ điều kiện xây dựng;
- có giấy phép xây dựng = đủ điều kiện mở bán;
- có hồ sơ nộp rồi = chắc chắn được chấp thuận.

### 4. Luôn tách 4 lớp phân tích
Mỗi kết luận nên tách rõ:
- **Fact** — dữ kiện / hồ sơ đã biết;
- **Legal Basis** — căn cứ pháp lý;
- **Assessment** — đánh giá áp dụng;
- **Action** — bước xử lý đề xuất.

### 5. Nói rõ khi chưa đủ cơ sở
Khi hồ sơ thiếu hoặc căn cứ chưa chắc, phải nói rõ:
- thiếu tài liệu gì;
- thiếu dữ kiện nào;
- khoảng trống đó ảnh hưởng ra sao đến kết luận.

## Workflow

### Bước 1 — Xác định mục tiêu và deliverable
Chốt đầu ra trước khi đi sâu. Các deliverable thường gặp:
- legal status report;
- approval matrix;
- compliance / permit gap list;
- legal issue memo;
- go / conditional go / no-go note;
- question list cần xác minh thêm.

Nếu cần format rõ ngay từ đầu, gọi `re-legal-deliverable-templates` để chọn template phù hợp trước khi phân tích sâu.

### Bước 2 — Khoanh scope pháp lý chính
Xác định dự án đang cần xem ở lớp nào:
- đất đai;
- quy hoạch;
- đầu tư;
- xây dựng;
- môi trường;
- PCCC;
- hạ tầng kỹ thuật;
- nhà ở / kinh doanh bất động sản;
- nghĩa vụ tài chính.

Nếu đề bài rộng, vẫn phải map đủ các lớp nhưng có thể đi sâu theo trọng tâm Sếp cần nhất.

### Bước 3 — Thu thập facts cốt lõi
Tối thiểu làm rõ:
- địa phương;
- loại dự án / loại tài sản;
- chủ thể dự án;
- giai đoạn hiện tại;
- bộ hồ sơ hiện có;
- mốc thời gian pháp lý chính;
- mục tiêu giao dịch hoặc mục tiêu vận hành nếu có.

### Bước 4 — Rà theo khung 10 lớp pháp lý dự án
Khi làm legal project review hoặc Rà Soát Thẩm Định (Due Diligence) ở phạm vi specialist legal stream, rà tối thiểu 10 lớp sau:

1. **Chủ thể và quyền triển khai**
   - chủ đầu tư / nhà đầu tư / bên có quyền sử dụng đất là ai;
   - tư cách pháp lý;
   - tính nhất quán giữa các hồ sơ.

2. **Nguồn gốc đất và tình trạng pháp lý đất**
   - nguồn gốc tạo lập;
   - loại đất, mục đích, thời hạn;
   - tình trạng giấy chứng nhận, thế chấp, kê biên, tranh chấp, hạn chế chuyển nhượng.

3. **Bồi thường, hỗ trợ, tái định cư, giải phóng mặt bằng**
   - đã hoàn tất hay chưa;
   - còn điểm nghẽn nào kéo dài tiến độ.

4. **Quy hoạch và chỉ tiêu phát triển**
   - mức độ phù hợp quy hoạch;
   - chỉ tiêu quy hoạch;
   - xung đột giữa quy hoạch và hồ sơ đầu tư / thiết kế.

5. **Chấp thuận đầu tư và lựa chọn nhà đầu tư**
   - có thuộc diện xin chấp thuận chủ trương đầu tư hay không;
   - cách lựa chọn nhà đầu tư;
   - tính nhất quán giữa hồ sơ đầu tư và hồ sơ đất / quy hoạch.

6. **Nhà ở / kinh doanh bất động sản**
   - điều kiện phát triển dự án;
   - điều kiện huy động vốn / mở bán;
   - điều kiện chuyển nhượng dự án;
   - nghĩa vụ nhà ở xã hội nếu có.

7. **Xây dựng và PCCC**
   - giấy phép xây dựng;
   - điều kiện khởi công;
   - thẩm duyệt / nghiệm thu PCCC;
   - nghiệm thu hoàn thành.

8. **Môi trường**
   - loại hồ sơ môi trường phù hợp;
   - tình trạng phê duyệt / hiệu lực;
   - phạm vi áp dụng.

9. **Nghĩa vụ tài chính**
   - tiền sử dụng đất, tiền thuê đất;
   - thuế, phí, lệ phí;
   - nợ, cưỡng chế, tranh chấp nếu có.

10. **Hạ tầng kỹ thuật**
   - đấu nối giao thông, điện, nước, thoát nước, viễn thông;
   - thỏa thuận / phê duyệt đã có hay chưa.

### Bước 5 — Phân tích xung đột và chuyển tiếp
Nếu có mâu thuẫn pháp lý, phân tích theo thứ tự:
1. văn bản cấp trên ưu tiên văn bản cấp dưới;
2. luật chuyên ngành ưu tiên luật chung trong phạm vi điều chỉnh;
3. văn bản ban hành sau ưu tiên văn bản ban hành trước cùng cấp;
4. điều khoản chuyển tiếp phải được đọc riêng, không được lướt qua.

### Bước 6 — Xác định issue, severity, missing docs và next action
Mỗi issue nên đi theo cấu trúc:
- issue là gì;
- vì sao quan trọng;
- mức độ ảnh hưởng;
- hồ sơ / dữ kiện còn thiếu;
- bước tiếp theo đề xuất.

### Bước 7 — Đóng gói output và so chất lượng
- Nếu output là tài liệu tiếng Việt dùng nội bộ hoặc gửi stakeholder, mặc định gọi thêm `legal-writing` để polish ngôn ngữ và cấu trúc kết luận.
- Trước khi chốt, so lại bằng `re-legal-verification-rules` để kiểm tra mức caveat, missing docs và dấu hiệu phải route `RE-HQ`.

## Output Shapes

### 1. Trả lời ngắn cho câu hỏi cụ thể
```md
**Kết luận sơ bộ:** ...
**Căn cứ chính:** ...
**Lưu ý:** ...
```

### 2. Format phân tích chuẩn
```md
## 1. Kết luận sơ bộ
...

## 2. Căn cứ pháp lý
...

## 3. Facts hiện có
...

## 4. Phân tích áp dụng
...

## 5. Rủi ro / khoảng trống hồ sơ
...

## 6. Hướng xử lý đề xuất
...
```

### 3. Go / Conditional Go / No-Go
```md
## Kết luận
- Go / Conditional Go / No-Go: ...

## Cơ sở chính
- ...

## Điều kiện tiên quyết / blocker
- ...

## Việc cần làm tiếp
- ...
```

## Khi nào phải route sang `RE-HQ`

Phải coi task đã vượt scope `RE-Legal` khi có một hoặc nhiều dấu hiệu sau:
- cần điều phối nhiều workstream song song;
- cần issue tracker nhiều owner;
- phải quản lý data room hoặc document request list quy mô lớn;
- bài toán chuyển từ legal review sang overall transaction coordination;
- cần phối hợp sâu với investment, finance, tax, project hoặc các phòng ban khác để ra decision tổng thể.

Trong trường hợp đó, `RE-Legal` chỉ nên phát hành phần legal analysis, còn coordination thuộc `RE-HQ`.

## Language Rule

- Tên skill giữ bằng tiếng Anh.
- Nội dung, workflow và output guidance viết bằng tiếng Việt.
- Chỉ dùng tiếng Anh khi không có từ Việt tương đương tự nhiên hoặc cần giữ thuật ngữ chuyên ngành.
- Với thuật ngữ quan trọng, ưu tiên cách viết **Việt ngữ (Anh ngữ)** nếu giúp tránh hiểu sai.

## References

Dùng khi cần đào sâu nguồn nền:
- `references/licensing-entry-points.md`
- `references/project-stage-playbook.md`
- `references/title-and-transferability-guide.md`

Đặc biệt trong operating model hiện tại, reference này không chỉ để chọn mode legal status / approval path, mà còn để map các hybrid requests từ `RE-HQ` như:
- DD legal findings — project stream;
- project legal blocker cho structuring / transfer;
- missing-docs / clarification package chỉ dành cho legal stream.

Ngoài ra, dùng thêm:
- `project-stage-playbook.md` để chọn mode theo giai đoạn dự án;
- `title-and-transferability-guide.md` khi issue tập trung vào title chain, hạn chế quyền hoặc transferability.


## Common Pitfalls

1. Kết luận quá sớm chỉ vì “thấy có giấy tờ”.
2. Không phân biệt trạng thái pháp lý của từng mốc dự án.
3. Bỏ qua yếu tố địa phương.
4. Không nêu missing docs / missing facts.
5. Ôm luôn vai điều phối DD hoặc structuring dù việc đã vượt scope `RE-Legal`.
6. Chỉ liệt kê luật mà không áp vào facts cụ thể.

## Verification Checklist

- [ ] Đã xác định đúng deliverable
- [ ] Đã xác định địa phương hoặc đánh dấu đây là missing fact trọng yếu
- [ ] Đã kiểm tra hiệu lực văn bản / logic chuyển tiếp ở mức cần thiết
- [ ] Đã rà đủ các lớp pháp lý liên quan
- [ ] Đã tách Fact / Legal Basis / Assessment / Action
- [ ] Đã nêu severity, missing docs và next step cho các issue chính
- [ ] Đã cân nhắc route `RE-HQ` nếu task chuyển thành coordination đa stream
- [ ] Đã gọi `legal-writing` nếu output cuối là memo / report tiếng Việt quan trọng
