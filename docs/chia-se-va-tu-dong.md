# Chạy tự động và chia sẻ repo

## 1. Vì sao dùng git

Mọi thứ đội agent biết nằm trong `knowledge/` dưới dạng file chữ. Mỗi lần chạy (của bạn, của người được chia sẻ,
hay của máy chủ) chỉ là thêm hoặc sửa file, rồi mở pull request (PR). Bạn đọc PR, thấy rõ đội vừa học gì, rồi merge.
Lịch sử git là nhật ký đầy đủ: ai ghi gì, khi nào, quay lại bản cũ được.

Để nhiều nơi ghi cùng lúc không đụng nhau:

- Mã bài học và thí nghiệm có ngày và 4 ký tự ngẫu nhiên (`L-20261201-3f9a`), nên hai máy không tạo trùng mã.
- `.gitattributes` đặt `merge=union` cho `LEARNINGS.md` và `trends-log.md`: khi hai nhánh cùng thêm dòng, git giữ cả hai.
  Nút merge trên web GitHub có thể vẫn báo xung đột; khi đó giữ cả hai dòng là xong.
- Không ai đẩy thẳng lên `main`. Mỗi lần chạy là một nhánh và một PR.

## 2. Ba cách chạy tự động

Mọi cách chạy đều làm theo cùng một lời nhắc: `automation/nghien-cuu-dinh-ky.md`. Muốn đổi việc cần làm, sửa file đó
(qua pull request); lịch nào cũng tự theo.

| Cách | Cần chuẩn bị | Tốn gì | Hợp khi |
|---|---|---|---|
| A. Lịch Claude trên cloud | Mỗi người tự tạo trên tài khoản claude.ai của mình | Hạn mức gói Claude của người tạo | Có một người dùng Claude đều đặn |
| B. GitHub Actions (`.github/workflows/weekly-research.yml`) | Một secret trong GitHub | Hạn mức gói Claude của người tạo token (hoặc tiền API) và phút chạy GitHub Actions | Muốn lịch nằm trong repo, chạy kể cả khi không ai mở Claude |
| C. Máy chủ hoặc máy tính riêng | Cài Claude Code, đặt lịch cron | Hạn mức gói Claude của người chạy | Đã có máy chạy 24/7 |

**Mỗi repo chỉ nên bật một lịch.** Mọi cách đều ghi vào cùng nhánh `auto/nghien-cuu-hang-tuan`, nên hai lịch cùng chạy sẽ
giẫm lên nhau. Người khác muốn chạy thì chạy tay (`/gr-weekly-loop`), hoặc fork repo rồi đặt lịch trên bản fork.

Ít khi vào repo? Đặt lịch hằng tháng thay vì hằng tuần, hoặc tắt lịch và chạy tay khi cần. Các kỳ chưa merge cộng dồn vào
một pull request (cách A và C). Riêng cách B làm mới pull request mỗi lần, nên báo cáo kỳ trước mất nếu chưa merge.

### A. Lịch Claude trên cloud

Lịch thuộc về tài khoản claude.ai của người tạo. Người khác không thấy, không dùng chung được, và commit hay pull request
mang tên GitHub của người tạo. Cần gói Pro, Max, Team hoặc Enterprise. Tài liệu gốc: https://code.claude.com/docs/en/routines

1. Mở https://claude.ai/code/routines → **New task**. Hoặc trong Claude Code gõ `/schedule`.
2. **Repository**: chọn `JavkVuong/agent` (hoặc bản fork của bạn). Tài khoản GitHub đã nối phải có quyền Write.
3. **Lời nhắc**: `Đọc và làm theo automation/nghien-cuu-dinh-ky.md.`
4. **Lịch**: Weekly, hoặc Custom với biểu thức cron (giờ UTC):
   - Sáng thứ Hai 8:17 giờ Việt Nam: `17 1 * * 1`
   - Ngày 1 hằng tháng, 8:17 giờ Việt Nam: `17 1 1 * *`
5. **Connectors** (trong Advanced settings): bỏ hết. Lần chạy này không cần Gmail, Slack hay dịch vụ nào khác.
6. Bấm **Create**, rồi **Run now** để thử một lần. Mỗi lần chạy mở một phiên mới; xem lại ở mục History.

