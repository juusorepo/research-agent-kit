---
name: ingest-review-comments
description: Turn leftover open Google Doc comments into contribution files. Use when they say Ingest review comments. Do not file accepted suggestions; those stay in the Doc until Sync the review copy.
license: MIT
compatibility: Requires a project filesystem. Google Docs optional; a pasted comment list is enough.
metadata:
  version: "0.3.0"
---

# Ingest review comments

Bring **open issues** from the review copy into `contributions/`. Then they use **Consolidate contributions**.

## Do

1. Read `review-copy.yml` (manuscript folder or `paths.review_copy`).
2. Get open **comment threads** from the Google Doc if you can. If not, ask them to paste the open comments (or attach an export) and wait.
3. **Skip** suggestions (deferred edits) and **resolved** comments. Those are not contributions. Wording is accepted in the Doc, then **Sync the review copy**.
4. For each remaining open thread, write one `C-NNN-*.md` via **Contribute to the project**. Set `source: docs-comment`, quote the span in `excerpt`, set `external_id` to the comment id. Skip a thread if that `external_id` already exists.
5. Classify roughly: editorial wording still open as a question vs method/claim (`researcher decision needed` if the science would change).

## Must not

- Edit the manuscript, overview, or analysis plan
- Duplicate threads
- Mark contributions `integrated`
- Ingest Word comments

Say: these are in the inbox. Small edits already accepted in the Doc are not listed here — sync those separately.
