# Agent instructions

This folder is a **paper**. Defaults and skills live in the Research Agent Kit (`kit_path` in `layout.yml`).

## Paper first, then kit

For conventions and skills, use the **paper file if it exists**, otherwise the same path in the kit.

| Need | Paper (only if you added it) | Else the kit |
|---|---|---|
| How to talk | `policies/how-to-talk.md` | `policies/how-to-talk.md` |
| AI in research | `policies/ai-policy.md` | `policies/ai-policy.md` |
| Skills | `.agents/skills/<name>/` | `skills/<name>/` |
| R conventions | `templates/analysis/r/` | `templates/analysis/r/` |

Do not copy the kit into this folder. Override a default by adding that one file here.

**This paper always has its own:** data-use rules (`policies/data-policy.md`), optional-features ticks (`policies/what-is-on.md`), overview, analysis plan, status, tasks, manuscript, data, scripts, outputs. Decision notes and working notes live under the record path in `layout.yml` (default `07-record/`).

## Read first

1. `layout.yml` — folder map and `kit_path`
2. `kit-lock.yml` — kit version this paper was started with
3. This paper’s `policies/what-is-on.md` and `policies/data-policy.md`
4. Overview, analysis plan, status, tasks (`layout.yml` paths)
5. `MEMORY.md` if present

Do not load `notes/` by default. Files in `contributions/` are proposals, not agreed analyses.

If `kit_path` is missing or you cannot read the kit, **stop** and ask them to open the kit folder too.

## How to talk

Follow `policies/how-to-talk.md` from the paper if it exists, otherwise from the kit.

Speak as to a social science researcher. Say *analysis plan*, *research decision note*, *draft output*, *approved result*, *researcher decision needed*.  
Do not say *spec*, *slug*, *RDR*, *checkpoint*, or *verified result* for an approved file.

## Rules

- You may implement, criticise, propose, and **write the files after they accept**. Acceptance can be in chat. They do not have to type the overview, plan, or decision notes themselves.
- If an analysis is not already in the agreed analysis plan, propose adding it. Do not silently edit the plan.
- A copied protocol or draft paper is background. It does not agree an analysis. Numbers in a draft manuscript are not approved results.
- If they copied existing files and the analysis plan is still empty, draft the overview and plan items from those files **in this reply**, then stop for acceptance. Do not write the overview file until they accept. Do not reconstruct a log of past decisions or past AI use unless they ask to record a specific choice now.
- If the change would alter design, measurement, sample, analysis, interpretation, or what the project may claim, say **researcher decision needed**, write a proposed research decision note if needed, and **stop**.
- Follow `data_access`. In `restricted` mode, do not read or run row-level real data.
- Extra files in `docs/` are background. They do not agree an analysis or override an approved result.
- Google Docs or Word copies used for co-author review are snapshots. The canonical manuscript is the path `manuscript` in `layout.yml`.
- Record a material AI-use event only if this paper’s `policies/what-is-on.md` has that box ticked. Default is off. Disclosure in the paper when AI affected reliability is still the researcher’s duty (`policies/ai-policy.md`).
- An AI system is not an author. Do not list one. Do not treat AI-suggested citations as read. Do not use another person’s unpublished manuscript or plan without permission.
- Work only on a task assigned to this run. They assign it by naming the task (for example **Do T-004**). Kind of work on that row is the role for this run.
- Do not invent real results. Do not treat draft or synthetic numbers as approved.

If the researcher says **Start the project** or **Initiate**, and `layout.yml` is missing, use the kit skill `start-research-project`. Read the name from the kit `researcher.md`. Ask the interview questions (with defaults) and wait. Read existing and uploaded files before suggesting next steps. Keep this folder’s name. Do not copy `CLAUDE.md`. Do not require Python or R.
