> **Lưu ý kiểm chứng:** Tài liệu này được migrate từ thư viện nghiệp vụ cũ. Mọi quy định, thuế suất, ngưỡng, thủ tục và cơ quan có thẩm quyền phải được kiểm tra lại bằng nguồn chính thức còn hiệu lực tại ngày sử dụng.

# Token-Lean re-legal Profile Optimization

Dùng khi cần giảm token overhead nền của agent `RE-Legal` mà không làm mất operating boundary pháp lý.

## Mục tiêu
Ưu tiên 3 đòn theo thứ tự:
1. **Giảm default toolsets** trong `config.yaml`.
2. **Rút prompt nền** ở `SOUL.md` và `OPERATING_GUIDE.md`.
3. **Dọn profile-local skill inventory** để chỉ giữ skill thật sự phục vụ specialist legal lane.

## Lean baseline đã được kiểm chứng cho `RE-Legal`
### Tool posture mặc định
Giữ:
- `file`
- `skills`
- `session_search`
- `memory`
- `web`
- `terminal`

Tắt khỏi default CLI nếu không thật sự cần:
- `browser`
- `clarify`
- `code_execution`
- `delegation`
- `kanban`
- `messaging`
- `todo`

## Prompt slimming rule
### `SOUL.md`
Chỉ giữ các lớp cốt lõi:
- role
- xưng hô
- scope boundary
- style
- routing nhanh
- core rules

### `OPERATING_GUIDE.md`
Chỉ giữ:
- mission
- default posture
- core skill loading strategy
- lean load order
- tool posture
- standard outputs
- quality bar

Không nhét lại SOP chi tiết nếu đã có skill bundle tương ứng như:
- `re-legal-intake-router`
- `re-legal-operating-matrix`
- `re-legal-deliverable-templates`
- `re-legal-verification-rules`

## Skill inventory pruning rule
### Nên giữ trong profile local
- legal core bundle của `RE-Legal`
- `general/concise-natural-response-style`
- `re-hq` nếu vẫn muốn tự quản trị Codex ngay trong profile này

### Nên đưa ra khỏi active inventory
- non-legal categories không phục vụ legal specialist lane
- legal skills đã thành boundary-only và thực chất thuộc `RE-HQ` orchestration lane
- extra agent-dev skills không cần cho vận hành thường ngày của `RE-Legal`

## Safe execution pattern
1. Backup `config.yaml`, `SOUL.md`, `OPERATING_GUIDE.md`, snapshot skill index và skill folders trước khi dọn.
2. Khi chỉnh toolsets qua CLI/config helper, verify lại file YAML sau đó để chắc giá trị đang là **list YAML thật**, không phải stringified JSON list.
3. Khi dọn skill inventory, ưu tiên **move vào archive/backup** thay vì xóa hẳn.
4. Verify lại số skill active sau khi dọn.
5. Nhắc user mở session mới hoặc dùng `/reset` và `/reload-skills` để Codex nhận config/toolset/skill graph mới.

## Verify tối thiểu
- `platform_toolsets.cli` còn đúng baseline lean.
- `agent.disabled_toolsets` phản ánh nhóm đã tắt.
- `SOUL.md` và `OPERATING_GUIDE.md` đã ngắn hơn rõ rệt nhưng vẫn giữ legal boundary.
- active `skills/` chỉ còn legal core + support skills đã chốt.
- backup path tồn tại và rollback được.
