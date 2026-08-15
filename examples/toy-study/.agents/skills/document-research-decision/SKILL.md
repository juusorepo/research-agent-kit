---
name: document-research-decision
description: Record an important methodological choice as a proposed research decision note. Use when design, measurement, sample, or claims would change. Do not use merely to add Table 1 to the plan.
license: MIT
compatibility: Requires a project filesystem.
metadata:
  version: "0.1.0"
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

## Must not

- Set `status: accepted`
- Fill `accepted_by`
- Edit `ANALYSIS_PLAN.md`
- Implement the new method in the same run
