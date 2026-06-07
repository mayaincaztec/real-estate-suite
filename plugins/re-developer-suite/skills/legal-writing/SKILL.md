---
name: legal-writing
description: Use when soạn hoặc rà soát công văn pháp lý, báo cáo pháp lý và các deliverable tiếng Việt cho licensing expert hoặc legal counsel workflows trong agent RE-Legal.
version: 1.2.0
license: MIT
---

# Legal Writing for Licensing — Vietnamese Professional Drafting

## Overview

Skill này dùng để soạn và rà soát **công văn pháp lý**, **báo cáo pháp lý** và các deliverable tiếng Việt khác trong agent `RE-Legal`. Mục tiêu là tạo ra văn bản:
- đúng mực;
- rõ việc;
- có judgment nghề;
- ít dấu vết AI;
- phù hợp vai specialist legal execution của `RE-Legal`.

Skill gồm 6 module companion:
1. `references/legal-drafting-cong-van.md` — soạn công văn pháp lý
2. `references/review-legal-cong-van.md` — rà soát công văn pháp lý
3. `references/legal-drafting-bao-cao.md` — soạn báo cáo pháp lý
4. `references/review-legal-bao-cao.md` — rà soát báo cáo pháp lý
5. `references/hybrid-specialist-input-drafting.md` — soạn specialist legal input cho HQ-led workflow
6. `references/hybrid-specialist-input-review.md` — rà specialist legal input trước khi gửi `RE-HQ`

## When to Use

- soạn công văn giải trình, bổ sung hồ sơ, đề nghị, phản hồi hoặc xin ý kiến;
- soạn báo cáo pháp lý về điều kiện cấp phép, legal status, issue / risk, licensing roadmap hoặc option analysis;
- soạn recommendation memo, issue memo, question list hoặc legal note tiếng Việt;
- rà soát draft legal tiếng Việt để bớt mùi AI nhưng vẫn giữ giọng pháp lý chuyên nghiệp;
- đóng vai companion skill cho `licensing-expert` hoặc `legal-counsel`.

Do not use for:
- redline hợp đồng clause-by-clause;
- opinion letter chuyên biệt ngoài scope profile;
- pure marketing content hoặc thought leadership;
- thay thế specialist analysis của `licensing-expert` hoặc `legal-counsel`.

## Routing

### 1. Dùng cùng `licensing-expert` khi:
- tài liệu gắn với giải trình thủ tục, hồ sơ cấp phép, approval path, legal status, compliance, điều kiện dự án hoặc permit gap analysis.

### 2. Dùng cùng `legal-counsel` khi:
- tài liệu là contract risk memo, negotiation memo, dispute brief, clause analysis, breach note hoặc transaction recommendation.

### 3. Dùng cùng `re-legal-intake-router` khi:
- đầu bài chưa rõ deliverable;
- cần xác định output có nên giữ trong `RE-Legal` hay đã thành bài toán coordination phải route `RE-HQ`.

### 4. Hai mode viết chính của operating model hiện tại
- **Standalone legal deliverable mode**
  - dùng cho memo, report, công văn, recommendation note hoặc issue list mà `RE-Legal` phát hành như deliverable độc lập cho Sếp.
- **HQ-specialist-input mode**
  - dùng khi output sẽ được `RE-HQ` nhúng vào DD report, structuring memo, IC note hoặc closing workflow;
  - mode này phải ưu tiên format ngắn, rõ owner boundary và tránh giọng coordination.

### 5. Không dùng skill này để ôm coordination
Nếu công việc đã chuyển thành điều phối Rà Soát Thẩm Định (Due Diligence), data room orchestration hoặc structuring nhiều phòng ban, skill này chỉ nên polish deliverable legal; phần coordination thuộc `RE-HQ`.

## Workflow

1. Xác định loại tài liệu: công văn, báo cáo, memo, issue list hay recommendation note.
2. Xác định vai nói: doanh nghiệp, specialist legal nội bộ, legal counsel hoặc phối hợp.
3. Xác định deliverable cuối và audience.
4. Chọn mode viết:
   - standalone legal deliverable;
   - HQ-specialist-input.
5. Load drafting module phù hợp.
6. Nếu nội dung liên quan thủ tục dự án / cơ quan / điều kiện pháp lý dự án, áp dụng cùng workflow của `licensing-expert`.
7. Nếu nội dung liên quan hợp đồng / risk allocation / đàm phán / tranh chấp, áp dụng cùng workflow của `legal-counsel`.
8. Nếu output sẽ được dùng trong HQ-led workflow, ưu tiên thêm `references/hybrid-specialist-input-drafting.md` để siết structure và owner boundary.
9. Soạn draft theo cấu trúc phù hợp.
10. Load review module tương ứng để làm sạch dấu vết AI, chuẩn hóa tiếng Việt và tăng độ nhất quán.
11. Với output gửi `RE-HQ`, rà thêm `references/hybrid-specialist-input-review.md` trước khi chốt.
12. Chỉ chốt bản cuối khi phần kết luận đã nêu rõ đề nghị, hướng xử lý hoặc bước tiếp theo.

