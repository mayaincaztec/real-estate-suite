---
name: re-legal-operations
description: Use to operate the RE-Legal bundle for a new legal task — triage the lane (project legal, contracts, document ops, or out-of-scope coordination), pick the primary skill, deliverable template, verification step, and escalation path. Single operations layer combining intake routing, the operating matrix, and the deliverable-template map.
version: 1.0.0
license: MIT
---

# RE-Legal Operations (intake → matrix → template)

## Tổng quan

Lớp vận hành duy nhất của `RE-Legal`: nhận task mới → chốt lane và deliverable → chọn primary skill + template + verification → quyết định escalation. Skill này thay thế ba lớp cũ (intake router, operating matrix, deliverable templates) để routing chỉ sống ở **một chỗ**.

`RE-Legal` là profile **specialist legal execution**. Việc đầu tiên của lớp này là phát hiện sớm task đã thành **coordination** để không ôm sai vai.

## Khi nào dùng

Dùng khi: Sếp giao task pháp lý mới chưa rõ lane; cần chọn nhanh skill + template + QC; cần chốt deliverable trước khi phân tích; cần quyết định giữ trong `RE-Legal` hay route ra ngoài.

Không dùng cho: phân tích pháp lý sâu sau khi lane đã rõ (vào thẳng specialist); thay specialist analysis; ôm coordination nhiều workstream.

## Bước 1 — Intake: phân loại và kiểm tra scope

Phân loại task vào một trong 4 nhóm:

- **Pháp lý dự án**: title, đất đai, quy hoạch, đầu tư, xây dựng, môi trường, PCCC, mở bán, chuyển nhượng dự án, approval path → `re-legal-licensing`
- **Hợp đồng / giao dịch**: NDA, LOI, SPA, SHA, clause risk, negotiation note, dispute note, drafting support → `re-legal-counsel`
- **Document ops**: rename, inventory, classify, move file quy mô nhỏ/vừa → `re-legal-doc-renamer`
- **Coordination / đa stream**: → route ra ngoài `RE-Legal` (xem dưới)

**Route ra ngoài `RE-Legal`** ngay khi thấy các dấu hiệu: nhiều workstream song song, nhiều owner, cần tracker / status management, cần phối hợp tiến độ ngoài legal:

- DD coordination → `RE-Investment-Finance` (`re-inv-dd-coordinator`);
- deal structuring / transaction architecture / LOI → `RE-Investment-Finance` (`re-inv-deal-structuring`);
- issue tracker nhiều workstream / data room orchestration của một thương vụ → `RE-Investment-Finance`;
- tổng hợp đa phòng (legal + investment + market + design) ở **tầm quyết định executive** → `RE-HQ`.

Doctrine đầy đủ: `../../references/routing-map.md`. Case hybrid: owner điều phối là `RE-Investment-Finance` (deal lifecycle) hoặc `RE-HQ` (executive synthesis); `RE-Legal` chỉ phát hành phần specialist legal — nói rõ ranh giới này trong chat.

**Chốt deliverable trước khi phân tích.** Danh mục mặc định: memo; issue list; checklist; approval matrix; legal status report; clause summary; question list; recommendation note. Nếu đề bài chưa nói rõ, chọn theo mục tiêu thực tế thay vì hỏi lại quá sớm.

## Bước 2 — Ma trận vận hành

