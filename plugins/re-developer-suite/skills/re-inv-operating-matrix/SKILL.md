---
name: re-inv-operating-matrix
description: Use to map a deal task to the right RE-Investment-Finance skill, specialist pulls, template, verification, and escalation — a quick selection layer for the investment deal lifecycle.
version: 1.0.0
license: MIT
---

# RE-Investment Operating Matrix

Bảng điều hướng vận hành của `RE-Investment-Finance`. Map nhanh từ **loại việc trong deal lifecycle** sang primary skill, specialist pull, template, verification và escalation — để giảm lệch lane và không phải quyết định lại từ đầu mỗi deal.

Skill này không thay phân tích. Nó là lớp chọn workflow nhanh, dùng cùng entry `re-inv`.

## Khi nào dùng

Dùng khi: deal mới vào nhưng đã rõ đang ở giai đoạn nào; cần chọn nhanh skill + template + QC; cần so flow giữa các giai đoạn lifecycle.

Không dùng cho: thay phân tích đầu tư; thay quyết định khi task còn quá mơ hồ (dùng entry `re-inv` để chốt mục tiêu trước).

## Ma trận chính

| Giai đoạn / loại việc | Primary skill | Specialist pull | Template / output | Verification | Escalation |
|---|---|---|---|---|---|
| Sàng lọc deal đầu vào | `re-inv-screening` | — (1 câu hỏi legal/market nếu cần) | `deal-screening-note` | `re-inv-verification-rules` | nếu Proceed → BC sơ bộ |
| Báo cáo đầu tư sơ bộ | `re-inv-preliminary-report` | `re-legal-licensing`+`tvpl`, `re-rnd`, `re-project-design-planning` | `preliminary-investment-report` | `re-inv-verification-rules` | nếu Go/Conditional → FS |
| Feasibility study (FS) | `re-inv-feasibility-study` | `re-project-design-planning` (GFA/mix), `re-rnd` (giá) | `fs-structure` + `fs-excel-build-guide` → `.xlsx` | `re-inv-verification-rules` | — |
| Báo cáo đầy đủ / IC memo | `re-inv-full-report` | `re-legal-licensing`+`re-legal-counsel`+`tvpl`, `re-rnd` | `full-investment-report` + `investment-memo` | `re-inv-verification-rules` | nếu cần duyệt đa phòng cấp executive → `RE-HQ` |
| Cấu trúc deal + LOI | `re-inv-deal-structuring` | `re-legal-counsel`/`re-legal-licensing`, `re-inv-feasibility-study` | `loi` + `loi-and-offer-guide` | `re-inv-verification-rules` | nếu cấu trúc cần trọng tài đa phòng → `RE-HQ` |
| Điều phối DD | `re-inv-dd-coordinator` | `RE-Legal` (`re-legal-licensing`/`re-legal-counsel`), các stream khác | `dd-executive-summary` + `finding` | `re-inv-verification-rules` | quyết định đa phòng cấp executive → `RE-HQ` |
| Closing checklist (CP/CD) | `re-inv-dd-coordinator` | `re-legal-counsel` (cp-closing, material-contract-schedule) | `closing-checklist` | `re-inv-verification-rules` | chứng nhận sẵn-sàng-closing là kết luận pháp lý → `RE-Legal` |
| Deal team briefing (theo altitude) | `re-inv` | findings từ `re-inv-dd-coordinator` | `deal-team-briefing` | `re-inv-verification-rules` | tổng hợp đa phòng cấp executive / trọng tài → `RE-HQ` |

> Template nằm ở `../../templates/` trừ FS spec (`re-inv-feasibility-study/references/`) và LOI guide (`re-inv-deal-structuring/references/`).

## Quy tắc chọn nhanh

1. Nếu task chưa rõ giai đoạn → dùng entry `re-inv` để chốt decision/deliverable trước.
2. Chọn primary skill theo giai đoạn lifecycle (screening → sơ bộ → FS → đầy đủ/IC → structure/LOI → DD).
3. Kéo specialist input đúng domain: pháp lý → `re-legal-licensing`/`re-legal-counsel` (+`tvpl`); thị trường → `re-rnd`; chỉ tiêu quy hoạch/product mix → `re-project-design-planning`.
4. Trước khi chốt bất kỳ output chính thức nào → `re-inv-verification-rules`.
5. Chỉ route `RE-HQ` khi cần tổng hợp đa phòng cấp executive hoặc trọng tài xung đột — không phải cho từng bước lifecycle.

## Quy tắc đồng bộ hệ thống

Khi đổi boundary hoặc lifecycle của bundle Investment, phải so đồng bộ:
- `re-inv` (entry: lifecycle map + load order);
- `re-inv-operating-matrix` (bảng này);
- `re-inv-verification-rules`;
- template liên quan trong `../../templates/`;
- `../../references/routing-map.md` nếu boundary với `RE-HQ`/`RE-Legal` bị tác động.

## Quy tắc ngôn ngữ

- Tên skill giữ bằng tiếng Anh; body và matrix viết bằng tiếng Việt; thuật ngữ quan trọng dùng kiểu **Việt ngữ (Anh ngữ)** khi cần.

## Lỗi thường gặp

1. Dùng matrix khi task còn quá mơ hồ (đáng ra chốt mục tiêu ở entry trước).
2. Chọn đúng skill nhưng quên template hoặc verification layer.
3. Route `RE-HQ` cho từng bước lifecycle thay vì chỉ khi cần executive synthesis.
4. Quên kéo specialist input đúng domain (pháp lý/thị trường/quy hoạch).

## Checklist kiểm tra

- [ ] Đã xác định đúng giai đoạn lifecycle
- [ ] Đã chọn đúng primary skill + specialist pull
- [ ] Đã chọn đúng template / output shape
- [ ] Đã chạy `re-inv-verification-rules` trước khi chốt
- [ ] Escalation `RE-HQ` chỉ dùng cho executive synthesis / trọng tài
