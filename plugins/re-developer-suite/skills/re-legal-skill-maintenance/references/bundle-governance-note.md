> **Lưu ý kiểm chứng:** Tài liệu này được migrate từ thư viện nghiệp vụ cũ. Mọi quy định, thuế suất, ngưỡng, thủ tục và cơ quan có thẩm quyền phải được kiểm tra lại bằng nguồn chính thức còn hiệu lực tại ngày sử dụng.

# re-legal Bundle Governance Note

## 1. Vai trò các lớp trong bundle legal
- **Intake / routing:** `re-legal-intake-router`
- **Operating selection / matrix:** `re-legal-operating-matrix`
- **Specialist analysis:** `licensing-expert`, `legal-counsel`, `doc-renamer`
- **Deliverable packaging:** `re-legal-deliverable-templates`
- **Drafting / polish:** `legal-writing`
- **Verification / QC:** `re-legal-verification-rules`
- **Maintenance / anti-drift:** `re-legal-skill-maintenance`
- **Boundary doctrine:** route `RE-HQ` khi task đã thành DD coordination, structuring hoặc workflow nhiều owner

## 2. Canonical operating doctrine
`RE-Legal` là profile **specialist legal execution**.

Điều đó có nghĩa:
- không ôm DD coordination tổng thể;
- không ôm structuring nhiều phòng ban;
- không biến legal question list thành multi-owner tracker;
- không biến document ops thành data room orchestration.

Nếu workflow đã chuyển sang coordination đa stream, phần điều phối thuộc `RE-HQ`.

## 3. Canonical pipeline
```text
intake → routing → specialist analysis → template selection → drafting/polish → verification → escalation
```

Nếu sửa một lớp mà làm lệch pipeline này, phải so lại toàn bundle.

## 4. Boundary doctrine với `RE-HQ`
- `RE-HQ` điều phối DD, structuring và workflow nhiều owner.
- `RE-Legal` chỉ phát hành specialist legal input.
- Hybrid output gửi `RE-HQ` phải nói rõ:
  - issue;
  - basis;
  - impact;
  - blocker hay confirm-point;
  - next step;
  - owner boundary.

## 5. Anti-drift priority
Khi hardening bundle, ưu tiên giữ đồng bộ 4 thứ:
1. routing rule;
2. load order;
3. template map;
4. metadata graph (`related_skills`).

Nếu body text đúng nhưng metadata graph sai, skill loader và cross-skill discovery vẫn có thể lệch.

## 6. Khi nào dùng `re-legal-skill-maintenance`
Dùng ngay khi:
- thay source folder cho một skill;
- đồng bộ lại canonical copy do Sếp cung cấp;
- refactor bundle nhiều file;
- nghi ngờ graph bị drift sau một đợt patch.