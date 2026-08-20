---
name: consolidate-contributions
description: For the lead researcher. Review pending contributions and recommend where each should go. Use when they say Consolidate contributions. Do not silently change the analysis plan or accept decisions.
license: MIT
compatibility: Requires a project filesystem.
metadata:
  version: "0.3.0"
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

If the science would change, say **researcher decision needed**. Editorial nits are not research decisions.

## Must not

- Automatically make scientifically consequential decisions
- Set a decision note to accepted
- Edit `ANALYSIS_PLAN.md` except after they accept
- Load `notes/` into context except for the note you are filing
- Treat accepted Google Doc suggestions as if they still need a contribution file

After they choose, use **Update the project record** for accepted items, and set the contribution `status` to `integrated` or `archived`.
