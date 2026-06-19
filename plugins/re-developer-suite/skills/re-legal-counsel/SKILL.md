---
name: re-legal-counsel
description: Use for contract and transaction legal work in RE-Legal — contract review, clause risk, negotiation positions, drafting support, dispute notes, transaction legal due-diligence on a document set (data room / contract portfolio, with materiality and severity), batch clause review grids, material-contract schedules, and drafting corporate approval instruments (board/shareholder resolutions and minutes) for Vietnamese real-estate and M&A.
version: 2.0.0
license: MIT
---

# Legal Counsel

## Tổng quan

Skill này là specialist procedure skill của `RE-Legal` cho **hợp đồng, giao dịch và dispute-oriented advisory**.

Dùng skill này khi trọng tâm công việc là:
- review hợp đồng từ góc nhìn một bên;
- nhận diện clause risk, drafting defects và negotiation points;
- soạn hoặc tái cấu trúc tài liệu giao dịch;
- viết dispute note, breach note hoặc strategic legal memo;
- phân tích legal implications của các điều khoản trong tài liệu giao dịch bất động sản và M&A.

Skill này phục vụ **specialist legal execution**. Nếu task chuyển thành điều phối deal nhiều stream, structuring nhiều bộ phận, hoặc DD coordination tổng thể, phải route sang `RE-Investment-Finance` (deal lifecycle owner); chỉ tổng hợp đa phòng cấp executive mới thuộc `RE-HQ`.

## Khi nào dùng

Dùng skill này khi:
- rà soát NDA, LOI, Term Sheet, SPA, SHA, JVA, hợp đồng chuyển nhượng dự án, hợp đồng thuê đất, hợp đồng mua bán nhà ở;
- cần clause-by-clause issue list hoặc review memo;
- cần negotiation position, fallback points hoặc walk-away points;
- cần drafting support hoặc redline strategy;
- cần dispute advisory note, notice of breach note, claim framing hoặc remedial options;
- cần giải thích legal effect của một điều khoản cho business / management / legal team.

Không dùng cho:
- approval path hoặc permit analysis;
- legal status review thuần dự án;
- DD coordination nhiều workstream;
- overall deal structuring / transaction architecture nhiều phòng ban;
- document renaming / inventory / move file.

## Skill đi kèm

- Dùng cùng `re-legal-operations` khi đầu bài mới vào chưa rõ lane, hoặc cần chọn nhanh format như contract review memo, clause issue list, legal question list hoặc recommendation memo.
- Dùng cùng `re-legal-verification-rules` ở cuối để kiểm tra quote support, mức ưu tiên, fallback và ranh giới scope.
- Dùng cùng `re-legal-writing` khi đầu ra là memo, report, notice, recommendation hoặc tài liệu tiếng Việt cần polish.
- Dùng cùng `re-legal-licensing` khi issue hợp đồng phụ thuộc điều kiện pháp lý dự án, tình trạng dự án, permits, chuyển nhượng dự án hoặc regulatory feasibility.

## Chế độ chính

### 1. Review Hợp đồng từ góc nhìn một bên
Áp dụng khi user đưa draft cần review theo vai Buyer / Seller / Investor / JV partner / Landlord / Tenant / Developer.

### 2. Drafting & Transaction Advisory
Áp dụng khi cần soạn mới, dựng khung điều khoản, viết fallback language hoặc chuẩn bị note cho đàm phán.

### 3. Dispute & Breach Advisory
Áp dụng khi cần đánh giá vi phạm, chiến lược xử lý, bằng chứng, thời hiệu, options đàm phán / trọng tài / tòa án.

### 4. Transaction Legal DD (rà soát bộ tài liệu giao dịch)
Áp dụng khi cần trích issue pháp lý từ **một bộ tài liệu** (data room, danh mục hợp đồng của target) cho M&A / chuyển nhượng dự án — theo nhóm vấn đề + materiality + severity, hoặc rà hàng loạt hợp đồng cùng loại bằng lưới (tabular review). Đây là **legal stream chuyên sâu** mà `re-inv-dd-coordinator` kéo về; `re-legal-counsel` phát hành findings, không ôm điều phối DD. Phương pháp: `references/transaction-dd-playbook.md` + `references/transaction-clause-checklists.md`.

### 5. Soạn văn kiện phê duyệt nội bộ
Áp dụng khi cần soạn nghị quyết/biên bản HĐQT, ĐHĐCĐ, HĐTV hoặc quyết định chủ sở hữu để **ủy quyền/chấp thuận giao dịch** (M&A, chuyển nhượng dự án, change-of-control, giao dịch lớn / với người có liên quan) theo Luật Doanh nghiệp 2020. Phương pháp + cổng chặn: `references/corporate-approvals-vn.md`.

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

