# Research Agent Kit

Research Agent Kit is an experimental, platform-agnostic toolkit for conducting research with AI agents while retaining epistemic control. It provides reusable research workflows, structured project memory, decision and provenance patterns, verification practices, and agent skills that can be used across Claude, Codex, Gemini, Cursor, local agents, and future platforms.

**Status: early development / v0.x.** APIs, structures, and conventions are expected to change.

Repository: [github.com/juusorepo/research-agent-kit](https://github.com/juusorepo/research-agent-kit)

The idea is simple: **from chat memory to a shared research record.** The record lives in ordinary files in your project. Any colleague or AI tool can read the same files. Nothing important should exist only in a chat.

You start by copying this folder and asking an assistant to set it up. You do not need Python or R for that. You do not need software-engineering vocabulary.

`SPEC.md` is the builder’s document (tests, metadata, invariants). This README is for researchers.

---

## What you keep in the project

| File | Question it answers |
|---|---|
| **Folder map** (`layout.yml`) | Where do scripts, outputs, and the manuscript live? (you may change this) |
| **Project overview** (`RESEARCH_CONTEXT.md`) | What are we studying? What do we know about the data? |
| **Analysis plan** (`ANALYSIS_PLAN.md`) | What have we *agreed* to analyse and report? |
| **Research decision notes** (`decisions/`) | Why did we make important methodological choices? |
| **Project status** (`STATUS.md`) | Where are we now? (a snapshot, not the last word) |
| **Tasks** (`TASKS.md`) | What is in progress? |
| **Data-use rules** (`policies/data-policy.md`) | What may AI do with the data? (`restricted` vs `agent-accessible`) |
| **Extra context** (`docs/`) | Preregistration, ethics, proposals. Background only — it does not override the analysis plan |
| **Manuscript** | The file the paper is written in (Quarto by default). Google Docs / Word copies for co-authors are review snapshots |

The **analysis plan** is stricter than a loose methods paragraph, but it is still an analysis plan:

> The current record of analyses the research team has agreed to run or report.

Each agreed analysis has a short id (`A-014`). Table 1 can be an agreed item without a long decision note. A change to the sample, a scale, or the main model should get a **research decision note**.

One Git folder can hold **several papers**. Shared rules live at the top; each paper has its own overview, plan, manuscript, and outputs.

---

## How a result becomes citable

```
Proposed analysis → agreed analysis → analysis run → result approved → used in the manuscript
```

1. Explore freely. Draft outputs are fine.
2. To stand behind a number, that analysis must already be in the **agreed analysis plan**.
3. Run the analysis under this project’s data-use rules. If the data are **restricted**, you (or a designated analyst) run the real data — not a cloud AI acting alone. If the data are **agent-accessible** (e.g. public tables), the assistant may work with them as the policy allows.
4. You **approve** the result file. That fact is written on the file, not only said in chat. Approval is not the same as an independent audit.

An AI assistant should ask, in plain language:

> Is this analysis already included in the agreed analysis plan?

If not, it proposes adding it. If the change is important, it suggests **recording a research decision** before implementing.

---

## What AI may and may not do

AI may implement, criticise, and propose.  
**You** accept claims and important decisions.

If your data are restricted, individual-level files stay **outside** the project folder and agents work from codebooks, synthetic/test data, and **AI-safe research outputs**. Public or in-repo teaching data can be marked agent-accessible in the project rules.

This is **epistemic control**: researcher decision points sit where the design, the analysis, or a claim would change — not after every keystroke, and not as a slogan the assistant repeats.

---

## Agent skills (v0.1)

Reusable ways of doing recurring jobs. The assistant should use ordinary verbs:

| Skill | What it does |
|---|---|
| Start the project | Short interview, then create folders and a folder map |
| Understand the project | Read the shared record and say where things stand |
| Develop analysis with safe data | Write and test analysis without crossing the data line |
| Document a research decision | Record an important choice (not every Table 1) |
| Update the project record | After you accept something, put it in the right file |

**Start-project questions** (defaults in **bold**):

- Your name (lead researcher)
- Restricted data or data the assistant may use?
- One paper or several? First paper name
- Manuscript: **Quarto**, Markdown, or Word (Word template comes later)
- Analysis code: **R** or Stata (Stata template comes later)
- Folders: **by-paper** (`papers/<name>/…`) or numbered (`01-data`, `02-scripts`, `05-outputs`, `06-docs`)

You can change folder names later by editing `layout.yml`. Assistants should follow that file rather than assuming `02-scripts`.

The kit ships a **Quarto manuscript stub** and an **R analysis stub**. A stricter Quarto *profile* (every number must come from an approved result file) is later work.

Small extra setup may be needed for Claude, Cursor, or another tool. That setup only *points* at these files. It does not invent a second set of rules.

---

## Start on day one

See [`START.md`](START.md). Copy this repository, open the folder with an assistant, and say **Start the project**. No Python or R required.

Then fill the overview. The analysis plan may start empty. Add decision notes when a real choice appears.

`scripts/install.py` is an optional shortcut if you already have Python. Kit *tests* use Python (`pytest`); researchers do not need it.

**v0.1 does not migrate existing live papers.** The first test is `examples/toy-study`. Structural tests and T13 (for kit builders):

```text
pip install -r requirements-dev.txt
pytest tests/toy-study
```

T1–T12 are scored on files after a separate agent run (`tests/toy-study/score.py`). Tag `v0.1.0` when those pass.
