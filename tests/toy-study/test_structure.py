from pathlib import Path

KIT = Path(__file__).resolve().parents[2]

REQUIRED_SKILLS = (
    "start-research-project",
    "understand-research-project",
    "develop-analysis-with-safe-data",
    "document-research-decision",
    "update-project-record",
)


def test_kit_tree_exists():
    for rel in (
        "README.md",
        "START.md",
        "SPEC.md",
        "BACKLOG.md",
        "CHANGELOG.md",
        "LICENSE",
        "policies/data-policy.md",
        "templates/layout/by-paper.yml",
        "templates/layout/numbered.yml",
        "templates/manuscript/quarto/paper.qmd",
        "templates/analysis/r/01_draft.R",
        "templates/manuscript/word/README.md",
        "templates/analysis/stata/README.md",
        "scripts/install.py",
        "adapters/claude/CLAUDE.md",
        "adapters/cursor/research-agent-kit.mdc",
        "examples/toy-study/layout.yml",
    ):
        assert (KIT / rel).exists(), rel


def test_skill_frontmatter():
    for name in REQUIRED_SKILLS:
        text = (KIT / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
        assert text.startswith("---\n")
        assert f"name: {name}" in text
        assert "description:" in text


def test_spec_is_frozen():
    spec = (KIT / "SPEC.md").read_text(encoding="utf-8")
    assert "frozen v0.1" in spec
    assert "draft — not frozen" not in spec
