# Google Drive for Desktop (Windows)

Tool setup only. Research rules live in the skills. Do **not** copy this folder into a paper.

Research papers may live in Google Drive so that source folders can be connected to NotebookLM and manuscript files can be shared with co-authors. On **Windows**, open the paper from a **real local folder**, not from Drive’s streamed letter.

This is not a Codex-only issue. Cursor, Claude Code, Codex, and similar tools start local programs in the project folder. Drive’s streamed path is a virtual drive. Those tools may be unable to start processes there even when the folder is marked “Available offline.”

## Do not open

Do not use the streamed virtual drive as the project folder, for example:

`G:\My Drive\paper-name`

“Available offline” only caches streamed files. The path remains a virtual drive.

Observed failures (Codex on Windows; treat the same class of error in Cursor or Claude as this setup problem until shown otherwise):

- `helper_unknown_error: setup refresh had errors`
- `CreateProcessWithLogonW failed: 267`

## Recommended setup

1. Open Google Drive for desktop.
2. Go to **Settings → Preferences → Folders from Drive**.
3. Under **My Drive syncing options**, select **Mirror files**.
4. Wait until Google Drive reports **Up to date**.
5. Open the kit and the paper from the real local mirrored path, for example:

   `C:\Users\<username>\My Drive\paper-name`

6. Do not select the `G:\My Drive` shortcut as the project folder.

The paper stays in Google Drive. Sharing, co-author access, and source-folder use are unchanged. Mirroring needs enough local disk space for the synchronized My Drive contents.

A Google Docs **review copy** still uses a Word conversion (Quarto has no Docs output). Render that Word file **outside** the synced Drive folder, then import a native Google Doc into the manuscript folder. Do not treat a Drive-hosted `.docx` as the co-author paper. Drive syncing this folder does not merge Doc edits into Quarto — that is **Sync the review copy**.

## If an assistant cannot start programs here

1. Look at the folder path.
2. If it is `G:\My Drive\...` (or another Drive letter for streamed My Drive), switch to **Mirror files** and reopen from `C:\Users\<username>\My Drive\...`.
3. Then try the same work again.

A simple comparison (Codex; other tools show the same pattern if they can run a command in the folder):

- A command that only prints `ok` succeeds from a local `C:\...` folder.
- The same command fails from the streamed `G:\My Drive\...` folder.

On Codex, `codex doctor` can also flag the environment. Do not tell a Cursor or Claude session to run that command.

## Must not

- Treat “Available offline” as a local disk
- Open `G:\My Drive` as the project folder on Windows
- Copy the paper out of Drive to dodge this — mirroring keeps the same shared folder
