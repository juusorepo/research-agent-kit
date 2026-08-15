---
name: start-research-project
description: Interview the researcher and create project folders by copying files from this repo. Use when they say Start the project, Initiate, or set up this folder. No Python or R required.
license: MIT
compatibility: Requires a project filesystem. No Python or R required.
metadata:
  version: "0.1.0"
---

# Start the project

Use when the researcher says **Start the project**, **Initiate**, or asks to set up this folder.

No Python or R is required. Copy files from this repository. Do not tell the researcher they must install a language to start.

## Interview

Ask. Do not invent answers. Defaults are in **bold**.

1. **Lead researcher name** (required — put it on the project overview)
2. Data-use: **restricted** or agent-accessible
3. One paper or several? First paper **slug** (short folder name, letters/digits/hyphens)
4. Manuscript: **Quarto** / Markdown / Word
5. Analysis code: **R** / Stata
6. Folders: **by-paper** (`papers/<slug>/…`) / numbered (`01-data`, `02-scripts`, `05-outputs`, `06-docs`)

If answers are already in `layout.yml`, confirm rather than re-ask.

## Then write files (copy; no installer)

Kit files live in this repo. Treat the folder the researcher opened as the project.

1. Copy `skills/<name>/` → `.agents/skills/<name>/` for each skill
2. Copy `policies/data-policy.md` → `policies/data-policy.md` (set `data_access` from the interview)
3. Copy `templates/project/AGENTS.md` → `AGENTS.md`
4. Copy `templates/project/.gitignore` if the project has no `.gitignore`
5. Copy `adapters/claude/CLAUDE.md` → `CLAUDE.md` and `adapters/cursor/research-agent-kit.mdc` → `.cursor/rules/research-agent-kit.mdc`
6. Write `kit-lock.yml` (versions only; do not put the version in `AGENTS.md`). Use `0.1.0` unless `kit-lock.yml` already exists
7. Copy `templates/layout/<preset>.yml` → `layout.yml`; replace `PAPER_SLUG`; set `code` and `manuscript_format`
8. Create `docs/` and the paper record files from `templates/project/` (overview, empty analysis plan, status, tasks). Put the lead researcher name on the overview
9. Copy the shipped manuscript stub (`templates/manuscript/quarto` or `markdown`) and analysis stub (`templates/analysis/r`) into the paths from `layout.yml`
10. If Word or Stata was chosen: create the reserved folder, copy its README stub, and say those templates are not shipped yet. Do not invent a Word or Stata toolchain

`scripts/install.py` is an optional shortcut for people who already have Python (and for kit tests). Do not require it.

## Must not

- Invent analyses or fill the analysis plan with guessed items
- Approve results
- Skip the interview when answers are not already in files
- Require Python or R to start
- Hard-code `02-scripts` in later work; always read `layout.yml`

## Say

Use researcher language. Mention the folder map, data-use mode, the lead researcher name as recorded, and that the analysis plan may start empty.
