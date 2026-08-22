# Local Stata run (optional)

Tool setup only. Research rules live in `skills/run-approved-stata-analysis/SKILL.md`. Do **not** copy this folder into a paper.

Windows first. One named `.do` file, in the foreground. Not a job queue.

## Configure the executable

Do not assume a path. Set **one** of:

- environment variable `STATA_BIN` — full path to this computer’s Stata program
- paper file `stata_bin.local.yml` (gitignored). Example: `templates/analysis/stata/stata_bin.local.yml.example`

## Run

From the **paper** folder:

```
powershell -File "<kit>\adapters\stata\run-stata.ps1" -DoFile "02-scripts\01_draft.do" -WorkDir "." -LogPath "02-scripts\logs\01_draft.log" -SidecarPath "05-outputs\tables\_dev\OUT-001.yml"
```

`-SidecarPath` must already exist. `-LogPath` is the expected log; the helper reports that exact path. If you omit it, the default is `<scripts>/logs/<stem>.log`.

The script prints `run_status`, `log_path`, `command`, `script_hash`, `started_at`, `ended_at`, `exit_code`, `stata_version`, and `stata_bin`, and writes those technical fields onto the existing sidecar. It does not change `status`, `approved_by`, or `approved_at`. A non-zero Stata exit is `run_status=failed` even if the log looks finished. On failure it keeps the log and exits non-zero.

## Must not

- Background or queued execution
- Guessing an install path
- Editing analysis code because a run failed
- Approving a result
- Word, paper compile, or a second provenance file
