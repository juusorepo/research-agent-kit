---
name: start-research-project
description: Create a clean research project folder after a short interview, ask them to copy existing plans and drafts into place, then hand off to Understand the project.
license: MIT
compatibility: Requires a project filesystem. No Python or R required.
metadata:
  version: "0.1.0"
---

# Start the project

Follow `policies/how-to-talk.md` if present. No Python or R required.

## This folder vs the project

If the current folder has `SPEC.md`, `skills/`, and `templates/`, it is the **kit**, not the research project.

- Create a **new, empty project folder** next to the kit (default name **paper-1**).
- Write only research-project files there.
- Do **not** copy `SPEC.md`, `tests/`, `examples/`, `templates/`, or canonical `skills/` into that folder.
- Then tell them to open the new folder.

If the current folder is already empty (or already a research project), write here.

## Interview

**Required:** their name.

**Usual case:** they already have a protocol, preregistration, or draft paper. A blank page is the exception.

**Defaults if they only send a name:** individual-level data stay closed; one paper; folder **paper-1**; Quarto; R; numbered folders; **AI-use record off**.

Also ask, in ordinary language (can be the same message or the next one):

1. After the folders exist, **copy existing files into this project** (usual):
   - plan / protocol / prereg → `06-docs/`
   - draft paper → `manuscript/` (keep the kit `paper.qmd` or replace it; do not leave the draft only in Downloads)
   Copied files are source material. They are not yet the analysis plan. Next we draft the overview and plan from them; they accept; you write.
2. Do you want a short record when AI does substantial work **from now on**? **Default no.** We do not back-fill AI use from before this folder existed. Write the answer on `policies/what-is-on.md` (tick the box only if yes).
3. When they say they have copied (or that there is nothing to copy), **look** in `06-docs/` and `manuscript/` and say what you found. Do not invent files. Refresh `STATUS.md` to a snapshot such as “existing draft copied; analysis plan not yet agreed” or “empty project.”

### Opening message

> I’ll create a research project folder (01-data, 02-scripts, manuscript — not a software kit). Most papers already have a plan or draft: after the folders exist I’ll ask you to copy those in. I can draft the overview and analysis plan from them; you say yes before they become the record. I will not invent a history of old decisions or old AI use.
>
> Your name? If you only send that, I’ll call it **paper-1**, use Quarto and R, and I won’t open individual-level data. I will not keep an AI-use log unless you ask.

Do **not** say: slug, repo, init, toolchain, agent-accessible, by-paper, data_access.

## Then write files into the **project** folder

From the kit checkout, copy only:

1. `skills/<name>/` → `.agents/skills/<name>/`
2. `policies/data-policy.md`, `how-to-talk.md`, and `what-is-on.md`
3. `templates/project/AGENTS.md` → `AGENTS.md`
4. `templates/project/.gitignore` and `folders.md` → `FOLDERS.md`
5. Claude / Cursor pointers
6. `kit-lock.yml`
7. `templates/layout/numbered.yml` (or the layout they chose) → `layout.yml`
8. Create every folder in `layout.yml` `paths`
9. Overview, empty analysis plan, status, tasks, `MEMORY.md`
10. `decisions/INDEX.md`, `decisions/RDR-000-template.md`, `contributions/`, `notes/` (working notes — do not load by default)
11. `01-data/raw/README.md`
12. Quarto files → `manuscript/`; R stub → `02-scripts/`

Set the AI-use box in `what-is-on.md` from the interview.

## After folders exist

1. Ask them to copy existing plan/draft files (usual) or confirm there are none.
2. Check `06-docs/` and `manuscript/` and say what is there. Do not treat those files as already agreed.
3. If they are still in the kit folder, tell them to **open the new project folder** and say **Understand the project**.
4. If you are already in the project folder, run **Understand the project** next (same chat is fine): summarise, then offer the next-step list from that skill — for existing files, that is usually “draft overview and analysis plan from what you copied.”

## Update the copied instructions

Recopy how-to files from the kit on request. Do not overwrite overview, analysis plan, data, scripts, outputs, or the manuscript. Keep their `what-is-on.md` ticks unless they ask to reset them.

## Must not

- Dump kit internals into the research folder
- Invent analyses, approve results, or reconstruct a history of old decisions / old AI use
- Skip asking for their name
- Require Python or R
- Offer literature search or other features marked “not in this version”
