---
type: summary
source: 01_Raw/github/modelcontextprotocol/python-sdk/examples/clients/sse-polling-client/README.md
source_url: https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/clients/sse-polling-client/README.md
title: "Python SDK example: SSE polling client (SEP-1699)"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Demonstrates **client-side auto-reconnect** for the SSE polling pattern from SEP-1699. Connects to the `mcp-sse-polling-demo` server, automatically reconnects when the server closes the SSE stream, resumes from `Last-Event-ID` to avoid missing messages, respects server-provided `retry` interval.

CLI options: `--url`, `--items` (number to process, default 10), `--checkpoint-every` (default 3), `--log-level` (default DEBUG).
