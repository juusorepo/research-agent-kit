---
name: consolidate-contributions
description: For the lead researcher. Review pending contributions and recommend where each should go. Use when they say Consolidate contributions. Do not silently change the analysis plan or accept decisions.
license: MIT
compatibility: Requires a project filesystem.
metadata:
  version: "0.3.1"
---

# Consolidate contributions

For the lead researcher / person who stewards the record.

Read `contributions/` files with `status: proposed`. For each, **recommend** one home:

- integrate into the project overview
- add or change an analysis-plan item (still a proposal until they accept)
- create or update a research decision note (still proposed until they accept)
- add a task
- apply a manuscript wording change (only after they accept; not a substitute for **Sync the review copy** when the wording was already accepted in Google Docs)
- keep as a working note in `notes/`
- archive or reject

For review findings, use `evidence_route` before recommending a manuscript edit:

- `none` — ordinary manuscript/editorial route
- `project-result-check` — a separate **Audit the research chain** run for the named link
- `literature-check` — **Audit literature claims** for a named source and statement, or **Map the evidence** if sources still need to be found
- `rerun-agreed-analysis` — a later assigned task tied to the existing agreed analysis
- `new-analysis` — an analysis proposal; add a proposed research decision note when the science would change

The lead researcher may accept, reject, or redirect the reviewer request. Do not convert an evidence route directly into analysis code, an agreed plan item, or an approved result. Do not apply manuscript wording that depends on evidence which has not yet been checked or produced.

If the science would change, say **researcher decision needed**. Editorial nits are not research decisions.

## Must not

- Automatically make scientifically consequential decisions
- Set a decision note to accepted
- Edit `ANALYSIS_PLAN.md` except after they accept
- Load `notes/` into context except for the note you are filing
- Treat accepted Google Doc suggestions as if they still need a contribution file

After they choose, use **Update the project record** for accepted items, and set the contribution `status` to `integrated` or `archived`.
