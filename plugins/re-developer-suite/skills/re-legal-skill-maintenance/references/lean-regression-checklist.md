> **Lưu ý kiểm chứng:** Tài liệu này được migrate từ thư viện nghiệp vụ cũ. Mọi quy định, thuế suất, ngưỡng, thủ tục và cơ quan có thẩm quyền phải được kiểm tra lại bằng nguồn chính thức còn hiệu lực tại ngày sử dụng.

# Lean Regression Checklist for re-legal

Dùng checklist này sau mỗi đợt hardening / cleanup / token optimization của agent `RE-Legal`.

## 1. Prompt baseline
- [ ] `SOUL.md` vẫn chỉ giữ role, scope, style, routing và core rules
- [ ] `OPERATING_GUIDE.md` vẫn là index vận hành ngắn, không bị biến lại thành SOP dài

## 2. Skill inventory
- [ ] active skills vẫn chủ yếu là legal core bundle + support skills đã chốt
- [ ] không có skill local mới thuộc lane coordination / structuring của `RE-HQ`
- [ ] nếu archive / backup skill, path backup vẫn còn để rollback khi cần

## 3. Metadata graph
- [ ] `skill relationship graph` còn phản ánh graph local thực tế
- [ ] không còn `related_skills` trỏ tới node không tồn tại local trong `RE-Legal`
- [ ] boundary với `RE-HQ` được thể hiện bằng wording hoặc reference, không giả lập local execution node

## 4. Tool posture
- [ ] baseline lean vẫn giữ các nhóm chính: `file`, `skills`, `session_search`, `memory`, `web`, `terminal`
- [ ] không vô tình bật lại `browser`, `clarify`, `code_execution`, `delegation`, `todo`, `messaging`, `cronjob`

## 5. Docs / output layer
- [ ] `README.md` vẫn là doctrine + index ngắn, không ôm quá nhiều SOP
- [ ] matrix / table Markdown còn render sạch
- [ ] nếu thêm examples, examples nằm ở `references/`, không làm phình core `SKILL.md`

## 6. Session reload note
- [ ] đã nhắc `/reload-skills` hoặc session reset khi thay đổi skill graph / tool posture / prompt nền

## Quick report format
```md
## Lean regression check
- Prompt baseline còn gọn: Có / Không
- Skill inventory còn lean: Có / Không
- Dangling graph edges: Có / Không
- Tool posture còn đúng: Có / Không
- README / docs còn sạch: Có / Không
- Reload skills recommended: Có / Không
```
