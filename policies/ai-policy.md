# How this kit treats AI in research

This file is the kit’s clarifying note. It does **not** replace national or institutional rules. Using the kit is not an ethics review and not a stamp of good scientific practice.

A paper may add the same path here to override this default. Otherwise follow the kit copy.

How the workflow is built is in `DESIGN_PRINCIPLES.md`.

## What we follow

The kit is meant to sit next to, not instead of:

- [TENK 2026, *AI in research*](https://tenk.fi/fi/ajankohtaista/uusi-kansallinen-suositus-tukee-tekoalyn-vastuullista-kayttoa-tutkimuksessa) ([English PDF](https://tenk.fi/sites/default/files/2026-06/Artificial%20Intelligence%20in%20Research.%20TENK%27s%20Recommendation%202026.pdf))
- TENK *Responsible conduct of research* (HTK 2023) and *Ethical review in the human sciences* (IEEA), which TENK’s AI recommendation complements
- Where useful: [ALLEA European Code of Conduct (2023)](https://allea.org/code-of-conduct/) and the [ERA living guidelines on generative AI in research](https://research-and-innovation.ec.europa.eu/document/download/2b6cf7e5-36ac-41cb-aab5-0d32050143dc_en)

TENK 2026: Finnish National Board on Research Integrity (2026). *Tekoäly tutkimuksessa: hyvä tieteellinen käytäntö ja eettiset periaatteet.* Publications 1/2026. English: *Artificial Intelligence in Research.* Publications 2/2026.

### In the workflow

| Guidance | What the kit does |
|---|---|
| The researcher is responsible for content, conclusions, and reliability | You accept claims and important decisions. Agents propose and implement. |
| Check AI outputs before they count | Draft outputs stay provisional. Numbers in a draft manuscript are not approved results. |
| Do not invent or distort results | Agents must not invent numbers. Propose, implement, and interpret in one run is forbidden. |
| Confidential or personal data only with adequate protection | Default: agents do not read row-level real data. |
| Keep synthetic data distinct from real data | A synthetic run stays a draft if the project requires a real-data approval. |
| AI is not an author | Do not list an AI system as an author. Do not invent authorship percentages. |
| Disclose material AI use that affects reliability | Say it in the paper (and in plans or ethics materials if they apply). The optional `ai-use/` files are extra, default off. |
| Do not feed others’ unpublished manuscripts or plans to an AI system without permission | Agents must not do that. |

## Where this kit takes a different path

These are deliberate. They are not TENK violations; they are limits of what a folder of files can do.

**Workflow stops, not a full ethics system.** TENK leaves case-by-case judgment with the researcher. This kit turns a few of those moments into files: agreed analysis plan, *researcher decision needed*, approved result. That machinery is ours. TENK does not require it.

**Optional log, required honesty.** The on-disk AI-use record defaults to **off**. TENK still expects you to disclose use that affected reliability. Off means “no extra kit file,” not “do not mention it.”

**Not an ethics committee.** The kit does not decide whether IEEA or another review is needed. AI use alone does not trigger review. Put protocols, consent text, and data-management plans in `06-docs/` when the study needs them. Extra docs do not agree an analysis.

**Not the whole of TENK.** This version does not assess bias, environmental cost, or organisational AI literacy. A paper can record a relevant choice as a research decision.

**Cloud tools are not certified.** A coding assistant that can read this folder may send project text (overview, plan, draft) to a vendor. Restricted mode does not stop that. Use a tool your organisation allows. Check that vendor’s terms against your research contract and funder rules.

**Licences on AI-written code.** Treat generated code like any third-party code. The kit does not check licences.

## Later

This file is the place to grow journal-specific disclosure, approved-tool lists, or a stronger default for the AI-use log — without rewriting the design principles.
