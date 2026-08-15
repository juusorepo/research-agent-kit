---
name: develop-analysis-with-safe-data
description: Write and test analysis under the project's data-use rules. Use when drafting scripts, producing draft outputs, or implementing an agreed analysis. Never cross a restricted data line.
license: MIT
compatibility: Requires a project filesystem. R is needed only when running R scripts.
metadata:
  version: "0.1.0"
---

# Develop analysis with safe data

Resolve script and output folders from `layout.yml`. Do not assume `analysis/` or `02-scripts`.

## Always allowed

Explore and draft under `data_access`. Write **draft** outputs (`status: provisional`) with output metadata (`id`, `status`, `source`, `produced_by`, `privacy_control`).

## Implementing

Only against an agreed `A-NNN` in the analysis plan.

## New analysis

Write `proposals/A-NNN.md`. If the change is important, also write a proposed research decision note. Then **stop**.

Say: “This is not yet in the agreed analysis plan.”

## Researcher decision needed

If the action would change design, measurement, sample, analysis, interpretation, or claims, say:

> Researcher decision needed — I suggest recording a research decision before implementing.

Write the proposed note if needed. **Stop.** Do not implement and interpret in the same run (I9).

## Before anyone marks `status: approved`

- `analysis_ref` is an agreed plan item (a proposal does not count)
- The run followed `data_access`
- `approved_by` / `approved_at` are set by the **lead researcher**, not by you
- If `source: real`, `run_by` is set
- If the policy has `approval_requires_real: true`, do not mark synthetic as approved

## Refuse

- Silent edits to the analysis plan or an accepted decision note
- Inventing real numbers
- Copying draft/synthetic numbers into approved files
- Approving against a proposal
- Reading restricted row-level real data when `data_access: restricted`
- Putting real numbers in the manuscript when there is no qualifying approved result

## Output metadata

Use `templates/output-metadata.yml`. Put metadata in the result file or a sidecar. Follow this project’s identifier and small-cell rules — the kit does not ban country or institution names unless the policy does.
