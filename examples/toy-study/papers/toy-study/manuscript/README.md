# Quarto manuscript

This is the paper. A Google Docs copy for co-authors is a **review copy**. Accept small wording there, then sync back. Open comments go to the contributions inbox. Word comment ingest is not in this version.

## Approach

Numbers in the manuscript come from **approved** result files only (paths from `layout.yml`). The manuscript does not read row-level data.

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

From the folder that contains `layout.yml`:

```text
quarto render papers/toy-study/manuscript/paper.qmd
```

Edit `paper.qmd` for the text. Change folder names in `layout.yml`; `helpers.R` reads that file.
