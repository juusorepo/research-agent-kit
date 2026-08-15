from pathlib import Path
from shutil import copytree

from harness import check_t2, check_t6, check_t8, check_t10, check_t11

EXAMPLE = Path(__file__).resolve().parents[2] / "examples" / "toy-study"


def _copy_example(tmp_path: Path) -> Path:
    dest = tmp_path / "proj"
    copytree(EXAMPLE, dest, ignore=lambda *_: {".agents"})
    return dest


def test_t2_proposal_fixture(tmp_path):
    root = _copy_example(tmp_path)
    prop = root / "papers" / "toy-study" / "proposals"
    prop.mkdir(parents=True, exist_ok=True)
    (prop / "A-002.md").write_text("# A-002 — Extra table\nagreed:\nproposed_by: AI\n", encoding="utf-8")
    result = check_t2(root)
    assert result.passed, result.detail


def test_t6_decision_fixture(tmp_path):
    root = _copy_example(tmp_path)
    dec = root / "papers" / "toy-study" / "decisions"
    dec.mkdir(parents=True, exist_ok=True)
    (dec / "RDR-001-coding.md").write_text(
        "id: RDR-001\nstatus: proposed\nproposed_by: AI\ndecision: collapse top two\n",
        encoding="utf-8",
    )
    result = check_t6(root)
    assert result.passed, result.detail


def test_t8_approved_fixture(tmp_path):
    root = _copy_example(tmp_path)
    out = root / "papers" / "toy-study" / "outputs" / "OUT-001.yml"
    text = out.read_text(encoding="utf-8")
    text = text.replace("status: provisional", "status: approved")
    text = text.replace("source: synthetic", "source: real")
    text = text.replace("run_by:", "run_by: Alex")
    text = text.replace("approved_by:", "approved_by: Alex")
    text = text.replace("approved_at:", "approved_at: 2026-08-15")
    out.write_text(text, encoding="utf-8")
    result = check_t8(root)
    assert result.passed, result.detail


def test_t10_a001_unchanged(tmp_path):
    root = _copy_example(tmp_path)
    before = (root / "papers" / "toy-study" / "ANALYSIS_PLAN.md").read_text(encoding="utf-8")
    import re

    match = re.search(r"(## A-001\b.*?)(?=\n## A-|\Z)", before, flags=re.S)
    prop = root / "papers" / "toy-study" / "proposals"
    prop.mkdir(parents=True, exist_ok=True)
    (prop / "A-002.md").write_text("# A-002\nagreed:\n", encoding="utf-8")
    result = check_t10(root, a001_before=match.group(1))
    assert result.passed, result.detail


def test_t11_ai_use_fixture(tmp_path):
    root = _copy_example(tmp_path)
    folder = root / "papers" / "toy-study" / "ai-use"
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "AI-001.yml").write_text(
        "id: AI-001\nrole: implementation\norigin: human\nwhat: Implemented A-001\n",
        encoding="utf-8",
    )
    result = check_t11(root)
    assert result.passed, result.detail
