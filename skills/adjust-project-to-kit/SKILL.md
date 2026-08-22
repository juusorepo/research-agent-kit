---
name: adjust-project-to-kit
description: Align this paper's instructions and version note with the current kit, after the researcher accepts. Use when they say Adjust this project to the new kit version. Do not edit science files.
license: MIT
compatibility: Requires a project filesystem. No Python or R required.
metadata:
  version: "0.3.3"
---

# Adjust this project to the new kit version

One job. Record that this paper follows the current kit. Do not change the science.

They are in **one paper** folder. The kit must be readable (`kit_path` in `layout.yml`).

Follow `policies/how-to-talk.md` if present. Say *adjust this project to the new kit version*. Do not say migrate, upgrade, or module unless they used those words.

The version number lives only in `kit-lock.yml`. Do not write a kit version into `AGENTS.md` or `what-is-on.md`.

**This file is complete.** Do not search workshop files or the toy example to learn how to adjust.

---

## When to use

They say **Adjust this project to the new kit version** (or mean that: align this paper after **Update the kit**).

If they are in the **kit** folder (`START.md` + `skills/` + `templates/`): **stop**. Ask them to open the paper. If they meant to fetch a new kit, use `skills/update-the-kit/SKILL.md` first.

If `kit_path` is missing or you cannot read the kit: **stop**. Ask them to open the kit folder too.

---

## Must not edit

Never write these, in this skill, even after they accept:

- Overview (`RESEARCH_CONTEXT.md`)
- Analysis plan (`ANALYSIS_PLAN.md`)
- Decision notes and `decisions/INDEX.md`
- Output files and output metadata
- Canonical manuscript
- Data (raw, processed, metadata)
- Scripts
- Contributions, notes, audits, proposals, AI-use events
- `layout.yml`
- `policies/data-policy.md` (inspect only). Do not change `data_access`.
- `TASKS.md` (do not add, close, or create a task)

Do not invent analyses. Do not approve results. Do not tick a new optional box for them. Do not write a research decision note or an AI-use event for this alignment.

---

## Inspect (before you propose)

Read, in this order:

1. This paper’s `kit-lock.yml` and the kit `templates/project/kit-lock.yml`
2. `layout.yml` (`kit_path`)
3. This paper’s `AGENTS.md` and the kit `templates/project/AGENTS.md`
4. This paper’s `policies/what-is-on.md` and the kit `policies/what-is-on.md`
5. This paper’s `policies/data-policy.md` — confirm `data_access` is present. If it is missing, say so. Do not fill it in. Do not copy the kit policy over theirs.

Do not load `notes/`, `audits/`, or the manuscript. You may read `STATUS.md` only so you can add a short configuration note later if they accept.

**Unknown or unavailable options:** compare ticked or named optional items in this paper’s `what-is-on.md` with the kit `policies/what-is-on.md`. If this paper enables something the kit file does not list as optional in this version, or that the kit marks **Not in this version**, **stop**. Say it is unknown or not available in this kit. Do not ignore it. Do not treat it as off. The same if `AGENTS.md` points at a skill folder that is missing from the kit.

**Missing settings are not “off”:** an unadjusted paper, or a `what-is-on.md` with no extra ticks, keeps current 0.3.x behaviour. Do not disable shipped skills because a future tick is absent.

**Visibility is not availability:** if they say a skill phrase that exists in the kit for this paper’s `kit-lock.yml` version, that skill still runs even if a later table hides the row. Do not remove 0.3.x routes from `AGENTS.md` unless they accepted that exact deletion.

If this paper’s `kit:` already matches the kit template and nothing else needs a patch: say it is already aligned. Write nothing.

---

## Propose, then wait

Compare first. In one short message, show only **configuration and instruction** patches:

- Current paper version and the kit version
- For each file: the **exact** lines you would add or delete (a minimal patch). Do not propose replacing the whole of `AGENTS.md` or `what-is-on.md`
- What stays as it is (science files; this paper’s data-use rules and `data_access`; optional ticks they already chose; paper-specific wording)

Typical 0.3.2 alignment: copy `kit:` and `skills:` from the kit `templates/project/kit-lock.yml` (do not invent numbers; keep any extra top-level keys this paper already had); add any missing skill-trigger **row** to `AGENTS.md`. `what-is-on.md` often needs no edit.

Keep every paper-specific sentence and row they already have, unless they accepted deleting that exact text.

Then a numbered list with defaults, and **stop**:

1. Accept the patches (**yes**)
2. Accept only some patches (they name which)
3. Not now

Do not write files in this inspect turn.

---

## After they accept

Write only the accepted patches:

1. `kit-lock.yml` — copy `kit:` and `skills:` from the kit template. Do not invent numbers. Keep extra top-level keys this paper already had.
2. `AGENTS.md` — apply the accepted line patch only. Do not replace the file.
3. `policies/what-is-on.md` — only if they accepted a patch; keep their ticks; never make data-use rules optional
4. `STATUS.md` — under the existing template headings, add or refresh **one factual line** that this paper’s instructions and version note now follow the kit in `kit-lock.yml`. Do not rewrite other STATUS content. Do not add dated headings. Do not treat this as a scientific event, a research decision, or a task.

Say what changed. Remind them: agreed analyses, decision notes, outputs, manuscript, data, and data-use rules were not edited.

---

## Must not

- Write science files, data, `layout.yml`, or `TASKS.md`
- Change `data_access` or overwrite `policies/data-policy.md`
- Replace the whole of `AGENTS.md` or `what-is-on.md`
- Ignore an unknown or unavailable enabled option
- Treat a missing future tick as “off”
- Tick optional features they did not tick
- Align the paper without a yes in this chat
- Fetch GitHub or update the kit folder (that is **Update the kit**)
- Treat this as **Update the project record**
- Offer features marked “not in this version”
- Use developer slang in chat
