---
name: sync-project-sources
description: Refresh this paper’s source list from a linked Zotero collection. Read-only by default. Optional PDF copies into this paper’s sources folder. Use when they say Sync the bibliography or Update project sources.
license: MIT
compatibility: Requires a project filesystem. No Python required. Zotero desktop or a Zotero API is optional.
metadata:
  version: "0.1.1"
---

# Sync the bibliography

One job. Refresh this paper’s **source list** from Zotero (or from a `references.bib` they exported). Do not invent citation keys. Do not treat the source list as agreed analyses or as approved results.

Follow `policies/how-to-talk.md` if present. Say *source list*, *bibliography*, *missing full text*. Do not say corpus, registry, or hash unless they used those words.

**This file is complete.**

---

## When to use

They say **Sync the bibliography** or **Update project sources**.

This is **not** **Map the evidence**. This is **not** writing to Zotero unless they explicitly ask later (not in this version).

---

## Authority

- Manuscript citations use `references.bib` next to the manuscript (Zotero Better BibTeX or another export). If that file is empty or a key is missing, ask them to export or attach it. Do not invent keys, DOIs, or years.
- Stable source identity, when a Zotero item is known, is `zotero:` plus the Zotero item key (for example `zotero:Z7K4M2`). Filenames, Drive file ids, and NotebookLM labels are not the identity.
- Records live under `layout.yml` path `source_records` (default `07-record/sources/`). Optional PDF copies live under path `sources` (default `08-sources/`). Those PDFs are copies for sharing and NotebookLM in **this** Google Drive folder. Do not create a second Drive library. Do not rename files inside Zotero.

---

## Read first

1. `layout.yml` — `paths.sources`, `paths.source_records`, optional `zotero.collection_key`
2. `policies/data-policy.md` — do not copy or upload restricted files
3. Existing `references.bib` and any files already in `07-record/sources/`

If `zotero.collection_key` is missing, ask them for the collection name or key (or to paste an identifier list). Wait once.

---

## Do

1. List items in the linked Zotero collection if a Zotero connector or local Zotero is available. If not, work from `references.bib` plus any PDFs already in `08-sources/` (or `paths.sources`), and say that the live Zotero collection was not read.
2. For each item, write or update one record `07-record/sources/zotero-<ITEMKEY>.yml` using `templates/sources/source-record.yml`. Status must distinguish: in this paper’s collection; PDF available; missing full text; not eligible to copy out (restricted).
3. Report counts in chat: items, PDFs available, missing full text. Do not pretend absence in this folder means the literature does not exist.
4. **PDF copies** (only if they asked, or they already use the sources folder for NotebookLM): copy the Zotero attachment into `paths.sources` (default `08-sources/`) with a name starting with the item key:

   `<itemkey>__<first-author>__<year>__<short-title>.pdf`

   Leave Zotero attachments untouched. Skip the copy when `data_policy` forbids sending the file out of this machine, or the source is marked restricted. Never upload to NotebookLM from this skill.
5. If they want items **added** to Zotero: output a clean DOI/ISBN list for them to paste into Zotero’s Add by Identifier. Do not create Zotero items in this version.

Do not crawl Zotero’s disk storage or WebDAV. Use Zotero’s own interface or API if present.

---

## Must not

- Invent bibliography records or citation keys
- Write to Zotero
- Treat the sources folder as canonical instead of Zotero
- Copy a second corpus to another Drive folder
- Upload files to NotebookLM
- Override the analysis plan, accepted decisions, or approved results
- Open row-level real data
