---
type: summary
source: 01_Raw/code.claude.com/docs/en/hooks.md
source_url: https://code.claude.com/docs/en/hooks
title: "Hooks reference"
summarized_at: 2026-05-05
entities_referenced: [Hooks, MCP-server, Subagent, Skill, Plugin, Settings, Permission-mode, Auto-mode, Checkpointing, Agent-team]
concepts_referenced: [Agentic-loop]
---

Reference for Claude Code hook events, configuration schema, JSON I/O, exit codes, and async/HTTP/prompt/MCP tool hooks. For hands-on intro see hooks-guide. **Note**: raw is large (~28k tokens); this summary captures the structural facts and event catalog, not every per-event schema.

**Definition**: hooks are user-defined shell commands, HTTP endpoints, or LLM prompts (also MCP tools, subagents) that execute automatically at specific Claude Code lifecycle points. **Deterministic** (vs. model-discretionary tool calls).

**Hook lifecycle event catalog** (cadence groups):

*Once per session*: `SessionStart`, `SessionEnd`, `Setup` (with `--init-only`, `--init`, `--maintenance` in `-p` mode — for CI prep).

*Once per turn*: `UserPromptSubmit`, `UserPromptExpansion` (slash command → prompt expansion; can block), `Stop`, `StopFailure` (turn ended due to API error; output/exit-code ignored).

*Per tool call (agentic loop)*: `PreToolUse` (can block), `PermissionRequest`, `PermissionDenied` (auto-mode classifier denial — return `{retry: true}` to allow retry), `PostToolUse`, `PostToolUseFailure`, `PostToolBatch` (after parallel batch resolves, before next model call).

*Subagent / task*: `SubagentStart`, `SubagentStop`, `TaskCreated`, `TaskCompleted`.

*Other lifecycle*: `Notification`, `TeammateIdle` (agent team), `InstructionsLoaded` (CLAUDE.md / `.claude/rules/*.md` loaded into context — fires at session start AND lazy load), `ConfigChange` (config file changes mid-session), `CwdChanged` (e.g., after `cd` — useful for direnv-style reactive env), `FileChanged` (watched file changes; `matcher` field specifies filenames), `WorktreeCreate` / `WorktreeRemove` (replaces default git worktree behavior), `PreCompact` / `PostCompact`, `Elicitation` / `ElicitationResult` (MCP server requests user input during tool call).

**Configuration nesting** (3 levels): hook event → matcher group → hook handler.

**Hook locations** (scope/shareability):
- `~/.claude/settings.json` — all your projects, local
- `.claude/settings.json` — project, committable
- `.claude/settings.local.json` — project, gitignored
- Managed policy — org-wide
- Plugin `hooks/hooks.json` — bundled with plugin
- Skill or subagent frontmatter — while component active

Enterprise: `allowManagedHooksOnly` blocks user/project/plugin hooks; force-enabled plugins via managed `enabledPlugins` are exempt (vetted-distribution path).

**Matcher patterns**:
- `"*"`, `""`, omitted → match all
- letters/digits/`_`/`|` only → exact string or `|`-separated exact list (e.g., `Bash`, `Edit|Write`)
- any other char → JS regex (e.g., `^Notebook`, `mcp__memory__.*`)

What the matcher filters depends on event:
- `PreToolUse`/`PostToolUse`/`PostToolUseFailure`/`PermissionRequest`/`PermissionDenied` → tool name
- `SessionStart` → start type (`startup`, `resume`, `clear`, `compact`)
- `FileChanged` does NOT follow these rules (separate watch-list spec)

**Worked example** (PreToolUse blocking destructive shell):
```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Bash",
      "hooks": [{
        "type": "command",
        "if": "Bash(rm *)",
        "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/block-rm.sh"
      }]
    }]
  }
}
```

The `if` condition is an extra filter that runs BEFORE spawning the handler — avoids process-spawn overhead when not matching. Without `if`, every handler in the matched group runs.

Hook script reads JSON input from stdin (or POST body for HTTP), can return decision JSON to stdout:
```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "deny",
    "permissionDecisionReason": "Destructive command blocked by hook"
  }
}
```
`exit 0` allows the call.

**Resolution flow**: event fires → matcher checks → `if` condition checks → handler runs → Claude Code acts on decision.

For full per-event input/output schemas, async hooks, HTTP hooks, prompt hooks, MCP tool hooks, exit codes, and field references, refer back to raw — those sections were not fully sampled here.
