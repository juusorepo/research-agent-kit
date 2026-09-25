# Changelog

## 0.4.6 — 2026-09-25

**Sync the bibliography** checks Zotero on this computer at `127.0.0.1:23119` with `curl` (on Windows, `curl.exe`). A failed PowerShell request is not a closed Zotero. The assistant asks you to allow other applications only when that check cannot connect. It then asks which collection, and writes the collection key in the folder map. Saying **Can you read Zotero** or **Link the Zotero collection** uses the same check.

Open manuscript-review points now say what kind of response they need: manuscript work, a check against existing project evidence, a literature check, a rerun of an agreed analysis, or a proposed new analysis. Review still stops at the inbox; it does not accept the reviewer request, run the analysis, or silently turn it into an agreed plan item.

A new paper uses `AGENTS.md`. Claude Code does not load that file. If you use Claude Code, add a one-line `CLAUDE.md` that says `@AGENTS.md` (`adapters/claude/`). The kit does not generate that file.

`policies/what-is-on.md` now says **where** a feature should run: this computer (chain audit, large sources, rendered Word/PDF, Stata), anywhere the record is (planning, prose, deciding), or either. **Not in this version** lists only features that are out.

An audit writes a hash list of files it actually read, keeps a required “what could not be checked” section, and does not narrow the scope the researcher named. It still writes only the report, at most one task row, and an AI-use note if that box is ticked. Checking a literature statement against a source adds a row to `claim-checks.md` (citation key, manuscript location, source, what was verified). That is per-statement; the AI-use `check:` field remains the whole run. Before a finding is filed, it is checked against accepted decision notes: reading a note is not applying it. A plan line that an accepted note has voided is not treated as live.

**Prepare a review copy** on a Drive paper turns Quarto into a native Google Doc. Saying the phrase is enough to render Word when the snapshot is missing or stale. A current `.docx` already on Drive is converted rather than uploaded twice; otherwise Word is rendered outside the synced folder and deleted after the Doc checks out (headings, tables, figures, captions, references). Quarto stays the paper. Prior review rounds are kept. Drive syncing the folder does not merge Doc edits into Quarto — that is **Sync the review copy**. To share Word on OneDrive instead, set `provider: word` in `review-copy.yml`; Sync and Ingest stay Google Docs only.

**Audit literature claims** records each statement’s role and required depth (`background` may rest on the abstract; `comparator` and `counterargument` need Methods or Results). A named computed quantity in those roles cannot be grounded from title or abstract. Cited keys with no claim-to-source row are flagged. **Map the evidence** packets locate which source, not what it computed.

A new Quarto paper is a thin `paper.qmd` (YAML, setup, includes) plus one `_*.qmd` file per section. Edit the section file. Do not keep a second copy of the same section, and do not assemble the `.qmd` with a script. Existing single-file papers stay as they are until the researcher asks to convert. **Adjust this project to the new kit version** does not rewrite the manuscript.

A **Scan for generic prose** still does not score the manuscript, infer authorship, or edit the file. Each finding now carries severity and how large a fix is, points at related findings or an open task when the same work is already on the list, and checks repetition across sections (for example abstract and introduction), not only inside one section. **Propose wording in prose scans** is a separate tick: off keeps diagnose-only; on adds a suggested replacement that is never applied in that run.

This kit can send a named manuscript to an optional **review service** (this computer or hosted; Coarse is one implementation). **Review the manuscript** still files proposals in the inbox. The kit only starts the review, polls until it finishes, and fetches the report — it does not depend on one vendor command line or one assistant product. Restricted files stay off the service. A prose scan never sends the file.

On Windows, open a Google Drive paper from the **local mirrored folder**, not the streamed Drive letter (`G:\My Drive`). “Available offline” is not enough. Cursor, Claude, Codex, and similar tools may be unable to start programs there. The note is `adapters/google-drive/README.md`.

**Author voice** is an optional, per-paper tick. When it is on, **Draft this in my voice** and **Edit this in my voice** write manuscript prose that follows a researcher-owned voice note (if they wrote one) and avoids generic filler, without changing numbers, hedges, citations, or quotations. Off papers are unchanged. **Scan for generic prose** still does not edit the manuscript; a rewrite of accepted passages is a later **Edit this in my voice**. The assistant does not invent the voice note, does not learn from edits unless they accept a patch, and does not run a scan and a rewrite in the same turn.

**Scan for generic prose** is a focused, optional mode of **Review the manuscript**. It puts concrete candidate passages—such as vague attribution, generic filler, unsupported importance claims, formulaic rhetoric, and unclear abstraction—into the usual inbox for the researcher to judge. It does not rewrite text, score a manuscript, infer AI authorship, or treat formal academic language, warranted uncertainty, quotations, displays, or cited claims as problems by default.

