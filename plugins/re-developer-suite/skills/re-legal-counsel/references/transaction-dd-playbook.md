# Transaction Legal DD Playbook — rà soát bộ tài liệu giao dịch

> Phương pháp trích issue pháp lý từ **bộ tài liệu giao dịch** (data room / contract portfolio) cho M&A và chuyển nhượng dự án BĐS. Đây là **legal stream chuyên sâu** mà `re-inv-dd-coordinator` kéo về — `re-legal-counsel` phát hành findings, **không** ôm điều phối DD đa workstream (việc đó thuộc `RE-Investment-Finance`).
>
> Adapt từ phương pháp diligence-issue-extraction + tabular-review của bộ corporate-legal, chuẩn hóa cho bối cảnh pháp lý VN.

## Phân vai với các skill khác

- **Project-legal DD** (đất đai, quy hoạch, đầu tư, xây dựng, môi trường, PCCC, điều kiện mở bán/chuyển nhượng dự án) → kéo `re-legal-licensing` (đã có khung 10 lớp). Playbook này **không lặp** các lớp đó.
- **Điều phối DD** (DRL, data room tracker, issue tracker đa stream, DD report tổng) → `re-inv-dd-coordinator`.
- Playbook này lo **corporate & transaction-document legal DD**: tư cách chủ thể, vốn/cổ phần, điều lệ & quản trị, hợp đồng trọng yếu, lao động, tranh chấp, nghĩa vụ tài chính/thuế ở góc pháp lý, SHTT.

## Nhóm vấn đề (issue categories) — bộ rà chuẩn

**1. Chủ thể & quản trị doanh nghiệp**
- Cơ cấu vốn góp / cổ phần, option/warrant đang lưu hành, tính nhất quán giữa điều lệ – sổ đăng ký – GCN ĐKDN.
- Thẩm quyền phê duyệt giao dịch (HĐQT / ĐHĐCĐ / chủ sở hữu) và các giao dịch cần phê duyệt đặc biệt.
- Ràng buộc trong SHA/điều lệ: drag-along, tag-along, ROFR/ROFO, quyền phủ quyết, hạn chế chuyển nhượng.
- Cấu trúc công ty con & giao dịch nội bộ (intercompany).

**2. Hợp đồng trọng yếu (material contracts)**
- **Change-of-control** & điều kiện cần consent khi đổi chủ.
- Hạn chế chuyển nhượng / assignment.
- Độc quyền / non-compete; điều khoản **MFN** về giá.
- Quyền chấm dứt gắn với giao dịch.
- Indemnity bất thường hoặc nghĩa vụ trách nhiệm vượt mức.
- (Chi tiết dấu hiệu từng loại: `transaction-clause-checklists.md`.)

**3. Lao động**
- Trigger trợ cấp/severance khi change-of-control; chi phí "parachute".
- Rủi ro giữ chân nhân sự chủ chốt (key person).
- Tranh chấp lao động đang chờ; rủi ro phân loại NLĐ/nhà thầu.

**4. Tranh chấp & tố tụng**
- Vụ việc đang chờ + dự phòng tài chính; khiếu nại đe dọa; điều tra của cơ quan quản lý; tranh chấp lặp lại theo mẫu.

**5. Nghĩa vụ tài chính & thuế (góc pháp lý)**
- Nghĩa vụ tiền sử dụng đất/thuê đất, thuế phí còn treo, nợ/cưỡng chế; rủi ro **successor liability** (xem cờ riêng bên dưới).

**6. Sở hữu trí tuệ**
- Quyền với thương hiệu dự án/nhãn hiệu; chuỗi sở hữu; license vs owned; tranh chấp SHTT.

> Bổ sung/cắt nhóm theo loại giao dịch (share deal / asset deal / chuyển nhượng dự án). Đất–quy hoạch–permit để `re-legal-licensing` phụ trách, gắn cross-reference thay vì tự kết luận.

## Logic materiality (ngưỡng trọng yếu)

- Áp ngưỡng theo bối cảnh giao dịch (giá trị hợp đồng, tầm quan trọng counterparty) — lấy từ handoff packet / deal dossier, **không tự bịa ngưỡng**.
- Với hợp đồng: sắp theo giá trị/độ quan trọng đối tác; rà từ trên xuống đến khi đạt ngưỡng hoặc hết nhóm. Không audit mọi tài liệu nếu ngưỡng đã loại.
- Nêu rõ ngưỡng đã dùng trong phần mở đầu findings.

## Quy trình 5 bước

1. **Kiểm kê data room** — lấy index tài liệu; map thư mục vào nhóm vấn đề; **ghi rõ khoảng trống coverage** (thiếu nhóm nào).
2. **Lọc theo materiality** — áp ngưỡng; ưu tiên hợp đồng theo giá trị/đối tác; dừng khi đạt ngưỡng.
3. **Trích issue** — đọc từng tài liệu theo bộ rà chuẩn của nhóm; áp **Quote-First Protocol** (trích nguyên văn cho claim dương tính; với claim âm tính "không có điều khoản X" phải thử nhiều biến thể trước khi chốt). Nhiều tài liệu cùng loại → dùng **tabular review** (xem dưới).
4. **Phát biểu từng finding** theo format bắt buộc; **không tự lấp khoảng trống** bằng suy đoán; văn bản luật viện dẫn phải kiểm chứng hiệu lực qua `tvpl` (`../../../references/tvpl-lookup-protocol.md`) hoặc gắn caveat "chưa kiểm chứng".
5. **Tổng hợp theo nhóm** — gom theo category, trong nhóm sắp theo severity; thêm bottom-line + mục khoảng trống (gaps).

