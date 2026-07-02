> **Nguồn gốc:** đúc kết từ *"Ask Smarter — 101 Questions for the Buy-Side"* (Herman, Henry & Dominic, ấn bản 5/2026, lưu hành nội bộ & chia sẻ cộng đồng). Toàn văn từng entry (nguyên văn câu hỏi tiếng Anh, Why ask, Clean answer, Red flags, Contract impact) tại `assets/re-legal-counsel/Herman, Henry & Dominic _Ask Smarter - 101 questions for the buy-side.md` — mở file gốc khi cần soạn câu hỏi nguyên văn gửi seller hoặc cần bộ red-flag chi tiết theo câu. Sách jurisdiction-neutral: mọi câu phải phủ thêm lớp luật Việt Nam trước khi kết luận.

# Buy-side DD Question Bank — 101 câu hỏi cho bên mua

> Ngân hàng câu hỏi buy-side cho `re-inv-dd-coordinator`, dùng ở 3 điểm trong quy trình DD: (1) **kickoff** — dựng câu hỏi mở màn theo workstream cùng lúc với DRL; (2) **clarification log** — chuẩn hoá câu hỏi gửi seller khi tài liệu thiếu/mâu thuẫn; (3) **management Q&A session** — chuẩn bị agenda phỏng vấn ban điều hành target. Bổ sung (không thay thế) Clarification Question Bank rút gọn trong `dd-document-request-templates.md`.

## Cấu trúc mỗi entry trong sách gốc (5 phần)

1. **The Question** — câu hỏi nguyên văn đặt cho seller, on the record;
2. **Why ask** — rủi ro mà câu hỏi đang truy tìm;
3. **A clean answer** — câu trả lời "sạch" từ target quản trị tốt trông như thế nào (baseline để so);
4. **Red flags** — tín hiệu có vấn đề (phần giá trị nhất khi thời gian gấp);
5. **Contract impact** — câu trả lời dẫn tới điều khoản nào: warranty / indemnity / CP / price mechanism.

Cách khai thác nhanh: hỏi theo cột "Câu hỏi" dưới đây → so câu trả lời với **Clean answer** trong sách gốc → nếu khớp **Red flags** thì ghi issue vào issue tracker (kèm severity) → dùng **Contract impact** để chuyển finding thành yêu cầu SPA (R&W bổ sung / specific indemnity / CP / điều chỉnh giá) — phần chuyển hoá này giao `re-legal-counsel` (xem `../../re-legal-counsel/references/ma-clause-playbook-vn.md` và `ma-traps-catalog.md`).

## Map 15 chương → workstream & owner

| Ch. | Chủ đề | Câu hỏi | Workstream | Owner chính |
|---|---|---|---|---|
| I | Corporate Structure & Governance | Q1–10 | Legal & Corporate | `re-legal-counsel` (khớp checklist CTCP nhóm 1–3) |
| II | Capitalization & Equity | Q11–16 | Legal & Corporate | `re-legal-counsel` |
| III | Financial Statements & Accounting | Q17–25 | Financial | Deal team / FA |
| IV | Tax | Q26–32 | Tax | Deal team / tax advisor |
| V | Material Contracts & Commercial | Q33–41 | Legal & Corporate | `re-legal-counsel` (tabular review) |
| VI | Customers, Suppliers & Revenue | Q42–46 | Commercial | Deal team |
| VII | Employment, Benefits & Key People | Q47–55 | HR / Legal | Deal team + `re-legal-counsel` (enforceability) |
| VIII | Intellectual Property | Q56–62 | Legal & Corporate | `re-legal-counsel` |
| IX | IT, Data Privacy & Cybersecurity | Q63–69 | IT / Legal | Deal team + `re-legal-counsel` (PDPL) |
| X | Real Estate & Tangible Assets | Q70–74 | Project Legal / Technical | `re-legal-licensing` + technical |
| XI | Litigation, Disputes & Investigations | Q75–80 | Legal & Corporate | `re-legal-counsel` |
| XII | Regulatory & Licensing | Q81–86 | Legal (entity) / Project Legal | licence pháp nhân → `re-legal-counsel`; permit dự án → `re-legal-licensing` |
| XIII | Anti-Corruption, Sanctions, AML & ESG | Q87–92 | Compliance | Deal team + `re-legal-counsel` |
| XIV | Insurance & Risk Transfer | Q93–95 | Financial / Ops | Deal team |
| XV | Related Parties & Deal Closing | Q96–101 | Legal & Corporate / Closing | `re-legal-counsel` + coordinator (CP → closing checklist) |

