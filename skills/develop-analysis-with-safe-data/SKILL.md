---
name: develop-analysis-with-safe-data
description: Write and test analysis under the project's data-use rules. Use when they say Develop analysis with safe data or are assigned a write-analysis-code task (Do T-NNN), or when drafting scripts, producing draft outputs, or implementing an agreed analysis. Never cross a restricted data line.
license: MIT
compatibility: Requires a project filesystem. R is needed only when running R scripts.
metadata:
  version: "0.1.4"
---

# Develop analysis with safe data

Resolve script and output folders from `layout.yml`. Do not assume `analysis/` or `02-scripts`.

## This run

Read the tasks file (`layout.yml` path `tasks`). Work only on a row with `assigned_to_this_run: yes`. They assign it by saying **Do T-004**.

If none is assigned, **stop** and ask which task — unless they only asked to explore metadata or write a throwaway draft. Implementing an agreed analysis needs an assigned task.

This skill is for **write analysis code** (and draft outputs). If the assigned row is **run on real data** and this paper’s `layout.yml` has `code: stata`, use `skills/run-approved-stata-analysis/SKILL.md` instead. If the assigned row is another kind of work, stop and follow that kind.

Restricted data: you may write scripts. **run on real data** is the authorised analyst, not this chat — except the Stata run skill, which still must follow this paper’s data-use rules.

## Inputs

`01-data/raw` is original files only. Do not overwrite them. Conversion and cleaning write to `01-data/processed` (layout path `data_processed`). Analysis scripts and configs read **processed**, never raw. Metadata and codebooks may live under `01-data/metadata`.

## Outputs

Canonical tables and figures go in the layout output folders. Pilots, smokes, and throwaways go under a `_dev` folder there (for example `05-outputs/tables/_dev/`). Do not leave them next to results a later search would treat as real.

If a file should go away and delete fails (common on Windows / OneDrive), move it to `99-archive/quarantine/` instead of retrying delete.

If this project uses a canonical unit id (study, country, wave, and so on), that id is a **column** on derived tables. The filename is only a hint.

## Keys

Do not put keys in chat, in committed configs, or in the manuscript. Inject them at run time from the environment (`.env` / `.Renviron`, already gitignored). Do not commit files that contain keys.

## Output metadata

Every result file needs a **sidecar** next to it (same stem, `.yml`), using `templates/output-metadata.yml`. Default `status: provisional`. Required fields: `id`, `status`, `source`, `analysis_ref`, `produced_by`, `privacy_control`. Set `run_by` when a person ran it. Follow this project’s identifier and small-cell rules — the kit does not ban country or institution names unless the policy does.

Do not treat a table without a sidecar as an approved result.

## Always allowed

Explore and draft under `data_access`. Write **draft** outputs (`status: provisional`) with a sidecar metadata file.

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
- A sidecar exists for the result file
- `approved_by` / `approved_at` are set by the **lead researcher**, not by you
- If `source: real`, `run_by` is set
- If the policy has `approval_requires_real: true`, do not mark synthetic as approved

## Refuse

- Silent edits to the analysis plan or an accepted decision note
- Implementing an agreed analysis with no task assigned to this run
- Inventing real numbers
- Copying draft/synthetic numbers into approved files
- Approving against a proposal
- Reading restricted row-level real data when `data_access: restricted`
- Pointing analysis inputs at `01-data/raw` (conversion may read raw; it must write processed)
- Writing a result file with no sidecar metadata
- Putting real numbers in the manuscript when there is no qualifying approved result

## Manuscript

The Quarto file cites **approved** result files only. It must not read row-level data. Do not paste draft or synthetic numbers into Results.
