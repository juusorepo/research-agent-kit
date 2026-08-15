import subprocess
import sys
from pathlib import Path

from harness import check_t13, load_layout

KIT = Path(__file__).resolve().parents[2]
INSTALL = KIT / "scripts" / "install.py"


def test_t13_on_example():
    result = check_t13(KIT / "examples" / "toy-study")
    assert result.passed, result.detail


def test_t13_fresh_init(tmp_path):
    dest = tmp_path / "new-paper"
    proc = subprocess.run(
        [
            sys.executable,
            str(INSTALL),
            str(dest),
            "--init",
            "--paper",
            "demo",
            "--preset",
            "by-paper",
            "--code",
            "r",
            "--manuscript",
            "quarto",
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 0
    result = check_t13(dest)
    assert result.passed, result.detail
    layout = load_layout(dest)
    assert layout["manuscript_format"] == "quarto"
    assert layout["code"] == "r"
    assert (dest / "docs").is_dir()
    assert (dest / "papers" / "demo" / "manuscript" / "paper.qmd").exists()


def test_numbered_preset(tmp_path):
    dest = tmp_path / "numbered"
    subprocess.run(
        [
            sys.executable,
            str(INSTALL),
            str(dest),
            "--init",
            "--paper",
            "p1",
            "--preset",
            "numbered",
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    result = check_t13(dest)
    assert result.passed, result.detail
    assert (dest / "02-scripts").is_dir()
    assert (dest / "06-docs" / "p1" / "ANALYSIS_PLAN.md").exists()


def test_word_stata_reserved(tmp_path):
    dest = tmp_path / "reserved"
    proc = subprocess.run(
        [
            sys.executable,
            str(INSTALL),
            str(dest),
            "--init",
            "--paper",
            "p1",
            "--code",
            "stata",
            "--manuscript",
            "word",
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    assert "not shipped" in (proc.stderr or "").lower() or (dest / "papers" / "p1" / "manuscript" / "README.md").exists()
    readme = (dest / "papers" / "p1" / "manuscript" / "README.md").read_text(encoding="utf-8")
    assert "not shipped" in readme.lower() or "Word" in readme
