---
name: update-project-record
description: After the lead researcher accepts something, write it into the shared record. Use when they say Update the project record, or when a proposal is accepted, a result is approved, a task finishes, or a material AI contribution should be kept. Not at the end of every chat.
license: MIT
compatibility: Requires a project filesystem.
metadata:
  version: "0.3.1"
---

# Update the project record

Do this when one of these happened — not because a chat ended:

- The lead researcher accepted or rejected a proposal or research decision note
- A plan item was added or changed
- A result file became approved
- An assigned task finished and something should be kept
- A material AI contribution should be retained

## Accept as one routine

When they accept a research decision (in chat is enough), do **all** of the following in this run. Do not stop after flipping the note.

1. Set the note `status: accepted` (or `rejected` / `superseded` as they said)
2. Fill `accepted_by` and `accepted_at` (leave them empty only on reject, if that is this paper’s habit)
3. If the decision governs a plan item, set that item’s `decision_ref` to the note id
4. Close or archive the matching accept-task on the task list
5. Rewrite `STATUS.md` in place (see below)

If any step is still open, acceptance is not finished. Finish it before other work.

**Amendments:** edit the existing note (or mark it `superseded` and point the new note at it). Rewrite Decision / Rationale. Never leave the old wording as a live paragraph above a new one.

## Do

- Merge an **accepted** proposal into `ANALYSIS_PLAN.md` (only after the human accepted). They do not have to type the file.
- After they accept a drafted overview, write it into `RESEARCH_CONTEXT.md`
- Fill `accepted_by`, `accepted_at`, `artifacts_changed` on an accepted decision note; set that row’s status in `decisions/INDEX.md`
- After they accept a contribution: apply the chosen home, then set the contribution `status` to `integrated` or `archived`
- After they accept a **Sync the review copy**, the manuscript update is already done in that skill; here only refresh `STATUS.md` if still stale
- Rewrite `STATUS.md` as a snapshot (not a log)
- Archive or close the assigned task
- **Record** a clearly material AI-use event only if `policies/what-is-on.md` has that box ticked. If the box is off, do not write `ai-use/` and do not ask. If the box is on: record when clearly material; ask only if ambiguous; never record orientation.

Use `templates/ai-use-event.yml`. Roles: `drafting` | `implementation` | `evaluation` | `co-ideation`.  
If AI wrote the script for an agreed human plan: `origin: human`, `role: implementation`.

## STATUS.md

Keep the template headings only: **Current stage**, **Active work**, **Blockers**, **Unresolved scientific questions**, **Recently completed**. Rewrite those sections. Do not add dated headings. Git is the archive.

If the same heading appears more than once, or the file has accreted dated sections, **collapse to the current state** under the five headings before you finish.

## Refuse

- Treating a proposal as agreed without human acceptance
- Marking a decision accepted without the full routine above
- Approving a result unless `analysis_ref` is already an agreed plan item
- Calling a run clean if propose → implement → interpret happened in one run
- Writing an AI-use event for understand-the-project orientation
- Treating an audit report as agreeing an analysis, approving a result, or replacing the analysis plan
