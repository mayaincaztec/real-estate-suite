---
name: legal-counsel
description: Use when rà soát hợp đồng, clause risk, negotiation position, drafting support, dispute note hoặc transaction legal memo trong agent RE-Legal.
version: 2.0.0
license: MIT
---

# Legal Counsel

## Overview

Skill này là specialist procedure skill của `RE-Legal` cho **hợp đồng, giao dịch và dispute-oriented advisory**.

Dùng skill này khi trọng tâm công việc là:
- review hợp đồng từ góc nhìn một bên;
- nhận diện clause risk, drafting defects và negotiation points;
- soạn hoặc tái cấu trúc tài liệu giao dịch;
- viết dispute note, breach note hoặc strategic legal memo;
- phân tích legal implications của các điều khoản trong tài liệu giao dịch bất động sản và M&A.

Skill này phục vụ **specialist legal execution**. Nếu task chuyển thành điều phối deal nhiều stream, structuring nhiều bộ phận, hoặc DD coordination tổng thể, phải route sang `RE-HQ`.

## When to Use

Dùng skill này khi:
- rà soát NDA, LOI, Term Sheet, SPA, SHA, JVA, hợp đồng chuyển nhượng dự án, hợp đồng thuê đất, hợp đồng mua bán nhà ở;
- cần clause-by-clause issue list hoặc review memo;
- cần negotiation position, fallback points hoặc walk-away points;
- cần drafting support hoặc redline strategy;
- cần dispute advisory note, notice of breach note, claim framing hoặc remedial options;
- cần giải thích legal effect của một điều khoản cho business / management / legal team.

Do not use for:
- approval path hoặc permit analysis;
- legal status review thuần dự án;
- DD coordination nhiều workstream;
- overall deal structuring / transaction architecture nhiều phòng ban;
- document renaming / inventory / move file.

## Companion Skills

- Dùng cùng `re-legal-deliverable-templates` để chọn nhanh format như contract review memo, clause issue list, legal question list hoặc recommendation memo.
- Dùng cùng `re-legal-verification-rules` ở cuối để kiểm tra quote support, mức ưu tiên, fallback và ranh giới scope.
- Dùng cùng `legal-writing` khi đầu ra là memo, report, notice, recommendation hoặc tài liệu tiếng Việt cần polish.
- Dùng cùng `licensing-expert` khi issue hợp đồng phụ thuộc điều kiện pháp lý dự án, tình trạng dự án, permits, chuyển nhượng dự án hoặc regulatory feasibility.
- Dùng cùng `re-legal-intake-router` khi đầu bài mới vào chưa rõ là contract-only hay mixed legal/project issue.

## Core Modes

### 1. Review Hợp đồng từ góc nhìn một bên
Áp dụng khi user đưa draft cần review theo vai Buyer / Seller / Investor / JV partner / Landlord / Tenant / Developer.

### 2. Drafting & Transaction Advisory
Áp dụng khi cần soạn mới, dựng khung điều khoản, viết fallback language hoặc chuẩn bị note cho đàm phán.

### 3. Dispute & Breach Advisory
Áp dụng khi cần đánh giá vi phạm, chiến lược xử lý, bằng chứng, thời hiệu, options đàm phán / trọng tài / tòa án.

## Nguyên tắc bắt buộc

### 1. Quote-First Protocol
Với mọi document review:
- **claim dương tính**: phải trích nguyên văn điều khoản hoặc nêu chính xác section / clause đang phân tích;
- **claim âm tính**: nếu kết luận “không có điều khoản X”, phải kiểm tra bằng nhiều biến thể tìm kiếm trước khi chốt;
- không được paraphrase mơ hồ rồi kết luận mạnh.

### 2. Xác định client-side trước khi đánh giá
Cùng một điều khoản có thể tốt cho Buyer nhưng bất lợi cho Seller. Trước khi review, phải xác định hoặc suy luận hợp lý:
- ai là client-side;
- ai soạn draft;
- mục tiêu thương mại / pháp lý của client;
- audience của output.

