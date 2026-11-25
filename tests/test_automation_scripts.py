"""Kiểm thử các script trong automation/ trên repo git tạm (một remote trần và các bản clone).

Không cần mạng. Bỏ qua trên Windows: script chạy bằng bash trên máy chủ, GitHub Actions (Ubuntu) và cloud.
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

GOC = Path(__file__).resolve().parent.parent
TU_DONG = GOC / "automation"
NHANH = "auto/nghien-cuu-hang-tuan"

pytestmark = pytest.mark.skipif(
    sys.platform == "win32" or not shutil.which("bash") or not shutil.which("git"),
    reason="cần bash và git (script chạy trên Linux, macOS)",
)


@pytest.fixture
def moi_truong(tmp_path):
    """Biến môi trường cho git tạm, kèm một lệnh gh giả ghi lại lời gọi."""
    gh_gia = tmp_path / "bin" / "gh"
    gh_gia.parent.mkdir()
    gh_gia.write_text(f'#!/usr/bin/env bash\necho "$@" >> "{tmp_path}/gh.log"\n', encoding="utf-8")
    gh_gia.chmod(0o755)
    env = dict(os.environ)
    env.update({
        "GIT_AUTHOR_NAME": "Kiem Thu", "GIT_AUTHOR_EMAIL": "kiem-thu@example.com",
        "GIT_COMMITTER_NAME": "Kiem Thu", "GIT_COMMITTER_EMAIL": "kiem-thu@example.com",
        "GIT_CONFIG_GLOBAL": str(tmp_path / "gitconfig"), "GIT_CONFIG_NOSYSTEM": "1",
        "PATH": f"{gh_gia.parent}{os.pathsep}{env.get('PATH', '')}",
    })
    return env


def _git(cwd, *args, env, check=True):
    return subprocess.run(["git", *args], cwd=cwd, env=env, check=check, capture_output=True, text=True)


def _chay(script, cwd, env):
    return subprocess.run(["bash", str(TU_DONG / script)], cwd=cwd, env=env, capture_output=True, text=True)


def _remote_va_clone(tmp_path, env, ten="may1"):
    """Tạo remote trần có main với một file, rồi clone ra thư mục ten."""
    remote = tmp_path / "remote.git"
    if not remote.exists():
        _git(tmp_path, "init", "--bare", "-b", "main", str(remote), env=env)
        hat = tmp_path / "hat"
        _git(tmp_path, "clone", str(remote), str(hat), env=env)
        (hat / "so.md").write_text("dòng 1\n", encoding="utf-8")
        _git(hat, "add", "-A", env=env)
        _git(hat, "commit", "-m", "đầu", env=env)
        _git(hat, "push", "origin", "HEAD:main", env=env)
    clone = tmp_path / ten
    _git(tmp_path, "clone", str(remote), str(clone), env=env)
    return remote, clone


def _them_vao_main(tmp_path, env, ten_file, noi_dung):
    hat = tmp_path / "hat"
    _git(hat, "pull", "-q", "origin", "main", env=env)
    (hat / ten_file).write_text(noi_dung, encoding="utf-8")
    _git(hat, "add", "-A", env=env)
    _git(hat, "commit", "-m", f"main sửa {ten_file}", env=env)
    _git(hat, "push", "origin", "HEAD:main", env=env)


def test_lan_dau_tao_nhanh_day_va_mo_pr(tmp_path, moi_truong):
    remote, clone = _remote_va_clone(tmp_path, moi_truong)
    kq = _chay("chuan-bi-nhanh.sh", clone, moi_truong)
    assert kq.returncode == 0, kq.stderr
    assert "Đã tạo nhánh" in kq.stdout
    (clone / "reports.md").write_text("báo cáo tuần 49\n", encoding="utf-8")
    kq = _chay("day-nhanh-va-mo-pr.sh", clone, moi_truong)
    assert kq.returncode == 0, kq.stderr
    assert _git(remote, "rev-parse", "--verify", NHANH, env=moi_truong).returncode == 0
    gh = (tmp_path / "gh.log").read_text(encoding="utf-8")
    assert "pr list" in gh and "pr create" in gh and "--base main" in gh


def test_cac_ky_chua_merge_duoc_cong_don(tmp_path, moi_truong):
    _, may1 = _remote_va_clone(tmp_path, moi_truong)
    _chay("chuan-bi-nhanh.sh", may1, moi_truong)
    (may1 / "tuan-49.md").write_text("kỳ 1\n", encoding="utf-8")
    assert _chay("day-nhanh-va-mo-pr.sh", may1, moi_truong).returncode == 0

    _them_vao_main(tmp_path, moi_truong, "main-moi.md", "main đổi sau kỳ 1\n")

    _, may2 = _remote_va_clone(tmp_path, moi_truong, "may2")  # như bản clone mới trên cloud hay Actions
    _git(may2, "config", "--unset-all", "remote.origin.fetch", env=moi_truong)  # clone trên cloud không có origin/main
    kq = _chay("chuan-bi-nhanh.sh", may2, moi_truong)
    assert kq.returncode == 0, kq.stderr
    assert "giữ các kỳ chưa merge" in kq.stdout
    assert (may2 / "tuan-49.md").exists() and (may2 / "main-moi.md").exists()


def test_xung_dot_thi_dung_va_khong_de_lai_merge_do(tmp_path, moi_truong):
    _, may1 = _remote_va_clone(tmp_path, moi_truong)
    _chay("chuan-bi-nhanh.sh", may1, moi_truong)
    (may1 / "so.md").write_text("nhánh tự động sửa\n", encoding="utf-8")
    assert _chay("day-nhanh-va-mo-pr.sh", may1, moi_truong).returncode == 0
    _them_vao_main(tmp_path, moi_truong, "so.md", "người dùng sửa trên main\n")

    _, may2 = _remote_va_clone(tmp_path, moi_truong, "may2")
    kq = _chay("chuan-bi-nhanh.sh", may2, moi_truong)
    assert kq.returncode == 1
    assert "xung đột" in kq.stderr
    assert not (may2 / ".git" / "MERGE_HEAD").exists()


def test_khong_xoa_commit_chua_day(tmp_path, moi_truong):
    _, may1 = _remote_va_clone(tmp_path, moi_truong)
    _chay("chuan-bi-nhanh.sh", may1, moi_truong)
    (may1 / "tuan-49.md").write_text("kỳ 1, đẩy lỗi\n", encoding="utf-8")
    _git(may1, "add", "-A", env=moi_truong)
    _git(may1, "commit", "-m", "chưa đẩy", env=moi_truong)
    kq = _chay("chuan-bi-nhanh.sh", may1, moi_truong)
    assert kq.returncode == 1 and "chưa có trên GitHub" in kq.stderr
    assert (may1 / "tuan-49.md").exists()


def test_thu_muc_ban_thi_dung(tmp_path, moi_truong):
    _, may1 = _remote_va_clone(tmp_path, moi_truong)
    (may1 / "nhap.md").write_text("chưa commit\n", encoding="utf-8")
    kq = _chay("chuan-bi-nhanh.sh", may1, moi_truong)
    assert kq.returncode == 1 and "chưa commit" in kq.stderr


def test_khong_co_gi_moi_thi_khong_day(tmp_path, moi_truong):
    remote, may1 = _remote_va_clone(tmp_path, moi_truong)
    _chay("chuan-bi-nhanh.sh", may1, moi_truong)
    kq = _chay("day-nhanh-va-mo-pr.sh", may1, moi_truong)
    assert kq.returncode == 0 and "không có gì mới" in kq.stdout
    assert _git(remote, "rev-parse", "--verify", NHANH, env=moi_truong, check=False).returncode != 0


def test_sai_nhanh_thi_khong_commit(tmp_path, moi_truong):
    _, may1 = _remote_va_clone(tmp_path, moi_truong)
    (may1 / "x.md").write_text("x\n", encoding="utf-8")
    kq = _chay("day-nhanh-va-mo-pr.sh", may1, moi_truong)
    assert kq.returncode == 1 and "chuan-bi-nhanh.sh" in kq.stderr


def test_chay_tren_may_chu_tu_dau_den_cuoi(tmp_path, moi_truong):
    """Chạy đủ vòng cron với lệnh claude giả: chuẩn bị nhánh, "nghiên cứu", kiểm thử, đẩy, mở PR."""
    remote = tmp_path / "remote.git"
    _git(tmp_path, "init", "--bare", "-b", "main", str(remote), env=moi_truong)
    hat = tmp_path / "hat"
    _git(tmp_path, "clone", str(remote), str(hat), env=moi_truong)
    shutil.copytree(TU_DONG, hat / "automation")
    (hat / "tests").mkdir()
    (hat / "tests" / "test_x.py").write_text("def test_x():\n    assert True\n", encoding="utf-8")
    (hat / ".gitignore").write_text("__pycache__/\n.pytest_cache/\n", encoding="utf-8")
    _git(hat, "add", "-A", env=moi_truong)
    _git(hat, "commit", "-m", "đầu", env=moi_truong)
    _git(hat, "push", "origin", "HEAD:main", env=moi_truong)

    claude_gia = tmp_path / "bin" / "claude"
    claude_gia.write_text('#!/usr/bin/env bash\nmkdir -p reports && echo "báo cáo" > reports/2026-W49-tu-dong.md\n',
                          encoding="utf-8")
    claude_gia.chmod(0o755)
    env = dict(moi_truong)

    may = tmp_path / "may-chu"
    _git(tmp_path, "clone", str(remote), str(may), env=env)
    kq = subprocess.run(["bash", "automation/chay-tren-may-chu.sh"], cwd=may, env=env, capture_output=True, text=True)
    assert kq.returncode == 0, kq.stdout + kq.stderr
    ds = _git(remote, "ls-tree", "-r", "--name-only", NHANH, env=env).stdout
    assert "reports/2026-W49-tu-dong.md" in ds
    assert "pr create" in (tmp_path / "gh.log").read_text(encoding="utf-8")

