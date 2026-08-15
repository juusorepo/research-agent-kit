---
name: start-research-project
description: Get the kit from GitHub into one folder, or start a paper from that local kit. Use when they say Copy the Research Agent Kit, Start the project, or Update the copied instructions.
license: MIT
compatibility: Requires a project filesystem. No Python or R required. May fetch from GitHub.
metadata:
  version: "0.1.0"
---

# Start the project

Two jobs. Do not mix them.

1. **Get the kit** — one folder on the computer. Conventions live only here.
2. **Start a paper** — copy how-to files from that kit into a new paper folder.

Follow `policies/how-to-talk.md` if present. No Python or R required. The researcher does not need to download the kit themselves.

Public kit: https://github.com/juusorepo/research-agent-kit

Do **not** say: slug, repo, init, toolchain, agent-accessible, by-paper, data_access.

---

## Get the kit

When they say this folder is the kit, or **Copy the Research Agent Kit** from GitHub:

- Fetch the public kit into **this** folder (git clone, or ZIP from GitHub). This is the full kit, including `templates/` and `skills/`.
- Do **not** turn this folder into a paper. Do not write `01-data` or `ANALYSIS_PLAN.md` here.
- Tell them: edit R conventions, how-to-talk, and other defaults **only here**. Then create a new folder to start a paper.

## Update the kit

When they are in the kit folder and want a new public version: fetch GitHub again. **Keep** `policies/how-to-talk.md` and `templates/analysis/` if they have already edited those.

---

## Start a paper

**If this folder is the kit** (`SPEC.md` + `skills/` + `templates/`): create a **new, empty project folder** next to it (default name **paper-1**). Tell them to open that folder. This is the reliable path: you can already see the kit.

**If they opened only an empty paper folder:** you must also be able to read their kit. If you cannot, **stop**. Ask them to open the kit folder as well, or to start from the kit instead. Do not fetch GitHub as a substitute (that would skip their R conventions).

**If both folders are open:** copy from **their local kit**, not from GitHub. Find the kit: they named a path; or a folder with `SPEC.md` + `skills/` + `templates/`.

Do **not** copy `SPEC.md`, `tests/`, `examples/`, `templates/`, or canonical `skills/` into the paper folder.

### Interview

**Required:** their name.

**Usual case:** they already have a protocol, preregistration, or draft paper. A blank page is the exception.

**Defaults if they only send a name:** individual-level data stay closed; Quarto; R; numbered folders; **AI-use record off**. Keep the current folder’s name (use **paper-1** only if you had to create a new folder next to the kit).

Also ask, in ordinary language (can be the same message or the next one):

1. After the folders exist, **copy existing files into this project** (usual):
   - plan / protocol / prereg → `06-docs/`
   - draft paper → `manuscript/` (keep the kit `paper.qmd` or replace it; do not leave the draft only in Downloads)
   Copied files are source material. They are not yet the analysis plan. Next we draft the overview and plan from them; they accept; you write.
2. Do you want a short record when AI does substantial work **from now on**? **Default no.** We do not back-fill AI use from before this folder existed. Write the answer on `policies/what-is-on.md` (tick the box only if yes).
3. When they say they have copied (or that there is nothing to copy), **look** in `06-docs/` and `manuscript/` and say what you found. Do not invent files. Refresh `STATUS.md` to a snapshot such as “existing draft copied; analysis plan not yet agreed” or “empty project.”

### Opening message

> I’ll copy the how-to files from your Research Agent Kit folder into this paper (01-data, 02-scripts, manuscript — not the kit’s tests). Edit R conventions in the kit, not here. Most papers already have a plan or draft: I’ll ask you to copy those in. I can draft the overview and analysis plan from them; you say yes before they become the record.
>
> Your name? If you only send that, I’ll use Quarto and R, keep this folder’s name, and I won’t open individual-level data. I will not keep an AI-use log unless you ask.

### Then write files into the **paper** folder

From **their kit**, copy only:

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
12. Quarto files → `manuscript/`; R stub from **their** `templates/analysis/r/` → `02-scripts/`

Set the AI-use box in `what-is-on.md` from the interview.

### After folders exist

1. Ask them to copy existing plan/draft files (usual) or confirm there are none.
2. Check `06-docs/` and `manuscript/` and say what is there. Do not treat those files as already agreed.
3. If they are still in the kit folder, tell them to **open the new project folder** and say **Understand the project**.
4. If you are already in the project folder, run **Understand the project** next (same chat is fine): summarise, then offer the next-step list from that skill — for existing files, that is usually “draft overview and analysis plan from what you copied.”

## Update the copied instructions (in a paper)

Copy how-to files again from **their local kit**, not from GitHub. You must be able to read the kit; if not, stop and ask them to open it too. Do not overwrite overview, analysis plan, data, scripts, outputs, or the manuscript. Keep their `what-is-on.md` ticks unless they ask to reset them. Do not treat the paper copy as the place to edit conventions.

## Must not

- Dump kit internals into the research folder
- Ask them to download ZIP or clone the kit themselves
- Start a paper by fetching GitHub and skipping their local kit
- Invent analyses, approve results, or reconstruct a history of old decisions / old AI use
- Skip asking for their name
- Require Python or R
- Offer literature search or other features marked “not in this version”
