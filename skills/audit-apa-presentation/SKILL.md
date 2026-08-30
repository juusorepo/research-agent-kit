---
name: audit-apa-presentation
description: Layout and APA-7 presentation check of the rendered manuscript (Word plus a PDF exported from that Word file). Diagnose only. Use when they say Audit APA presentation, Check tables and figures in Word, or APA layout audit. Not an audit of the research chain. Not a peer-style manuscript review.
license: MIT
compatibility: Requires a project filesystem. Needs the canonical manuscript plus a rendered Word file and a PDF exported from that Word file. A useful partial check is expected when a file is missing.
metadata:
  version: "0.1.0"
---

# Audit APA presentation

Check whether the **rendered paper** is intact and whether tables, figures, and manuscript frame follow the house list (APA 7 where the checker is sure).

This is an **audit**. It is not implementation, approval, or a peer review.

It is **not** `audit-research-chain` (plan → code → output → claims). It is **not** `review-the-manuscript` (peer-style findings in the inbox). Do not fold this into either.

If this same chat produced or changed the manuscript or the Word/PDF you would be checking, **stop**. Ask them to start a **separate** run (a new chat is enough).

Follow [checklist](references/checklist.md) and [report format](references/report-format.md).

Resolve folders from `layout.yml`. Save the report under `paths.audits`.

## When

They say **Audit APA presentation**, **Check tables and figures in Word**, or **APA layout audit**.

Work in the **paper** folder.

## Inputs

Required:

| File | Role |
|---|---|
| Canonical manuscript (`.qmd`, or Word/Markdown source) | Map: labels, captions, call-outs, YAML |
| Rendered **Word** file | What they would submit-like send |
| **PDF exported from that Word file** | What you can see: clipping, captions, icons, heading order |

Optional: `references.bib`; two to four screenshots if the PDF is hard to read; journal author instructions (those win over the house list).

Do **not** treat a Google Docs review copy as the object of this check. Do **not** knit a separate Quarto or Typst PDF as the APA object unless that is what they will submit.

If Word or the Word-exported PDF is missing: **NOT VERIFIED** on render integrity and on tables and figures. Do not audit the source file alone and call tables PASS.

If source and PDF disagree, the PDF is the rendered object. Mark **render integrity ISSUES** (stale PDF). Do not treat a placeholder that is already gone from the source as a live YAML error.

## Four gates (never one overall PASS)

The saved report, and the compact status in chat, must show **four** statuses:

1. **Render integrity** — does the source appear in this Word/PDF?
2. **APA tables**
3. **APA figures**
4. **APA manuscript** — title page, headings, text frame, references

Do not flatten the four into one overall PASS.

A gate is PASS only if it holds given what you could check. ISSUES if any substantive finding in that gate. NOT VERIFIED if you could not check it.

Uncertain house or APA rule → severity `note`, not ISSUES.

Do not check whether numbers match approved results. That is **Audit the research chain**.

## After the report

Save the full report under `paths.audits` (dated name, for example `2026-08-30-apa-presentation.md`). Do not overwrite an older report.

Then, if anything needs work, add **one** unassigned row on the tasks file. Do not copy every finding onto the list. Notes stay notes.

Add that row when any gate is ISSUES or NOT VERIFIED, or when any finding is `critical`, `major`, or `minor`. Do not add a row if every gate is PASS and leftover findings are `note` only. If an open task already points at this same report file, do not add another.

The row:

- **task** — address findings in the saved report (name the file)
- **kind of work** — `work on the manuscript` when the work is layout; `record a research decision` if the only remaining work is a researcher decision (for example an empty Discussion they have not agreed to write); `—` if those differ
- **from** — finding ids (for example `APA-002`)
- **assigned_to_this_run** — `no`
- **status** — `open`

In chat, do **not** reprint every finding. Give the **four gate statuses**, a short “what holds / what does not,” the path of the saved file, and the new task id if you added one. Then **stop**.

Do not ask a numbered list. Do not ask how to fix a finding. Do not start manuscript edits in this run.

If they want the next piece of work: new chat, **Do T-004**.

If this paper’s `what-is-on.md` has the AI-use box ticked, record one material event (`role: evaluation`, `check: apa-presentation-audit`). If the box is off, do not write `ai-use/` and do not ask.

## Must not

- Repair the manuscript in this run
- Invent bibliography records
- Restate or scrape the APA Publication Manual
- Use web search as required evidence
- One overall PASS
- Load old audit reports as scientific authority
- Treat a Google Docs review copy as the rendered paper
- Fold this into the research-chain audit or into **Review the manuscript**
