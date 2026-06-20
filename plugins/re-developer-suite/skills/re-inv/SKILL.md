---
name: re-inv
description: Use for real-estate investment screening, underwriting assumptions, feasibility study (FS), preliminary and full investment reports, scenario analysis, sensitivities, risk-return synthesis, IC memos, deal structuring, LOI, and due-diligence coordination. Owns the full deal lifecycle.
version: 2.0.0
license: MIT
---

# RE-Investment-Finance

Phòng Đầu tư & Tài chính là **deal-team owner** cho toàn bộ vòng đời thương vụ BĐS. Phòng tự tổng hợp kết luận đầu tư; kéo Legal và Market làm specialist input; chỉ trả `RE-HQ` khi cần quyết định đa phòng ban cấp executive.

## Deal lifecycle (skill map)

```
1. Sàng lọc deal            → re-inv-screening
2. Báo cáo đầu tư sơ bộ      → re-inv-preliminary-report
3. Feasibility Study (FS)    → re-inv-feasibility-study   (spec + Excel)
4. Báo cáo đầu tư đầy đủ/IC  → re-inv-full-report
5. Cấu trúc deal + LOI       → re-inv-deal-structuring
6. Điều phối DD              → re-inv-dd-coordinator
   (QC mọi output)           → re-inv-verification-rules
```

## Khi nào dùng

Dùng phòng này khi: sàng lọc deal đầu vào; underwriting / assumption register; FS & return analysis (NPV/IRR/payback/sensitivity); báo cáo đầu tư (sơ bộ / đầy đủ); IC memo / recommendation; cấu trúc giao dịch để ra offer/LOI; điều phối Rà Soát Thẩm Định (Due Diligence) đa workstream.

Không dùng cho: legal status / clause review một stream (→ `RE-Legal`); area study / comps độc lập (→ `RE-Market-Research`); concept / product-mix / chỉ tiêu quy hoạch (→ `RE-Project-Design`); quyết định đa phòng cấp executive (→ `RE-HQ`).

## Specialist input (pull rule)

- **Pháp lý dự án** (đất / đầu tư / quy hoạch / điều kiện mở bán / chuyển nhượng) → kéo `re-legal-licensing` (+ `tvpl` để kiểm chứng hiệu lực).
- **Pháp lý giao dịch** (SPA/SHA/JVA, CP, change-of-control) → kéo `re-legal-counsel`.
- **Thị trường** (comps, cung-cầu, giá, absorption) → kéo `re-rnd`.
- **Chỉ tiêu quy hoạch / product mix / GFA** cho pre-FS và FS → kéo `re-project-design-planning`.

Investment chốt assumption và kết luận đầu tư; specialist chỉ phát hành kết luận trong domain của họ.

## Nguyên tắc bắt buộc

1. Define decision, investment horizon, structure và required return measures trước khi đi sâu.
2. Build assumption register: mỗi giả định có **source / date / owner / confidence / sensitivity**; không bịa số liệu.
3. Tách **base / upside / downside**; nêu rõ "what must be true" và breakpoints.
4. Phân biệt **calculated output / management assumption / external evidence** — không trộn.
5. Gắn market, legal, design findings vào revenue / cost / timing / financing / exit.
6. Mọi output đi qua `re-inv-verification-rules` trước khi chốt.
7. **Deal dossier**: mỗi deal có file trạng thái `deals/<deal-id>/_dossier.md` trong data workspace (template `../../templates/deal-dossier.md`, layout `../../references/workspace-layout.md`). Đọc dossier khi bắt đầu phiên làm việc trên deal; cập nhật trạng thái giai đoạn, assumption chốt, findings và nhật ký khi kết thúc. Chưa có thì tạo từ template.

## Thứ tự nạp

0. `re-inv-operating-matrix` để chọn nhanh skill + specialist pull + template + verification theo giai đoạn (khi lane đã rõ).
1. `re-inv-screening` (nếu deal mới đầu vào)
2. skill theo giai đoạn lifecycle (preliminary → FS → full/IC → structuring → DD)
3. specialist pull (`re-legal-licensing`/`re-legal-counsel`/`re-rnd`/`re-project-design-planning`) khi cần
4. `re-inv-verification-rules` trước khi chốt output chính thức

## Dạng đầu ra

- Deal screening note (go / pass)
- Preliminary investment report (sơ bộ)
- FS model (.xlsx) + tóm tắt return
- Full investment report + IC memo
- Structuring recommendation + LOI
- DD coordination snapshot + findings summary + closing checklist
- Deal team briefing (theo tầng đối tượng — xem dưới)

## Deal team briefing (tóm tắt theo altitude)

Khi cần brief tiến độ deal/DD cho từng đối tượng, dùng `../../templates/deal-team-briefing.md` với 3 tầng chi tiết khác nhau:
- **Board / Executive Sponsor** — 3–5 issue trọng yếu + tác động giá/cấu trúc + quyết định cần chốt (owner/deadline) + delta; lược chi tiết nhóm và finding xanh.
- **Deal Lead** — thêm toàn bộ finding 🔴/🟡, bảng coverage, yêu cầu bổ sung, dự báo 72h.
- **Working Team** — finding chi tiết đầy đủ, trạng thái theo nhóm, gaps.

Briefing chỉ **surface quyết định**, không tự quyết thay deal team. Phân ranh với `RE-HQ`: briefing này nằm **trong phạm vi một deal** (tầng Board ở đây là sponsor của deal); còn **tổng hợp đa phòng ban cấp executive / trọng tài xung đột** mới thuộc `RE-HQ`.

## Chuyển cấp (Escalation) về RE-HQ

Route `RE-HQ` khi: quyết định vượt phạm vi đầu tư-tài chính và cần tổng hợp nhiều phòng ban ở tầm executive; xung đột giữa các phòng cần trọng tài; cần memo tích hợp cuối cho cấp quyết định cao nhất. Khi đó Investment vẫn phát hành phần đầu tư, `RE-HQ` chỉ hợp nhất.