### 6. Ngôn ngữ đầu ra theo bối cảnh hợp đồng
Ngôn ngữ làm việc là tiếng Việt, nhưng **deliverable theo ngôn ngữ của hợp đồng gốc / yêu cầu của Sếp** (xem `../../references/operating-contract.md` — Output language): hợp đồng/SPA bản tiếng Anh → review memo/redline tiếng Anh; hợp đồng VN → tiếng Việt; song ngữ khi một bên là tổ chức/cá nhân VN. Khi review hợp đồng song ngữ, nêu rõ **controlling language** (bản tiếng Việt thường được ưu tiên tại tòa Việt Nam).

## Quy trình

### Bước 1 — Xác định mục tiêu review hoặc drafting
Chốt rõ user muốn gì:
- issue list;
- review memo;
- redline strategy;
- negotiation note;
- draft từ đầu;
- dispute advisory.

Nếu cần format rõ ngay từ đầu, dùng bản đồ template trong `re-legal-operations` để chọn template phù hợp trước khi đi sâu vào analysis.

### Bước 2 — Xác định bối cảnh giao dịch
Tối thiểu làm rõ:
- client-side là ai;
- đối tác là ai;
- loại tài liệu là gì;
- giai đoạn đàm phán;
- pháp luật điều chỉnh nếu đã biết;
- audience của output là management, legal team hay cả hai.

Khi điều khoản dẫn chiếu hoặc phụ thuộc một văn bản luật cụ thể (governing law, điều kiện luật định, statutory remedy), **kiểm chứng văn bản đó qua MCP `tvpl`** theo `../../references/tvpl-lookup-protocol.md` (`check_hieu_luc` + `get_dieu`) trước khi kết luận về legal effect.

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

Với các điều khoản giao dịch trọng yếu (change-of-control, assignment, MAC, độc quyền/MFN, indemnity, termination, CP, successor liability), rà theo bộ dấu hiệu trong `references/transaction-clause-checklists.md`. Khi phải so **nhiều hợp đồng cùng loại**, dùng tabular review (lưới + ô trích nguyên văn ≤125 ký tự + 3 trạng thái not-found) theo `references/transaction-dd-playbook.md`, xuất bằng `../../templates/clause-review-grid.md`.

### Bước 6 — Đề xuất hướng sửa và fallback
Với từng issue quan trọng, nên trả lời đủ:
- điều khoản nào;
- vấn đề là gì;
- rủi ro cho client-side;
- hướng sửa hoặc ngôn ngữ thay thế;
- fallback nếu đối tác không chấp nhận;
- mức ưu tiên.

### Bước 7 — Kiểm tra xem có cần kéo `re-legal-licensing` không
Phải kéo `re-legal-licensing` nếu điều khoản phụ thuộc các vấn đề như:
- điều kiện chuyển nhượng dự án;
- tình trạng pháp lý đất / dự án;
- permit status;
- approval risk;
- điều kiện mở bán / huy động vốn;
- regulatory feasibility của cấu trúc chuyển nhượng.

### Bước 8 — Đóng gói output và so chất lượng
- Nếu output là memo / recommendation / breach note tiếng Việt, mặc định gọi `re-legal-writing` để polish ngôn ngữ và tăng độ counsel-ready.
- Trước khi chốt, so lại bằng `re-legal-verification-rules` để kiểm tra clause support, fallback quality, missing facts và ranh giới scope.

## Quy trình Mode 4 — Transaction Legal DD

Theo `references/transaction-dd-playbook.md`: (1) kiểm kê data room + map nhóm vấn đề, ghi gaps; (2) lọc theo materiality (ngưỡng lấy từ handoff/dossier, không tự bịa); (3) trích issue theo bộ rà chuẩn + Quote-First, nhiều tài liệu cùng loại dùng tabular review; (4) phát biểu finding theo format bắt buộc, kiểm chứng luật qua `tvpl`; (5) tổng hợp theo nhóm + bottom-line + gaps. Project-legal (đất/quy hoạch/permit) → kéo `re-legal-licensing`; điều phối DD đa stream → `re-inv-dd-coordinator`; CP/closing → `cp-closing-issue-note-template`. Đóng gói: `../../templates/transaction-dd-findings-memo.md`; schedule HĐ trọng yếu: `../../templates/material-contract-schedule.md`.

## Quy trình Mode 5 — Văn kiện phê duyệt nội bộ

Theo `references/corporate-approvals-vn.md`: xác định loại hình DN → cơ quan quyết định & loại văn kiện; **đọc điều lệ trước**; xác định thẩm quyền + tỷ lệ thông qua (kiểm chứng `tvpl`); cờ xung đột lợi ích (loại bên liên quan khỏi biểu quyết); cổng major one-off (M&A/huy động vốn/giải thể ký gấp → rà luật sư phụ trách). Output: `../../templates/corporate-resolution-vn.md`, đánh dấu DRAFT để rà soát.

## Dạng đầu ra

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

