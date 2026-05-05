---
type: summary
source: 01_Raw/code.claude.com/docs/en/agent-sdk/agent-loop.md
source_url: https://code.claude.com/docs/en/agent-sdk/agent-loop
title: "How the agent loop works"
summarized_at: 2026-05-05
entities_referenced: [Agent-SDK, Hooks, Subagent, MCP-server, Permission-mode, Auto-mode, Memory]
concepts_referenced: [Agentic-loop, Context-window, Prompt-caching, Extended-thinking]
---

Explains the message lifecycle inside the Agent SDK's agentic loop. Each session cycles: receive prompt → Claude evaluates and emits text + optional tool calls → SDK executes tools → results feed back → repeat until Claude returns a no-tool-call response. Each cycle is one "turn"; the loop terminates with a final `AssistantMessage` (no tool calls) plus a `ResultMessage` carrying the final text, token usage, cost, and `session_id`.

**Five core message types** streamed from the loop: `SystemMessage` (lifecycle, with `subtype: "init"` or `"compact_boundary"`), `AssistantMessage` (Claude output per turn), `UserMessage` (tool results sent back, also carries checkpoint UUIDs), `StreamEvent` (only when partial messages enabled), `ResultMessage` (terminal). TypeScript SDK adds extra observability events (hook events, tool progress, rate limits). Python checks types via `isinstance`; TypeScript via `message.type` string. TypeScript `AssistantMessage`/`UserMessage` wrap the API message in `.message`.

**Built-in tools** mirror the Claude Code CLI: file ops (`Read`/`Edit`/`Write`), search (`Glob`/`Grep`), execution (`Bash`), web (`WebSearch`/`WebFetch`), discovery (`ToolSearch`), orchestration (`Agent`/`Skill`/`AskUserQuestion`/`TodoWrite`). Extend via MCP servers, custom tool handlers, or project skills loaded via `settingSources`. Read-only tools (incl. MCP tools annotated `readOnly`/`readOnlyHint`) run concurrently; state-modifying tools run sequentially. Custom tools default to sequential.

**Loop control options** (`ClaudeAgentOptions` / `Options`):
- `max_turns` / `maxTurns` — caps tool-use turns; hitting it returns `ResultMessage` subtype `error_max_turns`
- `max_budget_usd` / `maxBudgetUsd` — cost cap; returns `error_max_budget_usd`
- `effort` — `"low"`/`"medium"`/`"high"`/`"xhigh"`/`"max"` (xhigh recommended on Opus 4.7; TS default `"high"`, Python defers to model). Independent of extended thinking.
- `permission_mode`/`permissionMode` — `default`, `acceptEdits`, `plan`, `dontAsk`, `auto` (TS-only, model classifier), `bypassPermissions` (cannot run as root on Unix)
- `model` — defaults to Claude Code's default per auth/subscription

**Context window**: accumulates across turns (system prompt, tool defs, history, tool I/O). Stable prefixes (system prompt, CLAUDE.md, tool defs) are prompt-cached. CLAUDE.md is re-injected every request when loaded via `settingSources`. **Automatic compaction** kicks in near the limit: emits `compact_boundary` system message; older history is summarized. Customize via summarization instructions inside CLAUDE.md, the `PreCompact` hook (with `trigger: "manual"|"auto"`), or `/compact` slash command sent as a prompt string.

**Result handling**: check `subtype` first — `success`, `error_max_turns`, `error_max_budget_usd`, `error_during_execution`, `error_max_structured_output_retries`. `result` field only on `success`. All carry `total_cost_usd`, `usage`, `num_turns`, `session_id`. `stop_reason` — `end_turn`, `max_tokens`, `refusal`.

**Hooks** fire at lifecycle points without consuming context (run in app process): `PreToolUse`, `PostToolUse`, `UserPromptSubmit`, `Stop`, `SubagentStart`/`SubagentStop`, `PreCompact`. PreToolUse can short-circuit a tool call. Sessions are resumable via captured `session_id`; can also fork.

Closes with end-to-end Python + TypeScript example wiring `allowedTools`, `settingSources: ["project"]`, `maxTurns: 30`, `effort: "high"`, capturing `sessionId` and handling termination subtypes.
