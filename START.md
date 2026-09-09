# Start here

Early development. You do not need Python or R.

This kit has two jobs: **doing the research** (files for the plan, decisions, and approved results) and an **independent check** of those artefacts (in this version: **Audit the research chain**). The first is an experimental workflow. The second reports what it could and could not check; it does not certify the paper. Use a **new chat** for the check — not the chat that wrote the files.

Keep **one kit folder**. Defaults live there. Each paper is a separate folder. Numbered folders, Quarto/APA, and a Google Docs co-author copy are the default working setup for a paper started here. They are not required to understand the two jobs.

The assistant uses a file from the **paper if it exists**, otherwise from the **kit**. Put a file in the paper only to override a default (for example this study’s R habits). Do not copy the whole kit into the paper.

## 1. Get the kit (do this once)

Create an empty folder (for example `research-agent-kit`). Open it with your AI assistant. Paste:

```
Copy the Research Agent Kit from https://github.com/juusorepo/research-agent-kit
This folder is the kit.
My name is
```

The assistant writes your name in `researcher.md` in this folder. You will not be asked again for each paper.

## 2. Start a new project or paper

The assistant must see the **kit** (for defaults and skills). A chat that only has an empty paper folder is not enough.

**Easiest:** open the **kit** folder, or the kit **and** an empty paper folder. Paste:

```
Start the project
```

The assistant finds the kit, writes only into the paper (it will not add files to the kit), asks a short list of questions (with defaults), and waits. After you answer, setup is copy-then-patch, not a second interview. If no paper folder is open yet, it creates one next to the kit (default **paper-1**). Numbered science folders (`01-data` … `07-record`, `99-archive`); the paper lives in `05-outputs/manuscript/`.

If `researcher.md` has no name yet, add `My name is` once — it is stored in the kit.

Usual case: you already have a protocol, analysis plan, or draft. Put those in `06-docs/` and `05-outputs/manuscript/` (or attach them in chat). After the folder exists, say **Understand the project**. The assistant should **read those files before** suggesting next steps.

One folder is one paper unless you say this project has several papers that share data and scripts. Then the numbered data and scripts stay shared; each paper gets its own record under `07-record/<name>/` and manuscript under `05-outputs/<name>/manuscript`.

The file agents follow is `AGENTS.md`. There is no `CLAUDE.md` in the paper folder.

## Later

Agent work: keep the kit available (kit + paper, or start from the kit). RStudio/writing can be the paper alone.

To override a default for **this paper only**, add that file in the paper (same relative path). To change a default for **every paper**, edit the kit.

How this kit treats AI in research — and where it does not replace national guidance — is in `policies/ai-policy.md`. The workflow design is in `DESIGN_PRINCIPLES.md`.

**Independent check.** Open a **new chat** and say **Audit the research chain** (full chain, or one link). You can say this in a kit paper **or** in a folder that was never set up with this kit. If there is no folder map, the assistant asks where the plan, code, outputs, and manuscript are (with defaults if it can see them) and waits once. It does not create a kit paper. Missing pieces are recorded as not checked, not as a pass.

The assistant diagnoses; it does not repair. The full report is a saved file. It keeps two statuses: whether numbers match, and whether the claims are supported — not one overall pass. If this paper already has a task list and anything needs work, it adds one row and stops. If there is no task list, remaining work stays in the report. It does not ask how to fix the findings. A new chat does the next task when you say which one (for example **Do T-004**). Do not paste the audit into that chat. After you have a Word file of the paper, export a PDF from that Word file and say **Audit APA presentation** to check layout (tables, figures, title page, headings). That is a separate independent check, not the research-chain check. Further independent checks may be added later.

If start chose Stata, you can later say **Run approved Stata analysis** for one named `.do` file on an assigned run-on-real-data task. Put this computer’s Stata path in `stata_bin.local.yml` (not in git) or `STATA_BIN` — do not assume a path.

Co-author review: render a Word file of the paper first (see the manuscript README), then say **Prepare a review copy**. Accept small wording in the Google Doc, then **Sync the review copy**. Say **Ingest review comments** for leftover open comments. **Review the manuscript** files an AI pass in the same inbox. Say **Explore alternative framings** when you want genuinely different interpretations before any combined wording.

New kit version from GitHub? Open the **kit** folder and paste:

```
Update the kit from https://github.com/juusorepo/research-agent-kit
Keep my how-to-talk and R templates.
```

Only new skills (overwrite the skills folder, leave the rest of the kit)? Paste:

```
Update the skills from https://github.com/juusorepo/research-agent-kit
```

The assistant must not change any paper folder. On a full kit update it must not overwrite your name, how-to-talk, or R templates if you asked to keep them. **Update the skills** overwrites the skills folder only.

A paper still on an older kit version? Open that **paper** folder (keep the kit available) and paste:

```
Adjust this project to the new kit version
```

The assistant inspects this paper, shows the exact proposed changes to instructions and the version note, and waits. It must not edit the analysis plan, decision notes, outputs, manuscript, or data.
