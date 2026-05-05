---
type: summary
source: 01_Raw/github/modelcontextprotocol/typescript-sdk/docs/server-quickstart.md
source_url: https://github.com/modelcontextprotocol/typescript-sdk/blob/main/docs/server-quickstart.md
title: "TS SDK Server Quickstart — build a weather server"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Hands-on tutorial building an MCP weather server with two tools (`get-alerts`, `get-forecast`) and connecting it to VS Code with GitHub Copilot.

**Core MCP concepts** introduced: Resources (file-like data), Tools (functions LLM can call with user approval), Prompts (pre-written templates). Tutorial focuses on tools.

**Prerequisites**: TypeScript and LLM familiarity, Node.js 20+. SDK also works with Bun and Deno (substitute `bun`/`deno` commands as appropriate). For HTTP-based servers on Bun/Deno, use `WebStandardStreamableHTTPServerTransport` instead of the Node-specific transport (see server guide).

Complete code at `examples/server-quickstart/` in the repo. Walks through project setup, dependency install, server file with `McpServer.registerTool()` for the two weather tools, and connecting the server to VS Code via `mcp.json` configuration.
