# AGENTS.md

Hướng dẫn cho mọi trợ lý AI lập trình mở repo này (Codex, Cursor, Gemini CLI, Copilot, Claude Code...).

Repo là "đội marketing" cho kênh Gumroad bán hai app mã nguồn mở Vutty và Vutidy. Toàn bộ quy tắc nằm trong
`CLAUDE.md`: đọc file đó trước, các quy tắc áp dụng cho mọi AI, không riêng Claude.

## Cách dùng khi AI của bạn không tự nhận skill

Claude Code tự nhận agent trong `.claude/agents/` và skill trong `.claude/skills/` (gõ `/gr-weekly-loop`).
AI khác: bảo nó đọc và làm theo file tương ứng, ví dụ:

> Đọc CLAUDE.md, rồi làm theo .claude/skills/gr-weekly-loop/SKILL.md.

| Việc | File hướng dẫn |
|---|---|
| Vòng làm việc hằng tuần | `.claude/skills/gr-weekly-loop/SKILL.md` |
| Quét thị trường | `.claude/skills/gr-market-scan/SKILL.md` |
| Đọc số liệu bán hàng | `.claude/skills/gr-sales-review/SKILL.md` |
| Định hướng tháng | `.claude/skills/gr-growth-plan/SKILL.md` |
| Viết bài, bài ra mắt | `.claude/skills/gr-content-piece/SKILL.md`, `.claude/skills/gr-launch-post/SKILL.md` |
| Trang bán Gumroad | `.claude/skills/gr-product-page/SKILL.md` |
| Kiểm tra trước khi đăng | `.claude/skills/gr-compliance-check/SKILL.md` |
| Dò skill mới mỗi tháng | `.claude/skills/gr-skill-scout/SKILL.md` |
| Lần chạy định kỳ không có người | `automation/nghien-cuu-dinh-ky.md` |
| Skill ngoài (trang bán, giá, ra mắt, README, email) | `.claude/skills/ext-*/SKILL.md`, danh sách ở `THIRD_PARTY.md` |
| Vai trò từng agent | `.claude/agents/*.md` (phần sau dòng `---` thứ hai là lời dặn cho vai đó) |

## Bắt buộc

- Đọc `knowledge/INDEX.md` và `knowledge/learnings/LEARNINGS.md` trước khi làm.
- Ghi sổ chỉ bằng `python tools/kb.py` (chỉ cần Python 3.9+). Không sửa tay bảng bài học và thí nghiệm.
- Làm trên nhánh riêng, mở pull request. Không đẩy thẳng lên `main`.
- Chạy `python tools/soat_skill.py` và `python -m pytest` trước khi đẩy.
- Không đăng bài, không sửa trang Gumroad, không gửi email thay người dùng.
- Không ghi token, mật khẩu, số tài khoản vào repo.
