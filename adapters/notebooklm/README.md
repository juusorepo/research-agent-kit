# NotebookLM (optional, experimental)

Tool setup only. Research rules live in the skills. Do **not** copy this folder into a paper.

NotebookLM is a **reading and retrieval** surface. It does not verify claims. A citation from NotebookLM is not an approved result and not a research-chain pass.

## Same folder, no extra copy

If this paper lives in a **Google Drive for Desktop** folder, NotebookLM should use **this paper’s** `sources/` directory (path `sources` in `layout.yml`). Co-authors share that folder. Do **not** copy PDFs into a second Drive library for NotebookLM.

Source identity stays `zotero:<item-key>` when a source record exists (`07-record/sources/`). NotebookLM titles or ids are labels only. Prefer exported filenames that start with the Zotero item key.

## What the skills need

| Skill | Role |
|---|---|
| Sync the bibliography | Optional PDF copies into `sources/` |
| Map the evidence | May read a pasted NotebookLM note as retrieval input, not as authority |
| Audit literature claims | Reads the manuscript and identifiable sources; does **not** trust NotebookLM or a research packet |

## Community connectors

Unofficial NotebookLM MCP servers exist. Treat them as **experimental**. Do not enable them by default. Do not put session cookies or secrets in the paper folder. If the assistant cannot reach NotebookLM, the researcher pastes an export or points at `sources/`.

Do not send restricted or confidential files to NotebookLM. Follow `policies/data-policy.md`.

## Must not

- Treat NotebookLM output as verified or as an approved interpretation
- Make the kit depend on Google
- Collapse “not in this notebook” with “no evidence exists”
- Use NotebookLM as the analysis plan or as approved results
