---
type: summary
source: 01_Raw/github/modelcontextprotocol/python-sdk/docs/experimental/tasks-client.md
source_url: https://github.com/modelcontextprotocol/python-sdk/blob/main/docs/experimental/tasks-client.md
title: "Python SDK: client task usage"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Detailed guide to calling task-augmented tools from MCP clients in Python and handling input_required states.

**Quick start**: `session.experimental.call_tool_as_task("process_data", {"input": "hello"}, ttl=60000)` returns `CreateTaskResult` with `task.taskId`. Then `async for status in session.experimental.poll_task(task_id):` polls until terminal state. Finally `session.experimental.get_task_result(task_id, CallToolResult)` for the result.

**`call_tool_as_task()` signature**: tool name, arguments dict, `ttl` (milliseconds), optional `meta`. Response includes `task.taskId`, `task.status`, `task.pollInterval` (server-suggested ms), `task.ttl`, `task.createdAt`.

**`poll_task()` async iterator**: respects `pollInterval`; stops at `completed` / `failed` / `cancelled`; yields each status for progress display.

**Handling `input_required`**: when status transitions, you must call `get_task_result()` to receive and respond to the elicitation — the **elicitation callback** set on the session does the actual user interaction.

**Elicitation callback**: provide `elicitation_callback=handle_elicitation` when constructing `ClientSession`. The callback receives `(context, params: ElicitRequestParams)` and returns `ElicitResult(action="accept", content={...})`.

**Sampling callback**: similarly `sampling_callback=handle_sampling`. Returns `CreateMessageResult(role="assistant", content=TextContent(...), model=...)` — call your own LLM here.

**Result type per request type**: `tools/call` → `CallToolResult`; `sampling/createMessage` → `CreateMessageResult`; `elicitation/create` → `ElicitResult`.

**Cancellation**: `session.experimental.cancel_task(task_id)` — cooperative; server must check.

**Listing tasks**: `session.experimental.list_tasks()` with cursor pagination (`result.nextCursor`).

**Advanced: client as task receiver**: servers can send task-augmented requests TO the client. Provide `experimental_task_handlers=task_handlers` (an `ExperimentalTaskHandlers` with `augmented_elicitation`, `get_task`, `get_task_result` callbacks) when creating the session. The client then maintains its own client-side `InMemoryTaskStore`, returns `CreateTaskResult` immediately, does async work in a background task, and the server polls for results. Enables flows where both ends create tasks during the same conversation.

Complete example provided wiring up `stdio_client` + elicitation callback + task polling.
