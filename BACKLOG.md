# Research Agent Kit — Backlog

This backlog contains ideas intentionally kept outside the minimal core. Items are grouped by function rather than implementation order.

## v0.1 additions — lightweight foundations

These should be included in the initial architecture because later features depend on them. Implement only the minimal data structures and workflow rules, not sophisticated automation.

### AI-use provenance and disclosure

Record **material AI contributions**, rather than attempting to identify which individual words were AI-generated.

A minimal AI-use event should be able to record:

* research stage;
* affected artifact;
* AI role, e.g. implementation, evaluation, drafting, co-ideation;
* whether the substantive idea originated with the researcher or AI;
* human review/decision;
* verification method.

Example uses:

* analysis code generated from a human-approved analysis plan;
* AI-generated methodological alternative considered by the researcher;
* AI-assisted interpretation that was substantially revised by the researcher;
* adversarial review of manuscript claims.

v0.1 should provide only:

* a minimal event schema;
* a place to store material AI-use events;
* a checkpoint rule for deciding when an event is worth recording.

Later versions can generate co-author summaries and journal-specific AI disclosures from this record.

### Epistemic-control monitoring

The workflow should notice when an AI interaction crosses from implementation into a research decision.

Minimal v0.1 distinction:

**Already agreed**
The relevant research decision already exists. The agent may implement it.

**Researcher decision needed**
The proposed action would materially alter design, measurement, analysis or interpretation. The agent may formulate the choice but must not silently adopt it.

The system should record consequential decision points so that later it is possible to establish:

* who proposed the change;
* who evaluated it;
* who made the decision;
* what evidence or reasoning supported it.

Future versions may develop richer risk levels or automatic monitoring, but v0.1 should keep this deliberately simple.

### Better artifact and evidence provenance

Every approved analysis result should have enough machine-readable metadata to answer:

* Which planned analysis does this belong to?
* Which script produced it?
* Was it produced from synthetic or real data?
* Who ran the real-data analysis?
* Who approved the result?
* When was it approved?

This should be stored with the output or in a machine-readable sidecar rather than relying primarily on a manually maintained artifact table.

Minimal relationship:

`analysis plan item → script → approved output`

Later versions can extend this to:

`approved output → table/figure → manuscript statement → scientific claim`

A human-readable evidence map should preferably be generated from this provenance rather than maintained independently.

---

# Quantitative research workflow

These are the first additions after v0.1 because they are required to use the framework productively in quantitative social-science papers.

## Quantitative research profile / Quarto

An optional profile for computational quantitative research rather than part of the universal core.

**Already in the kit:** start-project interview; `layout.yml`; numbered research folders; `06-docs` vs canonical `manuscript/`; share/gitignore; Quarto manuscript that reads **approved** result files only (APA format, `helpers.R`, no row-level data). Word and Stata are reserved.

This backlog item is the rest of the quantitative profile:

Potential components:

* `renv` for computational environment;
* `{targets}` where appropriate;
* analysis-script manifest;
* canonical / robustness / supplementary / parked analysis distinction;
* synthetic-data development workflow;
* disclosure-control checks for exported outputs.
* Word and Stata *toolchains* (beyond reserved folders)


Typical chain:

`analysis plan → script → real-data run → approved output → Quarto → table/figure/text`

JSON may be the default implementation, but the profile should support other suitable machine-readable formats.

## Full research-chain audit

Reusable agent skill for checking transitions across the research evidence chain.

Potential checks:

### Analysis plan ↔ code

* Was the agreed analysis implemented?
* Were sample definitions, reference groups and transformations preserved?
* Were additional analyses introduced without a documented decision?

### Code ↔ output

* Does the output actually derive from the stated code?
* Are results provisional or approved?
* Are synthetic and real results clearly distinguished?

### Output ↔ manuscript

* Are reported numbers correct?
* Are figures and tables linked to approved outputs?
* Are there manually typed numbers without provenance?

### Results ↔ scientific claims

* causal overreach;
* construct overreach;
* unsupported subgroup conclusions;
* discrepancy between statistical result and substantive claim;
* interpretations that exceed the study design.

Audit runs should be separate from the agent run that produced the work. A different model or verification mechanism can provide stronger independence but should not be mandatory for every audit.

---

# Collaboration and review

## Co-author manuscript review workflow

Keep the canonical manuscript in the project, while letting collaborators use familiar review interfaces.

Likely workflow:

`manuscript.qmd`
→ review snapshot
→ Google Docs or Word
→ co-author comments/suggestions
→ structured review issues
→ agent-assisted triage
→ researcher decisions
→ revised canonical manuscript

The workflow should support:

* extracting comments into structured issues;
* distinguishing editorial comments from methodological/scientific ones;
* linking comments to the analysis plan, research decisions and outputs;
* agent-proposed responses and revisions;
* human approval of substantive changes;
* semantic comparison between review rounds;
* tracking which comments have been addressed;
* generating a short change summary for co-authors.

Google Docs may become the preferred internal review surface because comments and replies are more accessible programmatically, while Word remains important for journal exchange.

## Journal peer-review workflow

Generalise the co-author workflow to journal reviews:

`reviewer comment → issue → evidence → required action → analysis/manuscript change → response`

Potential functionality:

* split long reviews into atomic issues;
* classify comments;
* detect when new analysis is required;
* link reviewer requests to existing project decisions;
* track resulting code/output changes;
* verify that the response letter accurately describes what was changed;
* preserve review-round history.

## Shared project contributions

