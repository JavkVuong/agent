#!/usr/bin/env python3
"""Soát skill trong .claude/skills trước khi merge, nhất là skill chép từ bên ngoài (thư mục ext-*).

Chỉ dùng thư viện chuẩn Python, không gửi gì ra mạng.

Lỗi (trả về 1, phải sửa trước khi merge):
    - ký tự vô hình hoặc đảo chiều chữ (zero-width, bidi, Unicode Tag) trong mọi skill
    - skill ext-* có file không phải Markdown (script, JSON, CSV, nhị phân...)
    - skill ext-* có allowed-tools hoặc hooks trong phần đầu SKILL.md
    - skill ext-* có lệnh chạy ngầm dạng !`lệnh`
    - skill ext-* thiếu LICENSE, thiếu disable-model-invocation: true, hoặc chưa ghi trong THIRD_PARTY.md

Cảnh báo (chỉ in ra, người duyệt đọc lại dòng đó):
    - curl, wget, base64, eval, ~/.ssh, .env, "ignore previous", "don't tell the user"...

Cách dùng:
    python tools/soat_skill.py            # soát cả repo
    python tools/soat_skill.py --goc DIR  # soát repo khác
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

GOC = Path(__file__).resolve().parent.parent

# Ký tự không hiện trên màn hình nhưng AI vẫn đọc được: zero-width, đảo chiều chữ, Unicode Tag.
KY_TU_AN = re.compile(
    "[​-‏‪-‮⁠-⁤⁦-⁩﻿\U000e0000-\U000e007f]"
)
LENH_NGAM = re.compile(r"!`[^`]+`")
FILE_DUOC_PHEP = {"LICENSE", "LICENSE.txt", "LICENSE.md", "NOTICE", "NOTICE.txt", "NOTICE.md"}
MAU_CANH_BAO = [
    (re.compile(r"\bcurl\b|\bwget\b", re.I), "tải từ mạng"),
    (re.compile(r"\bbase64\b", re.I), "mã hoá base64"),
    (re.compile(r"\beval\s*\(|\bexec\s*\(", re.I), "chạy mã động"),
    (re.compile(r"~/\.ssh|id_rsa|id_ed25519", re.I), "khoá SSH"),
    (re.compile(r"(^|[\s`'\"/])\.env\b|\benviron\b|printenv", re.I), "biến môi trường"),
    (re.compile(r"ignore (all )?(the )?previous|disregard (all )?previous", re.I), "lời bảo bỏ qua chỉ dẫn"),
    (re.compile(r"(do not|don't|never) (tell|inform|show) the user", re.I), "lời bảo giấu người dùng"),
]


class ToolError(Exception):
    """Lỗi dự kiến: in ra cho người dùng, không in traceback."""


@dataclass
class KetQua:
    loi: list[str] = field(default_factory=list)
    canh_bao: list[str] = field(default_factory=list)
    so_skill: int = 0
    so_skill_ngoai: int = 0


def _phan_dau(text: str) -> str:
    """Trả về phần frontmatter (giữa hai dòng ---) của SKILL.md, rỗng nếu không có."""
    if not text.startswith("---"):
        return ""
    cuoi = text.find("\n---", 3)
    return text[3:cuoi] if cuoi != -1 else ""


def _ten_trong_third_party(goc: Path) -> set[str]:
    path = goc / "THIRD_PARTY.md"
    if not path.exists():
        return set()
    return set(re.findall(r"`(ext-[a-z0-9-]+)`", path.read_text(encoding="utf-8")))


def soat(goc: Path) -> KetQua:
    """Soát mọi skill trong goc/.claude/skills và trả về danh sách lỗi, cảnh báo."""
    thu_muc = goc / ".claude" / "skills"
    if not thu_muc.is_dir():
        raise ToolError(f"Không thấy thư mục {thu_muc}. Chạy lệnh trong thư mục repo hoặc dùng --goc.")
    kq = KetQua()
    da_ghi = _ten_trong_third_party(goc)

    for skill in sorted(p for p in thu_muc.iterdir() if p.is_dir()):
        kq.so_skill += 1
        ngoai = skill.name.startswith("ext-")
        kq.so_skill_ngoai += ngoai
        ten = f".claude/skills/{skill.name}"

        if not (skill / "SKILL.md").exists():
            kq.loi.append(f"{ten}: thiếu SKILL.md.")
        if ngoai:
            if not any((skill / f).exists() for f in FILE_DUOC_PHEP if f.startswith("LICENSE")):
                kq.loi.append(f"{ten}: thiếu file LICENSE của tác giả gốc. Chép LICENSE từ repo nguồn vào thư mục này.")
            if skill.name not in da_ghi:
                kq.loi.append(f"{ten}: chưa ghi trong THIRD_PARTY.md (nguồn, commit, giấy phép).")

        for f in sorted(p for p in skill.rglob("*") if p.is_file()):
            rel = f.relative_to(goc).as_posix()
            if ngoai and f.suffix.lower() != ".md" and f.name not in FILE_DUOC_PHEP:
                kq.loi.append(f"{rel}: skill ngoài chỉ được chứa Markdown. Xoá file này hoặc chép nội dung cần dùng vào file .md.")
                continue
            try:
                text = f.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                kq.loi.append(f"{rel}: không đọc được dạng chữ UTF-8. Xoá file nhị phân khỏi skill.")
                continue

            for so, dong in enumerate(text.splitlines(), 1):
                an = KY_TU_AN.findall(dong)
                if an:
                    ma = ", ".join(sorted({f"U+{ord(c):04X}" for c in an}))
                    kq.loi.append(f"{rel}:{so}: có ký tự vô hình ({ma}). Xoá ký tự đó rồi đọc lại dòng này.")
                if not ngoai:
                    continue
                if LENH_NGAM.search(dong):
                    kq.loi.append(f"{rel}:{so}: có lệnh chạy ngầm dạng !`...`. Xoá dòng này.")
                for mau, nghia in MAU_CANH_BAO:
                    if mau.search(dong):
                        kq.canh_bao.append(f"{rel}:{so}: {nghia}: {dong.strip()[:120]}")

            if ngoai and f.name == "SKILL.md":
                dau = _phan_dau(text)
                if re.search(r"^allowed-tools\s*:", dau, re.M):
                    kq.loi.append(f"{rel}: skill ngoài không được có allowed-tools. Xoá dòng đó.")
                if re.search(r"^hooks\s*:", dau, re.M):
                    kq.loi.append(f"{rel}: skill ngoài không được có hooks. Xoá phần đó.")
                if not re.search(r"^disable-model-invocation\s*:\s*true\s*$", dau, re.M):
                    kq.loi.append(f"{rel}: thêm dòng 'disable-model-invocation: true' vào phần đầu.")
                if not re.search(rf"^name\s*:\s*{re.escape(skill.name)}\s*$", dau, re.M):
                    kq.loi.append(f"{rel}: dòng name phải là '{skill.name}' (trùng tên thư mục).")
    return kq


def main(argv: list[str] | None = None) -> int:
    for luong in (sys.stdout, sys.stderr):
        try:
            luong.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass
    p = argparse.ArgumentParser(prog="soat_skill.py", description="Soát skill trước khi merge.")
    p.add_argument("--goc", type=Path, default=GOC, help="thư mục gốc của repo (mặc định: repo này)")
    a = p.parse_args(argv)
    try:
        kq = soat(a.goc)
    except ToolError as e:
        print(f"Lỗi: {e}", file=sys.stderr)
        return 1
    for c in kq.canh_bao:
        print(f"Cảnh báo: {c}")
    for l in kq.loi:
        print(f"Lỗi: {l}")
    print(
        f"Đã soát {kq.so_skill} skill ({kq.so_skill_ngoai} skill ngoài): "
        f"{len(kq.loi)} lỗi, {len(kq.canh_bao)} cảnh báo."
    )
    if kq.canh_bao and not kq.loi:
        print("Cảnh báo không chặn merge. Đọc lại từng dòng được nêu và chắc rằng nó chỉ là ví dụ, không phải lệnh cho AI.")
    return 1 if kq.loi else 0


if __name__ == "__main__":
    sys.exit(main())
