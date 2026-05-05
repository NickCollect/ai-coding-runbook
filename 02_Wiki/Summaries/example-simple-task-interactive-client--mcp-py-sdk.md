---
type: summary
source: 01_Raw/github/modelcontextprotocol/python-sdk/examples/clients/simple-task-interactive-client/README.md
source_url: https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/clients/simple-task-interactive-client/README.md
title: "Python SDK example: simple interactive task client"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Minimal MCP client demonstrating responses to **interactive tasks** (elicitation and sampling). Pairs with `simple-task-interactive` server.

Demos: (1) `confirm_delete` — server asks confirmation, client responds via terminal y/n; (2) `write_haiku` — server requests LLM completion, client returns a hardcoded haiku.

**Key concepts**:
- `elicitation_callback(context, params)` returns `ElicitResult(action="accept", content={...})`
- `sampling_callback(context, params)` returns `CreateMessageResult(model=..., role="assistant", content=...)`
- `call_tool_as_task("tool_name", {"arg": "value"})` returns `CreateTaskResult` with `task.task_id`
- `get_task_result(task_id, CallToolResult)` is what triggers delivery of elicitation/sampling requests to your callbacks and blocks until task completes

Sample output shows the elicitation flow ("Server asks: Are you sure...?" → "Your response (y/n):") and the sampling flow ("Server requests LLM completion for: Write a haiku..." → returns the hardcoded haiku).
