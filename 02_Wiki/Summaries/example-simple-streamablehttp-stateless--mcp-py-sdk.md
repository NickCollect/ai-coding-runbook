---
type: summary
source: 01_Raw/github/modelcontextprotocol/python-sdk/examples/servers/simple-streamablehttp-stateless/README.md
source_url: https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/servers/simple-streamablehttp-stateless/README.md
title: "Python SDK example: stateless StreamableHTTP server"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Stateless MCP server demonstrating the **StreamableHTTP transport without session state** (`mcp_session_id=None`). Each request creates a new ephemeral connection with no persisted state — ideal for **multi-node deployment** where requests can be routed to any instance.

CLI options: `--port` (default 3000), `--log-level`, `--json-response` (use JSON instead of SSE streams).

Exposes a tool **"start-notification-stream"** with `interval` (seconds), `count`, and `caller` arguments.

Pairs with the TypeScript SDK's StreamableHTTP client examples or the MCP Inspector for testing (Python SDK does not yet provide a complementary stateless client example).
