#!/usr/bin/env bash
# Chạy nghiên cứu định kỳ trên máy chủ hoặc máy riêng, để cron gọi mỗi tuần hoặc mỗi tháng.
# Cần: git (có quyền đẩy lên repo), Python 3.9 trở lên, Claude Code (lệnh claude) đã đăng nhập. gh để tự mở PR (tuỳ chọn).
#
# Cài một lần:   git clone https://github.com/JavkVuong/agent.git ~/agent
# Dòng cron (giờ của máy chủ), sáng thứ Hai:
#   17 8 * * 1  cd ~/agent && bash automation/chay-tren-may-chu.sh >> ~/nghien-cuu.log 2>&1

chinh() {
  set -euo pipefail
  cd "$(dirname "${BASH_SOURCE[0]}")/.."
  # cron chạy với PATH rất ngắn: thêm vào cuối các chỗ hay cài claude, python3, gh (PATH có sẵn vẫn được ưu tiên).
  export PATH="$PATH:$HOME/.local/bin:$HOME/.npm-global/bin:$HOME/.claude/local:/opt/homebrew/bin:/usr/local/bin"

  local py
  py="$(command -v python3 || command -v python || true)"
  if [ -z "$py" ]; then echo "Lỗi: không thấy python3 hay python. Cài Python 3.9 trở lên." >&2; return 1; fi
  if ! command -v claude >/dev/null 2>&1; then
    echo "Lỗi: không thấy lệnh claude. Cài Claude Code rồi chạy claude một lần để đăng nhập." >&2; return 1
  fi

  echo "=== $(date '+%Y-%m-%d %H:%M') bắt đầu"
  bash automation/chuan-bi-nhanh.sh

  local claude_loi=0 test_loi=0
  claude -p "Đọc và làm theo automation/nghien-cuu-dinh-ky.md. Bạn đang chạy bằng automation/chay-tren-may-chu.sh: bỏ qua bước tạo nhánh, không commit, không push; script tự làm sau khi bạn xong." \
    --allowedTools "Read,Write,Edit,Glob,Grep,WebSearch,WebFetch,Bash(python tools/kb.py:*),Bash(python3 tools/kb.py:*),Bash(python -m pytest:*),Bash(python3 -m pytest:*),Bash(python tools/soat_skill.py:*),Bash(python3 tools/soat_skill.py:*)" \
    || claude_loi=$?
  "$py" -m pytest -q || test_loi=$?

  # Đẩy cả khi Claude dừng giữa chừng hay kiểm thử lỗi: kết quả không nằm lại trên máy (lần sau sẽ bị chặn vì
  # thư mục bẩn), và PR cho người duyệt thấy. Người duyệt đọc log trước khi merge.
  bash automation/day-nhanh-va-mo-pr.sh
  if [ "$claude_loi" -ne 0 ]; then
    echo "Cảnh báo: claude dừng với mã $claude_loi (hết hạn mức, mất mạng, chưa đăng nhập?). Kết quả có thể chưa đủ." >&2
  fi
  if [ "$test_loi" -ne 0 ]; then
    echo "Cảnh báo: kiểm thử lỗi. Đã đẩy nhánh để người duyệt xem; đừng merge trước khi sửa." >&2
  fi
  if [ "$claude_loi" -ne 0 ] || [ "$test_loi" -ne 0 ]; then
    return 1
  fi
  echo "=== $(date '+%Y-%m-%d %H:%M') xong"
}
chinh "$@"
