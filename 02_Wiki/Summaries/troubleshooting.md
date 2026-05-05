---
type: summary
source: 01_Raw/code.claude.com/docs/en/troubleshooting.md
source_url: https://code.claude.com/docs/en/troubleshooting
title: "Troubleshooting"
summarized_at: 2026-05-05
entities_referenced: [Subagent]
concepts_referenced: [Context-window]
---

Performance, stability, and search-related issues for a running Claude Code instance. For install/login/auth issues, see Troubleshoot installation and login. For settings/hooks/MCP not loading, see Debug your configuration. For API errors, see Error reference.

**First-line diagnostic**: `/doctor` inside Claude Code (or `claude doctor` from shell if claude won't start). Checks installation health, settings validity, MCP, context usage in one pass.

**Symptom routing table** in raw maps to other troubleshooting docs (install, errors, IDE pages, etc.).

**High CPU/memory**:
1. `/compact` regularly.
2. Restart Claude Code between major tasks.
3. Add large build dirs to `.gitignore`.
4. Persistent issues: `/heapdump` writes JS heap snapshot + memory breakdown to `~/Desktop` (or home dir on Linux). Open `.heapsnapshot` in Chrome DevTools → Memory → Load. Attach both to GitHub issue.

**Auto-compaction thrashing** (`Autocompact is thrashing: the context refilled to the limit...`): compaction succeeded but file/tool output immediately refilled context multiple times. Recovery:
1. Read oversized file in smaller chunks (line range / specific function).
2. `/compact keep only the plan and the diff` — focus compaction.
3. Move large-file work to a subagent.
4. `/clear` if earlier convo no longer needed.

**Hangs/freezes**: `Ctrl+C` to cancel; if still unresponsive, close terminal and restart. Conversation preserved — `claude --resume` in same dir.

**Search issues** (Search tool / `@file` / agents / skills not finding files): bundled `ripgrep` may not run on your system. Install platform package (`brew install ripgrep`, `apt install ripgrep`, `apk add ripgrep`, `pacman -S ripgrep`, `winget install BurntSushi.ripgrep.MSVC`) and set `USE_BUILTIN_RIPGREP=0`.

**WSL slow/incomplete search**: cross-filesystem read penalties between Linux and Windows partitions. `/doctor` shows OK. Solutions: more specific search prompts (scope to dir/filetype), move project to Linux fs (`/home/`) instead of `/mnt/c/`, or run native Windows.

**Other help**: `/feedback` to report directly to Anthropic; check anthropics/claude-code GitHub issues; ask Claude directly (it has docs access).
