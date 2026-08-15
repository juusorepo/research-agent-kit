# Start here

Early development. You do not need Python or R.

Keep **one kit folder**. That is the only place you edit R conventions, how the assistant should talk, and other defaults. Each paper is a separate folder.

## 1. Get the kit (do this once)

Create an empty folder (for example `research-agent-kit`). Open it with your AI agent / assistant. Paste:

```
Copy the Research Agent Kit from https://github.com/juusorepo/research-agent-kit
This folder is the kit.
```

Edit conventions **only here**.

## 2. Start a new project or paper

The assistant must **read your kit** to copy conventions. A new chat that only has the empty paper folder cannot see the kit.

**Easiest:** open the **kit** folder. Say **Start the project**. Give your name. The assistant creates a new paper folder next to the kit. Then copy your plan or draft into `06-docs/` and `manuscript/`, and say **Understand the project**.

**Or** open **both** the kit and the new paper folder, and paste (add your name):

```
Start the project from my Research Agent Kit folder
My name is
```

Do not edit R conventions in the paper. After this, day-to-day, open **only the paper**.

If you only send your name: Quarto, R, no individual-level data, no AI-use log. The folder keeps the name you gave it.

## Later

Day to day, open only the paper. The kit is not needed unless you are changing conventions or starting a new paper.

Changed a convention in the kit? Open the paper **and** the kit, then paste:

```
Update the copied instructions from my Research Agent Kit folder
```

Your overview, plan, data, scripts, and manuscript stay.

New kit version from GitHub? Open the **kit** folder and paste:

```
Update the kit from https://github.com/juusorepo/research-agent-kit
Keep my how-to-talk and R templates.
```
