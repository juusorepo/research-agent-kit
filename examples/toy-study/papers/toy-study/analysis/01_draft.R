# Draft analysis stub. When data_access is restricted, develop only against
# synthetic or development data. Do not mark outputs approved from this file.

out_dir <- Sys.getenv("RAK_OUTPUT_DIR", unset = "outputs")
dir.create(out_dir, showWarnings = FALSE, recursive = TRUE)

writeLines(
  paste(
    "id: OUT-001",
    "status: provisional",
    "source: synthetic",
    "analysis_ref: A-001",
    "produced_by: 01_draft.R",
    "run_by:",
    "approved_by:",
    "approved_at:",
    "privacy_control: project-policy",
    sep = "\n"
  ),
  file.path(out_dir, "OUT-001.yml")
)
