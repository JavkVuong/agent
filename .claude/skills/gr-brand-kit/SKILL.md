---
name: gr-brand-kit
description: Xây hoặc chỉnh thương hiệu chung cho Vutty và Vutidy - tên chung, trang chủ, tagline, giọng nói, ảnh bìa Gumroad, ảnh chụp, GIF, cách nói về riêng tư. Dùng khi làm trang chủ, ảnh bìa mới, hoặc khi các app nhìn không cùng một nhà.
---

# Bộ thương hiệu

Làm trên `knowledge/brand/brand-book.md`. Mỗi lần chốt một mục.

1. **Định vị** một câu: "Cho [ai] muốn [điều gì], [tên] [làm gì], khác vì [lý do]."
2. **Tên chung và trang chủ**: 3 phương án tên miền miễn phí hoặc rẻ (GitHub Pages là 0 đồng). Trang chủ liệt kê các app, link GitHub và Gumroad, có mục "Code signing policy" nếu dùng SignPath.
3. **Tagline từng app** (dưới 80 ký tự), kiểm tra không hứa quá (`gr-compliance-check`).
4. **Ảnh**: dùng tài sản có sẵn trong repo Vutty. Ảnh bìa Gumroad 1280x720, ảnh thu nhỏ 600x600, 4 đến 6 ảnh chụp, 1 GIF 10 giây làm một việc trọn vẹn.
5. **Giọng nói**: 5 từ nên dùng, 5 từ tránh.
6. **Kiểm tra một bài**: chấm 1 đến 5 cho định vị, giọng, sự cụ thể, nói thật điểm yếu. Dưới 4 thì nói sửa gì.

Mục đã chốt: bỏ `[CẦN ĐIỀN]`, đổi `cap_nhat:`, ghi `python tools/kb.py hoc --chu-de thuong-hieu --bai-hoc "Chốt ..." --do-tin cao --nguon nguoi-dung`.

README và trang GitHub (nút Gumroad, ảnh, huy hiệu): `.claude/skills/ext-github-presence/SKILL.md`.
