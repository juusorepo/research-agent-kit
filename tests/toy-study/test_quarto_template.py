from pathlib import Path

KIT = Path(__file__).resolve().parents[2]
QMD = (KIT / "templates" / "manuscript" / "quarto" / "paper.qmd").read_text(encoding="utf-8")
HELPERS = (KIT / "templates" / "manuscript" / "quarto" / "helpers.R").read_text(encoding="utf-8")


def test_quarto_uses_apa_and_approved_only():
    assert "apaquarto-docx" in QMD
    assert "apaquarto-html" in QMD
    assert "require_approved" in QMD or "require_approved" in HELPERS
    assert "01-data/metadata" in HELPERS
    assert "05-outputs/figures" in HELPERS
    assert "row-level" in QMD.lower() or "No row-level" in QMD
    assert "later Quarto profile" not in QMD


def test_helpers_refuse_draft_and_synthetic():
    assert "approved" in HELPERS
    assert "synthetic" in HELPERS
    assert "Do not cite" in HELPERS
