---
name: re-legal-intake-router
description: Use when nhận task mới trong agent RE-Legal và cần phân loại lane xử lý, xác định deliverable, chọn skill bundle, hoặc quyết định khi nào phải route sang re-hq.
version: 1.0.0
license: MIT
---

# re-legal Intake Router

## Overview

Skill này là lớp điều phối đầu vào của agent `RE-Legal`.

Mục tiêu là giúp agent làm đúng 4 việc ngay từ đầu:
1. xác định task có thuộc phạm vi `RE-Legal` hay phải route sang `RE-HQ`;
2. xác định lane chuyên môn chính;
3. xác định deliverable cuối;
4. chọn load order và companion skill phù hợp.

`RE-Legal` là profile **specialist legal execution**. Vì vậy skill này phải ưu tiên phát hiện sớm các bài toán đã chuyển thành **cross-functional coordination** để không ôm sai vai.

## When to Use

Dùng skill này khi:
- Sếp giao task mới nhưng chưa rõ nên vào lane nào;
- task có thể là pháp lý dự án, hợp đồng, document ops hoặc phối hợp nhiều stream;
- cần xác định có nên giữ việc trong `RE-Legal` hay chuyển sang `RE-HQ`;
- cần chốt deliverable trước khi bắt đầu phân tích;
- cần chọn companion skill như `legal-writing`.

Do not use for:
- phân tích nội dung pháp lý sâu sau khi lane đã rõ hoàn toàn;
- review hợp đồng chi tiết từng điều khoản;
- approval path analysis chi tiết;
- thao tác rename / move file cụ thể.

## Routing Logic

### 1. Giữ task trong `RE-Legal` khi:
- trọng tâm là **phân tích pháp lý dự án**;
- trọng tâm là **approval path / permits / compliance**;
- trọng tâm là **review hợp đồng / clause risk / drafting support**;
- trọng tâm là **chuẩn hóa document set đầu vào ở mức cơ bản**;
- kết quả đầu ra chủ yếu là memo, issue list, legal report hoặc recommendation từ góc legal specialist.

### 2. Route sang `RE-HQ` khi:
- task là điều phối Rà Soát Thẩm Định (Due Diligence);
- task cần issue tracker nhiều workstream;
- task cần data room orchestration quy mô lớn;
- task là deal structuring hoặc transaction architecture nhiều nhánh quyết định;
- cần phối hợp legal với investment, finance, tax, project, operations hoặc nhiều bộ phận khác;
- legal chỉ là một stream trong tổng thể deal coordination.

### 3. Trường hợp hybrid
Nếu task có phần legal specialist và phần coordination:
- `RE-HQ` giữ vai trò điều phối;
- `RE-Legal` chỉ xử lý phần memo / analysis / issue note thuộc legal stream.

Khi gặp case này, phải nói rõ trong chat rằng việc điều phối thuộc `RE-HQ`, còn `RE-Legal` phụ trách phần phân tích pháp lý chuyên sâu.

## Intake Workflow

### Bước 1 — Xác định loại việc chính
Phân loại nhanh task vào một trong 4 nhóm:
- **Pháp lý dự án**: title, đất đai, quy hoạch, đầu tư, xây dựng, môi trường, PCCC, mở bán, chuyển nhượng dự án, approval path
- **Hợp đồng / giao dịch**: NDA, LOI, SPA, SHA, clause risk, negotiation note, dispute note, drafting support
- **Document ops**: rename, inventory, classify, move file ở quy mô nhỏ hoặc vừa
- **Coordination / đa stream**: DD, issue tracking, data room orchestration, structuring, cross-functional workflow

### Bước 2 — Xác định deliverable
Chốt deliverable trước khi phân tích. Danh mục mặc định gồm:
- memo;
- issue list;
- checklist;
- approval matrix;
- legal status report;
- clause summary;
- question list;
- recommendation note.

Nếu đề bài chưa nói rõ, chọn deliverable theo mục tiêu thực tế của task thay vì hỏi lại quá sớm.

### Bước 3 — Chọn specialist lane
- **Pháp lý dự án** → `licensing-expert`
- **Hợp đồng / giao dịch** → `legal-counsel`
- **Document ops** → `doc-renamer`
- **Coordination / đa stream** → route `RE-HQ`

### Bước 4 — Quyết định sequencing giữa các lane
Dùng các rule sau khi task có dấu hiệu mixed legal issue:

- **Project legal drives contract** → vào `licensing-expert` trước
  - dùng khi câu hỏi hợp đồng phụ thuộc điều kiện chuyển nhượng dự án, title, permit status, approval path, điều kiện mở bán hoặc regulatory feasibility.
- **Document clause drives issue spotting** → vào `legal-counsel` trước
  - dùng khi đầu bài xoay quanh clause wording, CP / closing mechanics, indemnity, liability allocation, termination hoặc negotiation position.
- **Mixed nhưng cần 2 legal views song song** → chốt rõ primary lane + secondary lane
  - primary lane chịu trách nhiệm kết luận chính;
  - secondary lane chỉ phát hành integration note hoặc issue note hỗ trợ.

### Bước 5 — Chọn companion skill
Mặc định gọi `re-legal-deliverable-templates` khi:
- deliverable cần chốt bằng template rõ ràng ngay từ đầu;
- output là hybrid package, blocker memo, CP-closing issue note hoặc document ops report;
- cần tránh việc specialist analysis xong rồi mới quay lại dựng format.

