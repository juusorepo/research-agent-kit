from pathlib import Path

KIT = Path(__file__).resolve().parents[2]


def test_start_md_no_runtime():
    text = (KIT / "START.md").read_text(encoding="utf-8")
    assert "Start the project" in text
    assert "Python" in text
    assert "not" in text.lower()
    assert "name" in text.lower()


def test_start_skill_is_copy_not_installer():
    text = (KIT / "skills" / "start-research-project" / "SKILL.md").read_text(encoding="utf-8")
    assert "paper-1" in text
    assert "how-to-talk" in text
    assert "No Python or R" in text or "no Python or R" in text
    assert "Copy" in text or "copy" in text
    assert "what-is-on" in text
    assert "06-docs" in text
    assert "Understand the project" in text
    assert "Do **not** say: slug" in text or "Do not say: slug" in text


def test_what_is_on_ai_use_default_off():
    text = (KIT / "policies" / "what-is-on.md").read_text(encoding="utf-8")
    assert "- [ ] **Record of material AI use**" in text
    assert "Not in this version" in text
    assert "Literature search" in text


def test_understand_offers_next_steps_not_literature():
    text = (KIT / "skills" / "understand-research-project" / "SKILL.md").read_text(
        encoding="utf-8"
    )
    assert "Specify the analysis plan" in text
    assert "literature-search" in text.lower() or "literature search" in text.lower()
    assert "what-is-on" in text
    assert "not load" in text.lower() or "do not load" in text.lower()
    assert "Canonical" in text
    assert "Proposal" in text
    assert "superseded" in text.lower()
    assert "Tentative" in text or "tentative" in text
    assert "existing" in text.lower()
    assert "pre-history" in text.lower() or "back-history" in text.lower()


def test_analysis_plan_accept_then_write():
    text = (KIT / "templates" / "project" / "ANALYSIS_PLAN.md").read_text(encoding="utf-8")
    assert "only the lead researcher adds it here" not in text
    assert "accept" in text.lower()


def test_start_treats_existing_draft_as_usual():
    text = (KIT / "skills" / "start-research-project" / "SKILL.md").read_text(
        encoding="utf-8"
    )
    assert "Usual case" in text
    assert "source material" in text
    assert "from now on" in text
    assert "old decisions" in text or "old AI use" in text


def test_lean_memory_keeps_analysis_plan_name():
    assert (KIT / "templates" / "project" / "ANALYSIS_PLAN.md").exists()
    assert not (KIT / "templates" / "project" / "ANALYSIS_SPEC.md").exists()
    numbered = (KIT / "templates" / "layout" / "numbered.yml").read_text(encoding="utf-8")
    assert "reviews:" not in numbered
    assert "AI_USE_LOG.yaml" not in numbered
    assert "contributions:" in numbered
    assert "notes:" in numbered


def test_contribute_does_not_edit_canonical_record():
    text = (KIT / "skills" / "contribute-to-project" / "SKILL.md").read_text(encoding="utf-8")
    assert "Must not" in text
    assert "ANALYSIS_PLAN.md" in text
    assert "status: proposed" in text


def test_consolidate_recommends_only():
    text = (KIT / "skills" / "consolidate-contributions" / "SKILL.md").read_text(
        encoding="utf-8"
    )
    assert "recommend" in text.lower()
    assert "Must not" in text
    assert "ANALYSIS_PLAN.md" in text


def test_how_to_talk_is_editable_policy():
    text = (KIT / "policies" / "how-to-talk.md").read_text(encoding="utf-8")
    assert "yours to edit" in text.lower()
    assert "slug" in text
    assert "paper-1" in text


def test_readme_does_not_require_python_to_start():
    text = (KIT / "README.md").read_text(encoding="utf-8")
    assert "python scripts/install.py PATH/to/new-project" not in text
    assert "Start the project" in text
