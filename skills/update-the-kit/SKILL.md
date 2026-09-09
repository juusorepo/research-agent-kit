---
name: update-the-kit
description: Fetch a new public kit version. In the kit folder, replace kit files. In a paper with generated kit files, replace only those generated files from GitHub. Use when they say Update the kit or Update the skills.
license: MIT
compatibility: Requires a project filesystem. No Python or R required. May fetch from GitHub.
metadata:
  version: "0.4.0"
---

# Update the kit

Which folder this is decides the job. Do not mix them.

Public kit: https://github.com/juusorepo/research-agent-kit  
ZIP: https://github.com/juusorepo/research-agent-kit/archive/refs/heads/main.zip

Follow `policies/how-to-talk.md` if present. No Python or R required. They do not need to download the kit themselves.

Do **not** say: slug, repo, init, toolchain, agent-accessible, by-paper, data_access.

**This file is complete.** Do not search workshop files or the toy example to learn how to update.

---

## Which folder

**Kit folder** = `START.md` + `skills/` + `templates/` at the top (and this is not a research paper). Full kit update below, or **Update the skills**.

**Paper** = `layout.yml` is present, or generated files under `.rak/runtime/`. **Paper path** below. Fetch GitHub into a **temporary** folder; copy only generated kit files into this paper; delete the temporary folder. Do **not** clone the public kit into this paper.

If both kit and paper are open and they said **Update the kit**: if they are clearly in the paper, use the paper path; if they are clearly in the kit, use the kit path. If unclear, ask once.

If you cannot tell: **stop** and ask whether this folder is the kit or a paper.

---

## Fetch a public kit tree (temporary)

Use this for the paper path, for **Update the skills**, and for a full kit update.

1. Fetch into a **temporary** directory **outside** this project folder (system temp). ZIP or `git clone --depth 1`. Do not fetch into the paper or into the kit as the destination of the clone.
2. If the extract has a wrapper folder (`research-agent-kit-main/`), that inner folder is the kit root (`START.md` + `skills/` + `templates/`).
3. When the copy is done, **delete** the temporary directory.

Do not ask them to download ZIP or clone themselves.

---

## Paper path — replace generated kit files from GitHub

They are in a **paper**. They say **Update the kit** (often with the public GitHub address). This is how an assistant that can see **only this folder** refreshes generated kit files.

If `.rak/runtime/` is missing: this paper is not yet self-contained. Fetch a temporary kit, then follow `skills/make-paper-self-contained/SKILL.md` copy steps from that temporary kit (read that skill from the temporary `skills/` folder). Then delete the temporary folder. Wait once before the copy unless they already said yes in this chat.

If generated files are present:

Pinned: if `update_policy: pinned`, show that a newer public kit exists and **do not replace**. Wait.

Checksum: if `.rak/runtime.manifest.json` lists a file whose hash no longer matches, **stop**. Offer discard or move to `.agents/skills/` / paper `policies/`. Do not merge.

Inspect the temporary kit’s `templates/project/kit-lock.yml` vs this paper’s `kit-lock.yml`. Show files under `.rak/runtime/` and the generated `AGENTS.md` that would be replaced. Then a numbered list, and **stop**:

1. Accept the replacement (**yes**)
2. Not now

Do not write files in this inspect turn.

After yes: from the temporary kit, follow **Make this paper self-contained** copy steps (overwrite generated files only). Keep paper-owned files. Set `runtime: materialised`. Keep `update_policy`. Delete the temporary folder.

**Must never remain in this paper after the fetch:** `START.md`, `researcher.md`, `skills/` at the paper root, `templates/` at the paper root, `adapters/`, `examples/`, kit `README.md` / `CHANGELOG.md` / `LICENSE` / `AGENTS.md` other than the generated paper `AGENTS.md`, `dev/`, `tests/`. If a clone landed in this folder by mistake, remove those kit trees. Do not delete science files.

Remind them: analysis plan, decision notes, outputs, manuscript, data, and data-use rules were not edited. Do not edit `.rak/runtime/` or the generated `AGENTS.md`.

**Update the skills** in a paper: do **not** overwrite a `skills/` folder at the paper root (there must not be one). Refresh generated files as above, or stop and say that skills-only is a kit-folder job.

---

## Kit path — confirm this is the kit

This folder must have `START.md` + `skills/` + `templates/`. It is not a paper.

