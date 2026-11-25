# Đội agent Gumroad

Bộ agent và skill cho Claude Code để nghiên cứu thị trường, xây thương hiệu, viết nội dung và bán hàng cho
[Vutty](https://vunguyenvu.gumroad.com/l/vutty) và [Vutidy](https://vunguyenvu.gumroad.com/l/vutidy) trên Gumroad.

Đội **tự học**: mọi agent đọc sổ kiến thức trước khi làm và ghi bài học sau khi làm. Mỗi hướng mới được thử nhỏ
(tối đa 14 ngày, 0 đồng) rồi ghi kết quả, nên càng dùng càng sát với kênh của bạn.

## Đội gồm ai

| Agent | Việc chính |
|---|---|
| `market-researcher` | Đối thủ, giá, người dùng than phiền gì, thay đổi của Gumroad, Apple, Microsoft |
| `brand-strategist` | Định vị, tagline, trang chủ chung, ảnh bìa, giọng nói |
| `content-marketer` | Bài kỹ thuật, bài so sánh, bài ra mắt, thông báo phiên bản, bản dịch |
| `sales-optimizer` | Trang bán Gumroad, giá, gói đôi, mã giảm giá, email nhận hàng |
| `growth-advisor` | Số liệu, chọn kênh, thí nghiệm, định hướng mỗi tháng |
| `compliance-checker` | Kiểm tra trước khi đăng: Gumroad, lời hứa bảo mật, so sánh, luật cộng đồng |
| `learning-curator` | Gộp và rà soát bài học, đưa bài học vào playbook |

Skill (gõ `/tên-skill` trong Claude Code):

| Skill | Khi nào dùng |
|---|---|
| `gr-weekly-loop` | Mỗi thứ Hai: số liệu, thị trường, kênh, nội dung, báo cáo |
| `gr-market-scan` | Quét thị trường trong tuần |
| `gr-channel-pick` | Chọn nơi đăng bài |
| `gr-brand-kit` | Thương hiệu, trang chủ, ảnh |
| `gr-product-page` | Viết lại trang Gumroad |
| `gr-content-piece` | Một bài kỹ thuật hoặc so sánh |
| `gr-launch-post` | Bài ra mắt cho Show HN, Reddit, Product Hunt, AlternativeTo |
| `gr-release-announce` | Thông báo phiên bản mới |
| `gr-compliance-check` | Kiểm tra trước khi đăng |
| `gr-sales-review` | Đọc số liệu Gumroad và GitHub |
| `gr-growth-plan` | Định hướng đầu tháng |
| `gr-learn` | Ghi và rà soát bài học |

## Cách dùng

1. Mở repo này bằng Claude Code (máy tính hoặc claude.ai/code).
2. Mỗi thứ Hai gõ `/gr-weekly-loop`.
3. Mỗi tuần chép số liệu Gumroad (lượt xem, đơn, doanh thu theo nguồn) vào `knowledge/performance/YYYY-Www.csv`
   và số GitHub vào `knowledge/performance/github.csv`.
4. Đầu tháng gõ `/gr-growth-plan` rồi `/gr-learn`.
5. Muốn đội nhớ điều gì: nói "ghi nhớ: ...".

Agent chỉ soạn. Bạn tự đăng bài, tự sửa trang Gumroad, tự gửi email.

## Sổ kiến thức (`knowledge/`)

Đọc `knowledge/INDEX.md`. Quan trọng nhất: `learnings/LEARNINGS.md` (bài học), `experiments/EXPERIMENTS.md`
(thí nghiệm, đang chạy E-0001 nút Gumroad trên README và E-0002 giá trả tuỳ ý), `rules/compliance.md`.

## Công cụ `tools/kb.py`

Chỉ cần Python 3.9 trở lên, không cài thêm gì.

| Lệnh | Việc |
|---|---|
| `python tools/kb.py hoc --chu-de gia --bai-hoc "..." --do-tin cao` | Ghi bài học (`--thay-the L-0003` để thay bài cũ) |
| `python tools/kb.py thu-nghiem --gia-thuyet ... --cach-thu ... --chi-so ... --nguong ...` | Mở thí nghiệm |
| `python tools/kb.py ket-thuc E-0001 --ket-qua "..." --ket-luan thang` | Đóng thí nghiệm, tự ghi bài học |
| `python tools/kb.py cu` | File kiến thức nào quá hạn, cần nghiên cứu lại |
| `python tools/kb.py cham-diem` | Xếp hạng kênh quảng bá trong `knowledge/market/channels.csv` (kênh cấm tự quảng bá được 0 điểm) |
| `python tools/kb.py so-lieu file.csv --nhom-theo nguon` | Lượt xem, đơn, doanh thu, tỷ lệ chuyển đổi theo nguồn khách |
| `python tools/kb.py tong-quan` | Tình trạng sổ |

Kiểm thử: `python -m pytest`.
