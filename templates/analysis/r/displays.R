# Manuscript figures (APA 7 in the paper). Source from an analysis script.
# Number and title belong in the Quarto file, not in the image.
# Poster or talk: do not use these helpers; larger type and an on-image title are fine.
# List: templates/analysis/manuscript-displays.md

theme_manuscript_ggplot <- function(base_size = 11) {
  if (!requireNamespace("ggplot2", quietly = TRUE)) {
    stop("Package ggplot2 is needed for theme_manuscript_ggplot().")
  }
  ggplot2::theme_classic(base_size = base_size, base_family = "sans") +
    ggplot2::theme(
      legend.position = "bottom",
      legend.background = ggplot2::element_rect(fill = "white", colour = NA),
      axis.title = ggplot2::element_text(size = base_size),
      axis.text = ggplot2::element_text(size = max(8, base_size - 1)),
      strip.background = ggplot2::element_blank(),
      strip.text = ggplot2::element_text(size = base_size)
    )
}

save_manuscript_figure <- function(plot, path, width = 6.5, height = 4, dpi = 300) {
  if (!requireNamespace("ggplot2", quietly = TRUE)) {
    stop("Package ggplot2 is needed for save_manuscript_figure().")
  }
  ggplot2::ggsave(
    filename = path,
    plot = plot,
    width = width,
    height = height,
    dpi = dpi,
    units = "in"
  )
  path
}
