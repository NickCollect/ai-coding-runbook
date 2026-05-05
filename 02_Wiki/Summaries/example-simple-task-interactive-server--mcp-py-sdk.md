---
type: summary
source: 01_Raw/github/modelcontextprotocol/python-sdk/examples/servers/simple-task-interactive/README.md
source_url: https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/servers/simple-task-interactive/README.md
title: "Python SDK example: simple interactive task server"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Minimal MCP server demonstrating **interactive tasks** (elicitation + sampling). Default `http://localhost:8000/mcp`; use `--port` to change.

**Two tools**:
- `confirm_delete` (elicitation) — uses `task.elicit()` to ask the user for confirmation before "deleting" a file. Shows the elicitation flow: task → input_required → response → complete
- `write_haiku` (sampling) — uses `task.create_message()` to ask the LLM to write a haiku about a topic. Shows the sampling flow: task → input_required → response → complete

**Server-side concepts** demonstrated:
- `ServerTaskContext` provides `elicit()` and `create_message()` for user interaction
- `run_task()` spawns background work, auto-completes/fails, returns immediately
- `TaskResultHandler` delivers queued messages and routes responses
- Response routing: responses are routed back to waiting resolvers

Pairs with `simple-task-interactive-client`.