### 3. Phân biệt legal risk và negotiation posture
Không phải mọi điểm lệch khỏi thông lệ đều là deal-breaker. Nên tách:
- **must-win**;
- **negotiate**;
- **acceptable / concede**.

### 4. Không tách rời facts giao dịch khỏi điều khoản
Điều khoản chỉ được đánh giá đúng khi đặt vào bối cảnh:
- loại giao dịch;
- tài sản / target;
- giá trị / timeline;
- điều kiện tiên quyết;
- các ràng buộc pháp lý nền.

### 5. Nói rõ giới hạn khi thiếu tài liệu
Nếu chưa có phụ lục, định nghĩa, schedule, side letter hoặc tài liệu liên quan, phải ghi rõ đó là giới hạn của kết luận.

## Workflow

### Bước 1 — Xác định mục tiêu review hoặc drafting
Chốt rõ user muốn gì:
- issue list;
- review memo;
- redline strategy;
- negotiation note;
- draft từ đầu;
- dispute advisory.

Nếu cần format rõ ngay từ đầu, gọi `re-legal-deliverable-templates` để chọn template phù hợp trước khi đi sâu vào analysis.

### Bước 2 — Xác định bối cảnh giao dịch
Tối thiểu làm rõ:
- client-side là ai;
- đối tác là ai;
- loại tài liệu là gì;
- giai đoạn đàm phán;
- pháp luật điều chỉnh nếu đã biết;
- audience của output là management, legal team hay cả hai.

### Bước 3 — Đọc tài liệu theo Quote-First Protocol
Khi review hợp đồng:
- đọc toàn bộ tài liệu nếu phạm vi cho phép;
- đánh dấu clause theo nhóm vấn đề;
- trích nguyên văn phần quan trọng;
- nếu kết luận thiếu điều khoản, phải search nhiều biến thể trước khi chốt.

### Bước 4 — Phân loại issue theo mức ưu tiên
Dùng tối thiểu 3 mức:
- **Must-Win** — rủi ro trọng yếu, cần sửa hoặc kiểm soát chặt;
- **Negotiate** — nên sửa, có fallback;
- **Accept / Concede** — có thể chấp nhận hoặc dùng để đổi lấy điểm quan trọng hơn.

Nếu cần chi tiết hơn, có thể map thành:
- Critical
- High
- Medium
- Low

### Bước 5 — Nhóm issue theo section family
Với hợp đồng phức tạp, ưu tiên nhóm theo family thay vì liệt kê rời:
- definitions & construction;
- commercial terms / price / payment;
- representations & warranties;
- covenants;
- conditions precedent / conditions to closing;
- termination;
- indemnity / remedies;
- miscellaneous;
- drafting defects xuyên suốt.

### Bước 6 — Đề xuất hướng sửa và fallback
Với từng issue quan trọng, nên trả lời đủ:
- điều khoản nào;
- vấn đề là gì;
- rủi ro cho client-side;
- hướng sửa hoặc ngôn ngữ thay thế;
- fallback nếu đối tác không chấp nhận;
- mức ưu tiên.

### Bước 7 — Kiểm tra xem có cần kéo `licensing-expert` không
Phải kéo `licensing-expert` nếu điều khoản phụ thuộc các vấn đề như:
- điều kiện chuyển nhượng dự án;
- tình trạng pháp lý đất / dự án;
- permit status;
- approval risk;
- điều kiện mở bán / huy động vốn;
- regulatory feasibility của cấu trúc chuyển nhượng.

### Bước 8 — Đóng gói output và so chất lượng
- Nếu output là memo / recommendation / breach note tiếng Việt, mặc định gọi `legal-writing` để polish ngôn ngữ và tăng độ counsel-ready.
- Trước khi chốt, so lại bằng `re-legal-verification-rules` để kiểm tra clause support, fallback quality, missing facts và ranh giới scope.

## Output Shapes

