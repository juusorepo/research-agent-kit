# Shared research record

These files are small on purpose. Do not turn them into logs.

| File | Role | How to treat it |
|---|---|---|
| `RESEARCH_CONTEXT.md` | Stable orientation: problem, questions, design, data and its limits, constructs, terms, constraints. May include an **intellectual anchor** (why this project exists in the researcher’s own terms) | Canonical orientation. Rewrite in place. The Data section describes available data; it does not override the analysis plan, accepted notes, or approved results. The intellectual anchor is researcher-owned: preserve it unless they explicitly revise it. It is not an agreed analysis, approved result, or factual authority. |
| `07-record/author-voice.md` | Optional **voice note** (how manuscript prose should sound in this paper) | Researcher-owned. Only used if **Author voice** is ticked. Empty is fine. Not the intellectual anchor and not chat tone. |
| `STATUS.md` | Hot memory: stage, active work, blockers, open scientific questions | Hint only. Rewrite in place under the template headings. The analysis plan wins if they disagree. |
| `TASKS.md` | Remaining work. Kind of work is the role for the next run. | Temporary. Not the analysis plan. |
| `ANALYSIS_PLAN.md` | What analyses are **agreed** | Canonical. Agents propose; you accept. |
| `07-record/decisions/` | Research decision notes for important choices | Canonical once **accepted**. `INDEX.md` is a compact list, not a narrative. |
| `07-record/contributions/` | Inbox from collaborators, leftover Doc comments, journal points, AI review | **Proposal only.** Open issues, not accepted wording suggestions. |
| `review-copy.yml` (next to the manuscript) | Pointer to the current Google Docs review copy | Snapshot. Canonical paper is `paper.qmd` plus its `_*.qmd` section files. Drive syncing does not merge Doc edits into Quarto. |
| `07-record/notes/` | Working notebook | For later recall. **Do not load by default.** |
| `07-record/ai-use/` | Optional notes of substantial AI work | Off unless ticked in `policies/what-is-on.md`. One short file per event — not a prompt log. Off does not replace disclosure in the paper. |
| `07-record/claim-checks.md` | Per-statement literature checks (citation key, manuscript location, source, what was verified) | Written when a source was actually opened. Not an approved claim. Do not load by default. The `check:` field on an AI-use event is the whole run. |
| `07-record/audits/` | Reports from checking the research chain | History of a check. **Not** the analysis plan or an approved result. Do not load by default. |

Conversation or Google Doc comment → contribution (inbox) → your review → canonical record.  
Accepted wording in the Google Doc → **Sync the review copy** (not one contribution per comma).  
A contribution never skips the inbox path.

Shared conventions live in the kit. This paper may add the same file to override that default.

## Who writes

The assistant may draft these files. You accept (in chat is enough). Then the assistant updates the file. Accepting is the scientific act; typing is not.

## Starting from work you already have

Usual case. Copy the protocol, preregistration, or draft paper into `06-docs/` and `05-outputs/manuscript/`. Those files are **source material**. They do not become the analysis plan, and manuscript numbers do not become approved results, until you accept the corresponding record. The assistant should read them before suggesting next steps.

Decision notes and AI-use notes start from when this folder was created. Do not invent a history of earlier choices or earlier AI use. One line in the overview is enough (record started on DATE from the existing draft). If a past choice still governs the work, record that one decision now — as a new note, not a reconstructed log.
