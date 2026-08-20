---
name: start-research-project
description: Get the kit from GitHub into one folder, or start a paper that follows the kit with optional paper overrides. Use when they say Copy the Research Agent Kit, Start the project, or Initiate.
license: MIT
compatibility: Requires a project filesystem. No Python or R required. May fetch from GitHub.
metadata:
  version: "0.1.3"
---

# Start the project

Two jobs. Do not mix them.

1. **Get the kit** — one folder. Defaults and skills live here.
2. **Start a paper** — science files in a new folder. Follow kit files unless the paper has its own copy.

Follow `policies/how-to-talk.md` if present. No Python or R required. The researcher does not need to download the kit themselves.

Public kit: https://github.com/juusorepo/research-agent-kit

Do **not** say: slug, repo, init, toolchain, agent-accessible, by-paper, data_access.

**Lookup:** paper file if it exists, otherwise the same path in the kit. Do not duplicate the kit into the paper.

**This file is complete.** Do not search workshop files (`dev/`, `SPEC.md`, `tests/`, `scripts/install.py`) or the toy example to learn how to start. Do not guess missing defaults.

---

## Get the kit

When they say this folder is the kit, or **Copy the Research Agent Kit** from GitHub:

- Fetch the public kit into **this** folder (git clone, or ZIP from GitHub). This includes `templates/` and `skills/`.
- Then **delete** these if they are present (workshop only; not for researchers): `dev/`, `SPEC.md`, `BACKLOG.md`, `tests/`, `pytest.ini`, `requirements-dev.txt`, `scripts/install.py`. Do not mention them.
- Do **not** turn this folder into a paper. Do not write `01-data` or `ANALYSIS_PLAN.md` here.
- If `researcher.md` has no name yet, ask once and write it there (`Name: …`).
- Tell them: edit shared conventions here. For one paper only, add that file in the paper later.

## Update the kit

When they are in the kit folder and say **Update the kit** or **Update the skills**: use `skills/update-the-kit/SKILL.md`. Do not mix with starting a paper.

---

## Start a paper

They only need to say **Start the project**. Do not ask them to name the kit or the paper again if you can see the folders.

**Which folder is which**

- **Kit** = the folder with `START.md` + `skills/` + `templates/`. Never write science files here (`01-data`, overview, analysis plan, manuscript, …). The only kit write allowed at start is `researcher.md` if the name is still empty.
- **Paper** = any other opened folder. If one is already open, **keep its name** and write the project **only there**.
- **Only the kit is open:** after the interview, create a sibling folder (default **paper-1**).
- **Kit plus paper are both open:** use their local kit; write only into the paper.
- **Paper only, and you cannot read the kit:** **stop**. Ask them to open the kit too. Do not fetch GitHub as a substitute (that would skip their conventions).
- If more than one non-kit folder is open and it is unclear which is this paper, ask once.

Do **not** copy `dev/`, `SPEC.md`, `tests/`, `examples/`, `templates/`, canonical `skills/`, `how-to-talk.md`, `ai-policy.md`, or `CLAUDE.md` into the paper. The agent file is `AGENTS.md`. Follow the kit `policies/ai-policy.md` unless the paper adds its own.

### 0. Look before you interview

Read what is already here **and** what they attached in this chat (protocol, analysis plan, draft paper, codebook). Do not invent files.

If the target folder already has research files, you are starting **from existing work**. Never overwrite overview, analysis plan, manuscript, data, or scripts.

**Usual case:** they already have a protocol, preregistration, analysis plan, or draft paper. Those files are **source material**. Read them before suggesting next steps. Do not treat them as already agreed. We do not back-fill AI use **from now on** unless they opted in. Do not invent old decisions or old AI use.

### Interview — always ask, then wait

Ask every question below, with the default in parentheses. One short message. Then **stop and wait** for a reply.

Do not skip the questions because the defaults are fine. They may answer “defaults are fine” — that still counts as a reply. If they already answered a question in this chat, do not ask it again.

**Name:** read `researcher.md` in the **kit** (`Name:`). If it is set, use it (say so). If it is empty, ask once, write it in the kit file, then continue. Do not ask again for each paper.

**Questions:**

1. Folder name? (keep the paper folder if one is already open; if you are creating a folder next to the kit, **paper-1**)
2. One paper in this folder, or several that share the same data and scripts? (**one paper**)
3. Manuscript in Quarto, Word, or Markdown? (**Quarto**)
4. Analysis in R or Stata? (**R**)
5. Keep individual-level data closed to the assistant? (**yes**)
6. Keep a short note when AI does substantial work from now on? (**no**)
7. Do you already have a protocol, analysis plan, or draft paper? (**usual: yes**) We will read those files before suggesting what to do next.

### Opening message

