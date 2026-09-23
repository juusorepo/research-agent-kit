# Agent instructions

<!-- generated: do not edit. Kit files in this paper are replaced when you Update the kit from GitHub, or when you adjust this project to the new kit version. -->

This folder is a **paper**. Generated kit files live under `.rak/runtime/` (and this file). Do not edit them. Science and paper rules stay in the files listed below.

## Do not edit

- This `AGENTS.md`
- `.rak/runtime/`

To change how the assistant talks, add `policies/how-to-talk.md` in **this paper**. To fork one skill, copy it to `.agents/skills/<name>/`. Do not copy kit files into the paper as a general habit.

## Paper-owned (you may edit)

- `layout.yml`
- `policies/data-policy.md` (including whether individual-level data stay closed)
- `policies/what-is-on.md` (ticks only)
- `policies/how-to-talk.md` — only if this paper needs a different chat tone
- `07-record/author-voice.md` — researcher-owned voice note when **Author voice** is ticked
- `.agents/skills/<name>/` — only a deliberate skill fork
- overview, analysis plan, status, tasks, manuscript, data, scripts, `07-record/`

## Lookup

For conventions and skills, use the first that exists:

1. Paper override: `.agents/skills/<name>/` or this paper’s `policies/` file
2. Generated bundle: `.rak/runtime/skills/<name>/`, `.rak/runtime/policies/`, `.rak/runtime/templates/`
3. Kit folder (`kit_path` in `layout.yml`) — only if that folder is readable

If `.rak/runtime/` is present, **do not stop** when `kit_path` is missing or unreadable. **Update the kit** in this paper fetches the public kit into a temporary folder and replaces **generated** files only — it must not clone the whole repository into this paper. **Make this paper self-contained** and **Adjust this project to the new kit version** can use a local kit if it is open; if not, use **Update the kit** from GitHub.

If there is no generated bundle and you cannot read the kit: **stop** and ask them to open the kit — unless they asked to **audit the research chain** (or **audit literature claims**) and `layout.yml` is missing, in which case follow intake on that audit skill if you can already read it (from `.rak/runtime/` or the kit).

## Skill triggers

Resolve each skill by the lookup above. The phrase is enough — no long prompt. If more than one row could fit, ask which. This table only routes; each skill file holds its own rules. If they say a phrase for a skill that exists in the kit for this paper’s `kit-lock.yml` version, use that skill even if the row is missing from the table.

