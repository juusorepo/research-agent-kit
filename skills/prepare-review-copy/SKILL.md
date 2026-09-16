---
name: prepare-review-copy
description: Make a Google Docs snapshot of the Quarto manuscript for co-author comments and suggestions. Use when they say Prepare a review copy or send the paper to co-authors. Saying the phrase is enough to render Word when the snapshot is missing or stale. Word is a conversion step, not a second manuscript. The Doc is not the canonical manuscript.
license: MIT
compatibility: Requires a project filesystem. Google Docs is optional; if unavailable, say so and stop. A word provider shares a .docx instead (no comment ingest).
metadata:
  version: "0.4.0"
---

# Prepare a review copy

For co-author review. Canonical text stays in the Quarto manuscript (`paper.qmd` plus `_*.qmd` includes, or the file they actually edit). The Google Doc is a **snapshot**. Drive syncing the paper folder does **not** merge Doc edits into Quarto.

Quarto has no Google Docs output. The path is Quarto → Word → native Google Doc. Co-authors should only need the Doc. The `.docx` is a conversion intermediate, not another manuscript to maintain.

**Lookup:** this paper’s `review-copy.yml` (`paths.review_copy`); else the kit template. Drive path note: `adapters/google-drive/README.md`. Docs/Drive tools: `adapters/google-docs/README.md`.

**This file is complete.** Do not search workshop files or the toy example to learn this skill. Do not invent a Word comment workflow.

Work in the **paper** folder.

## Channel

Read `provider` in `review-copy.yml` (default `google-docs` if empty or missing).

| `provider` | What this skill does |
|---|---|
| `google-docs` | Native Google Doc in the manuscript folder. **Sync the review copy** and **Ingest review comments** apply. |
| `word` | Share a Word file (OneDrive or similar). Render if needed. Stop there. Those two skills do **not** run on this channel. |

Missing Google tools is not a reason to switch to `word`. If they asked for a Google Doc and Drive is not available from here, say so and stop.

## Google Docs

Saying **Prepare a review copy** is enough to render Word when the snapshot is missing or stale. Do not wait for a second yes.

**Windows Drive path.** If this paper’s path looks like streamed Google Drive (`G:\My Drive\...`), **stop once** and ask them to reopen from the mirrored folder (`adapters/google-drive/README.md`). Do not render from the streamed letter.

### Do

1. **Canonical source.** Note `paper.qmd` and every included `_*.qmd` (or the single file they edit). Compare times with any existing Word file and with **approved** result files the manuscript uses. A newer approved result makes a Word file stale even if the text did not change.
2. **Active round.** Read `review-copy.yml`. If `file_id` is set, do not overwrite that Google Doc. If it still has unsynced suggestions, open comments, or `synced_at` is empty, **stop once**: name the URL and the round. Offer a **new round** (old Doc kept, listed under `previous`) or wait until they **Sync the review copy** / **Ingest review comments**. If they already asked for a fresh snapshot or a new round in this chat, continue with a new Doc. You may replace a round only when that Doc was never shared and has no comments (failed conversion, retry).
3. **Word to convert.**
   - If a current `.docx` already sits in this paper’s Drive folder (`paper.docx` from a previous render, not a file in `99-archive/`): convert **that** Drive file to a native Google Doc. Do not upload a second copy of the same file.
   - Else render to a **temporary** `.docx` **outside** the synced Drive folder (this computer’s temp directory, not the manuscript folder and not `99-archive/`). From the folder that contains `layout.yml`: `quarto render` of the manuscript, with the Word output directed at that temp directory. Do not write `review-copy.docx` into the manuscript folder.
4. **Import.** Create a **native** Google Doc in the manuscript folder on Drive (Google Docs MIME type, not a Drive-hosted Word file). Title it so it does not collide with `paper.qmd` (for example `review-copy` on round 1, `review-copy-r2` on round 2). If the upload is too large, stop and ask them to import the Word file themselves, then write `file_id` / `url`.
5. **Check** the Doc before declaring it ready (below). If the check fails, do not update `review-copy.yml` to point at the new Doc; leave the previous round as current; remove the failed new Doc if you created it and it has no comments.
6. **Record** `review-copy.yml` (template fields). Fill `canonical_source`, `snapshot_id`, `file_id`, `url`, `round`, `updated_at`, and `source_docx` (`paper.docx` if reused; `temp` if you rendered). Leave `synced_at` as it was for a new round (empty). When starting a new round, copy the outgoing current round into `previous` first (keep `file_id` and `url`). Do not delete old Docs.
7. **Remove temps.** Delete the temporary `.docx` and any quarto intermediates in the temp directory. Do **not** delete `paper.docx` that was already in the manuscript folder before this run, files in `99-archive/`, or a submission Word file they named. Do not leave a second maintained manuscript.
8. Tell them what to do next (Say, below).

### Check (not Audit APA presentation)

Read the Google Doc (Drive/Docs tools if present; otherwise an export). Compare with the Quarto source:

- Headings present in the expected order
- Tables and figures still there (count vs the manuscript)
- Captions present
- References section present if `references.bib` is in use

If you cannot read the Doc, say so and do not declare it ready. This is a conversion check. Layout of a Word/PDF they would submit is **Audit APA presentation**.

## Word channel

Only when `provider: word` in `review-copy.yml`.

1. If `paper.docx` (or the Word file they named) is missing or stale, render it into the manuscript folder. Saying **Prepare a review copy** is enough to render. This is the file they share on OneDrive.
2. Write `canonical_source`, `snapshot_id`, `round`, `updated_at`, and `source_docx` on `review-copy.yml`. Leave `file_id` / `url` empty.
3. Say: Quarto remains the paper. Co-authors can edit the Word file. **Sync the review copy** and **Ingest review comments** are Google Docs only in this version — the kit will not read Word comments. Drive or OneDrive syncing the `.docx` does not merge those edits into Quarto.

Do not create a Google Doc on this channel unless they change `provider` to `google-docs`.

## Must not

- Treat the Doc or the Word file as the source of truth
- Promise a direct Quarto → Google Docs render
- Overwrite an active Google Doc, or trash a prior round
- Leave a temporary `.docx` after a successful Google Docs conversion
- Delete archival or submission Word files, or a `paper.docx` they already had
- Flatten the paper to markdown unless a Word conversion fails **and** they ask for a text snapshot
- Ingest comments in this skill (that is **Ingest review comments**)
- Run **Sync the review copy** in this skill
- Build a Word comment path
- Edit the analysis plan or approved results

Say: this is a review copy. Co-authors work in the Google Doc. Drive syncing this folder does not merge those edits into Quarto. Accept small wording in the Doc, then **Sync the review copy**. Open comments come back as contributions when they ask to ingest them.
