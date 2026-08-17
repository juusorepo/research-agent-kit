---
name: update-the-kit
description: Fetch a new public kit version into the kit folder, or overwrite skills only. Use when they say Update the kit or Update the skills.
license: MIT
compatibility: Requires a project filesystem. No Python or R required. May fetch from GitHub.
metadata:
  version: "0.2.2"
---

# Update the kit

One job. Do not start a paper. Do not edit a paper folder.

Public kit: https://github.com/juusorepo/research-agent-kit

Follow `policies/how-to-talk.md` if present. No Python or R required. They do not need to download the kit themselves.

Do **not** say: slug, repo, init, toolchain, agent-accessible, by-paper, data_access.

**This file is complete.** Do not search workshop files or the toy example to learn how to update.

---

## When to use

They are in the **kit** folder.

**Update the skills** (or “just the skills”, “overwrite skills”): replace only `skills/` with the public copy. Overwrite. Do not compare keep-files. Do not touch anything else.

**Update the kit** (often with the public GitHub address): full kit update below. They may add **Keep my …** (for example how-to-talk and R templates).

## Confirm this is the kit

This folder must have `START.md` + `skills/` + `templates/`. It is not a paper (`layout.yml` + `ANALYSIS_PLAN.md` as the research record).

If this is a paper folder, or you cannot tell: **stop**. Ask them to open the kit folder.

If both kit and paper are open: work only in the kit path.

---

## Must not touch

- Any **paper** folder next to the kit (overview, analysis plan, decisions, data, scripts, manuscript)

On a **full** kit update, also leave the **keep list** (below).

On **Update the skills**, overwrite `skills/` even if a skill file was edited locally. Touch nothing else.

Do not copy the kit into a paper. Do not update a paper’s `kit-lock.yml` in this skill. That is a later, separate step if they ask.

---

## Keep list (full kit only)

These rules apply to **Update the kit**, not to **Update the skills**.

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

## Skills only

When they say **Update the skills**:

1. Fetch the public kit into a **temporary** folder.
2. Replace this kit’s `skills/` with the public `skills/` (overwrite the whole folder).
3. Remove the temporary folder. Delete workshop files if they appeared.
4. Say which skills are new or changed. Do not copy skills into papers.

Keep `researcher.md`, how-to-talk, R templates, and all paper folders. Do not edit `START.md` or policies in this mode.

---

## How to fetch (full kit)

1. Fetch the public kit into a **temporary** folder (clone or ZIP). Do not fetch into a paper folder.
2. Build the keep list and the replace list from the rules above.
3. In one short message, say what you will **keep** and what you will **replace**. If a keep-file also changed upstream, stop and wait. Otherwise continue (their “Update the kit” is enough).
4. Copy only the replace paths into **this** kit folder. Leave keep files as they are.
5. Remove the temporary folder. Delete workshop files if present.
6. Say what changed (new skills, new templates). Remind them: papers still follow this kit; a paper file overrides the same path. Updating a paper’s version note (`kit-lock.yml`) is optional and only if they ask.

Do not require them to copy files by hand.

---

## Afterward

Shared conventions they kept still apply. New skills are available on the next request (paper file if it exists, otherwise the kit). Do not copy skills into papers.

If they then want a paper to record the new kit version, wait for that ask. Use **Update the project record** only in the paper, and only for `kit-lock.yml` plus a status line — not for science files.

---

## Must not

- Write into a paper folder, or treat a paper as the kit
- Replace `researcher.md`
- Replace how-to-talk, `ai-policy.md`, or `templates/analysis/` on a **full** kit update when they asked to keep them, or when those files already differ from GitHub, without asking
- Skip overwriting `skills/` when they said **Update the skills**
- Start a paper, fill an overview, or edit an analysis plan
- Mix keep and public text in the same file
- Ask them to download ZIP or clone the kit themselves
- Offer literature search or other features marked “not in this version”
