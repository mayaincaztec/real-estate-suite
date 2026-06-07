---
name: re-legal-skill-maintenance
description: Use when bảo trì thư viện skill của agent RE-Legal, đặc biệt khi thay skill hiện có bằng một source folder bên ngoài, cần backup, sync chính xác, verify artifact và quyết định có normalize theo Codex hay không.
version: 1.0.0
license: MIT
---

# re-legal Skill Maintenance

## Overview

Skill này dùng để bảo trì thư viện skill của agent `RE-Legal` ở lớp vận hành hệ thống.

Trọng tâm là các tình huống như:
- thay skill hiện có bằng một bản mới từ folder bên ngoài;
- sync bản do user cung cấp vào thư viện local của Codex;
- backup trước khi ghi đè;
- verify file sau khi sync;
- nhận diện khi bản thay thế làm mất metadata / related_skills / cấu trúc Codex đã có trước đó.

Skill này không dùng để chỉnh nội dung pháp lý chuyên môn của từng skill; nó là skill quản trị thư viện skill.

## When to Use

Dùng skill này khi:
- user nói “thay skill hiện tại bằng folder này / bản này / source này”; 
- có một canonical copy nằm ngoài `the installed RE Developer Suite skills directory` và cần sync vào profile;
- cần giữ đúng bản user cung cấp, thay vì tự ý rewrite lại theo format khác;
- cần kiểm tra tác động của việc sync đến skill graph hiện có.

Do not use for:
- cập nhật nội dung pháp lý nhỏ trong một skill đang ổn định;
- thêm reference file thông thường;
- tạo workflow legal mới không liên quan bảo trì skill library.

## Core Principle

Khi user **explicitly** cung cấp một replacement folder và nói đó là bản mới nhất, mặc định phải hiểu:
1. **source folder là source of truth** cho lần thay thế đó;
2. phải **copy đúng trước**, không auto-normalize ngay;
3. nếu thấy bản mới làm mất metadata hoặc lệch Codex style, phải báo rõ và tách thành **bước sau tùy chọn**, không tự trộn ngay vào source của user.

## Workflow

### Bước 1 — Xác định scope thay thế
Làm rõ:
- thay toàn bộ skill folder hay chỉ một số file;
- source folder có những file nào;
- target folder hiện có những file nào;
- có file local nào sẽ bị mất nếu mirror 1:1 không.

### Bước 2 — Backup trước khi ghi đè
Trước mọi thao tác replace:
- tạo backup của target skill folder;
- đặt tên backup đủ rõ để rollback;
- chỉ sau đó mới copy đè hoặc mirror.

### Bước 3 — Sync đúng source
- Nếu user muốn “thay bằng folder này”, ưu tiên copy đúng file từ source sang target.
- Không tự sửa wording, metadata hay format trong cùng bước replace, trừ khi user yêu cầu rõ.
- Nếu source chỉ có một phần file, không tự đoán các file còn thiếu là phải xóa; phải nêu rõ cách xử lý.

### Bước 4 — Verify sau sync
Tối thiểu phải verify:
- file nào đã được copy;
- source và target có khớp byte / hash không;
- target đã thực sự phản ánh đúng source chưa.

### Bước 5 — Đánh giá tác động Codex-layer
Sau khi đã sync đúng source, rà nhanh:
- còn frontmatter hợp lệ không;
- có mất `skill discovery tags` / `related_skills` không;
- có làm đứt skill graph hoặc cross-skill routing không;
- với bài toán clean-up graph, `related_skills` của skill local phải phản ánh **node local thực sự tồn tại trong `RE-Legal`**, không để dangling edge sang boundary-only node nằm ở profile khác;
- boundary với `RE-HQ` nên giữ ở body text / governance note / routing doctrine, không giả lập local execution dependency;
- có làm skill loader khó dùng hơn trong các session sau không;
- có làm hỏng dấu đóng `---` của frontmatter sau khi patch metadata không;
- có để lại bảng Markdown lệch số cột / separator sau khi sửa operating docs không;
- có giữ lại wording kiểu `Phase 4 / 5 / 6` ở nơi đáng ra nên đổi sang state-based wording như `operating model hiện tại` không.

