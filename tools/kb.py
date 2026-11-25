#!/usr/bin/env python3
"""Công cụ quản lý sổ kiến thức của đội agent bán phần mềm trên Gumroad.

Chỉ dùng thư viện chuẩn Python để chạy được trên Windows và macOS mà không cần cài gì.

Các lệnh:
    hoc         ghi một bài học mới vào knowledge/learnings/LEARNINGS.md
    thu-nghiem  mở một thí nghiệm mới trong knowledge/experiments/EXPERIMENTS.md
    ket-thuc    đóng thí nghiệm, ghi kết quả và tự tạo bài học
    cu          liệt kê file kiến thức đã quá hạn kiểm tra lại
    cham-diem   chấm điểm kênh quảng bá trong knowledge/market/channels.csv
    so-lieu     tóm tắt lượt xem trang, đơn, doanh thu (CSV) theo nguồn khách
    tong-quan   tình trạng sổ kiến thức
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import re
import secrets
import sys
from pathlib import Path

GOC = Path(__file__).resolve().parent.parent
KIEN_THUC = GOC / "knowledge"

DO_TIN = ("thap", "trung-binh", "cao")
KET_LUAN = ("thang", "thua", "chua-ro")

TIEU_DE_BAI_HOC = (
    "| ID | Ngày | Chủ đề | Bài học | Bằng chứng | Độ tin | Nguồn | Trạng thái |\n"
    "|---|---|---|---|---|---|---|---|\n"
)
TIEU_DE_THI_NGHIEM = (
    "| ID | Ngày mở | Giả thuyết | Cách thử | Chỉ số | Ngưỡng thắng | Trạng thái | Kết quả |\n"
    "|---|---|---|---|---|---|---|---|\n"
)


class ToolError(Exception):
    """Lỗi dự kiến: in ra cho người dùng, không in traceback."""


# ---------- tiện ích chung ----------

def _hom_nay(ngay: str | None = None) -> dt.date:
    if ngay:
        try:
            return dt.date.fromisoformat(ngay)
        except ValueError as e:
            raise ToolError(f"Ngày '{ngay}' sai dạng. Viết theo dạng 2026-11-25.") from e
    return dt.date.today()


def _o(text: str) -> str:
    """Làm sạch một ô bảng markdown: bỏ xuống dòng và dấu |."""
    return " ".join(str(text).replace("|", "/").split())


def _doc(path: Path) -> str:
    if not path.exists():
        raise ToolError(f"Không thấy file {path}. Chạy lệnh trong thư mục repo hoặc dùng --goc.")
    return path.read_text(encoding="utf-8")


def _ghi(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def _dong_bang(text: str, tien_to: str) -> list[list[str]]:
    hang = []
    for dong in text.splitlines():
        if dong.startswith(f"| {tien_to}-"):
            hang.append([c.strip() for c in dong.strip().strip("|").split("|")])
    return hang


def _id_moi(text: str, tien_to: str, ngay: dt.date) -> str:
    """ID gồm ngày và 4 ký tự ngẫu nhiên, ví dụ L-20261125-3f9a.

    Nhiều người hoặc nhiều máy chủ ghi cùng lúc trên các nhánh khác nhau vẫn không trùng ID,
    nên khi gộp nhánh chỉ cần giữ cả hai dòng.
    """
    for _ in range(50):
        ma = f"{tien_to}-{ngay.strftime('%Y%m%d')}-{secrets.token_hex(2)}"
        if f"| {ma} |" not in text:
            return ma
    raise ToolError("Không tạo được ID mới. Thử chạy lại lệnh.")


def _dam_bao_bang(path: Path, tieu_de_file: str, tieu_de_bang: str) -> str:
    if not path.exists():
        _ghi(path, f"{tieu_de_file}\n\n{tieu_de_bang}")
    text = _doc(path)
    if tieu_de_bang.splitlines()[0] not in text:
        raise ToolError(f"File {path} không có bảng đúng mẫu. Đừng sửa dòng tiêu đề bảng.")
    return text


def _them_dong(text: str, dong: str) -> str:
    if not text.endswith("\n"):
        text += "\n"
    return text + dong + "\n"


# ---------- bài học ----------

def them_bai_hoc(goc: Path, chu_de: str, bai_hoc: str, bang_chung: str, do_tin: str,
                 nguon: str, ngay: str | None = None) -> str:
    """Ghi một bài học và trả về ID mới."""
    if do_tin not in DO_TIN:
        raise ToolError(f"Độ tin phải là một trong: {', '.join(DO_TIN)}.")
    if not bai_hoc.strip():
        raise ToolError("Bài học đang trống. Viết một câu nói rõ điều đã học.")
    path = goc / "knowledge" / "learnings" / "LEARNINGS.md"
    text = _dam_bao_bang(path, "# Sổ bài học", TIEU_DE_BAI_HOC)
    hom_nay = _hom_nay(ngay)
    ma = _id_moi(text, "L", hom_nay)
    dong = (f"| {ma} | {hom_nay.isoformat()} | {_o(chu_de)} | {_o(bai_hoc)} | "
            f"{_o(bang_chung) or '-'} | {do_tin} | {_o(nguon) or '-'} | hieu-luc |")
    _ghi(path, _them_dong(text, dong))
    return ma


def thay_the_bai_hoc(goc: Path, ma_cu: str, ma_moi: str) -> None:
    """Đánh dấu bài học cũ đã bị bài học mới thay thế (không xoá)."""
    path = goc / "knowledge" / "learnings" / "LEARNINGS.md"
    text = _doc(path)
    dong_moi, thay = [], False
    for dong in text.splitlines():
        if dong.startswith(f"| {ma_cu} |"):
            o = dong.strip().strip("|").split("|")
            o[-1] = f" thay-the bởi {ma_moi} "
            dong = "|" + "|".join(o) + "|"
            thay = True
        dong_moi.append(dong)
    if not thay:
        raise ToolError(f"Không thấy bài học {ma_cu}.")
    _ghi(path, "\n".join(dong_moi) + "\n")


# ---------- thí nghiệm ----------

def mo_thi_nghiem(goc: Path, gia_thuyet: str, cach_thu: str, chi_so: str, nguong: str,
                  ngay: str | None = None) -> str:
    path = goc / "knowledge" / "experiments" / "EXPERIMENTS.md"
    text = _dam_bao_bang(path, "# Sổ thí nghiệm", TIEU_DE_THI_NGHIEM)
    hom_nay = _hom_nay(ngay)
    ma = _id_moi(text, "E", hom_nay)
    dong = (f"| {ma} | {hom_nay.isoformat()} | {_o(gia_thuyet)} | {_o(cach_thu)} | "
            f"{_o(chi_so)} | {_o(nguong)} | dang-chay | - |")
    _ghi(path, _them_dong(text, dong))
    return ma


def dong_thi_nghiem(goc: Path, ma: str, ket_qua: str, ket_luan: str,
                    ngay: str | None = None) -> str:
    """Đóng thí nghiệm và tự ghi một bài học. Trả về ID bài học."""
    if ket_luan not in KET_LUAN:
        raise ToolError(f"Kết luận phải là một trong: {', '.join(KET_LUAN)}.")
    path = goc / "knowledge" / "experiments" / "EXPERIMENTS.md"
    text = _doc(path)
    dong_moi, gia_thuyet = [], None
    for dong in text.splitlines():
        if dong.startswith(f"| {ma} |"):
            o = [c.strip() for c in dong.strip().strip("|").split("|")]
            if o[6] != "dang-chay":
                raise ToolError(f"Thí nghiệm {ma} đã đóng rồi ({o[6]}).")
            gia_thuyet = o[2]
            o[6] = ket_luan
            o[7] = _o(ket_qua)
            dong = "| " + " | ".join(o) + " |"
        dong_moi.append(dong)
    if gia_thuyet is None:
        raise ToolError(f"Không thấy thí nghiệm {ma}. Xem danh sách bằng: python tools/kb.py tong-quan")
    _ghi(path, "\n".join(dong_moi) + "\n")
    nhan = {"thang": "Đúng", "thua": "Sai", "chua-ro": "Chưa rõ"}[ket_luan]
    return them_bai_hoc(goc, "thi-nghiem", f"{nhan}: {gia_thuyet}", f"{ma}: {ket_qua}",
                        "cao" if ket_luan != "chua-ro" else "thap", "kenh", ngay)


# ---------- file quá hạn ----------

def _dau_file(text: str) -> dict[str, str]:
    m = re.match(r"^---\n(.*?)\n---", text, flags=re.S)
    if not m:
        return {}
    kq = {}
    for dong in m.group(1).splitlines():
        if ":" in dong:
            k, v = dong.split(":", 1)
            kq[k.strip()] = v.strip()
    return kq


def file_qua_han(goc: Path, ngay: str | None = None) -> list[tuple[str, int]]:
    """Trả về (đường dẫn, số ngày quá hạn) cho các file kiến thức cần kiểm tra lại."""
    hom_nay = _hom_nay(ngay)
    kq = []
    for p in sorted((goc / "knowledge").rglob("*.md")):
        dau = _dau_file(p.read_text(encoding="utf-8"))
        if "cap_nhat" not in dau:
            continue
        try:
            cap_nhat = dt.date.fromisoformat(dau["cap_nhat"])
            han = int(dau.get("can_kiem_tra_lai_sau_ngay", "30"))
        except ValueError:
            kq.append((p.relative_to(goc).as_posix(), -1))
            continue
        tre = (hom_nay - cap_nhat).days - han
        if tre > 0:
            kq.append((p.relative_to(goc).as_posix(), tre))
    return kq


# ---------- chấm điểm kênh quảng bá ----------

def _so(gia_tri: str, ten: str, dong: int) -> float:
    try:
        return float(str(gia_tri).replace(",", ".").strip() or 0)
    except ValueError as e:
        raise ToolError(f"Dòng {dong}: cột '{ten}' phải là số, đang là '{gia_tri}'.") from e


def _thang_5(hang: dict[str, str], ten: str, dong: int, mac_dinh: float = 3) -> float:
    gia_tri = hang.get(ten, "")
    v = _so(gia_tri, ten, dong) if str(gia_tri).strip() else mac_dinh
    if not 1 <= v <= 5:
        raise ToolError(f"Dòng {dong}: cột '{ten}' phải từ 1 đến 5, đang là {gia_tri}.")
    return v


def cham_diem(hang: dict[str, str], dong: int = 0) -> float:
    """Điểm 0 đến 100 cho một kênh quảng bá. Trọng số giải thích trong .claude/skills/gr-channel-pick/SKILL.md."""
    khop = _thang_5(hang, "khach_khop", dong)
    y_dinh = _thang_5(hang, "y_dinh_mua", dong)
    keo_dai = _thang_5(hang, "keo_dai", dong)
    quy_mo = _thang_5(hang, "quy_mo", dong)
    cong_suc = _thang_5(hang, "cong_suc", dong)
    cho_phep = str(hang.get("cho_phep_quang_ba", "")).strip().lower() in ("co", "có", "yes", "1", "x")
    if not cho_phep:
        return 0.0                                           # luật cộng đồng cấm thì không đăng
    diem = (khop / 5 * 25 + y_dinh / 5 * 25 + keo_dai / 5 * 20
            + quy_mo / 5 * 15 + (6 - cong_suc) / 5 * 15)
    return round(diem, 1)


def xep_hang_kenh(path: Path) -> list[tuple[str, float, str]]:
    with open(path, encoding="utf-8-sig", newline="") as f:
        hang = list(csv.DictReader(f))
    if not hang:
        raise ToolError(f"File {path} chưa có kênh nào.")
    if "ten" not in hang[0]:
        raise ToolError(f"File {path} thiếu cột 'ten'. Xem mẫu ở knowledge/market/channels.csv.")
    kq = []
    for i, h in enumerate(hang, start=2):
        d = cham_diem(h, i)
        ghi_chu = "" if d else "luật cộng đồng không cho tự quảng bá"
        kq.append((h["ten"], d, ghi_chu))
    return sorted(kq, key=lambda x: -x[1])


# ---------- số liệu bán hàng ----------

COT_SO_LIEU = ("nguon", "luot_xem", "don")


def tom_tat_so_lieu(path: Path, nhom_theo: str = "nguon") -> dict:
    """Tóm tắt lượt xem trang, đơn, doanh thu theo nguồn khách (hoặc cột khác)."""
    with open(path, encoding="utf-8-sig", newline="") as f:
        hang = list(csv.DictReader(f))
    if not hang:
        raise ToolError(f"File {path} không có dòng số liệu nào.")
    thieu = [c for c in COT_SO_LIEU if c not in hang[0]]
    if thieu:
        raise ToolError(f"File {path} thiếu cột: {', '.join(thieu)}. Xem mẫu ở knowledge/performance/README.md.")
    if nhom_theo not in hang[0]:
        raise ToolError(f"File {path} không có cột '{nhom_theo}' để nhóm.")
    nhom: dict[str, dict[str, float]] = {}
    tong = {"dong": 0, "luot_xem": 0.0, "don": 0.0, "doanh_thu": 0.0}
    for i, h in enumerate(hang, start=2):
        k = (h.get(nhom_theo) or "khong-ro").strip()
        g = nhom.setdefault(k, {"dong": 0, "luot_xem": 0.0, "don": 0.0, "doanh_thu": 0.0})
        for d in (g, tong):
            d["dong"] += 1
            d["luot_xem"] += _so(h["luot_xem"], "luot_xem", i)
            d["don"] += _so(h["don"], "don", i)
            d["doanh_thu"] += _so(h.get("doanh_thu", 0), "doanh_thu", i)

    def ty_le(d):
        xem = d["luot_xem"] or 1
        return {
            **d,
            "chuyen_doi_pct": round(d["don"] / xem * 100, 2),
            "doanh_thu_moi_1000_xem": round(d["doanh_thu"] / xem * 1000, 2),
        }

    return {
        "tong": ty_le(tong),
        "nhom": sorted(((k, ty_le(v)) for k, v in nhom.items()),
                       key=lambda kv: (-kv[1]["doanh_thu"], -kv[1]["don"])),
    }


# ---------- tổng quan ----------

def tong_quan(goc: Path, ngay: str | None = None) -> dict:
    hoc = goc / "knowledge" / "learnings" / "LEARNINGS.md"
    tn = goc / "knowledge" / "experiments" / "EXPERIMENTS.md"
    bai = _dong_bang(hoc.read_text(encoding="utf-8"), "L") if hoc.exists() else []
    thi = _dong_bang(tn.read_text(encoding="utf-8"), "E") if tn.exists() else []
    return {
        "bai_hoc_hieu_luc": sum(1 for b in bai if b[-1] == "hieu-luc"),
        "bai_hoc_tong": len(bai),
        "thi_nghiem_dang_chay": [t[0] + ": " + t[2] for t in thi if t[6] == "dang-chay"],
        "file_qua_han": file_qua_han(goc, ngay),
    }


# ---------- dòng lệnh ----------

def _parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="kb.py", description="Quản lý sổ kiến thức của đội agent Gumroad.")
    p.add_argument("--goc", type=Path, default=GOC, help="thư mục repo (mặc định: thư mục chứa tools/)")
    p.add_argument("--ngay", help="ngày làm việc dạng 2026-11-25 (mặc định: hôm nay)")
    sub = p.add_subparsers(dest="lenh", required=True)

    s = sub.add_parser("hoc", help="ghi một bài học mới")
    s.add_argument("--chu-de", required=True, help="ví dụ: gia, trang-ban, kenh, noi-dung, thuong-hieu")
    s.add_argument("--bai-hoc", required=True, help="một câu nói rõ điều đã học")
    s.add_argument("--bang-chung", default="", help="số đo hoặc link chứng minh")
    s.add_argument("--do-tin", default="trung-binh", choices=DO_TIN)
    s.add_argument("--nguon", default="kenh", help="'kenh' nếu tự đo, hoặc link")
    s.add_argument("--thay-the", help="ID bài học cũ mà bài này thay thế, ví dụ L-0003")

    s = sub.add_parser("thu-nghiem", help="mở thí nghiệm mới")
    s.add_argument("--gia-thuyet", required=True)
    s.add_argument("--cach-thu", required=True)
    s.add_argument("--chi-so", required=True, help="ví dụ: tỷ lệ chuyển đổi trang Gumroad")
    s.add_argument("--nguong", required=True, help="ví dụ: cao hơn 20% so với trung bình kênh")

    s = sub.add_parser("ket-thuc", help="đóng thí nghiệm và ghi bài học")
    s.add_argument("ma", help="ID thí nghiệm, ví dụ E-0001")
    s.add_argument("--ket-qua", required=True)
    s.add_argument("--ket-luan", required=True, choices=KET_LUAN)

    sub.add_parser("cu", help="liệt kê file kiến thức quá hạn kiểm tra")

    s = sub.add_parser("cham-diem", help="xếp hạng kênh quảng bá")
    s.add_argument("file", nargs="?", type=Path, help="mặc định: knowledge/market/channels.csv")

    s = sub.add_parser("so-lieu", help="tóm tắt lượt xem, đơn, doanh thu")
    s.add_argument("file", type=Path)
    s.add_argument("--nhom-theo", default="nguon", help="cột để nhóm: nguon, san_pham, gia...")

    sub.add_parser("tong-quan", help="tình trạng sổ kiến thức")
    return p


def main(argv: list[str] | None = None) -> int:
    for luong in (sys.stdout, sys.stderr):
        try:
            luong.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass
    args = _parser().parse_args(argv)
    goc: Path = args.goc
    try:
        if args.lenh == "hoc":
            ma = them_bai_hoc(goc, args.chu_de, args.bai_hoc, args.bang_chung, args.do_tin, args.nguon, args.ngay)
            if args.thay_the:
                thay_the_bai_hoc(goc, args.thay_the, ma)
            print(f"Đã ghi bài học {ma}.")
        elif args.lenh == "thu-nghiem":
            ma = mo_thi_nghiem(goc, args.gia_thuyet, args.cach_thu, args.chi_so, args.nguong, args.ngay)
            print(f"Đã mở thí nghiệm {ma}. Khi có kết quả: python tools/kb.py ket-thuc {ma} --ket-qua ... --ket-luan thang")
        elif args.lenh == "ket-thuc":
            ma = dong_thi_nghiem(goc, args.ma, args.ket_qua, args.ket_luan, args.ngay)
            print(f"Đã đóng {args.ma} và ghi bài học {ma}.")
        elif args.lenh == "cu":
            ds = file_qua_han(goc, args.ngay)
            if not ds:
                print("Mọi file kiến thức còn hạn.")
            for duong, tre in ds:
                print(f"{duong}: " + ("ngày cập nhật sai dạng" if tre < 0 else f"quá hạn {tre} ngày"))
        elif args.lenh == "cham-diem":
            path = args.file or goc / "knowledge" / "market" / "channels.csv"
            if not path.exists():
                raise ToolError(f"Không thấy file {path}.")
            for i, (ten, d, ghi_chu) in enumerate(xep_hang_kenh(path), start=1):
                print(f"{i:>2}. {d:>5} điểm  {ten}" + (f"  ({ghi_chu})" if ghi_chu else ""))
        elif args.lenh == "so-lieu":
            if not args.file.exists():
                raise ToolError(f"Không thấy file {args.file}.")
            kq = tom_tat_so_lieu(args.file, args.nhom_theo)
            t = kq["tong"]
            print(f"Tổng: {int(t['luot_xem'])} lượt xem trang, {int(t['don'])} đơn, "
                  f"doanh thu {t['doanh_thu']:.2f}, chuyển đổi {t['chuyen_doi_pct']}%, "
                  f"{t['doanh_thu_moi_1000_xem']} trên 1.000 lượt xem.")
            print(f"Theo {args.nhom_theo} (doanh thu cao xuống thấp):")
            for k, v in kq["nhom"]:
                print(f"  {k}: {int(v['luot_xem'])} xem, {int(v['don'])} đơn, doanh thu {v['doanh_thu']:.2f}, "
                      f"chuyển đổi {v['chuyen_doi_pct']}%")
        elif args.lenh == "tong-quan":
            kq = tong_quan(goc, args.ngay)
            print(f"Bài học còn hiệu lực: {kq['bai_hoc_hieu_luc']} / {kq['bai_hoc_tong']}")
            print(f"Thí nghiệm đang chạy: {len(kq['thi_nghiem_dang_chay'])}")
            for t in kq["thi_nghiem_dang_chay"]:
                print(f"  {t}")
            print(f"File quá hạn kiểm tra: {len(kq['file_qua_han'])}")
            for duong, tre in kq["file_qua_han"]:
                print(f"  {duong}")
    except ToolError as e:
        print(f"Lỗi: {e}", file=sys.stderr)
        return 1
    except (OSError, csv.Error) as e:
        print(f"Lỗi: không đọc hoặc ghi được file ({e}). Kiểm tra đường dẫn và quyền ghi.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
