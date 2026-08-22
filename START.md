# Start here

Early development. You do not need Python or R.

Keep **one kit folder**. Defaults live there. Each paper is a separate folder.

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

The assistant finds the kit, writes only into the paper (it will not add files to the kit), asks a short list of questions (with defaults), and waits. If no paper folder is open yet, it creates one next to the kit (default **paper-1**). Numbered science folders (`01-data` … `07-record`, `99-archive`); the paper lives in `05-outputs/manuscript/`.

If `researcher.md` has no name yet, add `My name is` once — it is stored in the kit.

Usual case: you already have a protocol, analysis plan, or draft. Put those in `06-docs/` and `05-outputs/manuscript/` (or attach them in chat). The assistant should **read them before** suggesting next steps.

One folder is one paper unless you say this project has several papers that share data and scripts. Then the numbered data and scripts stay shared; each paper gets its own record under `07-record/<name>/` and manuscript under `05-outputs/<name>/manuscript`.

The file agents follow is `AGENTS.md`. There is no `CLAUDE.md` in the paper folder.

## Later

Agent work: keep the kit available (kit + paper, or start from the kit). RStudio/writing can be the paper alone.

To override a default for **this paper only**, add that file in the paper (same relative path). To change a default for **every paper**, edit the kit.

How this kit treats AI in research — and where it does not replace national guidance — is in `policies/ai-policy.md`. The workflow design is in `DESIGN_PRINCIPLES.md`. You can ask to **audit the research chain** (full chain, or one link). The assistant diagnoses; it does not repair. The full report is a file under the record path. It keeps two statuses: whether numbers match, and whether the claims are supported — not one overall pass. In chat it asks a short list (now / later / notes) with defaults, then waits. A new chat does the next task when you say which one (for example **Do T-004**). Do not paste the audit into that chat.

Co-author review: say **Prepare a review copy** (Google Doc). Accept small wording in the Doc, then **Sync the review copy**. Say **Ingest review comments** for leftover open comments. **Review the manuscript** files an AI pass in the same inbox.

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
