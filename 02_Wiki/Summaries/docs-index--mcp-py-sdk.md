---
type: summary
source: 01_Raw/github/modelcontextprotocol/python-sdk/docs/index.md
source_url: https://github.com/modelcontextprotocol/python-sdk/blob/main/docs/index.md
title: "Python SDK docs landing page"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Landing page for the MkDocs-rendered Python SDK documentation. Brief MCP intro, quick example showing `MCPServer` with `@mcp.tool()`, `@mcp.resource("greeting://{name}")`, `@mcp.prompt()` decorators and `mcp.run(transport="streamable-http")`. Run via `uv run --with mcp server.py`, then test via MCP Inspector at `http://localhost:8000/mcp` (`npx -y @modelcontextprotocol/inspector`).

Pointers to: Install, Concepts, Authorization, Low-Level Server, and the auto-generated API Reference under `api/mcp/`.
