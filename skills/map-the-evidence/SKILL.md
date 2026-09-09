---
name: map-the-evidence
description: Draft a source-grounded evidence packet for a named question. Use when they say Map the evidence. Not an audit. Not an approved claim.
license: MIT
compatibility: Requires a project filesystem. No Python required.
metadata:
  version: "0.1.0"
---

# Map the evidence

One job. Write a **draft** evidence packet for a question they named, from sources in this paper (PDFs in `sources/`, attached files, or a note they pasted from NotebookLM). Stop for acceptance. This is **doing the research**, not an independent check.

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
- `07-record/sources/` and `sources/` (layout paths)
- `references.bib`
- Any NotebookLM export they pasted — treat it as **retrieval notes**, not as approved interpretation

Do not treat a research packet, NotebookLM answer, or provider confidence as an approved result or as what the project may claim.

---

## Distinctions (do not collapse)

```
not in these sources  ≠  no evidence exists  ≠  evidence of no effect
  ≠  this design cannot identify the effect
source-grounded       ≠  the inference is warranted
association reported  ≠  causal claim
```

Provider confidence (a tool is sure it found a sentence) is not scientific confidence.

---

## Write

1. If they did not name a question, ask once (default: the manuscript’s main question if there is a draft) and wait.
2. Map relevant sources. Keep source identity `zotero:<item-key>` when a record exists; otherwise use the bibliography key from `references.bib`. Do not invent keys.
3. For each included point, separate: quoted or closely located passage; what the **source authors** claim; what you extracted; study design if stated; population; what kind of inference the source itself makes; limitations.
4. List agreements, apparent contradictions (and whether they might be different populations or measures), and what is **not answerable from current sources**.
5. Save a draft packet under `paths.record` (default `07-record/notes/`) named `evidence-packet-<short>.md` plus a sidecar `status: provisional` (use `templates/evidence/research-packet.md` and `templates/output-metadata.yml`, with `analysis_ref` only if an agreed plan item already exists; otherwise leave it empty and say the packet is not an agreed analysis).
6. Stop. Candidate wording for the paper is not approved. Causal language must not be stronger than the sources support.

If they want an independent check of manuscript claims, tell them to open a **new chat** and say **Audit literature claims**.

---

## Must not

- Run in the same chat as an audit of this packet
- Treat NotebookLM output as verified
- Upgrade association to causation
- Invent sources or citation keys
- Override the analysis plan, accepted decisions, or approved results
- Copy PDFs to another folder for NotebookLM (this paper’s `sources/` is the folder)
