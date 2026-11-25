#!/usr/bin/env bash
# Commit kết quả lần chạy định kỳ, đẩy nhánh, mở pull request vào main nếu chưa có.
# Dùng cho GitHub Actions và cron. Lịch Claude trên cloud tự commit và mở PR, không cần script này.
#
# Cách dùng: bash automation/day-nhanh-va-mo-pr.sh
# Cần: đang ở nhánh do automation/chuan-bi-nhanh.sh tạo; quyền đẩy lên origin.
# Mở PR cần lệnh gh đã đăng nhập (trên GitHub Actions: biến GH_TOKEN). Không có gh thì chỉ đẩy nhánh.

chinh() {
  set -euo pipefail
  local nhanh="${NHANH:-auto/nghien-cuu-hang-tuan}"
  local tieu_de="Nghiên cứu thị trường định kỳ"
  cd "$(git rev-parse --show-toplevel)"

  if [ "$(git rev-parse --abbrev-ref HEAD)" != "$nhanh" ]; then
    echo "Lỗi: đang không ở nhánh $nhanh. Chạy automation/chuan-bi-nhanh.sh trước." >&2
    return 1
  fi

  git add -A
  if git diff --cached --quiet; then
    echo "Lần chạy này không đổi file nào."
  else
    git commit --quiet -m "$tieu_de ($(date -u +%Y-%m-%d))"
    echo "Đã commit thay đổi."
  fi

  git fetch --quiet origin main
  if [ "$(git rev-list --count FETCH_HEAD..HEAD)" = "0" ]; then
    echo "Nhánh không có gì mới so với main. Không đẩy, không mở pull request."
    return 0
  fi

  # Không bao giờ đẩy đè (force): nhánh trên origin đổi thì lần sau chuan-bi-nhanh.sh gộp lại.
  git push --quiet origin "HEAD:refs/heads/$nhanh"
  echo "Đã đẩy nhánh $nhanh."

  if ! command -v gh >/dev/null 2>&1; then
    echo "Không có lệnh gh: lần đầu, tự mở pull request từ $nhanh vào main trên GitHub. Các lần sau PR tự có thêm commit."
    return 0
  fi
  local so
  so="$(gh pr list --head "$nhanh" --base main --state open --json number --jq '.[].number' 2>/dev/null | head -n 1 || true)"
  if [ -n "$so" ]; then
    echo "Pull request #$so đã mở từ trước, đã có thêm commit mới."
    return 0
  fi
  if ! gh pr create --base main --head "$nhanh" --title "$tieu_de" \
      --body "Lần chạy định kỳ theo automation/nghien-cuu-dinh-ky.md. Báo cáo trong reports/. Đọc rồi merge nếu ổn; đóng mà không merge thì xoá luôn nhánh $nhanh."; then
    echo "Lỗi: không mở được pull request. Trên GitHub Actions: bật Settings → Actions → General → 'Allow GitHub Actions to create and approve pull requests'. Trên máy riêng: chạy gh auth login, hoặc tự mở PR từ nhánh $nhanh." >&2
    return 1
  fi
}
chinh "$@"