## Ngân hàng câu hỏi

### I. Corporate Structure & Governance (Q1–10)
| Q | Hỏi seller |
|---|---|
| 1 | Target thành lập hợp lệ và đang "good standing" tại mọi nơi đăng ký/hoạt động? |
| 2 | Cung cấp một sơ đồ nhóm công ty duy nhất, có ngày — đủ mọi entity, mọi tỷ lệ %, cả công ty "ngủ đông"? |
| 3 | Điều lệ và SHA hiện hành có nhất quán với cap table không? |
| 4 | Thành viên HĐQT/BGĐ là ai, hồ sơ bổ nhiệm có đầy đủ? |
| 5 | Biên bản HĐQT/ĐHĐCĐ đầy đủ, đã ký, không còn action treo? |
| 6 | Tồn tại quyền pre-emption / ROFR / drag / tag / consent nào — thời hạn thông báo bao lâu? |
| 7 | Các đợt tái cấu trúc / sáp nhập / chuyển nhượng cổ phần trước đây có thực hiện hợp lệ, đã đăng ký? |
| 8 | Có deadlock, quyền bảo vệ cổ đông nhỏ, quyền veto nào mà bên mua sẽ thừa kế? |
| 9 | Sổ đăng ký cổ đông và hồ sơ UBO (chủ sở hữu hưởng lợi) có cập nhật? |
| 10 | Các POA target đã cấp: còn hiệu lực, phạm vi, thu hồi được khi closing? |

### II. Capitalization & Equity (Q11–16)
| Q | Hỏi seller |
|---|---|
| 11 | Cap table fully-diluted: mọi cổ phần, option, warrant, SAFE, phantom? |
| 12 | Mọi đợt phát hành cổ phần có phê duyệt hợp lệ và đã góp đủ tiền? |
| 13 | ESOP / phantom / profit-participation nào tồn tại — acceleration khi CoC thế nào? |
| 14 | Convertible note / SAFE / cổ phần ưu đãi chuyển đổi đang lưu hành — cơ chế khi M&A? |
| 15 | Có side letter hoặc cam kết equity ngoài cap table không? |
| 16 | Các đợt phát hành có tuân thủ điều kiện chào bán riêng lẻ / exemption? |

### III. Financial Statements & Accounting (Q17–25)
| Q | Hỏi seller |
|---|---|
| 17 | BCTC kiểm toán 3–5 năm gần nhất — loại ý kiến kiểm toán? |
| 18 | Chuẩn mực kế toán đang dùng — có thay đổi trong kỳ được định giá? |
| 19 | Trình bày chính sách ghi nhận doanh thu + 5 hoá đơn lớn nhất quý gần nhất? |
| 20 | Bridge adjusted-EBITDA, từng add-back và workpaper chứng minh? |
| 21 | Xu hướng working capital — mức "normalised" cho deal định nghĩa thế nào? |
| 22 | Net debt là bao nhiêu — "debt" gồm gì trong bridge cash-free/debt-free? |
| 23 | Nghĩa vụ off-balance-sheet, bảo lãnh, contingent nào tồn tại? |
| 24 | Số dư intercompany, transfer pricing, management charge cấu trúc ra sao? |
| 25 | Có restatement, điều chỉnh kiểm toán trọng yếu, hay đổi công ty kiểm toán? |

### IV. Tax (Q26–32)
| Q | Hỏi seller |
|---|---|
| 26 | Tờ khai thuế trọng yếu đã nộp đủ — có cuộc thanh/kiểm tra, ấn định, tranh chấp thuế đang mở? |
| 27 | Effective tax rate lịch sử — driver là gì? |
| 28 | Transfer pricing có hồ sơ, benchmark, khớp với substance? |
| 29 | Ruling / ưu đãi / miễn giảm thuế nào deal có thể kích hoạt hoặc làm mất? |
| 30 | Uncertain tax positions / dự phòng thuế nào tồn tại? |
| 31 | Exposure VAT, thuế nhà thầu / khấu trừ tại nguồn, payroll, thuế gián thu? |
| 32 | Cấu trúc deal có kích hoạt thuế change-of-control, stamp duty, indirect-transfer? |