A paper can hold **generated kit files** so an assistant that cannot see the kit folder (ChatGPT, a co-author, NotebookLM) can still follow the workflow. **Start the project from** the GitHub URL in an empty paper folder fetches a temporary copy and writes those files here — not a full clone. **Update the kit** in that paper refreshes generated files from GitHub the same way. Do not edit those files. **Adjust this project to the new kit version** still works when the kit folder is open. Shared papers belong in a Google Drive synced folder so co-authors and NotebookLM use the same `08-sources/` — no extra copy. **Make this paper self-contained** creates that folder if it is missing. **Sync the bibliography** refreshes a source list from Zotero or `references.bib` without inventing citation keys. **Map the evidence** writes a draft packet; **Audit literature claims** is a separate new-chat check and does not trust that packet. NotebookLM is optional retrieval, not verification. An **experimental NotebookLM connector** may query a notebook if you tick it **and** list its tool names in this paper’s folder map (the kit does not guess). If you ask, it may also create or delete a notebook, or run a **named search**. Usable search hits are for Zotero first (Add by Identifier, then Find Full Text), not a silent notebook import. Studio, sharing, and other extra NotebookLM products stay unused. Later work is rebuilding `08-sources/` from Zotero and automating notebook sources. The conducting workflow stays experimental; it does not guarantee quality.

The kit states two jobs: **doing the research** (an experimental file workflow) and an **independent check** of artefacts. The check in this version is the research-chain audit (two statuses, no certificate, new chat). You can run that check on a folder that was never set up with the kit: the assistant asks where the plan, code, outputs, and manuscript are, and does not create a kit paper. The kit supports inspectability; it does not ensure integrity. Restricted data remains a rule the assistant follows, not a lock. Numbered folders, Quarto/APA, and the Google Docs copy are the default working setup, not the method. Further independent checks may be added later.

**Start the project:** after the answers, setup is copy-then-patch from a ready-made paper skeleton (four line patches). If no paper folder is already open and they have not given a path, the interview asks **where** to create it (default **paper-1** next to the kit). Codex (one folder): they create the paper folder first, open it, and name the **local kit** path — do not fetch GitHub. GitHub start is only when there is no local kit. Two ways stay current: the paper can read a local kit folder, or hold generated kit files so it works alone. The assistant does not read template files and does not use Cursor’s create-project helper. Understand the project is the next message.

The project overview may hold a short **intellectual anchor** (why this paper exists in the researcher’s own terms). The assistant reads it before consequential framing work and flags a narrowing instead of silently smoothing it away. Empty is fine; the assistant does not invent it.

**Explore alternative framings:** when you ask, the assistant generates genuinely different interpretations independently, then stops for you to choose. It does not use fictional personas, and it does not average the alternatives into one wording before you have seen them.

## 0.4.5 — 2026-08-30

The assistant does not invent bibliography records or citation keys. `references.bib` comes from a Zotero (or other) export. If the file is empty, it asks for that export first, then matches `[@key]` in the paper. A paper chat may propose kit wording as a note; it does not edit the kit folder.

## 0.4.4 — 2026-08-30

You can say **Audit APA presentation** (or **Check tables and figures in Word**). The assistant checks the rendered Word file and a PDF exported from it: whether the render is intact, and whether tables, figures, and the manuscript frame hold. Four statuses, not one overall pass. Missing Word or PDF means tables cannot pass from the source file alone. This is not an audit of the research chain and not a peer-style manuscript review. Diagnose only; if anything needs work, one row on the task list.

## 0.4.3 — 2026-08-30

**Prepare a review copy** uploads a Word snapshot you already rendered. If that file is missing or older than the paper, the assistant stops and asks you to render; it does not knit a workaround unless you say to. A new approved result can make the Word file stale even if you did not edit the text. The Google Doc remains a snapshot; the Quarto file remains the paper.

## 0.4.2 — 2026-08-23

After an audit, the assistant writes the report and, if anything needs work, one row on the task list. It does not ask how to fix the findings or wait for you to sort them into now / later / notes. The next chat does that work when you say **Do T-004**.

## 0.4.1 — 2026-08-22

Tables and figures that go into the **paper** follow a shared APA 7 list. Posters and talks do not. R scripts get a manuscript ggplot helper; the Quarto file supplies the number and title. **Review the manuscript** checks the list as editorial findings. An audit still checks whether a display can be read as evidence; missing italics or extra lines do not fail the two statuses.

## 0.4.0 — 2026-08-22

Start can choose Stata as well as R. If you chose Stata, you can say **Run approved Stata analysis** to run one named `.do` file for an agreed analysis on an assigned task. Configure this computer’s Stata path; the kit does not guess it. A fresh Stata start records kit 0.4.0 and the full skill list, including this run skill. A non-zero Stata exit is a failed run even if the log looks finished; the helper reports the expected log path and does not approve the result. Word automation is still not in this version.

## 0.3.4 — 2026-08-22

An audit now reports **two** statuses in the saved file: whether numbers match, and whether the claims are supported. Passing the first does not mean the second passed. If a link cannot be checked, it is not treated as a pass. **Audit data construction** is available if you ask for it: one central claim, not part of an ordinary check. The project overview has a short Data section for source, access, coverage, and limits; that description does not override the analysis plan or approved results.

