# Quarto manuscript

This is the paper. A Google Docs copy for co-authors is a **review copy**. Accept small wording there, then sync back. Open comments go to the contributions inbox. Word comment ingest is not in this version.

## Approach

Numbers in the manuscript come from **approved** result files only (paths from `layout.yml`). The manuscript does not read row-level data.

Typical chain:

`agreed analysis → script → real-data run → approved result → this Quarto file → table, figure, or sentence`

If a result is still a draft, or was produced only from synthetic data, do not cite it here.

Tables and figures in this file follow `templates/analysis/manuscript-displays.md` (APA 7 for the paper). Number and title are the chunk caption, not part of the image. Poster and talk displays are a different destination.

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

That writes a Word file next to the paper (`paper.docx` with the apaquarto Word format). For co-authors, render that Word file first, then say **Prepare a review copy**. The assistant uploads it as a Google Doc; it does not rebuild the paper unless you ask.

To **Audit APA presentation**, export a PDF from that same Word file (File → Save As → PDF, or Print to PDF). Say the phrase in the **paper** folder. Do not use a Google Docs review copy as the object of that check.

## Bibliography

`references.bib` is their export (Zotero or another manager). Prefer Better BibTeX so keys stay stable. The assistant does not invent records or keys. If the file is empty, they export or attach it first; then citations in the Quarto file use those keys (`[@key]`). After they overwrite the `.bib`, ask the assistant to update any `[@…]` that no longer match.

Edit `paper.qmd` for the text. Change folder names in `layout.yml`; `helpers.R` reads that file.
