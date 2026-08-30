---
name: audit-research-chain
description: Audit whether scientific meaning held from agreed analysis plan through code, output, manuscript, and claims. Report numbers/reproducibility and estimand/claim validity as separate statuses. Diagnose only; write the report and, if anything needs work, one task. Do not repair or ask how to repair. Use when they say Audit the research chain, for a full chain check or one link. Use when they say Audit data construction to trace one named central claim (opt-in only).
license: MIT
compatibility: Requires a project filesystem. Running analysis code is optional and must follow this paper’s data-use rules. A useful partial audit is expected when code cannot be run.
metadata:
  version: "0.2.9"
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

If they asked for APA layout, tables in Word, or a presentation check of the rendered paper, use `skills/audit-apa-presentation/SKILL.md` instead. Do not fold that into this skill.

## Two gates (never one overall PASS)

The saved report, and the compact status in chat, must show **two** statuses:

1. **Numbers / reproducibility** — do code, outputs, tables, and manuscript agree?
2. **Estimand / claim validity** — does the design and evidence support what is claimed?

A project may pass the first and still have ISSUES or NOT VERIFIED on the second. Do **not** flatten the two into one overall PASS. Passing numbers never implies that the claims are supported.

APA table and figure cosmetics (italic titles, vertical lines, typeface) are **not** a third gate here. Source wording is **Review the manuscript**. The rendered Word/PDF is **Audit APA presentation**. An ordinary research-chain audit still checks whether a display can be read as evidence (see the checklists).

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

If authoritative files conflict, **report the conflict** as a finding (`next`: **researcher decision needed**). Do not pick a winner. Do not ask which file should win in this run.

Copied protocols and extra docs are background. Draft outputs are not approved results. An audit report is **history**, not a new analysis plan.

Record hygiene (stale STATUS lines, open tasks that only say “accept/reject”) belongs in the audit **only when it changes what counts as agreed**. Do not add a fifth PASS / ISSUES / NOT VERIFIED row for documentation.

## Diagnose, do not repair

**Do:** name discrepancies; say when a link cannot be checked; classify severity; say why it matters; point to files; in the saved report, name the **kind of work** for a next action (or **researcher decision needed**).

**Do not:** edit the analysis plan; accept a research decision; change analysis code; regenerate results; rewrite manuscript claims; mark a finding resolved because you proposed a fix; draft a patch, script, or protocol in this run; ask how a finding should be framed or which unagreed design to pick.

A finding may say that implementation should match the agreed sample. It may not specify an unagreed design (how to resume a run, which extra checks to add, which metadata fields to invent) unless that design is already in the plan or an accepted note.

If a fix needs a methodological choice, write **researcher decision needed** in that finding’s `next`. Do not write or accept that decision in this run. Do not ask them to choose among designs here.

## Do not invent missing evidence

If you cannot establish a link, the status is **NOT VERIFIED** — not PASS, and not a reconstructed story.

Examples: no `produced_by`; the named script is missing; output is still a draft; a manuscript number has no identifiable approved source; you cannot run the code; this paper’s data-use rules close the files you would need.

Do not re-run against row-level real data when this paper’s data-use rules forbid it. Partial audit from files is still useful — say what you could not check.

Do not assume that a file existing proves the stated script produced it.

## Full audit

Do not only concatenate four checklists. If an earlier link is broken, say so when judging a later one (for example: the manuscript copies a number that came from code that does not match the plan).

Set each gate from the links in that gate. Gate PASS only if every in-scope link for that gate is PASS. If any is ISSUES, the gate is ISSUES. Else if any is NOT VERIFIED, the gate is NOT VERIFIED. Never roll the two gates into one line.

## After the report

Save the full report under `paths.audits`. Follow [report format](references/report-format.md).

Then, if anything needs work, add **one** unassigned row on the tasks file (`layout.yml` path `tasks`). Do not start a second list. Do not copy every finding onto the list. Notes stay notes.

Add that row when either gate is ISSUES or NOT VERIFIED, or when any finding is `critical`, `major`, or `minor`. Do not add a row if both gates are PASS and leftover findings are `note` only. If an open task already points at this same report file, do not add another.

The row:

- **task** — address findings in the saved report (name the file)
- **kind of work** — if every work finding shares one kind, use that; if they differ, use `—` (the later chat reads the report)
- **from** — finding ids (for example `AUD-002`)
- **assigned_to_this_run** — `no`
- **status** — `open`

**Kind of work** (one, when they share it): write analysis code · run on real data · record a research decision · update the analysis plan · check the research chain · work on the manuscript. **Researcher decision needed** is not write analysis code; if that is the only remaining work, the kind is record a research decision.

If the tasks file has no kind-of-work or status column yet, add them when you write this row.

In chat, do **not** reprint every finding. Give the **two gate statuses**, a short “what holds / what does not,” the path of the saved file, and the new task id if you added one. Then **stop**.

Do not ask a numbered list. Do not ask how to frame or fix a finding. Do not ask whether to add the task. Do not draft a research decision note. Do not start write-analysis-code in this run. Do not start another assistant. Do not end with a block for them to paste into another chat.

If they want the next piece of work: new chat, **Do T-004** (the row you added). That later chat — not this one — chooses designs, records decisions, and edits files.

Accepted scientific changes later use **Update the project record**.

Do not copy agreed analyses or output metadata into the report beyond what a finding needs.

If this paper’s `what-is-on.md` has the AI-use box ticked, record one material event (`role: evaluation`, `check: audit-run`). If the box is off, do not write `ai-use/` and do not ask.

## Must not

- Repair the work you are auditing
- Flatten the two gates into one overall PASS
- Fail Numbers or Claims for APA cosmetics (italic title, vertical lines, typeface)
- Add data construction unless they asked
- Ask how to frame or fix a finding, or which unagreed design to pick
- Start an unassigned task, or another assistant, from this run (writing one task *row* is not starting the task)
- Treat a draft or synthetic output as an approved result
- Call an approved result a *verified result*
- Load working notes or old audit reports as current scientific authority
- Treat the overview Data section as overriding the plan, accepted notes, or result files
- Cross a restricted data line in order to “complete” the audit
- Print a prompt for them to paste to a later coding chat
