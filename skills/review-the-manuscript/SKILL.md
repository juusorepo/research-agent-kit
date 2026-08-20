---
name: review-the-manuscript
description: AI pass on the manuscript as open issues in contributions/. Use when they say Review the manuscript, AI review, or coarse-review. Not an audit of the research chain. Do not edit the paper in this run.
license: MIT
compatibility: Requires a project filesystem. An external review tool is optional.
metadata:
  version: "0.3.0"
---

# Review the manuscript (AI)

A peer-style pass on the **canonical manuscript** (or a file they name). Findings are **proposals**.

This is **not** `audit-research-chain` (plan → code → output → claim). Do not repair the paper here.

## Do

1. Read the manuscript they named (default: `paths.manuscript`). Do not treat draft numbers as approved results.
2. Produce findings however you can (your own reading, or an external reviewer such as coarse-review if they asked for that tool). The kit does not require a particular product.
3. Write each atomic finding as a contribution (`source: ai-review`) via **Contribute to the project**. Wording nits can be `type: editorial`. Method or claim issues stay issues; say **researcher decision needed** when the science would change.
4. Do **not** push findings into Google Docs in this skill unless they also asked to prepare a review copy. The inbox is enough.
5. If `policies/what-is-on.md` has material AI-use ticked, record one event after they have seen the inbox (or use **Update the project record**). If the box is off, do not write `ai-use/`.

## Must not

- Edit the manuscript, analysis plan, or accepted decision notes
- Mark contributions `integrated`
- Call this an independent audit or a verified result
- Invent citations

Say: findings are in the inbox. They are not part of the record until you accept them.
