---
name: re-inv-verification-rules
description: Use to quality-control RE-Investment-Finance outputs before finalizing — screening notes, preliminary and full investment reports, feasibility models, IC memos, structuring/LOI, and DD summaries. Checks for fabricated numbers, missing cases, weak assumptions, and scope drift.
version: 1.0.0
license: MIT
---

# RE-Investment Verification Rules

Quality-control layer của `RE-Investment-Finance`, dùng ở cuối workflow trước khi chốt output cho Sếp hoặc IC. Mirror vai trò của `re-legal-verification-rules` bên pháp lý.

## Khi nào dùng

Dùng khi chuẩn bị chốt: screening note, báo cáo đầu tư (sơ bộ/đầy đủ), FS model, IC memo, structuring/LOI, DD summary.

Không dùng cho: thay phân tích gốc; quyết định routing từ đầu.

## Quy tắc chung

### 1. Không bịa số liệu
Thiếu dữ kiện → giả định có căn cứ + đánh dấu, không điền số khống. Không nâng giả định thành sự thật.

### 2. Phân biệt 3 loại số
**Calculated output** (NPV/IRR/margin…) ≠ **management assumption** (giá bán, suất đầu tư, absorption) ≠ **external evidence** (comps, tiền đất, lãi suất). Output phải cho thấy số nào thuộc loại nào.

### 3. Đủ base / upside / downside
Mọi kết luận đầu tư phải có ít nhất 3 kịch bản hoặc sensitivity cho driver trọng yếu, kèm "what must be true" và breakpoints.

### 4. Nguồn có ngày
Mọi external input (giá thị trường, chi phí, pháp lý) phải có nguồn + ngày; pháp lý dẫn chiếu phải đã kiểm chứng hiệu lực qua `tvpl` (qua specialist) hoặc gắn caveat.

### 5. Calc tie-out
Với output có số từ FS: dòng tiền cân, NPV/IRR/payback/peak-funding khớp model; con số trong report khớp file FS.

### 6. Kiểm tra escalation
Nếu quyết định thực chất cần tổng hợp đa phòng cấp executive, nói rõ phần nào thuộc Investment, phần nào route `RE-HQ`.

## Deliverable-specific

- **Screening note**: kết luận go/pass/watch + lý do; không phình thành mini-FS.
- **Preliminary report**: đủ 5 phần; pháp lý & thị trường đã kéo specialist; pre-FS nêu rõ giới hạn.
- **FS model**: assumption register đủ; công thức không hardcode; sensitivity ≥1 chiều; file .xlsx mở được.
- **Full report / IC memo**: thesis + cases + conditions + owners; số tie-out FS.
- **Structuring / LOI**: option có tiêu chí so sánh; LOI nêu rõ điều kiện, tính ràng buộc/không ràng buộc, CP.
- **DD summary**: go/conditional/no-go + deal-breakers + owners + missing items.
- **Closing checklist**: mỗi CP/CD có id + nhóm + phụ trách + hạn + trạng thái + blocking + nguồn (Điều/khoản); dedup theo (counterparty + loại hành động); critical path tính đúng (`hạn − hôm nay < ước tính` = at-risk); không tự chứng nhận "sẵn sàng closing" (đó là kết luận pháp lý → `RE-Legal`).
- **Deal team briefing**: đúng altitude của tầng đối tượng (Board/Exec gọn 3–5 issue + quyết định; Working Team mới full chi tiết); surface quyết định, không tự quyết thay deal team; phân ranh rõ với `RE-HQ` (briefing trong một deal, không phải tổng hợp đa phòng executive).

## Mẫu kiểm tra nhanh

Với deliverable chính thức, **đính block này vào cuối deliverable** và ghi tóm tắt vào `_dossier.md` của deal — xem mục Verification trace trong `../../references/operating-contract.md`. Thiếu block = bản nháp chưa QC.

```md
## Kiểm tra trước khi chốt (Investment)
- Deliverable: ...
- Số đã tie-out với FS: có / không / n/a
- Calculated vs assumption vs external: đã phân biệt? ...
- Base/upside/downside + what-must-be-true: ...
- Nguồn + ngày cho external input: ...
- Hiệu lực pháp lý (qua specialist + tvpl): ...
- Có cần route `RE-HQ` không: ...
```

## Lỗi thường gặp

1. Trộn số tính toán với giả định, người đọc tưởng là chắc chắn.
2. Chỉ đưa base case, không sensitivity/downside.
3. Số trong report lệch với file FS.
4. Quên kiểm chứng hiệu lực pháp lý cho điểm trọng yếu.
5. Ôm quyết định đa phòng đáng ra route `RE-HQ`.