| If the researcher says (or means) | Skill file | For |
|---|---|---|
| Understand the project · Where do we stand · Why did we do X | `skills/understand-research-project/SKILL.md` | Orient from the record, then suggest the next step |
| Start the project · Initiate (when `layout.yml` is missing) | `skills/start-research-project/SKILL.md` | Set up a paper folder; with a GitHub URL and no local kit, fetch a temporary copy and write generated kit files here |
| Make this paper self-contained | `skills/make-paper-self-contained/SKILL.md` | Write generated kit files into this paper so an assistant can work without the kit folder |
| Update the kit · Update the skills | `skills/update-the-kit/SKILL.md` | In this paper: replace generated kit files from GitHub (temporary fetch; not a full clone). In a kit folder: fetch the public kit |
| Develop analysis with safe data · Do T-NNN (write analysis code) | `skills/develop-analysis-with-safe-data/SKILL.md` | Write and test analysis under the data-use rules |
| Run approved Stata analysis · Do T-NNN (run on real data, Stata) | `skills/run-approved-stata-analysis/SKILL.md` | Run one named `.do` file for an agreed analysis; Windows first |
| Document a research decision · Record a research decision | `skills/document-research-decision/SKILL.md` | Record a consequential choice as a proposed note |
| Audit the research chain (full chain or one link) | `skills/audit-research-chain/SKILL.md` | Independent check of plan → code → output → manuscript → claim; new chat; diagnose only; not a certificate |
| Audit literature claims · Check claim support | `skills/audit-research-chain/SKILL.md` | Independent check of literature statements against identifiable sources; new chat; do not trust a research packet or NotebookLM as authority |
| Audit APA presentation · Check tables and figures in Word · APA layout audit | `skills/audit-apa-presentation/SKILL.md` | Independent check of the rendered Word/PDF; diagnose only; not the research chain |
| Contribute to the project | `skills/contribute-to-project/SKILL.md` | File a collaborator's remark or an open review issue in `contributions/` |
| Consolidate contributions | `skills/consolidate-contributions/SKILL.md` | Review the inbox; recommend a home for each |
| Prepare a review copy | `skills/prepare-review-copy/SKILL.md` | Google Docs snapshot of the Quarto paper (Word is a conversion step); not the canonical manuscript |
| Ingest review comments | `skills/ingest-review-comments/SKILL.md` | Open Doc comments → inbox; skip accepted suggestions |
| Sync the review copy | `skills/sync-review-copy/SKILL.md` | After suggestions are accepted in the Doc, update the manuscript |
| Review the manuscript · AI review · coarse-review · Scan for generic prose · Plain-language review | `skills/review-the-manuscript/SKILL.md` | AI findings as contributions, routed to manuscript work or the evidence work they require; does not start that work; optional external review service if this paper allows it; not an audit of the research chain |
| Draft this in my voice · Edit this in my voice · Build my voice note | `skills/author-voice/SKILL.md` | Optional; off until ticked. Draft or edit manuscript prose; does not rewrite during a scan |
| Explore alternative framings · Give me genuinely different interpretations · Diverge before synthesis · Challenge the current framing | `skills/explore-alternative-framings/SKILL.md` | Independent alternatives before synthesis; optional; not routine editing |
| Map the evidence | `skills/map-the-evidence/SKILL.md` | Draft a source-grounded evidence packet; not an audit; not an approved claim |
| Create a notebook · Delete a notebook | `skills/map-the-evidence/SKILL.md` | Create or delete this paper’s NotebookLM notebook only if they asked; write a packet only if they also named a question |
| Search with NotebookLM · Delegate a search to the notebook | `skills/map-the-evidence/SKILL.md` | Named web/Drive search only if they asked; usable hits go to Zotero first, not into the notebook |
| Sync the bibliography · Update project sources · Link the Zotero collection · Can you read Zotero | `skills/sync-project-sources/SKILL.md` | Read-only source list from a Zotero collection on this computer; copies in `08-sources/` when asked |
| Update the project record | `skills/update-project-record/SKILL.md` | After acceptance, write it into the shared record |
| Adjust this project to the new kit version | `skills/adjust-project-to-kit/SKILL.md` | Replace generated kit files from a local kit, or from GitHub if the kit folder is not here; do not edit science files |

Agreeing the analysis plan is **not** a separate skill: propose items under **Understand the project**, the researcher accepts, then **Update the project record** writes the file.

**This paper always has its own:** data-use rules (`policies/data-policy.md`), optional-features ticks (`policies/what-is-on.md`), overview, analysis plan, status, tasks, manuscript, data, scripts, outputs. Decision notes and working notes live under the record path in `layout.yml` (default `07-record/`).

## Read first

1. `layout.yml` — folder map and `kit_path`
2. `kit-lock.yml` — kit version this paper follows
3. This paper’s `policies/what-is-on.md` and `policies/data-policy.md`
4. How to talk: this paper’s `policies/how-to-talk.md` if present, otherwise `.rak/runtime/policies/how-to-talk.md`, otherwise the kit
5. Overview, analysis plan, status, tasks (`layout.yml` paths)
6. `MEMORY.md` if present

Do not load `notes/` or `claim-checks.md` by default. Files in `contributions/` are proposals, not agreed analyses. A research packet and evidential-status notes are drafts unless an approved result says otherwise. They do not override the analysis plan, accepted decisions, or approved results.

## How to talk

Follow `policies/how-to-talk.md` from the paper if it exists, otherwise from `.rak/runtime/policies/`, otherwise from the kit.

Speak as to a social science researcher. Say *analysis plan*, *research decision note*, *draft output*, *approved result*, *researcher decision needed*.
Do not say *spec*, *slug*, *RDR*, *checkpoint*, or *verified result* for an approved file.

## Rules

