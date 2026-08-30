---
name: prepare-review-copy
description: Make a Google Docs snapshot of the manuscript for co-author comments and suggestions. Use when they say Prepare a review copy or send the paper to co-authors. Upload a Word snapshot they already rendered; do not knit unless they ask. The Doc is not the canonical manuscript.
license: MIT
compatibility: Requires a project filesystem. Google Docs is optional; if unavailable, say so and stop.
metadata:
  version: "0.3.1"
---

# Prepare a review copy

For co-author review. Canonical text stays in the manuscript folder (`layout.yml` `paths.manuscript`). The Doc is a **snapshot**. You do not rebuild the paper in this run.

Work in the **paper** folder. If Google Drive is not available from here, say so and stop. Do not invent a Word comment workflow.

## Do

1. Look in the manuscript folder for a named Word snapshot. Default names: `review-copy.docx`, or `paper.docx` if that is what `quarto render` writes. Compare its time with the manuscript file (`paper.qmd` or the file they actually edit).
2. If an **approved** result file the manuscript uses is newer than the Word file, treat the Word file as stale even if they did not edit the text. Numbers live in those result files.
3. If the Word file exists and is newer than the manuscript (and not stale from step 2): **do not render**. Upload that Word file as a Google Doc. If the upload is too large for this chat, stop and ask them to put the Word file in Drive themselves (or to share the Doc URL), then write `file_id` / `url` / `round` / `updated_at`. Leave `synced_at`. Do **not** flatten the paper to plain text unless they ask.
4. If the Word file is missing or older: **do not knit a workaround**. Tell them to render from the paper folder (`quarto render` of the manuscript, as in the manuscript README) and ask again. Knit only if they say to render it in this run.
5. Write or update `review-copy.yml` in the manuscript folder (or `paths.review_copy` if set). Use the kit template. Fill `file_id`, `url`, `round`, `updated_at`. Leave `synced_at` as it was.
6. Tell them: co-authors should **suggest** small wording in the Doc and **comment** only when something is an issue. Gemini in Docs, if they use it, is still on this snapshot.

Do not add a parallel markdown review path unless a Word upload fails **and** they ask for a text snapshot. Markdown is harder for co-authors and loses the figure.

## Must not

- Treat the Doc as the source of truth
- Knit or flatten the paper unless they asked (step 3–4)
- Edit the analysis plan or approved results
- Ingest comments in this skill (that is **Ingest review comments**)
- Build a Word comment path

Say: this is a review copy. Accept small wording in the Google Doc. Open comments come back as contributions when they ask to ingest them.