Minimal v0.1 is in the kit: `contributions/` inbox, `contribute-to-project` (proposal only), `consolidate-contributions` (recommend; lead researcher accepts).

Later: richer automatic classification, contradiction detection, and multi-reviewer triage.

Allow collaborators to use their preferred AI systems while contributing to a shared research record.

Potential later model:

`co-author + agent → proposed contribution → project review → canonical record`

---

# Research memory and project continuity

## Richer research-memory consolidation

Extend the v0.1 project-update mechanism with:

* candidate-memory inbox;
* automatic classification into decision / task / context / result / discard;
* stale-state detection;
* contradiction detection;
* periodic project-state consolidation;
* rebuilding `STATUS.md` from authoritative sources;
* retrieval of relevant older decisions when needed.

## Research notes / lab notebook

Minimal v0.1: `notes/` exists; assistants must not load it by default.

Later: optional chronological record for exploratory work that does not yet belong in canonical project state.

Potential contents:

* preliminary observations;
* unsuccessful approaches;
* exploratory analyses;
* questions to revisit;
* methodological reflections.

This should remain selectively retrieved rather than automatically loaded into every agent session.

## Project-memory querying

Minimal v0.1: retrieval order lives in `understand-research-project` (overview → status → plan → decision index → relevant notes → contributions if needed → `notes/` / Git only if necessary).

Later agent skill for questions such as:

* Why did we make this methodological choice?
* Has this robustness analysis already been run?
* Which decision governs this variable coding?
* What remains unresolved?
* When and why did the primary analysis change?

Retrieval order should favour current authoritative state before historical notes.

---

# AI provenance, disclosure and governance

## Disclosure generator

Transform structured AI-use provenance into:

* internal team summary;
* manuscript methods/disclosure statement;
* journal-specific disclosure;
* funding/institutional reporting where required.

Avoid claims such as percentages of AI-written text.

## Co-author AI visibility

Provide collaborators with a concise view of AI involvement by research stage, for example:

* conceptualisation;
* methodology;
* coding;
* analysis;
* interpretation;
* writing;
* verification.

This should distinguish AI execution from AI-originated scientific ideas.

## Richer epistemic-control safeguards

Potential future development beyond the simple v0.1 decision point:

* detect AI-originated methodological changes;
* detect agent proposing, implementing and interpreting the same unapproved method;
* require stronger verification for higher-risk transitions;
* flag absence of independent human reasoning;
* produce an epistemic-control summary for a completed project.

---

# Agent skills

Potential reusable skills beyond the v0.1 core:

* `audit-research-chain`
* `process-review-round`
* `prepare-coauthor-review`
* `generate-ai-disclosure`
* `create-synthetic-data`
* `inspect-codebook`
* `check-results-claims`
* `adversarial-peer-review`
* `check-reproducibility`

Skills should remain agent-agnostic procedures. Project facts belong in project files, while external service integrations belong in adapters or MCP tools.

---

# Evaluation and quality assurance

## Golden skill evals

For each important skill, maintain known test cases with expected behaviour.

Examples:

* detect unsupported causal claim;
* detect silent change in reference category;
* refuse to treat synthetic output as a real result;
* identify undocumented specification deviation;
* avoid flagging an explicitly accepted methodological decision.

## Regression testing

Run the same eval cases after:

* changing a skill;
* changing a policy;
* upgrading the Research Agent Kit;
* changing the underlying AI model.

## Cross-model comparisons

Compare the same skill across:

* Claude;
* OpenAI models;
* Gemini;
* local models.

Measure important failures rather than generic subjective quality.

## Langfuse / observability

Potential later infrastructure for:

* traces;
* eval experiments;
* model comparisons;
* failure analysis;
* skill-version comparisons.

This is infrastructure for maintaining shared research agents/skills, not a prerequisite for researchers using the workflow.

---

# Integrations and infrastructure

## MCP integrations

Potential external research tools:

* bibliographic and literature services;
* Scite;
* DMP Analyser;
* GitHub;
* cloud storage;
* Google Docs;
* institutional research infrastructure.

MCP should provide capabilities and resources. Research methodology should remain in Agent Skills and project rules.

## Secure/institutional execution

Adapters for:

* university AI services;
* secure compute environments;
* register-data environments;
* controlled runners;
* allowlisted data export.

## Local/private AI profile

Potential support for:

* Ollama;
* LM Studio;
* local coding agents;
* local inference APIs;
* private codebook/document processing;
* comparison of local vs institutional vs commercial AI.

---

# Domain-specific profiles

## Quantitative social science

Potential reusable guidance for:

* survey data;
* multilevel models;
* longitudinal analysis;
* weighting;
* subgroup comparisons;
* missingness;
* sensitivity analyses.

## Register research

Potential additions for:

* cohort construction;
* register linkage;
* event histories;
* disclosure control;
* synthetic development datasets;
* safe export contracts;
* secure execution.

These should extend the generic Research Agent Kit rather than become assumptions of the core framework.

---

# Higher-level interfaces

## Continuum

Potential orchestration/interface layer over:

* shared project record;
* tasks;
* decisions;
* skills;
* provenance;
* AI-use events;
* review rounds;
* different AI agents.

The canonical research record should remain portable files rather than becoming dependent on Continuum.

## Course Assistant

Teaching layer using the same workflow principles:

* guide participants through project setup;
* surface researcher decision points;
* demonstrate safe delegation;
* compare agents;
* collect anonymised workflow failures;
* turn suitable failures into future eval cases.
