---
type: summary
source: 01_Raw/code.claude.com/docs/en/headless.md
source_url: https://code.claude.com/docs/en/headless
title: "Run Claude Code programmatically (Agent SDK CLI)"
summarized_at: 2026-05-05
entities_referenced: [Headless-mode, Agent-SDK, Permission-mode, Plugin, MCP-server, Subagent, Skill]
concepts_referenced: []
---

The `-p` (`--print`) flag runs Claude Code non-interactively — same loop, tools, context management as interactive. Previously called "headless mode."

**Basic**: `claude -p "Find and fix the bug in auth.py" --allowedTools "Read,Edit,Bash"`

**`--bare` flag**: skips auto-discovery of hooks/skills/plugins/MCP/auto-memory/CLAUDE.md → faster startup, deterministic results across machines. Only flags you pass take effect. Bare mode also skips OAuth and keychain reads — auth must come from `ANTHROPIC_API_KEY` or `apiKeyHelper` in `--settings` JSON. Recommended for scripts/CI; will become default for `-p` in future. Has Bash + file read/edit tools by default. Pass context via:
- `--append-system-prompt` / `--append-system-prompt-file`
- `--settings <file-or-json>`
- `--mcp-config <file-or-json>`
- `--agents <json>`
- `--plugin-dir <path>`

**Stdin**: `cat build-error.txt | claude -p 'explain the error' > output.txt`

**Output formats** via `--output-format`:
- `text` (default)
- `json` — `{result, session_id, total_cost_usd, ...}`
- `stream-json` — newline-delimited JSON events. Use with `--verbose --include-partial-messages` for token streaming.

**Structured output**: `--output-format json --json-schema '{"type":"object",...}'`. Result lands in `structured_output` field.

**Stream events of note**:
- `system/init` — session metadata, including `plugins` and `plugin_errors` arrays. Use `plugin_errors` to fail CI when a plugin didn't load.
- `system/api_retry` — fields: `attempt`, `max_retries`, `retry_delay_ms`, `error_status`, `error` (category enum: authentication_failed, oauth_org_not_allowed, billing_error, rate_limit, invalid_request, server_error, max_output_tokens, unknown).
- `system/plugin_install` — when `CLAUDE_CODE_SYNC_PLUGIN_INSTALL` set, fired during marketplace plugin install before first turn. `status`: started/installed/failed/completed.

**Auto-approve tools**: `--allowedTools "Bash,Read,Edit"`. For session-wide baseline use `--permission-mode`:
- `dontAsk` — denies anything not in `permissions.allow` or read-only command set (locked-down CI).
- `acceptEdits` — auto-approves writes + common FS commands (mkdir, touch, mv, cp). Other shell + network still need explicit allow.

**Permission rule syntax**: `Bash(git diff *)` — trailing space + `*` for prefix matching. Without space, `Bash(git diff*)` would also match `git diff-index`.

**Continue conversations**: `--continue` for most-recent in cwd. `--resume <session-id>` for specific. Capture session_id from JSON output: `session_id=$(claude -p "..." --output-format json | jq -r '.session_id')`.

**Custom system prompt**: `--append-system-prompt` adds to default; `--system-prompt` replaces.

**Important**: user-invoked skills (`/commit`, etc.) and built-in commands are interactive-only. In `-p` mode, describe the task instead.

For Python/TypeScript packages with structured outputs, callbacks, native message objects → see Agent SDK docs.
