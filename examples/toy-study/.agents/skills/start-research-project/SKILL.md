---
name: start-research-project
description: Copy how-to files from the public Research Agent Kit into the researcher's folder, ask them to copy existing plans and drafts into place, then hand off to Understand the project.
license: MIT
compatibility: Requires a project filesystem. No Python or R required. May fetch from GitHub.
metadata:
  version: "0.1.0"
---

# Start the project

One researcher action: copy how-to files **and** create the paper folders in the directory they opened. Do not treat “copy the kit” and “start a paper” as two visits.

Follow `policies/how-to-talk.md` if present. No Python or R required. The researcher does not need to download the kit themselves.

Public kit: https://github.com/juusorepo/research-agent-kit

## Where to write

**Usual:** they created an empty folder and opened it with you. The first message must name the public kit (`https://github.com/juusorepo/research-agent-kit`). Fetch that. Write the research project **here**. Keep the folder’s name.

**If this folder is the kit** (`SPEC.md` + `skills/` + `templates/`): create a **new, empty project folder** next to it (default name **paper-1**). Tell them to open that folder.

Do **not** copy `SPEC.md`, `tests/`, `examples/`, `templates/`, or canonical `skills/` into the paper folder.

## Where to copy from

1. This folder, if it is already the kit.
2. Else a kit folder on this computer, if you can see one.
3. Else fetch the public kit (git clone to a temp folder, or download the ZIP from GitHub). Copy only the research-project files below. Then delete the temp copy.

## Interview

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

> I’ll copy the how-to files from the public Research Agent Kit into this folder (01-data, 02-scripts, manuscript — not the kit’s tests). Most papers already have a plan or draft: I’ll ask you to copy those in. I can draft the overview and analysis plan from them; you say yes before they become the record. I will not invent a history of old decisions or old AI use.
>
> Your name? If you only send that, I’ll use Quarto and R, keep this folder’s name, and I won’t open individual-level data. I will not keep an AI-use log unless you ask.

Do **not** say: slug, repo, init, toolchain, agent-accessible, by-paper, data_access.

## Then write files into the **project** folder

From the kit (local or fetched), copy only:

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

On request, fetch the public kit again (or use a local kit if present). Recopy how-to files. Do not overwrite overview, analysis plan, data, scripts, outputs, or the manuscript. Keep their `what-is-on.md` ticks unless they ask to reset them.

## Must not

- Dump kit internals into the research folder
- Ask them to download ZIP or clone the kit themselves
- Invent analyses, approve results, or reconstruct a history of old decisions / old AI use
- Skip asking for their name
- Require Python or R
- Offer literature search or other features marked “not in this version”
