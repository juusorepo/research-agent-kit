# Quarto manuscript

This is the paper. Google Docs or Word copies sent to co-authors are review snapshots.

## Approach

Numbers in the manuscript come from **approved** result files only (paths from `layout.yml`: metadata and outputs). The manuscript does not read row-level data. Figures are files already written to the figures path in `layout.yml`.

Typical chain:

`agreed analysis → script → real-data run → approved result → this Quarto file → table, figure, or sentence`

If a result is still a draft, or was produced only from synthetic data, do not cite it here.

## Once on this computer

The template uses the [apaquarto](https://github.com/wjschne/apaquarto) format (Word and HTML). From the project folder:

```text
quarto add wjschne/apaquarto
```

Packages used in `helpers.R`: `here`, `yaml`, `jsonlite`, `dplyr`, `flextable`, `knitr`.

## Render

From the **project** folder (the one that contains `layout.yml`):

```text
quarto render 05-outputs/manuscript/paper.qmd
```

Edit `paper.qmd` for the text. Change folder names in `layout.yml`; `helpers.R` reads that file.
