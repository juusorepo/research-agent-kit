---
name: contribute-to-project
description: Turn a collaborator's useful remark or an open review issue into a contribution file in contributions/. Use when they say Contribute to the project, or when someone proposes a finding, method, issue, or decision, but must not edit the analysis plan or accepted decisions.
license: MIT
compatibility: Requires a project filesystem.
metadata:
  version: "0.3.4"
---

# Contribute to the project

For collaborators and their assistants. Also used by **Ingest review comments** and **Review the manuscript**.

Write a file in the contributions folder (see `layout.yml` `paths.contributions` if set, else `07-record/contributions/`). Use `contributions/template.md` from the kit (or the paper override). Name it `C-NNN-short-title.md`. Leave `status: proposed`.

For an open review issue, set `evidence_route` to one of:

| Value | Use when the issue needs |
|---|---|
| `none` | manuscript or editorial work only |
| `project-result-check` | a check against an existing analysis plan, result file, table, figure, or claim |
| `literature-check` | support from, or verification against, an identifiable source |
| `rerun-agreed-analysis` | another run of an analysis that is already agreed |
| `new-analysis` | a new or changed analysis that is not yet agreed |

Write the concrete request under **Evidence needed**. Routing is diagnostic: it does not accept a reviewer request, create an analysis-plan item, run code, or make a scientific decision. Use `none` when no evidence work is needed. For `new-analysis`, say **researcher decision needed** when design, measurement, sample, analysis, interpretation, or claims would change.

Set `source` (`collaborator`, `docs-comment`, `journal-review`, or `ai-review`). If this is a Google Doc comment, set `external_id` and `excerpt`. If this is a comment from an external review service, set `external_id` to `review-service:<review id>:<comment id>`. Do not write a file for a wording **suggestion** that belongs on the review copy.

If they asked to keep alternative framings from **Explore alternative framings**, write **one contribution file per alternative** (`type: interpretation`). Do not merge them into one averaged proposal.

For a **Scan for generic prose** finding (`source: ai-review`), set `severity` and `fix_scope`, and fill `related` when another new finding or an open task is the same work or changes how this one should be fixed. Omit `suggested_replacement` unless this paper’s `what-is-on.md` has **Propose wording in prose scans** ticked. Never apply a replacement in this run.

## Must not

- Edit `RESEARCH_CONTEXT.md`, `ANALYSIS_PLAN.md`, `STATUS.md`, or accepted decision notes
- Mark a contribution `integrated`
- Approve results
- Treat this as agreeing an analysis
- Treat `evidence_route` as approval to perform the work
- Duplicate an existing `external_id`

Say: this is in the inbox for the lead researcher. It is not yet part of the project record.
