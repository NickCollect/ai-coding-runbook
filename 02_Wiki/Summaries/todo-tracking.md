---
type: summary
source: 01_Raw/code.claude.com/docs/en/agent-sdk/todo-tracking.md
source_url: https://code.claude.com/docs/en/agent-sdk/todo-tracking
title: "Todo Lists (Agent SDK)"
summarized_at: 2026-05-05
entities_referenced: [Agent-SDK, Subagent]
concepts_referenced: []
---

Brief doc on the Agent SDK's built-in todo-tracking facility (the `TodoWrite` tool). Todos follow a fixed lifecycle: `pending` → `in_progress` → `completed`, with all items removed once a group finishes.

**SDK auto-creates todos** for:
- Complex multi-step tasks (3+ distinct actions)
- User-provided task lists with multiple items
- Non-trivial operations that benefit from progress tracking
- Explicit user requests

**Monitoring pattern**: iterate the response stream, look for `AssistantMessage` whose content blocks include a `tool_use` with `name == "TodoWrite"`. The `block.input.todos` array contains items shaped `{content, status, activeForm}` — `activeForm` is the present-progressive form shown when `status == "in_progress"` (e.g., "Reading auth.ts" vs content "Read auth.ts").

The doc shows a `TodoTracker` class wrapper for both Python and TS that aggregates progress percentage and re-renders the list each time `TodoWrite` fires.