> I’ll set up the paper folder. Shared conventions stay in the kit. I will not add project files to the kit. This paper can override a default by adding that one file here.
>
> Please confirm or change these (defaults in parentheses). “Defaults are fine” is enough once you have seen the list:
>
> 1. Folder name (**keep this paper folder** if one is already open; otherwise **paper-1**)
> 2. One paper here, or several sharing data and scripts? (**one paper**)
> 3. Manuscript: Quarto, Word, or Markdown? (**Quarto**)
> 4. Analysis: R or Stata? (**R**)
> 5. Keep individual-level data closed? (**yes**)
> 6. Record substantial AI use from now on? (**no**)
> 7. Do you already have a protocol, analysis plan, or draft? (**yes — we will read it before deciding next steps**)
>
> If the kit already has your name, I will use it.

### After they reply — write files into the **paper** folder

Use **numbered** folders (`templates/layout/numbered.yml`) for one paper. If they chose several papers sharing data, use `templates/layout/numbered-multipaper.yml`.

Set `kit_path` in `layout.yml` to their kit folder (relative path). Replace `PAPER_SLUG` and `KIT_PATH`.

Copy **only** this list, from the **kit** paths on the left:

1. `templates/project/AGENTS.md` → `AGENTS.md`
2. `templates/project/.gitignore` → `.gitignore`
3. `templates/project/folders.md` → `FOLDERS.md`
4. `templates/project/MEMORY.md` → `MEMORY.md`
5. Copy `templates/project/kit-lock.yml` → `kit-lock.yml` (do not invent version numbers)
6. Chosen layout template → `layout.yml` with `kit_path` set
7. Create every **folder** in `layout.yml` `paths` (not files that do not exist yet)
8. If missing: overview, analysis plan, status, tasks from `templates/project/` — put the kit `researcher.md` name on the overview. **Skip any of these that already exist.**
9. `policies/data-policy.md` and `policies/what-is-on.md` (this paper’s rules) unless they already exist
10. `templates/decisions/INDEX.md` → `07-record/decisions/INDEX.md` (or the layout `decisions` path); `templates/decision-note.md` → `RDR-000-template.md` in that folder
11. `templates/contributions/` → the layout `contributions` path; `templates/notes/README.md` → the layout `notes` path; `templates/audits/README.md` → the layout `audits` path
12. `templates/project/data-raw-README.md` → `01-data/raw/README.md`
13. Quarto (or their format) from `templates/manuscript/<format>/` → `05-outputs/manuscript/` (or the layout `manuscript` path). If they already have a draft there, keep theirs.
14. One R starting script from `templates/analysis/r/` → `02-scripts/` unless that folder already has scripts

Do **not** copy `skills/`, `how-to-talk.md`, `ai-policy.md`, `CLAUDE.md`, or Cursor rule files. Agents follow `AGENTS.md`. Optional tool pointers live in the kit `adapters/` folder; the researcher can copy one later if a tool requires it.

Tick the AI-use box in `what-is-on.md` only if they said yes.

First-level folders must be numbered (`01-data` … `07-record`, `99-archive`) plus `policies/`. The manuscript lives in `05-outputs/manuscript/`, not as its own top-level folder. Do not put `decisions`, `notes`, `contributions`, `proposals`, `ai-use`, or `audits` at the top level.

### After folders exist

1. If they said they have existing files (or you already found some): ask them to put protocol/prereg/plan in `06-docs/` and a draft paper in `05-outputs/manuscript/` unless the files are already in the folder or attached in chat. You may move chat attachments into those folders.
2. **Read** `06-docs/`, `05-outputs/manuscript/`, any `ANALYSIS_PLAN.md`, overview, and attachments. Say what you found. Do not invent files. Do not treat copied files as already agreed.
3. Refresh `STATUS.md` from what you actually saw (“existing draft copied; analysis plan not yet agreed” or “empty project”).
4. **Then** decide next steps (Understand the project). Next steps must follow the files you read. Do not offer a blank-project script if they already have a plan or draft.
5. If they are still in the kit folder, tell them to **open the new project folder** (keep the kit available) and say **Understand the project**.
6. If you are already in the project folder and can read the kit, run **Understand the project** next.

## Must not

- Dump kit internals or a second copy of skills into the research folder
- Copy `CLAUDE.md` or other tool-branded files into the paper
- Ask them to download ZIP or clone the kit themselves
- Start a paper by fetching GitHub and skipping their local kit
- Skip the interview questions, or write folders before they reply
- Add project files to the kit (except `researcher.md` when the name is still empty)
- Search SPEC, tests, or `install.py` for how to start
- Invent analyses, approve results, or reconstruct a history of old decisions / old AI use
- Overwrite an existing overview, analysis plan, manuscript, or data
- Suggest next steps before reading uploaded and copied files
- Skip writing their name into the kit `researcher.md` when it is still empty
- Require Python or R
- Offer literature search or other features marked “not in this version”
- List an AI system as an author
- Use another person’s unpublished manuscript or plan without permission
- Treat an AI-suggested citation as a source already read
