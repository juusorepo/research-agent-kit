# This folder is the Research Agent Kit

This is the **kit**, not a paper. Shared conventions and skills live here. Each paper is a separate folder.

If they say **Copy the Research Agent Kit** from GitHub: fetch the public kit into this folder. Then delete any workshop files if they came along (`dev/`, `SPEC.md`, `BACKLOG.md`, `tests/`, `pytest.ini`, `requirements-dev.txt`, `scripts/install.py`). Do not mention those files. Do not turn this folder into a paper. If `researcher.md` has no name yet, ask once and write it there.

If they say **Audit the research chain**: use `skills/audit-research-chain/SKILL.md`. If the folder they want checked has no `layout.yml`, that skill still runs (intake). Do not Start the project. Do not audit this kit folder.

If they say **Start the project** or **Initiate**: use `skills/start-research-project/SKILL.md` and `policies/how-to-talk.md`. Ask the interview questions (with defaults) and wait. After they reply, copy the paper skeleton and patch; do not read template files. Understand the project is the next message. Default folder **paper-1**, numbered `01-data` … `07-record`, manuscript in `05-outputs/manuscript/`. Do not copy `CLAUDE.md`. Use the name in `researcher.md`. Do not require Python or R.

If they say **Update the kit**: use `skills/update-the-kit/SKILL.md`. Work only in this kit folder. Do not overwrite `researcher.md` or files they asked to keep. Do not touch paper folders.

If they say **Update the skills**: use the same skill, skills-only path. Overwrite `skills/`. Do not edit the rest of the kit or any paper.

If they say **Adjust this project to the new kit version**: they must be in a **paper** folder. Use `skills/adjust-project-to-kit/SKILL.md`. Inspect, propose instruction and version changes, wait. Do not edit science files. If they are still in the kit, stop and ask them to open the paper.

If they are in a **paper** folder and propose a kit change: write a note under that paper’s record path. Do not edit this kit folder from the paper.

Researchers start from `START.md` and `README.md` (doing the research vs an independent check). A paper file overrides the same path in the kit. How the kit sits next to national guidance is in `policies/ai-policy.md`.

Paper skill phrases (Understand the project, Audit the research chain, Record a research decision, and the rest) live in that paper’s AGENTS.md skill-trigger table — same table as `templates/project/AGENTS.md`. The phrase is enough; do not ask for a long prompt. Each skill file holds its own rules.

If a `dev/` folder is present, this copy is a kit workshop — also follow `dev/AGENTS.md`.
