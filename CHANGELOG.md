# Nhật ký thay đổi

## 25/11/2026: soát lỗi toàn bộ repo

- `kb.py hoc`, `thu-nghiem`, `ket-thuc` không còn báo lỗi trên Python 3.9, bản có sẵn của macOS. Trước đây mọi lệnh ghi sổ đều
  dừng với `TypeError` trên máy đó. CI giờ chạy thêm Python 3.9 (trên Windows).
- `kb.py so-lieu` và `cham-diem` đọc `1,234` lượt xem là một nghìn hai trăm ba mươi tư (trước đây hiểu thành một phẩy hai),
  đọc đúng `1.234,50` và `$15`;
  đọc được CSV lưu bằng Excel bản tiếng Việt (dấu `;`); file không phải UTF-8 thì báo cách lưu lại, không in traceback.
- `kb.py hoc --thay-the` với mã sai không còn ghi bài học mới rồi mới báo lỗi (chạy lại sẽ thành hai bài trùng).
  Dòng bảng thiếu cột không làm lệnh dừng bằng traceback.
- Lần chạy tự động qua GitHub Actions giờ cộng dồn vào một nhánh như hai cách kia. Trước đây mỗi lần chạy làm lại
  pull request từ `main`, nên báo cáo kỳ trước mất nếu chưa merge.
- Script chung `automation/chuan-bi-nhanh.sh` thay cho lệnh git trong lời nhắc: chạy được cả khi bản clone trên cloud không có
  `origin/main` (lỗi đã gặp thật), không xoá commit chưa đẩy, dừng rõ ràng khi xung đột.
- Cron dùng `automation/chay-tren-may-chu.sh`. Lệnh cũ trong tài liệu hỏng từ lần chạy thứ hai: `git clone` báo thư mục đã có,
  nên các lệnh sau chạy sai thư mục; kiểm thử lỗi thì kết quả nằm lại trên máy.
- `tools/soat_skill.py` không còn chứa ký tự đảo chiều thật trong mã (GitHub cảnh báo file như vậy), soát thêm ký tự ẩn trong
  `knowledge/`, `automation/`, `.claude/agents/`, CLAUDE.md, AGENTS.md, GEMINI.md, và chặn symlink trong skill ngoài.
- Lần chạy tự động không mở hay đóng thí nghiệm. Trước khi đóng, hỏi người dùng đã đổi từ ngày nào: ngày 25/11/2026
  README Vutty vẫn chưa có nút Gumroad, nên E-0001 chưa thật sự bắt đầu.
- Báo cáo tự động tên `reports/YYYY-Www-tu-dong.md`, không trùng với báo cáo của `/gr-weekly-loop`.
- Skill ngoài có thêm ghi chú về liên kết tới skill và file không chép về. 54 kiểm thử.

## 25/11/2026: thêm 15 skill mạnh của cộng đồng, lịch chạy dùng chung

- 15 skill ngoài `ext-*` lấp chỗ `gr-*` còn thiếu: chẩn đoán trang bán, câu chữ, lý do trả tiền, giá, khung ra mắt, danh bạ nên nộp,
  Hacker News, Reddit, README, tăng trưởng dự án mã nguồn mở, chuỗi email, FAQ, thư trả lời khách.
  Lấy từ marketingskills (MIT, 60 nghìn sao), devmarketing-skills (MIT) và Anthropic (Apache-2.0). Chỉ chép Markdown, giữ LICENSE gốc,
  ghim commit trong `THIRD_PARTY.md`. Skill ngoài không tự chạy; `gr-*` dẫn tới khi cần.
- `python tools/soat_skill.py` soát skill trước khi merge: ký tự ẩn, lệnh chạy ngầm, script, hook, `allowed-tools`, thiếu giấy phép hay nguồn.
  Kiểm thử chạy nó trên chính repo, nên quên giấy phép là CI báo đỏ.
- Skill `gr-skill-scout` dò skill mới mỗi tháng từ 7 nguồn, soát an toàn, chỉ đề xuất. `gr-compliance-check` thêm 3 mục:
  từ so sánh nhất không bằng chứng, lời chứng thực chưa xin phép, đoạn viết lại quá sát bài người khác.
- Mọi cách chạy tự động dùng chung lời nhắc `automation/nghien-cuu-dinh-ky.md` và cộng dồn vào một nhánh, nên ít vào repo
  cũng không bị nhiều pull request. Hướng dẫn tự đặt lịch Claude cho từng người trong `docs/chia-se-va-tu-dong.md`.
- Kiểm thử không còn phụ thuộc số bài học và ngày cập nhật thật trong sổ, nên lần chạy định kỳ ghi sổ không làm CI đỏ.
- Báo cáo nghiên cứu: `docs/nghien-cuu/bo-skill-marketing-2026-11.md`. 26 kiểm thử.

## 25/11/2026: chạy tự động và chia sẻ

- Workflow `weekly-research` quét thị trường mỗi sáng thứ Hai (8:17 giờ Việt Nam) và mở pull request. Chưa có secret thì tự bỏ qua.
- Mã bài học và thí nghiệm mới có dạng `L-20261201-3f9a`, nên nhiều người, nhiều máy ghi cùng lúc không trùng. Mã cũ `L-0001` vẫn dùng được.
- Hai nhánh cùng thêm bài học thì git giữ cả hai dòng (`merge=union`).
- Thêm `AGENTS.md` và `GEMINI.md` để Codex, Cursor, Gemini CLI làm theo cùng quy tắc; hướng dẫn chia sẻ ở `docs/chia-se-va-tu-dong.md`. 16 kiểm thử.

## 25/11/2026: bản đầu

- 7 agent (nghiên cứu thị trường, thương hiệu, nội dung, bán hàng, tăng trưởng, kiểm tra, thủ thư) và 12 skill `gr-*` cho kênh Gumroad bán Vutty và Vutidy.
- Sổ kiến thức có sẵn thông tin hai app, đối thủ và giá (Termius, Pearcleaner, Mole), phí Gumroad, điều kiện ký mã SignPath, 11 kênh quảng bá đã chấm điểm, 5 bài học và 2 thí nghiệm đầu tiên.
- `tools/kb.py`: ghi bài học, mở và đóng thí nghiệm, báo file quá hạn, chấm điểm kênh quảng bá (kênh cấm tự quảng bá được 0 điểm), tóm tắt lượt xem, đơn, doanh thu theo nguồn. 14 kiểm thử.
