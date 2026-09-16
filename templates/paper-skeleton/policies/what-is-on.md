# What the assistant does in this project

You may edit this file. The assistant should follow it.

## Always on

- Shared research record (overview, analysis plan, status, tasks)
- Collaborator inbox stays a proposal until you accept it
- Data-use rules (do not open individual-level data unless this project allows it)
- Do not invent numbers or treat draft results as approved
- Important methodological choices need your decision
- Distinctive motivation stays unless they revise it (intellectual anchor in the overview, if they wrote one)

## Optional (this version)

- [ ] **Record of material AI use** — a short note when AI did substantial work (some journals ask). Default is off. Tick this box to turn it on. Off means no extra kit file. You still disclose in the paper when AI affected reliability. See `policies/ai-policy.md`.
- [ ] **Map the evidence** — draft source-grounded packets when you say **Map the evidence**. Default is off as a reminder; the phrase still runs if you say it.
- [ ] **Experimental NotebookLM connector** — the assistant may query your NotebookLM notebook if a connector is available in this tool (Cursor, Codex, or Claude Code). Not official Google. Non-sensitive sources only. Default is off. If you tick this, the assistant will ask which notebook tools to use — it does not guess names. Ticking it, or asking in that chat to query, map evidence, or add `08-sources/` to this paper’s notebook, is enough: do not ask for a second authorization, and do not refuse the named question as unpublished framing. If off, it uses this paper’s `08-sources/` folder and any note you paste, unless you asked to query the notebook in that chat.
- [ ] **Author voice** — when drafting or editing manuscript prose, follow this paper’s voice note and avoid generic filler. Default is off. Tick this box to turn it on for **this paper**. Off means ordinary drafting; **Scan for generic prose** still works. If off, saying **Draft this in my voice** does not run until you tick the box.
- [ ] **Propose wording in prose scans** — when you say **Scan for generic prose**, each finding may include a suggested replacement. Default is off. Off means diagnose only (no proposed wording). The scan still does not edit the manuscript. Tick this if you want the extra field so a later edit does not start from a blank page.
- [ ] **External manuscript review** — the assistant may send the named manuscript to the review service in this paper’s folder map (this computer or hosted; Coarse is one implementation). Restricted or confidential files stay off that service. Default is off. If off, **Review the manuscript** is the assistant’s own reading, unless you ask in that chat for an external review or **coarse-review**. A prose scan never sends the file. Findings still go to the inbox; they are not an audit.

## Where to run

Some features need the files on this computer. A cloud session that only sees staged uploads cannot hash what it has not transferred, and that is not an audit.

- **This computer.** **Audit the research chain**, **Audit data construction**, **Audit literature claims** when sources or outputs are large, **Audit APA presentation** of the rendered Word/PDF, **Run approved Stata analysis**. Hash the files you actually read. Do not upload tens of megabytes to finish a check.
- **Anywhere the record is.** Planning, deciding, **Understand the project**, **Review the manuscript**, **Scan for generic prose**, **Author voice**, **Explore alternative framings**, **Map the evidence**. These need the manuscript and the shared record.
- **Either.** **Contribute to the project**, **Prepare a review copy** / **Sync the review copy** / **Ingest review comments** (Google tools if used), **Update the project record**, **Document a research decision**.

## Not in this version

Journal disclosure forms, Word as the canonical manuscript, Word comment ingest, automatic background audits, writing to Zotero, a required Python program, treating NotebookLM as verification, and the assistant starting unassigned tasks. Do not offer those as kit features.
