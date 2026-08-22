# Stata analysis stub

Put `.do` files in the scripts path from `layout.yml`.

Write **draft** outputs with a sidecar metadata file (`templates/output-metadata.yml`). Do not mark them approved. Analysis reads processed data, not raw. If individual-level real data are closed to the assistant, develop against synthetic or development data only.

If a table or figure will appear in the **manuscript**, follow `templates/analysis/manuscript-displays.md` (paper copy if they added one, otherwise the kit). Stata how-to for that list is later work; the list still applies. Poster, talk, and `_dev/` pilots are the exceptions.

To run one agreed analysis on this machine, say **Run approved Stata analysis** (assigned task, kind of work **run on real data**). Configure this computer’s Stata path in `stata_bin.local.yml` (gitignored) or `STATA_BIN`. Do not assume an install path.

Copy `stata_bin.local.yml.example` to `stata_bin.local.yml` in the paper folder and fill the path.
