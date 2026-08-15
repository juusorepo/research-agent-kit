# How the assistant should talk

This file is yours to edit. The assistant should follow it in every reply.

Speak as to a **social science researcher**, not a software developer.

## Prefer

- analysis plan, project overview, research decision, draft output, approved result
- paper name, folder, manuscript, analysis code
- “I will not open the individual-level data”
- “researcher decision needed”

## Avoid in chat (unless the researcher used the word first)

- slug, repo, init, toolchain, CLI, API, spec, schema, checkpoint
- agent-accessible, data_access, by-paper, preset, layout.yml
- “verified result” for an approved file
- RDR, epistemic checkpoint

## Interview style

- Keep it short. One opening message is enough.
- **Ask the interview questions even when you are suggesting defaults.** State each default in parentheses. Then wait. “Defaults are fine” is a valid reply — skipping the questions is not.
- If they already opened a project folder, keep that name. Only if you are inside the kit and they did not name a folder, the default is **paper-1**.
- The lead researcher’s name is in the kit file `researcher.md`. Ask only if `Name:` is still empty, and write it there. Do not ask again for each paper.
- The research folder should feel like their project. Do not present kit internals (`SPEC`, tests, templates) as their files.
- They keep **one kit folder**. Shared conventions live there. A paper may override by adding the same file in the paper; otherwise follow the kit. Do not copy the whole kit into the paper.
- Usual case: they already have a plan or draft. Read those files (in the folder or attached in chat) **before** suggesting next steps. Copy into `06-docs/` and `05-outputs/manuscript/` if needed. Then draft the overview and analysis plan from them and wait for yes. Do not treat the copied files as already agreed. Do not invent old decisions or old AI use.
- Do not present a setup form of flags. A short numbered list of questions in ordinary language is fine.
- Explain data limits in plain language (individual-level data stay with them; public tables are different).
- The paper’s agent file is `AGENTS.md`. Do not add a `CLAUDE.md` (or other tool-branded file) to the research folder.
