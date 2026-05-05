---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/plugin-dev/skills/mcp-integration/SKILL.md
title: "MCP Integration (plugin-dev skill)"
summarized_at: 2026-05-05
entities_referenced: [MCP-server, Plugin, Skill]
concepts_referenced: []
---

Skill in `plugin-dev` plugin for integrating MCP servers into Claude Code plugins. Triggered by phrases: "add MCP server", "integrate MCP", "configure MCP in plugin", "use .mcp.json", "set up Model Context Protocol", "connect external service", `${CLAUDE_PLUGIN_ROOT}` with MCP, MCP server types (SSE/stdio/HTTP/WebSocket).

**Two configuration methods**:
- **Recommended**: dedicated `.mcp.json` at plugin root — clearer separation, easier to maintain, better for multiple servers
- **Inline**: `mcpServers` field in `plugin.json` — single config file, good for simple single-server plugins

**Server types** (sampled):
- **stdio (local process)**: child process via `command` + `args` + `env`. Best for file system, local DB, custom servers, npm-packaged. Spawned + managed by Claude Code, stdin/stdout, terminates on exit.
- **SSE (Server-Sent Events)**: hosted MCP servers with OAuth. `{"type": "sse", "url": "https://..."}`. Best for cloud (Asana, GitHub-hosted etc.), no local install. OAuth flows handled automatically; tokens managed by Claude Code.
- **HTTP** (REST API) — covered later in raw, not sampled

**Key capabilities**: connect external services (DBs, APIs, FS), provide many tools from one service, handle OAuth/complex auth, bundle MCP servers with plugins for auto-setup.

**Conventions**: use `${CLAUDE_PLUGIN_ROOT}` for paths to bundled binaries/configs; pass env vars via `env` field with `${VAR}` substitution.

(Full per-type config syntax + WebSocket + auth details in remainder of raw — not sampled.)
