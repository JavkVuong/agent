---
name: gr-growth-plan
description: Đề xuất định hướng phát triển mỗi tháng cho kênh Gumroad - tính năng bán được, app mới, thị trường ngôn ngữ, kênh mới, mô hình giá, ký mã - mỗi hướng có căn cứ, thí nghiệm 0 đồng và chỉ số dừng hoặc tiếp. Dùng đầu tháng hoặc khi doanh số chững lại.
---

# Định hướng tháng

## Đầu vào

Toàn bộ `LEARNINGS.md`, `EXPERIMENTS.md`, số liệu 4 tuần, 4 mục đầu `trends-log.md`, `competitors.md`, file tháng trước trong `knowledge/directions/`, kế hoạch 90 ngày.

## Tìm hướng mới ở 6 chỗ

1. **Gấp đôi cái đang thắng:** nguồn khách có doanh thu cao nhất, kiểu bài có `ref` ra đơn.
2. **Khoảng trống đối thủ:** app ngừng phát triển, đổi giá, bị chê nhiều (Pearcleaner On Hold, thuê bao Termius).
3. **Tính năng bán được:** yêu cầu lặp lại trong Issues, bình luận; tính năng đối thủ thu tiền mà Vutty có miễn phí.
4. **Ngôn ngữ:** cộng đồng Việt, Nhật, Trung; số liệu nguồn khách theo nước.
5. **Mô hình giá:** trả tuỳ ý, cố định, gói đôi, bản hỗ trợ ưu tiên, giấy phép cho công ty nhỏ. Kiểm tra với giấy phép MIT.
6. **App mới local-first:** việc người dùng hiện tại làm bằng tay. Chỉ đề xuất khi có ít nhất 3 tín hiệu có link.

## Đầu ra: `knowledge/directions/YYYY-MM.md`

```
# Định hướng tháng MM/YYYY

## Tháng trước: hướng đã thử, kết quả (ID thí nghiệm, ID bài học)

## 3 hướng tháng này
### 1. [Tên]
- Căn cứ: L-xxxx / link
- Giả thuyết:
- Thí nghiệm (≤ 14 ngày, 0 đồng):
- Chỉ số và ngưỡng: tiếp nếu ..., dừng nếu ...
- Công sức ước tính (giờ):
- Rủi ro uy tín:

## Không làm tháng này (và vì sao)
```

Mở thí nghiệm cho từng hướng bằng `python tools/kb.py thu-nghiem`, ghi ID vào file. Trả lời người dùng 3 hướng, mỗi hướng 2 dòng, một hướng khuyến nghị làm trước.

## Tham khảo thêm (skill ngoài)

- Giá và gói: `.claude/skills/ext-pricing/SKILL.md`, `.claude/skills/ext-offers/SKILL.md`.
- Tăng trưởng dự án mã nguồn mở: `.claude/skills/ext-open-source-marketing/SKILL.md`.
- Chuỗi email cho người mua: `.claude/skills/ext-email-sequence/SKILL.md`.
