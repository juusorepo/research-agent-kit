# Agent instructions

This folder is a **paper**. Defaults and skills live in the Research Agent Kit (`kit_path` in `layout.yml`).

## Paper first, then generated files, then kit

For conventions and skills, use the **first that exists**:

1. Paper override — `.agents/skills/<name>/` or this paper’s `policies/` file
2. Generated kit files — `.rak/runtime/skills/<name>/` (if this paper is self-contained)
3. The kit at `kit_path`

| Need | Paper (only a deliberate override) | Generated (`.rak/runtime/`) | Else the kit |
|---|---|---|---|
| How to talk | `policies/how-to-talk.md` | `policies/how-to-talk.md` | `policies/how-to-talk.md` |
| AI in research | `policies/ai-policy.md` | `policies/ai-policy.md` | `policies/ai-policy.md` |
| Skills | `.agents/skills/<name>/` | `skills/<name>/` | `skills/<name>/` |
| R conventions | — | `templates/analysis/r/` | `templates/analysis/r/` |
| Stata conventions | — | `templates/analysis/stata/` | `templates/analysis/stata/` |
| Tables and figures in the manuscript | — | `templates/analysis/manuscript-displays.md` | `templates/analysis/manuscript-displays.md` |

Do not edit generated kit files. Do not copy the kit into this folder as a general habit. To change how the assistant talks, add `policies/how-to-talk.md` here. To fork one skill, copy it to `.agents/skills/<name>/`.

## Skill triggers

Resolve each skill file by the lookup above: `.agents/skills/<name>/SKILL.md` if this paper has a fork, else `.rak/runtime/skills/<name>/SKILL.md` if present, else the kit `skills/<name>/SKILL.md`. The phrase is enough — no long prompt. If more than one row could fit, ask which. This table only routes; each skill file holds its own rules. If they say a phrase for a skill that exists in the kit for this paper’s `kit-lock.yml` version, use that skill even if the row is missing from the table.

| If the researcher says (or means) | Skill file | For |
|---|---|---|
| Understand the project · Where do we stand · Why did we do X | `skills/understand-research-project/SKILL.md` | Orient from the record, then suggest the next step |
| Start the project · Initiate (when `layout.yml` is missing) | `skills/start-research-project/SKILL.md` | Set up a paper folder; with a GitHub URL and no local kit, fetch a temporary copy and write generated kit files here |
| Make this paper self-contained | `skills/make-paper-self-contained/SKILL.md` | Write generated kit files so an assistant can work without the kit folder |
| Develop analysis with safe data · Do T-NNN (write analysis code) | `skills/develop-analysis-with-safe-data/SKILL.md` | Write and test analysis under the data-use rules |
| Run approved Stata analysis · Do T-NNN (run on real data, Stata) | `skills/run-approved-stata-analysis/SKILL.md` | Run one named `.do` file for an agreed analysis; Windows first |
| Document a research decision · Record a research decision | `skills/document-research-decision/SKILL.md` | Record a consequential choice as a proposed note |
| Audit the research chain (full chain or one link) | `skills/audit-research-chain/SKILL.md` | Independent check of plan → code → output → manuscript → claim; new chat; diagnose only; not a certificate |
| Audit literature claims · Check claim support | `skills/audit-research-chain/SKILL.md` | Independent check of literature statements against identifiable sources; new chat; do not trust a research packet as authority |
| Audit APA presentation · Check tables and figures in Word · APA layout audit | `skills/audit-apa-presentation/SKILL.md` | Independent check of the rendered Word/PDF; diagnose only; not the research chain |
| Contribute to the project | `skills/contribute-to-project/SKILL.md` | File a collaborator's remark or an open review issue in `contributions/` |
| Consolidate contributions | `skills/consolidate-contributions/SKILL.md` | Review the inbox; recommend a home for each |
| Prepare a review copy | `skills/prepare-review-copy/SKILL.md` | Google Docs snapshot from a Word file you rendered; not the canonical manuscript |
| Ingest review comments | `skills/ingest-review-comments/SKILL.md` | Open Doc comments → inbox; skip accepted suggestions |
| Sync the review copy | `skills/sync-review-copy/SKILL.md` | After suggestions are accepted in the Doc, update the manuscript |
| Review the manuscript · AI review | `skills/review-the-manuscript/SKILL.md` | AI findings as contributions; not an audit of the research chain |
| Explore alternative framings · Give me genuinely different interpretations · Diverge before synthesis · Challenge the current framing | `skills/explore-alternative-framings/SKILL.md` | Independent alternatives before synthesis; optional; not routine editing |
| Map the evidence | `skills/map-the-evidence/SKILL.md` | Draft a source-grounded evidence packet; not an audit |
| Sync the bibliography · Update project sources | `skills/sync-project-sources/SKILL.md` | Read-only source list from a Zotero collection; optional PDF copies in this paper’s sources folder |
| Update the project record | `skills/update-project-record/SKILL.md` | After acceptance, write it into the shared record |
| Adjust this project to the new kit version | `skills/adjust-project-to-kit/SKILL.md` | Replace generated kit files from a local kit, or from GitHub if the kit folder is not here; do not edit science files |
| Update the kit · Update the skills | `skills/update-the-kit/SKILL.md` | In a paper: replace generated kit files from GitHub (temporary fetch; not a full clone). In the kit folder: fetch the public kit |

