# Research Agent Kit

An experimental kit of ordinary files and short phrases for using AI on a research paper. Works with Claude, Codex, Gemini, Cursor, local agents, and similar tools.

**Status: early development / v0.x.** Conventions will change.

When AI agents write analysis, they often make measurement and design choices that nobody recorded. A draft number can look like a result. A manuscript claim can outrun the design. (See Gao and Xiao, 2026, [Nonstandard Errors in AI Agents](https://arxiv.org/abs/2603.16744).)

This kit has **two jobs**:

1. **Doing the research** — keep an agreed analysis plan, decisions, and approved results in files the team can read. Chat is a working space, not the record. This workflow is experimental. It does not guarantee quality.
2. **Independent check** — in a **new chat**, check artefacts: did meaning hold from plan through code, output, manuscript, and claim? The check in this version is **Audit the research chain**. It reports two statuses (whether numbers match; whether the claims are supported) and says when a link could not be checked. It does not repair, certify the paper, or collapse those into one pass. You can say this in a folder that was never set up with the kit; the assistant asks where the plan, code, outputs, and manuscript are if that is not already clear. Further independent checks may be added later; they stay separate from doing the research.

The kit **supports inspectability**. It does not ensure integrity. Restricted individual-level data is a **rule the assistant follows** (those files stay outside the project). It is not a lock on the disk.

Repository: [github.com/juusorepo/research-agent-kit](https://github.com/juusorepo/research-agent-kit)

Keep **one kit folder** if you want it on disk. Each paper is a separate folder. A paper folder alone can start and refresh generated kit files from GitHub. See [`START.md`](START.md). You do not need Python or R. You do not need software-engineering vocabulary.

The defaults for a new paper (numbered folders, Quarto and APA, a Google Docs co-author copy, Stata on Windows if you chose it) are a **working setup used in real papers**. They are not the method. You can change folder names in `layout.yml`.

---

## How it works

The conducting idea: **from chat memory to a shared research record.** The record lives in ordinary files. Any colleague or AI tool can read the same files. Nothing important should exist only in a chat.

One kit folder; each paper is a separate folder. Shared papers meant for co-authors or NotebookLM live in a **Google Drive** synced folder so everyone uses the same files — do not copy sources elsewhere. The assistant uses a **deliberate paper override** if it exists, otherwise **generated kit files** in the paper if present, otherwise the **kit**. Edit R conventions and other defaults only in the kit. Do not edit generated kit files in the paper.

**You** accept claims and important decisions (a yes in chat is enough). Then the assistant writes the files. Draft outputs are not approved results.

For quantitative work the chain is:

**agreed analysis plan → implementation → research output → manuscript → scientific claim**

If the data are restricted, agents do not read row-level files. The longer *why* is in [`DESIGN_PRINCIPLES.md`](DESIGN_PRINCIPLES.md). How this sits next to national guidance is in [`policies/ai-policy.md`](policies/ai-policy.md).

---

## What you keep in the project

| File | Question it answers |
|---|---|
| **Folder map** (`layout.yml`) | Where do scripts, outputs, and the manuscript live? (you may change this) |
| **Project overview** (`RESEARCH_CONTEXT.md`) | What are we studying? What do we know about the data? Optional **intellectual anchor**: why this project exists in the researcher’s own terms |
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
| **Manuscript** (`05-outputs/manuscript/`) | The file the paper is written in (Quarto by default). A Google Docs copy for co-authors is a review copy — Drive sync does not merge it back |

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

Researcher decision points sit where the design, the analysis, or a claim would change — not after every keystroke. **You** accept; then the assistant records that acceptance. That record is inspectable. It is not tamper-proof, and it is not a certificate that the science is sound.

---

## What you can say

Say these in chat. The assistant should use ordinary verbs.

| Skill | What it does |
|---|---|
| Start the project | Create a paper folder that follows the kit. With a local kit, writes only into the paper. With only a paper folder, paste **Start the project from https://github.com/juusorepo/research-agent-kit** (temporary fetch; not a full clone) |
| Make this paper self-contained | Write generated kit files into this paper so an assistant can work without opening the kit. Do not edit those files |
| Update the kit | In the **kit** folder: fetch a new public version; keep your name and files you asked to keep. In a **paper**: replace generated kit files from GitHub (temporary fetch; not a full clone). Say **Update the skills** only in the kit folder |
| Understand the project | Where things stand (canonical vs proposal vs note), then what to do next. Agreeing analyses is a next step here: the assistant proposes items, you accept, then the analysis plan is written |
| Contribute to the project | Collaborator inbox — does not overwrite the record |
| Consolidate contributions | You review the inbox; the assistant recommends, you decide |
| Prepare a review copy | Native Google Doc snapshot of the Quarto paper. Saying the phrase is enough to render Word when the snapshot is missing. Word is a conversion step, not a second manuscript. Not the paper file itself |
| Ingest review comments | Leftover open comments → inbox. Skip wording already accepted in the Doc |
| Sync the review copy | After you accept suggestions in the Doc, update the manuscript once |
| Review the manuscript · Scan for generic prose | AI pass; findings go to the inbox. Optional **external manuscript review** (this computer or hosted; Coarse is one service) if you tick it or ask in that chat. A prose scan flags vague attribution, generic filler, puffery, formulaic rhetoric, and unclear abstraction as candidate passages; it does not score or judge authorship, and it does not send the file. Findings note severity and whether an open task already covers them. Proposed wording only if you tick **Propose wording in prose scans**. Not an audit of the research chain |
| Draft this in my voice · Edit this in my voice | Optional. Off until you tick **Author voice** in that paper’s `policies/what-is-on.md`. Drafts or restyles manuscript prose; does not rewrite during a scan. Integrity (numbers, hedges, citations) wins over style |
| Explore alternative framings | Genuinely different interpretations, generated independently, then you choose. Optional. Not for routine editing |
| Document a research decision | Record an important choice (not every Table 1) |
| Develop analysis with safe data | Write and test analysis without crossing the data line |
| Run approved Stata analysis | If start chose Stata: run one named `.do` file for an agreed analysis on an assigned **run on real data** task. Configure this computer’s Stata path; do not assume one. Windows first |
| Update the project record | After you accept something, put it in the right file |
| Audit the research chain | Independent check: plan → code → output → manuscript → claims. Use a **new chat**, not the one that wrote the files. Works on a kit paper or on a folder that was never set up with the kit (the assistant asks where the four pieces are). The saved report keeps **two** statuses: whether numbers match, and whether the claims are supported. Matching numbers is not enough. Diagnose only. If this paper already has a task list and anything needs work, add one task pointing at the report, then stop. Next work: **Do T-004** in a new chat, not a pasted prompt. If there is no task list, remaining work stays in the report |
| Audit literature claims | Independent check of literature statements against identifiable sources (new chat). Does not trust a draft evidence packet or NotebookLM as authority. Not the same as **Map the evidence** |
| Map the evidence | Draft a source-grounded evidence packet for a named question. Not an audit. Not an approved claim. **Create a notebook**, **Delete a notebook**, and **Search with NotebookLM** use the same skill for the optional connector. Search hits go to Zotero first |
| Sync the bibliography | Refresh this paper’s source list from a Zotero collection or from `references.bib`. Citation keys still come from that export. Copies for sharing stay in `08-sources/` (Zotero stays canonical) |
| Adjust this project to the new kit version | After you updated the kit, replace this paper’s generated kit files (or a small instruction patch if it has none). Science files stay as they are |
| Audit APA presentation | Independent check of the rendered Word file and a PDF exported from it. Four statuses (render, tables, figures, manuscript frame). Not the research chain. Diagnose only |

Optional in this version: a record of material AI use — **off** unless you tick it in `policies/what-is-on.md`. Off means no extra kit file. You still disclose in the paper when AI affected reliability. See [`policies/ai-policy.md`](policies/ai-policy.md). **Author voice** is also off until you tick it in that paper; other papers stay ordinary. **Propose wording in prose scans** is off until you tick it; the scan still does not edit the manuscript. **External manuscript review** is off until you tick it or ask in that chat; findings stay proposals. Not in this version: journal disclosure forms, Word as the canonical manuscript, Word comment ingest, automatic background audits, the assistant starting unassigned tasks on its own, writing to Zotero, a required Python program, or treating NotebookLM as verification. **Audit literature claims** is in this version (independent check; it does not certify the paper). This workflow is experimental; it does not guarantee quality.

The workflow design is in [`DESIGN_PRINCIPLES.md`](DESIGN_PRINCIPLES.md).

**Start the project:** empty Drive folder plus **Start the project from** the GitHub URL is enough for a self-contained paper (Claude does not need the kit folder). Or keep one kit folder and start papers from it. The assistant asks the interview questions (with defaults) and waits; after the answers, setup is copy-then-patch. Understand the project is the next message. Generated kit files are replaced from GitHub with **Update the kit** in that paper, or from a local kit with **Adjust this project**. Do not edit them. How it talks is in `policies/how-to-talk.md`.

You can change folder names later by editing `layout.yml`. Assistants should follow that file rather than assuming `02-scripts`. First-level folders stay numbered (`01-data` … `08-sources`, `99-archive`). The manuscript sits in `05-outputs/manuscript/` next to figures and tables.

The kit ships a **Quarto manuscript** (APA format) that reads **approved** result files only — the same approach as a quantitative paper that builds tables from those files and includes figures already written to `05-outputs/figures`. The paper is a thin `paper.qmd` plus `_*.qmd` section files (one copy of each section). It does not read row-level data. Tables and figures that go into the paper follow the manuscript display list (APA 7); posters and talks do not. `renv` and `{targets}` are later work.

Small extra setup may be needed for a specific tool. That setup lives in the kit `adapters/` folder and only *points* at these files (Stata, Drive, Docs, NotebookLM, Claude Code, and an optional manuscript review service). On **Windows**, a Google Drive paper should be opened from the local mirrored folder, not `G:\My Drive` — see `adapters/google-drive/`. Papers use `AGENTS.md`. A thin `CLAUDE.md` points at that file so Claude Code can start; see `adapters/claude/`.

---

## Start on day one

See [`START.md`](START.md). **Start the project from** the GitHub URL in an empty paper folder, or get one kit folder and start papers from it. Paper files override the kit when present.

Then fill the overview. If you copied a protocol, preregistration, or draft and the overview is empty, the assistant should draft it **in that reply** and write the file after you accept. It should leave the intellectual anchor for you to dictate — it must not invent why you are doing the paper. The analysis plan may start empty until you accept items. Add decision notes when a real choice appears — including one past choice that still governs the work, if you want it on the record. Do not expect a reconstructed history of earlier AI use.

**v0.2 does not migrate existing live papers.** A small worked example is in `examples/toy-study`.
