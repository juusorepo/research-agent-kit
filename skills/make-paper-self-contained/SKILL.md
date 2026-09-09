---
name: make-paper-self-contained
description: Write generated kit files into this paper so an assistant can work from this folder without opening the kit. Use when they say Make this paper self-contained.
license: MIT
compatibility: Requires a project filesystem. No Python or R required. Needs the kit folder readable to copy from.
metadata:
  version: "0.1.1"
---

# Make this paper self-contained

One job. Copy generated kit files into **this paper** so an assistant that can see only this folder can still follow the workflow. Do not edit science files.

They are in **one paper** folder. The kit must be readable: `kit_path`, or the kit is also open, or a **temporary** GitHub extract (ZIP/clone outside this paper). Do not clone the public kit into this paper.

Follow `policies/how-to-talk.md` if present. Say *make this paper self-contained*. Do not say runtime, bundle, or migrate unless they used those words.

**This file is complete.** Do not search workshop files or the toy example to learn how to copy.

---

## When to use

They say **Make this paper self-contained** (or mean that: this paper must work when ChatGPT, a co-author, or NotebookLM cannot see the kit folder).

**Start the project** also runs the copy below when they said this paper should work without the kit folder. Do not wait a second time in that run.

If they are in the **kit** folder (`START.md` + `skills/` + `templates/`): **stop**. Ask them to open the paper.

If you cannot read a local kit: fetch the public kit into a **temporary** folder (see `skills/update-the-kit/SKILL.md` fetch steps) and copy from there, then delete the temporary folder. If they refused GitHub and there is no kit: **stop**. Ask them to open the kit or paste the GitHub URL.

---

## Must not edit

Never write these, even after they accept:

- Overview, analysis plan, decision notes, outputs, manuscript, data, scripts
- Contributions, notes, audits, proposals, AI-use events
- `layout.yml` (except you may add missing `paths.sources` / `paths.source_records` only if those keys are absent — do not rename existing paths)
- `policies/data-policy.md` and `data_access`
- `policies/what-is-on.md` ticks
- `TASKS.md`
- `.agents/skills/` (paper forks stay)

Do not invent analyses. Do not approve results.

---

## Propose, then wait

(Skip this wait when **Start the project** already has their yes to work without the kit folder.)

In one short message:

- This paper will get **generated kit files** under `.rak/runtime/` and a generated `AGENTS.md`. Those files are replaced later with **Update the kit** from GitHub, or **Adjust this project to the new kit version** if the kit folder is open. Do not edit them.
- Science files, data-use rules, and ticks stay as they are.
- If this paper already has a long `AGENTS.md` they wrote themselves: it will be **replaced** by the generated file. If they need extra instructions, those belong in `policies/how-to-talk.md` or `.agents/skills/`.

Then wait for yes, unless this copy is part of Start after they already answered.

---

## Copy (after yes)

Read `templates/runtime/layers.yml` in the **kit**. Copy only what that file lists, plus the generated `AGENTS.md`.

1. Create `.rak/runtime/skills/`, `.rak/runtime/policies/`, `.rak/runtime/templates/` as needed.
2. For each skill name in `core.skills`, `profile.skills`, and `audit.skills`: copy `skills/<name>/` from the kit to `.rak/runtime/skills/<name>/`. Overwrite generated copies. Include skill `references/` subfolders.
3. If `layout.yml` has `code: stata`, also copy `profile.skills_if_stata`.
4. If `manuscript_format` is `word` or `quarto`, also copy `profile.skills_if_word_render` (Quarto papers still render Word for the review copy).
5. Copy kit `policies/how-to-talk.md` and `policies/ai-policy.md` to `.rak/runtime/policies/`. Do **not** overwrite this paper’s `policies/` if those files already exist there.
6. If `code: r` (default), copy `templates/analysis/r/` and `templates/analysis/manuscript-displays.md` into `.rak/runtime/templates/analysis/`. If `code: stata`, copy the Stata templates the same way.
7. Copy kit `templates/runtime/AGENTS.md` onto **this paper’s** `AGENTS.md` (replace). Also copy it to `.rak/runtime/AGENTS.md`.
8. Copy kit `templates/project/kit-lock.yml` onto this paper’s `kit-lock.yml` **only for** `kit:` and `skills:` (do not invent numbers). Set `runtime: materialised`. Keep `update_policy:` if already present; otherwise write `update_policy: latest-compatible`. Keep any extra top-level keys this paper already had. Do not delete paper-only keys.
9. Write `.rak/runtime.manifest.json`: kit version, `generated_at` (ISO date), and every generated file path with `sha256` and `layer` (`core` / `profile` / `audit`). Include the paper-root `AGENTS.md`. Use SHA-256 of file bytes (PowerShell `Get-FileHash -Algorithm SHA256`, or `sha256sum`).
10. If `STATUS.md` exists, under existing headings add or refresh **one factual line** that this paper now has generated kit files so an assistant can work from this folder alone. Do not rewrite other STATUS content.

If a file already under `.rak/runtime/` or the paper-root `AGENTS.md` is listed in an existing manifest but the hash no longer matches: **stop** before overwrite. Offer (1) discard the edit and copy, or (2) move the file to `.agents/skills/` or paper `policies/` and then copy. Do not three-way merge.

#### Copy skills (Windows PowerShell)

```powershell
$kit = "<kit folder>"
$paper = "<paper folder>"
$names = @("<skill-name>", "<skill-name>")
New-Item -ItemType Directory -Force -Path (Join-Path $paper ".rak\runtime\skills") | Out-Null
foreach ($n in $names) {
  $dest = Join-Path $paper ".rak\runtime\skills\$n"
  if (Test-Path $dest) { Remove-Item -Recurse -Force $dest }
  Copy-Item -Recurse -Force (Join-Path $kit "skills\$n") $dest
}
```

#### Copy skills (Unix)

```bash
mkdir -p "$paper/.rak/runtime/skills"
for n in skill-name skill-name; do
  rm -rf "$paper/.rak/runtime/skills/$n"
  cp -R "$kit/skills/$n" "$paper/.rak/runtime/skills/$n"
done
```

Do not copy `dev/`, tests, examples, SPEC, `start-research-project`, `adjust-project-to-kit`, or this skill into the paper. Copy `update-the-kit` only because `layers.yml` lists it under core (paper-only GitHub refresh).

---

## Afterward

Say: this paper’s generated kit files are in place. An assistant can work from this folder without the kit. To refresh those files, say **Update the kit from https://github.com/juusorepo/research-agent-kit** (temporary fetch; not a full clone). **Adjust this project** still works if the kit folder is open. Do not edit `.rak/runtime/` or the generated `AGENTS.md`. Understand the project is the next message if they just started.

If this paper already had a Google Drive synced folder, they can share **this folder** with co-authors and point NotebookLM at `sources/` **inside it**. Do not copy sources elsewhere.

---

## Must not

- Edit science files, data-use rules, or ticks
- Copy the whole kit, `CLAUDE.md`, or workshop files
- Three-way merge `AGENTS.md`
- Require Python
- Treat generated files as the analysis plan or as approved results
- Upload confidential files to an external tool
- Invent numbers, analyses, or citation keys
