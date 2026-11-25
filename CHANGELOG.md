# Nhật ký thay đổi

## 25/11/2026: chạy tự động và chia sẻ

- Workflow `weekly-research` quét thị trường mỗi sáng thứ Hai (8:17 giờ Việt Nam) và mở pull request. Chưa có secret thì tự bỏ qua.
- Mã bài học và thí nghiệm mới có dạng `L-20261201-3f9a`, nên nhiều người, nhiều máy ghi cùng lúc không trùng. Mã cũ `L-0001` vẫn dùng được.
- Hai nhánh cùng thêm bài học thì git giữ cả hai dòng (`merge=union`).
- Thêm `AGENTS.md` và `GEMINI.md` để Codex, Cursor, Gemini CLI làm theo cùng quy tắc; hướng dẫn chia sẻ ở `docs/chia-se-va-tu-dong.md`. 16 kiểm thử.

## 25/11/2026: bản đầu

- 7 agent (nghiên cứu thị trường, thương hiệu, nội dung, bán hàng, tăng trưởng, kiểm tra, thủ thư) và 12 skill `gr-*` cho kênh Gumroad bán Vutty và Vutidy.
- Sổ kiến thức có sẵn thông tin hai app, đối thủ và giá (Termius, Pearcleaner, Mole), phí Gumroad, điều kiện ký mã SignPath, 11 kênh quảng bá đã chấm điểm, 5 bài học và 2 thí nghiệm đầu tiên.
- `tools/kb.py`: ghi bài học, mở và đóng thí nghiệm, báo file quá hạn, chấm điểm kênh quảng bá (kênh cấm tự quảng bá được 0 điểm), tóm tắt lượt xem, đơn, doanh thu theo nguồn. 14 kiểm thử.