- You may implement, criticise, propose, and **write the files after they accept**. Acceptance can be in chat. They do not have to type the overview, plan, or decision notes themselves.
- If an analysis is not already in the agreed analysis plan, propose adding it. Do not silently edit the plan.
- A copied protocol or draft paper is background. It does not agree an analysis. Numbers in a draft manuscript are not approved results.
- If they copied existing files and the analysis plan is still empty, draft the overview and plan items from those files **in this reply**, then stop for acceptance. Include the Intellectual anchor headings. Do not invent why they are doing the paper or its distinctive contribution — invite them to dictate that part. Do not write the overview file until they accept. Do not reconstruct a log of past decisions or past AI use unless they ask to record a specific choice now.
- If the change would alter design, measurement, sample, analysis, interpretation, what the project may claim, or would narrow or replace the intellectual anchor, say **researcher decision needed**, write a proposed research decision note if needed, and **stop**.
- Before drafting or substantially revising the title, abstract, introduction, discussion, contribution statement, or a response to conceptual reviewer comments: read the intellectual anchor (if written) and any linked framing memo. Do not optimise framing only for conventionality, defensibility, or reviewer expectations. Preserve the researcher's distinctive motivation and conceptual connections. If a proposed revision changes or narrows the intellectual anchor, state what would change and request a researcher decision. The researcher may revise the anchor deliberately. An empty anchor does not block technical work.
- If this paper’s `policies/what-is-on.md` has **Author voice** ticked: before drafting or editing manuscript prose, follow `skills/author-voice/SKILL.md` (voice note if written; do not invent one). If the box is off or missing, do not apply author voice. If they said **Draft this in my voice** while it is off, stop and say to tick the box. **Scan for generic prose** still never rewrites.
- Follow `data_access`. In `restricted` mode, do not read or run row-level real data.
- Analysis reads `01-data/processed`, not `01-data/raw`. Raw stays original.
- Every result file needs a sidecar metadata record (`status: provisional` until approved).
- Extra files in `docs/` are background. They do not agree an analysis or override an approved result.
- Google Docs used for co-author review is a **review copy** (snapshot). Saying **Prepare a review copy** is enough to render Word when the snapshot is missing; Word is a conversion step, not a second manuscript. Accept small wording in the Doc, then **Sync the review copy**. Open comments become contributions. Drive syncing this folder does not merge Doc edits into Quarto. The canonical manuscript is the path `manuscript` in `layout.yml`. Word comment ingest is not in this version. To share a Word file on OneDrive instead, set `provider: word` in `review-copy.yml` — Sync and Ingest still do not run.
- Quarto papers: `paper.qmd` holds YAML, the setup chunk, and `{{< include >}}` lines. Section text lives in `_intro.qmd`, `_method.qmd`, and the other `_*.qmd` files next to it. Edit the section file. Title and abstract stay in the YAML. If this paper is still a single `paper.qmd` with the sections inside it, edit that file; do not split it unless they asked. Do not keep the same section as both a `.md` and an include. Do not assemble the paper with a script.
- Record a material AI-use event only if this paper’s `policies/what-is-on.md` has that box ticked. Default is off. Disclosure in the paper when AI affected reliability is still the researcher’s duty (`policies/ai-policy.md`).
- An AI system is not an author. Do not list one. Do not treat AI-suggested citations as read. Do not use another person’s unpublished manuscript or plan without permission.
- Do not invent bibliography records or citation keys. The file `references.bib` next to the manuscript comes from their Zotero (or other reference manager) export. If it is empty or a source is missing, ask them to export or attach it first; then put `[@key]` to match those keys. After they overwrite the file, update any `[@…]` that no longer match. Do not invent DOIs, years, or a reference list. A Zotero item key (`zotero:…`) is source identity for the source list; citation keys in the paper still come from that export.
- When you check a literature statement against an identifiable source, add a row to `claim-checks.md` beside the audit reports (parent of `paths.audits`; default `07-record/claim-checks.md`): citation key, manuscript location, source file, what was verified, date. That row is not an approved claim. The `check:` field on an AI-use event is the whole run, not a per-statement record.
- Do not edit generated kit files. Do not edit the kit folder from this paper. Propose kit wording as a note under the record path (`07-record/notes/`).
- Work only on a task assigned to this run. They assign it by naming the task (for example **Do T-004**). Kind of work on that row is the role for this run.
- Do not invent real results. Do not treat draft or synthetic numbers as approved.
- Restricted or confidential files must not be uploaded to NotebookLM or other external source tools. If this paper allows the connector and they asked to use it, do not stop for a second upload yes, and do not refuse the named mapping question as unpublished framing.

If the researcher says **Audit the research chain** or **Audit literature claims** and `layout.yml` is missing, use `audit-research-chain` (intake). Do not Start the project. Do not write a folder map or an analysis plan in that run.

If the researcher says **Start the project** or **Initiate**, and `layout.yml` is missing, use `start-research-project` from a local kit if you can read it, otherwise fetch the public kit into a **temporary** folder and follow **GitHub paper start** in that skill. Ask the interview questions (with defaults) and wait. After they reply, copy the paper skeleton and patch; do not read template files. Understand the project is the next message. Keep this folder’s name. Do not copy `CLAUDE.md`. Do not require Python or R. Do not clone the whole repository into this paper.
