---
name: start-research-project
description: Get the kit from GitHub into one folder, or start a paper that follows the kit. Use when they say Copy the Research Agent Kit, Start the project, or Initiate. An empty folder plus the GitHub URL starts a self-contained paper (temporary fetch; do not leave the full kit in that folder). After the start interview, copy the paper skeleton and patch; do not read template files.
license: MIT
compatibility: Requires a project filesystem. No Python or R required. May fetch from GitHub.
metadata:
  version: "0.6.2"
---

# Start the project

Two jobs. Do not mix them.

1. **Get the kit** — one folder. Defaults and skills live here. They say this folder **is the kit**.
2. **Start a paper** — science files in a folder. From a local kit, or from GitHub into **this** empty (or already-open) paper folder as a **self-contained** paper.

Follow `policies/how-to-talk.md` if present. No Python or R required. The researcher does not need to download the kit themselves.

Public kit: https://github.com/juusorepo/research-agent-kit

Do **not** say: slug, repo, init, toolchain, agent-accessible, by-paper, data_access.

**Lookup:** paper override (`.agents/skills/`, paper `policies/`) if it exists; else generated files under `.rak/runtime/` if present; else the kit. Do not copy kit files into the paper except the generated bundle in **Make this paper self-contained**.

**This file is complete.** Do not search workshop files (`dev/`, `SPEC.md`, `tests/`, `scripts/install.py`) or the toy example to learn how to start. Do not guess missing defaults. Do not treat start as a reading tour of `templates/`.

---

## Get the kit

When they say this folder is the kit, or **Copy the Research Agent Kit** from GitHub:

- Fetch the public kit into **this** folder (git clone, or ZIP from GitHub). This includes `templates/` and `skills/`.
- Then **delete** these if they are present (workshop only; not for researchers): `dev/`, `SPEC.md`, `BACKLOG.md`, `tests/`, `pytest.ini`, `requirements-dev.txt`, `scripts/install.py`. Do not mention them.
- Do **not** turn this folder into a paper. Do not write `01-data` or `ANALYSIS_PLAN.md` here.
- If `researcher.md` has no name yet, ask once and write it there (`Name: …`).
- Tell them: edit shared conventions here. For one paper only, add that file in the paper later.

## Update the kit

When they say **Update the kit** or **Update the skills**: use `skills/update-the-kit/SKILL.md` (kit folder or paper — that skill chooses). Do not mix with starting a paper.

---

## Start a paper

They only need to say **Start the project**. Do not ask them to name the kit or the paper again if you can see the folders.

**Which folder is which**

