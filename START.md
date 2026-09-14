# Start here

Early development. You do not need Python or R.

This kit has two jobs: **doing the research** (files for the plan, decisions, and approved results) and an **independent check** of those artefacts (in this version: **Audit the research chain**). The first is an experimental workflow. The second reports what it could and could not check; it does not certify the paper. Use a **new chat** for the check — not the chat that wrote the files.

Keep **one kit folder** if you want shared conventions on disk. Each paper is a separate folder. A colleague who only has a paper folder can start and refresh generated kit files from GitHub instead. Numbered folders, Quarto/APA, and a Google Docs co-author copy are the default working setup for a paper started here. They are not required to understand the two jobs.

The assistant uses a file from the **paper if it exists** (a deliberate override), otherwise generated kit files in the paper if present, otherwise from the **kit**. Put `policies/how-to-talk.md` in the paper only to change how the assistant talks. Do not edit generated kit files. Do not copy the whole kit into the paper.

## 1. Get the kit (optional — only if you keep a kit folder)

Create an empty folder (for example `research-agent-kit`). Open it with your AI assistant. Paste:

```
Copy the Research Agent Kit from https://github.com/juusorepo/research-agent-kit
This folder is the kit.
My name is
```

The assistant writes your name in `researcher.md` in this folder. You will not be asked again for each paper. Skip this if you only work in a paper folder (Claude on Drive): go to **2b**.

## 2. Start a new project or paper

### 2a. You have the kit folder

**Easiest for sharing:** create an empty folder in **Google Drive for Desktop**. Open the **kit** folder **and** that empty paper folder. Paste:

```
Start the project
```

The assistant finds the kit, writes only into the paper, asks a short list of questions (with defaults), and waits. After you answer, setup is copy-then-patch. If you said this paper should work without the kit folder (the default when a paper folder is already open), it also writes **generated kit files** into the paper — do not edit those.

### 2b. Paper folder only (Claude, Drive, no kit)

Create an empty folder (Drive if co-authors or NotebookLM will use it). Open **only that folder**. Paste:

```
Start the project from https://github.com/juusorepo/research-agent-kit
This folder is the paper. Fetch the kit into a temporary folder, not here.
```

The assistant fetches the public kit into a **temporary** folder, writes a self-contained paper **here**, then deletes the temporary copy. This folder must not become a clone of the whole repository. Do not say **Copy the Research Agent Kit** here — that would turn this folder into a kit.

If `researcher.md` has no name yet (kit path only), add `My name is` once. On a paper-only start, the assistant asks your name and writes it on the overview.

Usual case: you already have a protocol, analysis plan, or draft. Put those in `06-docs/` and `05-outputs/manuscript/` (or attach them in chat). After the folder exists, say **Understand the project**. The assistant should **read those files before** suggesting next steps.

One folder is one paper unless you say this project has several papers that share data and scripts. Then the numbered data and scripts stay shared; each paper gets its own record under `07-record/<name>/` and manuscript under `05-outputs/<name>/manuscript`.

The file agents follow is `AGENTS.md`. There is no `CLAUDE.md` in the paper folder.

Numbered science folders (`01-data` … `08-sources`, `99-archive`); the paper lives in `05-outputs/manuscript/`.

## Later

Agent work: a paper with generated kit files can be the only folder. To refresh those files from GitHub (Claude on Drive, no kit): paste **Update the kit from https://github.com/juusorepo/research-agent-kit**. The assistant fetches a temporary copy and replaces generated files only — not a full clone. To change how the assistant talks for **this paper only**, add `policies/how-to-talk.md` in the paper. Do not edit generated kit files.

How this kit treats AI in research — and where it does not replace national guidance — is in `policies/ai-policy.md`. The workflow design is in `DESIGN_PRINCIPLES.md`.

**Independent check.** Open a **new chat** and say **Audit the research chain** (full chain, or one link). You can say this in a kit paper **or** in a folder that was never set up with this kit. If there is no folder map, the assistant asks where the plan, code, outputs, and manuscript are (with defaults if it can see them) and waits once. It does not create a kit paper. Missing pieces are recorded as not checked, not as a pass.

The assistant diagnoses; it does not repair. The full report is a saved file. It keeps two statuses: whether numbers match, and whether the claims are supported — not one overall pass. If this paper already has a task list and anything needs work, it adds one row and stops. If there is no task list, remaining work stays in the report. It does not ask how to fix the findings. A new chat does the next task when you say which one (for example **Do T-004**). Do not paste the audit into that chat. After you have a Word file of the paper, export a PDF from that Word file and say **Audit APA presentation** to check layout (tables, figures, title page, headings). That is a separate independent check, not the research-chain check. Further independent checks may be added later.

If start chose Stata, you can later say **Run approved Stata analysis** for one named `.do` file on an assigned run-on-real-data task. Put this computer’s Stata path in `stata_bin.local.yml` (not in git) or `STATA_BIN` — do not assume a path.

Co-author review: render a Word file of the paper first (see the manuscript README), then say **Prepare a review copy**. Accept small wording in the Google Doc, then **Sync the review copy**. Say **Ingest review comments** for leftover open comments. **Review the manuscript** files an AI pass in the same inbox. Say **Scan for generic prose** for a focused, detection-only pass: it flags candidate vague attribution, generic filler, puffery, formulaic rhetoric, and unclear abstraction, but does not rewrite or judge authorship. After a scan, if that paper has **Author voice** ticked, say **Edit this in my voice** to restyle accepted passages — not in the same run. Say **Draft this in my voice** for a first abstract or results section (tick **Author voice** in that paper’s `policies/what-is-on.md` first). Say **Explore alternative framings** when you want genuinely different interpretations before any combined wording.

New kit version from GitHub into the **kit** folder? Open the kit and paste:

```
Update the kit from https://github.com/juusorepo/research-agent-kit
Keep my how-to-talk and R templates.
```

New kit version **in a paper** (no kit folder open)? Open that paper and paste:

```
Update the kit from https://github.com/juusorepo/research-agent-kit
This folder is the paper. Fetch into a temporary folder; replace generated kit files only.
```

The assistant must not clone the whole repository into the paper. It replaces generated kit files only. It must not edit the analysis plan, decision notes, outputs, manuscript, or data.

Only new skills in the **kit** folder (overwrite the skills folder, leave the rest)? Paste:

```
Update the skills from https://github.com/juusorepo/research-agent-kit
```

On a full **kit folder** update it must not overwrite your name, how-to-talk, or R templates if you asked to keep them.

A paper still on an older kit version, with the **kit** open? You can also paste:

```
Adjust this project to the new kit version
```

The assistant inspects this paper, shows what generated kit files would change (or a small instruction patch if this paper has no generated files), and waits. It must not edit the analysis plan, decision notes, outputs, manuscript, or data.

A paper that must work when ChatGPT or a co-author cannot see the kit? Open the paper (keep the kit available) and paste:

```
Make this paper self-contained
```
