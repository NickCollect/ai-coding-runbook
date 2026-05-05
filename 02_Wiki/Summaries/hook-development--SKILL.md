---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/plugin-dev/skills/hook-development/SKILL.md
title: "Hook Development for Claude Code Plugins (skill)"
summarized_at: 2026-05-05
entities_referenced: [Hooks, Plugin, Subagent, Settings, MCP-server]
concepts_referenced: []
---

Skill in the `plugin-dev` plugin teaching how to author hooks for Claude Code plugins. Triggers on prompts about hook creation, PreToolUse/PostToolUse/Stop, validating tool use, prompt-based hooks, `${CLAUDE_PLUGIN_ROOT}`, etc.

**Two hook types** (per `type:` field):
- **Prompt-based** (recommended): LLM-driven decisions. Supported events: Stop, SubagentStop, UserPromptSubmit, PreToolUse. Default 30s timeout. Better for context-aware reasoning.
- **Command**: deterministic bash. Default 60s timeout. Use for fast checks, FS ops, external tools, perf-critical work.

**Two config formats** — important distinction:
- **Plugin `hooks/hooks.json`**: wrapper format `{"description": "...", "hooks": {"PreToolUse": [...], ...}}`. `description` optional, `hooks` field required.
- **Settings `.claude/settings.json`**: direct format — events at top level, no wrapper, no description.

**Lifecycle events**: PreToolUse, PostToolUse, Stop, SubagentStop, UserPromptSubmit, SessionStart (special: persist env via `$CLAUDE_ENV_FILE`), SessionEnd, PreCompact, Notification.

**PreToolUse decisions** via `hookSpecificOutput.permissionDecision`: `allow`/`deny`/`ask`, plus `updatedInput` to rewrite tool args. `systemMessage` shown to Claude.

**Stop decisions** via `decision: approve|block` + `reason`.

**Standard output**: `{continue: bool, suppressOutput: bool, systemMessage: str}`. Exit codes: 0=success (stdout shown), 2=blocking error (stderr → Claude), other=non-blocking.

**Hook input on stdin** — JSON with `session_id`, `transcript_path`, `cwd`, `permission_mode`, `hook_event_name`, plus event-specific fields (`tool_name`/`tool_input`/`tool_result` for tool events, `user_prompt`, `reason`).

**Env vars in command hooks**: `$CLAUDE_PROJECT_DIR`, `$CLAUDE_PLUGIN_ROOT` (always use for portability), `$CLAUDE_ENV_FILE` (SessionStart only), `$CLAUDE_CODE_REMOTE`.

**Matchers** (regex on tool name): `Write`, `Read|Write|Edit`, `*`, `mcp__.*__delete.*`, case-sensitive. Common patterns: all MCP `mcp__.*`, specific plugin `mcp__plugin_asana_.*`.

**Parallel execution**: all matching hooks run in parallel — design for independence, no ordering, no inter-hook output sharing.

**Security best practices** (command hooks):
- `set -euo pipefail`.
- Validate inputs (regex check tool_name format).
- Path traversal check (`*..*`).
- Sensitive file check (`.env`, etc.).
- Always quote variables.
- Set appropriate timeouts.

**Temporarily active hooks**: gate via flag file (`.enable-strict-validation`) or config-based (`jq` reads JSON setting).

**Hook lifecycle gotcha**: hooks load at SESSION START. Editing `hooks.json` mid-session has NO EFFECT. Must restart Claude Code (`exit` then `claude`). Use `/hooks` to see loaded.

**Debugging**: `claude --debug` for execution logs. Test scripts directly: `echo '{"tool_name":"Write",...}' | bash hook.sh; echo $?`. Validate JSON output with `jq .`.

References sibling files: `references/patterns.md`, `references/migration.md`, `references/advanced.md`, `examples/validate-write.sh`, `examples/validate-bash.sh`, `examples/load-context.sh`, plus utility scripts in `scripts/`.
