---
type: summary
source: 01_Raw/github/modelcontextprotocol/python-sdk/examples/clients/simple-task-client/README.md
source_url: https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/clients/simple-task-client/README.md
title: "Python SDK example: simple task client"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Minimal MCP client demonstrating **polling for task results** over Streamable HTTP. Pairs with the `mcp-simple-task` server.

Flow: connects via streamable HTTP → calls `long_running_task` as a task → polls task status until completion → retrieves and prints result.

Output sample shows status transitions (`working - Starting work...` → `Processing step 1...` → `completed`).
