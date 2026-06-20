---
name: re-inv-dd-coordinator
description: Use to coordinate multi-workstream due diligence (DD) in RE-Investment-Finance — DD scope, document request list, data room tracker with new-upload triage, clarification log, issue tracker, closing checklist (conditions precedent and closing deliverables), and the consolidated DD findings report; pulls RE-Legal specialists only for deep legal findings.
version: 3.0.0
license: MIT
---

# DD Coordinator

## Tổng quan

Trong workflow `RE-Investment-Finance`, skill này là **orchestration skill** cho Rà Soát Thẩm Định (Due Diligence) nhiều workstream. Phòng Đầu tư (deal team) chạy DD; chỉ route `RE-HQ` khi DD bắc cầu một quyết định đa phòng cấp executive.

Vai trò của skill này là:
- xác định scope DD và workstreams;
- dựng DRL, data room tracker, clarification log, issue tracker và DD timeline;
- điều phối đầu vào từ các nhóm legal, financial, tax, technical, commercial và vận hành;
- tổng hợp findings thành DD report và recommendation cho cấp điều phối.

Skill này **không tự làm sâu toàn bộ legal analysis**. Khi cần findings pháp lý chuyên sâu, phải huy động specialist phù hợp ở agent `RE-Legal`.

## Khi nào dùng

Dùng skill này khi:
- cần điều phối DD nhiều workstream;
- cần DRL hoặc data room tracker;
- cần clarification tracker với seller / counterparty;
- cần issue list nhiều owner;
- cần DD findings report hoặc executive summary tổng hợp;
- legal chỉ là một stream trong chương trình DD tổng thể.

Không dùng cho:
- legal status review một stream;
- clause review hoặc contract memo một stream;
- approval path analysis độc lập;
- document ops nhẹ không cần multi-team coordination.

## Quy tắc kéo chuyên môn

Chỉ huy động `RE-Legal` khi cần **nội dung đánh giá pháp lý chuyên sâu**.

### Map legal request sang specialist ở `RE-Legal`
- **Key Findings DD về pháp lý dự án** → gọi `re-legal-licensing`
  - ví dụ: đất đai, quy hoạch, đầu tư, xây dựng, môi trường, PCCC, điều kiện mở bán, chuyển nhượng dự án, permit gaps.
- **Key Findings DD về pháp lý công ty / corporate legal / transaction documents** → gọi `re-legal-counsel`
  - ví dụ: corporate status, shareholder arrangements, material contracts, financing documents, dispute exposure, change-of-control implications.
  - `re-legal-counsel` rà bộ tài liệu theo `transaction-dd-playbook` (nhóm vấn đề + materiality + severity, tabular review cho hợp đồng hàng loạt) và trả `transaction-dd-findings-memo`; coordinator điều phối, không tự làm legal extraction.
- **Cần polish legal memo tiếng Việt** → sau khi specialist legal xong, có thể yêu cầu `re-legal-writing` trong `RE-Legal`.

Nguyên tắc: `RE-Investment-Finance` điều phối DD; `RE-Legal` phát hành legal analysis chuyên sâu theo từng lane.

## Quy trình

### Bước 1 — Xác định scope DD
Chốt tối thiểu:
- loại giao dịch: share deal / asset deal / JV / minority investment;
- đối tượng: dự án, công ty, nhóm tài sản hay platform;
- workstreams cần mở;
- timeline và mốc quyết định;
- stakeholders / owners theo từng workstream.

### Bước 2 — Dựng control layer
Thiết lập các lớp điều phối phù hợp:
- DRL;
- data room tracker (kèm **new-upload triage** — xem dưới);
- clarification tracker;
- issue tracker;
- closing checklist (CP/CD — xem Bước 7);
- DD timeline / milestone view.

Không yêu cầu mọi task đều phải có đủ tất cả lớp; chọn theo quy mô deal.

**New-upload triage (on-demand, không phải cron):** khi data room có tài liệu mới, đối chiếu thời điểm rà gần nhất → liệt kê tài liệu thêm từ lần trước; map vào nhóm theo DRL; **cờ ưu tiên cao** cho 3 nhóm: hợp đồng trọng yếu (Material Contracts), tranh chấp/tố tụng (Litigation), sở hữu trí tuệ (IP). Output: số tài liệu mới + breakdown theo nhóm ưu tiên (kèm tên file) + phần còn lại theo nhóm. Skill này **chỉ cờ để người rà**, không đọc nội dung — đọc & trích issue là việc của `re-legal-counsel` (theo `transaction-dd-playbook`).

### Bước 3 — Phân luồng yêu cầu theo workstream
Tách rõ:
- legal;
- financial / tax;
- technical / construction;
- commercial / market;
- operations / HR / compliance khác nếu có.

