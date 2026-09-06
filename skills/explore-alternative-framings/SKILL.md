---
name: explore-alternative-framings
description: Generate genuinely different interpretations or directions independently, then stop for the researcher to choose. Use when they say Explore alternative framings, Give me genuinely different interpretations, Diverge before synthesis, or Challenge the current framing. Not for routine editing or settled analyses.
license: MIT
compatibility: Requires a project filesystem. No Python or R required.
metadata:
  version: "0.1.0"
---

# Explore alternative framings

Optional. Use when they want genuinely different interpretations, not a smoother version of the current one.

Follow `policies/how-to-talk.md` if present. Say *intellectual anchor*, *genuinely different interpretations*, *researcher decision needed*. Do not say persona, homogenisation, or research-intent drift unless they used those words.

**This file is complete.** Do not search workshop files or the toy example to learn this skill.

## When not to use

Routine copy-edits, settled analyses, and technical tasks do not need this. If the evidence strongly supports one conclusion, say so; do not manufacture disagreement. Do not reward novelty for its own sake.

If they asked **Review the manuscript** and also asked for differentiated reviews, run this skill on the review question **before** combining findings.

## Read first

- The intellectual anchor in the overview, if written, and any linked framing memo
- The research problem and questions
- Relevant accepted decisions and approved results
- The specific claim, section, or decision they named

Do not treat the current manuscript wording as the only legitimate starting point. The anchor is context; at least one direction may challenge it. Departures must be visible. The original idea does not always win.

## Procedure

**Anchor → diverge → choose.** Diversity should be created before answers are exposed to one another and before synthesis begins.

1. Identify the question on which genuine variation is wanted.
2. Choose a **small** set of differentiated epistemic lenses for **this** question (typically three to five). Do not apply a fixed list mechanically.
3. Generate each alternative **independently**. Later alternatives must not merely revise the first. One agent, separated passes, is enough. If several agents are available: give each the common evidence and the anchor; do not show another agent’s answer during generation; compare only after all outputs are in. Different models are not independent confirmation.
4. Present the alternatives **separately**.
5. For each, state:
   - its central claim
   - what it preserves from the intellectual anchor
   - what it challenges or changes
   - what evidence it requires
   - its main risk or limitation
6. Compare only after all have been generated. Alternatives must differ in reasoning, estimand, assumptions, or implications — not merely wording. If two are stylistic variants, say so and drop the duplicate.
7. **Stop** for researcher selection before producing a synthesized framing when the choice would materially change the science.
8. Write nothing into the manuscript, analysis plan, or intellectual anchor in this run. If they want some alternatives kept, file **one contribution per alternative** (**Contribute to the project**, `type: interpretation`). Do not average them into one proposal. Do not fill the inbox unless they asked to retain them.

## Epistemic lenses (choose for the question)

Use functional lenses, **not** simulated identities or fictional demographic personas.

Examples: theoretical contribution; measurement and construct validity; alternative estimand; causal identification; rival explanation; critical or adversarial interpretation; domain transfer; practical implementation; connection to the researcher’s wider programme.

## After they choose

- A new or narrowed intellectual purpose is **researcher decision needed**. Do not rewrite the anchor here.
- A wording they accept for the paper is still a proposal until **Update the project record**.
- Agreement among several AI passes is not independent confirmation.

## Must not

- Invent evidence or treat draft numbers as approved results
- Use fictional demographic or cultural personas
- Synthesize a compromise framing before they have seen the separate alternatives
- Erase an inconvenient alternative without showing it
- Edit the manuscript, analysis plan, or intellectual anchor in this run
- Treat this as an audit of the research chain