### V. Material Contracts & Commercial (Q33–41)
| Q | Hỏi seller |
|---|---|
| 33 | Master contracts register ở đâu — đầy đủ đến mức nào so với data room? |
| 34 | Hợp đồng nào có điều khoản CoC / anti-assignment — đã flag với đối tác nào chưa? |
| 35 | Điều khoản exclusivity / non-compete / MFN nào đang ràng buộc target? |
| 36 | Đối tác có quyền termination-for-convenience / for-material-breach nào? |
| 37 | Auto-renewal, evergreen, trigger chấm dứt bất thường nào tồn tại? |
| 38 | Cap và carve-out trách nhiệm của target trong các hợp đồng chính? |
| 39 | Hợp đồng nào chưa ký, hết hạn nhưng vẫn đang thực hiện, hoặc bất thường? |
| 40 | Có đối tác nhà nước / SOE / politically-exposed không? |
| 41 | Hợp đồng ngoại tệ / FX exposure chưa hedge? |

### VI. Customers, Suppliers & Revenue (Q42–46)
| Q | Hỏi seller |
|---|---|
| 42 | Top 10 khách hàng theo doanh thu từng năm trong 3 năm — đã mất khách nào? |
| 43 | Độ tập trung nhà cung cấp — có single-sourcing đầu vào quan trọng? |
| 44 | Khách/NCC chính nào đã báo chấm dứt, không gia hạn, hoặc đòi repricing? |
| 45 | Đàm phán giá / RFP / gia hạn hợp đồng nào đang treo? |
| 46 | Điều khoản thanh toán điển hình + ageing — có factoring / supplier finance? |

### VII. Employment, Benefits & Key People (Q47–55)
| Q | Hỏi seller |
|---|---|
| 47 | Key employees là ai — điều gì đang giữ chân họ? |
| 48 | CoC treatment trong HĐLĐ và bonus plan trên toàn bộ workforce? |
| 49 | Non-compete / non-solicit / bảo mật có đủ — khả thi thực thi tại từng jurisdiction? |
| 50 | Cấu trúc workforce: nhân viên / contractor / agency / secondee? |
| 51 | Có lịch sử misclassification contractor thành độc lập? |
| 52 | Pension / trợ cấp thôi việc / end-of-service — funded và hạch toán đủ? |
| 53 | CBA / công đoàn — nhân viên có tự động chuyển theo TUPE / tương đương? |
| 54 | Tranh chấp lao động / harassment / whistleblower đang treo hoặc đe doạ? |
| 55 | Work permit / right-to-work có duy trì đầy đủ? |

### VIII. Intellectual Property (Q56–62)
| Q | Hỏi seller |
|---|---|
| 56 | Target **sở hữu** hay chỉ **license** IP mà nó phụ thuộc? |
| 57 | IP register (patent, nhãn hiệu, kiểu dáng, domain) đầy đủ, cập nhật? |
| 58 | Inventor / nhân viên / contractor đã assign IP hợp lệ cho target? |
| 59 | Licence-in nào có scope hẹp, điều khoản CoC, hoặc audit clause? |
| 60 | Open-source trong codebase — AI training data lấy nguồn thế nào? |
| 61 | Đã có claim xâm phạm IP, opposition, invalidity action nào? |
| 62 | Trade secret được bảo vệ bằng biện pháp kỹ thuật + hợp đồng đủ chưa? |

### IX. IT, Data Privacy & Cybersecurity (Q63–69)
| Q | Hỏi seller |
|---|---|
| 63 | Kiến trúc IT — phụ thuộc vendor / cloud / seller group đến mức nào? |
| 64 | Deal có cần IT separation / TSA — chi phí và timeline carve-out? |
| 65 | Target xử lý dữ liệu cá nhân gì, trên cơ sở pháp lý nào? |
| 66 | DPA và cơ chế chuyển dữ liệu xuyên biên giới có đủ chưa? |
| 67 | Đã có data breach / ransomware / thông báo cơ quan quản lý nào? |
| 68 | Cybersecurity posture: pen test, SOC report, IR plan, bảo hiểm cyber? |
| 69 | Hệ thống AI có tạo exposure quản lý / IP / bias không? |

### X. Real Estate & Tangible Assets (Q70–74)
| Q | Hỏi seller |
|---|---|
| 70 | BĐS nào sở hữu vs thuê — hồ sơ title / lease ở đâu? |
| 71 | Lease trọng yếu có trigger CoC / landlord consent? |
| 72 | Encumbrance, easement, hạn chế quy hoạch — estate có compliant khí hậu? |
| 73 | Tình trạng, tuổi, capex backlog của máy móc thiết bị và tồn kho? |
| 74 | Vấn đề ô nhiễm môi trường / remediation / permit gắn với site nào? |

