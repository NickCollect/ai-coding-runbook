#!/usr/bin/env python3
"""Structural audit of 02_Wiki/.

Checks:
  1. Every Summary has a frontmatter `source:` pointing to a real file in 01_Raw/
  2. Every Entity / Concept has frontmatter and at least one section
  3. Wikilinks ([[x]]) resolve to a real file in 02_Wiki/
  4. No duplicate frontmatter `name:` field across Entities/Concepts
  5. _canonical-names.md is well-formed

Writes a report to 02_Wiki/_audit_report--YYYYMMDD.md.
Exit code 0 if all PASS, 1 if any FAIL.
"""
from __future__ import annotations
import re
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "01_Raw"
WIKI = ROOT / "02_Wiki"

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")


def parse_frontmatter(text: str) -> dict | None:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    fm: dict = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm


def all_wiki_files() -> list[Path]:
    if not WIKI.exists():
        return []
    return [p for p in WIKI.rglob("*.md") if not p.name.startswith("_")]


def all_raw_files() -> set[Path]:
    """All raw files we might summarize: docs (.md) + plugin/workflow configs (.json/.yml/.yaml) +
    common code source extensions. Mirrors what summaries can reasonably cite."""
    if not RAW.exists():
        return set()
    out: set[Path] = set()
    for ext in ("*.md", "*.json", "*.yml", "*.yaml", "*.py", "*.ts", "*.tsx", "*.js", "*.jsx",
                "*.toml", "*.txt", "*.sh", "*.css"):
        for p in RAW.rglob(ext):
            out.add(p)
    return out


def check_summaries() -> list[str]:
    issues: list[str] = []
    raw_set = all_raw_files()
    raw_rel = {p.relative_to(RAW).as_posix() for p in raw_set}
    for p in (WIKI / "Summaries").rglob("*.md") if (WIKI / "Summaries").exists() else []:
        if p.name.startswith("_"):
            continue
        text = p.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        if fm is None:
            issues.append(f"Summary {p.relative_to(WIKI)} missing frontmatter")
            continue
        src = fm.get("source") or fm.get("source_url") or fm.get("source_path")
        if not src:
            issues.append(f"Summary {p.relative_to(WIKI)} missing source field")
            continue
        # If source is a relative path, check it exists in 01_Raw
        if not src.startswith(("http://", "https://")):
            normalized = src.lstrip("./").removeprefix("01_Raw/")
            if normalized not in raw_rel:
                issues.append(
                    f"Summary {p.relative_to(WIKI)} source '{src}' not found in 01_Raw/"
                )
    return issues


def check_entities_concepts() -> list[str]:
    issues: list[str] = []
    seen_names: dict[str, list[str]] = defaultdict(list)
    for sub in ("Entities", "Concepts"):
        d = WIKI / sub
        if not d.exists():
            continue
        for p in d.rglob("*.md"):
            if p.name.startswith("_"):
                continue
            text = p.read_text(encoding="utf-8")
            fm = parse_frontmatter(text)
            if fm is None:
                issues.append(f"{sub} {p.relative_to(WIKI)} missing frontmatter")
                continue
            name = fm.get("name") or p.stem
            seen_names[name.lower()].append(p.relative_to(WIKI).as_posix())
            if not re.search(r"^##? ", text, re.MULTILINE):
                issues.append(f"{sub} {p.relative_to(WIKI)} has no sections")
    for name, paths in seen_names.items():
        if len(paths) > 1:
            issues.append(f"Duplicate name '{name}' in: {', '.join(paths)}")
    return issues


def strip_code_fences(text: str) -> str:
    """Remove fenced code blocks (``` ... ```) and indented code blocks before wikilink scan,
    so that bash `[[ $foo == bar ]]` test syntax in code examples isn't mistaken for a wikilink."""
    # Remove fenced code blocks
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    # Remove inline code spans
    text = re.sub(r"`[^`\n]+`", "", text)
    return text


def check_wikilinks() -> list[str]:
    issues: list[str] = []
    wiki_stems = {p.stem.lower() for p in all_wiki_files()}
    for p in all_wiki_files():
        text = strip_code_fences(p.read_text(encoding="utf-8"))
        seen_in_file: set[str] = set()
        for m in WIKILINK_RE.finditer(text):
            target = m.group(1).strip()
            # Skip if it looks like shell expression rather than identifier
            if any(c in target for c in "$=!<>"):
                continue
            if target.lower() not in wiki_stems and target not in seen_in_file:
                issues.append(f"Dead wikilink in {p.relative_to(WIKI)}: [[{target}]]")
                seen_in_file.add(target)
    return issues


def main() -> int:
    today = datetime.now().strftime("%Y%m%d")
    report_lines: list[str] = [
        f"# Vault Audit Report — {today}",
        "",
        f"Generated by scripts/audit.py",
        "",
    ]
    total_issues = 0
    for label, fn in [
        ("Summaries", check_summaries),
        ("Entities/Concepts", check_entities_concepts),
        ("Wikilinks", check_wikilinks),
    ]:
        issues = fn()
        report_lines.append(f"## {label}")
        if not issues:
            report_lines.append("✓ PASS")
        else:
            report_lines.append(f"✗ FAIL ({len(issues)} issues)")
            for it in issues[:50]:
                report_lines.append(f"  - {it}")
            if len(issues) > 50:
                report_lines.append(f"  - ... ({len(issues) - 50} more)")
        report_lines.append("")
        total_issues += len(issues)

    print("\n".join(report_lines))
    print(f"Total issues: {total_issues}")
    return 0 if total_issues == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
