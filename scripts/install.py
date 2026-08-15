#!/usr/bin/env python3
"""Optional copy helper. Researchers do not need this — see START.md.

Usage:
  python scripts/install.py TARGET
  python scripts/install.py TARGET --init --paper toy-study
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

KIT_VERSION = "0.1.0"
SKILLS = (
    "start-research-project",
    "understand-research-project",
    "develop-analysis-with-safe-data",
    "document-research-decision",
    "update-project-record",
    "contribute-to-project",
    "consolidate-contributions",
)
REQUIRED_PATH_KEYS = (
    "docs",
    "scripts",
    "outputs",
    "manuscript",
    "overview",
    "analysis_plan",
    "status",
    "tasks",
)


def kit_root() -> Path:
    return Path(__file__).resolve().parent.parent


def copy_tree(src: Path, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if src.is_dir():
        if dest.exists():
            shutil.rmtree(dest)
        shutil.copytree(src, dest)
    else:
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)


def write_kit_lock(target: Path) -> None:
    lines = ["kit: " + KIT_VERSION, "skills:"]
    for name in SKILLS:
        lines.append(f"  {name}: {KIT_VERSION}")
    (target / "kit-lock.yml").write_text("\n".join(lines) + "\n", encoding="utf-8")


def install_core(target: Path, adapters: list[str]) -> None:
    root = kit_root()
    for name in SKILLS:
        copy_tree(root / "skills" / name, target / ".agents" / "skills" / name)
    copy_tree(root / "policies" / "data-policy.md", target / "policies" / "data-policy.md")
    copy_tree(root / "policies" / "how-to-talk.md", target / "policies" / "how-to-talk.md")
    copy_tree(root / "policies" / "what-is-on.md", target / "policies" / "what-is-on.md")
    copy_tree(root / "templates" / "project" / "AGENTS.md", target / "AGENTS.md")
    gitignore_src = root / "templates" / "project" / ".gitignore"
    if gitignore_src.exists() and not (target / ".gitignore").exists():
        shutil.copy2(gitignore_src, target / ".gitignore")
    write_kit_lock(target)

    if "claude" in adapters:
        copy_tree(root / "adapters" / "claude" / "CLAUDE.md", target / "CLAUDE.md")
    if "cursor" in adapters:
        copy_tree(
            root / "adapters" / "cursor" / "research-agent-kit.mdc",
            target / ".cursor" / "rules" / "research-agent-kit.mdc",
        )


def set_policy_fields(target: Path, data_access: str) -> None:
    path = target / "policies" / "data-policy.md"
    text = path.read_text(encoding="utf-8")
    text = text.replace("data_access: restricted", f"data_access: {data_access}", 1)
    path.write_text(text, encoding="utf-8")


def write_layout(
    target: Path,
    *,
    preset: str,
    paper: str,
    code: str,
    manuscript: str,
) -> Path:
    root = kit_root()
    src = root / "templates" / "layout" / f"{preset}.yml"
    if not src.exists():
        raise SystemExit(f"Unknown preset: {preset}")
    text = src.read_text(encoding="utf-8")
    text = text.replace("PAPER_SLUG", paper)
    text = text.replace("code: r", f"code: {code}", 1)
    text = text.replace("manuscript_format: quarto", f"manuscript_format: {manuscript}", 1)
    dest = target / "layout.yml"
    dest.write_text(text, encoding="utf-8")
    return dest


def resolve_path(template: str, paper: str) -> str:
    return template.replace("{paper}", paper)


def init_project(
    target: Path,
    *,
    paper: str,
    preset: str,
    code: str,
    manuscript: str,
    data_access: str,
    lead_researcher: str,
    adapters: list[str],
) -> None:
    root = kit_root()
    target.mkdir(parents=True, exist_ok=True)
    install_core(target, adapters)
    set_policy_fields(target, data_access)
    write_layout(
        target, preset=preset, paper=paper, code=code, manuscript=manuscript
    )

    layout_text = (target / "layout.yml").read_text(encoding="utf-8")
    paths = {}
    in_paths = False
    for raw in layout_text.splitlines():
        line = raw.rstrip()
        if line.startswith("paths:"):
            in_paths = True
            continue
        if in_paths:
            if line and not line.startswith(" ") and not line.startswith("\t"):
                break
            if ":" in line:
                key, val = line.split(":", 1)
                paths[key.strip()] = val.strip()

    def p(key: str) -> Path:
        if key not in paths:
            raise SystemExit(f"layout.yml missing paths.{key}")
        return target / resolve_path(paths[key], paper)

    for key, rel in paths.items():
        dest = target / resolve_path(rel, paper)
        if dest.suffix:
            dest.parent.mkdir(parents=True, exist_ok=True)
        else:
            dest.mkdir(parents=True, exist_ok=True)

    docs = p("docs")
    if not any(docs.iterdir()) if docs.is_dir() else True:
        docs.mkdir(parents=True, exist_ok=True)
        (docs / ".gitkeep").write_text("", encoding="utf-8")

    folders_src = root / "templates" / "project" / "folders.md"
    if folders_src.exists() and not (target / "FOLDERS.md").exists():
        shutil.copy2(folders_src, target / "FOLDERS.md")
    raw_readme = root / "templates" / "project" / "data-raw-README.md"
    if raw_readme.exists() and "data_raw" in paths:
        dest_raw = p("data_raw") / "README.md"
        if not dest_raw.exists():
            dest_raw.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(raw_readme, dest_raw)

    for key, template_name in (
        ("overview", "RESEARCH_CONTEXT.md"),
        ("analysis_plan", "ANALYSIS_PLAN.md"),
        ("status", "STATUS.md"),
        ("tasks", "TASKS.md"),
    ):
        dest = p(key)
        dest.parent.mkdir(parents=True, exist_ok=True)
        if not dest.exists():
            text = (root / "templates" / "project" / template_name).read_text(encoding="utf-8")
            if lead_researcher:
                text = text.replace("Lead researcher:", f"Lead researcher: {lead_researcher}", 1)
                text = text.replace("- Name:", f"- Name: {lead_researcher}", 1)
            dest.write_text(text, encoding="utf-8")

    memory_src = root / "templates" / "project" / "MEMORY.md"
    if memory_src.exists() and not (target / "MEMORY.md").exists():
        shutil.copy2(memory_src, target / "MEMORY.md")

    def copy_into(dir_key: str, *rel_files: str) -> None:
        if dir_key not in paths:
            return
        dest_dir = p(dir_key)
        dest_dir.mkdir(parents=True, exist_ok=True)
        for rel in rel_files:
            src = root / "templates" / rel
            if src.exists():
                dest = dest_dir / src.name
                if not dest.exists():
                    shutil.copy2(src, dest)

    copy_into("decisions", "decisions/INDEX.md")
    if "decisions" in paths:
        rdr_template = p("decisions") / "RDR-000-template.md"
        src_rdr = root / "templates" / "decision-note.md"
        if src_rdr.exists() and not rdr_template.exists():
            shutil.copy2(src_rdr, rdr_template)
    copy_into("contributions", "contributions/README.md", "contributions/template.md")
    copy_into("notes", "notes/README.md")

    ms_src = root / "templates" / "manuscript" / manuscript
    if ms_src.exists():
        for item in ms_src.iterdir():
            dest = p("manuscript") / item.name
            if item.is_file() and not dest.exists():
                shutil.copy2(item, dest)
    else:
        (p("manuscript") / "README.md").write_text(
            f"{manuscript} manuscript folder reserved. Template not shipped in v0.1.\n",
            encoding="utf-8",
        )

    code_src = root / "templates" / "analysis" / code
    if code_src.exists():
        for item in code_src.iterdir():
            dest = p("scripts") / item.name
            if item.is_file() and not dest.exists():
                shutil.copy2(item, dest)
    else:
        (p("scripts") / "README.md").write_text(
            f"{code} analysis folder reserved. Template not shipped in v0.1.\n",
            encoding="utf-8",
        )

    reserved_notes = []
    if manuscript == "word":
        reserved_notes.append("Word manuscript template is not shipped in v0.1.")
    if code == "stata":
        reserved_notes.append("Stata analysis template is not shipped in v0.1.")
    if reserved_notes:
        print("Note: " + " ".join(reserved_notes), file=sys.stderr)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Install Research Agent Kit into a paper repo.")
    parser.add_argument("target", type=Path, help="Destination project folder")
    parser.add_argument("--init", action="store_true", help="Create layout.yml and paper folders")
    parser.add_argument("--paper", default="paper-1", help="First paper name")
    parser.add_argument(
        "--preset",
        choices=("numbered", "numbered-multipaper", "by-paper"),
        default="numbered",
    )
    parser.add_argument("--code", choices=("r", "stata"), default="r")
    parser.add_argument("--manuscript", choices=("quarto", "markdown", "word"), default="quarto")
    parser.add_argument(
        "--data-access",
        dest="data_access",
        choices=("restricted", "agent-accessible"),
        default="restricted",
    )
    parser.add_argument("--lead-researcher", default="")
    parser.add_argument(
        "--adapters",
        default="claude,cursor",
        help="Comma-separated: claude,cursor (or empty)",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    target = args.target.resolve()
    adapters = [a.strip() for a in args.adapters.split(",") if a.strip()]
    if args.init:
        init_project(
            target,
            paper=args.paper,
            preset=args.preset,
            code=args.code,
            manuscript=args.manuscript,
            data_access=args.data_access,
            lead_researcher=args.lead_researcher,
            adapters=adapters,
        )
    else:
        target.mkdir(parents=True, exist_ok=True)
        install_core(target, adapters)
    print(f"Installed Research Agent Kit {KIT_VERSION} -> {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
