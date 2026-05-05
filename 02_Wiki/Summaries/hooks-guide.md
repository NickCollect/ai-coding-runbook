---
type: summary
source: 01_Raw/code.claude.com/docs/en/hooks-guide.md
source_url: https://code.claude.com/docs/en/hooks-guide
title: "Automate workflows with hooks"
summarized_at: 2026-05-05
entities_referenced: [Hooks, Settings, Skill, Subagent, Plugin, Permission-mode, MCP-server, Memory]
concepts_referenced: [Agent-team]
---

User-facing guide to Claude Code hooks (the reference is `/en/hooks`). Hooks are user-defined shell commands (or HTTP/MCP/prompt/agent invocations) that fire at lifecycle points and give **deterministic** control vs LLM-judgment. Use to enforce rules, automate, integrate.

**Hook types** (`type:` field):
- `command` — shell command (most common). Communicates via stdin/stdout/stderr/exit code.
- `http` — POST event JSON to a URL. Decisions returned in response body. Header env-var interpolation requires `allowedEnvVars` allowlist.
- `mcp_tool` — call a tool on a connected MCP server.
- `prompt` — single-turn LLM call (Haiku default). Returns `{ok, reason}`. For judgment-based decisions.
- `agent` — multi-turn subagent with tool access (60s default timeout, ≤50 tool turns, **experimental**). For verification needing codebase inspection.

**Lifecycle events** (extensive list):
SessionStart, Setup, UserPromptSubmit, UserPromptExpansion, PreToolUse, PermissionRequest, PermissionDenied, PostToolUse, PostToolUseFailure, PostToolBatch, Notification, SubagentStart, SubagentStop, TaskCreated, TaskCompleted, Stop, StopFailure, TeammateIdle, InstructionsLoaded, ConfigChange, CwdChanged, FileChanged, WorktreeCreate, WorktreeRemove, PreCompact, PostCompact, Elicitation, ElicitationResult, SessionEnd.

**Common patterns** (each shown with ready-to-use JSON):
- Desktop notification on `Notification` (osascript / notify-send / PowerShell). Matchers like `permission_prompt`, `idle_prompt`.
- Auto-format with Prettier on `PostToolUse` matcher `Edit|Write` using `jq -r '.tool_input.file_path' | xargs npx prettier --write`.
- Block protected files (`.env`, `package-lock.json`, `.git/`) via `PreToolUse` script that exits 2 with stderr message.
- Re-inject context after compaction: `SessionStart` matcher `compact` echoes reminders to stdout.
- Audit `ConfigChange` events to a log; matcher filters by source (`user_settings`/`project_settings`/`local_settings`/`policy_settings`/`skills`).
- Reload env on directory change: `SessionStart` + `CwdChanged` writing `direnv export bash > $CLAUDE_ENV_FILE`. Or `FileChanged` with matcher `.envrc|.env`.
- Auto-approve `ExitPlanMode` via `PermissionRequest` returning JSON `{decision:{behavior:"allow"}}`. Can also flip mode via `updatedPermissions: [{type:"setMode", mode:"acceptEdits", destination:"session"}]`.

**Communication protocol**:
- Input on stdin: JSON with `session_id`, `cwd`, `hook_event_name`, plus event-specific fields (e.g. `tool_name`, `tool_input` for `PreToolUse`).
- Output via exit code: `0` proceed (stdout becomes context for SessionStart/UserPromptSubmit/etc.), `2` block (stderr → Claude as feedback), other → proceed but log error.
- Or: exit 0 + JSON to stdout for structured control. `PreToolUse` `permissionDecision`: `allow` / `deny` / `ask` / `defer` (headless only).
- `allow` skips interactive prompt but does NOT override deny rules from settings/managed policy. Hooks tighten, never loosen.

**Matchers**: regex on a field that varies by event (`tool_name` for tool events, source/reason for lifecycle, server name for elicitation, etc.). Empty/missing matcher = always fire. Pipe alternation: `Edit|Write`. MCP tools: `mcp__server__tool` naming, `mcp__github__.*` matches all of one server.

**`if` field** (v2.1.85+): permission-rule syntax (`Bash(git *)`, `Edit(*.ts)`) for finer filtering than `matcher`. Only on tool events. Compound bash commands evaluated per subcommand.

**Locations / scope**:
- `~/.claude/settings.json` — all your projects, local.
- `.claude/settings.json` — single project, committed.
- `.claude/settings.local.json` — single project, gitignored.
- Managed policy — org-wide.
- Plugin `hooks/hooks.json` — bundled with plugin.
- Skill / agent frontmatter — active while skill or agent is running.

`/hooks` shows configured hooks (read-only browser). `disableAllHooks: true` to nuke. File watcher reloads on edits.

**Decision merging when multiple hooks match**: most restrictive wins. `deny` from any beats all `allow`s. `additionalContext` from every hook is concatenated.

**Limitations**:
- Hooks can't trigger slash commands or tool calls — only return text/decisions.
- Default 10-min timeout per hook.
- `PostToolUse` can't undo (already executed).
- `PermissionRequest` doesn't fire in headless `-p` mode — use `PreToolUse`.
- Multiple `updatedInput` rewrites: last hook to finish wins (parallel execution).

**Permission-mode interaction**: `PreToolUse` deny blocks **even in `bypassPermissions`** or `--dangerously-skip-permissions`. Hooks tighten, can't loosen past permission rules.

**Common bugs**:
- JSON parse errors from echo statements in `~/.zshrc` — guard with `if [[ $- == *i* ]]; then echo ...`.
- Stop hook infinite loop — check `stop_hook_active` in input and exit 0 early.
- Hook not firing — `/hooks` to verify, check matcher case-sensitive, confirm event type.

Debug: `claude --debug-file /tmp/claude.log` then `tail -f`. Or `/debug` mid-session. Transcript view (`Ctrl+O`) shows per-hook one-line summaries.
