"""Kiểm thử tools/kb.py trên một bản sao sổ kiến thức tạm."""

import re
import shutil
import sys
from pathlib import Path

import pytest

GOC = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(GOC / "tools"))
import kb  # noqa: E402


@pytest.fixture
def repo(tmp_path):
    shutil.copytree(GOC / "knowledge", tmp_path / "knowledge")
    return tmp_path


def _doc(p):
    return p.read_text(encoding="utf-8")


def test_hoc_tang_id_va_lam_sach_o(repo):
    ma = kb.them_bai_hoc(repo, "gia", "Trả tuỳ ý | thắng\ngiá cố định", "W48", "cao", "kenh", "2026-11-30")
    assert re.fullmatch(r"L-20261130-[0-9a-f]{4}", ma)
    text = _doc(repo / "knowledge/learnings/LEARNINGS.md")
    assert f"| {ma} | 2026-11-30 | gia | Trả tuỳ ý / thắng giá cố định | W48 | cao | kenh | hieu-luc |" in text


def test_id_khong_trung_khi_ngau_nhien_lap(repo, monkeypatch):
    gia_tri = iter(["aaaa", "aaaa", "bbbb"])
    monkeypatch.setattr(kb.secrets, "token_hex", lambda n: next(gia_tri))
    a = kb.them_bai_hoc(repo, "gia", "Một", "", "cao", "kenh", "2026-11-30")
    b = kb.them_bai_hoc(repo, "gia", "Hai", "", "cao", "kenh", "2026-11-30")
    assert (a, b) == ("L-20261130-aaaa", "L-20261130-bbbb")


def test_id_cu_van_dung_duoc(repo):
    ma = kb.them_bai_hoc(repo, "gia", "Mới", "", "cao", "kenh")
    kb.thay_the_bai_hoc(repo, "L-0001", ma)
    assert f"thay-the bởi {ma}" in _doc(repo / "knowledge/learnings/LEARNINGS.md")


def test_hoc_do_tin_sai(repo):
    with pytest.raises(kb.ToolError):
        kb.them_bai_hoc(repo, "x", "y", "", "rat-cao", "kenh")


def test_hoc_bai_hoc_trong(repo):
    with pytest.raises(kb.ToolError):
        kb.them_bai_hoc(repo, "x", "   ", "", "cao", "kenh")


def test_thay_the_giu_bai_cu(repo):
    truoc = kb.tong_quan(repo)["bai_hoc_hieu_luc"]
    ma = kb.them_bai_hoc(repo, "noi-dung", "Bài mới", "", "cao", "kenh")
    kb.thay_the_bai_hoc(repo, "L-0002", ma)
    text = _doc(repo / "knowledge/learnings/LEARNINGS.md")
    assert "| L-0002 |" in text and f"thay-the bởi {ma}" in text
    assert kb.tong_quan(repo)["bai_hoc_hieu_luc"] == truoc  # thêm 1, thay thế 1
    with pytest.raises(kb.ToolError):
        kb.thay_the_bai_hoc(repo, "L-0999", ma)


def test_thi_nghiem_mo_dong_tao_bai_hoc(repo):
    dang_chay = len(kb.tong_quan(repo)["thi_nghiem_dang_chay"])
    ma = kb.mo_thi_nghiem(repo, "Gói đôi bán chạy hơn", "14 ngày", "doanh thu", "+20%", "2026-11-25")
    assert re.fullmatch(r"E-20261125-[0-9a-f]{4}", ma)
    assert len(kb.tong_quan(repo)["thi_nghiem_dang_chay"]) == dang_chay + 1
    bai = kb.dong_thi_nghiem(repo, ma, "trước 45 USD, sau 40 USD", "thua", "2026-12-09")
    text = _doc(repo / "knowledge/learnings/LEARNINGS.md")
    assert f"| {bai} | 2026-12-09 | thi-nghiem | Sai: Gói đôi bán chạy hơn |" in text
    with pytest.raises(kb.ToolError):
        kb.dong_thi_nghiem(repo, ma, "lại", "thang")
    with pytest.raises(kb.ToolError):
        kb.dong_thi_nghiem(repo, "E-0099", "x", "thang")


