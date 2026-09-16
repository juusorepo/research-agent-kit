---
name: sync-review-copy
description: After wording suggestions are accepted in the Google Doc, update the canonical manuscript from that snapshot. Use when they say Sync the review copy. Do not treat this as agreeing an analysis.
license: MIT
compatibility: Requires a project filesystem. Google Docs optional; an exported Doc is enough.
metadata:
  version: "0.3.3"
---

# Sync the review copy

One merge of **accepted wording**, not one file per comma.

If `review-copy.yml` has `provider: word`, **stop**. This skill is Google Docs only. Drive or OneDrive syncing a `.docx` does not merge edits into Quarto, and Word comment ingest is not in this version.

Drive syncing the paper folder does **not** merge Google Docs edits into Quarto. This skill does.

## Do

1. Confirm they have accepted (or rejected) suggestions **in the Google Doc**. If not, stop and ask them to finish that there.
2. Get the current Doc text (or an export they attach).
3. Update the canonical manuscript so it matches the accepted snapshot. Write each section into the matching `_*.qmd` (or into `paper.qmd` if that section still lives there). Keep Quarto structure, citations, and code that reads **approved** results. Do not invent numbers. Do not copy draft or synthetic figures into Results. Do not paste a second copy of a section into the shell. Do not rebuild `paper.qmd` with an assemble script.
4. Set `synced_at` on `review-copy.yml`. Rewrite `STATUS.md` in place under the template headings (review copy merged; open comments still inbox if any). Do not append a dated section.
5. If open comments remain, say they still need **Ingest review comments** — this skill does not file them.

If the Doc would change a claim, estimand, sample, or analysis, say **researcher decision needed**, do not silently rewrite Results as if that were already agreed.

## Must not

- File a contribution for each accepted suggestion
- Treat the Doc as agreeing an analysis or approving a result
- Overwrite the manuscript from a copy that still has unreviewed suggestions unless they ask to pull a draft
- Ingest Word track changes
- Rebuild `paper.qmd` with an assemble script, or paste a second copy of a section into the shell

Say: the manuscript is updated from the accepted review copy. Open comments are a separate step.
