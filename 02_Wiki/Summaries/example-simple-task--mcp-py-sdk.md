---
type: summary
source: 01_Raw/github/modelcontextprotocol/python-sdk/examples/servers/simple-task/README.md
source_url: https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/servers/simple-task/README.md
title: "Python SDK example: simple task server"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Minimal MCP server demonstrating the **experimental tasks feature** over Streamable HTTP. Default `http://localhost:8000/mcp`.

Exposes one tool **`long_running_task`** that:
1. Must be called as a task (with `task` metadata in the request)
2. Takes ~3 seconds to complete
3. Sends status updates during execution
4. Returns a result on completion

Pairs with `simple-task-client` (run server in one terminal, client in another).
