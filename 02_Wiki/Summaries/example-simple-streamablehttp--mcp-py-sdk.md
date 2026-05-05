---
type: summary
source: 01_Raw/github/modelcontextprotocol/python-sdk/examples/servers/simple-streamablehttp/README.md
source_url: https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/servers/simple-streamablehttp/README.md
title: "Python SDK example: StreamableHTTP server with resumability"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

MCP server demonstrating the **StreamableHTTP transport** with resumability via `InMemoryEventStore`. Supports REST API operations (POST, GET, DELETE) on the `/mcp` endpoint, sends multiple notifications over time.

CLI options: `--port` (default 3000), `--log-level`, `--json-response` (JSON instead of SSE streams).

**Resumability** — clients can:
- Reconnect after disconnection
- Resume event streaming from where they left off via `Last-Event-ID` header

The server generates unique event IDs per SSE message, stores events in memory for replay, replays missed events on reconnect with `Last-Event-ID`. The `InMemoryEventStore` is for demo only — production needs persistent storage.

Tool: **"start-notification-stream"** with `interval`, `count`, `caller` arguments. Pairs with TypeScript SDK or MCP Inspector for testing.
