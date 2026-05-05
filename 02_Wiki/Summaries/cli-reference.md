---
type: summary
source: 01_Raw/code.claude.com/docs/en/cli-reference.md
source_url: https://code.claude.com/docs/en/cli-reference
title: "CLI reference"
summarized_at: 2026-05-05
entities_referenced: [Native-interface, Agent-SDK, Subagent, MCP-server, Plugin, Permission-mode, Auto-mode, Hooks, IDE-integration, Settings, Channel, Agent-team]
concepts_referenced: [Channel, Agent-team, Headless-mode]
---

Complete reference for the `claude` CLI commands and flags. `claude --help` does not list every flag — absence from help does not mean unavailable.

**Top-level commands**:
- `claude` / `claude "query"` — interactive session
- `claude -p "query"` — print mode (SDK-style, non-interactive)
- `cat file | claude -p "query"` — pipe content
- `claude -c` / `claude -r "<session>"` — continue / resume
- `claude update`, `claude install [version|stable|latest]`
- `claude auth login [--email --sso --console]` / `auth logout` / `auth status`
- `claude agents` — list configured subagents grouped by source
- `claude auto-mode defaults` / `auto-mode config` — show classifier rules JSON
- `claude mcp` — configure MCP servers
- `claude plugin` (alias `plugins`) — manage plugins; e.g. `plugin install code-review@claude-plugins-official`
- `claude project purge [path]` — delete local state (transcripts, task lists, debug logs, edit history, prompt history). Flags `--dry-run`, `-y/--yes`, `-i/--interactive`, `--all`
- `claude remote-control` — server mode for Claude.ai/Claude app control
- `claude setup-token` — long-lived OAuth token for CI/scripts (subscription required)
- `claude ultrareview [target]` — non-interactive ultrareview; `--json`, `--timeout <minutes>` (default 30)

Mistyped subcommands suggest closest match (e.g., `claude udpate` → "Did you mean claude update?").

**Notable flags** (selected from a long list):
- `--add-dir` — additional working dirs (file access only, not config discovery)
- `--agent`, `--agents '{json}'` — specify or define subagents
- `--allowedTools` / `--disallowedTools` / `--tools` — tool control (`--tools ""` disables all built-ins)
- `--append-system-prompt[-file]`, `--system-prompt[-file]` — four prompt-customization flags; replacement and append are mutually exclusive (replacement) but combinable. Prefer append to keep built-ins.
- `--bare` — minimal mode: skip auto-discovery of hooks/skills/plugins/MCP/auto-memory/CLAUDE.md; sets `CLAUDE_CODE_SIMPLE`. Bash + read + edit only.
- `--betas` — beta headers (API key only)
- `--channels`, `--dangerously-load-development-channels` — research preview
- `--chrome` / `--no-chrome` — Chrome browser integration
- `--continue`, `-c` / `--resume`, `-r` / `--from-pr <num|url>` / `--fork-session` — session control
- `--dangerously-skip-permissions` (≡ `--permission-mode bypassPermissions`)
- `--allow-dangerously-skip-permissions` — adds bypass to Shift+Tab cycle without starting in it
- `--debug "api,hooks"` (or `"!statsig,!file"`), `--debug-file <path>`
- `--effort low|medium|high|xhigh|max` — model effort level (session-scoped)
- `--exclude-dynamic-system-prompt-sections` — moves per-machine sections into first user message for prompt-cache reuse across users/machines (only with default system prompt; use with `-p`)
- `--fallback-model` — auto-fallback when overloaded (print mode)
- `--ide` — auto-connect IDE if exactly one valid available
- `--init`, `--init-only`, `--maintenance` — Setup hooks matchers
- `--include-hook-events`, `--include-partial-messages`, `--input-format`, `--output-format text|json|stream-json`
- `--json-schema` — validated structured output (print mode)
- `--max-budget-usd`, `--max-turns` — limits (print mode)
- `--mcp-config`, `--strict-mcp-config`
- `--model claude-sonnet-4-6` / aliases `sonnet`/`opus`
- `--name|-n`, `--session-id <uuid>` — naming/IDs; `/rename` mid-session
- `--no-session-persistence` (print mode)
- `--permission-mode default|acceptEdits|plan|auto|dontAsk|bypassPermissions`
- `--permission-prompt-tool` — MCP tool for non-interactive permission prompts
- `--plugin-dir` — repeatable, session-only plugin loading
- `--print|-p`, `--remote "task"`, `--remote-control|--rc`, `--teleport`
- `--replay-user-messages` (stream-json roundtrip)
- `--setting-sources user,project,local`, `--settings <file|json>`
- `--teammate-mode auto|in-process|tmux` — agent team display mode
- `--tmux[=classic]` — requires `--worktree`; uses iTerm2 native panes when available
- `--worktree|-w [name]` — start in `<repo>/.claude/worktrees/<name>`
- `--verbose`, `--version|-v`

**`--enable-auto-mode`** removed in v2.1.111 — auto mode is in `Shift+Tab` cycle by default; use `--permission-mode auto`.
