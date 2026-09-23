---
name: sync-project-sources
description: Refresh this paper’s source list from a linked Zotero collection. Read-only by default. Optional PDF copies into this paper’s sources folder. Use when they say Sync the bibliography, Update project sources, Link the Zotero collection, or ask whether Zotero on this computer can be read.
license: MIT
compatibility: Requires a project filesystem. No Python required. Zotero desktop or a Zotero API is optional.
metadata:
  version: "0.1.7"
---

# Sync the bibliography

One job. Refresh this paper’s **source list** from Zotero (or from a `references.bib` they exported). Do not invent citation keys. Do not treat the source list as agreed analyses or as approved results.

Follow `policies/how-to-talk.md` if present. Say *source list*, *bibliography*, *missing full text*. Do not say corpus, registry, or hash unless they used those words.

**This file is complete.**

---

## When to use

They say **Sync the bibliography**, **Update project sources**, or **Link the Zotero collection**, or they ask whether Zotero on this computer can be read.

This is **not** **Map the evidence**. This is **not** writing to Zotero unless they explicitly ask later (not in this version).

---

## Authority

- Manuscript citations use `references.bib` next to the manuscript (Zotero Better BibTeX or another export). If that file is empty or a key is missing, ask them to export or attach it. Do not invent keys, DOIs, or years.
- Stable source identity, when a Zotero item is known, is `zotero:` plus the Zotero item key (for example `zotero:Z7K4M2`). Filenames, Drive file ids, and NotebookLM labels are not the identity.
- Records live under `layout.yml` path `source_records` (default `07-record/sources/`). Optional copies live under path `sources` (default `08-sources/`). That folder is this paper’s **materialised corpus** (sharing, Drive, NotebookLM). Zotero remains canonical. In this version, copies happen when they asked (or they already use the folder). Rebuilding `08-sources/` from the registry is later. Do not create a second Drive library. Do not rename files inside Zotero.

---

## Read first

1. `layout.yml` — `paths.sources`, `paths.source_records`, optional `zotero.collection_key`
2. `policies/data-policy.md` — do not copy or upload restricted files
3. Existing `references.bib` and any files already in `07-record/sources/`

If `zotero.collection_key` is missing, run **Find Zotero on this computer** below. If Zotero answers and they already named a collection, match it and write the key. If they have not named one, list the collection names and ask once. Wait once. If Zotero does not answer, ask for a collection name or key, or a pasted identifier list, and work from `references.bib`.

---

## Find Zotero on this computer

Desktop Zotero on this computer answers at `http://127.0.0.1:23119`. No plugin. No key. Read-only. In chat say *Zotero on this computer*. Do not say API.

Check with curl. On Windows run `curl.exe`. Elsewhere run `curl`. Do **not** use PowerShell `Invoke-WebRequest` or `Invoke-RestMethod`. Those clients fail against Zotero’s reply and look like a closed interface. A failed PowerShell request is not evidence that Zotero is off.

1. Ping: `curl.exe -sS --max-time 8 http://127.0.0.1:23119/connector/ping` — the body contains `Zotero is running`.
2. Collections: `curl.exe -sS --max-time 8 -H "Zotero-Allowed-Request: 1" "http://127.0.0.1:23119/api/users/0/collections?limit=100"` — a JSON list. Each item’s name is `data.name` and its key is `key`. If a `Link` header has `rel="next"`, follow it until the list is complete. Match the name they gave (ignore case). If two collections share a name, show both keys and ask once. Then write this into `layout.yml` (paper-owned; replace the commented stub):

```yaml
zotero:
  library: user
  collection_key: <KEY>
```

3. Items in that collection: `http://127.0.0.1:23119/api/users/0/collections/<KEY>/items?limit=100` with the same header. Follow `rel="next"` the same way.

Only if curl cannot connect (connection refused or timed out — not an HTTP error from a client that mishandles the reply): say Zotero is not answering. Then, and only then, ask them to open Zotero and turn on **Edit → Settings → Advanced → Allow other applications on this computer to communicate with Zotero**, restart Zotero if it was already open, and say **Sync the bibliography** again. Do not ask for that when curl was not tried.

---

## Do

1. List items in the linked Zotero collection after **Find Zotero on this computer**. If that check cannot connect, work from `references.bib` plus any PDFs already in `08-sources/` (or `paths.sources`), and say that Zotero on this computer was not read.
2. For each item, write or update one record `07-record/sources/zotero-<ITEMKEY>.yml` using `templates/sources/source-record.yml`. Status must distinguish: in this paper’s collection; PDF available; missing full text; not eligible to copy out (restricted).
3. Report counts in chat: items, PDFs available, missing full text. Do not pretend absence in this folder means the literature does not exist.
4. **PDF copies** (only if they asked, or they already use the sources folder for NotebookLM): copy the Zotero attachment into `paths.sources` (default `08-sources/`) with a name starting with the item key:

   `<itemkey>__<first-author>__<year>__<short-title>.pdf`

   Leave Zotero attachments untouched. Skip the copy when `data_policy` forbids sending the file out of this machine, or the source is marked restricted. Never upload to NotebookLM from this skill. Do not watch Zotero and push every new PDF into a notebook. Automatic corpus rebuild is later.
   5. If they want those copies **in a NotebookLM notebook** as well: that is `sync_source` in `adapters/notebooklm/README.md`. Asking to add `08-sources/` to this paper’s notebook, or to use the connector with that folder, **is** that ask. Do not stop for a second authorization. Skip restricted files. If they asked to **create** that notebook first, that is `create_collection` (same conditions).
6. If they want items **added** to Zotero (including after **Search with NotebookLM**): do **not** write to Zotero and do not hunt for a Zotero connector. Put a **paste-ready** list in chat (one DOI or ISBN per line; title + URL if there is no identifier). Tell them: open this paper’s Zotero collection (name or key from `layout.yml` if present); click the **magic wand** (Add Item by Identifier); paste; **Select All**, right-click, **Find Full Text**; then say **Sync the bibliography**. Do not invent DOIs or citation keys. Usable search hits are not project sources until they are in Zotero.

Do not crawl Zotero’s disk storage or WebDAV. Use Zotero’s own interface or API if present.

---

## Must not

- Invent bibliography records or citation keys
- Hunt for a connector in order to create items; give a paste-ready identifier list instead
- Treat a failed PowerShell `Invoke-WebRequest` or `Invoke-RestMethod` as Zotero being off
- Ask them to enable “Allow other applications on this computer to communicate with Zotero” unless the curl check cannot connect
- Treat NotebookLM search hits, Drive file ids, or notebook labels as source identity instead of `zotero:<item-key>`
- Copy a second corpus to another Drive folder
- Ask for a second yes before adding non-restricted files from `paths.sources` when they already asked to use this paper’s notebook
- Watch Zotero and push new PDFs into a notebook automatically
- Override the analysis plan, accepted decisions, or approved results
- Open row-level real data
