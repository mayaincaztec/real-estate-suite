---
name: deal-structuring-advisor
description: Use when điều phối bài toán deal structuring, transaction architecture hoặc cross-functional decision design ở workflow RE-HQ; chỉ huy động re-legal khi cần legal assessment chuyên sâu về dự án, corporate, governance hoặc transaction documents.
version: 3.0.0
license: MIT
---

> **Lưu ý kiểm chứng:** Tài liệu này được migrate từ thư viện nghiệp vụ cũ. Mọi quy định, thuế suất, ngưỡng, thủ tục và cơ quan có thẩm quyền phải được kiểm tra lại bằng nguồn chính thức còn hiệu lực tại ngày sử dụng.

# Deal Structuring Advisor

## Overview

Trong workflow `RE-HQ`, skill này là **coordination skill** cho bài toán cấu trúc giao dịch, transaction architecture và decision design nhiều phòng ban.

Vai trò của skill này là:
- xác định các cấu trúc khả thi;
- điều phối đầu vào từ legal, tax, finance, investment, operations và commercial;
- so sánh các option theo tiêu chí thống nhất;
- chốt recommendation về cấu trúc giao dịch ở cấp điều phối.

Skill này **không tự thay specialist legal analysis**. Khi cần ý kiến pháp lý chuyên sâu, phải huy động specialist phù hợp ở agent `RE-Legal`.

## When to Use

Dùng skill này khi:
- cần so sánh share deal / asset deal / JV / minority investment / SPV structure;
- cần recommendation về governance, sequencing, approvals, exit structure;
- cần điều phối đầu vào legal + tax + finance + investment để ra cấu trúc tối ưu;
- legal chỉ là một phần của overall structuring decision.

Do not use for:
- review hợp đồng một stream;
- legal status review dự án độc lập;
- permit / approval path analysis độc lập;
- memo pháp lý chuyên sâu không gắn với overall structuring.

## Specialist Pull Rule

Chỉ huy động `RE-Legal` khi cần **legal assessment chuyên sâu** để hỗ trợ structuring.

### Map legal request sang specialist ở `RE-Legal`
- **Regulatory feasibility / project-side legal constraints** → gọi `licensing-expert`
  - ví dụ: điều kiện chuyển nhượng dự án, title / permit blockers, approval path, khả năng mở bán, khả năng huy động vốn, hạn chế pháp lý đối với asset / project.
- **Corporate legal / governance / transaction document implications** → gọi `legal-counsel`
  - ví dụ: shareholder rights, governance design, SPA / SHA / JVA implications, change-of-control clauses, allocation of liability, CP / closing structure.
- **Cần polish legal recommendation bằng tiếng Việt** → sau khi legal specialist hoàn tất, có thể yêu cầu `legal-writing` trong `RE-Legal`.

Nguyên tắc: `RE-HQ` thiết kế cấu trúc tổng thể; `RE-Legal` chỉ cung cấp legal input chuyên sâu theo từng nhánh.

## Workflow

### Bước 1 — Chốt bài toán structuring
Xác định rõ:
- loại giao dịch đang cân nhắc;
- buyer / investor profile;
- asset / target / project scope;
- mục tiêu chính: thuế, tốc độ, control, clean risk allocation, exit flexibility;
- các phòng ban hoặc stream phải tham gia.

### Bước 2 — Dựng option set
Chọn 2–4 cấu trúc khả thi để so sánh, ví dụ:
- share deal trực tiếp;
- asset deal;
- SPV / holding structure;
- JV / minority structure.

### Bước 3 — Huy động specialist inputs
Điều phối inputs tối thiểu từ:
- legal;
- tax;
- finance;
- investment / deal team;
- operations / project nếu cần.

Với legal stream:
- gọi `licensing-expert` khi câu hỏi là project legal feasibility / regulatory constraints;
- gọi `legal-counsel` khi câu hỏi là governance / corporate / transaction document implications.

### Bước 4 — So sánh đa tiêu chí
Chuẩn hóa ma trận so sánh theo các tiêu chí như:
- legal feasibility;
- tax burden;
- execution timeline;
- governance / control;
- financing implications;
- exit flexibility;
- implementation complexity.

### Bước 5 — Chốt recommendation và sequencing
Kết luận rõ:
- cấu trúc ưu tiên;
- cấu trúc fallback;
- điều kiện tiên quyết;
- approvals / consents cần có;
- phần việc follow-up theo từng phòng ban.

## Output Shapes

### 1. Structuring Option Matrix
```md
## Structuring Option Matrix
- Deal objective: ...
- Options compared: ...
- Legal input owner from `RE-Legal`: ...
- Tax / finance owners: ...
- Preferred structure: ...
- Key reasons: ...
- Key blockers / next steps: ...
```

### 2. Structuring Recommendation Note
```md
## Structuring Recommendation Note
- Recommended structure: ...
- Why this structure wins: ...
- Legal constraints needing confirmation from `RE-Legal`: ...
- Governance / document implications: ...
- Required approvals / sequencing: ...
- Next actions by owner: ...
```

## References

- `references/structuring-tax-guide.md`

## Common Pitfalls

1. Biến `deal-structuring-advisor` thành legal memo writer thay vì coordinator.
2. Gọi `RE-Legal` quá sớm khi câu hỏi legal còn mơ hồ.
3. Không tách project-side legal constraints với corporate / governance implications.
4. Chốt cấu trúc dựa trên một tiêu chí đơn lẻ mà bỏ qua execution reality.
5. Đẩy phần architecting tổng thể sang `RE-Legal` thay vì giữ ở `RE-HQ`.

## Verification Checklist

- [ ] Đã giữ vai trò structuring coordinator ở `RE-HQ`
- [ ] Project legal feasibility đã map sang `licensing-expert` khi cần
- [ ] Corporate / governance / transaction legal implications đã map sang `legal-counsel` khi cần
- [ ] Option matrix đã phản ánh input đa phòng ban, không chỉ legal
- [ ] Recommendation cuối đã có owner / sequencing / next step rõ ràng
