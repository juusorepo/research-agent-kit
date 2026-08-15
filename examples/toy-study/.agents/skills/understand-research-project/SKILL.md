---
name: understand-research-project
description: Read the shared research record and say where the project stands. Use at the start of a session, before analysis, or when asked what is agreed.
license: MIT
compatibility: Requires a project filesystem.
metadata:
  version: "0.1.0"
---

# Understand the project

Orientation only. Do not create an AI-use event for this skill alone.

## Read in this order

1. `AGENTS.md`
2. `kit-lock.yml` (version lives only here)
3. `layout.yml` — resolve every later path from `paths`
4. `policies/data-policy.md` (`data_access`)
5. `STATUS.md` as a **hint only**
6. Project overview
7. **`ANALYSIS_PLAN.md`** — this is what is agreed
8. Result-file metadata under `paths.outputs`
9. Proposals, decision notes, tasks
10. `docs/` for extra context (prereg, ethics). **I10:** this does not agree an analysis or override an approved result
11. `ai-use/` if present

If `STATUS.md` disagrees with the analysis plan, the **plan** wins. Say that.

## Say back (researcher language)

- Folder preset and manuscript/code formats from `layout.yml`
- `data_access` mode
- Agreed analyses (`A-NNN`) from the plan — invent none
- Which of those have an **approved** result
- Open proposals and proposed research decision notes
- The task assigned to this run, if any

## Must not

- Invent facts or numbers
- Treat `docs/` as agreeing an analysis
- Write `ai-use/AI-*.yml` for orientation
- Edit the analysis plan
