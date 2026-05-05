---
type: summary
source: 01_Raw/github/modelcontextprotocol/python-sdk/README.md
source_url: https://github.com/modelcontextprotocol/python-sdk/blob/main/README.md
title: "MCP Python SDK — main README"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

The official MCP Python SDK (PyPI: `mcp`). README is **frozen at v1** (a pre-commit hook rejects edits) — see `README.v2.md` for v2 content. Implements the full MCP specification for both servers and clients with stdio, SSE, and Streamable HTTP transports.

The README itself is large (~32k tokens) and walks through:
- Quick install (`pip install mcp` / `uv add "mcp[cli]"`) with `mcp` CLI for testing/dev
- The high-level **FastMCP** server class (`@mcp.tool()`, `@mcp.resource("uri")`, `@mcp.prompt()` decorators)
- Three core MCP primitives explained for Python: tools (functions LLMs call), resources (data exposed via URIs), prompts (reusable templates)
- Server features: lifespan management for async resources, structured output via type-annotated returns, ImageContent/AudioContent helpers, ServerSettings, image utilities, completion helpers
- Authorization (OAuth 2.0 server with bearer token validation)
- Low-level server (`mcp.server.lowlevel.Server`) for full control
- Client API: `ClientSession`, `stdio_client`, `sse_client`, `streamable_http_client`, callbacks for sampling/elicitation/list_roots
- Sampling examples (server requesting LLM completions from client)
- Streaming, completion, JSON-RPC concepts
- Testing patterns with `Client(server)` in-memory transport
- CLI tooling: `mcp dev`, `mcp install`, `mcp run`

Note: the v1 README focuses on `from mcp.server.fastmcp import FastMCP`. In v2 (current `main` branch) the class is renamed to `MCPServer` under `mcp.server.mcpserver` — see `README--v2--mcp-py-sdk` and `migration--mcp-py-sdk` summaries.
