---
name: gr-launch-post
description: Chuẩn bị bài ra mắt cho một kênh cụ thể - Show HN, subreddit (r/selfhosted, r/sysadmin, r/homelab, r/devops, r/macapps), Product Hunt, AlternativeTo, OpenAlternative - theo đúng luật và văn hoá từng nơi, kèm câu trả lời bình luận dự kiến. Dùng khi sắp đăng giới thiệu app ở một cộng đồng.
---

# Bài ra mắt

1. Đọc luật của kênh (mở trang luật thật, ghi link). Ghi tóm tắt vào cuối `knowledge/rules/compliance.md` nếu chưa có.
2. Kiểm tra điều kiện: tài khoản đã tham gia đủ lâu chưa (bài học L-0004), app đã đủ ổn để người lạ thử chưa, có link tải trực tiếp không.
3. Viết theo văn hoá kênh:
   - **Show HN**: tiêu đề `Show HN: Vutty – <một dòng>`, đoạn đầu do tác giả viết, nói vì sao làm, cái gì khác, cái gì chưa có. Link GitHub, không link trang bán.
   - **Reddit**: kể vấn đề mình gặp và cách app giải quyết; nói rõ là tác giả; trả lời mọi bình luận trong 24 giờ.
   - **Product Hunt**: tagline 60 ký tự, 4 ảnh, bình luận đầu của maker.
   - **AlternativeTo, OpenAlternative**: mô tả ngắn, gắn làm thay thế cho Termius (Vutty) hoặc CleanMyMac, Pearcleaner (Vutidy).
4. Viết sẵn 8 câu trả lời cho câu hỏi dễ gặp: "Khác Termius chỗ nào?", "Sao không ký mã?", "Sao lại bán app mã nguồn mở?", "Dữ liệu ở đâu?", "Có app điện thoại không?", "Có audit bảo mật chưa?"...
5. Chọn ngày giờ đăng theo khán giả (Show HN: sáng thứ Ba đến thứ Năm giờ bờ Đông Mỹ là thói quen phổ biến, chưa kiểm chứng cho kênh này).
6. `gr-compliance-check`, lưu ở `content/launch-<kenh>-YYYY-MM-DD.md`.
7. Sau 7 ngày: ghi kết quả (lượt xem, sao, đơn theo `ref`) thành bài học `--chu-de kenh`.

## Tham khảo thêm (skill ngoài)

- Khung và thứ tự ra mắt: `.claude/skills/ext-launch/SKILL.md`.
- Danh bạ nên nộp, bộ nội dung nộp: `.claude/skills/ext-directory-submissions/SKILL.md`.
- Hacker News: `.claude/skills/ext-hacker-news-strategy/SKILL.md`. Reddit: `.claude/skills/ext-reddit-engagement/SKILL.md`.
- Quy tắc trong file này và `CLAUDE.md` thắng khi khác với skill ngoài.
