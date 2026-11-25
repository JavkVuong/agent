---
name: gr-release-announce
description: Biến release notes của Vutty hoặc Vutidy thành nội dung - bài cập nhật gửi người mua và người theo dõi trên Gumroad, bài ngắn cho X, Mastodon, Bluesky, dòng changelog cho trang bán, cập nhật knowledge/products. Dùng mỗi khi phát hành phiên bản mới.
---

# Thông báo phiên bản

1. Đọc RELEASE_NOTES.md của bản mới (trong repo app). Cập nhật `knowledge/products/<app>.md` (phiên bản, ngày, tính năng mới, mục "chưa thử").
2. Chọn tối đa 3 thay đổi người dùng thấy rõ nhất. Bỏ thay đổi nội bộ.
3. Viết:
   - **Bài Gumroad gửi người mua và người theo dõi** (tiếng Anh, dưới 150 từ): 3 thay đổi, cách cập nhật, link tải.
   - **Bài ngắn** cho X, Mastodon, Bluesky (dưới 280 ký tự), có ảnh hoặc GIF.
   - **Dòng "What's new"** cho trang bán.
4. Nói thật phần "chưa thử trên máy thật" nếu release notes có.
5. `gr-compliance-check`, lưu ở `content/release-<app>-<phien-ban>.md`.

Bài thông báo kéo ít đơn mới (bài học L-0002); mục đích chính là giữ người đã mua và người theo dõi.

Chuỗi email gửi người mua sau mỗi bản lớn: `.claude/skills/ext-email-sequence/SKILL.md`.
