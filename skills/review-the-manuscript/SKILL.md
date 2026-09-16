---
name: review-the-manuscript
description: AI pass on the manuscript as open issues in contributions/. Use when they say Review the manuscript, AI review, coarse-review, external review, or Scan for generic prose. Not an audit of the research chain. Do not edit the paper in this run.
license: MIT
compatibility: Requires a project filesystem. An external review service is optional.
metadata:
  version: "0.4.2"
---

# Review the manuscript (AI)

A peer-style pass on the **canonical manuscript** (or a file they name). Findings are **proposals**.

This is **not** `audit-research-chain` (plan → code → output → claim). It is **not** `audit-apa-presentation` (layout of the rendered Word/PDF). Do not repair the paper here.

**Lookup:** this paper’s `policies/` and `.agents/skills/` if present; else `.rak/runtime/` (including this skill’s `references/`); else the kit. Setup notes: `adapters/review-service/README.md` when the kit is readable.

## Do

1. Read the manuscript they named (default: `paths.manuscript`). If `paper.qmd` has `{{< include >}}` shortcodes, read those `_*.qmd` files too — the shell alone is not the paper. Locate findings in the include file (heading; line number if that file has stable lines). Do not treat draft numbers as approved results. If the overview has an intellectual anchor (or a linked framing memo), read it before judging the title, abstract, introduction, discussion, or contribution statement. Before filing findings, also read the open task list and open contributions. If this is a prose scan and **Author voice** is ticked, read the voice note (`paths.author_voice` or `07-record/author-voice.md`) so you do not flag a habit it protects.
2. Produce findings:
   - If they said **Scan for generic prose** or **Plain-language review**, do the focused editorial pass in step 3. **Never** call a review service.
   - Else if this paper allows an **external review service** (below), use that service for the peer-style pass. Do not run a second full peer-style review yourself. Still do steps 4–5 (kit checks the service does not know).
   - Else read the manuscript yourself. If they asked for **differentiated reviews** or **Explore alternative framings**, do not produce one synthesized review: use `skills/explore-alternative-framings/SKILL.md` on the review question first, then file the distinct findings separately.
3. If they say **Scan for generic prose** or **Plain-language review**, do a focused editorial pass rather than a full peer-style review. Flag only candidate passages that have one of these concrete problems:
   - vague attribution without an identifiable source (for example, “studies show” or “experts agree”);
   - unsupported importance or contribution puffery;
   - generic filler that could describe almost any study;
   - repetitive, formulaic rhetorical setups or endings (including the same framing restated in the abstract and the introduction, or later in the body — not only repetition inside one section); or
   - a sentence whose abstraction or tangled structure prevents a clear reading.
   Quote the passage, name the pattern, give a short rationale, and give a location they can find again (include filename if used; section heading; line number if that file has stable lines). Do not score the manuscript or infer whether a person or AI wrote it. Do not flag quotations, necessary methods language, tables or figure notes, warranted uncertainty, disciplinary terms, genuine conceptual contrasts, or properly cited claims merely because they are formal or abstract. A passage is a candidate for the researcher to judge, not a defect established by the scan.
   In chat, say this scan does not check literature support, numerical accuracy, or evidential correctness. Also name a few passages that should **stay**, with locations — not only what is wrong.
   Do not edit the manuscript. If **Propose wording in prose scans** is ticked, a finding may include a `suggested_replacement` (proposal only; never applied in this run). If that box is off, do not propose replacement prose. If **Author voice** is ticked and they want flagged passages rewritten into the paper, that is **Edit this in my voice** in a **later** message. If they asked to scan and to draft or edit in their voice in the same message, do this scan only, then stop.
4. Unless this is a focused prose scan, for tables and figures in the **paper**, also check `templates/analysis/manuscript-displays.md` (paper file if they added it, otherwise `.rak/runtime/templates/`, otherwise the kit). APA cosmetics (lines, italics, numbering, call-outs, notes) are `type: editorial`. A caption that overclaims, or notes that do not match the test, stay issues. This is not an audit of the research chain. Skip this list if they asked you to review a poster or a talk. If they asked to check the **rendered Word/PDF** (clipping, heading order, title page), stop and use **Audit APA presentation** instead.
5. Unless this is a focused prose scan, if an intellectual anchor is written, also check intellectual continuity. These are proposals (`type: interpretation` or `issue`), not a restore of old wording and not a block on conceptual development:
   - Is the original research problem still visible?
   - Has the distinctive contribution become a generic methodological claim?
   - Have wider programme connections been removed as incidental background?
   - Has a conceptual distinction been reduced to a performance or accuracy result?
   - Have productive tensions been silently resolved through smoother wording?
   - If the framing changed, was that change deliberate and researcher-approved?
   If a finding would narrow or replace the anchor, say **researcher decision needed**. If the anchor is empty, skip this check; do not invent one.