Xem thêm: `references/department-application.md` để áp dụng skill này theo bối cảnh specialist legal team.

## Language Rule

Đây là rule chuẩn của `RE-Legal` ở phase hiện tại:
- tên skill giữ bằng tiếng Anh theo convention Codex;
- toàn bộ body, workflow và SOP viết bằng tiếng Việt;
- tiếng Anh chỉ dùng khi không có từ tiếng Việt tương đương tự nhiên hoặc cần giữ thuật ngữ chuyên ngành;
- với thuật ngữ quan trọng, ưu tiên kiểu **Việt ngữ (Anh ngữ)**, ví dụ: Rà Soát Thẩm Định (Due Diligence), Điều Kiện Tiên Quyết (Conditions Precedent), Điều Khoản Bồi Thường (Indemnity).

## Domain Adaptation Rule

Không bê nguyên một lớp review tiếng Việt phổ thông vào tài liệu pháp lý mà không chỉnh theo domain.

Quy tắc bền vững của skill này là:
- **công văn pháp lý** phải giữ tính chuẩn thức hành chính – pháp lý, cho phép dùng có kiểm soát các nhãn như `Kính gửi:`, `Căn cứ:`, `Nội dung như sau:`;
- **báo cáo pháp lý / memo pháp lý** phải giữ issue framing, judgment, risk articulation và recommendation có thể hành động;
- anti-AI cleanup dùng để loại bỏ cấu trúc đối xứng rỗng, câu dịch máy và filler chung chung, **không** phải để làm văn bản casual;
- thuật ngữ tiếng Anh có thể được giữ khi đó là ngôn ngữ chuẩn của hồ sơ, giao dịch hoặc audience.

## Response Packaging for This User

Khi trao đổi với Sếp trong chat về draft / review legal, không trả lời kiểu quá cụt hoặc chỉ nêu kết luận một dòng nếu bản chất câu hỏi đang cần giải thích.

Mặc định nên trình bày theo phong cách gần với Codex / Claude Code:
- mở bằng kết luận ngắn;
- theo sau là 1–3 đoạn hoặc bullet giải thích vì sao;
- dùng bullet khi cần scan nhanh, nhưng tránh biến mọi câu trả lời thành checklist khô cứng;
- với câu hỏi reasoning / troubleshooting / workflow, nên nêu rõ `kết luận → căn cứ → hệ quả / bước tiếp theo`.

## PDF Deliverable Mode

Khi Sếp yêu cầu báo cáo pháp lý hoặc memo ở dạng **PDF**, deliverable không hoàn tất ở bước soạn text. Skill này phải coi PDF là artifact cuối cần được tạo và xác minh thực tế.

Quy tắc thực hiện:
- ưu tiên dùng converter có sẵn nếu môi trường đã có;
- nếu không có converter quen thuộc nhưng có `node` / `npm`, có thể fallback sang render PDF bằng `pdf-lib` + `@pdf-lib/fontkit`;
- với Windows host, có thể tận dụng font hệ thống trong `C:\\Windows\\Fonts\\` để nhúng font tiếng Việt ổn định;
- phải kiểm tra file đầu ra tồn tại thật, có định dạng PDF hợp lệ và tên file chuyên nghiệp.

Xem thêm reference: `references/pdf-export-workflow.md`.

## Common Pitfalls

1. Trộn giọng công văn với giọng báo cáo trong cùng một tài liệu.
2. Chỉ paraphrase quy định mà không áp vào dữ kiện thực tế.
3. Dùng nhãn AI như Summary, Key Issue, Takeaway trong legal output tiếng Việt.
4. Lạm dụng bullet hoặc câu bị động để tạo vẻ trang trọng giả.
5. Không tách procedural note khỏi legal judgment.
6. Không phân định rõ phần kết luận thuộc `licensing-expert` hay `legal-counsel`.
7. Không phát hiện lúc deliverable legal thực chất chỉ là một phần của workflow coordination thuộc `RE-HQ`.
8. Viết chat reply quá ngắn và quá cộc, làm đúng ý nhưng tạo cảm giác máy móc.

## Verification Checklist

- [ ] Đã chọn đúng module theo loại tài liệu
- [ ] Vai nói nhất quán từ đầu đến cuối
- [ ] Thuật ngữ pháp lý và procedural được dùng nhất quán
- [ ] Văn bản đủ formal nhưng không máy móc
- [ ] Kết luận / đề nghị đủ cụ thể để hành động
- [ ] Nếu là licensing / procedural memo: đã kiểm tra thẩm quyền, hiệu lực văn bản, địa phương và bước thủ tục theo `licensing-expert`
- [ ] Nếu là counsel / transaction memo: đã xác định đúng client-side, risk allocation, fallback và deliverable theo `legal-counsel`
- [ ] Nếu task đã thành coordination đa stream, đã giữ skill này ở vai trò companion thay vì ôm luôn phần điều phối
