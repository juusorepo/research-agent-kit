---
name: run-approved-stata-analysis
description: Run one named Stata do-file for an agreed analysis on an assigned run-on-real-data task. Use when they say Run approved Stata analysis, or Do T-NNN when that task is run on real data and this paper’s analysis language is Stata. Windows first. Diagnose a failed run; do not change the analysis to repair it.
license: MIT
compatibility: Requires a project filesystem. Stata is needed only when running. Windows is the supported run path in this version.
metadata:
  version: "0.4.0"
---

# Run approved Stata analysis

Run **one** named `.do` file that already implements an agreed analysis. This is not writing new analysis code, not approving a result, and not a background job.

“Approved” here means the **analysis is agreed** and the **task is assigned**. It does not mean the result file is already `status: approved`. The lead researcher still approves the sidecar.

Follow this paper’s data-use rules. Resolve folders from `layout.yml`.

The optional helper is `adapters/stata/run-stata.ps1` in the kit. Use it if present. Do not copy it into the paper.

## When

They say **Run approved Stata analysis**, or they name a task (**Do T-004**) whose kind of work is **run on real data**.

Stop unless **all** of these hold:

1. `layout.yml` has `code: stata` (or they clearly chose Stata for this paper)
2. A task is assigned to this run (`assigned_to_this_run: yes`) and kind of work is **run on real data**
3. The `.do` file is **named** (in the task, the plan item, or this chat) and lives under the scripts path
4. `analysis_ref` on the run is an agreed `A-NNN` in the analysis plan

If they did not name the `.do` file, ask which one (one question) and **wait**. Do not pick a script to “be helpful.”

If `code:` is not Stata, **stop**. Do not invent an R runner here.

## Data-use rules

| Mode | What you may do |
|---|---|
| Individual-level data closed (`restricted`) | Do **not** invoke Stata on row-level real data. You may tell the authorised analyst which named `.do` to run, and you may fill sidecar fields from a log they already produced. |
| This project allows the assistant to use the named data (`agent-accessible`) | You may run locally, only on the data the policy names, from this machine. |

Do not read local path-config files that point at closed real data in order to complete a run.

## Find the Stata executable (do not assume a path)

Use the first that is set and exists:

1. `STATA_BIN` in the environment
2. `stata_bin.local.yml` in the paper folder (`stata_bin:` full path). That file is machine-only and gitignored.

If neither is set, **stop**. Ask them to put the full path to this computer’s Stata program in `stata_bin.local.yml` (copy the example in `templates/analysis/stata/`) or to set `STATA_BIN`. Do not guess `Program Files` or a Unix location.

This version is **Windows first**. On Windows, batch run is `/e do "path\to\file.do"` with working directory = the paper folder (`paper_root` in `layout.yml`, else the folder that contains `layout.yml`).

## Run

1. Record start time.
2. SHA-256 of the `.do` file if practical.
3. Create `02-scripts/logs/` (or the scripts path + `/logs`) if needed.
4. Run only that named file. Do not chain extra scripts. Do not start a second job in the background.
5. Keep the log where it was written (default: `02-scripts/logs/<stem>.log` if the do-file opened a log there; otherwise the Stata log next to the working directory).
6. If the log shows a Stata error (`r(#);`) or there is no log, **stop**. Leave the log. Do not edit the `.do` file, the plan, or the data to make the run succeed.
7. If the run finished, update the **existing** output sidecar (`templates/output-metadata.yml`) for the result this script writes. Default `status: provisional`. Do not mark `approved`.

Sidecar fields to set or update (same file, not a second provenance system):

- `produced_by` — the `.do` path
- `analysis_ref` — the agreed `A-NNN`
- `run_by` — who ran it (the authorised analyst when the assistant must not run)
- `stata_version` — from the log header if present
- `command` — the executable and arguments actually used
- `script_hash` — SHA-256 of the `.do` file
- `started_at` / `ended_at`
- `run_status` — `completed` or `failed`
- `log_path`

If no sidecar exists for the output, write one as **provisional**. Do not invent numbers in the manuscript.

## After a failed run

In chat: the log path, that the run failed, and that the analysis was not changed. Ask whether they want a **write analysis code** task (new chat, **Do T-NNN**) or to leave it. Wait.

## Must not

- Run if the analysis is not already agreed, or if no run-on-real-data task is assigned to this run
- Run more than one unnamed `.do` file
- Run against row-level real data when this paper’s rules close that data
- Assume a Stata install path
- Start a background or queued job
- Edit the `.do` file, the analysis plan, or the data to repair a failed run
- Mark the result `approved`
- Compile a paper, run Word, or start other assistants
