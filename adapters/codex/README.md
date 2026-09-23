# Codex

Tool setup only. Research rules live in `AGENTS.md` and the skills. Do **not** copy this folder into a paper.

Codex reads `AGENTS.md`. After a paper exists, open Codex in **that paper folder**. Do not add a Codex-branded instruction file.

## Start (paper folder first)

Create an empty paper folder (Drive mirrored path on Windows). Open Codex in that folder. Paste **Start the project** with the path to your **local kit** — see `START.md` **2b**. Do not fetch GitHub if the kit is on this computer.

The empty folder has no `AGENTS.md` yet. The paste must name the kit so Codex can read `skills/start-research-project/SKILL.md` from there. After start, this paper has `AGENTS.md` and generated kit files. Later chats in this folder do not need the kit open. The folder map still records the local kit path for when it is readable (Cursor, or **Adjust this project to the new kit version**).

GitHub start (`START.md` **2c**) is only when there is no local kit.

On Windows Drive papers, open the mirrored local path, not `G:\My Drive` — see `adapters/google-drive/`.

## Zotero on this computer

Do not copy this note into the paper. **Can you read Zotero**, **Link the Zotero collection**, and **Sync the bibliography** follow `skills/sync-project-sources/SKILL.md`. A self-contained paper gets that skill under `.rak/runtime/skills/`. The check is `curl.exe` against `http://127.0.0.1:23119`. PowerShell web requests fail against Zotero and are not evidence that it is off.
