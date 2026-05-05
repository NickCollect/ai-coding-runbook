---
type: summary
source: 01_Raw/code.claude.com/docs/en/debug-your-config.md
source_url: https://code.claude.com/docs/en/debug-your-config
title: "Debug your configuration"
summarized_at: 2026-05-05
entities_referenced: [Settings, Memory, Hooks, MCP-server, Skill, Subagent, Permission-mode, Sandboxing, Slash-command]
concepts_referenced: []
---

Diagnostic page for "Claude ignored my X" / "feature not loading" issues. Covers the inspection commands and the most common location/syntax mistakes.

**Inspection slash commands**:
- `/context` — full breakdown of what's in the context window (system prompt, memory files, skills, MCP tools, messages)
- `/memory` — which CLAUDE.md and rules files loaded, plus auto-memory entries
- `/skills` — available skills (project + user + plugin)
- `/agents` — configured subagents
- `/hooks` — active hook configs
- `/mcp` — connected MCP servers + status
- `/permissions` — resolved allow/deny rules currently in effect
- `/doctor` — schema/config validation, install health
- `/status` — active settings sources (incl. managed settings)

**Subdirectory `CLAUDE.md` files load on demand** when Claude reads a file in that directory via the Read tool — NOT at session start, NOT when writing/creating files.

CLAUDE.md vs. permissions/hooks distinction: CLAUDE.md is *guidance*; permissions and hooks are *enforcement*. Use the latter when you need a guarantee.

**Settings precedence**: managed > local > project > user, with CLI flags / env vars layered on top.

**MCP server pitfalls**: project servers in `.mcp.json` need one-time approval (dismissed prompt → server stays disabled); relative paths in `command`/`args` resolve from launch dir, not `.mcp.json` location; servers showing "connected, 0 tools" → `Reconnect`; `claude --debug mcp` for stderr.

**Hook pitfalls**: hooks live under `"hooks"` key in `settings.json`, NOT a standalone `hooks.json`. `matcher` is a single string with `|` for alternation (`"Edit|Write"`), array values are schema errors that get dropped. Tool names case-sensitive: `Bash`, `Edit`, `Write`, `Read`. `claude --debug hooks` watches evaluation live.

**Common-cause table** (highlights):
| Symptom | Cause | Fix |
|---|---|---|
| Hook never fires | matcher is JSON array | use single string with `\|` |
| Hook never fires | matcher is lowercase `"bash"` | use capitalized `"Bash"` |
| `permissions`/`hooks`/`env` ignored | added to `~/.claude.json` | move to `~/.claude/settings.json` (different file!) |
| `settings.json` value ignored | same key in `settings.local.json` | local overrides project overrides user |
| Skill missing from `/skills` | `.claude/skills/name.md` flat | use `.claude/skills/name/SKILL.md` folder |
| Skill never invokes | `disable-model-invocation: true` or description mismatch | check "user-only" badge |
| Subagent ignores CLAUDE.md | subagents don't always inherit project memory | put critical rules in agent body |
| `.mcp.json` never loads | put under `.claude/` or used Desktop format | repo root, Claude Code format |
| MCP env vars missing | placed in settings.json `env` | use per-server `env` in `.mcp.json` |
| `Bash(rm *)` deny doesn't block `/bin/rm` / `find -delete` | prefix rules match literal command string | add explicit patterns or use PreToolUse hook / sandbox |
