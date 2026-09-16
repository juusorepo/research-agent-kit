---
name: adjust-project-to-kit
description: Align this paper with the current kit after the researcher accepts. With generated kit files, replace that bundle. Without them, one-time migrate or a small instruction patch. Use when they say Adjust this project to the new kit version. Do not edit science files.
license: MIT
compatibility: Requires a project filesystem. No Python or R required.
metadata:
  version: "0.5.2"
---

# Adjust this project to the new kit version

One job. Record that this paper follows the current kit. Do not change the science.

They are in **one paper** folder. Prefer a readable local kit (`kit_path` in `layout.yml`). If the kit is missing, use **Update the kit** from GitHub (paper path) instead of stopping.

Follow `policies/how-to-talk.md` if present. Say *adjust this project to the new kit version*. Do not say migrate, upgrade, module, or runtime unless they used those words.

The version number lives only in `kit-lock.yml`. Do not write a kit version into `what-is-on.md`.

**This file is complete.** Do not search workshop files or the toy example to learn how to adjust.

---

## When to use

They say **Adjust this project to the new kit version** (or mean that: align this paper after **Update the kit**).

If they are in the **kit** folder (`START.md` + `skills/` + `templates/`): **stop**. Ask them to open the paper. If they meant to fetch a new kit, use `skills/update-the-kit/SKILL.md` first.

If `kit_path` is missing or you cannot read the kit: do **not** stop if this paper already has generated files or they gave a GitHub URL. Use `skills/update-the-kit/SKILL.md` **paper path** (fetch GitHub into a temporary folder; replace generated files only). Prefer `.rak/runtime/skills/update-the-kit/SKILL.md` if present. If there are no generated files and no GitHub URL, ask them to open the kit **or** paste **Update the kit from https://github.com/juusorepo/research-agent-kit**.

Which path:

1. **Generated kit files present** (`.rak/runtime/` or `kit-lock.yml` has `runtime: materialised`) — replace the generated files. Do not line-patch `AGENTS.md`.
2. **No generated files** — offer **Make this paper self-contained** (preferred). If they want to stay on a hand-maintained `AGENTS.md` for now, use the **small patch** path below (old papers only). Do not extend that path.

---

## Must not edit (every path)

Never write these, in this skill, even after they accept:

- Overview (`RESEARCH_CONTEXT.md`)
- Analysis plan (`ANALYSIS_PLAN.md`)
- Decision notes and `decisions/INDEX.md`
- Output files and output metadata
- Canonical manuscript (do not rewrite it into includes)
- Data (raw, processed, metadata)
- Scripts
- Contributions, notes, audits, proposals, AI-use events, source records, evidence packets
- `layout.yml`
- `policies/data-policy.md` (inspect only). Do not change `data_access`.
- `TASKS.md` (do not add, close, or create a task)
- `.agents/skills/` (paper forks stay)
- `policies/what-is-on.md` ticks (do not tick new boxes; do not insert new optional boxes unless they asked)

Do not invent analyses. Do not approve results. Do not write a research decision note or an AI-use event for this alignment. Do not three-way merge `AGENTS.md`. Do not replace the whole of `what-is-on.md`.

---

## Path A — replace generated kit files

### Inspect

Read:

1. This paper’s `kit-lock.yml` and the kit `templates/project/kit-lock.yml`
2. `.rak/runtime.manifest.json` if present
3. `layout.yml` (`kit_path`)
4. This paper’s `policies/what-is-on.md` (ticks only; do not edit)
5. `policies/data-policy.md` — confirm `data_access` is present. If missing, say so. Do not fill it in.

**Pinned:** if `update_policy: pinned` (or they said this paper is pinned), show that a newer kit exists and **do not replace**. Wait. They may say to unpin (then use `latest-compatible`) or not now.

**Unknown or unavailable options:** if `what-is-on.md` enables something the kit does not list as optional, or marks **Not in this version**, **stop**. Say it is unknown or not available. Do not ignore it. Do not treat it as off.

