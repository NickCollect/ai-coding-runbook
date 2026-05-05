#!/usr/bin/env python3
"""Find raw files in 01_Raw/ that don't yet have a corresponding summary in 02_Wiki/Summaries/.
Also detects rogue/empty files accidentally created by agents outside legitimate directories.

Run at session start (CLAUDE.md hooks this) so the LLM sees:
    📋 待 ingest: N 个文件
"""
from __future__ import annotations
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "01_Raw"
SUMMARIES = ROOT / "02_Wiki" / "Summaries"

LEGITIMATE_TOP = {
    "01_Raw", "02_Wiki", "03_Output", "scripts", "docs",
    ".git", ".github", ".obsidian", ".claude", ".claudian", ".venv",
}
LEGITIMATE_ROOT_FILES = {"CLAUDE.md", "AGENTS.md", "README.md", "system_instructions.md"}


def list_raw_files() -> list[Path]:
    """List every .md file under 01_Raw/, following symlinks (defensive)."""
    files: list[Path] = []
    for p in RAW.rglob("*.md"):
        rel = p.relative_to(RAW)
        if any(part.startswith("_") or part.startswith(".") for part in rel.parts):
            continue
        files.append(p)
    return files


def list_summaries() -> set[str]:
    """Return the set of raw paths (relative to repo root) covered by existing summaries.

    Priority: parse the `source:` frontmatter field in each summary.
    Fallback: use the summary stem (matches only when naming is 1-to-1).
    """
    if not SUMMARIES.exists():
        return set()
    covered: set[str] = set()
    for p in SUMMARIES.rglob("*.md"):
        if p.name.startswith("_"):
            continue
        source_val: str | None = None
        try:
            with p.open(encoding="utf-8") as fh:
                in_front = False
                for i, line in enumerate(fh):
                    if i == 0 and line.strip() == "---":
                        in_front = True
                        continue
                    if in_front:
                        if line.strip() == "---":
                            break
                        if line.startswith("source:"):
                            source_val = line[len("source:"):].strip().strip('"').strip("'")
                            break
                    if i > 25:
                        break
        except OSError:
            pass
        if source_val:
            covered.add(source_val.lstrip("/").replace("\\", "/"))
        else:
            covered.add(p.stem)
    return covered


def check_rogue_files() -> list[str]:
    """Detect empty or misplaced .md files that agents may have accidentally created."""
    issues = []
    for p in ROOT.rglob("*.md"):
        try:
            rel = p.relative_to(ROOT)
        except ValueError:
            continue
        top = rel.parts[0] if len(rel.parts) > 1 else ""
        name = rel.name

        # Files at root level — only known files allowed
        if len(rel.parts) == 1:
            if name not in LEGITIMATE_ROOT_FILES:
                issues.append(f"ROGUE ROOT FILE: {rel}  ({p.stat().st_size} bytes)")
            continue

        # Files inside unknown top-level dirs
        if top not in LEGITIMATE_TOP:
            issues.append(f"ROGUE FILE: {rel}  ({p.stat().st_size} bytes)")
            continue

        # Empty .md files outside 01_Raw and hidden dirs
        if top not in {"01_Raw", ".git", ".claude", ".claudian", ".venv", ".obsidian"} and \
                p.stat().st_size == 0:
            issues.append(f"EMPTY FILE: {rel}")

    return issues


def main() -> int:
    # --- Rogue file check ---
    rogue = check_rogue_files()
    if rogue:
        print("⚠️  流氓/空文件（agent 误写，需手动删除）：")
        for r in rogue:
            print(f"  {r}")
        print()

    # --- Pending ingest check ---
    raw_files = list_raw_files()
    covered = list_summaries()

    def is_covered(p: Path) -> bool:
        rel_from_root = str(p.relative_to(ROOT)).replace("\\", "/")
        if rel_from_root in covered:
            return True
        return p.stem in covered

    pending = [p for p in raw_files if not is_covered(p)]

    if not pending:
        print(f"✅ 无 pending（{len(raw_files)} raw，{len(covered)} summaries）")
        return 0

    print(f"📋 待 ingest: {len(pending)} 个文件 (共 {len(raw_files)} raw)")
    print()
    by_source: dict[str, list[Path]] = {}
    for p in pending:
        rel = p.relative_to(RAW)
        source = rel.parts[0] if rel.parts else "(root)"
        by_source.setdefault(source, []).append(p)
    for source, files in sorted(by_source.items()):
        print(f"  {source}: {len(files)} files")
        for p in files[:5]:
            print(f"    - {p.relative_to(RAW)}")
        if len(files) > 5:
            print(f"    ... ({len(files) - 5} more)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
