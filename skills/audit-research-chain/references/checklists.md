# Audit checklists

Use the scopes they asked for. A full audit uses the four links, then the cross-chain paragraph. Do **not** add data construction unless they asked.

Distinguish a **substantive** deviation from a harmless implementation detail (file names, comment wording, equivalent syntax).

Keep **two gates**. Do not flatten them into one overall PASS.

## What is currently agreed (always)

Before the links, establish what you are checking against:

- agreed analysis plan items
- accepted research decision notes (and their index)

If those conflict with each other, or with STATUS or the task list about whether a choice is already accepted, record a finding. Ask them in the numbered questions. Do not resolve it in the report.

Do not treat STATUS, working notes, or old audit reports as what is agreed. Do not treat the overview Data section as what was agreed to analyse or as an approved result. Do not turn a full audit into a documentation tidy-up. Skip stale wording that does not change the scientific target.

## Gate 1 — numbers / reproducibility

Do code, outputs, tables, and manuscript agree?

Passing this gate does not answer Gate 2.

### Analysis plan ↔ code

Does implementation match the agreed analysis?

Check, where the plan states them: sample or population; outcome; exposure or predictor; reference group; transformations; covariates; interactions; estimand or contrast; model family; clustering or weights; missing-data handling; planned subgroups or robustness analyses.

Look especially for:

- an agreed item not implemented
- implementation that differs materially from the plan
- extra analyses with no agreed plan item
- coding or measurement choices that should have triggered a research decision
- obsolete code still treated as the analysis

Harmless: comments, equivalent function names, output path wiring — unless they change the scientific meaning.

### Code ↔ output

Can this research output legitimately be attributed to the stated implementation?

Use the project’s output metadata (`id`, `status`, `source`, `analysis_ref`, `produced_by`, `run_by`, `approved_by`, `approved_at`, privacy fields if present).

Look especially for:

- synthetic or development results presented as real
- a draft output (`status: provisional`) treated as approved
- a result file with no sidecar metadata
- analysis inputs pointing at raw data (conversion may read raw; it must write processed)
- `analysis_ref` pointing at the wrong or missing plan item
- `produced_by` pointing at a script that does not implement that analysis
- unexplained numbers (no metadata)
- stale output after the code changed in a way that would change the result
- missing provenance so the link cannot be checked

If you cannot run the code, say what file metadata can and cannot establish. Do not invent a PASS.

### Output ↔ manuscript

Does the manuscript accurately use **approved** research outputs?

Look especially for:

- numbers that differ from the approved file
- numbers with no identifiable approved source
- figures or tables based on draft or stale outputs
- labels or reference groups that do not match the output
- confidence intervals, p-values, sample sizes, units, scales, or signs reported incorrectly
- text describing a different analysis from the one that produced the result

Do not require a particular manuscript or output format. Use whatever provenance this paper has. If machine-linked citations exist, use them. If they do not, audit as far as possible and state the limit.

Review copies (Google Docs, emailed Word) are snapshots. The canonical manuscript is `paths.manuscript`.

## Gate 2 — estimand / claim validity

Does the design and evidence support what is claimed?

### Results ↔ scientific claims

This is claim calibration, not copy-editing. Check Results, Discussion, Abstract, title, conclusions, and table or figure captions.

Look especially for:

- causal language the design does not support
- construct overreach
- population or generalisation overreach
- unsupported subgroup claims
- treating a non-significant result as proof of no effect
- claiming a difference between groups because one is significant and the other is not
- conclusions that ignore the reported uncertainty
- exploratory or draft analyses presented as settled
- interpretation that exceeds the estimand
- wording that overstates or understates the magnitude
- statements contradicted by the reported result

Do not enforce style preferences. Focus on scientific meaning and evidential support.

Matching numbers on Gate 1 never implies a pass here.

## Data construction (opt-in only)

Run this **only** if they asked to audit data construction. Do not add it to an ordinary full audit or to a descriptive project that did not ask.

Trace **one** material central claim: manuscript or table → result file → analysis code → processed analysis data → raw source. Name the claim in the report. Stop at files this paper’s data-use rules allow. If those rules close row-level real data, that part of the chain is **NOT VERIFIED** — not a pass.

Look especially for mechanical artefacts:

- merges (match rates; unmatched cases that differ systematically)
- denominators (shared denominator; residual or complement; parts that sum to one)
- transformations that change the scientific meaning
- sample restrictions that do not match the claimed sample
- the same source building both exposure/treatment and outcome
- selection into the analysis file
- mismatch between the observed measure and the claimed construct
- unit of observation that is not consistent through the build
- coverage or collection breaks that still appear in a table or figure

Diagnose only. Do not rebuild data or rewrite analysis code in this run.

Findings here may affect Gate 2. They do not turn a Gate 1 pass into an overall pass.

## Across the chain (full audit only)

Ask whether a later stage inherited an earlier problem, for example:

- the plan names one outcome, code uses a modified scale, the output follows the code, the manuscript reports the original construct
- an extra analysis was never agreed but became the headline result
- code changed after the approved output was produced
- the manuscript copies a number that still came from code that does not match the plan