Với legal stream, chỉ gửi brief chuyên sâu sang `RE-Legal` khi câu hỏi đã được xác định đủ cụ thể.

### Bước 4 — Huy động legal stream từ `RE-Legal` khi cần
Khi legal findings là một phần của DD report:
- gửi yêu cầu **pháp lý dự án** sang `re-legal-licensing`;
- gửi yêu cầu **pháp lý công ty / corporate legal / transaction documents** sang `re-legal-counsel`;
- không yêu cầu `RE-Legal` điều phối toàn bộ DD.

### Bước 5 — Tổng hợp findings đa phòng ban
Chuẩn hóa output về cùng cấu trúc:
- issue;
- severity;
- evidence / source;
- business impact;
- recommendation / mitigation;
- owner / next step.

### Bước 6 — Chốt DD recommendation
Kết luận rõ:
- go / conditional go / no-go;
- key deal breakers;
- key conditions precedent / remedial actions;
- missing items còn treo;
- action owners sau DD.

### Bước 7 — Closing checklist (CP/CD)
Khi deal tiến tới ký/closing, dựng **closing checklist** theo `../../templates/closing-checklist.md`:
- **CP** (điều kiện tiên quyết): regulatory approval, third-party consent, điều kiện hợp đồng — mỗi item có id (CP-###), nhóm, phụ trách, hạn, trạng thái, blocking, nguồn (Điều/khoản), ước tính hoàn tất.
- **CD** (deliverables tại closing): chứng nhận, opinion, nghị quyết HĐQT/ĐHĐCĐ, giấy tờ.
- **Tự cập nhật từ** findings DD (mọi finding hàm ý hành động trước closing), `material-contract-schedule` (CoC/anti-assignment) và `cp-closing-issue-note` của `re-legal`. **Dedup theo (counterparty + loại hành động)**, không theo tên tự do.
- **Critical path:** với item blocking, `(hạn − hôm nay) < ước tính hoàn tất` → at-risk; báo cáo 3 tầng 🔴 at-risk / 🟡 đúng tiến độ / ✅ hoàn tất.
- Chứng nhận "sẵn sàng closing" là kết luận pháp lý → kéo `re-legal`; coordinator chỉ giữ tracker + báo cáo trạng thái.

## Dạng đầu ra

### 1. DD Coordination Snapshot
```md
## DD Coordination Snapshot
- Deal / Asset: ...
- Workstreams mở: ...
- Trạng thái data room: ...
- Critical missing items: ...
- Legal stream cần huy động từ `RE-Legal`: ...
- Key blockers / next steps: ...
```

### 2. DD Findings Summary
```md
## DD Findings Summary
- Overall recommendation: Go / Conditional Go / No-Go
- Deal breakers: ...
- Major issues: ...
- Legal findings owner: `RE-Legal` / specialist tương ứng
- Other workstream owners: ...
- Next actions: ...
```

### 3. Closing Checklist Status
Theo `../../templates/closing-checklist.md` — báo cáo 3 tầng (🔴 blocking at-risk / 🟡 blocking on-track / ✅ complete) + critical path + days-to-close + đếm theo trạng thái.

### 4. New-Upload Triage
```md
## Data room — tài liệu mới (từ [ngày rà trước])
- Tổng mới: [n]
- Ưu tiên cao: Material Contracts [..files], Litigation [..files], IP [..files]
- Còn lại theo nhóm: ...
- Cần `re-legal-counsel` đọc & trích issue: ...
```

## Deal dossier

Đọc `deals/<deal-id>/_dossier.md` khi bắt đầu (giai đoạn, findings, câu hỏi mở từ các bước trước); trong quá trình DD, ghi findings trọng yếu và issue còn treo vào dossier; khi chốt DD, cập nhật recommendation go/conditional/no-go và deal-breakers.

## References

- `references/dd-document-request-templates.md`

## Lỗi thường gặp

1. Biến `re-inv-dd-coordinator` thành legal specialist thay vì coordinator.
2. Kéo `RE-Legal` vào điều phối tổng thể thay vì chỉ yêu cầu legal findings chuyên sâu.
3. Gửi brief legal quá mơ hồ, làm specialist phải tự đoán scope.
4. Trộn findings giữa các workstream mà không gắn owner rõ ràng.
5. Chốt recommendation khi critical missing items vẫn chưa được flag.

## Checklist kiểm tra

- [ ] Đã tách rõ coordination layer với specialist legal layer
- [ ] Legal project findings đã map sang `re-legal-licensing` khi cần
- [ ] Legal corporate / transaction findings đã map sang `re-legal-counsel` khi cần
- [ ] DD report đã gắn owner / next step theo từng issue
- [ ] Không đẩy vai điều phối tổng thể sang `RE-Legal`
