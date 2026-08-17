# Audit report format

Write the report in this chat. Then save a copy under `paths.audits` in `layout.yml` (default `07-record/audits/`). Create that folder if needed.

Use a dated file name, for example `2026-08-17-full.md`. Do not overwrite an older report.

The saved file is a **record of a check**. It is not the analysis plan, not an approved result, and not a research decision.

## Report contents

1. Scope audited (full chain, or which link)
2. Material checked (plan items, scripts, result files, manuscript sections)
3. Overall assessment (a few sentences)
4. Findings, ordered by severity
5. Links that could not be checked, and why
6. Recommended next actions

For a full audit, include this compact status. Do not let it replace the findings.

```
Analysis plan → code       PASS / ISSUES / NOT VERIFIED
Code → output              PASS / ISSUES / NOT VERIFIED
Output → manuscript        PASS / ISSUES / NOT VERIFIED
Results → claims           PASS / ISSUES / NOT VERIFIED
```

- **PASS** — this link holds, given what you could check
- **ISSUES** — at least one substantive finding on this link
- **NOT VERIFIED** — you could not establish the link (missing provenance, cannot run the code, draft output only). Do not treat this as PASS

Do not call an approved result a *verified result*. These labels are about **links**, not about promoting a file.

## Finding fields

Each substantive finding:

| Field | Content |
|---|---|
| id | `AUD-001`, `AUD-002`, … (this report only) |
| transition | `plan→code`, `code→output`, `output→manuscript`, `results→claims` (more than one if the problem spans links) |
| severity | `critical` / `major` / `minor` / `note` |
| where | file and location |
| expected | what the authoritative file says |
| observed | what you found |
| why it matters | scientific consequence |
| next | concrete action (task with kind of work, researcher decision needed, re-run, leave as note) |

A finding is an audit observation, **not** a research decision.

If `next` is a task, name the **kind of work**. Do not treat **researcher decision needed** as write analysis code. Notes stay notes — they do not become tasks.

### Severity

- **critical** — a result or claim should not currently be relied on
- **major** — substantive discrepancy; needs correction or a researcher decision
- **minor** — real inconsistency with limited effect on interpretation
- **note** — uncertainty, missing provenance, or a useful observation that is not established as an error

Do not add more levels.

If the next action is a methodological choice, write **researcher decision needed** in `next`. Do not implement the change in this run.
