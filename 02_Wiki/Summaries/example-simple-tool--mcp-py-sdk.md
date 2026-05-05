---
type: summary
source: 01_Raw/github/modelcontextprotocol/python-sdk/examples/servers/simple-tool/README.md
source_url: https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/servers/simple-tool/README.md
title: "Python SDK example: simple tool server"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Minimal MCP server exposing a website-fetching tool. Run via stdio (default) or `--transport streamable-http --port 8000`.

Exposes a tool **"fetch"** with one required argument: `url` (the website to fetch).

Sample Python client shows `session.list_tools()` then `session.call_tool("fetch", {"url": "https://example.com"})` over the stdio transport.
