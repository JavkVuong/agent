---
name: gr-channel-pick
description: Chấm điểm và chọn kênh quảng bá cho Vutty, Vutidy - theo độ khớp khách, ý định mua, độ kéo dài, quy mô, công sức, và bắt buộc cộng đồng cho phép tự quảng bá. Dùng khi chọn nơi đăng bài tuần tới hoặc đánh giá một kênh mới.
---

# Chọn kênh

1. Mở `knowledge/market/channels.csv`. Thêm kênh mới với đủ cột:
   `ten, link, san_pham, khach_khop, y_dinh_mua, keo_dai, quy_mo, cong_suc (đều 1 đến 5), cho_phep_quang_ba (co/khong), ghi_chu`.
   Ô có dấu phẩy thì bọc trong ngoặc kép, ví dụ `"Qiita, Zenn"`, nếu không các cột sẽ lệch.
2. `cho_phep_quang_ba`: đọc luật của kênh. Không cho phép hoặc không rõ thì ghi `khong`.
3. Chạy `python tools/kb.py cham-diem`.
4. Đọc bài học chủ đề `kenh`: có thể loại kênh điểm cao (ví dụ từng bị gỡ bài).
5. Đề xuất 1 đến 2 kênh cho tuần tới, mỗi kênh: điểm, bài sẽ đăng, mã `ref` để đo.

## Thang điểm (0 đến 100, trong `tools/kb.py`)

| Yếu tố | Tối đa | Ý nghĩa |
|---|---|---|
| Khách khớp | 25 | Người ở đó dùng SSH hoặc dùng Mac và hay cài app |
| Ý định mua | 25 | Họ đang tìm thay thế (cao) hay chỉ lướt (thấp) |
| Kéo dài | 20 | Bài còn mang khách sau nhiều tháng (SEO, trang thay thế) hay chỉ một ngày |
| Quy mô | 15 | Số người xem |
| Công sức | 15 | 1 = rất ít công, 5 = rất nhiều (điểm đảo ngược) |
| Không cho tự quảng bá | | Điểm = 0 |

Khi số liệu kênh cho thấy yếu tố nào quan trọng hơn, đề xuất đổi trọng số, ghi bài học, rồi sửa `cham_diem` trong `tools/kb.py` kèm kiểm thử.
