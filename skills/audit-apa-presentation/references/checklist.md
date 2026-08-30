# APA presentation — house checklist

Observable items only. Do not paste the Publication Manual into the report.

## Authority

1. Journal author instructions **if they attached them**
2. This house list
3. APA 7 only when you are sure of the rule

Uncertain rule → severity `note`, not ISSUES.

Table and figure *construction* for the paper (call-outs, notes, lines, colour) is also in `templates/analysis/manuscript-displays.md` (paper file if they added it, otherwise the kit). Use that list here for the **rendered** Word/PDF, not for a poster.

Do not require a running head unless the journal file says so. `floatsintext: true` is a journal or house choice, not an automatic APA fail.

## Render integrity (source → Word/PDF)

- Every table and figure in the source appears in Word and in the PDF.
- Call-outs in the text resolve to those displays.
- No raw chunk debris (unevaluated code, leftover labels, broken cross-references).
- If the PDF is older than the source and they disagree, the finding is a **stale render**, not a live source error.
- ORCID: the PDF may show an icon while Word shows alt-text if a converter is missing (common on Windows). Check both, or mark Word-on-screen **NOT VERIFIED**. A missing icon is a **render** finding, not a missing ORCID in the YAML.

## APA tables

- Not clipped at the page or column edge. Clipping is **critical**.
- Title and number are distinct (number, then title).
- Limited gridlines (three-line / booktabs-like). No full cell grid.
- *Note.* where stars, abbreviations, or *n* need it.
- Wide tables: split, stack, or fit to the text column (about 6.5 in). Side-by-side panels that run off the page are ISSUES.

## APA figures

- Present in Word and PDF.
- Caption usable (not truncated so the figure cannot be identified).
- Colour is not the only encoding if that can be seen (linetype, shape, or labels as well).

## APA manuscript (title, headings, text, references)

- Title page: no leftover placeholder affiliation or author line that they already replaced in the source (if it remains in the PDF, that is render integrity, not a new YAML error).
- Headings: an empty `# Discussion` after an appendix heading can be promoted to a fake “Appendix B”. Appendices should use a descriptive level-1 heading with `{#apx-…}`.
- Empty Discussion (or other promised section) with no agreed text: **researcher decision needed** if they have not agreed to write it yet — not a silent layout patch.
- Bibliography: keys cited in the source exist in `.bib`. Incomplete records are findings; do not invent fields.
- TeX-style capitals in `.bib` (for example `{\TH}` for Þ) often drop the capital in Word. Prefer Unicode in the `.bib` file.