### 4. DD Findings Memo (bộ tài liệu giao dịch)
Theo `../../templates/transaction-dd-findings-memo.md`: coverage data room → bottom-line (đếm theo mức 🔴🟠🟡🟢) → findings theo nhóm (mỗi finding có Trích dẫn + Kiểm chứng luật + Khuyến nghị + Owner) → gaps → next-step. Là **legal input** cho `re-inv-dd-coordinator`, không phải DD report tổng.

### 5. Văn kiện phê duyệt nội bộ
Theo `../../templates/corporate-resolution-vn.md` (nghị quyết/biên bản/quyết định) — luôn ở trạng thái DRAFT để rà soát; nêu rõ thẩm quyền, tỷ lệ thông qua, xử lý xung đột lợi ích.

## Khi nào phải route ra ngoài `RE-Legal`

Phải coi task đã vượt scope `RE-Legal` khi:
- không còn là contract review thuần mà thành overall deal coordination;
- cần điều phối DD nhiều stream để support drafting / signing / closing;
- cần kéo nhiều bộ phận cùng ra decision về structure, approvals, finance, tax hoặc execution timeline;
- legal chỉ là một module trong chương trình điều phối lớn hơn.

Trong case đó, `RE-Legal` vẫn làm contract memo / legal note, nhưng **coordination deal lifecycle (DD, structuring, closing) thuộc `RE-Investment-Finance`**; chỉ tổng hợp đa phòng cấp executive mới thuộc `RE-HQ`.

## Quy tắc ngôn ngữ

- Tên skill giữ bằng tiếng Anh.
- Nội dung, workflow và output guidance viết bằng tiếng Việt.
- Chỉ dùng tiếng Anh khi không có từ Việt tương đương tự nhiên hoặc cần giữ thuật ngữ chuẩn giao dịch.
- Với thuật ngữ quan trọng, ưu tiên cách viết **Việt ngữ (Anh ngữ)** nếu giúp giữ đúng nghĩa.

## References

Dùng khi cần đào sâu guide theo loại tài liệu:
- `references/re-legal-counsel-entry-points.md`
- `references/ma-document-guides.md`
- `references/transaction-document-family-map.md`
- `references/cp-closing-and-structuring-support.md`
- `references/negotiation-and-dispute-playbook.md` — tier issue, đàm phán 3 vòng, khung & bảng so sánh phương án tranh chấp, thời hiệu, trọng tài
- `references/transaction-dd-playbook.md` — rà bộ tài liệu giao dịch: nhóm vấn đề, materiality, severity, finding format, tabular review (Mode 4)
- `references/transaction-clause-checklists.md` — bộ dấu hiệu change-of-control / assignment / MAC / MFN / indemnity / termination / CP / successor liability
- `references/corporate-approvals-vn.md` — soạn nghị quyết/biên bản phê duyệt giao dịch theo Luật Doanh nghiệp 2020 (Mode 5)

Đặc biệt trong operating model hiện tại, `references/re-legal-counsel-entry-points.md` cũng là map cho các hybrid requests từ `RE-HQ` như:
- DD legal findings — corporate / transaction stream;
- CP / closing mechanics support;
- structuring-driven legal input;
- missing-docs / clarification package cho legal stream.

Ngoài ra, dùng thêm:
- `transaction-document-family-map.md` để chọn sub-mode theo family của tài liệu;
- `cp-closing-and-structuring-support.md` khi issue xoay quanh CP, closing hoặc structuring-driven legal input.

## Lỗi thường gặp

1. Review hợp đồng mà chưa xác định client-side.
2. Kết luận “không có điều khoản X” mà không search kỹ.
3. Trộn legal risk với negotiating preference.
4. Chỉ nói điều khoản bất lợi nhưng không đề xuất fallback.
5. Bỏ qua ảnh hưởng của pháp lý dự án lên điều khoản giao dịch.
6. Ôm luôn phần structuring / DD coordination thay vì route `RE-Investment-Finance`.

## Checklist kiểm tra

- [ ] Đã xác định client-side và mục tiêu output
- [ ] Đã áp dụng Quote-First Protocol cho các issue trọng yếu
- [ ] Đã phân loại mức ưu tiên của issue
- [ ] Đã đưa fallback hoặc hướng sửa cho các điểm quan trọng
- [ ] Đã kiểm tra xem issue có phụ thuộc pháp lý dự án hay không
- [ ] Văn bản luật dẫn chiếu đã được kiểm chứng qua `tvpl` (hoặc nêu rõ chưa kiểm chứng được)
- [ ] Đã cân nhắc gọi `re-legal-licensing` nếu có project/regulatory dependency
- [ ] Đã route `RE-HQ` nếu task đã chuyển thành coordination đa stream
- [ ] Đã gọi `re-legal-writing` nếu output cuối là memo / notice / recommendation tiếng Việt quan trọng
