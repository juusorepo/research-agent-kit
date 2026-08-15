from pathlib import Path

KIT = Path(__file__).resolve().parents[2]

REQUIRED_SKILLS = (
    "start-research-project",
    "understand-research-project",
    "develop-analysis-with-safe-data",
    "document-research-decision",
    "update-project-record",
    "contribute-to-project",
    "consolidate-contributions",
)


def test_kit_tree_exists():
    for rel in (
        "README.md",
        "START.md",
        "researcher.md",
        "SPEC.md",
        "BACKLOG.md",
        "CHANGELOG.md",
        "LICENSE",
        "policies/data-policy.md",
        "policies/how-to-talk.md",
        "policies/what-is-on.md",
        "templates/layout/by-paper.yml",
        "templates/layout/numbered.yml",
        "templates/layout/numbered-multipaper.yml",
        "templates/project/folders.md",
        "templates/project/MEMORY.md",
        "templates/decisions/INDEX.md",
        "templates/contributions/README.md",
        "templates/contributions/template.md",
        "templates/notes/README.md",
        "templates/manuscript/quarto/paper.qmd",
        "templates/manuscript/quarto/helpers.R",
        "templates/manuscript/quarto/references.bib",
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
