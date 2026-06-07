> **Lưu ý kiểm chứng:** Tài liệu này được migrate từ thư viện nghiệp vụ cũ. Mọi quy định, thuế suất, ngưỡng, thủ tục và cơ quan có thẩm quyền phải được kiểm tra lại bằng nguồn chính thức còn hiệu lực tại ngày sử dụng.

# Maintenance Checklist After Editing re-legal Bundle

## A. File-level checks
- [ ] SKILL.md frontmatter còn hợp lệ
- [ ] `name` và `description` không bị lệch trigger
- [ ] `skill discovery tags` còn hợp lý
- [ ] `skill relationship graph` phản ánh graph thực tế hiện tại
- [ ] reference files mới đã được link từ SKILL.md nếu cần

## B. Cross-skill sync checks
- [ ] `README.md` còn đúng operating doctrine
- [ ] `re-legal-intake-router` còn đúng load order hiện hành
- [ ] `re-legal-operating-matrix` còn đúng primary skill / template / escalation logic
- [ ] `re-legal-deliverable-templates` còn đúng template map
- [ ] `legal-writing` còn đúng drafting mode nếu output shape thay đổi
- [ ] `re-legal-verification-rules` còn đúng QC logic cho output mới
- [ ] boundary wording sang `RE-HQ` còn đúng và không tạo cảm giác như `RE-Legal` có execution skill local cho coordination / structuring

## C. Hybrid / HQ boundary checks
- [ ] output gửi `RE-HQ` có template rõ chưa
- [ ] owner boundary wording còn nhất quán chưa
- [ ] legal question list có bị phình thành tracker nhiều owner không
- [ ] có đoạn nào vô tình kéo `RE-Legal` sang vai coordination không

## D. Document ops checks
- [ ] nếu sửa `doc-renamer`, đã so lại `document ops report` shape chưa
- [ ] nếu document ops task bắt đầu thành orchestration, đã ghi rõ escalation chưa

## E. Final verification format
```md
## Hardening verification
- Files touched: ...
- Graph impact: ...
- Related skills updated: Có / Không
- README / matrix / router synced: Có / Không
- Boundary với `RE-HQ` còn đúng: Có / Không
- Reload skills recommended: Có / Không
```

## F. Lean regression checks
- [ ] `SOUL.md` và `OPERATING_GUIDE.md` không bị phình lại ngoài core doctrine
- [ ] active skill inventory vẫn bám legal core bundle + support skills đã chốt
- [ ] không còn `related_skills` trỏ tới node không tồn tại local trong `RE-Legal`
- [ ] tool posture vẫn giữ baseline lean, không vô tình bật lại browser / clarify / delegation / todo / messaging / cronjob
- [ ] nếu thêm examples, examples nằm ở `references/` chứ không làm phình core `SKILL.md`