**Missing ticks are not “off”:** do not disable shipped skills because a future box is absent.

**Checksum:** for each path in the manifest, hash the current file (SHA-256). If a generated file was edited (hash ≠ manifest) and it is not already a paper fork under `.agents/skills/` or paper `policies/`: **stop**. Offer (1) discard the edit and replace, or (2) move that file to `.agents/skills/` or paper `policies/` and then replace. Do not merge.

If `kit:` already matches the kit template, the manifest matches the current kit files, and nothing is dirty: say it is already aligned. Write nothing.

### Propose, then wait

Show:

- Current paper kit version and the kit version
- Files that would be **added, changed, or removed** under `.rak/runtime/` and the generated `AGENTS.md` (names, not a line diff of the skill table)
- That science files, data-use rules, ticks, and `.agents/skills/` stay as they are

Then a numbered list with defaults, and **stop**:

1. Accept the replacement (**yes**)
2. Not now

Do not write files in this inspect turn.

### After they accept

1. Follow **Make this paper self-contained** copy steps (overwrite generated files; keep paper-owned files).
2. `kit-lock.yml` — copy `kit:` and `skills:` from the kit template. Keep `runtime: materialised`. Keep `update_policy` unless they unpinned. Keep extra top-level keys this paper already had. Do not invent numbers.
3. Replace `.rak/runtime.manifest.json` with new hashes.
4. `STATUS.md` — under existing headings, add or refresh **one factual line** that generated kit files now follow the kit in `kit-lock.yml`. Do not rewrite other STATUS content.
5. If this paper has no `CLAUDE.md`, copy `templates/paper-skeleton/CLAUDE.md`. Do not overwrite an existing one.

Say what changed. Remind them: agreed analyses, decision notes, outputs, manuscript, data, and data-use rules were not edited. If `.agents/skills/` has a fork, warn that this paper is not on the stock skill for that name.

---

## Path B — small patch (no generated files yet)

Use only if they refused self-contained copy for now.

Inspect as in 0.3.2: `kit-lock.yml`, `layout.yml`, this paper’s `AGENTS.md` vs kit `templates/project/AGENTS.md`, `what-is-on.md`, `data-policy.md`.

**Unknown or unavailable enabled options fail visibly.** Missing future ticks are not “off”. Visibility is not availability: a skill phrase that exists in this paper’s `kit-lock.yml` version still runs if the row is missing from the table.

If `kit:` already matches and nothing else needs a patch: say it is already aligned. Write nothing.

Propose **exact line patches**. Do **not** replace the whole of `AGENTS.md` or `what-is-on.md` on this path. Keep every paper-specific sentence unless they accepted deleting that exact text.

Typical patch: copy `kit:` and `skills:` into `kit-lock.yml`; add any missing skill-trigger **row** to `AGENTS.md`. If this paper has no `CLAUDE.md`, offer the skeleton pointer.

Wait for yes / only some / not now. Do not write files in this inspect turn.

After yes: apply accepted patches only; one factual STATUS line; do not change `data_access`.

Prefer they then say **Make this paper self-contained** so later adjustments replace generated files instead of patching `AGENTS.md`.

---

## Must not

- Write science files, data, `layout.yml`, or `TASKS.md`
- Change `data_access` or overwrite `policies/data-policy.md`
- Line-patch generated `AGENTS.md` when Path A applies
- Replace the whole of `what-is-on.md`
- Ignore an unknown or unavailable enabled option
- Treat a missing future tick as “off”
- Tick optional features they did not tick
- Replace generated files while `update_policy: pinned` unless they unpinned
- Three-way merge
- Align the paper without a yes in this chat
- Fetch GitHub or update the kit folder (that is **Update the kit**)
- Treat this as **Update the project record**
- Offer features marked “not in this version”
- Use developer slang in chat
