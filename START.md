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

**Easiest:** open the **kit** folder. Say **Start the project**. The assistant uses the name in `researcher.md`. Then copy your plan or draft into `06-docs/` and `manuscript/`, and say **Understand the project**.

**Or** open **both** folders, and paste:

```
Start the project from my Research Agent Kit folder
```

If `researcher.md` has no name yet, add `My name is` once — it is stored in the kit.

## Later

Agent work: keep the kit available (kit + paper, or start from the kit). RStudio/writing can be the paper alone.

To override a default for **this paper only**, add that file in the paper (same relative path). To change a default for **every paper**, edit the kit.

New kit version from GitHub? Open the **kit** folder and paste:

```
Update the kit from https://github.com/juusorepo/research-agent-kit
Keep my how-to-talk and R templates.
```
