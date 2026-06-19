---
name: re-legal-verification-rules
description: Use to quality-control RE-Legal outputs before finalizing — legal status memos, approval paths, permit gap analyses, contract reviews, clause issue lists, recommendation memos, and question lists. Checks over-claiming, missing caveats, tvpl verification, and scope drift.
version: 1.0.0
license: MIT
---

# re-legal Verification Rules

## Tổng quan

Skill này là quality-control layer của `RE-Legal`.

Mục tiêu là buộc agent kiểm tra lại output theo logic phù hợp với từng loại deliverable, thay vì chỉ nhìn xem câu chữ đã ổn hay chưa.

Skill này dùng ở cuối workflow, sau khi specialist analysis đã xong và trước khi chốt deliverable cho Sếp.

## Khi nào dùng

Dùng skill này khi:
- chuẩn bị chốt legal memo, legal report, approval matrix, issue list hoặc recommendation;
- cần xác nhận rằng kết luận đã được nâng đỡ bằng facts, legal basis và phạm vi kết luận phù hợp;
- cần check xem task có đang bị over-claim hay under-qualified không;
- cần rà nhanh chất lượng câu trả lời chat pháp lý ngắn trước khi gửi Sếp.
- rà nhanh tính đồng bộ giữa template layer, specialist skills và verification graph sau khi refactor legal workflow.

Không dùng cho:
- thay thế specialist analysis ban đầu;
- quyết định routing lane từ đầu;
- thay thế việc polish tiếng Việt của `re-legal-writing`.

## Quy tắc chung

### 1. Không kết luận mạnh hơn hồ sơ hiện có
Nếu hồ sơ thiếu, phải nêu rõ giới hạn. Không được biến inference thành fact.

### 2. Mọi output phải làm rõ next step nếu còn việc phải làm
Nếu issue chưa đóng, output phải nói rõ bước tiếp theo hoặc tài liệu cần bổ sung.

### 3. Phân biệt legal judgment với procedural note
Không trộn nhận định pháp lý với hướng xử lý hành chính theo cách làm người đọc tưởng đó là kết luận chắc chắn.

### 4. Kiểm tra routing lần cuối
Nếu đến cuối mới lộ ra task thực chất là coordination đa stream, phải nói rõ phần nào thuộc `RE-Legal`, phần nào đáng ra phải route `RE-HQ`.

### 5. Kiểm chứng hiệu lực văn bản (tvpl)
Nếu output có viện dẫn văn bản pháp luật, phải đã đối chiếu tình trạng hiệu lực qua MCP `tvpl` (xem `../../references/tvpl-lookup-protocol.md`) hoặc gắn caveat **"chưa kiểm chứng hiệu lực"**. Không để output dẫn một văn bản có thể đã bị thay thế mà không có dấu kiểm chứng hoặc caveat. Điều này đặc biệt quan trọng với Legal Status Report, Approval Matrix và Recommendation Memo.

## Quy tắc theo loại deliverable

### A. Legal Status Report
Phải kiểm tra:
- facts cốt lõi đã đủ chưa;
- đã nêu địa phương và giai đoạn dự án chưa;
- đã tách facts / legal basis / assessment / action chưa;
- đã chỉ ra blocker, gap và mức ảnh hưởng chưa.

### B. Approval Matrix
Phải kiểm tra:
- từng hạng mục đã có cơ quan / thẩm quyền chưa;
- điều kiện chính và hồ sơ chính có bị ghi quá chung chung không;
- đã nêu tình trạng hiện tại và gap / blocker cho từng dòng chưa;
- matrix có thể hành động được hay vẫn chỉ là danh sách tên thủ tục.

### C. Permit Gap List
Phải kiểm tra:
- khoảng trống có gắn với điều kiện / giấy phép cụ thể không;
- mức độ ảnh hưởng có được nêu rõ không;
- có bước tiếp theo tương ứng cho từng gap không.

