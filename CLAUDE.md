# CLAUDE.md

Repo này là "đội marketing" bằng Claude Code cho một lập trình viên độc lập bán app mã nguồn mở trên Gumroad.
Gồm các agent (`.claude/agents/`), các skill (`.claude/skills/gr-*`) và sổ kiến thức (`knowledge/`) mà mọi agent
đọc trước khi làm và ghi thêm sau khi làm.

## Kênh và sản phẩm

- Cửa hàng: https://vunguyenvu.gumroad.com
- **Vutty**: app SSH có két mã hoá trên máy, macOS, Windows, Linux. Mã nguồn MIT: https://github.com/vunguyenvu35/vutty
- **Vutidy**: app dọn và tối ưu Mac có xem trước và hoàn tác. Mã nguồn MIT.
- Khách là lập trình viên, DevOps, sysadmin, người dùng Mac quốc tế. Trang bán, bài viết, tên tính năng bằng tiếng Anh;
  bản Việt, Nhật, Trung cho cộng đồng riêng (giao diện app có 4 ngôn ngữ này).
- Chi tiết sản phẩm: `knowledge/products/`. Kế hoạch 90 ngày đầu: 25/11/2026 đến 23/2/2027.
- Không có ngân sách quảng cáo. Không đề xuất dịch vụ trả tiền trừ khi người dùng hỏi.

## Quy tắc chung cho mọi agent

1. **Đọc trước khi làm.** Mở `knowledge/INDEX.md`, rồi các file liên quan, nhất là `knowledge/learnings/LEARNINGS.md`
   và `knowledge/rules/compliance.md`.
2. **Ghi sau khi làm.** Mỗi việc xong để lại ít nhất một dòng trong sổ: bài học (`python tools/kb.py hoc ...`),
   thí nghiệm (`python tools/kb.py thu-nghiem ...`), hoặc cập nhật file kiến thức kèm ngày `cap_nhat:`.
   Không xoá bài học cũ; bài sai thì ghi bài mới với `--thay-the`.
3. **Có nguồn hoặc nói rõ là đoán.** Mỗi con số kèm link và ngày đọc. Số của kênh ghi nguồn `kenh`. Mở trang gốc, không dùng đoạn trích tìm kiếm.
4. **Kiểm tra trước khi đăng.** Mọi trang bán, bài viết, bài ra mắt qua skill `gr-compliance-check`.
5. **Agent soạn, người dùng đăng.** Agent không tự đăng bài, không tự sửa trang Gumroad, không gửi email cho khách.
   Agent lưu bản soạn trong `content/` để người dùng dán.
6. **Tiếng Việt có dấu, câu ngắn** khi nói với người dùng. Lời khuyên phải làm được ngay: việc gì, làm thế nào, đo bằng gì.
7. **Hướng mới có căn cứ.** Mỗi hướng kèm giả thuyết, thí nghiệm ≤ 14 ngày, 0 đồng, và chỉ số dừng hoặc tiếp.

## Ranh giới

- Chỉ nói tính năng có trong mã nguồn hoặc release notes. Không "unhackable", "military-grade", "X times faster" chưa đo.
- Nói rõ mã nguồn miễn phí; tiền mua là để ủng hộ, bản dựng sẵn, hỗ trợ. Nói rõ trạng thái ký mã.
- So sánh đối thủ chỉ bằng thông tin chính thức có link và ngày, nói cả chỗ đối thủ hơn.
- Luôn nói rõ mình là tác giả. Không tài khoản ảo, không đánh giá giả, không nhờ upvote.
- Đọc luật từng cộng đồng trước khi đăng.

## Nhiều người, nhiều máy, chạy tự động

- Làm trên nhánh riêng (`auto/...` cho lần chạy tự động, tên bất kỳ cho người), mở pull request. Không đẩy thẳng lên `main`.
- Mã bài học và thí nghiệm do `tools/kb.py` tạo (ngày + 4 ký tự ngẫu nhiên), không bao giờ trùng giữa các máy. Không tự đặt mã.
- Lần chạy không có người (GitHub Actions, cron): không hỏi lại, ghi câu hỏi vào báo cáo trong `reports/`.
- Không ghi token, mật khẩu, email khách hàng vào repo.
- AI không phải Claude đọc `AGENTS.md`. Hướng dẫn chia sẻ và chạy tự động: `docs/chia-se-va-tu-dong.md`.
- Lời nhắc chung cho mọi lần chạy định kỳ: `automation/nghien-cuu-dinh-ky.md`. Mỗi repo chỉ bật một lịch.

## Skill ngoài (`ext-*`)

- Chép từ cộng đồng, giữ nguyên giấy phép gốc. Nguồn và commit ghi trong `THIRD_PARTY.md`.
- Chỉ là tài liệu tham khảo: quy tắc trong file này thắng khi khác. Skill ngoài không được làm agent tự đăng, tự nộp, tự gửi.
- Không sửa thân bài skill ngoài, trừ khi cập nhật lên commit mới theo `gr-skill-scout`. Ghi chú riêng đặt trong khối tiếng Việt ở đầu.
- Thêm hay cập nhật skill ngoài: chỉ khi có người duyệt, qua pull request, và `python tools/soat_skill.py` phải sạch.
  Lần chạy tự động chỉ được đề xuất trong báo cáo.

## Kiểm thử

`tools/kb.py` và `tools/soat_skill.py` chỉ dùng thư viện chuẩn Python (3.9 trở lên). Chạy `python -m pytest` trước khi đẩy code.
Ghi thay đổi vào đầu `CHANGELOG.md`.
