# Manuscript helpers. Read approved research result files only.
# Do not point this file at row-level data.

PATHS <- list(
  metadata = here::here("01-data/metadata"),
  outputs = here::here("05-outputs"),
  figures = here::here("05-outputs/figures"),
  tables = here::here("05-outputs/tables")
)

EM_DASH <- "\u2014"

read_result <- function(filename, dir = PATHS$metadata) {
  path <- file.path(dir, filename)
  if (!file.exists(path)) {
    path <- file.path(PATHS$outputs, filename)
  }
  if (!file.exists(path)) {
    stop(
      "Result file not found: ", filename,
      "\nExpected under 01-data/metadata or 05-outputs."
    )
  }
  if (grepl("\\.ya?ml$", filename, ignore.case = TRUE)) {
    if (!requireNamespace("yaml", quietly = TRUE)) {
      stop("Package yaml is needed to read ", filename)
    }
    obj <- yaml::read_yaml(path)
  } else {
    obj <- jsonlite::fromJSON(path, simplifyVector = FALSE)
  }
  obj
}

require_approved <- function(obj, label = "result file") {
  status <- obj$status
  if (is.null(status) || !identical(as.character(status), "approved")) {
    stop(
      label, " is not an approved result (status=",
      if (is.null(status)) "missing" else status,
      "). Do not cite it in the manuscript."
    )
  }
  if (identical(as.character(obj$source), "synthetic")) {
    stop(label, " is synthetic. Do not cite it as a study result.")
  }
  invisible(obj)
}

p_stars <- function(p) {
  if (is.null(p) || length(p) != 1L || is.na(p)) return("")
  if (p < 0.001) "***" else if (p < 0.01) "**" else if (p < 0.05) "*" else ""
}

format_p <- function(p) {
  if (is.null(p) || length(p) != 1L || is.na(p)) return("")
  if (p < 0.001) "<0.001" else sprintf("%.3f", p)
}

format_est_se <- function(estimate, se, digits = 3) {
  sprintf(
    paste0("%.", digits, "f (%.", digits, "f)"),
    as.numeric(estimate),
    as.numeric(se)
  )
}

format_est_se_p <- function(estimate, se, p, digits = 3) {
  paste0(format_est_se(estimate, se, digits), p_stars(p))
}

style_flextable <- function(ft) {
  flextable::theme_booktabs(ft) |>
    flextable::fontsize(size = 10, part = "all") |>
    flextable::padding(padding = 3, part = "all") |>
    flextable::align(align = "center", part = "header") |>
    flextable::align(j = 1, align = "left", part = "body") |>
    flextable::autofit()
}

figure_path <- function(filename) {
  path <- file.path(PATHS$figures, filename)
  if (!file.exists(path)) {
    stop("Figure not found: ", path, "\nRender it from an approved result first.")
  }
  path
}
