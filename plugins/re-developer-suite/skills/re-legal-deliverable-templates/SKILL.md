---
name: re-legal-deliverable-templates
description: Use when cần chọn hoặc áp dụng template đầu ra chuẩn cho legal status report, approval matrix, permit gap list, contract review memo, clause issue list, legal question list hoặc recommendation memo trong agent RE-Legal.
version: 1.0.0
license: MIT
---

# re-legal Deliverable Templates

## Overview

Skill này là template layer của `RE-Legal`.

Mục tiêu là giúp agent không phải dựng lại format đầu ra từ đầu mỗi lần, mà chọn đúng khung cho từng loại deliverable pháp lý thường gặp trong profile này.

Skill này **không thay thế** specialist analysis. Nó chỉ cung cấp khung đóng gói đầu ra để dùng cùng `licensing-expert`, `legal-counsel` và `legal-writing`.

## When to Use

Dùng skill này khi:
- cần chốt format đầu ra trước khi bắt đầu phân tích;
- cần chuẩn hóa memo / report / issue list để nhiều task có cùng logic trình bày;
- cần giao cho `legal-writing` một khung sườn rõ ràng để polish;
- cần lựa chọn giữa nhiều dạng output gần nhau nhưng mục đích khác nhau.

Do not use for:
- thay thế việc phân tích pháp lý nền;
- quyết định routing lane;
- điều phối Rà Soát Thẩm Định (Due Diligence) hoặc deal workflow nhiều stream.

## Template Map

### 1. Dùng với `licensing-expert`
- `references/legal-status-report-template.md`
- `references/approval-matrix-template.md`
- `references/permit-gap-list-template.md`
- `references/legal-question-list-template.md`
- `references/recommendation-memo-template.md`
- `references/blocker-memo-template.md`
- `references/hybrid-legal-package-template.md`

### 2. Dùng với `legal-counsel`
- `references/contract-review-memo-template.md`
- `references/clause-issue-list-template.md`
- `references/legal-question-list-template.md`
- `references/recommendation-memo-template.md`
- `references/cp-closing-issue-note-template.md`
- `references/hybrid-legal-package-template.md`

### 3. Dùng với `legal-writing`
- dùng khi đã chốt template và cần polish câu chữ, logic chuyển đoạn, mức formal và cấu trúc kết luận.
- với output cho HQ-led workflow, ưu tiên kết hợp thêm `references/hybrid-legal-package-template.md`, `references/blocker-memo-template.md` hoặc `references/cp-closing-issue-note-template.md` tùy stream.
- nếu cần điểm neo rất ngắn để ra bản nháp nhanh, có thể xem thêm:
  - `references/hybrid-legal-package-short-example.md`
  - `references/blocker-memo-short-example.md`
  - `references/document-ops-report-short-example.md`

### 4. Dùng với `doc-renamer`
- `references/document-ops-report-template.md`
- dùng khi rename / inventory / classify / move file cần được chốt thành output có cấu trúc thay vì chỉ báo ngắn bằng chat.

## Selection Rule

### Chọn `legal-status-report-template` khi:
- cần một view tổng quan về tình trạng pháp lý dự án / tài sản;
- cần kết luận sơ bộ theo cấu trúc facts → legal basis → assessment → action.

### Chọn `approval-matrix-template` khi:
- cần map thủ tục, thẩm quyền, hồ sơ, điều kiện và next step theo từng mốc pháp lý.

### Chọn `permit-gap-list-template` khi:
- cần chỉ ra hồ sơ đang thiếu gì, rủi ro của từng khoảng trống, và việc cần làm tiếp.

### Chọn `contract-review-memo-template` khi:
- cần review memo tương đối đầy đủ cho hợp đồng / tài liệu giao dịch.

### Chọn `clause-issue-list-template` khi:
- cần scan nhanh theo clause, issue, risk, proposal, priority.

### Chọn `legal-question-list-template` khi:
- hồ sơ còn thiếu nhiều facts và output chính là danh sách câu hỏi / yêu cầu làm rõ.

### Chọn `recommendation-memo-template` khi:
- cần chốt hướng xử lý, option comparison hoặc go / conditional go / no-go recommendation.

### Chọn `hybrid-legal-package-template` khi:
- output sẽ được gửi cho `RE-HQ` để nhúng vào DD, structuring, IC memo hoặc HQ-led workflow khác;
- cần format issue → basis → impact → blocker/confirm-point → next step → owner boundary.

### Chọn `blocker-memo-template` khi:
- trọng tâm là một blocker pháp lý dự án đang chặn transferability, commercialization, DD conclusion hoặc structuring path.

### Chọn `cp-closing-issue-note-template` khi:
- trọng tâm là CP, closing deliverables, signing-closing gap hoặc legal dependency đang ảnh hưởng việc đóng giao dịch.

### Chọn `document-ops-report-template` khi:
- task chủ yếu là rename / inventory / classify / move file ở mức support workflow;
- cần một bảng output có cấu trúc để chốt kết quả document ops;
- chưa đến mức phải route `RE-HQ` như một data room orchestration thực thụ.

## Workflow

1. Xác định lane chuyên môn chính bằng `re-legal-intake-router` nếu cần.
2. Xác định deliverable mục tiêu.
3. Nếu output là hybrid package cho `RE-HQ`, chốt trước đây là project stream hay corporate / transaction stream.
4. Chọn template gần nhất với mục tiêu sử dụng thực tế.
5. Dùng specialist skill chính để tạo nội dung nền.
6. Dùng `legal-writing` để polish đầu ra nếu là deliverable tiếng Việt quan trọng.
7. Với HQ-led workflow, bảo đảm output cuối có đủ issue / basis / impact / blocker-or-confirm point / next step / owner boundary.
8. So checklist bằng `re-legal-verification-rules` trước khi chốt.

## Language Rule

- Tên skill giữ bằng tiếng Anh.
- Body, workflow và template guidance viết bằng tiếng Việt.
- Thuật ngữ chuyên ngành quan trọng có thể trình bày theo kiểu **Việt ngữ (Anh ngữ)** khi cần.

## Common Pitfalls

1. Chọn template theo thói quen thay vì theo mục tiêu thật của task.
2. Dùng report template cho một câu hỏi đáng ra chỉ cần issue list ngắn.
3. Trộn memo phân tích với question list trong cùng một output.
4. Có template rồi nhưng không kiểm tra lại bằng verification layer.

## Verification Checklist

- [ ] Đã xác định đúng lane chuyên môn trước khi chọn template
- [ ] Template phù hợp với mục tiêu sử dụng thực tế của output
- [ ] Nếu output là tiếng Việt quan trọng, đã cân nhắc gọi `legal-writing`
- [ ] Đã so lại bằng `re-legal-verification-rules` trước khi chốt
