---
name: prepare-review-copy
description: Make a Google Docs snapshot of the manuscript for co-author comments and suggestions. Use when they say Prepare a review copy or send the paper to co-authors. The Doc is not the canonical manuscript.
license: MIT
compatibility: Requires a project filesystem. Google Docs is optional; if unavailable, say so and stop.
metadata:
  version: "0.3.0"
---

# Prepare a review copy

For co-author review. Canonical text stays in the manuscript folder (`layout.yml` `paths.manuscript`).

## Do

1. Read the canonical manuscript (Quarto or other format in that folder).
2. Make a **Google Doc** snapshot (upload/export). If you cannot reach Google, say so and stop. Do not invent a Word review workflow.
3. Write or update `review-copy.yml` in the manuscript folder (or `paths.review_copy` if set). Use the kit template. Fill `file_id`, `url`, `round`, `updated_at`. Leave `synced_at` as it was.
4. Tell them: co-authors should **suggest** small wording in the Doc and **comment** only when something is an issue. Gemini in Docs, if they use it, is still on this snapshot.

## Must not

- Treat the Doc as the source of truth
- Edit the analysis plan or approved results
- Ingest comments in this skill (that is **Ingest review comments**)
- Build a Word comment path

Say: this is a review copy. Accept small wording in the Google Doc. Open comments come back as contributions when they ask to ingest them.
