---
name: update-project-record
description: After the lead researcher accepts something, write it into the shared record. Use when they say Update the project record, or when a proposal is accepted, a result is approved, a task finishes, or a material AI contribution should be kept. Not at the end of every chat.
license: MIT
compatibility: Requires a project filesystem.
metadata:
  version: "0.3.0"
---

# Update the project record

Do this when one of these happened — not because a chat ended:

- The lead researcher accepted or rejected a proposal or research decision note
- A plan item was added or changed
- A result file became approved
- An assigned task finished and something should be kept
- A material AI contribution should be retained

## Do

- Merge an **accepted** proposal into `ANALYSIS_PLAN.md` (only after the human accepted). They do not have to type the file.
- After they accept a drafted overview, write it into `RESEARCH_CONTEXT.md`
- Fill `accepted_by`, `accepted_at`, `artifacts_changed` on an accepted decision note; set that row’s status in `decisions/INDEX.md`
- After they accept a contribution: apply the chosen home, then set the contribution `status` to `integrated` or `archived`
- After they accept a **Sync the review copy**, the manuscript update is already done in that skill; here only refresh `STATUS.md` if still stale
- Refresh `STATUS.md` as a snapshot
- Archive or close the assigned task
- **Record** a clearly material AI-use event only if `policies/what-is-on.md` has that box ticked. If the box is off, do not write `ai-use/` and do not ask. If the box is on: record when clearly material; ask only if ambiguous; never record orientation.

Use `templates/ai-use-event.yml`. Roles: `drafting` | `implementation` | `evaluation` | `co-ideation`.  
If AI wrote the script for an agreed human plan: `origin: human`, `role: implementation`.

## Refuse

- Treating a proposal as agreed without human acceptance
- Approving a result unless `analysis_ref` is already an agreed plan item
- Calling a run clean if propose → implement → interpret happened in one run
- Writing an AI-use event for understand-the-project orientation
- Treating an audit report as agreeing an analysis, approving a result, or replacing the analysis plan
