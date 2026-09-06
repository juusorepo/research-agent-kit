---
name: review-the-manuscript
description: AI pass on the manuscript as open issues in contributions/. Use when they say Review the manuscript, AI review, or coarse-review. Not an audit of the research chain. Do not edit the paper in this run.
license: MIT
compatibility: Requires a project filesystem. An external review tool is optional.
metadata:
  version: "0.3.3"
---

# Review the manuscript (AI)

A peer-style pass on the **canonical manuscript** (or a file they name). Findings are **proposals**.

This is **not** `audit-research-chain` (plan → code → output → claim). It is **not** `audit-apa-presentation` (layout of the rendered Word/PDF). Do not repair the paper here.

## Do

1. Read the manuscript they named (default: `paths.manuscript`). Do not treat draft numbers as approved results. If the overview has an intellectual anchor (or a linked framing memo), read it before judging the title, abstract, introduction, discussion, or contribution statement.
2. Produce findings however you can (your own reading, or an external reviewer such as coarse-review if they asked for that tool). The kit does not require a particular product. If they asked for **differentiated reviews** or **Explore alternative framings**, do not produce one synthesized review: use `skills/explore-alternative-framings/SKILL.md` on the review question first, then file the distinct findings separately.
3. For tables and figures in the **paper**, also check `templates/analysis/manuscript-displays.md` (paper file if they added it, otherwise the kit). APA cosmetics (lines, italics, numbering, call-outs, notes) are `type: editorial`. A caption that overclaims, or notes that do not match the test, stay issues. This is not an audit of the research chain. Skip this list if they asked you to review a poster or a talk. If they asked to check the **rendered Word/PDF** (clipping, heading order, title page), stop and use **Audit APA presentation** instead.
4. If an intellectual anchor is written, also check intellectual continuity. These are proposals (`type: interpretation` or `issue`), not a restore of old wording and not a block on conceptual development:
   - Is the original research problem still visible?
   - Has the distinctive contribution become a generic methodological claim?
   - Have wider programme connections been removed as incidental background?
   - Has a conceptual distinction been reduced to a performance or accuracy result?
   - Have productive tensions been silently resolved through smoother wording?
   - If the framing changed, was that change deliberate and researcher-approved?
   If a finding would narrow or replace the anchor, say **researcher decision needed**. If the anchor is empty, skip this check; do not invent one.
5. Write each atomic finding as a contribution (`source: ai-review`) via **Contribute to the project**. Wording nits can be `type: editorial`. Method or claim issues stay issues; say **researcher decision needed** when the science would change.
6. Do **not** push findings into Google Docs in this skill unless they also asked to prepare a review copy. The inbox is enough.
7. If `policies/what-is-on.md` has material AI-use ticked, record one event after they have seen the inbox (or use **Update the project record**). If the box is off, do not write `ai-use/`.

## Must not

- Edit the manuscript, analysis plan, or accepted decision notes
- Restore old framing automatically, or treat the intellectual anchor as something the agent must agree with
- Mark contributions `integrated`
- Call this an independent audit or a verified result
- Invent citations

Say: findings are in the inbox. They are not part of the record until you accept them.