## Format finding (trường bắt buộc)

```
Finding #N: [Tiêu đề]
Nhóm: [category]
Mức độ: 🔴 / 🟠 / 🟡 / 🟢   (xem thang dưới)
Tài liệu: [đường dẫn data room + tên tài liệu] (+ Điều/khoản)
Trích dẫn: "<nguyên văn điều khoản then chốt>"
Nội dung: [tài liệu nói gì và vì sao quan trọng cho giao dịch]
Kiểm chứng luật: [tvpl: tình trạng + ngày | hoặc "chưa kiểm chứng"]
Khuyến nghị: [điều chỉnh giá / indemnity / yêu cầu consent / rep & warranty / CP / walk-away]
Owner / next step: [bên chịu trách nhiệm + bước tiếp]
```

Format này tương thích finding schema trong `../../../references/operating-contract.md` — giữ Status (confirmed/inferred/assumed/unresolved) khi bàn giao cho `re-inv-dd-coordinator`.

## Thang mức độ (đồng bộ 4 mức của suite)

- 🔴 **Đỏ** — tác động giá trị/cấu trúc giao dịch: cần consent trọng yếu của khách hàng/đối tác; tranh chấp trọng yếu chưa công bố; lỗ hổng chuỗi sở hữu (đất/SHTT); change-of-control chặn giao dịch.
- 🟠 **Cam** — rủi ro cao nhưng có đường xử lý rõ; cần làm sớm để không thành blocker.
- 🟡 **Vàng** — cần lưu ý, xử lý được: consent nhiều khả năng lấy được; rủi ro phân loại lao động; điểm cần confirm.
- 🟢 **Xanh** — ghi nhận hồ sơ; phù hợp với reps; không cần hành động ngoài rep.

## Tabular review — rà hàng loạt hợp đồng cùng loại

Khi phải so nhiều hợp đồng (vd toàn bộ HĐ thuê, BCC, HĐ phân phối của target):

- **Hàng** = một tài liệu; **cột** = một data point.
- Mỗi ô = giá trị + trạng thái + **trích nguyên văn ≤125 ký tự** + vị trí (Điều/khoản/trang).
- **Loại cột:** `verbatim` (trích nguyên văn) · `classify` (1 giá trị từ danh sách cố định, vd `cần_consent` / `im_lặng` / `tự_động_chấm_dứt`) · `date` (ISO) · `duration` (số + đơn vị) · `currency` (số + đơn vị tiền) · `number` · `free` (tóm tắt ngắn, dùng hạn chế).
- **3 trạng thái "không tìm thấy":** `không_có` (đã đọc, không có điều khoản) · `chưa_rõ` (có chữ nhưng chưa đủ tự tin) · `cần_review` (có nội dung, cần người phán đoán).
- **Quy trình:** (0) chốt scope + danh sách cột → (1) dựng schema cột, confirm → (2) **chạy mẫu 3–5 tài liệu**, chỉnh prompt/options → (3) rà toàn bộ, mỗi tài liệu một hàng → (4) chuẩn hóa: spot-check ≥3–5 hàng/cột (hoặc 10%) đối chiếu nguyên văn với nguồn, lệch → hạ `cần_review` + ghi `lệch_trích_dẫn`, mở rộng spot-check → (5) xuất lưới (xem template `clause-review-grid`).
- **Quy tắc nguyên văn (cơ học):** trích phải lấy lại được **từng ký tự** tại vị trí dẫn; không ghép/diễn giải/tái dựng/nối bằng dấu "…". Không lấy được nguồn → `cần_review`, value null, ghi `thiếu_trích_dẫn`.
- **Mỗi ô là một đầu mối, không phải kết luận** — vẫn cần verify trước khi đưa vào memo.

## Cờ & quy tắc bắt buộc

- **Cờ successor liability:** khiếu nại tort/sản phẩm, nghĩa vụ môi trường, rủi ro bulk-sale/chuyển nhượng nhằm tẩu tán, kế hoạch giải thể bên bán → nêu riêng, mức 🔴.
- **Trigger consent:** mọi finding hàm ý hành động trước closing (biểu quyết, nộp hồ sơ cơ quan, consent đối tác, giải chấp, cơ chế escrow) → bàn giao sang **CP/closing** (`cp-closing-issue-note-template`) và báo `re-inv-dd-coordinator`.
- **Kiểm chứng nguồn không thương lượng:** mọi viện dẫn luật phải có dấu tvpl hoặc caveat; **không tự lấp** bằng web/model knowledge khi hồ sơ mỏng — dừng và hỏi.
- **Batch lớn (>300 tài liệu):** xử lý theo lô; phát hiện 🔴 báo ngay.

## Cấu trúc output

Header work-product + ghi chú bảo mật/đặc quyền → tổng quan coverage data room → bottom-line (đếm theo mức + 1 takeaway chính) → findings theo nhóm → mục gaps → next-step (cờ blocker, bàn giao CP/closing, owner). Đóng gói theo `../../../templates/transaction-dd-findings-memo.md`; QC qua `re-legal-verification-rules` trước khi chốt.
