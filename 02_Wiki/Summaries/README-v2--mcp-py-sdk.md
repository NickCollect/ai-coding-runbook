---
type: summary
source: 01_Raw/github/modelcontextprotocol/python-sdk/README.v2.md
source_url: https://github.com/modelcontextprotocol/python-sdk/blob/main/README.v2.md
title: "MCP Python SDK — v2 README (current main branch)"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Active editable README for v2 (the v1 `README.md` is frozen via pre-commit hook). Large file (~31k tokens) describing the v2 API surface — same content scope as v1 but with renamed/restructured APIs.

Major v2 changes covered (see `migration--mcp-py-sdk` for the full migration matrix):
- `FastMCP` → `MCPServer` (under `mcp.server.mcpserver` instead of `mcp.server.fastmcp`)
- Field names changed from camelCase to snake_case (Python attribute access; JSON wire format unchanged via Pydantic aliases)
- `streamablehttp_client` removed → use `streamable_http_client` (returns 2-tuple, takes `httpx.AsyncClient`)
- `McpError` → `MCPError` (and constructor signature simplified — takes `code`, `message`, optional `data` directly)
- `MCPServer.get_context()` removed — context now injected via `ctx: Context` parameter
- `RequestContext` / `Context` type parameters simplified
- Lowlevel `Server`: handlers registered via constructor `on_*` kwargs (not decorators); type parameter reduced from 2 to 1; auto return-value wrapping removed; `request_handlers`/`notification_handlers` dicts removed
- `RootModel` union types replaced by union types with `TypeAdapter` validation (no more `.root` access)
- Resource URI changed from `AnyUrl` to plain `str` (allows relative paths like `users/me`)
- Transport-specific parameters moved from constructor to `run()`/`sse_app()`/`streamable_http_app()` methods

The v2 README provides the canonical examples for the new API:
```python
from mcp.server.mcpserver import MCPServer

mcp = MCPServer("Test Server", json_response=True)

@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b

@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    return f"Hello, {name}!"

@mcp.prompt()
def greet_user(name: str, style: str = "friendly") -> str:
    return f"Write a {style} greeting for someone named {name}."

mcp.run(transport="streamable-http")
```

Run via `uv run --with mcp server.py` and connect MCP Inspector at `http://localhost:8000/mcp`.
