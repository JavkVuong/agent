---
name: gr-learn
description: Ghi, gộp và rà soát bài học của đội - cách viết bài học tốt, khi nào nâng hay hạ độ tin, gộp bài trùng, đưa bài học vào playbook, nhắc file quá hạn. Dùng khi người dùng nói "ghi nhớ điều này", "rút kinh nghiệm", hoặc mỗi tháng một lần.
---

# Học và cập nhật liên tục

## Ghi một bài học

`python tools/kb.py hoc --chu-de <chu-de> --bai-hoc "<một câu>" --bang-chung "<số hoặc file>" --do-tin <thap|trung-binh|cao> --nguon <kenh|nguoi-dung|link>`

Chủ đề: `gia`, `trang-ban`, `kenh`, `noi-dung`, `thuong-hieu`, `san-pham`, `thi-truong`, `luat`, `thi-nghiem`.

Bài học tốt: cụ thể, có số, có điều kiện ("với bài trên dev.to có tag ssh"), làm được. Bài học kém: "nội dung hay sẽ ra đơn".

Người dùng nói "ghi nhớ" hoặc sửa cách làm của đội: ghi ngay, nguồn `nguoi-dung`, độ tin `cao`.

## Độ tin

- `thap` → `trung-binh`: thêm một lần quan sát khớp.
- → `cao`: thí nghiệm thắng với đủ mẫu (300 lượt xem hoặc 14 ngày mỗi bên), hoặc trang chính thức.
- Đổi độ tin = ghi bài mới với `--thay-the` bài cũ.

## Rà soát tháng (agent learning-curator)

1. `python tools/kb.py tong-quan` và `python tools/kb.py cu`.
2. Gộp trùng, phân xử mâu thuẫn, đề xuất thí nghiệm cho bài học `thap` quan trọng.
3. Đưa bài học `cao` vào `playbooks/*.md`, `brand/brand-book.md`, hoặc trọng số trong `tools/kb.py`.
4. Giao file quá hạn cho agent phụ trách (xem `knowledge/INDEX.md`).
5. Ghi dòng thay đổi vào `CHANGELOG.md`.
