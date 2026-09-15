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
- [ ] **External manuscript review** — the assistant may send the named manuscript to the review service in this paper’s folder map (this computer or hosted; Coarse is one implementation). Restricted or confidential files stay off that service. Default is off. If off, **Review the manuscript** is the assistant’s own reading, unless you ask in that chat for an external review or **coarse-review**. A prose scan never sends the file. Findings still go to the inbox; they are not an audit.

## Not in this version

Journal disclosure forms, Word toolchains, Word comment ingest, and automatic background audits. On-demand “audit the research chain”, “audit literature claims”, and “audit APA presentation” are in this version (independent checks; they do not certify the paper). Writing to Zotero, a required Python program, and treating NotebookLM as verification are not in this version. **Explore alternative framings** is in this version (optional; not for routine editing). **Author voice** is in this version (optional; off until you tick it). A Google Docs review copy (suggestions there, open comments to the inbox) is in this version. **External manuscript review** is in this version (optional; off until you tick it or ask; proposals only, not an audit). If this paper’s `layout.yml` has `code: stata`, a local Stata run (**Run approved Stata analysis**) is in this version. Do not offer the others as kit features.
