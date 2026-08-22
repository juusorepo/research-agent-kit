# Research Agent Kit

Research Agent Kit is an experimental, platform-agnostic toolkit for conducting research with AI agents while retaining epistemic control. It provides reusable research workflows, structured project memory, decision and provenance patterns, verification practices, and agent skills that can be used across Claude, Codex, Gemini, Cursor, local agents, and future platforms.

**Status: early development / v0.x.** APIs, structures, and conventions are expected to change.

Repository: [github.com/juusorepo/research-agent-kit](https://github.com/juusorepo/research-agent-kit)

The idea is simple: **from chat memory to a shared research record.** The record lives in ordinary files in your project. Any colleague or AI tool can read the same files. Nothing important should exist only in a chat.

Keep **one kit folder** on your computer. Edit R conventions and other defaults only there. Each paper is a separate folder. See [`START.md`](START.md). You do not need Python or R. You do not need software-engineering vocabulary.

---

## How it works

One kit folder; each paper is a separate folder. The assistant uses a file from the **paper if it exists**, otherwise from the **kit**.

**You** accept claims and important decisions (a yes in chat is enough). Then the assistant writes the files. Draft outputs are not approved results.

For quantitative work the chain is:

**agreed analysis plan → implementation → research output → manuscript → scientific claim**

If the data are restricted, agents do not read row-level files. The longer *why* is in [`DESIGN_PRINCIPLES.md`](DESIGN_PRINCIPLES.md). How this sits next to national guidance is in [`policies/ai-policy.md`](policies/ai-policy.md).

---

## What you keep in the project

| File | Question it answers |
|---|---|
| **Folder map** (`layout.yml`) | Where do scripts, outputs, and the manuscript live? (you may change this) |
| **Project overview** (`RESEARCH_CONTEXT.md`) | What are we studying? What do we know about the data? |
| **Analysis plan** (`ANALYSIS_PLAN.md`) | What have we *agreed* to analyse and report? |
| **Research decision notes** (`07-record/decisions/`) | Why did we make important methodological choices? (`INDEX.md` is a short list) |
| **Contributions** (`07-record/contributions/`) | Inbox from collaborators — proposals until you accept them |
| **Working notes** (`07-record/notes/`) | Chronological scratchpad — not loaded by default |
| **Audit reports** (`07-record/audits/`) | A check of the research chain — history, not the analysis plan |
| **Project status** (`STATUS.md`) | Where are we now? (a snapshot you rewrite in place, not a log) |
| **Tasks** (`TASKS.md`) | What is still to do? Kind of work is the role for the next chat. |
| **Data-use rules** (`policies/data-policy.md`) | What may AI do with the data? (`restricted` vs `agent-accessible`) |
| **AI in research** (`policies/ai-policy.md`) | How this kit sits next to national guidance. A paper may override. |
| **Extra context** (`06-docs/`) | Preregistration, ethics, proposals. Background only — it does not override the analysis plan |
| **Manuscript** (`05-outputs/manuscript/`) | The file the paper is written in (Quarto by default). A Google Docs copy for co-authors is a review copy |

The **analysis plan** is stricter than a loose methods paragraph, but it is still an analysis plan:

> The current record of analyses the research team has agreed to run or report.

The assistant may draft that file. **You** accept (a yes in chat is enough). Then the assistant writes it. You do not have to type it yourself.

Each agreed analysis has a short id (`A-014`). Table 1 can be an agreed item without a long decision note. A change to the sample, a scale, or the main model should get a **research decision note**.

One Git folder is usually **one paper**. If several papers share the same data and scripts, keep the numbered folders shared; each paper has its own record under `07-record/<name>/` and manuscript under `05-outputs/<name>/manuscript`.

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

## What you can say

Say these in chat. The assistant should use ordinary verbs.

| Skill | What it does |
|---|---|
| Start the project | Create a paper folder that follows the kit. Writes only into the paper, not the kit |
| Update the kit | Fetch a new public version into the kit folder; keep your name and files you asked to keep; do not touch papers. Say **Update the skills** to overwrite only the skills folder |
| Understand the project | Where things stand (canonical vs proposal vs note), then what to do next. Agreeing analyses is a next step here: the assistant proposes items, you accept, then the analysis plan is written |
| Contribute to the project | Collaborator inbox — does not overwrite the record |
| Consolidate contributions | You review the inbox; the assistant recommends, you decide |
| Prepare a review copy | Google Docs snapshot for co-authors (not the paper file itself) |
| Ingest review comments | Leftover open comments → inbox. Skip wording already accepted in the Doc |
| Sync the review copy | After you accept suggestions in the Doc, update the manuscript once |
| Review the manuscript | AI pass; findings go to the inbox. Not an audit of the research chain |
| Document a research decision | Record an important choice (not every Table 1) |
| Develop analysis with safe data | Write and test analysis without crossing the data line |
| Run approved Stata analysis | If start chose Stata: run one named `.do` file for an agreed analysis on an assigned **run on real data** task. Configure this computer’s Stata path; do not assume one. Windows first |
| Update the project record | After you accept something, put it in the right file |
| Audit the research chain | Check plan → code → output → manuscript → claims. The saved report keeps **two** statuses: whether numbers match, and whether the claims are supported. Matching numbers is not enough. Diagnose only; chat asks what to put on the task list now or later. Next work: **Do T-004**, not a pasted prompt |
| Adjust this project to the new kit version | After you updated the kit, align this paper’s instructions and version note. Science files stay as they are |

Optional in this version: a record of material AI use — **off** unless you tick it in `policies/what-is-on.md`. Off means no extra kit file. You still disclose in the paper when AI affected reliability. See [`policies/ai-policy.md`](policies/ai-policy.md). Not in this version: journal disclosure forms, Word toolchains, Word comment ingest, automatic background audits, the assistant starting unassigned tasks on its own.

The workflow design is in [`DESIGN_PRINCIPLES.md`](DESIGN_PRINCIPLES.md).

**Start the project:** get **one kit folder** from GitHub. Start each paper from that kit. The assistant asks the interview questions (with defaults) and waits; then it reads any files you already have before suggesting next steps. The assistant uses a paper file if it exists, otherwise the kit. How it talks is in `policies/how-to-talk.md`.

You can change folder names later by editing `layout.yml`. Assistants should follow that file rather than assuming `02-scripts`. First-level folders stay numbered (`01-data` … `07-record`, `99-archive`). The manuscript sits in `05-outputs/manuscript/` next to figures and tables.

The kit ships a **Quarto manuscript** (APA format) that reads **approved** result files only — the same approach as a quantitative paper that builds tables from those files and includes figures already written to `05-outputs/figures`. It does not read row-level data. Tables and figures that go into the paper follow the manuscript display list (APA 7); posters and talks do not. `renv` and `{targets}` are later work.

Small extra setup may be needed for a specific tool. That setup lives in the kit `adapters/` folder and only *points* at these files. Papers use `AGENTS.md`. Do not add a `CLAUDE.md` to the research folder.

---

## Start on day one

See [`START.md`](START.md). Get one kit folder, then start each paper from it. Paper files override the kit when present.

Then fill the overview. If you copied a protocol, preregistration, or draft and the overview is empty, the assistant should draft it **in that reply** and write the file after you accept. The analysis plan may start empty until you accept items. Add decision notes when a real choice appears — including one past choice that still governs the work, if you want it on the record. Do not expect a reconstructed history of earlier AI use.

**v0.2 does not migrate existing live papers.** A small worked example is in `examples/toy-study`.
