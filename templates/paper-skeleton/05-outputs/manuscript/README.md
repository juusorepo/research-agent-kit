# Quarto manuscript

This is the paper. A Google Docs copy for co-authors is a **review copy**. Accept small wording there, then sync back. Open comments go to the contributions inbox. Drive syncing this folder does not merge Doc edits into Quarto. Word comment ingest is not in this version.

## Source files

`paper.qmd` is a thin shell: YAML (title, abstract, authors), the setup chunk, `{{< include >}}` lines, and the References heading. Each section lives in one `_*.qmd` file next to it.

That is the whole paper. There is no second copy of Introduction in a `.md` file, and no script that pastes the parts into `paper.qmd`.

Default sections:

- `_intro.qmd`
- `_method.qmd`
- `_results.qmd`
- `_discussion.qmd`

The underscore prefix stops Quarto from rendering a part as its own document. Included files must not have their own YAML.

**Edit the section file.** Title and abstract stay in the YAML in `paper.qmd`. If this paper is still one file with the sections inside `paper.qmd`, edit that file — do not split it unless they asked.

**One copy.** If a part file becomes an include, archive or delete the old `.md`. Do not leave both. Convert or archive — never both.

**Do not assemble.** Do not write a script that rebuilds `paper.qmd` from parts. Edits in the assembled file would be overwritten on the next run, and byte-identity checks on “frozen” regions fail as soon as a legitimate edit lands. Quarto already composes the paper at render.

To add a section (a theoretical framework, appendices): create `_framework.qmd` with no YAML, put its heading in that file, and add `{{< include _framework.qmd >}}` in `paper.qmd` in the right order.

## Paths, code, and cross-references

Relative paths inside an include (figures, `references.bib`, helpers) resolve against the folder that contains `paper.qmd`, not against the include’s own folder. Keep the `_*.qmd` files in that same folder. Chunk labels must be unique across all includes. Inline `r ` calls and cross-references (`@tbl-…`, `@fig-…`) belong to the main document after include; they should work across section files. Confirm on first render rather than assuming.

## Approach

Numbers in the manuscript come from **approved** result files only (paths from `layout.yml`: metadata and outputs). The manuscript does not read row-level data. Figures are files already written to the figures path in `layout.yml`.

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

From the **project** folder (the one that contains `layout.yml`):

```text
quarto render 05-outputs/manuscript/paper.qmd
```

That writes a Word file next to the paper (`paper.docx` with the apaquarto Word format). For co-authors, say **Prepare a review copy**. Quarto has no Google Docs output: the assistant may render Word as a conversion step (enough to say the phrase; no second yes) and import a **native Google Doc** into this folder. Reuse a current `paper.docx` already on Drive rather than uploading it twice. Temporary Word files used only for conversion are deleted after the Doc checks out. Co-authors should only need the Doc. Keep `paper.docx` when you need it for **Audit APA presentation** or a journal submission.

Drive syncing this folder does not merge Google Docs edits into Quarto. Accept small wording in the Doc, then **Sync the review copy**. Open comments: **Ingest review comments**. To share a Word file on OneDrive instead of a Google Doc, set `provider: word` in `review-copy.yml` — Sync and Ingest do not run on that channel.

To **Audit APA presentation**, export a PDF from that same Word file (File → Save As → PDF, or Print to PDF). Say the phrase in the **paper** folder. Do not use a Google Docs review copy as the object of that check.

## Bibliography

`references.bib` is their export (Zotero or another manager). Prefer Better BibTeX so keys stay stable. The assistant does not invent records or keys. If the file is empty, they export or attach it first; then citations in the Quarto file use those keys (`[@key]`). After they overwrite the `.bib`, ask the assistant to update any `[@…]` that no longer match.

Edit the `_*.qmd` file for that section. Change folder names in `layout.yml`; `helpers.R` reads that file.

## Convert a single-file paper

Only if they asked. **Adjust this project to the new kit version** does not do this. Science files stay as they are.

1. Move each section’s text from `paper.qmd` into `_intro.qmd` (and the others). No YAML in those files.
2. Leave YAML, setup, include lines, and `# References` in `paper.qmd`.
3. If a parallel `.md` part file exists, move it to `99-archive/` and remove it from the manuscript folder.
4. Render once.
5. Do not add an assemble script.
