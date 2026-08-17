---
name: audit-research-chain
description: Audit whether scientific meaning held from agreed analysis plan through code, output, manuscript, and claims. Diagnose only; do not repair. Use for a full chain check or one link.
license: MIT
compatibility: Requires a project filesystem. Running analysis code is optional and must follow this paper’s data-use rules. A useful partial audit is expected when code cannot be run.
metadata:
  version: "0.2.2"
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

If they do not say, do a **full** audit.

## Authority (do not invent a second one)

| Question | What wins |
|---|---|
| What analyses are agreed? | Analysis plan |
| Why was an important choice made? | Accepted research decision notes |
| How was this result produced and approved? | Output metadata on the result file |
| What do we currently report? | Canonical manuscript (`paths.manuscript`) |
| What changed in the past? | Git — history, not current scientific authority |

Do not infer the intended analysis from the manuscript or the overview when an agreed plan exists.

If authoritative files conflict, **report the conflict**. Do not resolve it.

Copied protocols and extra docs are background. Draft outputs are not approved results. An audit report is **history**, not a new analysis plan.

## Diagnose, do not repair

**Do:** name discrepancies; say when a link cannot be checked; classify severity; say why it matters; point to files; propose a next action.

**Do not:** edit the analysis plan; accept a research decision; change analysis code; regenerate results; rewrite manuscript claims; mark a finding resolved because you proposed a fix.

If a fix needs a methodological choice, say **researcher decision needed**. Do not write or accept that decision in this run unless they separately ask to record a research decision.

## Do not invent missing evidence

If you cannot establish a link, the status is **NOT VERIFIED** — not PASS, and not a reconstructed story.

Examples: no `produced_by`; the named script is missing; output is still a draft; a manuscript number has no identifiable approved source; you cannot run the code (including **restricted** row-level real data).

Do not re-run against row-level real data when this paper’s data-use rules forbid it. Partial audit from files is still useful — say what you could not check.

Do not assume that a file existing proves the stated script produced it.

## Full audit

Do not only concatenate four checklists. If an earlier link is broken, say so when judging a later one (for example: the manuscript copies a number that came from code that does not match the plan).

## After the report

The work list is the tasks file (`layout.yml` path `tasks`). Do not start a second list.

Save the report. Then in chat ask a **short numbered list** (defaults in parentheses) and **wait**. Do not leave a wall of next steps. Follow [report format](references/report-format.md) for the questions.

Group only in those questions:

1. **Decide now** — researcher decision needed, or anything that blocks approving results
2. **Task list now** — already-agreed work they want as `open` (point at an existing task if one covers it)
3. **Later** — still write a task row with status `later`, so it is not forgotten
4. **Notes** — default: leave as notes; do not copy them onto the task list

**Kind of work** (one): write analysis code · run on real data · record a research decision · update the analysis plan · check the research chain · work on the manuscript. **from**: finding ids (for example `AUD-002`).

After they answer: write the accepted rows (`open` or `later`; `assigned_to_this_run` stays `no`). If they asked for a research decision note, draft it as **proposed** and stop. Do not start write-analysis-code in this run. If they want coding, say: new chat, **Do T-004**.

If the tasks file has no kind-of-work or status column yet, add them when you write the first proposed row.

Accepted changes later use **Update the project record**.

Do not copy agreed analyses or output metadata into the report beyond what a finding needs.

If this paper’s `what-is-on.md` has the AI-use box ticked, record one material event (`role: evaluation`, `check: audit-run`). If the box is off, do not write `ai-use/` and do not ask.

## Must not

- Repair the work you are auditing
- Start an unassigned task, or another assistant, from this run
- Treat a draft or synthetic output as an approved result
- Call an approved result a *verified result*
- Load working notes or old audit reports as current scientific authority
- Cross a restricted data line in order to “complete” the audit