### D. Contract Review Memo
Phải kiểm tra:
- client-side đã được xác định rõ chưa;
- các issue trọng yếu đã có trích dẫn clause / section đủ cụ thể chưa;
- đã phân biệt must-win / negotiate / accept chưa;
- đã có fallback hoặc hướng sửa cho điểm quan trọng chưa;
- issue nào phụ thuộc project legal status đã được flag chưa.

### E. Clause Issue List
Phải kiểm tra:
- từng dòng có đủ clause, issue, risk, proposal, priority chưa;
- tránh lặp cùng một issue ở nhiều dòng mà không nói rõ khác biệt;
- tránh ghi proposal quá chung như “xem xét sửa lại”.

### F. Recommendation Memo
Phải kiểm tra:
- câu hỏi cần quyết định đã được phát biểu rõ chưa;
- khuyến nghị chính có dựa trên căn cứ đủ mạnh không;
- option comparison có công bằng và rõ điều kiện tiên quyết không;
- nếu facts còn thiếu, recommendation đã được qualified đúng mức chưa.

### G. Legal Question List
Phải kiểm tra:
- câu hỏi có đủ cụ thể để counterpart / internal team trả lời không;
- mỗi câu hỏi đã nói rõ vì sao cần và ảnh hưởng nếu chưa có chưa;
- tránh hỏi trùng hoặc hỏi những thứ không ảnh hưởng đến kết luận.

### H. Chat-Native Legal Output
Phải kiểm tra:
- đã có **kết luận ngắn ngay đầu** chưa;
- đã nêu rõ **vì sao** hoặc căn cứ chính chưa, thay vì chỉ chốt một dòng;
- nếu facts thiếu, đã gắn caveat hoặc missing fact chưa;
- nếu còn việc phải làm, đã nêu next step ngắn gọn chưa;
- câu trả lời có đang quá dài như memo hoặc quá cộc như one-liner không;
- nếu task thực chất đã thành coordination / structuring, đã nói rõ ranh giới scope và hướng route `RE-HQ` chưa.

### I. Hybrid Legal Package for `RE-HQ`
Phải kiểm tra:
- output có nói rõ đây là **specialist legal input** chứ không phải coordination report tổng thể không;
- đã nêu rõ **issue / basis / impact / blocker-or-confirm point / next step / owner boundary** chưa;
- đã phân biệt phần việc còn thuộc `RE-Legal` với phần cần `RE-HQ` điều phối chưa;
- legal question list hoặc missing-docs note có bị phình thành tracker nhiều owner không.

### J. Transaction DD Findings Memo (bộ tài liệu giao dịch)
Phải kiểm tra:
- đã nêu **coverage data room + ngưỡng materiality** (nguồn ngưỡng, không tự bịa) và **gaps** chưa;
- mỗi finding đủ: mức độ (🔴🟠🟡🟢) · trích nguyên văn (Quote-First) · kiểm chứng luật qua `tvpl` hoặc caveat · khuyến nghị · owner;
- **không tự lấp khoảng trống** bằng web/model knowledge khi hồ sơ mỏng;
- project-legal (đất/quy hoạch/permit) đã kéo `re-legal-licensing`, không tự kết luận;
- cờ successor liability + CP/closing đã bàn giao đúng (cp-closing-issue-note / `re-inv-dd-coordinator`);
- output là **legal input**, không phình thành DD report tổng (đó là việc của `re-inv-dd-coordinator`).

### K. Clause Review Grid (tabular review)
Phải kiểm tra:
- schema cột đã confirm + chạy mẫu trước khi rà toàn bộ chưa;
- mỗi ô có **trích nguyên văn ≤125 ký tự + vị trí**; ô không lấy được nguồn để `cần_review` + `thiếu_trích_dẫn`;
- đã spot-check ≥3–5 hàng/cột (hoặc 10%) đối chiếu ký tự; lệch → `lệch_trích_dẫn`;
- nhắc rõ mỗi ô là **đầu mối, không phải kết luận**.

