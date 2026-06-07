---
name: re-legal-operating-matrix
description: Use when cần map loại task legal sang primary skill, companion skills, deliverable template, verification rule và escalation trigger trong agent RE-Legal.
version: 1.0.0
license: MIT
---

# re-legal Operating Matrix

## Overview

Skill này là bảng điều hướng vận hành của `RE-Legal`.

Mục tiêu là map nhanh từ **loại việc** sang:
- primary skill;
- companion skill;
- deliverable template;
- verification rule;
- escalation trigger.

Skill này không thay thế analysis. Nó là lớp chọn workflow nhanh để giảm lệch lane và giảm việc phải quyết định lại từ đầu ở mỗi task.

## When to Use

Dùng skill này khi:
- task mới vào nhưng lane đã tương đối rõ;
- cần chọn nhanh bundle skill phù hợp;
- cần so operating flow giữa nhiều loại legal task;
- cần kiểm tra xem output nên đi theo template nào.

Do not use for:
- thay specialist analysis;
- thay intake decision nếu task còn mơ hồ hoàn toàn;
- ôm coordination nhiều workstream.

## Core Matrix

| Loại việc | Primary skill | Companion skill(s) | Template / output | Verification | Escalation trigger |
|---|---|---|---|---|---|
| Legal status review | `licensing-expert` | `legal-writing` | `legal-status-report-template` | `re-legal-verification-rules` | nếu task thành DD coordination hoặc cần multi-owner tracker |
| Approval path / thủ tục | `licensing-expert` | `legal-writing` | `approval-matrix-template` | `re-legal-verification-rules` | nếu approval strategy phụ thuộc coordination nhiều phòng ban |
| Permit / compliance gap | `licensing-expert` | `legal-writing` | `permit-gap-list-template` | `re-legal-verification-rules` | nếu gap remediation cần cross-functional program management |
| Điều kiện mở bán / chuyển nhượng / huy động vốn | `licensing-expert` | `legal-writing` | `recommendation-memo-template` hoặc `permit-gap-list-template` | `re-legal-verification-rules` | nếu kết luận phụ thuộc structuring / DD tổng thể |
| NDA / LOI / Term Sheet review | `legal-counsel` | `legal-writing` | `clause-issue-list-template` hoặc `contract-review-memo-template` | `re-legal-verification-rules` | nếu review trở thành overall deal coordination |
| SPA / SHA / JVA / project transfer review | `legal-counsel` | `licensing-expert`, `legal-writing` | `contract-review-memo-template` | `re-legal-verification-rules` | nếu drafting/signing phụ thuộc DD coordination hoặc structuring đa stream |
| Clause scan nhanh | `legal-counsel` | none hoặc `legal-writing` | `clause-issue-list-template` | `re-legal-verification-rules` | nếu issue thật ra là project legal blocker chứ không chỉ clause risk |
| Recommendation legal note | `licensing-expert` hoặc `legal-counsel` | `legal-writing` | `recommendation-memo-template` | `re-legal-verification-rules` | nếu recommendation cần overall investment/deal decision framework |
| Legal question list / missing docs | `licensing-expert` hoặc `legal-counsel` | none hoặc `legal-writing` | `legal-question-list-template` | `re-legal-verification-rules` | nếu question list đã biến thành request tracker nhiều owner |
| Rename / inventory / classify / move nhẹ | `doc-renamer` | none | `document-ops-report-template` | `re-legal-verification-rules` nếu output cần chốt | nếu thành data room orchestration / multi-team flow |
| Hybrid legal input cho `RE-HQ` — project stream | `licensing-expert` | `legal-writing` hoặc none | `hybrid-legal-package-template` hoặc `blocker-memo-template` hoặc `legal-question-list-template` | `re-legal-verification-rules` | nếu package bắt đầu phình thành multi-owner tracker hoặc overall DD coordination |
| Hybrid legal input cho `RE-HQ` — corporate / transaction stream | `legal-counsel` | `legal-writing` hoặc none | `hybrid-legal-package-template` hoặc `cp-closing-issue-note-template` hoặc `legal-question-list-template` | `re-legal-verification-rules` | nếu package bắt đầu phình thành closing coordination hoặc structuring decision framework tổng thể |