Agreeing the analysis plan is **not** a separate skill: propose items under **Understand the project**, the researcher accepts, then **Update the project record** writes the file.

**This paper always has its own:** data-use rules (`policies/data-policy.md`), optional-features ticks (`policies/what-is-on.md`), overview, analysis plan, status, tasks, manuscript, data, scripts, outputs. Decision notes and working notes live under the record path in `layout.yml` (default `07-record/`).

## Read first

1. `layout.yml` — folder map and `kit_path`
2. `kit-lock.yml` — kit version this paper follows (started with, or last adjusted to)
3. This paper’s `policies/what-is-on.md` and `policies/data-policy.md`
4. Overview, analysis plan, status, tasks (`layout.yml` paths)
5. `MEMORY.md` if present

Do not load `notes/` by default. Files in `contributions/` are proposals, not agreed analyses.

If `kit_path` is missing or you cannot read the kit, **stop** and ask them to open the kit folder too — unless `.rak/runtime/` is present (then continue; **Update the kit** from GitHub refreshes generated files), or they asked to **audit the research chain** (or **audit literature claims**) and `layout.yml` is missing, in which case follow the audit skill (intake) if you can already read that skill.

## How to talk

Follow `policies/how-to-talk.md` from the paper if it exists, otherwise from the kit.

Speak as to a social science researcher. Say *analysis plan*, *research decision note*, *draft output*, *approved result*, *researcher decision needed*.  
Do not say *spec*, *slug*, *RDR*, *checkpoint*, or *verified result* for an approved file.

## Rules

- You may implement, criticise, propose, and **write the files after they accept**. Acceptance can be in chat. They do not have to type the overview, plan, or decision notes themselves.
- If an analysis is not already in the agreed analysis plan, propose adding it. Do not silently edit the plan.
- A copied protocol or draft paper is background. It does not agree an analysis. Numbers in a draft manuscript are not approved results.
- If they copied existing files and the analysis plan is still empty, draft the overview and plan items from those files **in this reply**, then stop for acceptance. Include the Intellectual anchor headings. Do not invent why they are doing the paper or its distinctive contribution — invite them to dictate that part. Do not write the overview file until they accept. Do not reconstruct a log of past decisions or past AI use unless they ask to record a specific choice now.
- If the change would alter design, measurement, sample, analysis, interpretation, what the project may claim, or would narrow or replace the intellectual anchor, say **researcher decision needed**, write a proposed research decision note if needed, and **stop**.
- Before drafting or substantially revising the title, abstract, introduction, discussion, contribution statement, or a response to conceptual reviewer comments: read the intellectual anchor (if written) and any linked framing memo. Do not optimise framing only for conventionality, defensibility, or reviewer expectations. Preserve the researcher's distinctive motivation and conceptual connections. If a proposed revision changes or narrows the intellectual anchor, state what would change and request a researcher decision. The researcher may revise the anchor deliberately. An empty anchor does not block technical work.
- Follow `data_access`. In `restricted` mode, do not read or run row-level real data.
- Analysis reads `01-data/processed`, not `01-data/raw`. Raw stays original.
- Every result file needs a sidecar metadata record (`status: provisional` until approved).
- Extra files in `docs/` are background. They do not agree an analysis or override an approved result.
- Google Docs used for co-author review is a **review copy** (snapshot). Accept small wording there, then **Sync the review copy**. Open comments become contributions. The canonical manuscript is the path `manuscript` in `layout.yml`. Word comment ingest is not in this version.
- Record a material AI-use event only if this paper’s `policies/what-is-on.md` has that box ticked. Default is off. Disclosure in the paper when AI affected reliability is still the researcher’s duty (`policies/ai-policy.md`).
- An AI system is not an author. Do not list one. Do not treat AI-suggested citations as read. Do not use another person’s unpublished manuscript or plan without permission.
- Do not invent bibliography records or citation keys. The file `references.bib` next to the manuscript comes from their Zotero (or other reference manager) export. If it is empty or a source is missing, ask them to export or attach it first; then put `[@key]` to match those keys. After they overwrite the file, update any `[@…]` that no longer match. Do not invent DOIs, years, or a reference list.
- Do not edit the kit from this paper. Propose kit wording as a note under the record path (`07-record/notes/`).
- Work only on a task assigned to this run. They assign it by naming the task (for example **Do T-004**). Kind of work on that row is the role for this run.
- Do not invent real results. Do not treat draft or synthetic numbers as approved.

If the researcher says **Audit the research chain** or **Audit literature claims** and `layout.yml` is missing, use the kit skill `audit-research-chain` (intake). Do not Start the project. Do not write a folder map or an analysis plan in that run.

If the researcher says **Start the project** or **Initiate**, and `layout.yml` is missing, use the kit skill `start-research-project` if you can read the kit; otherwise fetch the public kit into a temporary folder and follow **GitHub paper start**. Ask the interview questions (with defaults) and wait. After they reply, copy the paper skeleton and patch; do not read template files. Understand the project is the next message. Keep this folder’s name. Do not copy `CLAUDE.md`. Do not require Python or R. Do not clone the whole repository into this paper.
