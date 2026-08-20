---
name: document-research-decision
description: Record an important methodological choice as a proposed research decision note. Use when they say Document a research decision or Record a research decision, or when design, measurement, sample, or claims would change. Do not use merely to add Table 1 to the plan.
license: MIT
compatibility: Requires a project filesystem.
metadata:
  version: "0.1.2"
---

# Document a research decision

Write a **proposed** note. Do not accept it yourself.

Path: `paths.decisions` from `layout.yml` → `RDR-NNN-short-slug.md`.

When unsure whether a note is needed, propose one and stop. See [when a note is needed](references/when-needed.md).

Add a row to `decisions/INDEX.md` (id, title, status, date). Keep the index short.

## Short form (required)

`id`, `title`, `status: proposed`, `decision`, `rationale`, `proposed_by` (`human` | `AI` | `mixed`).

Use `decisions/RDR-000-template.md` if present, otherwise `templates/decision-note.md`. Add context / alternatives / consequences when the choice is an estimand, sample, or model.

## Not this skill

“Please add Table 1 to the analysis plan” → write a proposal (`proposals/A-NNN.md`), `decision_ref: —`. No decision note.

## Changing a note that already exists

Rewrite the Decision and Rationale in place. If the old choice is no longer in force, set that note `superseded`, point `supersedes` on the new note, and do not leave the old paragraph as current text above a new one. Acceptance is a separate skill.

## Must not

- Set `status: accepted`
- Fill `accepted_by`
- Edit `ANALYSIS_PLAN.md`
- Implement the new method in the same run
