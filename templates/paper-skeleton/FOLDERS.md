# Folders

This is a research project folder. First-level folders are numbered. Assistant files (`AGENTS.md`, `layout.yml`, `policies/`) stay in the background.

| Folder | What goes here |
|---|---|
| `01-data/raw` | Unmodified original files. Do not overwrite. Mixed formats are fine. |
| `01-data/processed` | Conversion and cleaning outputs. Analysis reads **only** from here. |
| `01-data/metadata` | Codebooks, dictionaries, AI-safe summaries |
| `02-scripts` | Analysis scripts |
| `03-supplementary` | Extra material for sharing |
| `04-notebooks` | Notebooks and working notes |
| `05-outputs/figures` | Graphs (pilots under `_dev/`) |
| `05-outputs/tables` | Result tables (pilots under `_dev/`) |
| `05-outputs/manuscript` | The paper you are writing (plus `review-copy.yml` for a Google Docs snapshot) |
| `06-docs` | Preregistration, ethics, extra context (does not override the analysis plan) |
| `07-record` | Research decision notes, collaborator inbox, working notes, audit reports |
| `99-archive` | Old versions. If delete fails, put discards in `99-archive/quarantine/`. |

Project overview, analysis plan, status, and tasks sit at the top of a one-paper folder. If this folder holds several papers, each paper’s record is under `07-record/<name>/` and its manuscript under `05-outputs/<name>/manuscript`. See `MEMORY.md` for how those files relate.