### XI. Litigation, Disputes & Investigations (Q75–80)
| Q | Hỏi seller |
|---|---|
| 75 | Schedule đầy đủ litigation: pending, threatened, mới settle? |
| 76 | Điều tra hình sự / quản lý nhà nước nào mở hoặc đã đóng trong 5 năm? |
| 77 | Demand letter, hoà giải, thông báo trọng tài pre-litigation nào? |
| 78 | Phương pháp trích lập dự phòng litigation — khớp với đánh giá của external counsel? |
| 79 | Class action / product liability / mass tort exposure? |
| 80 | Judgment, injunction, consent decree, undertaking nào đang ràng buộc target? |

### XII. Regulatory & Licensing (Q81–86)
| Q | Hỏi seller |
|---|---|
| 81 | Target giữ licence / permit / authorisation nào — cái nào deal-critical? |
| 82 | Licence nào gắn cá nhân pháp nhân, không chuyển nhượng được, hoặc cần consent khi CoC? |
| 83 | Inspection đang mở, deficiency letter, remediation plan nào? |
| 84 | Deal có trigger merger control / FDI / phê duyệt ngành? (VN: thông báo TTKT — Luật Cạnh tranh; thủ tục M&A approval — Luật Đầu tư) |
| 85 | Chế độ compliance ngành nào áp dụng — bằng chứng tuân thủ ở đâu? |
| 86 | Compliance program: policy, hồ sơ training, monitoring có bằng chứng? |

### XIII. Anti-Corruption, Sanctions, AML & ESG (Q87–92)
| Q | Hỏi seller |
|---|---|
| 87 | Anti-bribery program có tài liệu hoá, tương xứng risk profile? |
| 88 | Third-party intermediaries đã được risk-rate và screen? |
| 89 | Target / UBO / đối tác đã screen sanctions và PEP list? |
| 90 | AML / KYC có phù hợp với business và tệp khách hàng? |
| 91 | Exposure modern slavery / forced labor / nhân quyền chuỗi cung ứng? |
| 92 | ESG disclosure / rating / commitment nào đã công bố — chứng minh được không? |

### XIV. Insurance & Risk Transfer (Q93–95)
| Q | Hỏi seller |
|---|---|
| 93 | Chương trình bảo hiểm — limit và coverage có tương xứng risk profile? |
| 94 | Lịch sử claim, claim bị từ chối, notification of circumstance? |
| 95 | W&I (R&W) insurance có khả thi — underwriter sẽ lo ngại gì? |

### XV. Related Parties & Deal Closing (Q96–101)
| Q | Hỏi seller |
|---|---|
| 96 | Giao dịch bên liên quan nào với cổ đông / giám đốc / affiliates — có arm's length? |
| 97 | Dịch vụ / IP licence / tài trợ nội bộ nhóm nào phải thay thế hoặc unwind khi closing? |
| 98 | Bảo lãnh, security, LC, performance bond nào cần giải phóng khi closing? |
| 99 | Side agreement, MOU, thoả thuận chưa tiết lộ nào với management / cổ đông? |
| 100 | CP, third-party consent, thông báo quản lý nào cần cho closing? |
| 101 | "Skeleton" nào seller đã biết — seller đã chủ động disclose chưa? |

## Quy tắc dùng

- **Chọn lọc theo deal, không bắn cả 101.** Kickoff chọn theo workstream đã mở ở Bước 1 (scope); deal BĐS Việt Nam điển hình ưu tiên Ch. I, II, V, X, XI, XII, XV + III/IV.
- **Câu trả lời của seller phải đối chiếu tài liệu**, không nhận câu trả lời miệng — mỗi câu trong sách gốc có "Clean answer" mô tả bộ hồ sơ đi kèm; thiếu hồ sơ → ghi vào DRL gap.
- **Red flag → issue tracker** với severity + owner; red flag pháp lý chuyên sâu giao `re-legal-counsel` / `re-legal-licensing` theo map ở trên, coordinator không tự kết luận pháp lý.
- **Contract impact → SPA:** finding từ câu hỏi phải chảy về điều khoản (R&W / specific indemnity / CP / price mechanism) — brief cho `re-legal-counsel` kèm số câu hỏi và tài liệu nguồn.
- **Lớp luật Việt Nam:** sách jurisdiction-neutral; các câu chạm luật VN (Q32 thuế chuyển nhượng, Q53 chuyển giao lao động, Q65–66 PDPL, Q84 TTKT/M&A approval...) phải kiểm chứng qua MCP `legal` trước khi kết luận trong findings.
