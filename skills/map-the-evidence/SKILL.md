---
name: map-the-evidence
description: Draft a source-grounded evidence packet for a named question. Use when they say Map the evidence. Also use when they say Create a notebook, Delete a notebook, or Search with NotebookLM (connector operations only; write a packet only if they also named a mapping question). Not an audit. Not an approved claim.
license: MIT
compatibility: Requires a project filesystem. No Python required.
metadata:
  version: "0.2.0"
---

# Map the evidence

One job. Write a **draft** evidence packet for a question they named, from sources in this paper. Retrieval may use local PDFs (`08-sources/` or `paths.sources`), a note they pasted, or an **experimental NotebookLM connector** if this paper allows it (`adapters/notebooklm/README.md`). Stop after the draft packet. This is **doing the research**, not an independent check.

A packet grounds **which source**, not **what the source computed**. Its rows are abstract-level unless a Methods or Results passage is quoted.

Follow `policies/how-to-talk.md` if present. Say *draft evidence packet*, *not in these sources*, *researcher decision needed*. Do not say verified, grounded-synthesis, or evidential status as if it were authority.

**This file is complete.**

---

## When not to use

- **Audit the research chain** or **Audit literature claims** — new chat; diagnose only
- Routine copy-edits
- Inventing a literature search this paper did not ask for

If they also want genuinely different interpretations, run **Explore alternative framings** on the same question **after** the packet exists, or in a later message. Do not fold that into this file as a second skill.

Optional. If `what-is-on.md` lists **Map the evidence** and the box is unticked, still run when they said the phrase (visibility is not availability).

---

## Read first

- The question they named
- Intellectual anchor if written
- `07-record/sources/` and `08-sources/` (layout paths `source_records` and `sources`)
- `references.bib`
- Any NotebookLM export they pasted — treat it as **locators** into this paper’s sources, not as a claim to verify elsewhere
- `adapters/notebooklm/README.md` (kit) — operations and when a connector may be used

Do not treat a research packet, NotebookLM answer, a connector reply, or provider confidence as an approved result or as what the project may claim.

### How to retrieve

1. **`local_corpus` (always available):** PDFs in `paths.sources` and pasted notes.
2. **`query_grounded`:** only if this paper allows it (`what-is-on.md` tick **or** they asked to query the notebook in this chat), `data-policy.md` does not forbid sending these files out, **and** `layout.yml` has `notebooklm.capabilities.query_grounded` set to a tool that is actually present. Use only those named tools. A host prefix around a mapped name (the mapped name, or a name ending with `__` plus that name) is the same tool. Do not guess other tool names. If the mapping is missing, ask once (they may copy a block from `adapters/notebooklm/connector-shapes.yml` into `layout.yml`), then use `local_corpus` until it is set. If the call fails, fall back to `local_corpus`. Do not stop. **Do not refuse** because the question is unpublished project framing. Sending the **question they named** (and the least extra needed to query these sources) is what they asked for. Do not paste another person’s unpublished manuscript. Do not paste this paper’s full draft unless they asked to query that text.
3. After a connector answer: map NotebookLM labels and any source id to `zotero:<item-key>` via source records. Unmatched labels or ids stay labels. Write the packet from passages you can locate in those sources (the PDF or quoted export), not from the tool’s summary alone. If a hit cannot be located, say so. Do **not** send the notebook answer to Scite, a citation index, or another model to “verify” it. That does not check the source. An independent check of manuscript claims is **Audit literature claims** in a **new** chat, against identifiable sources.
4. **`create_collection` / `remove_collection`:** only if they asked in this chat, the tick or an explicit ask allows the connector, and the mapped tools are present. Create: use their title, or propose one and wait if they did not give one. After create, write `notebook_id` and title on `layout.yml`. Delete: they must name the notebook; do not delete a notebook this paper did not record. If they asked only to create or delete a notebook and did not name a mapping question: do that, then **stop** (no packet).
5. **`research_sources`:** only if they asked in this chat (for example **Search with NotebookLM**). Use the question they named. Web unless they asked for Drive; do not search Drive if `data-policy.md` forbids sending those files out. Poll with `research_status` only if that capability is set. **Do not import** hits into the notebook. **Do not write to Zotero** and do not hunt for a Zotero connector. **Zotero is canonical:** for usable hits, stop with a **paste-ready** list (one DOI or ISBN per line; title + URL on its own line if there is no identifier). Do not invent DOIs or citation keys. In chat, tell them: open this paper’s Zotero collection (name or key from `layout.yml` if present); click the **magic wand** (Add Item by Identifier); paste the list; **Select All**, right-click, **Find Full Text**; then say **Sync the bibliography**. Then **stop** unless they also asked for a packet from sources already in this paper.

Do not call `sync_source` or `remove_source` unless they asked to add or remove sources, **or** they asked to use this paper’s notebook with files already in `paths.sources`. Asking to add `08-sources/` (or `paths.sources`) to the notebook, to fill this paper’s notebook, or to **Map the evidence** with the connector on, **is** that ask. Skip files `data-policy.md` marks restricted or confidential. Do **not** stop for a second “I authorize the upload” line.

---

## Distinctions (do not collapse)

```
not in these sources  ≠  no evidence exists  ≠  evidence of no effect
  ≠  this design cannot identify the effect
source-grounded (which source)  ≠  what the source computed
source-grounded       ≠  the inference is warranted
association reported  ≠  causal claim
```

Provider confidence (a tool is sure it found a sentence) is not scientific confidence.

---

## Write

1. If they did not name a question, ask once (default: the manuscript’s main question if there is a draft) and wait.
2. Map relevant sources. Keep source identity `zotero:<item-key>` when a record exists; otherwise use the bibliography key from `references.bib`. Do not invent keys.
3. For each included point, separate: quoted or closely located passage; what the **source authors** claim; what you extracted; study design if stated; population; what kind of inference the source itself makes; limitations. Put the statement in the claim-to-source table with `role` (`background` | `precedent` | `comparator` | `counterargument`). A source in **Sources in scope** needs a row.
4. List agreements, apparent contradictions (and whether they might be different populations or measures), and what is **not answerable from current sources**.
5. Save a draft packet under `paths.record` (default `07-record/notes/`) named `evidence-packet-<short>.md` plus a sidecar `status: provisional` (use `templates/evidence/research-packet.md` and `templates/output-metadata.yml`, with `analysis_ref` only if an agreed plan item already exists; otherwise leave it empty and say the packet is not an agreed analysis).
6. Stop. Candidate wording for the paper is not approved. Causal language must not be stronger than the sources support.

If they want an independent check of manuscript claims, tell them to open a **new chat** and say **Audit literature claims**.

---

## Must not

- Run in the same chat as an audit of this packet
- Guess connector tool names
- Call leftover NotebookLM products (studio, sharing, notes, pipelines, or importing search hits) even if those tools are visible
- Treat a notebook answer as something to verify with Scite, a citation index, or another model
- Treat NotebookLM output or a connector reply as what the project may claim
- Treat web/Drive search hits as this paper’s sources; they belong in Zotero first
- Ask them to re-authorize an upload or a notebook query after they already asked to use this paper’s notebook (tick, **Map the evidence**, add `08-sources/`, or query)
- Refuse `query_grounded` because the named question is unpublished project framing
- Send restricted or confidential files through a consumer connector
- Upgrade association to causation
- Hunt for a Zotero connector or local Zotero interface to create items
- Override the analysis plan, accepted decisions, or approved results
- Copy PDFs to another folder for NotebookLM (this paper’s `08-sources/` folder, or `paths.sources`, is the folder)
