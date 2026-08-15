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
            "paper-1",
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
    assert layout["preset"] == "numbered"
    assert (dest / "01-data" / "raw").is_dir()
    assert (dest / "02-scripts").is_dir()
    assert (dest / "05-outputs" / "figures").is_dir()
    assert (dest / "06-docs").is_dir()
    assert (dest / "99-archive").is_dir()
    assert (dest / "ANALYSIS_PLAN.md").exists()
    assert (dest / "manuscript" / "paper.qmd").exists()
    assert (dest / "FOLDERS.md").exists()
    assert (dest / "MEMORY.md").exists()
    assert (dest / "contributions").is_dir()
    assert (dest / "notes" / "README.md").exists()
    assert (dest / "decisions" / "INDEX.md").exists()
    assert (dest / "decisions" / "RDR-000-template.md").exists()
    layout_text = (dest / "layout.yml").read_text(encoding="utf-8")
    assert "KIT_PATH" not in layout_text
    assert "kit_path:" in layout_text


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
    assert (dest / "01-data" / "metadata").is_dir()
    assert (dest / "ANALYSIS_PLAN.md").exists()


def test_by_paper_preset_still_works(tmp_path):
    dest = tmp_path / "nested"
    subprocess.run(
        [
            sys.executable,
            str(INSTALL),
            str(dest),
            "--init",
            "--paper",
            "demo",
            "--preset",
            "by-paper",
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    assert (dest / "papers" / "demo" / "manuscript" / "paper.qmd").exists()
    assert (dest / "papers" / "demo" / "contributions" / "template.md").exists()
    assert (dest / "papers" / "demo" / "notes" / "README.md").exists()
    assert (dest / "MEMORY.md").exists()


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
    readme_path = dest / "manuscript" / "README.md"
    assert "not shipped" in (proc.stderr or "").lower() or readme_path.exists()
    readme = readme_path.read_text(encoding="utf-8")
    assert "not shipped" in readme.lower() or "Word" in readme


def test_numbered_multipaper_inbox_is_per_paper(tmp_path):
    dest = tmp_path / "multi"
    subprocess.run(
        [
            sys.executable,
            str(INSTALL),
            str(dest),
            "--init",
            "--paper",
            "p1",
            "--preset",
            "numbered-multipaper",
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    assert (dest / "06-docs" / "p1" / "contributions" / "template.md").exists()
    assert (dest / "06-docs" / "p1" / "notes" / "README.md").exists()
    assert (dest / "06-docs" / "p1" / "decisions" / "INDEX.md").exists()
    assert (dest / "MEMORY.md").exists()
