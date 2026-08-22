# Tables and figures in the manuscript

Use this list when a table or figure will appear in the **paper**. It is not for a poster or a talk.

Do not copy the APA manual into the project. The official pages are the source:

- [Tables and figures](https://apastyle.apa.org/style-grammar-guidelines/tables-figures)
- [Table setup](https://apastyle.apa.org/style-grammar-guidelines/tables-figures/tables)
- [Figure setup](https://apastyle.apa.org/style-grammar-guidelines/tables-figures/figures)
- [Accessible use of colour](https://apastyle.apa.org/style-grammar-guidelines/tables-figures/colors)

What to *report* (sample size, confidence intervals, effect sizes) is a different matter — Journal Article Reporting Standards, not this file.

A paper may override this file by adding the same path here. Otherwise follow the kit.

## Destination

| Destination | Follow this list? |
|---|---|
| Manuscript (default) | Yes |
| Poster or talk | No. Larger type, titles on the image, and more colour are fine. Number and title may be omitted. |
| Pilot under `_dev/` | No. Do not polish a throwaway to manuscript rules. |

If destination is unclear, ask once (default: manuscript) and wait.

## Shared setup (tables and figures)

- Mention it in the text by number before it appears (*Table 1*, *Figure 2*). Do not say “the table above.”
- Number in the order first mentioned. Table numbers and figure numbers are separate sequences.
- **Number** on its own line, bold (Table 1 / Figure 1).
- **Title** on the next line: italic, title case, brief, descriptive. No extra period at the end.
- Number and title live in the **manuscript** (Quarto caption / apaquarto), not burned into a PNG or a spreadsheet screenshot.
- **Note** below only as needed, left-aligned, starting with *Note.* Three kinds, in this order when more than one is needed:
  1. General — abbreviations, the sample, copyright if the display is reprinted or adapted
  2. Specific — superscript letters pointing at a cell or row
  3. Probability — if the display uses asterisks, say what they mean (`*p < .05`. `**p < .01`. `***p < .001`.)
- A reader should understand the display from the title, body or image, legend, and notes. Do not duplicate the whole display in the Results text.

## Tables

- No vertical lines. No box around every cell.
- Horizontal lines only where they help: top of the table, under the column headings, bottom of the table. A line above a totals row is allowed.
- Every column has a heading. The stub column (left) is a label, not a data column without a heading.
- Align the stub left. Align numbers so they can be compared (same decimal places in a column).
- Format the cells *before* applying a theme. Do not let a theme round *p* values to two decimals.
- For *p*, *r*, and other values that cannot exceed 1, omit the zero before the decimal (`p < .001`, not `p < 0.001`).

## Figures

- The image is the graph. Axes have labels and units. Lines are sharp. Type in the image is a simple sans-serif, about 8–14 points.
- Legend (if needed) sits inside the figure, title case.
- Do not use 3-D effects or decoration that is not data.
- Colour is not the only way to tell series apart (also use linetype, shape, or direct labels). Contrast should still work in greyscale. See APA’s colour page above.
- Save a manuscript figure as a file the paper can include. Do not put “Figure 1” or the title in the image.

## How this list is used

- **Writing analysis code** — follow it when the output will be cited in the paper. Language how-to: `templates/analysis/r/` (R) or `templates/analysis/stata/` (Stata how-to later; the list still applies).
- **Review the manuscript** — editorial check against this list. Findings go to the inbox. Not an audit.
- **Audit the research chain** — check whether the display can be read as evidence (numbers, units, notes that match the test, caption vs claim). Do not fail the two audit statuses for missing italics or an extra vertical line.