Mặc định gọi `legal-writing` khi:
- đầu ra là memo / report / legal letter / recommendation bằng tiếng Việt;
- cần polish lập luận, wording và kết luận;
- đầu ra dự kiến sẽ được dùng nội bộ hoặc gửi stakeholder.

Mặc định gọi `re-legal-verification-rules` khi:
- output dự kiến sẽ được chốt thành deliverable chính thức;
- task là hybrid legal package cho `RE-HQ`;
- vừa có một đợt refactor workflow và cần rà anti-drift ở lớp output.

Không nhất thiết gọi `legal-writing` khi:
- Sếp chỉ cần raw issue bullets rất ngắn;
- task chỉ là inventory hoặc rename;
- output mới là working notes tạm thời.

### Bước 6 — Kiểm tra dấu hiệu vượt scope
Trước khi bắt đầu xử lý sâu, rà lại xem task có dấu hiệu sau không:
- nhiều workstream song song;
- nhiều owner hoặc nhiều phòng ban;
- cần tracker / status management;
- cần phối hợp tiến độ ngoài legal;
- câu hỏi chuyển từ “legal analysis” sang “overall deal coordination”.

Nếu có, route `RE-HQ` ngay thay vì cố giữ việc trong `RE-Legal`.

### Bước 7 — Nếu là case hybrid, chốt legal output contract cho `RE-HQ`
Khi `RE-HQ` điều phối nhưng vẫn cần `RE-Legal` phát hành legal input, phải chốt rõ legal package theo một trong các dạng sau:
- **Project legal input** → legal status note / approval matrix / permit gap list / blocker memo từ `licensing-expert`
- **Corporate / transaction legal input** → contract review memo / clause issue list / CP-closing issue note từ `legal-counsel`
- **Missing docs / clarification support** → legal question list có cấu trúc, không biến thành tracker điều phối

Legal package tối thiểu nên trả lời được:
- issue là gì;
- căn cứ / hồ sơ chính;
- ảnh hưởng đến deal / dự án;
- blocker hay chỉ là point cần confirm;
- next step thuộc legal hay thuộc `RE-HQ`.

## Load Order Recommendation

### Case 1 — Pháp lý dự án
1. `re-legal-intake-router`
2. `licensing-expert`
3. `re-legal-deliverable-templates`
4. `legal-writing` nếu output cuối là memo / report tiếng Việt
5. `re-legal-verification-rules`

### Case 2 — Hợp đồng / giao dịch
1. `re-legal-intake-router`
2. `legal-counsel`
3. `licensing-expert` nếu issue hợp đồng phụ thuộc tình trạng pháp lý dự án
4. `re-legal-deliverable-templates`
5. `legal-writing` nếu output cuối là memo / recommendation tiếng Việt
6. `re-legal-verification-rules`

### Case 3 — Document ops
1. `re-legal-intake-router`
2. `doc-renamer`
3. `re-legal-deliverable-templates` nếu cần chốt `document-ops-report-template`
4. `re-legal-verification-rules` nếu output cần chốt chính thức

### Case 4 — Coordination / đa stream
1. `re-legal-intake-router`
2. xác nhận đây là việc phải route `RE-HQ`
3. nếu vẫn cần deliverable legal riêng, chỉ giữ phần specialist legal trong `RE-Legal`
4. nếu vừa sửa boundary hoặc workflow graph, cân nhắc `re-legal-skill-maintenance` để rà anti-drift

## Output Shape for Intake

Khi task chưa rõ lane, có thể trả lời bằng format intake ngắn sau:

```md
## Nhận diện task
- Lane chính: ...
- Có nằm trong scope `RE-Legal` không: Có / Không / Một phần
- Deliverable nên chốt: ...

## Hướng xử lý đề xuất
- Skill chính: ...
- Companion skill: ...
- Có cần route `RE-HQ` không: ...

## Lý do
- ...
```

## Language Rule

- Tên skill giữ bằng tiếng Anh theo convention của Codex.
- Body, workflow và SOP viết bằng tiếng Việt.
- Chỉ dùng tiếng Anh khi không có từ Việt tương đương tự nhiên hoặc cần giữ thuật ngữ chuẩn.
- Với thuật ngữ quan trọng, ưu tiên kiểu **Việt ngữ (Anh ngữ)** nếu giúp rõ nghĩa hơn.

## Common Pitfalls

1. Thấy từ “DD” rồi tự động ôm luôn trong `RE-Legal` dù bản chất là coordination.
2. Không chốt deliverable đầu ra nên phân tích lan man.
3. Load quá nhiều skill cùng lúc dù task thực ra chỉ có một lane rõ ràng.
4. Không gọi `legal-writing` cho memo/report tiếng Việt quan trọng, làm output thiếu polish.
5. Không phát hiện lúc task đã vượt khỏi specialist legal execution và đáng ra phải route `RE-HQ`.

## Verification Checklist

- [ ] Đã xác định task thuộc lane nào
- [ ] Đã xác định deliverable cuối
- [ ] Đã kiểm tra xem task có vượt scope `RE-Legal` không
- [ ] Đã chọn đúng specialist skill chính
- [ ] Đã cân nhắc `legal-writing` cho đầu ra tiếng Việt quan trọng
- [ ] Nếu task là hybrid, đã nêu rõ ranh giới giữa phần `RE-HQ` và phần `RE-Legal`
