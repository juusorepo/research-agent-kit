from pathlib import Path

KIT = Path(__file__).resolve().parents[2]


def test_start_md_no_runtime():
    text = (KIT / "START.md").read_text(encoding="utf-8")
    assert "Start the project" in text
    assert "Python" in text
    assert "not" in text.lower()
    assert "your name" in text.lower() or "lead researcher" in text.lower()


def test_start_skill_is_copy_not_installer():
    text = (KIT / "skills" / "start-research-project" / "SKILL.md").read_text(encoding="utf-8")
    assert "Lead researcher name" in text
    assert "No Python or R" in text or "no Python or R" in text
    assert "Copy" in text or "copy" in text
    assert "install.py" in text
    assert "optional" in text.lower()


def test_readme_does_not_require_python_to_start():
    text = (KIT / "README.md").read_text(encoding="utf-8")
    assert "python scripts/install.py PATH/to/new-project" not in text
    assert "Start the project" in text
