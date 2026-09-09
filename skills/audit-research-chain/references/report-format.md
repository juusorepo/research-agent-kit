# Audit report format

Save the full report under `paths.audits` in `layout.yml` (default `07-record/audits/`) when that folder map exists. If it does not, save under `audits/` in the folder you checked. Create the folder if needed.

Use a dated file name, for example `2026-08-17-full.md`. Do not overwrite an older report.

The saved file is a **record of a check**. It is not the analysis plan, not an approved result, and not a research decision.

In **this chat**, do not reprint the whole report. Write: the **two gate statuses**, a few sentences on what holds and what does not, the path of the saved file, and the new task id if you added one. Then stop. Do not ask how to fix the findings.

## Report contents (saved file)

1. Scope audited (full chain, which link, or data construction)
2. **Where the files were** — plan, code, outputs, manuscript (or “none / not provided”). Required when there was no folder map
3. Material checked (plan items, scripts, result files, manuscript sections; the one central claim if data construction was asked)
4. Two gate statuses, then a few sentences of assessment — **not** one overall PASS
5. Findings, ordered by severity
6. Links that could not be checked, and why
7. If a task row was added, name it. If none was added (no task list), say so. Do not list how to repair each finding. The `next` field on each finding is enough.

If plan or accepted notes conflict with STATUS or the task list about what is agreed, record that as a finding. Do not give it a fifth status row.

For a full audit, include this compact status. Do not let it replace the findings. Do **not** add a combined PASS line.

```
Numbers / reproducibility     PASS / ISSUES / NOT VERIFIED
Estimand / claim validity     PASS / ISSUES / NOT VERIFIED

Analysis plan → code          PASS / ISSUES / NOT VERIFIED
Code → output                 PASS / ISSUES / NOT VERIFIED
Output → manuscript           PASS / ISSUES / NOT VERIFIED
Results → claims              PASS / ISSUES / NOT VERIFIED
```

A project may pass numbers / reproducibility and still have ISSUES or NOT VERIFIED on estimand / claim validity.

If they asked to audit data construction, add one extra line (omit it otherwise):

```
Data construction             PASS / ISSUES / NOT VERIFIED
Central claim: …
```

- **PASS** — this gate or link holds, given what you could check
- **ISSUES** — at least one substantive finding
- **NOT VERIFIED** — you could not establish the link (missing provenance, cannot run the code, draft output only, or data-use rules close the files). Do not treat this as PASS

Set each **gate** from the links in that gate: PASS only if every in-scope link is PASS; ISSUES if any is ISSUES; otherwise NOT VERIFIED if any is NOT VERIFIED.

Do not call an approved result a *verified result*. These labels are about **gates and links**, not about promoting a file.

## Finding fields

Each substantive finding:

| Field | Content |
|---|---|
| id | `AUD-001`, `AUD-002`, … (this report only) |
| transition | `plan→code`, `code→output`, `output→manuscript`, `results→claims`, `data-construction` (more than one if the problem spans links) |
| severity | `critical` / `major` / `minor` / `note` |
| where | file and location |
| expected | what the authoritative file says |
| observed | what you found |
| why it matters | scientific consequence |
| next | kind of work, researcher decision needed, or leave as note |

A finding is an audit observation, **not** a research decision.

If `next` names work, name the **kind of work**. Do not treat **researcher decision needed** as write analysis code. Notes stay notes — they do not become tasks.

Do not put an implementation sketch in `next` (script design, extra checks, new metadata fields) unless that design is already agreed.

### Severity

- **critical** — a result or claim should not currently be relied on
- **major** — substantive discrepancy; needs correction or a researcher decision
- **minor** — real inconsistency with limited effect on interpretation
- **note** — uncertainty, missing provenance, or a useful observation that is not established as an error

Do not add more levels.

If the next action is a methodological choice, write **researcher decision needed** in `next`. Do not implement the change in this run. Do not ask which design to pick.

## After the report (in chat)

Do not add a second essay. Do not paste a prompt for a later coding chat. Do not ask a numbered list.

Example:

Numbers / reproducibility: ISSUES. Estimand / claim validity: ISSUES.

The plan→code link holds for the main models. Two major findings (AUD-002, AUD-003) need work; the notes stay in the report.

Saved: `07-record/audits/2026-08-23-full.md`. Added **T-010** on the task list.

If they want the next piece of work: new chat, **Do T-010**. That chat reads the report. This chat stops here.

If there was no task list, omit the “Added T-…” line. Remaining work stays in the report.