def test_file_qua_han(repo):
    # Đặt mọi ngày cập nhật về 25/11/2026 để kiểm thử không hỏng khi lần chạy định kỳ cập nhật sổ thật.
    for f in (repo / "knowledge").rglob("*.md"):
        f.write_text(re.sub(r"(?m)^cap_nhat: .*$", "cap_nhat: 2026-11-25", _doc(f)), encoding="utf-8")
    assert kb.file_qua_han(repo, "2026-11-26") == []
    ds = dict(kb.file_qua_han(repo, "2026-12-10"))
    assert ds["knowledge/market/trends-log.md"] == 8
    assert ds["knowledge/products/vutty.md"] == 1
    assert "knowledge/rules/compliance.md" not in ds


def test_cham_diem_kenh():
    h = {"khach_khop": "5", "y_dinh_mua": "5", "keo_dai": "5", "quy_mo": "5", "cong_suc": "1",
         "cho_phep_quang_ba": "co"}
    assert kb.cham_diem(h) == 100
    h["cong_suc"] = "5"
    assert kb.cham_diem(h) == 88
    h["cho_phep_quang_ba"] = "khong"
    assert kb.cham_diem(h) == 0


def test_cham_diem_ngoai_thang(tmp_path):
    p = tmp_path / "k.csv"
    p.write_text("ten,khach_khop,cho_phep_quang_ba\nA,9,co\n", encoding="utf-8")
    with pytest.raises(kb.ToolError, match="1 đến 5"):
        kb.xep_hang_kenh(p)


def test_xep_hang_mau(repo):
    kq = kb.xep_hang_kenh(repo / "knowledge/market/channels.csv")
    diem = [d for _, d, _ in kq]
    assert diem == sorted(diem, reverse=True)
    assert kq[-1][1] == 0 and "không cho" in kq[-1][2]
    assert kq[0][0] in ("AlternativeTo (Termius)", "README GitHub")


def test_so_lieu_mau(repo):
    kq = kb.tom_tat_so_lieu(repo / "knowledge/performance/mau.csv")
    t = kq["tong"]
    assert t["luot_xem"] == 420 and t["don"] == 6
    assert t["chuyen_doi_pct"] == 1.43
    assert [k for k, _ in kq["nhom"]] == ["github", "reddit", "direct", "discover"]


def test_so_lieu_thieu_cot(tmp_path):
    p = tmp_path / "s.csv"
    p.write_text("nguon,luot_xem\nA,10\n", encoding="utf-8")
    with pytest.raises(kb.ToolError, match="don"):
        kb.tom_tat_so_lieu(p)


def test_so_lieu_cot_nhom_khong_co(repo):
    with pytest.raises(kb.ToolError, match="kieu"):
        kb.tom_tat_so_lieu(repo / "knowledge/performance/mau.csv", "kieu")


def test_main_loi_tra_ve_1(repo, capsys):
    assert kb.main(["--goc", str(repo), "so-lieu", str(repo / "khong-co.csv")]) == 1
    assert "Lỗi:" in capsys.readouterr().err


def test_main_cac_lenh(repo, capsys):
    g = ["--goc", str(repo), "--ngay", "2026-11-26"]
    assert kb.main(g + ["hoc", "--chu-de", "kenh", "--bai-hoc", "README kéo khách"]) == 0
    assert kb.main(g + ["thu-nghiem", "--gia-thuyet", "a", "--cach-thu", "b", "--chi-so", "c", "--nguong", "d"]) == 0
    ma_tn = re.search(r"Đã mở thí nghiệm (E-\S+)\.", capsys.readouterr().out).group(1)
    assert kb.main(g + ["ket-thuc", ma_tn, "--ket-qua", "x", "--ket-luan", "chua-ro"]) == 0
    assert kb.main(g + ["cu"]) == 0
    assert kb.main(g + ["cham-diem"]) == 0
    assert kb.main(g + ["so-lieu", str(repo / "knowledge/performance/mau.csv")]) == 0
    assert kb.main(g + ["tong-quan"]) == 0
    out = capsys.readouterr().out
    assert "Mọi file kiến thức còn hạn." in out
    assert "chuyển đổi 1.43%" in out
