---
type: summary
source: 01_Raw/github/modelcontextprotocol/servers/src/fetch/README.md
source_url: https://github.com/modelcontextprotocol/servers/blob/main/src/fetch/README.md
title: "Fetch MCP server (web content fetching)"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Python MCP server for **web content fetching** — retrieves URLs and converts HTML→markdown for easier LLM consumption. Registry: `io.github.modelcontextprotocol/server-fetch`.

**Caution**: can access local/internal IP addresses — security risk. Be careful when using to avoid exposing sensitive data.

**Tool**: `fetch(url, max_length=5000, start_index=0, raw=false)` — fetches URL, returns markdown. Truncates by default; `start_index` lets the model read in chunks until it finds what it needs. `raw=true` returns unconverted HTML.

**Prompt**: `fetch(url)` — fetch a URL and extract its contents as markdown.

**Install**: optionally install Node.js (more robust HTML simplifier). Then `uvx mcp-server-fetch` (recommended) or `pip install mcp-server-fetch && python -m mcp_server_fetch`.

**Configure for Claude.app / Claude Desktop**: standard `mcpServers` entry pointing to `uvx mcp-server-fetch` (or `python -m mcp_server_fetch`).