### 1. Clause Review ngắn
```md
- **Điều khoản:** ...
- **Vấn đề:** ...
- **Rủi ro cho [client-side]:** ...
- **Đề xuất:** ...
- **Mức ưu tiên:** Must-Win / Negotiate / Accept
```

### 2. Review Memo
```md
## 1. Kết luận điều hành
...

## 2. Các rủi ro chính
...

## 3. Phân tích theo nhóm điều khoản
...

## 4. Điểm cần đàm phán
...

## 5. Fallback / concession strategy
...

## 6. Việc cần xác minh thêm
...
```

### 3. Dispute / Breach Note
```md
## 1. Tóm tắt sự việc
...

## 2. Cơ sở pháp lý / cơ sở hợp đồng
...

## 3. Đánh giá vị thế các bên
...

## 4. Rủi ro và chứng cứ cần bổ sung
...

## 5. Các phương án xử lý
...

## 6. Khuyến nghị bước tiếp theo
...
```

## Khi nào phải route sang `RE-HQ`

Phải coi task đã vượt scope `RE-Legal` khi:
- không còn là contract review thuần mà thành overall deal coordination;
- cần điều phối DD nhiều stream để support drafting / signing / closing;
- cần kéo nhiều bộ phận cùng ra decision về structure, approvals, finance, tax hoặc execution timeline;
- legal chỉ là một module trong chương trình điều phối lớn hơn.

Trong case đó, `RE-Legal` vẫn có thể làm contract memo hoặc legal note, nhưng coordination thuộc `RE-HQ`.

## Language Rule

- Tên skill giữ bằng tiếng Anh.
- Nội dung, workflow và output guidance viết bằng tiếng Việt.
- Chỉ dùng tiếng Anh khi không có từ Việt tương đương tự nhiên hoặc cần giữ thuật ngữ chuẩn giao dịch.
- Với thuật ngữ quan trọng, ưu tiên cách viết **Việt ngữ (Anh ngữ)** nếu giúp giữ đúng nghĩa.

## References

Dùng khi cần đào sâu guide theo loại tài liệu:
- `references/legal-counsel-entry-points.md`
- `references/ma-document-guides.md`
- `references/transaction-document-family-map.md`
- `references/cp-closing-and-structuring-support.md`

Đặc biệt trong operating model hiện tại, `references/legal-counsel-entry-points.md` cũng là map cho các hybrid requests từ `RE-HQ` như:
- DD legal findings — corporate / transaction stream;
- CP / closing mechanics support;
- structuring-driven legal input;
- missing-docs / clarification package cho legal stream.

Ngoài ra, dùng thêm:
- `transaction-document-family-map.md` để chọn sub-mode theo family của tài liệu;
- `cp-closing-and-structuring-support.md` khi issue xoay quanh CP, closing hoặc structuring-driven legal input.

## Common Pitfalls

1. Review hợp đồng mà chưa xác định client-side.
2. Kết luận “không có điều khoản X” mà không search kỹ.
3. Trộn legal risk với negotiating preference.
4. Chỉ nói điều khoản bất lợi nhưng không đề xuất fallback.
5. Bỏ qua ảnh hưởng của pháp lý dự án lên điều khoản giao dịch.
6. Ôm luôn phần structuring / DD coordination thay vì route `RE-HQ`.

## Verification Checklist

- [ ] Đã xác định client-side và mục tiêu output
- [ ] Đã áp dụng Quote-First Protocol cho các issue trọng yếu
- [ ] Đã phân loại mức ưu tiên của issue
- [ ] Đã đưa fallback hoặc hướng sửa cho các điểm quan trọng
- [ ] Đã kiểm tra xem issue có phụ thuộc pháp lý dự án hay không
- [ ] Đã cân nhắc gọi `licensing-expert` nếu có project/regulatory dependency
- [ ] Đã route `RE-HQ` nếu task đã chuyển thành coordination đa stream
- [ ] Đã gọi `legal-writing` nếu output cuối là memo / notice / recommendation tiếng Việt quan trọng