6. Write each atomic finding as a contribution (`source: ai-review`) via **Contribute to the project**. Wording nits can be `type: editorial`. Method or claim issues stay issues; say **researcher decision needed** when the science would change. If a review service returned comments, file **one contribution per comment** (and one for the overall recommendation if present). Do not dump the whole report as a single inbox item. Skip a comment whose `external_id` already exists.
   For a **prose scan**, assign the `C-NNN` ids first, then on each file set `severity` (`minor` | `moderate` | `major`) and `fix_scope` (`word` | `sentence` | `paragraph` | `section`). Put interacting findings in `related` (other `C-NNN`). If an **open** task already covers the same work, still file the finding, put that `T-NNN` in `related`, and set suggested home to that existing task — it needs no new decision. If **Propose wording in prose scans** is ticked, add `suggested_replacement` (if **Author voice** is also ticked, follow the voice note). Leave `suggested_replacement` off when the box is off.
7. Do **not** push findings into Google Docs in this skill unless they also asked to prepare a review copy. The inbox is enough.
8. If `policies/what-is-on.md` has material AI-use ticked, record one event after they have seen the inbox (or use **Update the project record**). If the box is off, do not write `ai-use/`.

## External review service

Optional. The kit does not require a particular product. Coarse is one service that can implement the operations; any host that does the same is fine.

**When it may run** (all of these):

- This is a full peer-style review, not a prose scan.
- `data-policy.md` does not forbid sending this file out, and the file is not restricted or confidential.
- **Either** this paper’s `policies/what-is-on.md` has **External manuscript review** ticked, **or** they asked in this chat for an external review / **coarse-review** / this paper’s review service. Do not ask for a second authorization.
- `layout.yml` has `review_service.base_url`.

If they asked for the service and `base_url` is missing: **stop once**, ask them to set `review_service` in the folder map (channel `local_api` or `hosted_api`, and the URL). Until then, review by reading the manuscript yourself.

If the tick is off and they did not ask for an external review: do not call the service.

**How to call.** Use whatever HTTP this environment already has (a request tool, or a local command that sends JSON). Do not require a named assistant product or a vendor command line. Do not invent extra operations.

Read `review_service.capabilities` if set; otherwise the defaults in this skill’s `references/review-service-contract.yml` (or `adapters/review-service/api-contract.yml` if that is readable):

| Operation | Default |
|---|---|
| `review_start` | `POST /reviews` |
| `review_status` | `GET /reviews/{id}` |
| `review_result` | `GET /reviews/{id}/result` |

Join `base_url` and the path. Replace `{id}` with the `review_id`. If `token_env` is set, send `Authorization: Bearer` with that environment variable’s value. Never echo the token. Never write it into the paper.

`review_start` JSON:

- `channel`: `local_api` or `hosted_api` from the folder map
- `filename`, `media_type`
- `local_api`: `path` (absolute path the service can read). Do not upload unless the service rejects path.
- `hosted_api`: `content_base64` (the named manuscript). Say in chat that the file is sent off this machine.

If `paper.qmd` uses includes, a service that reads one file will miss the sections. Prefer the rendered Word when it is current. If the service needs a text/qmd file, write a temporary concatenation **outside** the manuscript folder, send that, and delete it after `review_start` accepts. Never leave an assembled copy next to `paper.qmd`.

`review_start` must return a `review_id` before the review finishes. Poll `review_status` until `complete` or `failed`. Wait about 30 seconds between polls. If a wait is cut short, poll again with the **same** `review_id`. Do not start a second review of the same file in this run unless they asked.

When `complete`, call `review_result`. Write `markdown` to `paths.contributions` / `reviews/<review_id>.md` (create `reviews/` if needed). Chat: the recommendation, how many comments, and that findings are in the inbox — not the full report.

File comments with `external_id: review-service:<review_id>:<comment id>`. `type: editorial` when severity is editorial; otherwise `issue` (or `interpretation` when it is a framing point). If there are no structured comments, split the markdown into atomic findings as best you can; still save the full file.

If the service **fails** or HTTP is unavailable: say so, then review by reading the manuscript yourself. Do not stop the skill.

## Must not

- Edit the manuscript, analysis plan, or accepted decision notes
- Write an assembled copy of the paper into the manuscript folder
- Restore old framing automatically, or treat the intellectual anchor as something the agent must agree with
- Mark contributions `integrated`
- Call this an independent audit or a verified result
- Invent citations
- Send restricted or confidential files to a review service
- Pin this skill to one vendor command line or one assistant product

Say: findings are in the inbox. They are not part of the record until you accept them.