## Quick Selection Rule

1. Nếu task chưa rõ lane → dùng `re-legal-intake-router` trước.
2. Nếu lane đã rõ nhưng chưa rõ output → dùng `re-legal-deliverable-templates`.
3. Nếu output là tiếng Việt quan trọng → gọi `legal-writing`.
4. Trước khi chốt bất kỳ output chính thức nào → dùng `re-legal-verification-rules`.
5. Nếu xuất hiện dấu hiệu coordination đa stream → route `RE-HQ`.
   - DD coordination → `dd-coordinator` tại workflow `RE-HQ`
   - deal structuring / transaction architecture → `deal-structuring-advisor` tại workflow `RE-HQ`
6. Nếu task là mixed legal issue:
   - project legal drives contract / transferability → `licensing-expert` trước
   - clause / CP-closing / liability allocation drives issue → `legal-counsel` trước
7. Nếu `RE-HQ` chỉ cần specialist legal package, output tối thiểu phải có:
   - issue
   - basis / supporting document or clause
   - impact
   - blocker hay confirm-point
   - next step và owner boundary
8. Với HQ-led workflow, ưu tiên template hóa trước thay vì biến output thành memo dài mặc định:
   - project stream → `hybrid-legal-package-template` hoặc `blocker-memo-template`
   - corporate / transaction stream → `hybrid-legal-package-template` hoặc `cp-closing-issue-note-template`

## System Sync Rule

Khi thay đổi operating boundary hoặc hybrid workflow của bundle `RE-Legal`, không được chỉ sửa một skill đơn lẻ rồi dừng.

Tối thiểu phải so đồng bộ các lớp sau nếu chúng có liên quan:
- `README.md` của bundle legal;
- `re-legal-intake-router`;
- `re-legal-operating-matrix`;
- `re-legal-deliverable-templates`;
- `legal-writing`;
- `re-legal-verification-rules`;
- specialist skill / references tương ứng như `licensing-expert`, `legal-counsel` hoặc `doc-renamer`;
- boundary notes như `dd-coordinator` và `deal-structuring-advisor` nếu boundary với `RE-HQ` bị tác động;
- `re-legal-skill-maintenance` nếu thay đổi có ảnh hưởng đến graph, metadata hoặc source-sync rule.

Đặc biệt với các thay đổi boundary giữa `RE-Legal` và `RE-HQ`:
- routing rule;
- template map;
- writing mode;
- owner boundary wording;
- escalation trigger;
- metadata `related_skills`

phải nói cùng một logic ở tất cả các lớp trên. Nếu không, agent sẽ chọn đúng lane nhưng phát hành sai output shape, hoặc ngược lại.

## Language Rule

- Tên skill giữ bằng tiếng Anh.
- Body và matrix guidance viết bằng tiếng Việt.
- Thuật ngữ quan trọng có thể dùng kiểu **Việt ngữ (Anh ngữ)** khi cần.

## Common Pitfalls

1. Dùng matrix này như quyết định cuối cùng dù task vẫn còn mơ hồ.
2. Chọn đúng primary skill nhưng quên template layer.
3. Có output quan trọng nhưng quên verification layer.
4. Thấy task phình thành coordination mà vẫn cố giữ trong `RE-Legal`.

## Verification Checklist

- [ ] Đã xác định đúng loại việc trước khi dùng matrix
- [ ] Đã chọn đúng primary skill
- [ ] Đã chọn đúng template / output shape
- [ ] Đã cân nhắc `legal-writing` nếu output là tiếng Việt quan trọng
- [ ] Đã kiểm tra escalation trigger sang `RE-HQ`
