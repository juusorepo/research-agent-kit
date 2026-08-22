# R analysis

Put scripts in the `scripts` path from `layout.yml`.

Write **draft** outputs with a sidecar metadata file (`templates/output-metadata.yml`). Do not mark them approved. Analysis reads processed data, not raw. If `data_access` is `restricted`, develop against synthetic or development data only.

## Tables and figures

If the file will appear in the **manuscript**, follow `templates/analysis/manuscript-displays.md` (paper copy if they added one, otherwise the kit). That list is APA 7 for the paper. It is not a poster style.

Default destination is the manuscript. Poster, talk, and `_dev/` pilots are the exceptions.

**Content first, then appearance.** Build a data frame with the numbers already rounded and labelled. Then style. Do not let a theme silently change what the cells say.

### Manuscript tables

Compose them in the Quarto file from an **approved** result, with `style_flextable()` in `helpers.R` (`flextable::theme_apa()` when available). The table number and title are the chunk caption (apaquarto), not part of the flextable.

### Manuscript figures

Use `displays.R` in this folder (`theme_manuscript_ggplot()`, `save_manuscript_figure()`). Save to the figures path in `layout.yml`. Leave `labs(title = …)` empty — the paper supplies Figure N and the title. Encode series with linetype or shape as well as colour.

### Poster or talk

Larger type and a title on the image are fine. Do not force three-line tables or 11-pt axes.
