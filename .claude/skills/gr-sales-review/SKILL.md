---
name: gr-sales-review
description: Đọc số liệu Gumroad (lượt xem, đơn, doanh thu theo nguồn) và GitHub (sao, lượt xem repo, nguồn giới thiệu) hằng tuần, tính tỷ lệ chuyển đổi, so với tuần trước, rút bài học, đóng thí nghiệm. Dùng khi người dùng gửi số liệu, file CSV hoặc ảnh chụp Gumroad, GitHub Insights.
---

# Đọc số liệu tuần

1. Ảnh chụp: chép số vào `knowledge/performance/YYYY-Www.csv` theo `mau.csv`; hỏi lại chỗ đọc không rõ. Số GitHub vào `knowledge/performance/github.csv`.
2. Chạy:
   - `python tools/kb.py so-lieu knowledge/performance/YYYY-Www.csv --nhom-theo nguon`
   - như trên với `--nhom-theo san_pham`
3. So với tuần trước. Chẩn đoán:

| Triệu chứng | Hay do | Thử |
|---|---|---|
| Ít lượt xem trang | Chưa có kênh kéo khách | Bài kỹ thuật, trang thay thế, nút Gumroad ở README |
| Nhiều xem, chuyển đổi dưới 1% | Trang không nói vì sao trả tiền, thiếu ảnh, sợ app chưa ký | `gr-product-page` |
| Nhiều sao GitHub, ít lượt xem Gumroad | README không mời mua | Thí nghiệm E-0001 |
| Hoàn tiền nhiều | App không mở được, kỳ vọng sai | Email nhận hàng, nói rõ trạng thái ký mã |

4. Rút tối đa 3 bài học, mỗi bài một câu có số, độ tin `cao` chỉ khi mỗi nhóm có từ 300 lượt xem:
   `python tools/kb.py hoc --chu-de kenh --bai-hoc "..." --bang-chung "2026-W48.csv" --do-tin thap --nguon kenh`
5. Thí nghiệm đủ dữ liệu: `python tools/kb.py ket-thuc E-xxxx --ket-qua "..." --ket-luan thang|thua|chua-ro`.
6. Báo người dùng: 3 con số chính, bài học (ID), 1 việc đổi tuần này.
