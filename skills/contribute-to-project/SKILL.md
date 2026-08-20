---
name: contribute-to-project
description: Turn a collaborator's useful remark or an open review issue into a contribution file in contributions/. Use when they say Contribute to the project, or when someone proposes a finding, method, issue, or decision, but must not edit the analysis plan or accepted decisions.
license: MIT
compatibility: Requires a project filesystem.
metadata:
  version: "0.3.0"
---

# Contribute to the project

For collaborators and their assistants. Also used by **Ingest review comments** and **Review the manuscript**.

Write a file in the contributions folder (see `layout.yml` `paths.contributions` if set, else `07-record/contributions/`). Use `contributions/template.md` from the kit (or the paper override). Name it `C-NNN-short-title.md`. Leave `status: proposed`.

Set `source` (`collaborator`, `docs-comment`, `journal-review`, or `ai-review`). If this is a Google Doc comment, set `external_id` and `excerpt`. Do not write a file for a wording **suggestion** that belongs on the review copy.

## Must not

- Edit `RESEARCH_CONTEXT.md`, `ANALYSIS_PLAN.md`, `STATUS.md`, or accepted decision notes
- Mark a contribution `integrated`
- Approve results
- Treat this as agreeing an analysis
- Duplicate an existing `external_id`

Say: this is in the inbox for the lead researcher. It is not yet part of the project record.
