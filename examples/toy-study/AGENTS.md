# Agent instructions

This project uses the Research Agent Kit. The installed version is recorded only in `kit-lock.yml`.

## Read first

1. `kit-lock.yml` — installed kit and skill versions
2. `layout.yml` — where folders live (do not assume `02-scripts` or `analysis/`)
3. `policies/data-policy.md` — data-use rules, including `data_access`
4. The paper’s project overview, analysis plan, status, and tasks (paths from `layout.yml`)
5. `MEMORY.md` if present — which files are canonical vs proposal vs note

Do not load `notes/` by default. Files in `contributions/` are proposals, not agreed analyses.

## How to talk

Say *analysis plan*, *research decision note*, *draft output*, *approved result*, *researcher decision needed*.  
Do not say *spec*, *RDR*, *checkpoint*, or *verified result* for an approved file.

## Rules

- You may implement, criticise, propose, and **write the files after they accept**. Acceptance can be in chat. They do not have to type the overview, plan, or decision notes themselves.
- If an analysis is not already in the agreed analysis plan, propose adding it. Do not silently edit the plan.
- A copied protocol or draft paper is background. It does not agree an analysis. Numbers in a draft manuscript are not approved results.
- If they copied existing files and the analysis plan is still empty, draft the overview and plan items from those files, then stop for acceptance. Do not reconstruct a log of past decisions or past AI use unless they ask to record a specific choice now.
- If the change would alter design, measurement, sample, analysis, interpretation, or what the project may claim, say **researcher decision needed**, write a proposed research decision note if needed, and **stop**.
- Follow `data_access`. In `restricted` mode, do not read or run row-level real data.
- Extra files in `docs/` are background. They do not agree an analysis or override an approved result.
- Google Docs or Word copies used for co-author review are snapshots. The canonical manuscript is the path `manuscript` in `layout.yml`.
- Record a material AI-use event when the contribution is clearly material. Do not record orientation. Ask only if it is ambiguous.
- Work only on a task assigned to this run.
- Do not invent real results. Do not treat draft or synthetic numbers as approved.

Skills are installed under `.agents/skills/`. Use them by name when the job matches.
