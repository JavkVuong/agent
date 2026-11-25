# Nội dung của bên thứ ba

Repo này có chép skill của người khác vào `.claude/skills/ext-*`. File này ghi nguồn, commit đã ghim, giấy phép và phần đã sửa
của từng skill, để đúng giấy phép và để biết cần cập nhật gì.

## Quy tắc

- Mỗi thư mục `ext-*` giữ nguyên file `LICENSE` của tác giả gốc. Không xoá.
- Chỉ chép file Markdown. Không chép script, hook, `.mcp.json`, JSON, CSV, file nhị phân.
- Phần đầu `SKILL.md` đổi `name` thành `ext-<tên>` và thêm `disable-model-invocation: true`, để skill ngoài không tự chạy
  thay `gr-*`. Gọi bằng tay (`/ext-cro`) hoặc để skill `gr-*` dẫn tới.
- Ngay dưới phần đầu có khối ghi chú tiếng Việt: nguồn, ngày sửa, phần đã bỏ, và cách áp cho Vutty, Vutidy.
  Đây cũng là thông báo "đã sửa file" mà giấy phép Apache-2.0 (mục 4b) yêu cầu.
- Trước khi merge, chạy `python tools/soat_skill.py` (kiểm thử cũng chạy nó). Lỗi thì sửa; cảnh báo thì đọc lại dòng đó.
- Cập nhật skill ngoài: làm theo `.claude/skills/gr-skill-scout/SKILL.md`, mở pull request có diff từ commit cũ sang commit mới.
  Không đồng bộ tự động, không cài plugin thay cho bản chép này.

## Skill đã chép

Ngày chép: 25/11/2026.

