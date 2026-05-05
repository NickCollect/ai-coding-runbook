---
type: summary
source: 01_Raw/github/modelcontextprotocol/python-sdk/docs/testing.md
source_url: https://github.com/modelcontextprotocol/python-sdk/blob/main/docs/testing.md
title: "Testing MCP servers (Python SDK)"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

How to write tests for MCP servers using the SDK's `Client` class with an in-memory transport — no network overhead.

**Pattern**: assume a simple `MCPServer` with one tool. Install `inline-snapshot` and `pytest`. Define `anyio_backend` pytest fixture (`"asyncio"` by default; `"trio"` if using trio). Define a `client` fixture that opens `Client(app, raise_exceptions=True)` as an async context manager and yields the connected client. Write `@pytest.mark.anyio` async tests that call `client.call_tool("add", {"a": 1, "b": 2})` and assert against an `inline_snapshot(CallToolResult(content=[TextContent(...)], structuredContent={...}))`.

**Recommended libraries**: `inline-snapshot` for golden-snapshot testing of structured outputs; `anyio` (not asyncio directly) for async testing per the SDK's AGENTS.md guidance.
