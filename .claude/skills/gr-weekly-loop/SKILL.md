---
name: gr-weekly-loop
description: Chạy vòng làm việc hằng tuần cho kênh Gumroad (Vutty, Vutidy) - đọc số liệu Gumroad và GitHub, quét thị trường, rút bài học, chọn kênh, viết nội dung tuần tới, so với kế hoạch 90 ngày. Dùng mỗi thứ Hai hoặc khi người dùng nói "làm việc tuần này", "tuần này làm gì".
---

# Vòng làm việc hằng tuần

Vòng học liên tục: **nghiên cứu → làm → đo → học → làm tốt hơn**.

1. **Tình trạng sổ** (learning-curator): `python tools/kb.py tong-quan`.
2. **Số liệu tuần trước** (growth-advisor, skill `gr-sales-review`): file mới trong `knowledge/performance/`.
   Chưa có thì hỏi người dùng chép số liệu Gumroad và GitHub Insights theo `knowledge/performance/README.md`, rồi đi tiếp.
3. **Quét thị trường** (market-researcher, skill `gr-market-scan`).
4. **Kênh tuần tới** (growth-advisor, skill `gr-channel-pick`): 1 đến 2 kênh.
5. **Nội dung** (content-marketer, skill `gr-content-piece` hoặc `gr-launch-post`): 1 bài chính, kèm bản ngôn ngữ khác nếu kịp.
6. **Trang bán** (sales-optimizer): chỉ đổi khi có thí nghiệm đã đóng hoặc mới mở.
7. **Kiểm tra** (compliance-checker, skill `gr-compliance-check`) cho mọi thứ sẽ đăng.
8. **Báo cáo** tối đa 15 dòng, lưu ở `reports/YYYY-Www.md`:
   - Tuần trước: lượt xem trang, đơn, doanh thu, sao GitHub, bài học mới (ID).
   - Tiến độ so với kế hoạch 90 ngày (25/11/2026 đến 23/2/2027): đang ở giai đoạn nào, đã qua cổng nào.
   - Thị trường: 3 điều mới.
   - Tuần này: bài sẽ viết, kênh sẽ đăng, thí nghiệm.
   - Việc người dùng phải tự làm (đăng bài dưới tên họ, chép số liệu, phát hành bản mới).

Ngày đầu tháng: thêm `gr-growth-plan` và `gr-learn`.

Tờ kiểm để rà vòng tuần (điều kiện dừng, điểm chờ người, nhật ký): `.claude/skills/ext-marketing-loops/SKILL.md`.
Đầu tháng chạy thêm `gr-skill-scout` để tìm skill mới đáng lấy.
