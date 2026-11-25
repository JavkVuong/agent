---
name: gr-content-piece
description: Viết một bài kỹ thuật hoặc bài so sánh kéo người đọc về Vutty, Vutidy - chọn chủ đề từ nỗi đau có thật, tiêu đề theo từ khoá tìm kiếm, nội dung dùng được, nhắc app ở cuối, bản dịch Việt Nhật Trung. Dùng khi cần bài cho dev.to, Hashnode, Viblo, Qiita, Zenn, blog riêng.
---

# Bài viết

## Chọn chủ đề

- Từ `trends-log.md` (mục `[Nỗi đau]`), GitHub Issues của Vutty và đối thủ, câu hỏi trên Reddit.
- Ví dụ cho Vutty: "Manage a Linux server over SSH without installing an agent", "Sync SSH hosts between machines with a private Git repo", "Port forwarding and SOCKS5 explained with examples", "Termius vs open-source alternatives in 2027".
- Ví dụ cho Vutidy: "Free up space taken by Docker, Xcode and node_modules safely", "What is safe to delete on macOS".

## Mẫu bài

```
# <Tiêu đề = câu người ta gõ vào Google>

<2 câu: vấn đề, ai gặp>

## <Cách làm bằng lệnh, không cần app>   ← phần giúp người đọc thật
...

## <Cách làm nhanh hơn>                   ← app xuất hiện ở đây, ngắn, có ảnh
...

---
I build <app>, an open-source <...>. Code: <GitHub>. Builds and support: <Gumroad>?ref=<ten-bai>
```

## Quy tắc

- Lệnh phải chạy được; ảnh chụp là ảnh thật của app.
- Không quá 20% bài nói về app.
- Bản dịch: dịch lại ý cho tự nhiên, đổi ví dụ cho hợp cộng đồng.
- Chạy `gr-compliance-check`, lưu ở `content/YYYY-MM-DD-<ten>.md`, ghi `ref` vào cuối file để đo.

Sửa câu chữ trước khi giao: `.claude/skills/ext-copy-editing/SKILL.md` (bỏ dấu hiệu văn AI). Bài cho dev.to, Hashnode: xem thêm `.claude/skills/ext-open-source-marketing/SKILL.md`.
