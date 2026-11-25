# Số liệu bán hàng

Mỗi tuần, chép số liệu từ Gumroad Analytics (lượt xem, đơn, doanh thu theo nguồn) vào một file CSV ở đây,
đặt tên `2026-W48.csv` (năm và số tuần).

Cột bắt buộc: `nguon`, `luot_xem`, `don`. Nên có: `ngay`, `san_pham`, `doanh_thu`, `gia`.
`nguon` là nơi khách đến: `github`, `direct`, `google`, `reddit`, `hn`, `devto`, `discover`, `x`...

Thêm số GitHub mỗi tuần vào `github.csv`: `tuan, repo, sao, luot_xem_repo, nguoi_xem_rieng, clone`.

Tóm tắt: `python tools/kb.py so-lieu knowledge/performance/2026-W48.csv --nhom-theo nguon`
Mẫu: `mau.csv` (số giả, chỉ để minh hoạ cách ghi).
