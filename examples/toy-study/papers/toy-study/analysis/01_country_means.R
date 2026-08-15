# Synthetic development only. Do not point this script at real row-level data.

dev <- read.csv("dev_data.csv", stringsAsFactors = FALSE)
means <- aggregate(wellbeing ~ country, data = dev, FUN = mean)

out_dir <- Sys.getenv("RAK_OUTPUT_DIR", unset = "../outputs")
dir.create(out_dir, showWarnings = FALSE, recursive = TRUE)

lines <- c(
  "id: OUT-001",
  "status: provisional",
  "source: synthetic",
  "analysis_ref: A-001",
  "produced_by: 01_country_means.R",
  "run_by:",
  "approved_by:",
  "approved_at:",
  "privacy_control: project-policy",
  "note: country means from synthetic development file"
)
writeLines(lines, file.path(out_dir, "OUT-001.yml"))
