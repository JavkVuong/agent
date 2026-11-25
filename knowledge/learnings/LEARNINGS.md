# Sổ bài học

Mọi agent đọc file này trước khi làm việc. Chỉ thêm dòng mới bằng `python tools/kb.py hoc ...`.
Không xoá dòng cũ. Bài học bị bác bỏ thì ghi bài mới với `--thay-the L-xxxx`.

Độ tin: `cao` (số của kênh từ đủ mẫu, hoặc trang chính thức), `trung-binh` (nguồn uy tín nhưng hoàn cảnh khác), `thap` (một lần quan sát, ý kiến).

| ID | Ngày | Chủ đề | Bài học | Bằng chứng | Độ tin | Nguồn | Trạng thái |
|---|---|---|---|---|---|---|---|
| L-0001 | 2026-11-25 | gia | Đơn 15 USD bán trực tiếp mất 2 USD phí Gumroad; đơn từ Discover mất 30%. | Trang phí Gumroad | cao | https://gumroad.com/help/article/66-gumroads-fees.html | hieu-luc |
| L-0002 | 2026-11-25 | noi-dung | Bài kỹ thuật kéo 5 đến 15 đơn tuần sau; bài thông báo 0 đến 3; Product Hunt chỉ một ngày. | Một người bán app Mac trên Gumroad | trung-binh | https://dev.to/hiyoyok/selling-mac-apps-on-gumroad-what-works-what-doesnt-honest-numbers-3f0m | hieu-luc |
| L-0003 | 2026-11-25 | trang-ban | Khoảng 15 đến 20% người dùng bỏ đi ở hộp cảnh báo app chưa ký mã trên macOS. | Ước tính của cùng người bán | thap | https://dev.to/hiyoyok/selling-mac-apps-on-gumroad-what-works-what-doesnt-honest-numbers-3f0m | hieu-luc |
| L-0004 | 2026-11-25 | kenh | Tài khoản Reddit mới đăng link vào nhiều nhóm trong một tuần bị khoá; phải tham gia trước. | Một người làm công cụ self-hosted | trung-binh | https://www.indiehackers.com/post/30-days-promoting-a-self-hosted-tool-with-0-budget-heres-what-actually-worked-and-what-got-me-banned-aa1796f9c1 | hieu-luc |
| L-0005 | 2026-11-25 | trang-ban | README Vutty chỉ có nút Ko-fi ở dòng 148, chưa có link Gumroad; khách nóng nhất chưa được mời mua. | Đọc README ngày 25/11/2026 | cao | https://github.com/vunguyenvu35/vutty | hieu-luc |
| L-20261125-52ca | 2026-11-25 | skill | Không bộ skill công khai nào viết cho Gumroad, app Mac hay công cụ SSH; skill ngoài chỉ lấp khung chung (trang bán, giá, ra mắt, README), luật kênh và quy tắc đăng vẫn do gr-* giữ | docs/nghien-cuu/bo-skill-marketing-2026-11.md | trung-binh | https://github.com/coreyhaines31/marketingskills | hieu-luc |
| L-20261125-98fa | 2026-11-25 | skill | Chợ skill công cộng có mã độc thật, nên chỉ chép Markdown từ repo có tác giả rõ, ghim commit, giữ LICENSE và soát bằng tools/soat_skill.py trước khi merge | Snyk ToxicSkills 5/2/2026: 76 payload độc trong 3.984 skill (số của hãng bán công cụ) | trung-binh | https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/ | hieu-luc |
