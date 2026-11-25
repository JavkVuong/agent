---
name: gr-compliance-check
description: Kiểm tra trang bán, bài viết, bài ra mắt trước khi đăng - quy định Gumroad, mã nguồn mở, lời hứa bảo mật và hiệu năng, so sánh đối thủ, luật cộng đồng - trả về được đăng, sửa rồi đăng, hoặc không đăng, kèm câu sửa. Dùng trước mọi lần đăng.
---

# Kiểm tra trước khi đăng

Đọc `knowledge/rules/compliance.md`. Kiểm từng mục:

| # | Câu hỏi | Nếu sai |
|---|---|---|
| 1 | Mọi tính năng nhắc tới có trong mã nguồn hoặc release notes bản hiện tại? | SUA_ROI_DANG |
| 2 | Có lời hứa quá mức ("unhackable", "military-grade", "100% safe", "X times faster" chưa đo)? | SUA_ROI_DANG |
| 3 | Trang bán nói rõ mã nguồn miễn phí, người mua nhận gì, ký mã hay chưa, hoàn tiền thế nào? | SUA_ROI_DANG |
| 4 | So sánh đối thủ có link nguồn, ngày đọc, và nói cả chỗ đối thủ hơn? | SUA_ROI_DANG |
| 5 | Dùng tên, logo đối thủ ngoài việc so sánh? | KHONG_DANG |
| 6 | Nói rõ mình là tác giả? | SUA_ROI_DANG |
| 7 | Đúng luật tự quảng bá của kênh (đã mở trang luật)? | KHONG_DANG nếu cấm |
| 8 | Có đánh giá, lời khen giả, nhờ upvote, tài khoản ảo? | KHONG_DANG |
| 9 | Số liệu (dung lượng dọn, tốc độ, số người dùng) có nguồn hoặc cách đo? | SUA_ROI_DANG |
| 10 | Có từ so sánh nhất ("best", "fastest", "only", "first") mà không kèm bằng chứng hay phạm vi? | SUA_ROI_DANG |
| 11 | Có trích lời khen, lời chứng thực mà không ghi ai nói và chưa được người đó đồng ý? | SUA_ROI_DANG |
| 12 | Có đoạn viết lại quá sát bài, trang của người khác (nguy cơ bản quyền)? | SUA_ROI_DANG |

## Đầu ra

```
Kết luận: DUOC_DANG | SUA_ROI_DANG | KHONG_DANG
- Mục 2: "unhackable vault" → "vault encrypted with AES-256-GCM, key derived with Argon2id"
```

Lỗi gặp lần thứ hai: thêm vào `compliance.md`, ghi bài học `--chu-de luat`.

Mục 10 đến 12 lấy ý từ lượt rà "Legal and Compliance Flags" trong skill brand-review của Anthropic (Apache-2.0, xem `THIRD_PARTY.md`).
Khi cần sửa câu chữ, xem thêm `.claude/skills/ext-copy-editing/SKILL.md`.
