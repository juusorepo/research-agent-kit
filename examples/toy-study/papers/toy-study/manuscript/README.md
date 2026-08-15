# Quarto manuscript

This is the paper. Google Docs or Word copies sent to co-authors are review snapshots.

## Approach

Numbers in the manuscript come from **approved** result files only (`01-data/metadata` or `05-outputs`). The manuscript does not read row-level data. Figures are files already written to `05-outputs/figures`.

Typical chain:

`agreed analysis → script → real-data run → approved result → this Quarto file → table, figure, or sentence`

If a result is still a draft, or was produced only from synthetic data, do not cite it here.

## Once on this computer

The template uses the [apaquarto](https://github.com/wjschne/apaquarto) format (Word and HTML). From the project folder:

```text
quarto add wjschne/apaquarto
```

Packages used in `helpers.R`: `here`, `jsonlite`, `dplyr`, `flextable`, `knitr`.

## Render

From the **project** folder (so `here::here()` finds `01-data` and `05-outputs`):

```text
quarto render manuscript/paper.qmd
```

Edit `paper.qmd` for the text. Edit `helpers.R` only if your folder map differs from `01-data` / `05-outputs`.
