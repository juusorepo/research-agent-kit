# This folder is the Research Agent Kit

This is the **kit**, not a paper. Shared conventions and skills live here. Each paper is a separate folder.

If they say **Copy the Research Agent Kit** from GitHub: fetch the public kit into this folder. Then delete any workshop files if they came along (`dev/`, `SPEC.md`, `BACKLOG.md`, `tests/`, `pytest.ini`, `requirements-dev.txt`, `scripts/install.py`). Do not mention those files. Do not turn this folder into a paper. If `researcher.md` has no name yet, ask once and write it there.

If they say **Audit the research chain**: use `skills/audit-research-chain/SKILL.md`. If the folder they want checked has no `layout.yml`, that skill still runs (intake). Do not Start the project. Do not audit this kit folder.

If they say **Start the project** or **Initiate**: use `skills/start-research-project/SKILL.md` and `policies/how-to-talk.md`. Ask the interview questions (with defaults) and wait. After they reply, copy the paper skeleton and patch; do not read template files. If there is no local kit and they gave a GitHub URL, fetch a temporary copy, write a self-contained paper into the open folder, delete the temporary copy. Understand the project is the next message. Default folder **paper-1** only if Start runs inside the kit. Do not copy `CLAUDE.md`. Do not require Python or R.

If they say **Update the kit**: use `skills/update-the-kit/SKILL.md`. In the **kit** folder: fetch the public kit; do not overwrite `researcher.md` or files they asked to keep; do not touch paper folders. In a **paper**: fetch GitHub into a temporary folder; replace generated kit files only; do not clone the whole repository into the paper.

If they say **Update the skills**: kit folder only. Overwrite `skills/`. Do not edit the rest of the kit or any paper.

If they say **Make this paper self-contained**: they must be in a **paper** folder. Use `skills/make-paper-self-contained/SKILL.md`. Copy from a local kit or a temporary GitHub extract. Writes generated kit files into the paper so an assistant can work without the kit folder.

If they say **Adjust this project to the new kit version**: they must be in a **paper** folder. Use `skills/adjust-project-to-kit/SKILL.md`. Inspect, propose, wait. With generated kit files, replace that bundle. If the kit folder is unreadable, use **Update the kit** from GitHub. Do not edit science files. If they are still in the kit, stop and ask them to open the paper.

If they are in a **paper** folder and propose a kit change: write a note under that paper’s record path. Do not edit this kit folder from the paper.

Researchers start from `START.md` and `README.md` (doing the research vs an independent check). A paper file overrides the same path in the kit. How the kit sits next to national guidance is in `policies/ai-policy.md`.

Paper skill phrases (Understand the project, Audit the research chain, Record a research decision, and the rest) live in that paper’s AGENTS.md skill-trigger table — same table as `templates/project/AGENTS.md`. The phrase is enough; do not ask for a long prompt. Each skill file holds its own rules.

If a `dev/` folder is present, this copy is a kit workshop — also follow `dev/AGENTS.md`.