## 0.3.3 — 2026-08-22

The design note now states plainly that this is not an autonomous paper factory: the assistant may compare, extract, and do assigned work; researchers judge and stay accountable. Specialised methods stay optional, not the default path.

## 0.3.2 — 2026-08-21

You can **Adjust this project to the new kit version**. The assistant inspects this paper, shows the exact instruction and version-note patches, and waits for a yes. It does not edit the analysis plan, decision notes, outputs, manuscript, or data. Updating the kit still leaves every paper folder untouched until you ask.

## 0.3.1 — 2026-08-20

Acceptance is one routine: the decision note, who accepted it and when, the plan’s link to that note, the matching task, and STATUS are updated together. STATUS keeps five headings and is rewritten in place. Analysis reads processed data, not raw originals. Every result file needs a sidecar metadata record (draft until you approve it). Pilots stay in a `_dev` folder; if a file cannot be deleted, it goes to quarantine. Keys stay out of chat and out of committed files.

## 0.3.0 — 2026-08-20

Co-authors can work in a **Google Docs review copy**. Small wording is accepted there (like track changes), then you **sync** once back to the paper. Leftover **open comments**, journal points, and an **AI manuscript review** land in the same contributions inbox — not a second reviews folder, and not one file per comma. Word comment ingest is not in this version. Google’s Docs tools, if the assistant has them, are optional; a pasted comment list still works.

## 0.2.5 — 2026-08-20

A short phrase is enough. The paper `AGENTS.md` now lists which phrase opens which skill (Understand the project, Audit the research chain, Record a research decision, and the rest). How each skill works is still only in that skill file. Each skill’s short description names the same phrase, so tools that match descriptions and tools that read the table agree.

## 0.2.4 — 2026-08-20

After an audit, the full report is the saved file. Chat stays short: what holds, the four links, then a numbered list with defaults. Findings may name the kind of work; they do not draft a patch or a prompt to paste into a coding chat. Next work is **Do T-004**. What is agreed (plan and accepted notes) is always read first; a stale STATUS line is only in scope when it changes that.

## 0.2.3 — 2026-08-18

The example paper follows the kit for skills (no extra copy in the paper). Agreeing analyses is a next step after Understand the project — not a separate skill. The Quarto helpers follow the folder map. Restricted data remains a rule the assistant follows; it is not a lock on the files.

Say **Start the project**. The assistant finds the kit, writes only into the paper folder, and asks the usual questions. You do not need a longer paste.

After an audit, the assistant asks a short list — decide now, add to the task list, or later — then waits. What you accept is written on the task list (`later` if you said later), so you do not have to remember.

## 0.2.2 — 2026-08-17

After an audit, remaining work goes on the task list. Kind of work is the role for the next chat (write analysis code, record a research decision, and so on). Say **Do T-004** to assign it. The checking chat does not start the coding.

The README now says how the kit works in one place: one kit, many papers; you accept; then the file is written.

If you copied a protocol, preregistration, or draft and the overview is still empty, the assistant should draft that overview in the same reply — not put “fill the overview” on a later list — and write the file only after you accept.

You can **Update the kit** from GitHub without overwriting your name, how you asked the assistant to talk, or your R templates, and without changing any paper folder. **Update the skills** overwrites only the skills folder.

## 0.2.0 — 2026-08-17

You can ask the assistant to audit the research chain (analysis plan through claims). It diagnoses; it does not repair. The report is a record of a check, not a new source of scientific truth. You may ask for the full chain or one link.

## 0.1.1 — 2026-08-15

A short note now says how this kit sits next to national AI-in-research guidance, and where it does not try to replace it. The optional AI-use file is still off by default; that does not mean material use may stay hidden in the paper. Restricted data still means row-level files stay closed; a cloud assistant may still send project text to a vendor.

## 0.1.0 — 2026-08-15

Frozen v0.1: skills, `layout.yml` presets, Quarto and R stubs, data-use policy, toy study, and file-assertion tests T1–T13.

Lean project memory: overview + analysis plan + status; `decisions/INDEX.md`; collaborator inbox (`contributions/`); working `notes/` not loaded by default. Keep the name `ANALYSIS_PLAN.md`. AI-use stays one optional file per event.

Usual start is an existing draft: copy into `06-docs/` and `05-outputs/manuscript/`; assistant reads those files before next steps; drafts; researcher accepts; assistant writes. No reconstructed pre-history of decisions or AI use.

Start path: one kit folder; papers follow it unless they add an override file. Interview asks questions with defaults, then waits. First-level folders are numbered (`01-data` … `07-record`). The manuscript is `05-outputs/manuscript/`. Papers use `AGENTS.md` (no `CLAUDE.md`). Agent sessions need the kit visible. No Python or R required.

The public kit is researcher-facing. Workshop files (`dev/`, including the spec and the “update the changelog” habit, plus tests) stay on the builder machine and are removed if they appear in a copy.
