---
name: start-research-project
description: Get the kit from GitHub into one folder, or start a paper that follows the kit with optional paper overrides. Use when they say Copy the Research Agent Kit or Start the project.
license: MIT
compatibility: Requires a project filesystem. No Python or R required. May fetch from GitHub.
metadata:
  version: "0.1.0"
---

# Start the project

Two jobs. Do not mix them.

1. **Get the kit** — one folder. Defaults and skills live here.
2. **Start a paper** — science files in a new folder. Follow kit files unless the paper has its own copy.

Follow `policies/how-to-talk.md` if present. No Python or R required. The researcher does not need to download the kit themselves.

Public kit: https://github.com/juusorepo/research-agent-kit

Do **not** say: slug, repo, init, toolchain, agent-accessible, by-paper, data_access.

**Lookup:** paper file if it exists, otherwise the same path in the kit. Do not duplicate the kit into the paper.

---

## Get the kit

When they say this folder is the kit, or **Copy the Research Agent Kit** from GitHub:

- Fetch the public kit into **this** folder (git clone, or ZIP from GitHub). This is the full kit, including `templates/` and `skills/`.
- Do **not** turn this folder into a paper. Do not write `01-data` or `ANALYSIS_PLAN.md` here.
- If `researcher.md` has no name yet, ask once and write it there (`Name: …`).
- Tell them: edit shared conventions here. For one paper only, add that file in the paper later.

## Update the kit

When they are in the kit folder and want a new public version: fetch GitHub again. **Keep** `policies/how-to-talk.md` and `templates/analysis/` if they have already edited those.

---

## Start a paper

**If this folder is the kit** (`SPEC.md` + `skills/` + `templates/`): create a **new, empty project folder** next to it (default name **paper-1**). Tell them to open that folder. This is the reliable path: you can already see the kit.

**If they opened only an empty paper folder:** you must also be able to read their kit. If you cannot, **stop**. Ask them to open the kit folder as well, or to start from the kit instead. Do not fetch GitHub as a substitute (that would skip their conventions).

**If both folders are open:** use **their local kit**. Find it: they named a path; or a folder with `SPEC.md` + `skills/` + `templates/`.

Do **not** copy `SPEC.md`, `tests/`, `examples/`, `templates/`, canonical `skills/`, or `how-to-talk.md` into the paper.

### Interview

**Name:** read `researcher.md` in the **kit** (`Name:`). If it is set, use it. If it is empty, ask once, write it in the kit file, then continue. Do not ask again for each paper. A paper overview may still name a different lead researcher for that study.

**Usual case:** they already have a protocol, preregistration, or draft paper. A blank page is the exception.

**Defaults:** individual-level data stay closed; Quarto; R; numbered folders; **AI-use record off**. Keep the current folder’s name (use **paper-1** only if you had to create a new folder next to the kit).

Also ask, in ordinary language (can be the same message or the next one):

1. After the folders exist, **copy existing files into this project** (usual):
   - plan / protocol / prereg → `06-docs/`
   - draft paper → `manuscript/` (keep the kit `paper.qmd` or replace it; do not leave the draft only in Downloads)
   Copied files are source material. They are not yet the analysis plan. Next we draft the overview and plan from them; they accept; you write.
2. Do you want a short record when AI does substantial work **from now on**? **Default no.** We do not back-fill AI use from before this folder existed. Write the answer on `policies/what-is-on.md` (tick the box only if yes).
3. When they say they have copied (or that there is nothing to copy), **look** in `06-docs/` and `manuscript/` and say what you found. Do not invent files. Refresh `STATUS.md` to a snapshot such as “existing draft copied; analysis plan not yet agreed” or “empty project.”

### Opening message

> I’ll create the paper folders next to your kit. Shared conventions stay in the kit. This paper can override a default by adding that one file here. Most papers already have a plan or draft: I’ll ask you to copy those in.
>
> If the kit already has your name, I will use it. If you only send that, I’ll use Quarto and R, keep this folder’s name, and I won’t open individual-level data. I will not keep an AI-use log unless you ask.

### Then write files into the **paper** folder

Write the **science** tree. Set `kit_path` in `layout.yml` to their kit folder. Copy only:

1. `templates/project/AGENTS.md` → `AGENTS.md`
2. `templates/project/.gitignore` and `folders.md` → `FOLDERS.md`
3. Claude / Cursor pointers (they should follow paper-then-kit)
4. `kit-lock.yml`
5. `templates/layout/numbered.yml` (or the layout they chose) → `layout.yml` with `kit_path` set
6. Create every folder in `layout.yml` `paths`
7. Overview, empty analysis plan, status, tasks, `MEMORY.md` — put the kit `researcher.md` name on the overview
8. `policies/data-policy.md` and `policies/what-is-on.md` (this paper’s rules)
9. `decisions/INDEX.md`, `decisions/RDR-000-template.md`, `contributions/`, `notes/`
10. `01-data/raw/README.md`
11. Quarto files → `manuscript/`; one R starting script from the kit’s `templates/analysis/r/` → `02-scripts/` (this becomes their analysis, not a second conventions folder)

Do **not** copy `skills/` or `how-to-talk.md`. Those stay in the kit unless they later add a paper override.

Set the AI-use box in `what-is-on.md` from the interview.

### After folders exist

1. Ask them to copy existing plan/draft files (usual) or confirm there are none.
2. Check `06-docs/` and `manuscript/` and say what is there. Do not treat those files as already agreed.
3. If they are still in the kit folder, tell them to **open the new project folder** (keep the kit available) and say **Understand the project**.
4. If you are already in the project folder and can read the kit, run **Understand the project** next.

## Must not

- Dump kit internals or a second copy of skills into the research folder
- Ask them to download ZIP or clone the kit themselves
- Start a paper by fetching GitHub and skipping their local kit
- Invent analyses, approve results, or reconstruct a history of old decisions / old AI use
- Skip writing their name into the kit `researcher.md` when it is still empty
- Require Python or R
- Offer literature search or other features marked “not in this version”