| Loại việc | Primary skill | Companion | Template / output | Verification | Escalation trigger |
|---|---|---|---|---|---|
| Legal status review | `re-legal-licensing` | `re-legal-writing` | `legal-status-report-template` | `re-legal-verification-rules` | task thành DD coordination / multi-owner tracker |
| Approval path / thủ tục | `re-legal-licensing` | `re-legal-writing` | `approval-matrix-template` | `re-legal-verification-rules` | approval strategy phụ thuộc coordination nhiều phòng |
| Permit / compliance gap | `re-legal-licensing` | `re-legal-writing` | `permit-gap-list-template` | `re-legal-verification-rules` | gap remediation cần cross-functional program |
| Điều kiện mở bán / chuyển nhượng / huy động vốn | `re-legal-licensing` | `re-legal-writing` | `recommendation-memo-template` hoặc `permit-gap-list-template` | `re-legal-verification-rules` | kết luận phụ thuộc structuring / DD tổng thể |
| NDA / LOI / Term Sheet review | `re-legal-counsel` | `re-legal-writing` | `clause-issue-list-template` hoặc `contract-review-memo-template` | `re-legal-verification-rules` | review thành overall deal coordination |
| SPA / SHA / JVA / project transfer review | `re-legal-counsel` | `re-legal-licensing`, `re-legal-writing` | `contract-review-memo-template` | `re-legal-verification-rules` | drafting/signing phụ thuộc DD / structuring đa stream |
| Clause scan nhanh | `re-legal-counsel` | — hoặc `re-legal-writing` | `clause-issue-list-template` | `re-legal-verification-rules` | issue thật ra là project legal blocker |
| Recommendation legal note | `re-legal-licensing` hoặc `re-legal-counsel` | `re-legal-writing` | `recommendation-memo-template` | `re-legal-verification-rules` | recommendation cần deal decision framework tổng thể |
| Legal question list / missing docs | `re-legal-licensing` hoặc `re-legal-counsel` | — hoặc `re-legal-writing` | `legal-question-list-template` | `re-legal-verification-rules` | question list đã thành request tracker nhiều owner |
| Rename / inventory / classify / move nhẹ | `re-legal-doc-renamer` | — | `document-ops-report-template` | `re-legal-verification-rules` nếu cần chốt | thành data room orchestration / multi-team flow |
| Hybrid legal input — project stream | `re-legal-licensing` | `re-legal-writing` hoặc — | `hybrid-legal-package-template` / `blocker-memo-template` / `legal-question-list-template` | `re-legal-verification-rules` | package phình thành multi-owner tracker / DD coordination |
| Hybrid legal input — corporate / transaction stream | `re-legal-counsel` | `re-legal-writing` hoặc — | `hybrid-legal-package-template` / `cp-closing-issue-note-template` / `legal-question-list-template` | `re-legal-verification-rules` | package phình thành closing coordination / structuring framework |
| Transaction legal DD (bộ tài liệu / data room) | `re-legal-counsel` | `re-legal-licensing` (project-legal), `re-legal-writing` | `transaction-dd-findings-memo` (+ `clause-review-grid`, `material-contract-schedule`) | `re-legal-verification-rules` | điều phối DD đa stream → `re-inv-dd-coordinator` |
| Soạn văn kiện phê duyệt nội bộ (nghị quyết/biên bản) | `re-legal-counsel` | `re-legal-writing` | `corporate-resolution-vn` | `re-legal-verification-rules` | quyết định cấu trúc/giao dịch tổng thể → `re-inv-deal-structuring` |

Template nằm ở `../../templates/`.

## Bước 3 — Sequencing khi task là mixed legal issue

- **Project legal drives contract** → vào `re-legal-licensing` trước: khi câu hỏi hợp đồng phụ thuộc điều kiện chuyển nhượng dự án, title, permit status, approval path, điều kiện mở bán hoặc regulatory feasibility.
- **Document clause drives issue spotting** → vào `re-legal-counsel` trước: khi đầu bài xoay quanh clause wording, CP / closing mechanics, indemnity, liability allocation, termination hoặc negotiation position.
- **Cần 2 legal views song song** → chốt rõ primary lane (chịu trách nhiệm kết luận chính) + secondary lane (chỉ phát hành integration note / issue note hỗ trợ).

## Bước 4 — Companion skill

- Gọi `re-legal-writing` khi đầu ra là memo / report / legal letter / recommendation tiếng Việt quan trọng, cần polish lập luận và wording. Không cần khi Sếp chỉ cần raw issue bullets, inventory/rename, hoặc working notes tạm.
- Gọi `re-legal-verification-rules` trước khi chốt mọi deliverable chính thức.

## Quy tắc chọn template

