---
name: gr-product-page
description: Viết lại hoặc kiểm tra trang bán Gumroad của Vutty hay Vutidy - tiêu đề, ảnh, vì sao trả tiền cho app mã nguồn mở, tính năng, so sánh, riêng tư, file nhận được, hoàn tiền, FAQ, giá. Dùng khi sửa trang Gumroad hoặc trang có lượt xem mà ít đơn.
---

# Trang bán Gumroad

1. Đọc trang hiện tại (mở link trong `knowledge/products/*.md`), `knowledge/playbooks/gumroad-page.md`, file `GUMROAD.md` trong repo của app nếu có.
2. Chấm trang theo 9 mục trong `gumroad-page.md` (có / thiếu / yếu).
3. Viết bản mới, giữ đúng thứ tự 9 mục. Mọi tính năng phải có trong README hoặc release notes.
4. Viết luôn: email nhận hàng (cách mở app chưa ký, SHA256SUMS, email hỗ trợ), chính sách hoàn tiền.
5. Đề xuất giá theo trạng thái ký mã (xem `gumroad-page.md`). Đổi giá thì mở thí nghiệm.
6. Chạy `gr-compliance-check`.
7. Lưu ở `content/gumroad-<app>-YYYY-MM-DD.md`, đưa người dùng dán vào Gumroad. Agent không tự sửa trang Gumroad.

Sau 14 ngày, so tỷ lệ chuyển đổi trước và sau (skill `gr-sales-review`), đóng thí nghiệm.

## Tham khảo thêm (skill ngoài)

- Chẩn đoán trang và thứ tự sửa: `.claude/skills/ext-cro/SKILL.md`.
- Viết và sửa câu chữ: `.claude/skills/ext-copywriting/SKILL.md`, `.claude/skills/ext-copy-editing/SKILL.md`.
- Vì sao trả tiền, gói đôi, bảo đảm hoàn tiền: `.claude/skills/ext-offers/SKILL.md`.
- Giá: `.claude/skills/ext-pricing/SKILL.md` (đọc mục về mức giá kết thúc bằng 9).
- Câu hỏi thường gặp trên trang: `.claude/skills/ext-kb-article/SKILL.md`.
