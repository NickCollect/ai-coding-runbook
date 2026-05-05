---
type: summary
source: 01_Raw/code.claude.com/docs/en/agent-sdk/hooks.md
source_url: https://code.claude.com/docs/en/agent-sdk/hooks
title: "Intercept and control agent behavior with hooks (Agent SDK)"
summarized_at: 2026-05-05
entities_referenced: [Hooks, Agent-SDK, Subagent, MCP-server, Permission-mode]
concepts_referenced: [Agentic-loop]
---

The Agent SDK hooks doc covers programmatic callback hooks (in-process, scoped to main session) as opposed to filesystem shell hooks. Use cases: block dangerous ops, log/audit, transform inputs/outputs, require human approval, manage session lifecycle.

**Lifecycle**: event fires → SDK collects registered hooks (callbacks + shell hooks loaded via `settingSources`) → matchers filter → callbacks execute with `(input_data, tool_use_id, context)` → callback returns decision object.

**Available events** (TS has more than Python):
- Both: `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `UserPromptSubmit`, `Stop`, `SubagentStart`, `SubagentStop`, `PreCompact`, `PermissionRequest`, `Notification`.
- TS only: `PostToolBatch`, `SessionStart`, `SessionEnd`, `Setup`, `TeammateIdle`, `TaskCompleted`, `ConfigChange`, `WorktreeCreate`, `WorktreeRemove`.

**Matchers**: regex string against tool name (or notification type for `Notification`). MCP tools use `mcp__<server>__<action>`. `timeout` defaults 60s. Matcher only filters by tool name — to filter by file path check `tool_input.file_path` inside the callback.

**Callback output**:
- Top-level: `systemMessage` (injects context visible to model), `continue`/`continue_`.
- `hookSpecificOutput`: for `PreToolUse` — `permissionDecision` (`allow` / `deny` / `ask`; TS also `defer`), `permissionDecisionReason`, `updatedInput`. For `PostToolUse` — `additionalContext` or `updatedToolOutput`.
- Return `{}` to allow without changes.
- Priority: **deny > defer > ask > allow**.

**Async output**: return `{"async": True/true, "asyncTimeout": ms}` to fire-and-forget side effects (logging, webhooks). Cannot block or modify.

Examples shown: `.env` write blocking, sandbox path redirect via `updatedInput`, `/etc` block with `systemMessage`, auto-approve read-only tools, hook chaining (run in array order), regex matchers for file-mod/MCP/global, subagent tracking via `SubagentStop`, HTTP/Slack webhooks.

**Gotchas**: `updatedInput` requires `permissionDecision: "allow"`. Hook event names case-sensitive. Hooks may not fire when agent hits `max_turns`. `SessionStart`/`SessionEnd` not in Python — use shell hooks via `setting_sources=["project"]`. Subagents don't auto-inherit parent permissions; use auto-approve hooks. Watch for recursive `UserPromptSubmit` loops when spawning subagents.