| Skill trong repo | Nguồn | Commit | Giấy phép | Tác giả | File đã bỏ |
|---|---|---|---|---|---|
| `ext-directory-submissions` | [coreyhaines31/marketingskills/skills/directory-submissions](https://github.com/coreyhaines31/marketingskills/tree/8fd2fcade2fd6629026e9dfe6d133b55b36968b9/skills/directory-submissions) | `8fd2fcade2fd` (2026-11-23) | MIT | Corey Haines | evals/evals.json, references/submission-tracker-template.csv |
| `ext-launch` | [coreyhaines31/marketingskills/skills/launch](https://github.com/coreyhaines31/marketingskills/tree/8fd2fcade2fd6629026e9dfe6d133b55b36968b9/skills/launch) | `8fd2fcade2fd` (2026-11-23) | MIT | Corey Haines | evals/evals.json |
| `ext-cro` | [coreyhaines31/marketingskills/skills/cro](https://github.com/coreyhaines31/marketingskills/tree/8fd2fcade2fd6629026e9dfe6d133b55b36968b9/skills/cro) | `8fd2fcade2fd` (2026-11-23) | MIT | Corey Haines | evals/evals.json |
| `ext-copywriting` | [coreyhaines31/marketingskills/skills/copywriting](https://github.com/coreyhaines31/marketingskills/tree/8fd2fcade2fd6629026e9dfe6d133b55b36968b9/skills/copywriting) | `8fd2fcade2fd` (2026-11-23) | MIT | Corey Haines | evals/evals.json |
| `ext-copy-editing` | [coreyhaines31/marketingskills/skills/copy-editing](https://github.com/coreyhaines31/marketingskills/tree/8fd2fcade2fd6629026e9dfe6d133b55b36968b9/skills/copy-editing) | `8fd2fcade2fd` (2026-11-23) | MIT | Corey Haines | evals/evals.json |
| `ext-offers` | [coreyhaines31/marketingskills/skills/offers](https://github.com/coreyhaines31/marketingskills/tree/8fd2fcade2fd6629026e9dfe6d133b55b36968b9/skills/offers) | `8fd2fcade2fd` (2026-11-23) | MIT | Corey Haines | evals/evals.json |
| `ext-pricing` | [coreyhaines31/marketingskills/skills/pricing](https://github.com/coreyhaines31/marketingskills/tree/8fd2fcade2fd6629026e9dfe6d133b55b36968b9/skills/pricing) | `8fd2fcade2fd` (2026-11-23) | MIT | Corey Haines | evals/evals.json |
| `ext-marketing-loops` | [coreyhaines31/marketingskills/skills/marketing-loops](https://github.com/coreyhaines31/marketingskills/tree/8fd2fcade2fd6629026e9dfe6d133b55b36968b9/skills/marketing-loops) | `8fd2fcade2fd` (2026-11-23) | MIT | Corey Haines | evals/evals.json |
| `ext-hacker-news-strategy` | [jonathimer/devmarketing-skills/skills/hacker-news-strategy](https://github.com/jonathimer/devmarketing-skills/tree/500b44b53220292879223a807ce0d349aafe2537/skills/hacker-news-strategy) | `500b44b53220` (2026-03-03) | MIT | Jonathan Reimer | README.md |
| `ext-reddit-engagement` | [jonathimer/devmarketing-skills/skills/reddit-engagement](https://github.com/jonathimer/devmarketing-skills/tree/500b44b53220292879223a807ce0d349aafe2537/skills/reddit-engagement) | `500b44b53220` (2026-03-03) | MIT | Jonathan Reimer | README.md |
| `ext-github-presence` | [jonathimer/devmarketing-skills/skills/github-presence](https://github.com/jonathimer/devmarketing-skills/tree/500b44b53220292879223a807ce0d349aafe2537/skills/github-presence) | `500b44b53220` (2026-03-03) | MIT | Jonathan Reimer | README.md |
| `ext-open-source-marketing` | [jonathimer/devmarketing-skills/skills/open-source-marketing](https://github.com/jonathimer/devmarketing-skills/tree/500b44b53220292879223a807ce0d349aafe2537/skills/open-source-marketing) | `500b44b53220` (2026-03-03) | MIT | Jonathan Reimer | README.md |
| `ext-email-sequence` | [anthropics/knowledge-work-plugins/marketing/skills/email-sequence](https://github.com/anthropics/knowledge-work-plugins/tree/5e504ae11498f2b8daa30d86b7dab97b2ecd8092/marketing/skills/email-sequence) | `5e504ae11498` (2026-11-23) | Apache-2.0 | Anthropic | không |
| `ext-kb-article` | [anthropics/knowledge-work-plugins/customer-support/skills/kb-article](https://github.com/anthropics/knowledge-work-plugins/tree/5e504ae11498f2b8daa30d86b7dab97b2ecd8092/customer-support/skills/kb-article) | `5e504ae11498` (2026-11-23) | Apache-2.0 | Anthropic | không |
| `ext-draft-response` | [anthropics/knowledge-work-plugins/customer-support/skills/draft-response](https://github.com/anthropics/knowledge-work-plugins/tree/5e504ae11498f2b8daa30d86b7dab97b2ecd8092/customer-support/skills/draft-response) | `5e504ae11498` (2026-11-23) | Apache-2.0 | Anthropic | không |

## Ý tưởng tham khảo (không chép chữ)

| Nơi dùng | Lấy ý từ | Giấy phép |
|---|---|---|
| `gr-compliance-check`, mục 10 đến 12 | Lượt rà "Legal and Compliance Flags" trong [anthropics/knowledge-work-plugins/marketing/skills/brand-review](https://github.com/anthropics/knowledge-work-plugins/tree/5e504ae11498f2b8daa30d86b7dab97b2ecd8092/marketing/skills/brand-review) | Apache-2.0, Anthropic |
| `tools/soat_skill.py`, `gr-skill-scout` | Danh sách kiểm tra rút từ nghiên cứu ToxicSkills của Snyk (5/2/2026), Unit 42, tài liệu bảo mật plugin của Anthropic | Không chép mã |

## Không chép (và vì sao)

- `hesreallyhim/awesome-claude-code`: giấy phép CC BY-NC-ND 4.0, cấm làm bản phái sinh. Chỉ đọc để dò skill mới.
- `travisvn/awesome-claude-skills`: không có giấy phép, nên mặc định không được chép.
- `aaron-he-zhu/aaron-marketing-skills`, `infrasity-labs/dev-gtm-claude-skills`: nhiều hook hoặc hàng trăm file script.
- `Varnan-Tech/opendirectory`: có script và tuỳ chọn tự đăng bài bằng tài khoản, trái quy tắc "agent soạn, người đăng".
- Plugin `marketing` của Anthropic cài nguyên bộ: kèm `.mcp.json` nối Slack, HubSpot, Gmail... Chỉ chép `SKILL.md` cần dùng.

Báo cáo đầy đủ: `docs/nghien-cuu/bo-skill-marketing-2026-11.md`.
