---
name: audit-research-chain
description: Audit whether scientific meaning held from agreed analysis plan through code, output, manuscript, and claims. Report numbers/reproducibility and estimand/claim validity as separate statuses. Diagnose only; do not repair. Use when they say Audit the research chain, for a full chain check or one link. Use when they say Audit data construction to trace one named central claim (opt-in only).
license: MIT
compatibility: Requires a project filesystem. Running analysis code is optional and must follow this paper’s data-use rules. A useful partial audit is expected when code cannot be run.
metadata:
  version: "0.2.6"
---

# Audit the research chain

Check whether scientific meaning stayed intact:

**agreed analysis plan → implementation → research output → manuscript result → scientific claim**

This is an **audit**. It is not implementation, approval, or revision.

If this same chat produced or changed the files you would be checking, **stop**. Ask them to start a **separate audit run** (a new chat is enough). Do not call that independent verification.

Follow [checklists](references/checklists.md) and [report format](references/report-format.md).

Resolve folders from `layout.yml`. Do not assume `02-scripts` or `07-record/`.

## When

They ask to audit the research chain, or one link:

- full chain
- analysis plan and code
- code and output
- output and manuscript
- results and scientific claims

**Audit data construction** only if they asked for it. It is not part of an ordinary full audit. Trace **one** material central claim. If they did not name the claim, ask which (default: the manuscript’s main empirical claim) and **wait**.

If they do not say a scope, do a **full** audit of the four links. Do not add data construction unless they asked.

## Two gates (never one overall PASS)

The saved report, and the compact status in chat, must show **two** statuses:

1. **Numbers / reproducibility** — do code, outputs, tables, and manuscript agree?
2. **Estimand / claim validity** — does the design and evidence support what is claimed?

A project may pass the first and still have ISSUES or NOT VERIFIED on the second. Do **not** flatten the two into one overall PASS. Passing numbers never implies that the claims are supported.

Where this paper’s data-use rules prevent tracing a link (including closed row-level real data), that link is **NOT VERIFIED**. Do not treat the gap as a pass.

## Authority (do not invent a second one)

| Question | What wins |
|---|---|
| What analyses are agreed? | Analysis plan |
| Why was an important choice made? | Accepted research decision notes |
| How was this result produced and approved? | Output metadata on the result file |
| What do we currently report? | Canonical manuscript (`paths.manuscript`) |
| What data are available, and what are the limits? | Overview Data section — **description only**. It does not override the plan, accepted notes, or result files |
| What changed in the past? | Git — history, not current scientific authority |

Do not infer the intended analysis from the manuscript or the overview when an agreed plan exists.

**What is agreed** is always in scope. Read the analysis plan and accepted decision notes before judging any link. `STATUS.md` and the task list are not scientific authority.

If authoritative files conflict, **report the conflict**. Do not pick a winner in the report. Ask one numbered question about it (defaults in parentheses) and wait. Their answer is theirs; a default in the question is not an accepted research decision.

Copied protocols and extra docs are background. Draft outputs are not approved results. An audit report is **history**, not a new analysis plan.

Record hygiene (stale STATUS lines, open tasks that only say “accept/reject”) belongs in the audit **only when it changes what counts as agreed**. Do not add a fifth PASS / ISSUES / NOT VERIFIED row for documentation.

## Diagnose, do not repair

**Do:** name discrepancies; say when a link cannot be checked; classify severity; say why it matters; point to files; name the **kind of work** for a next action (or **researcher decision needed**).

**Do not:** edit the analysis plan; accept a research decision; change analysis code; regenerate results; rewrite manuscript claims; mark a finding resolved because you proposed a fix; draft a patch, script, or protocol in this run.

A finding may say that implementation should match the agreed sample. It may not specify an unagreed design (how to resume a run, which extra checks to add, which metadata fields to invent) unless that design is already in the plan or an accepted note.

If a fix needs a methodological choice, say **researcher decision needed**. Do not write or accept that decision in this run unless they separately ask to record a research decision.

## Do not invent missing evidence

If you cannot establish a link, the status is **NOT VERIFIED** — not PASS, and not a reconstructed story.

Examples: no `produced_by`; the named script is missing; output is still a draft; a manuscript number has no identifiable approved source; you cannot run the code; this paper’s data-use rules close the files you would need.

Do not re-run against row-level real data when this paper’s data-use rules forbid it. Partial audit from files is still useful — say what you could not check.

Do not assume that a file existing proves the stated script produced it.

## Full audit

Do not only concatenate four checklists. If an earlier link is broken, say so when judging a later one (for example: the manuscript copies a number that came from code that does not match the plan).

Set each gate from the links in that gate. Gate PASS only if every in-scope link for that gate is PASS. If any is ISSUES, the gate is ISSUES. Else if any is NOT VERIFIED, the gate is NOT VERIFIED. Never roll the two gates into one line.

## After the report

Save the full report under `paths.audits`. In chat, do **not** reprint every finding. Give the **two gate statuses**, a short “what holds / what does not,” point at the file, then ask a **short numbered list** (defaults in parentheses) and **wait**. Follow [report format](references/report-format.md).

The work list is the tasks file (`layout.yml` path `tasks`). Do not start a second list. Do not end with a block for them to paste into another chat. The task row is the next assignment.

Group only in those questions:

1. **Decide now** — researcher decision needed, or anything that blocks approving results
2. **Task list now** — already-agreed work they want as `open` (point at an existing task if one covers it)
3. **Later** — still write a task row with status `later`, so it is not forgotten
4. **Notes** — default: leave as notes; do not copy them onto the task list

**Kind of work** (one): write analysis code · run on real data · record a research decision · update the analysis plan · check the research chain · work on the manuscript. **from**: finding ids (for example `AUD-002`).

After they answer: write the accepted rows (`open` or `later`; `assigned_to_this_run` stays `no`). If they asked for a research decision note, draft it as **proposed** and stop. Do not start write-analysis-code in this run. Do not start another assistant. If they want coding, one line: new chat, **Do T-004**.

If the tasks file has no kind-of-work or status column yet, add them when you write the first proposed row.

Accepted changes later use **Update the project record**.

Do not copy agreed analyses or output metadata into the report beyond what a finding needs.

If this paper’s `what-is-on.md` has the AI-use box ticked, record one material event (`role: evaluation`, `check: audit-run`). If the box is off, do not write `ai-use/` and do not ask.

## Must not

- Repair the work you are auditing
- Flatten the two gates into one overall PASS
- Add data construction unless they asked
- Start an unassigned task, or another assistant, from this run
- Treat a draft or synthetic output as an approved result
- Call an approved result a *verified result*
- Load working notes or old audit reports as current scientific authority
- Treat the overview Data section as overriding the plan, accepted notes, or result files
- Cross a restricted data line in order to “complete” the audit
- Print a prompt for them to paste to a later coding chat
