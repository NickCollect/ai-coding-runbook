---
type: summary
source: 01_Raw/github/modelcontextprotocol/python-sdk/examples/servers/sse-polling-demo/README.md
source_url: https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/servers/sse-polling-demo/README.md
title: "Python SDK example: SSE polling demo server (SEP-1699)"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Demonstrates the **SSE polling pattern with server-initiated stream close** for long-running tasks (per SEP-1699).

**Features**: priming events (automatic with EventStore); server-initiated stream close via `close_sse_stream()` callback; client auto-reconnect with `Last-Event-ID`; progress notifications during long-running tasks; configurable `--retry-interval` (ms).

**Tool: `process_batch`** — processes items with periodic checkpoints that trigger SSE stream closes:
- `items`: number of items to process (1-100, default 10)
- `checkpoint_every`: close stream after this many items (1-20, default 3)

Pairs with the `mcp-sse-polling-client` companion CLI for end-to-end testing of the resume-via-Last-Event-ID flow.
