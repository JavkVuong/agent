#!/usr/bin/env bash
# Chuẩn bị nhánh cho lần chạy nghiên cứu định kỳ (dùng chung cho lịch Claude, GitHub Actions, cron).
#
# - Nhánh auto/nghien-cuu-hang-tuan đã có trên origin: lấy về, gộp main mới nhất vào.
#   Các kỳ chưa merge nhờ vậy cộng dồn vào một pull request.
# - Chưa có: tạo nhánh từ main mới nhất.
# Không dựa vào origin/main (bản clone trên cloud có thể không có), chỉ dùng FETCH_HEAD.
#
# Cách dùng: bash automation/chuan-bi-nhanh.sh     (đổi tên nhánh: NHANH=ten-khac bash ...)

# Bọc trong hàm: script đổi nhánh giữa chừng, bash phải đọc hết file trước khi chạy.
chinh() {
  set -euo pipefail
  local nhanh="${NHANH:-auto/nghien-cuu-hang-tuan}"
  cd "$(git rev-parse --show-toplevel)"

  if [ -n "$(git status --porcelain)" ]; then
    echo "Lỗi: thư mục repo còn thay đổi chưa commit. Commit hoặc bỏ chúng (git status) rồi chạy lại." >&2
    return 1
  fi
  if [ "$(git rev-parse --is-shallow-repository)" = "true" ]; then
    git fetch --quiet --unshallow origin   # gộp nhánh cần đủ lịch sử
  fi

  git fetch --quiet origin main
  local main tren_origin=""
  main="$(git rev-parse FETCH_HEAD)"
  if git fetch --quiet origin "$nhanh" 2>/dev/null; then
    tren_origin="$(git rev-parse FETCH_HEAD)"
  fi

  # Máy chạy cron giữ nhánh cũ: không xoá commit chưa lên GitHub (ví dụ lần trước đẩy lỗi).
  if git show-ref --verify --quiet "refs/heads/$nhanh" \
      && [ -n "$(git rev-list "${tren_origin:-$main}..refs/heads/$nhanh")" ]; then
    echo "Lỗi: nhánh $nhanh trên máy có commit chưa có trên GitHub. Đẩy tay (git push origin $nhanh)," \
      "hoặc nếu pull request đã merge thì xoá nhánh trên máy (git branch -D $nhanh), rồi chạy lại." >&2
    return 1
  fi

  if [ -n "$tren_origin" ]; then
    git checkout --quiet -B "$nhanh" "$tren_origin"
    if ! git merge --quiet --no-edit "$main"; then
      git merge --abort || true
      echo "Lỗi: gộp main vào $nhanh bị xung đột. Gộp tay: git checkout $nhanh && git fetch origin main && git merge FETCH_HEAD" >&2
      return 1
    fi
    echo "Đang ở nhánh $nhanh: giữ các kỳ chưa merge, đã gộp main mới nhất."
  else
    git checkout --quiet -B "$nhanh" "$main"
    echo "Đã tạo nhánh $nhanh từ main mới nhất."
  fi
}
chinh "$@"
