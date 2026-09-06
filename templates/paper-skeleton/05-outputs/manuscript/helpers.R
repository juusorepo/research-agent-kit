# Manuscript helpers. Read approved research result files only.
# Do not point this file at row-level data.
# Paths come from layout.yml (walk up from the working directory). Numbered
# defaults are used only if that file is missing.

layout_file <- function() {
  starts <- unique(stats::na.omit(c(
    tryCatch(normalizePath(getwd(), winslash = "/", mustWork = FALSE), error = function(e) NA_character_),
    tryCatch(here::here(), error = function(e) NA_character_)
  )))
  for (start in starts) {
    dir <- start
    for (i in seq_len(12)) {
      candidate <- file.path(dir, "layout.yml")
      if (file.exists(candidate)) {
        return(normalizePath(candidate, winslash = "/", mustWork = FALSE))
      }
      parent <- dirname(dir)
      if (identical(parent, dir)) break
      dir <- parent
    }
  }
  NULL
}

paper_slug <- function(layout) {
  papers <- layout$papers
  if (is.null(papers) || length(papers) < 1) {
    return("paper-1")
  }
  first <- papers[[1]]
  slug <- first$slug
  if (is.null(slug) || !nzchar(as.character(slug)[1])) slug <- first$id
  if (is.null(slug) || !nzchar(as.character(slug)[1])) "paper-1" else as.character(slug)[1]
}

resolve_layout_path <- function(root, layout, key, default) {
  raw <- NULL
  if (!is.null(layout) && !is.null(layout$paths)) {
    raw <- layout$paths[[key]]
  }
  if (is.null(raw) || !nzchar(as.character(raw)[1])) raw <- default
  raw <- gsub("{paper}", paper_slug(layout), as.character(raw)[1], fixed = TRUE)
  file.path(root, raw)
}

load_layout_paths <- function() {
  defaults <- list(
    metadata = "01-data/metadata",
    outputs = "05-outputs",
    figures = "05-outputs/figures",
    tables = "05-outputs/tables"
  )
  lf <- layout_file()
  if (is.null(lf)) {
    root <- tryCatch(here::here(), error = function(e) getwd())
    return(list(
      root = root,
      metadata = file.path(root, defaults$metadata),
      outputs = file.path(root, defaults$outputs),
      figures = file.path(root, defaults$figures),
      tables = file.path(root, defaults$tables)
    ))
  }
  if (!requireNamespace("yaml", quietly = TRUE)) {
    stop("Package yaml is needed to read layout.yml")
  }
  layout <- yaml::read_yaml(lf)
  root <- dirname(lf)
  outputs <- resolve_layout_path(root, layout, "outputs", defaults$outputs)
  paths <- layout$paths
  figures_key <- if (is.null(paths)) NULL else paths$outputs_figures
  tables_key <- if (is.null(paths)) NULL else paths$outputs_tables
  list(
    root = root,
    metadata = resolve_layout_path(root, layout, "metadata", defaults$metadata),
    outputs = outputs,
    figures = if (is.null(figures_key) || !nzchar(as.character(figures_key)[1])) {
      file.path(outputs, "figures")
    } else {
      resolve_layout_path(root, layout, "outputs_figures", file.path(defaults$outputs, "figures"))
    },
    tables = if (is.null(tables_key) || !nzchar(as.character(tables_key)[1])) {
      file.path(outputs, "tables")
    } else {
      resolve_layout_path(root, layout, "outputs_tables", file.path(defaults$outputs, "tables"))
    }
  )
}

PATHS <- load_layout_paths()

EM_DASH <- "\u2014"

read_result <- function(filename, dir = PATHS$metadata) {
  path <- file.path(dir, filename)
  if (!file.exists(path)) {
    path <- file.path(PATHS$outputs, filename)
  }
  if (!file.exists(path)) {
    stop(
      "Result file not found: ", filename,
      "\nLooked in layout.yml paths metadata and outputs."
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
  if (p < .001) "***" else if (p < .01) "**" else if (p < .05) "*" else ""
}

format_p <- function(p) {
  if (is.null(p) || length(p) != 1L || is.na(p)) return("")
  if (p < .001) return("< .001")
  sub("^0\\.", ".", sprintf("%.3f", as.numeric(p)))
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
  # APA 7 three-line table. Format cell text before calling this.
  themed <- if ("theme_apa" %in% getNamespaceExports("flextable")) {
    flextable::theme_apa(ft)
  } else {
    flextable::theme_booktabs(ft)
  }
  themed |>
    flextable::fontsize(size = 10, part = "all") |>
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
