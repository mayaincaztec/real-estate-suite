# Clause Review Grid — rà hàng loạt hợp đồng
> Ngày: YYYY-MM-DD | Bộ tài liệu: [nguồn + số lượng] | Schema cột: [template/mô tả]
> Mỗi ô = giá trị + trạng thái + trích nguyên văn ≤125 ký tự + vị trí. Mỗi ô là **đầu mối**, không phải kết luận.

## Schema cột (xác nhận trước khi rà)
| Cột | Loại | Options (nếu classify) | Prompt |
|---|---|---|---|
| Counterparty | verbatim | — | tên pháp nhân đối tác |
| Change-of-control | classify | cần_consent / tự_động_chấm_dứt / chỉ_thông_báo / im_lặng | hệ quả khi đổi chủ |
| Assignment | classify | cấm / tự_do / cần_consent / carve-out_affiliate | quyền chuyển nhượng |
| MAC | classify | có_định_lượng / định_tính / không_có | điều khoản thay đổi bất lợi |
| Term/expiry | date | — | ngày hết hiệu lực |
| Termination | free | — | căn cứ chấm dứt chính |

## Lưới
| # | Tài liệu | Counterparty | Change-of-control | Assignment | MAC | Term/expiry | Termination | Trạng thái ô cần review |
|---|---|---|---|---|---|---|---|---|
| 1 | | | | | | | | |

> Trạng thái không-tìm-thấy: `không_có` / `chưa_rõ` / `cần_review`. Ô không lấy được nguồn → `cần_review` + `thiếu_trích_dẫn`.

## Nguồn trích dẫn (kèm theo, không gộp vào lưới chính)
| # | Cột | Trích nguyên văn (≤125 ký tự) | Vị trí (Điều/khoản/trang) |
|---|---|---|---|

## Tổng hợp & verify
- Số tài liệu / cột / ô đã điền: ...
- Spot-check đã làm (≥3–5 hàng/cột hoặc 10%): ... ; ô lệch → `lệch_trích_dẫn`: ...
- Cột cần chú ý (>10% bất thường): ...
- Ô `cần_review` chuyển sang Mode 4 (findings): ...
