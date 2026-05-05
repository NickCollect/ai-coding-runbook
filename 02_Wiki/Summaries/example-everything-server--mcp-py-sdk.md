---
type: summary
source: 01_Raw/github/modelcontextprotocol/python-sdk/examples/servers/everything-server/README.md
source_url: https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/servers/everything-server/README.md
title: "Python SDK example: Everything server (conformance reference)"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Comprehensive MCP server implementing **all protocol features** for **conformance testing**. Used with the MCP Conformance Test Framework (`modelcontextprotocol/conformance`) to validate MCP client and server implementations.

**Run**: `uv run -m mcp_everything_server --port 3001 --log-level DEBUG`. Default port 3001 at `http://localhost:3001/mcp`.

This is the Python SDK's reference implementation for the per-SDK conformance suite required by SEP-1730 (SDKs Tiering System). Each official SDK ships an Everything server implementing the same defined spec; the Conformance Test Client runs test cases against it to verify protocol compliance.
