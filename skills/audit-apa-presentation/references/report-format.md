# APA presentation — report format

Save the full report under `paths.audits` in `layout.yml` (default `07-record/audits/`). Create that folder if needed.

Use a dated file name, for example `2026-08-30-apa-presentation.md`. Do not overwrite an older report.

The saved file is a **record of a check**. It is not the analysis plan, not an approved result, and not a research decision.

In **this chat**, do not reprint the whole report. Write: the **four gate statuses**, a few sentences on what holds and what does not, the path of the saved file, and the new task id if you added one. Then stop. Do not ask how to fix the findings.

## Report contents (saved file)

1. Scope (APA presentation; Word and PDF paths used)
2. Material checked (source file, Word, PDF, optional `.bib` / journal instructions / screenshots)
3. Four gate statuses, then a few sentences of assessment — **not** one overall PASS
4. Findings, ordered by severity
5. What could not be checked, and why
6. If a task row was added, name it. Do not list how to repair each finding. The `next` field on each finding is enough.

Include this compact status. Do not let it replace the findings. Do **not** add a combined PASS line.

```
Render integrity (source → Word/PDF)     PASS / ISSUES / NOT VERIFIED
APA tables                               PASS / ISSUES / NOT VERIFIED
APA figures                              PASS / ISSUES / NOT VERIFIED
APA manuscript (title, headings, text, references)   PASS / ISSUES / NOT VERIFIED
```

- **PASS** — this gate holds, given what you could check
- **ISSUES** — at least one substantive finding in this gate
- **NOT VERIFIED** — you could not check it (missing Word or PDF, unreadable page, Word-on-screen not available). Do not treat this as PASS

If Word or the Word-exported PDF is missing, render integrity, APA tables, and APA figures are **NOT VERIFIED**. Do not mark tables PASS from the source file alone.

## Finding fields

| Field | Content |
|---|---|
| id | `APA-001`, `APA-002`, … (this report only) |
| layer | `render` / `tables` / `figures` / `manuscript` (more than one if it spans) |
| severity | `critical` / `major` / `minor` / `note` |
| where | file and location (PDF page, Word section, source chunk) |
| expected | what the house list or attached journal file says |
| observed | what you found |
| why it matters | whether a reader or a journal can use the display |
| next | kind of work, researcher decision needed, or leave as note |

A finding is an audit observation, **not** a research decision.

### Severity

- **critical** — a table or figure cannot be read (clipped, missing)
- **major** — substantive layout or heading error; needs correction or a researcher decision
- **minor** — real inconsistency with limited effect (for example a long caption)
- **note** — uncertainty, or a rule you are not sure of

Do not add more levels. Uncertain APA rules stay `note`.
