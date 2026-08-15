---
name: understand-research-project
description: Retrieve project memory and suggest the next step. Use at the start of a session, after Start the project, or for questions like why did we do X.
license: MIT
compatibility: Requires a project filesystem.
metadata:
  version: "0.1.0"
---

# Understand the project

Orientation and retrieval. Do not create an AI-use event for this skill alone. Do not load everything.

## Before you suggest next steps

Read what is already in the folder **and** what they attached in this chat. Do this before the next-step list.

Look for: protocol, preregistration, analysis plan, draft manuscript, codebook, overview. Paths are in `layout.yml` (defaults: `06-docs/`, `05-outputs/manuscript/`). Also any `ANALYSIS_PLAN.md` they already wrote.

Do not invent files. Do not assume a blank project.

## Retrieval order (stop when you can answer)

1. `RESEARCH_CONTEXT.md` — canonical orientation (path from `layout.yml`)
2. `STATUS.md` — hint only
3. `ANALYSIS_PLAN.md` — canonical agreed analyses
4. Decision notes (`07-record/decisions/INDEX.md` unless `layout.yml` says otherwise) — then only the relevant notes
5. `contributions/` — only if the question is about a pending proposal
6. `notes/` and Git — **only if the researcher asks or the files above are not enough**

Also read: `layout.yml` (`kit_path`), this paper’s `what-is-on.md` and data-use rules, how-to-talk (paper if present, else kit), manuscript folder (is there a draft?), result-file metadata. If you cannot read the kit, stop and ask them to open it.

## Say what kind of source it is

| Kind | Where |
|---|---|
| Canonical | overview, agreed plan items, **accepted** decision notes, approved results |
| Proposal | `contributions/`, `proposals/`, decision notes still `proposed` |
| Superseded | decision notes with `status: superseded` |
| Tentative | `notes/`, `STATUS.md` |
| Source material | copied protocol, prereg, draft paper — not yet agreed |

If status and the analysis plan disagree, the **plan** wins. Extra files in `06-docs/` do not agree an analysis. A draft manuscript is not a set of approved results.

## If they started from existing files (usual)

Look in `06-docs/` and `05-outputs/manuscript/` as well as the templates.

Say clearly:

- What was copied or already present (background / source material)
- Whether they already have an analysis plan file — if yes, draft kit plan *items* from it; do not ignore it
- The kit analysis plan is empty until they accept items (unless they already accepted)
- Decision notes and AI-use are blank on purpose — the record starts now
- Do not reconstruct a pre-history of choices or AI use unless they ask to record a **specific** past choice now (one new note, not a log)

If the plan is empty and they copied source files, the fitting next step is: draft the overview and proposed plan items from those files (write `proposals/A-NNN.md` if useful), then **stop for acceptance**. After they accept, use **Update the project record**. You may refresh `STATUS.md` to “existing draft copied; analysis plan not yet agreed.”

If they already have a filled analysis plan or a near-final draft, do not offer “fill the overview” as if nothing exists. Offer the matching next step (map the existing plan into agreed items, or continue analysis, or work from approved results).

## Say back

- What they already copied or uploaded (plan, draft manuscript)
- Agreed analyses — invent none
- Which have an approved result
- Open proposals, contributions, and proposed decisions
- What is optional and off

## Then suggest what to do next

Only after the read above. Only these, and only those that fit **this** folder:

1. Fill the overview  
2. Specify the analysis plan  
3. Record a research decision  
4. Start or continue analysis  
5. Work on the manuscript (approved results only)  
6. Review pending contributions (if any)

Do not offer a literature search.

## Must not

- Invent facts or a back-history of decisions / AI use
- Load `notes/` by default
- Write an AI-use event for orientation
- Edit the analysis plan before they accept
- Treat a copied protocol or draft paper as already agreed
- Suggest next steps before reading existing and uploaded files
