---
type: summary
source: 01_Raw/github/modelcontextprotocol/python-sdk/docs/installation.md
source_url: https://github.com/modelcontextprotocol/python-sdk/blob/main/docs/installation.md
title: "Python SDK installation"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

`pip install mcp` or `uv add mcp`. PyPI package: `mcp`.

**Auto-installed dependencies**: `httpx` (HTTP client for Streamable HTTP and SSE), `httpx-sse` (SSE), `pydantic` (types/JSON schema/validation), `starlette` (HTTP transport endpoints), `python-multipart` (HTTP body parsing), `sse-starlette` (SSE for Starlette), `pydantic-settings` (settings for `MCPServer`), `uvicorn` (ASGI server), `jsonschema` (validation), `pywin32` (Windows CLI deps).

**Optional groups**: `cli` installs `typer` and `python-dotenv` for the MCP CLI tools.