Nếu có, báo theo format:
- **đã thay đúng source**;
- **ảnh hưởng phụ** là gì;
- **bước tùy chọn tiếp theo** nếu muốn re-normalize theo Codex.

### Bước 6 — Nhắc về cache / reload
Sau khi sửa skill library:
- nhắc rằng session hiện tại có thể đang cache skill;
- gợi ý mở session mới hoặc dùng `/reload-skills` / `/reset` nếu cần loader thấy bản mới.

## Output Shape

```md
## Kết quả sync skill
- Source: ...
- Target: ...
- Backup: ...
- File đã thay: ...
- Verify: khớp / không khớp

## Ảnh hưởng hệ thống
- Mất / giữ metadata: ...
- Có ảnh hưởng skill graph không: ...
- Có cần normalize lại theo Codex không: ...

## Bước tiếp theo
- ...
```

## Common Pitfalls

1. Ghi đè skill local mà không backup.
2. Thấy source mới “không chuẩn Codex” rồi tự rewrite luôn, làm mất ý định của user.
3. Không verify hash/byte equivalence sau khi copy.
4. Quên nhắc rằng skill loader trong session hiện tại có thể vẫn cache bản cũ.
5. Không tách bạch giữa **replace đúng source** và **normalize theo Codex** như hai quyết định khác nhau.
6. Chỉ sửa body nhưng quên kiểm tra frontmatter closing `---`, làm SKILL.md nhìn đúng nhưng parse lỗi.
7. Patch operating docs nhưng không rà lại bảng Markdown, khiến header và separator lệch số cột.
8. Để lại wording theo roadmap như `Phase 4 / 5 / 6` trong canonical skill sau khi system đã ổn định, làm tài liệu nhanh lỗi thời.
9. Giữ `related_skills` trỏ sang node không tồn tại local trong `RE-Legal`, đặc biệt với các boundary-only workflow thực chất nằm ở `RE-HQ`.
10. Sửa `README.md` kiểu partial patch rồi vô tình làm hỏng cấu trúc Markdown ở phạm vi rộng hơn; với file doctrine/index quan trọng, nếu patch cục bộ bắt đầu lan lỗi, nên rewrite sạch toàn file thay vì tiếp tục vá chồng.

## References

Xem thêm:
- `references/bundle-governance-note.md` — governance doctrine và anti-drift map cho toàn bundle
- `references/maintenance-checklist.md` — checklist verify sau mỗi lần sửa bundle
- `references/token-lean-profile-optimization.md` — playbook giảm token footprint cho `RE-Legal` qua toolsets, prompt nền và skill inventory
- `references/lean-regression-checklist.md` — checklist chống token / graph regression sau mỗi đợt hardening

Nếu sau này có thêm mẫu sync / rollback / merge, tiếp tục bổ sung trong `references/` thay vì làm SKILL.md quá dài.

## Verification Checklist

- [ ] Đã xác định rõ source và target
- [ ] Đã backup target trước khi thay
- [ ] Đã sync đúng theo ý user, không tự ý normalize trong cùng bước
- [ ] Đã verify source-target khớp sau khi copy
- [ ] Đã báo rõ nếu source mới làm mất metadata hoặc cross-skill linkage
- [ ] Nếu vừa làm clean-up graph, `related_skills` local không còn dangling edge sang node không tồn tại trong `RE-Legal`
- [ ] Boundary với `RE-HQ` vẫn được giữ ở doctrine / routing wording thay vì local execution graph
- [ ] Đã kiểm tra frontmatter mở/đóng còn hợp lệ sau patch metadata
- [ ] Đã rà table formatting ở README / matrix / operating docs nếu có sửa
- [ ] Nếu README hoặc index doctrine bị patch lỗi dây chuyền, đã rewrite sạch toàn file thay vì để lại Markdown drift
- [ ] Đã thay wording phase-based bằng state-based wording khi tài liệu đã thành canonical doctrine
- [ ] Đã nhắc reload / reset nếu cần để Codex thấy bản mới