### L. Văn kiện phê duyệt nội bộ (corporate resolution)
Phải kiểm tra:
- đúng cơ quan quyết định theo loại hình DN; thẩm quyền + tỷ lệ thông qua đã kiểm chứng qua `tvpl` + điều lệ;
- người có liên quan đã loại khỏi biểu quyết (nếu áp dụng);
- điều kiện tiến hành họp đủ (không tạo văn bản hàm ý cuộc họp hợp lệ khi chưa đủ);
- quyết nghị nêu chính xác hành động/giá trị/đối tác/ủy quyền ký;
- major action đã gắn cờ rà soát luật sư; bản giữ trạng thái **DRAFT**.

## Dấu hiệu chuyển cấp

Phải cân nhắc route ra ngoài `RE-Legal` (deal lifecycle → `RE-Investment-Finance`; tổng hợp đa phòng cấp executive → `RE-HQ`) hoặc ít nhất ghi chú rõ ranh giới scope khi có các dấu hiệu sau:
- output đòi hỏi tracker nhiều owner;
- cần điều phối response từ nhiều phòng ban;
- legal chỉ là một module trong deal workflow tổng thể;
- recommendation phụ thuộc structuring hoặc DD coordination ngoài phạm vi legal specialist.

## Quy tắc rà hardening

Khi vừa sửa skill graph hoặc refactor workflow, phải rà thêm:
- entry `re-legal` và `re-legal-operations` có còn nói cùng một load order và cùng một matrix không;
- template map trong `re-legal-operations` có theo kịp output shape mới không;
- boundary note với `RE-HQ` / `RE-Investment-Finance` có bị mâu thuẫn ở đâu không;
- `routing-map.md` có cần cập nhật không.

Nếu một trong các điểm trên lệch, chưa nên coi refactor là hoàn tất.

## Mẫu kiểm tra nhanh

Với deliverable chính thức, **đính block này vào cuối deliverable** (hoặc ghi vào deal dossier nếu thuộc một deal) — xem mục Verification trace trong `../../references/operating-contract.md`. Thiếu block = bản nháp chưa QC.

```md
## Kiểm tra trước khi chốt
- Deliverable: ...
- Điểm đã đủ cơ sở: ...
- Điểm còn qualified / cần caveat: ...
- Missing facts / missing docs: ...
- Hiệu lực văn bản đã kiểm chứng qua tvpl: có / chưa (caveat)
- Có cần route `RE-HQ` không: ...
```

### Mini format cho chat-native legal reply

```md
- Kết luận ngắn: ...
- Căn cứ / vì sao: ...
- Caveat / thiếu dữ kiện: ...
- Bước tiếp theo: ...
```

## Quy tắc ngôn ngữ

- Tên skill giữ bằng tiếng Anh.
- Body, workflow và rule viết bằng tiếng Việt.
- Thuật ngữ quan trọng có thể trình bày theo kiểu **Việt ngữ (Anh ngữ)** khi cần.

## Lỗi thường gặp

1. Chỉ rà ngôn ngữ mà không rà logic kết luận.
2. Không kiểm tra xem output có đang over-claim không.
3. Bỏ sót routing check cuối cùng.
4. Dùng cùng một checklist cho mọi loại deliverable.
5. Sau khi refactor skill graph, không rà lại template pointers và verification handoff nên hệ thống nhìn đúng nhưng load order thực tế bị lệch.
6. Với output gửi `RE-HQ`, chỉ tóm tắt findings mà không nói rõ owner boundary nên dễ bị hiểu nhầm là `RE-Legal` đang ôm coordination.
7. Để legal question list / missing-docs note phình thành multi-owner tracker, làm lệch vai specialist legal execution.

## Checklist kiểm tra

- [ ] Đã áp đúng rule theo loại deliverable
- [ ] Kết luận không vượt quá hồ sơ hiện có
- [ ] Missing facts / missing docs đã được nêu rõ nếu còn thiếu
- [ ] Next step hoặc action đã đủ cụ thể
- [ ] Đã kiểm tra dấu hiệu phải route `RE-HQ`
