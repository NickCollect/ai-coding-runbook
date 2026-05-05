---
type: summary
source: 01_Raw/github/modelcontextprotocol/servers/src/everything/docs/architecture.md
source_url: https://github.com/modelcontextprotocol/servers/blob/main/src/everything/docs/architecture.md
title: "Everything server architecture"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

High-level architecture of the Everything MCP server.

**Purpose**: minimal modular MCP server showcasing core MCP features — exposes simple tools, prompts, and resources; runs over multiple transports (STDIO, SSE, Streamable HTTP).

**Design**: a small "server factory" constructs the MCP server and registers features. Transports are separate entry points handling network concerns. Tools, prompts, and resources are organized in their own submodules.

**Multi-client**: server supports multiple concurrent clients. Per-session data tracked via resource subscriptions and simulated logging.

**Build and distribution**: TypeScript sources compiled to `dist/` via `npm run build`. Build script copies `docs/` into `dist/` so instruction files ship alongside the compiled server. CLI bin configured in `package.json` as `mcp-server-everything` → `dist/index.js`.

Crosslinks to companion docs: Project Structure, Startup Process, Server Features, Extension Points, How It Works.
