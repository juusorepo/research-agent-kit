---
name: update-project-record
description: After the lead researcher accepts something, write it into the shared record. Use when a proposal is accepted, a result is approved, a task finishes, or a material AI contribution should be kept. Not at the end of every chat.
license: MIT
compatibility: Requires a project filesystem.
metadata:
  version: "0.1.0"
---

# Update the project record

Do this when one of these happened — not because a chat ended:

- The lead researcher accepted or rejected a proposal or research decision note
- A plan item was added or changed
- A result file became approved
- An assigned task finished and something should be kept
- A material AI contribution should be retained

## Do

- Merge an **accepted** proposal into `ANALYSIS_PLAN.md` (only after the human accepted)
- Fill `accepted_by`, `accepted_at`, `artifacts_changed` on an accepted decision note
- Refresh `STATUS.md` as a snapshot
- Archive or close the assigned task
- **Record** a clearly material AI-use event (`ai-use/AI-NNN.yml`), or **ask** only if ambiguous
- Never record orientation

Use `templates/ai-use-event.yml`. Roles: `drafting` | `implementation` | `evaluation` | `co-ideation`.  
If AI wrote the script for an agreed human plan: `origin: human`, `role: implementation`.

## Refuse

- Treating a proposal as agreed without human acceptance
- Approving a result unless `analysis_ref` is already an agreed plan item
- Calling a run clean if propose → implement → interpret happened in one run
- Writing an AI-use event for understand-the-project orientation
