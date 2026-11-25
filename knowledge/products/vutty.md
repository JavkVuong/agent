---
chu_de: san-pham-vutty
cap_nhat: 2026-11-25
do_tin: cao
can_kiem_tra_lai_sau_ngay: 14
---

# Vutty

- Trang bán: https://vunguyenvu.gumroad.com/l/vutty (15 USD, giá cố định, đọc ngày 25/11/2026)
- Mã nguồn: https://github.com/vunguyenvu35/vutty (MIT, 7 sao, 2 fork, ngày 25/11/2026)
- Bản mới nhất: 1.6.10, ngày 19/11/2026, beta. Bản Windows "chưa thử bằng tay" theo release notes.
- Hệ điều hành: macOS (Apple silicon, Intel), Windows 64-bit, Linux 64-bit. Có Homebrew cask.
- Ký mã: chưa notarize macOS, chưa ký Windows. Người dùng phải bấm "Open Anyway" / "Run anyway". Homebrew tự gỡ cảnh báo.
- Ngôn ngữ giao diện: Anh, Việt, Nhật, Trung.

## Một câu

Vutty là app SSH cho macOS, Windows, Linux, giữ host, khoá và mật khẩu trong một két mã hoá trên máy bạn. Không tài khoản, không cloud, không thu thập dữ liệu.

## Điểm mạnh để bán (có trong mã nguồn)

- Két AES-256-GCM, khoá từ mật khẩu chính qua Argon2id. Khoá riêng và mật khẩu không bao giờ tới giao diện.
- Đồng bộ qua repo Git riêng hoặc thư mục cloud của người dùng, miễn phí.
- Panel: quản lý server Linux (tiến trình, systemd, Docker, log, tường lửa, cron, Incident) qua SSH, không cài gì trên server.
- Kubernetes: pods, workloads, Helm, log, shell trong pod, từ kubeconfig.
- SFTP có hàng đợi tiếp tục được, đồng bộ thư mục không xoá, sửa file từ xa.
- Chạy một lệnh trên nhiều host; snippet có biến.
- Bảo vệ máy production: khung đỏ, nhãn PROD, hỏi trước khi dán nhiều dòng.
- Trợ lý AI tuỳ chọn qua CLI chính chủ, chỉ thấy màn hình đã che bí mật, chỉ gợi ý lệnh.

## Điểm yếu phải nói thật

- Không có app điện thoại, không có tính năng nhóm, không có đồng bộ cloud do Vutty vận hành.
- Bản beta, bản build chưa ký mã.

## Quy định khi viết về Vutty

- Không nói "bảo mật tuyệt đối", "không thể bị hack". Nói đúng cơ chế: AES-256-GCM, Argon2id, dữ liệu trên máy.
- So sánh với Termius chỉ dùng điều có trong trang giá của Termius, ghi ngày đọc (xem `docs/evaluation/comparison.md` của repo Vutty).