- **Kit** = the folder with `START.md` + `skills/` + `templates/`. Never write science files here (`01-data`, overview, analysis plan, manuscript, …). The only kit write allowed at start is `researcher.md` if the name is still empty.
- **Paper** = any other opened folder. If one is already open, **keep its name** and write the project **only there**.
- **Only the kit is open:** after the interview, create a sibling folder (default **paper-1**). Prefer they instead open an empty **Google Drive** folder (for sharing and NotebookLM) plus the kit, then keep that paper name.
- **Kit plus paper are both open:** use their local kit; write only into the paper. Never create a sibling of the kit if they already named or opened a paper folder (including a Drive folder).
- **Paper only, and you cannot read a local kit:** if they gave a GitHub URL, or they said **Start the project from** the public kit, this is a **GitHub paper start** (below). Do not stop. If they did not give GitHub and there is no local kit: ask once for the public URL (default https://github.com/juusorepo/research-agent-kit) or to open the kit.
- If more than one non-kit folder is open and it is unclear which is this paper, ask once.

**Windows Drive path.** If this computer is Windows and the paper (or kit) path looks like streamed Google Drive — usually `G:\My Drive\...` — **stop once** before writing files. Ask them to set Google Drive to **Mirror files** and reopen from the local path (usually `C:\Users\<name>\My Drive\...`). Full note: `adapters/google-drive/README.md` (say the same steps if you cannot read that file). Do not continue until they have seen this. If they say continue anyway, continue. Cursor, Claude, Codex, and similar tools may be unable to run from the streamed letter. “Available offline” is not enough.

### GitHub paper start (no local kit)

They opened **this** folder (often empty Drive) and said **Start the project** with the GitHub address. The result must be a **paper**, not a kit.

1. Fetch the public kit into a **temporary** folder (ZIP `https://github.com/juusorepo/research-agent-kit/archive/refs/heads/main.zip` or `git clone --depth 1`). Not into this paper. If the extract has `research-agent-kit-main/`, that is the kit root.
2. Read `skills/start-research-project/SKILL.md` from that temporary kit if you do not already have this file. Then interview (below). Question 8 default **yes**. Question 9 default **yes** if this looks like Drive.
3. After they reply: copy `templates/paper-skeleton/` from the **temporary** kit into **this** folder (same copy commands; `$kit` is the temporary root). Patch paper name. For `KIT_PATH`, write an empty path (`kit_path: ""`) — there is no local kit. Patch data-use and AI-use ticks as usual.
4. **Name:** there is no kit `researcher.md`. Ask once if you do not have a name. Write it on the overview Lead researcher line only. Do not create `researcher.md` in the paper.
5. Always run **Make this paper self-contained** copy steps from the temporary kit in this same turn (question 8 is yes). Do not wait again.
6. **Delete** the temporary folder. This paper must **not** contain `START.md`, kit `README.md`, `skills/` at the root, `templates/` at the root, `adapters/`, `examples/`, or `researcher.md`.

Do not use **Copy the Research Agent Kit** in a paper folder — that would turn this folder into a kit.

Do **not** copy `dev/`, `SPEC.md`, `tests/`, `examples/`, `templates/` as a whole, or `adapters/` into the paper. Copy **only** `templates/paper-skeleton/` (below), then — if they want this paper to work without the kit folder — generated kit files via `skills/make-paper-self-contained/SKILL.md`. The skeleton already includes a thin `CLAUDE.md` that points at `AGENTS.md`. Follow the kit `policies/ai-policy.md` unless the paper adds its own.

### 0. Look before you interview

Read what is already in the **target paper folder** (if it exists) **and** what they attached in this chat (protocol, analysis plan, draft paper, codebook). Do not invent files. Do not read kit template bodies.

If the target folder already has research files, you are starting **from existing work**. Never overwrite overview, analysis plan, manuscript, data, or scripts.

**Usual case:** they already have a protocol, preregistration, analysis plan, or draft paper. Those files are **source material**. After the folder exists, put them in place if they are attached. Do not treat them as already agreed. We do not back-fill AI use **from now on** unless they opted in. Do not invent old decisions or old AI use.

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
8. Should this paper work when the assistant cannot see the kit folder (ChatGPT, a co-author, NotebookLM)? (**yes** if a paper folder is already open; **no** if we are creating a folder next to the kit)
9. Is this folder a Google Drive synced project (for sharing this folder, and — in this version — pointing NotebookLM at `08-sources/` here yourself)? (**yes** if they already opened a paper folder; **no** if we are creating a sibling of the kit)

### Opening message

> I’ll set up the paper folder. Shared conventions stay in the kit. I will not add project files to the kit. Generated kit files in the paper (if you want this folder to work alone) are replaced later — do not edit them.
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
> 8. Work without the kit folder? (**yes** if this paper folder is already open; **no** if creating a folder next to the kit)
> 9. Google Drive synced folder for sharing / NotebookLM? (**yes** if this paper folder is already open; **no** otherwise)
>
> If the kit already has your name, I will use it.

### After they reply — copy, then patch

Do **not** read template bodies. Copy, then patch a few lines. Do not assemble the paper from a per-file list. Do not send the assistant through Cursor’s create-project helper (or any other app step that is not in this skill).

The skeleton is a ready-made numbered paper (one paper, Quarto, R, individual-level data closed, material AI-use notes off). It includes `kit-lock.yml` (same `kit:` / `skills:` as `templates/project/kit-lock.yml`).

1. Create the paper folder if needed (sibling of the kit, default **paper-1**). If a paper folder is already open, use it. Create the directory only (`mkdir` / `New-Item`). Do not initialise git.
2. Copy `templates/paper-skeleton/` into that folder with **one** command (block below). Numbered folders are already there.
3. Apply **four patches only** (search-and-replace in those two files; do not restudy them):
   - **Paper folder name** — in `layout.yml`, replace `PAPER_SLUG` with that name
   - **Path to the kit** — in `layout.yml`, replace `KIT_PATH` with a relative path from the paper to the kit (forward slashes)
   - **Individual-level data allowed or closed** — in `policies/data-policy.md`, keep `restricted` if closed (default); write `agent-accessible` only if they allowed it
   - **Material AI-use notes on or off** — in `policies/what-is-on.md`, tick the box only if they said yes
4. Write the kit `researcher.md` name onto the overview Lead researcher line. Skip if that line already has a name.

If the paper folder already has research files, copy only missing paths. Never overwrite overview, analysis plan, manuscript, data, or scripts.

5. If they said this paper should work without the kit folder (question 8, default **yes** when a paper folder was already open): after the four patches, follow `skills/make-paper-self-contained/SKILL.md` copy steps in this same turn. Do not wait again. Do not copy `skills/` into the paper except as that generated bundle.

#### Copy command (Windows PowerShell)

```powershell
$kit = "<kit folder>"
$paper = "<paper folder>"
New-Item -ItemType Directory -Force -Path $paper | Out-Null
Get-ChildItem -Force -Path (Join-Path $kit "templates\paper-skeleton") |
  Copy-Item -Destination $paper -Recurse -Force
```

`Get-ChildItem -Force` is required so `.gitignore` is copied.

#### Copy command (Unix)

```bash
mkdir -p "$paper"
cp -R "$kit/templates/paper-skeleton/." "$paper/"
```

Run this in the terminal yourself. Do not use Cursor `create_project`. Do not use `move_agent_to_root` as a substitute for the copy. Do not use Python or a per-file copy list.

#### If they did not take the defaults

Copy the matching extra tree. Do not read those files.

- **Several papers** sharing data: copy `templates/layout/numbered-multipaper.yml` onto `layout.yml`, then repeat the kit-path and paper-name patches. Make `07-record/<name>/` and `05-outputs/<name>/manuscript/` as that file maps them.
- **Word:** copy `templates/manuscript/word/` into `05-outputs/manuscript/`; set `manuscript_format: word` in `layout.yml`.
- **Markdown:** copy `templates/manuscript/markdown/` into `05-outputs/manuscript/`; set `manuscript_format: markdown` in `layout.yml`.
- **Stata:** copy `templates/analysis/stata/` into `02-scripts/` (include `01_draft.do` and the path-config example; do not invent a Stata path); set `code: stata` in `layout.yml`. You may remove the R stubs.

Do not add a second skill for a “fast start.”

First-level folders must be numbered (`01-data` … `08-sources`, `99-archive`) plus `policies/`. The manuscript lives in `05-outputs/manuscript/` (or `05-outputs/<name>/manuscript` if several papers). Do not put `decisions`, `notes`, `contributions`, `proposals`, `ai-use`, or `audits` at the top level.

### After the folder exists

1. If they attached files in this chat, put protocol / preregistration / plan in `06-docs/` and a draft paper in `05-outputs/manuscript/` unless those files are already there. Keep an existing draft.
2. If they said they have those files and they are not in the folder, ask them to put them there.
3. If a protocol or draft is already present, name the files you found. Do not invent a blank-project analysis.
4. Do **not** run **Understand the project** in this turn. That is the next message, once protocol or draft is in the folder — or they confirm the folder is empty.
5. If they are still in the kit folder, tell them to **open the new project folder** (keep the kit available) and say **Understand the project**.

## Must not

- Dump kit internals or copy `skills/` into the paper except the generated bundle when they asked for a folder that works without the kit
- Copy `adapters/` into the paper, or replace the skeleton `CLAUDE.md` with a second rule set
- Ask them to download ZIP or clone the kit themselves
- Skip a **local** kit that is already open (use it). If there is no local kit, GitHub paper start is allowed
- Leave a full GitHub clone in the paper folder (`skills/` or `templates/` at the paper root)
- Skip the interview questions, or write folders before they reply
- Add project files to the kit (except `researcher.md` when the name is still empty)
- Search SPEC, tests, or `install.py` for how to start
- Treat start as a reading tour of `templates/`
- Read template bodies after they reply; copy, then patch
- Send the assistant through Cursor’s create-project helper (or any app step that is not in this skill)
- Run **Understand the project** in the same turn as the copy
- Invent analyses, approve results, or reconstruct a history of old decisions / old AI use
- Overwrite an existing overview, analysis plan, manuscript, or data
- Suggest next steps before protocol or draft is in the folder (or they confirm there is none)
- Skip writing their name into the kit `researcher.md` when it is still empty
- Require Python, R, or Stata to start
- Offer features marked “not in this version”
- List an AI system as an author
- Use another person’s unpublished manuscript or plan without permission
- Treat an AI-suggested citation as a source already read
- Invent bibliography records, citation keys, DOIs, or years
