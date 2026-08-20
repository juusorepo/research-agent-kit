---
name: sync-review-copy
description: After wording suggestions are accepted in the Google Doc, update the canonical manuscript from that snapshot. Use when they say Sync the review copy. Do not treat this as agreeing an analysis.
license: MIT
compatibility: Requires a project filesystem. Google Docs optional; an exported Doc is enough.
metadata:
  version: "0.3.0"
---

# Sync the review copy

One merge of **accepted wording**, not one file per comma.

## Do

1. Confirm they have accepted (or rejected) suggestions **in the Google Doc**. If not, stop and ask them to finish that there.
2. Get the current Doc text (or an export they attach).
3. Update the canonical manuscript so it matches the accepted snapshot. Keep Quarto structure, citations, and code that reads **approved** results. Do not invent numbers. Do not copy draft or synthetic figures into Results.
4. Set `synced_at` on `review-copy.yml`. Refresh `STATUS.md` in one line (review copy merged; open comments still inbox if any).
5. If open comments remain, say they still need **Ingest review comments** — this skill does not file them.

If the Doc would change a claim, estimand, sample, or analysis, say **researcher decision needed**, do not silently rewrite Results as if that were already agreed.

## Must not

- File a contribution for each accepted suggestion
- Treat the Doc as agreeing an analysis or approving a result
- Overwrite the manuscript from a copy that still has unreviewed suggestions unless they ask to pull a draft
- Ingest Word track changes

Say: the manuscript is updated from the accepted review copy. Open comments are a separate step.
