# Google Docs review copy (optional)

Tool setup only. Research rules live in the skills. Do **not** copy this folder into a paper.

The review copy is a **snapshot**. The canonical manuscript is `paths.manuscript` in `layout.yml` (Quarto: `paper.qmd` plus `_*.qmd` files). Drive syncing the folder does **not** merge Google Docs edits into Quarto. **Sync the review copy** does that. Open comments: **Ingest review comments**.

Quarto has no Google Docs output. **Prepare a review copy** converts via Word, then imports a **native** Google Doc into the manuscript folder. The `.docx` is a conversion step, not a second manuscript. Saying the phrase is enough to render when the snapshot is missing or stale.

## What the skills need

| Skill | Needs from the Doc |
|---|---|
| Prepare a review copy | Convert current Word (reuse a Drive `.docx` if it is current; otherwise render outside Drive) to a native Google Doc; store `canonical_source`, `snapshot_id`, `file_id`, `url`, `round` in `review-copy.yml`. Do not overwrite an active round. |
| Ingest review comments | List **open comment threads**. Do not turn suggestions (deferred edits) into contributions. Google Docs only. |
| Sync the review copy | After suggestions are accepted in the Doc, export the text and update the manuscript. Google Docs only. |

`review-copy.yml` `provider: word` shares a `.docx` (OneDrive). That channel does not get Sync or Ingest.

Prefer **Google’s** Docs and Drive remote MCP servers (same endpoints for Claude, Cursor, Antigravity, and other MCP clients), or the Google Docs / Drive interfaces they wrap. Do not require a Cursor-only plugin.

Docs MCP: `https://docsmcp.googleapis.com/mcp/v1`  
Drive MCP: `https://drivemcp.googleapis.com/mcp/v1`  

See Google’s guide: [Configure the Google Workspace MCP servers](https://developers.google.com/workspace/guides/configure-mcp-servers).

Comments and suggestions on the document itself are in the Docs developer preview (`insertComment`, replies, accept/reject suggestion). Use that when the assistant has it. If the assistant cannot reach Google, the skills fall back to a pasted comment list or an exported file.

Upload Word with conversion to a Google Doc (do not set “keep as Word”). Put the Doc in the manuscript folder. A new round is a new Doc; keep the old one.

## Must not

- Treat the Doc as the analysis plan or as approved results
- File a contribution for each accepted suggestion
- Ingest Word track changes (not in this version)
- Overwrite an active review copy
- Put OAuth secrets in the paper folder
