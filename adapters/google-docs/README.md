# Google Docs review copy (optional)

Tool setup only. Research rules live in the skills. Do **not** copy this folder into a paper.

The review copy is a **snapshot**. The canonical manuscript is `paths.manuscript` in `layout.yml`.

## What the skills need

| Skill | Needs from the Doc |
|---|---|
| Prepare a review copy | Create or upload a Google Doc from the manuscript; store `file_id` / url in `review-copy.yml` |
| Ingest review comments | List **open comment threads**. Do not turn suggestions (deferred edits) into contributions |
| Sync the review copy | After suggestions are accepted in the Doc, export the text and update the manuscript |

Prefer **Google’s** Docs and Drive remote MCP servers (same endpoints for Claude, Cursor, Antigravity, and other MCP clients), or the Google Docs / Drive interfaces they wrap. Do not require a Cursor-only plugin.

Docs MCP: `https://docsmcp.googleapis.com/mcp/v1`  
Drive MCP: `https://drivemcp.googleapis.com/mcp/v1`  

See Google’s guide: [Configure the Google Workspace MCP servers](https://developers.google.com/workspace/guides/configure-mcp-servers).

Comments and suggestions on the document itself are in the Docs developer preview (`insertComment`, replies, accept/reject suggestion). Use that when the assistant has it. If the assistant cannot reach Google, the skills fall back to a pasted comment list or an exported file.

## Must not

- Treat the Doc as the analysis plan or as approved results
- File a contribution for each accepted suggestion
- Ingest Word track changes (not in this version)
- Put OAuth secrets in the paper folder
