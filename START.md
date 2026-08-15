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

**Easiest:** open the **kit** folder. Say **Start the project**. The assistant asks a short list of questions (with defaults) and waits. Then it creates a sibling folder of numbered science folders (`01-data` … `07-record`, `99-archive`). The paper lives in `05-outputs/manuscript/`.

**Or** open **both** folders, and paste:

```
Start the project from my Research Agent Kit folder
```

If `researcher.md` has no name yet, add `My name is` once — it is stored in the kit.

Usual case: you already have a protocol, analysis plan, or draft. Put those in `06-docs/` and `05-outputs/manuscript/` (or attach them in chat). The assistant should **read them before** suggesting next steps.

One folder is one paper unless you say this project has several papers that share data and scripts. Then the numbered data and scripts stay shared; each paper gets its own record under `07-record/<name>/` and manuscript under `05-outputs/<name>/manuscript`.

The file agents follow is `AGENTS.md`. There is no `CLAUDE.md` in the paper folder.

## Later

Agent work: keep the kit available (kit + paper, or start from the kit). RStudio/writing can be the paper alone.

To override a default for **this paper only**, add that file in the paper (same relative path). To change a default for **every paper**, edit the kit.

How this kit treats AI in research — and where it does not replace national guidance — is in `policies/ai-policy.md`. The workflow design is in `DESIGN_PRINCIPLES.md`.

New kit version from GitHub? Open the **kit** folder and paste:

```
Update the kit from https://github.com/juusorepo/research-agent-kit
Keep my how-to-talk and R templates.
```
