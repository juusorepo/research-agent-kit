# Data-use rules

Copy this file into a paper and edit it. Installed copies win over the kit default.

```yaml
data_access: restricted
privacy_control: project-policy
disclosure_min_n: 10
approval_requires_real: true
```

## Data-access mode

| Value | Meaning |
|---|---|
| `restricted` | Agents must not read or run against row-level real data. An authorised analyst runs real data (usually outside this folder). Agents use codebooks, synthetic or development data, and AI-safe research outputs. |
| `agent-accessible` | This project allows the agent to read and/or run the permitted data named below. |

**This template defaults to `restricted`.** Change the field above if the data are public or otherwise allowed.

## What agents may use (restricted default)

- Codebooks and variable dictionaries in the project
- Synthetic or development data the project has placed for that purpose
- AI-safe research outputs (`status: provisional` or `approved`)
- The shared research record (overview, analysis plan, decision notes)

## What agents must not use (restricted default)

- Row-level real data
- Local path-config files that point at restricted data
- Local-only full extracts
- Identifiers or labels this project forbids (edit the list below)

## Identifier and small-cell rules (edit for this study)

These are **examples**. Replace them.

- Do not include person names, exact dates of birth, or row-level IDs in any shared file.
- Suppress or band cells with n below `disclosure_min_n`.
- Institution or school names: **forbidden in this default template**. A country study may allow country names — change this paragraph if so.

## Share boundary

**Typically shareable with co-authors:** project overview, analysis plan, research decision notes, scripts, AI-safe result files, the canonical manuscript, and `docs/` that contain no restricted extracts.

**Stay on the authorised analyst’s machine:** row-level real data, local path config, local-only full extracts, secrets.

The project `.gitignore` implements the common cases. This section is the rule.

`restricted` is a **rule** the assistant must follow. It is not a technical lock on the files. Keep row-level real data **outside** this folder and gitignored. A cloud assistant can still send **project text** (overview, analysis plan, drafts) to a vendor. Use a tool your organisation allows. See `policies/ai-policy.md`.

## Running analysis on this machine

A local Stata run uses the same `data_access` rule as any other run.

- Closed individual-level data (`restricted`): the assistant must not invoke Stata on row-level real data. The authorised analyst may run a named `.do` file on their machine.
- Permitted data (`agent-accessible`): the assistant may run locally only on the data named in this file.

The path to this computer’s Stata program is machine config (`stata_bin.local.yml` or `STATA_BIN`). It is not a data path. Do not commit it. Do not put restricted data locations in committed `.do` files.

## Raw and processed

`01-data/raw` holds original files and is not overwritten. Conversion and cleaning write to `01-data/processed`. Analysis reads processed only.

## Keys

Do not put keys in chat or in files you commit. Load them at run time from the environment (`.env` / `.Renviron`). Keep them in `secrets/` or equivalent, which is gitignored.

## Approving a result

A result file may be marked `approved` only when:

1. `analysis_ref` points at an agreed analysis in `ANALYSIS_PLAN.md`
2. A sidecar metadata file sits next to the result (`status` then becomes `approved`)
3. The run followed this file’s `data_access` mode
4. If `source: real`, `run_by` names the authorised analyst
5. If `approval_requires_real: true`, `source` must be `real` (synthetic stays a draft output)

Approval is not an independent audit.
