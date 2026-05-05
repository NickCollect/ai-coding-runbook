---
type: summary
source: 01_Raw/github/modelcontextprotocol/servers/src/everything/README.md
source_url: https://github.com/modelcontextprotocol/servers/blob/main/src/everything/README.md
title: "Everything MCP server (reference / test server)"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Reference MCP server that **exercises all features of the MCP protocol** — prompts, tools, resources, sampling, and more. Not intended to be useful — it's a test server for builders of MCP clients (and the basis of the cross-SDK conformance suite).

**npm package**: `@modelcontextprotocol/server-everything`. Run via `npx -y @modelcontextprotocol/server-everything` (or via `cmd /c npx ...` on Windows). Docker image: `mcp/everything`.

**Transports**: stdio (default), SSE (deprecated), Streamable HTTP — selected via CLI argument: `node dist/index.js [stdio|sse|streamableHttp]`.

**Installation paths**: Claude Desktop (`claude_desktop_config.json` `mcpServers` entry), VS Code (one-click install buttons + manual via user `mcp.json` from Command Palette `MCP: Open User Configuration` or workspace `.vscode/mcp.json`).

**Documentation deep-dive** (lives under `docs/`): Architecture, Project Structure, Startup Process, Server Features, Extension Points, How It Works, Server Instructions. See companion summaries below.