- `legal-status-report-template` — view tổng quan tình trạng pháp lý dự án/tài sản (facts → legal basis → assessment → action).
- `approval-matrix-template` — map thủ tục, thẩm quyền, hồ sơ, điều kiện, next step theo mốc pháp lý.
- `permit-gap-list-template` — hồ sơ thiếu gì, rủi ro từng khoảng trống, việc cần làm tiếp.
- `contract-review-memo-template` — review memo đầy đủ cho hợp đồng / tài liệu giao dịch.
- `clause-issue-list-template` — scan nhanh theo clause, issue, risk, proposal, priority.
- `legal-question-list-template` — hồ sơ thiếu nhiều facts, output chính là danh sách câu hỏi / yêu cầu làm rõ.
- `recommendation-memo-template` — chốt hướng xử lý, option comparison, go / conditional go / no-go.
- `hybrid-legal-package-template` — output gửi owner điều phối deal (`RE-Investment-Finance`, hoặc `RE-HQ` ở tầm executive) để nhúng vào DD / structuring / IC memo; format issue → basis → impact → blocker/confirm-point → next step → owner boundary.
- `blocker-memo-template` — một blocker pháp lý dự án đang chặn transferability, commercialization, DD conclusion hoặc structuring path.
- `cp-closing-issue-note-template` — CP, closing deliverables, signing–closing gap, legal dependency ảnh hưởng việc đóng giao dịch.
- `transaction-dd-findings-memo` — trích issue pháp lý từ bộ tài liệu giao dịch theo nhóm + materiality + severity (legal input cho `re-inv-dd-coordinator`); kèm `clause-review-grid` (rà hàng loạt hợp đồng) và `material-contract-schedule` (danh mục HĐ trọng yếu).
- `corporate-resolution-vn` — nghị quyết/biên bản HĐQT/ĐHĐCĐ/HĐTV phê duyệt giao dịch theo Luật Doanh nghiệp 2020 (luôn DRAFT để rà soát).
- `document-ops-report-template` — chốt kết quả document ops có cấu trúc.

Bản nháp nhanh có thể neo theo: `hybrid-legal-package-short-example.md`, `blocker-memo-short-example.md`, `document-ops-report-short-example.md` (cùng thư mục `../../templates/`).

## Hợp đồng output cho hybrid package

Khi owner điều phối cần `RE-Legal` phát hành legal input, package tối thiểu phải trả lời: issue là gì; căn cứ / hồ sơ chính; ảnh hưởng đến deal / dự án; blocker hay chỉ là point cần confirm; next step thuộc legal hay thuộc owner điều phối.

## Dạng đầu ra intake (khi task chưa rõ lane)

```md
## Nhận diện task
- Lane chính: ...
- Có nằm trong scope `RE-Legal` không: Có / Không / Một phần
- Deliverable nên chốt: ...

## Hướng xử lý đề xuất
- Skill chính: ...
- Companion skill: ...
- Có cần route `RE-Investment-Finance` / `RE-HQ` không: ...

## Lý do
- ...
```

## Quy tắc đồng bộ

Khi đổi boundary hoặc workflow của bundle `RE-Legal`, so đồng bộ: entry `re-legal`; skill này; `re-legal-verification-rules`; specialist skill liên quan; `../../references/routing-map.md` nếu boundary với `RE-HQ` / `RE-Investment-Finance` bị tác động.

## Lỗi thường gặp

1. Thấy từ "DD" rồi ôm luôn trong `RE-Legal` dù bản chất là coordination (→ `RE-Investment-Finance`).
2. Không chốt deliverable nên phân tích lan man.
3. Load nhiều skill cùng lúc dù task chỉ có một lane rõ ràng.
4. Chọn đúng skill nhưng quên template hoặc verification layer.
5. Dùng report template cho câu hỏi chỉ cần issue list ngắn.
6. Không gọi `re-legal-writing` cho memo/report tiếng Việt quan trọng.

## Checklist kiểm tra

- [ ] Đã xác định lane và deliverable cuối
- [ ] Đã kiểm tra dấu hiệu vượt scope (coordination → `RE-Investment-Finance`; executive synthesis → `RE-HQ`)
- [ ] Đã chọn đúng primary skill + template / output shape
- [ ] Đã cân nhắc `re-legal-writing` cho đầu ra tiếng Việt quan trọng
- [ ] Đã chạy `re-legal-verification-rules` trước khi chốt
- [ ] Nếu hybrid, đã nêu rõ owner boundary