**Update the skills** (or “just the skills”, “overwrite skills”): replace only this kit’s `skills/` with the public copy. Overwrite. Do not compare keep-files. Do not touch anything else.

**Update the kit** (often with the public GitHub address): full kit update below. They may add **Keep my …** (for example how-to-talk and R templates).

---

## Must not touch (kit path)

- Any **paper** folder next to the kit (overview, analysis plan, decisions, data, scripts, manuscript, `kit-lock.yml`, `AGENTS.md`, `STATUS.md`, `what-is-on.md`)

On a **full** kit update, also leave the **keep list** (below).

On **Update the skills**, overwrite `skills/` even if a skill file was edited locally. Touch nothing else.

Do not copy the whole kit into a paper. After a **kit-folder** update, papers still follow their own `kit-lock.yml` until they **Update the kit** in that paper (GitHub) or **Adjust this project to the new kit version** with a local kit.

---

## Keep list (full kit only)

These rules apply to **Update the kit** in the **kit** folder, not to **Update the skills**, and not to the paper path.

Always keep (never replace from GitHub):

- `researcher.md`

Keep if they named them, or if the local file already differs from the incoming public file:

- `policies/how-to-talk.md`
- `policies/ai-policy.md`
- `templates/analysis/` (R or Stata conventions)

Also keep any other kit path they named in this chat (“Keep my …”).

If a keep-file would change because GitHub changed it too: **stop**. Show that file. Ask whether to keep theirs or take the public one. Do not mix the two silently.

Leave extra files that exist only in this folder (not in the public kit).

---

## Replace list (full kit only)

Replace with the public version (unless it is on the keep list):

- `skills/`
- `templates/` other than `templates/analysis/` when that folder is kept
- `adapters/`
- `examples/`
- `policies/` other than kept policy files
- `START.md`, `README.md`, `AGENTS.md`, `LICENSE`, `CHANGELOG.md`, `DESIGN_PRINCIPLES.md`

If workshop files appear after the fetch (`dev/`, `SPEC.md`, `BACKLOG.md`, `tests/`, `pytest.ini`, `requirements-dev.txt`, `scripts/install.py`): delete them. Do not mention them.

---

## Skills only (kit folder)

When they say **Update the skills** and this is the kit:

1. Fetch the public kit into a **temporary** folder.
2. Replace this kit’s `skills/` with the public `skills/` (overwrite the whole folder).
3. Remove the temporary folder. Delete workshop files if they appeared.
4. Say which skills are new or changed. Do not copy skills into papers except generated files on the paper path.

Keep `researcher.md`, how-to-talk, R templates, and all paper folders. Do not edit `START.md` or policies in this mode.

---

## How to fetch (full kit)

1. Fetch the public kit into a **temporary** folder (clone or ZIP). Do not fetch into a paper folder.
2. Build the keep list and the replace list from the rules above.
3. In one short message, say what you will **keep** and what you will **replace**. If a keep-file also changed upstream, stop and wait. Otherwise continue (their “Update the kit” is enough).
4. Copy only the replace paths into **this** kit folder. Leave keep files as they are.
5. Remove the temporary folder. Delete workshop files if present.
6. Say what changed (new skills, new templates). Remind them: a paper with generated kit files does not change until they say **Update the kit** in **that paper** (from GitHub) or **Adjust this project to the new kit version** with the kit open.

Do not require them to copy files by hand.

---

## Afterward

**Kit folder:** shared conventions they kept still apply. New skills are available on the next request.

**Paper:** generated kit files now follow the public kit version in `kit-lock.yml`. Science files were not edited.

Do not use **Update the project record** for kit versions.

---

## Must not

- Clone or copy the **whole** public kit into a paper folder
- Leave `skills/` or `templates/` at the paper root
- Write science files, `data_access`, or ticks
- Replace `researcher.md` in the kit
- Replace how-to-talk, `ai-policy.md`, or `templates/analysis/` on a **full** kit update when they asked to keep them, or when those files already differ from GitHub, without asking
- Skip overwriting `skills/` when they said **Update the skills** in the **kit**
- Start a paper, fill an overview, or edit an analysis plan
- Mix keep and public text in the same file
- Ask them to download ZIP or clone the kit themselves
- Offer features marked “not in this version”
- Replace generated files in a paper while `update_policy: pinned` unless they unpinned
