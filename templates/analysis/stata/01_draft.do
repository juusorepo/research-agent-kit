* Draft analysis stub. When individual-level real data are closed to the
* assistant, develop only against synthetic or development data.
* Do not mark outputs approved from this file.
* Run with working directory = the paper folder (the folder with layout.yml).

capture mkdir "02-scripts/logs"
capture mkdir "05-outputs/tables/_dev"
capture log close _all
log using "02-scripts/logs/01_draft.log", replace text

* Analysis reads processed data, not raw originals.
* local processed "01-data/processed"

file open sidecar using "05-outputs/tables/_dev/OUT-001.yml", write replace
file write sidecar "id: OUT-001" _n
file write sidecar "status: provisional" _n
file write sidecar "source: synthetic" _n
file write sidecar "analysis_ref: A-001" _n
file write sidecar "produced_by: 02-scripts/01_draft.do" _n
file write sidecar "run_by:" _n
file write sidecar "approved_by:" _n
file write sidecar "approved_at:" _n
file write sidecar "privacy_control: project-policy" _n
file write sidecar "run_status: completed" _n
file write sidecar "log_path: 02-scripts/logs/01_draft.log" _n
file close sidecar

log close
