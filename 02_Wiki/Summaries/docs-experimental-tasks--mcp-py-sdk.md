---
type: summary
source: 01_Raw/github/modelcontextprotocol/python-sdk/docs/experimental/tasks.md
source_url: https://github.com/modelcontextprotocol/python-sdk/blob/main/docs/experimental/tasks.md
title: "Python SDK experimental tasks (overview)"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Overview of the experimental tasks feature in the Python SDK (tracks draft MCP spec, see SEP-1686).

**When to use**: operations taking seconds-to-minutes; need progress updates during execution; require user input mid-execution (elicitation, sampling); should run without blocking the requestor. Common use cases: long-running data processing, multi-step workflows with user confirmation, LLM-powered ops requiring sampling, OAuth flows requiring user browser interaction.

**Lifecycle**: `working` → `completed` / `failed` / `cancelled` (terminal); `working` ↔ `input_required` for elicitation/sampling pauses.

**Bidirectional**: tasks work both client→server (most common — long tool calls) AND server→client (for elicitation/sampling).

**Key concepts**:
- **TaskMetadata** — `TaskMetadata(ttl=60000)` (TTL in milliseconds) — augments a request with task execution
- **TaskStore** — servers persist task state. SDK provides `InMemoryTaskStore`; for production implement against a database/cache
- **Capabilities** — server: `tasks.requests.tools.call`; client: `tasks.requests.sampling.createMessage`, `tasks.requests.elicitation.create`. SDK manages these automatically.

**Quick server example**: `server.experimental.enable_tasks()` (one-line setup); inside `@server.call_tool()`, call `ctx.experimental.validate_task_mode(TASK_REQUIRED)` then `await ctx.experimental.run_task(work)` where `work(task: ServerTaskContext)` does the actual work, calls `task.update_status(...)` for progress, returns `CallToolResult`.

**Quick client example**: `session.experimental.call_tool_as_task(...)` returns `CreateTaskResult` with `task.taskId`; `async for status in session.experimental.poll_task(task_id):` to wait; `session.experimental.get_task_result(task_id, CallToolResult)` for the final value.

Pointers to deeper docs: tasks-server.md (server impl), tasks-client.md (client usage).