### B. Bật GitHub Actions

1. Trên máy có Claude Code, chạy `claude setup-token`, chép token in ra.
   Token này dùng gói Pro, Max, Team hoặc Enterprise của người tạo ra nó. Muốn trả theo API thì dùng khoá `ANTHROPIC_API_KEY` thay thế.
2. Trên GitHub: repo → Settings → Secrets and variables → Actions → New repository secret.
   Tên `CLAUDE_CODE_OAUTH_TOKEN`, giá trị là token vừa chép.
3. Settings → Actions → General → Workflow permissions: chọn "Read and write permissions" và tick
   "Allow GitHub Actions to create and approve pull requests".
4. Tab Actions → `weekly-research` → Run workflow để thử một lần. Sau đó nó chạy mỗi sáng thứ Hai (8:17 giờ Việt Nam) và mở PR `auto/nghien-cuu-hang-tuan`.
5. Nếu bước Claude báo cần Claude GitHub App: mở Claude Code trong repo, gõ `/install-github-app`.

Chưa có secret thì workflow tự bỏ qua, không báo lỗi. Tài liệu gốc: https://code.claude.com/docs/en/github-actions

### C. Chạy trên máy chủ riêng

```bash
git clone https://github.com/JavkVuong/agent.git && cd agent
git fetch origin && (git checkout auto/nghien-cuu-hang-tuan && git merge --no-edit origin/main || git checkout -b auto/nghien-cuu-hang-tuan origin/main)
claude -p "Đọc và làm theo automation/nghien-cuu-dinh-ky.md. Bỏ qua bước tạo nhánh. Không commit, không push." \
  --allowedTools "Read,Write,Edit,Glob,Grep,WebSearch,WebFetch,Bash(python tools/kb.py:*),Bash(python -m pytest:*),Bash(python tools/soat_skill.py:*)"
python -m pytest -q && git add -A && git commit -m "Nghiên cứu thị trường định kỳ" && git push -u origin HEAD
```

Đặt vào cron mỗi tuần hoặc mỗi tháng. Lần đầu, mở PR từ nhánh `auto/nghien-cuu-hang-tuan`; các lần sau PR tự có thêm commit.

## 3. Chia sẻ cho người khác

1. GitHub → repo → Settings → Collaborators → Add people. Chọn quyền:
   - **Read**: xem và tự chạy trên máy họ, không đẩy được lên repo của bạn (họ gửi lại bằng fork và PR).
   - **Write**: đẩy nhánh và mở PR trực tiếp. Bật bảo vệ nhánh `main` (Settings → Branches → yêu cầu PR) để không ai sửa thẳng.
2. Người được chia sẻ clone repo và dùng AI của họ:
   - **Claude Code**: mở thư mục là nhận đủ agent và skill, gõ `/gr-weekly-loop`.
   - **Codex, Cursor, Gemini CLI, Copilot**: các AI này đọc `AGENTS.md` (Gemini đọc `GEMINI.md`). Skill là file hướng dẫn
     bằng chữ, nên bảo AI "làm theo .claude/skills/gr-market-scan/SKILL.md". Công cụ `tools/kb.py` chỉ cần Python.
   - Mỗi người dùng tài khoản AI của chính họ; repo không chứa khoá hay token nào.
3. Họ làm trên nhánh riêng và mở PR; bạn duyệt rồi merge.

## 4. Lưu ý khi chia sẻ

- Người có quyền Read thấy hết `knowledge/`, kể cả số liệu bán hàng trong `knowledge/performance/`. Nếu không muốn,
  giữ số liệu ở repo riêng hoặc chỉ ghi số đã làm tròn.
- Không commit token, mật khẩu, email khách hàng. Token để trong GitHub Secrets.
- Một AI khác có thể làm sai quy tắc. Đọc kỹ PR trước khi merge, nhất là thay đổi ở `knowledge/rules/` và `tools/`.
- Gỡ quyền: Settings → Collaborators → Remove. Token đã lộ: tạo token mới và xoá secret cũ.
