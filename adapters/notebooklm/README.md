# NotebookLM (optional, experimental)

Tool setup only. Research rules live in the skills. Do **not** copy this folder into a paper.

NotebookLM is a **reading and retrieval** surface. It does not verify claims. A citation from NotebookLM is not an approved result and not a research-chain pass.

The kit talks to NotebookLM only through the **operations** below. That contract is the product. Channels behind it can change. It does **not** depend on one named community server.

## Now vs later

**Now (this version):** the capability contract plus **local files** and an **optional consumer connector**. Setting up the notebook and its sources is still **manual** (temporary MVP). `08-sources/` may be filled by **Sync the bibliography** or by files they add. Do not treat that manual step as the intended end state.

**Later:** the same contract plus an **official API** when worthwhile. Then: automated corpus materialisation and notebook source lifecycle (create/update/remove sources, stable ids).

Deferred (planned, not “unnecessary”):

- Zotero → this paper’s source registry (`07-record/sources/`)
- Reproducible materialisation of `08-sources/` from Zotero / project inclusion
- Notebook source lifecycle automation
- Stable mapping of NotebookLM source ids back to `zotero:…`
- Official Enterprise adapter

Do not build a large Python provider tree until those earn their keep on a real paper.

## Same folder, no extra copy

`08-sources/` (path `sources` in `layout.yml`) is this paper’s **materialised project corpus** — copies for sharing, Drive, and NotebookLM. **Zotero remains canonical.** In this version the folder may still be filled by hand or by an optional copy step; later it should be rebuildable from the source registry. Do **not** copy PDFs into a second Drive library for NotebookLM.

Source identity stays `zotero:<item-key>` when a record exists (`07-record/sources/`). NotebookLM titles, labels, and (later) official source ids are representations (`representations.notebooklm` on the source record). Prefer exported filenames that start with the Zotero item key.

## What RAK knows (operations)

Skills request **only** these. Do not invent extra kit operations from a vendor’s 30-tool catalogue.

| Operation | For |
|---|---|
| `list_collections` | List notebooks |
| `list_sources` | What is in the selected notebook |
| `query_grounded` | Ask a question; keep source locators |
| `sync_source` | Add or update one source **only if they asked in this chat** (later: automated lifecycle) |
| `remove_source` | Remove one source **only if they asked in this chat** (later: automated lifecycle) |

## Explicit mapping (do not guess)

Do **not** map whatever tools happen to be installed onto these operations. Two unofficial connectors can use the same English words with different meaning.

Read `notebooklm.capabilities` in this paper’s `layout.yml` (see the commented block in the paper skeleton). Those values are the **tool names** to call. If the tick is on but `capabilities` is missing or a named tool is not present: **stop once**, ask them to fill the mapping (or pick a listed shape in `adapters/notebooklm/connector-shapes.yml`), then use `local_corpus` until they have. Do not invent names.

## Channels

| Channel | When |
|---|---|
| `local_corpus` | Always the fallback. Read PDFs in `08-sources/` (or `paths.sources`) and any note they pasted. |
| `consumer_mcp` | Optional. They added a NotebookLM connector in Cursor or Claude Code **and** listed its tool names under `notebooklm.capabilities`. Windows is fine. Experimental. |
| `enterprise_api` | Later / institutional. Official authentication, PDF upload, stable source ids. Not wired in this version. |

Default for a paper: `local_corpus`. Use `consumer_mcp` only when the connector is available, **capabilities are set**, **and** this paper allows it (tick, or they asked to query the notebook in this chat).

Classification when `consumer_mcp` is in use:

- provider: notebooklm
- channel: consumer_mcp
- stability: experimental
- data_sensitivity: **non-sensitive only**

Consumer connectors typically use undocumented Google endpoints and a browser session. They can break when Google changes the product. The official Notebook / Gemini Enterprise API already has a similar resource model (notebooks, sources, ids); this kit’s operations match that model on purpose. Do **not** pin the kit to one GitHub MCP package. If the connector is missing or fails, fall back to `local_corpus`. Do not stop the skill.

## When the assistant may query

Read this paper’s `policies/what-is-on.md`, `policies/data-policy.md`, and `layout.yml` (`notebooklm` if present).

- **Restricted or confidential files:** do not send to NotebookLM. Do not call `sync_source`. Use `local_corpus` only if the files are allowed on this machine.
- **Optional tick** “Experimental NotebookLM connector”: if ticked, capabilities are set, and tools exist, **Map the evidence** may call `query_grounded`.
- If the tick is off: use `local_corpus`, unless they explicitly asked to query the notebook in this chat, capabilities are set, and the sources are not restricted.
- After a grounded answer: map NotebookLM labels **and** any source id to `zotero:<item-key>` via source records. If a label or id does not match, say so. Do not invent a Zotero key. Stable id mapping is incomplete until records store it.
- A grounded answer is **retrieval**. Write it into the draft packet as retrieval notes plus passages you can locate. It is not an approved interpretation.

**Sync the bibliography** still does not upload. Copies land in `08-sources/`. Adding those files to a notebook is `sync_source`, and only when they asked — until lifecycle automation exists.

## What the skills need

| Skill | Role |
|---|---|
| Sync the bibliography | Source registry + optional copies into `08-sources/`. No notebook upload unless they asked (`sync_source`) |
| Map the evidence | `query_grounded` only via explicit capabilities; else paste or local PDFs. Draft packet; not authority |
| Audit literature claims | Reads the manuscript and identifiable sources; does **not** trust NotebookLM, a connector, or a research packet |

## Must not

- Treat NotebookLM output as verified or as an approved interpretation
- Guess connector tool names
- Make the kit depend on Google or on one community connector
- Collapse “not in this notebook” with “no evidence exists”
- Use NotebookLM as the analysis plan or as approved results
- Send restricted or confidential files through a consumer connector
- Store session cookies or secrets in the paper folder
- Treat `08-sources/` as more canonical than Zotero
