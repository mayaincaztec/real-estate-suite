# re-legal Legal Skills Map

Bundle `legal/` trong agent `RE-Legal` là hệ thống specialist skills cho **pháp lý bất động sản** ở phạm vi **specialist legal execution**.

Không dùng bundle này làm lớp điều phối chính cho:
- Rà Soát Thẩm Định (Due Diligence) nhiều workstream;
- deal structuring nhiều phòng ban;
- issue tracker liên phòng ban;
- data room orchestration quy mô lớn.

Các bài toán đó thuộc `RE-HQ`.

---

## 1. Operating model ngắn

Pipeline canonical của `RE-Legal`:

```text
intake → routing → specialist analysis → template selection → drafting/polish → verification → escalation
```

### Các lớp chính
1. **Intake / routing**
   - `re-legal-intake-router`
2. **Specialist analysis**
   - `licensing-expert`
   - `legal-counsel`
   - `doc-renamer`
3. **Deliverable packaging**
   - `re-legal-deliverable-templates`
   - `legal-writing`
4. **Quality control**
   - `re-legal-verification-rules`
5. **Maintenance / anti-drift**
   - `re-legal-skill-maintenance`

---

## 2. Skill map theo vai trò

### `re-legal-intake-router`
- dùng khi task mới vào chưa rõ lane;
- chốt scope `RE-Legal` hay route `RE-HQ`;
- chốt deliverable và load order.

### `licensing-expert`
- pháp lý dự án;
- permits / compliance / approval path;
- title / transferability / legal status.

### `legal-counsel`
- review hợp đồng / clause risk;
- drafting / negotiation support;
- transaction legal memo / CP-closing legal issues.

### `doc-renamer`
- rename / inventory / classify / move file mức cơ bản;
- support document ops nhẹ, không phải data room orchestration.

### `re-legal-deliverable-templates`
- chọn khung output chuẩn cho memo / matrix / issue list / blocker note / hybrid package.

### `legal-writing`
- polish tiếng Việt cho deliverable pháp lý quan trọng.

### `re-legal-verification-rules`
- QC cuối trước khi chốt output.

---

## 3. Routing boundary với `RE-HQ`

### Giữ trong `RE-Legal` khi
- trọng tâm là legal analysis một stream;
- output cuối là memo / issue list / report / recommendation từ góc legal specialist;
- document ops chỉ là support step mức cơ bản.

### Route `RE-HQ` khi
- task là DD coordination;
- task là structuring nhiều phòng ban;
- cần issue tracker nhiều owner;
- cần data room orchestration lớn;
- legal chỉ là một stream trong workflow điều phối tổng thể.

### Case hybrid
- `RE-HQ` điều phối tổng thể;
- `RE-Legal` chỉ phát hành specialist legal input;
- output tối thiểu nên trả lời được: issue, basis, impact, blocker-or-confirm point, next step và owner boundary.

---

## 4. Recommended load order

### Pháp lý dự án
1. `re-legal-intake-router`
2. `licensing-expert`
3. `re-legal-deliverable-templates`
4. `legal-writing` nếu cần polished Vietnamese output
5. `re-legal-verification-rules`

### Hợp đồng / giao dịch
1. `re-legal-intake-router`
2. `legal-counsel`
3. `licensing-expert` nếu có project / regulatory dependency
4. `re-legal-deliverable-templates`
5. `legal-writing` nếu cần polished Vietnamese output
6. `re-legal-verification-rules`

### Document ops
1. `re-legal-intake-router`
2. `doc-renamer`
3. `re-legal-deliverable-templates` nếu cần `document-ops-report-template`
4. `re-legal-verification-rules` nếu cần chốt output

### Coordination / đa stream
1. `re-legal-intake-router`
2. xác nhận phải route `RE-HQ`
3. nếu vẫn cần legal output riêng, chỉ giữ specialist legal lane tương ứng trong `RE-Legal`
4. nếu vừa sửa graph / boundary, rà `re-legal-skill-maintenance`

---

## 5. Cross-skill operating matrix

| Loại việc | Primary skill | Companion skill(s) | Template / output | Verification |
|---|---|---|---|---|
| Legal status review | `licensing-expert` | `legal-writing` | `legal-status-report-template` | `re-legal-verification-rules` |
| Approval path / thủ tục | `licensing-expert` | `legal-writing` | `approval-matrix-template` | `re-legal-verification-rules` |
| Permit / compliance gap | `licensing-expert` | `legal-writing` | `permit-gap-list-template` | `re-legal-verification-rules` |
| Điều kiện mở bán / chuyển nhượng / huy động vốn | `licensing-expert` | `legal-writing` | `recommendation-memo-template` / `permit-gap-list-template` | `re-legal-verification-rules` |
| NDA / LOI / Term Sheet review | `legal-counsel` | `legal-writing` | `clause-issue-list-template` / `contract-review-memo-template` | `re-legal-verification-rules` |
| SPA / SHA / JVA / project transfer review | `legal-counsel` | `licensing-expert`, `legal-writing` | `contract-review-memo-template` | `re-legal-verification-rules` |
| Clause scan nhanh | `legal-counsel` | none hoặc `legal-writing` | `clause-issue-list-template` | `re-legal-verification-rules` |
| Recommendation legal note | `licensing-expert` hoặc `legal-counsel` | `legal-writing` | `recommendation-memo-template` | `re-legal-verification-rules` |
| Legal question list / missing docs | `licensing-expert` hoặc `legal-counsel` | none hoặc `legal-writing` | `legal-question-list-template` | `re-legal-verification-rules` |
| Hybrid legal input cho `RE-HQ` — project stream | `licensing-expert` | `legal-writing` hoặc none | `hybrid-legal-package-template` / `blocker-memo-template` / `legal-question-list-template` | `re-legal-verification-rules` |
| Hybrid legal input cho `RE-HQ` — corporate / transaction stream | `legal-counsel` | `legal-writing` hoặc none | `hybrid-legal-package-template` / `cp-closing-issue-note-template` / `legal-question-list-template` | `re-legal-verification-rules` |
| Rename / inventory / classify / move nhẹ | `doc-renamer` | none | `document-ops-report-template` | `re-legal-verification-rules` nếu cần chốt output |

---

## 6. Governance / maintenance pointers

Khi sửa bundle legal ở mức system:
- rà `README.md`, `re-legal-intake-router`, `re-legal-operating-matrix`, `re-legal-deliverable-templates`, `re-legal-verification-rules` và specialist skill liên quan;
- với boundary change giữa `RE-Legal` và `RE-HQ`, giữ wording nhất quán rằng execution coordination nằm ở `RE-HQ`, không ở local graph của `RE-Legal`;
- dùng `re-legal-skill-maintenance` để rà anti-drift và lean regression.

Reference nên xem:
- `re-legal-skill-maintenance/references/bundle-governance-note.md`
- `re-legal-skill-maintenance/references/maintenance-checklist.md`
- `re-legal-skill-maintenance/references/lean-regression-checklist.md`

---

## 7. Checklist vận hành ngắn

- [ ] Task đã được intake chưa
- [ ] Deliverable đã được chốt chưa
- [ ] Đã chọn đúng primary skill chưa
- [ ] Có cần template layer không
- [ ] Có cần `legal-writing` không
- [ ] Đã chạy verification layer trước khi chốt chưa
- [ ] Có dấu hiệu phải route `RE-HQ` không
