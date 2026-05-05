---
type: summary
source: 01_Raw/code.claude.com/docs/en/agent-sdk/mcp.md
source_url: https://code.claude.com/docs/en/agent-sdk/mcp
title: "Connect to external tools with MCP"
summarized_at: 2026-05-05
entities_referenced: [MCP-server, Agent-SDK, Permission-mode]
concepts_referenced: [Context-window, Tool-use]
---

How to configure external MCP servers in the Agent SDK. MCP is the open standard for connecting agents to databases, APIs (Slack/GitHub), and services without writing custom tool code.

**Three transport types**, picked by what the server docs give you:
- **stdio** — local process, command + args + env. Use for `npx @modelcontextprotocol/server-*`-style servers.
- **HTTP / SSE** — remote URL with optional `headers`. `"type": "http"` for non-streaming, `"type": "sse"` for SSE.
- **SDK MCP server** — defined in code, runs in-process. See `custom-tools` doc.

**Configuration** can live in `query()` options (`mcpServers`) or in a `.mcp.json` at project root (loaded when `project` setting source is enabled, which is the default).

**Permissions**: MCP tools require explicit `allowedTools`. Naming pattern `mcp__<server>__<tool>`. Wildcard `mcp__github__*` allows all from a server.

**Important note on permission modes vs allowedTools**: `permissionMode: "acceptEdits"` does NOT auto-approve MCP tools (only file edits and FS Bash). `bypassPermissions` does, but disables all other safety. Prefer wildcard in `allowedTools` for narrow MCP access.

**Discovery**: inspect `system` init message — `message.mcp_servers` lists available tools and connection status.

**Auth**: stdio servers use `env` field for credentials; HTTP/SSE servers use `headers` (Authorization Bearer). OAuth 2.1 supported by spec — SDK doesn't run the flow but you can pass tokens via headers post-flow.

**Error detection**: SDK emits `system` message with subtype `init` containing `mcp_servers[].status`. Filter by `status !== "connected"` to detect failures before agent runs.

**Tool search** (enabled by default): withholds tool definitions from context until needed — solves context-window bloat from many MCP tools.

**Troubleshooting**: failed status → check missing env vars, server not installed, bad connection string, network. Tools-not-called → check `allowedTools`. Default 60s connection timeout.

**Examples**: GitHub `list_issues` with `GITHUB_TOKEN`, Postgres `query` with connection string passed as arg, Playwright browser automation.
