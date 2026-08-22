# Changelog

## 0.3.2 — 2026-08-21

You can **Adjust this project to the new kit version**. The assistant inspects this paper, shows the exact instruction and version-note patches, and waits for a yes. It does not edit the analysis plan, decision notes, outputs, manuscript, or data. Updating the kit still leaves every paper folder untouched until you ask.

## 0.3.1 — 2026-08-20

Acceptance is one routine: the decision note, who accepted it and when, the plan’s link to that note, the matching task, and STATUS are updated together. STATUS keeps five headings and is rewritten in place. Analysis reads processed data, not raw originals. Every result file needs a sidecar metadata record (draft until you approve it). Pilots stay in a `_dev` folder; if a file cannot be deleted, it goes to quarantine. Keys stay out of chat and out of committed files.

## 0.3.0 — 2026-08-20

Co-authors can work in a **Google Docs review copy**. Small wording is accepted there (like track changes), then you **sync** once back to the paper. Leftover **open comments**, journal points, and an **AI manuscript review** land in the same contributions inbox — not a second reviews folder, and not one file per comma. Word comment ingest is not in this version. Google’s Docs tools, if the assistant has them, are optional; a pasted comment list still works.

## 0.2.5 — 2026-08-20

A short phrase is enough. The paper `AGENTS.md` now lists which phrase opens which skill (Understand the project, Audit the research chain, Record a research decision, and the rest). How each skill works is still only in that skill file. Each skill’s short description names the same phrase, so tools that match descriptions and tools that read the table agree.

## 0.2.4 — 2026-08-20

After an audit, the full report is the saved file. Chat stays short: what holds, the four links, then a numbered list with defaults. Findings may name the kind of work; they do not draft a patch or a prompt to paste into a coding chat. Next work is **Do T-004**. What is agreed (plan and accepted notes) is always read first; a stale STATUS line is only in scope when it changes that.

## 0.2.3 — 2026-08-18

The example paper follows the kit for skills (no extra copy in the paper). Agreeing analyses is a next step after Understand the project — not a separate skill. The Quarto helpers follow the folder map. Restricted data remains a rule the assistant follows; it is not a lock on the files.

Say **Start the project**. The assistant finds the kit, writes only into the paper folder, and asks the usual questions. You do not need a longer paste.

After an audit, the assistant asks a short list — decide now, add to the task list, or later — then waits. What you accept is written on the task list (`later` if you said later), so you do not have to remember.

## 0.2.2 — 2026-08-17

After an audit, remaining work goes on the task list. Kind of work is the role for the next chat (write analysis code, record a research decision, and so on). Say **Do T-004** to assign it. The checking chat does not start the coding.

The README now says how the kit works in one place: one kit, many papers; you accept; then the file is written.

If you copied a protocol, preregistration, or draft and the overview is still empty, the assistant should draft that overview in the same reply — not put “fill the overview” on a later list — and write the file only after you accept.

You can **Update the kit** from GitHub without overwriting your name, how you asked the assistant to talk, or your R templates, and without changing any paper folder. **Update the skills** overwrites only the skills folder.

## 0.2.0 — 2026-08-17

You can ask the assistant to audit the research chain (analysis plan through claims). It diagnoses; it does not repair. The report is a record of a check, not a new source of scientific truth. You may ask for the full chain or one link.

## 0.1.1 — 2026-08-15

A short note now says how this kit sits next to national AI-in-research guidance, and where it does not try to replace it. The optional AI-use file is still off by default; that does not mean material use may stay hidden in the paper. Restricted data still means row-level files stay closed; a cloud assistant may still send project text to a vendor.

## 0.1.0 — 2026-08-15

Frozen v0.1: skills, `layout.yml` presets, Quarto and R stubs, data-use policy, toy study, and file-assertion tests T1–T13.

Lean project memory: overview + analysis plan + status; `decisions/INDEX.md`; collaborator inbox (`contributions/`); working `notes/` not loaded by default. Keep the name `ANALYSIS_PLAN.md`. AI-use stays one optional file per event.

Usual start is an existing draft: copy into `06-docs/` and `05-outputs/manuscript/`; assistant reads those files before next steps; drafts; researcher accepts; assistant writes. No reconstructed pre-history of decisions or AI use.

Start path: one kit folder; papers follow it unless they add an override file. Interview asks questions with defaults, then waits. First-level folders are numbered (`01-data` … `07-record`). The manuscript is `05-outputs/manuscript/`. Papers use `AGENTS.md` (no `CLAUDE.md`). Agent sessions need the kit visible. No Python or R required.

The public kit is researcher-facing. Workshop files (`dev/`, including the spec and the “update the changelog” habit, plus tests) stay on the builder machine and are removed if they appear in a copy.
