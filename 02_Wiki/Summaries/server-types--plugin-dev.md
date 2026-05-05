---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/plugin-dev/skills/mcp-integration/references/server-types.md
title: "plugin-dev: mcp-integration server-types reference"
summarized_at: 2026-05-05
entities_referenced: [Plugin, MCP-server]
concepts_referenced: []
---

Reference doc inside `plugin-dev`'s `mcp-integration` skill. Deep dive on the four MCP server transport types supported in Claude Code.

**stdio**: spawn local process, JSON-RPC over stdin/stdout. Lifecycle: process spawned at session start, runs entire session, terminated on exit. Best for: NPM packages, custom scripts, Python servers, local file/DB tools. Best practices: use `${CLAUDE_PLUGIN_ROOT}` paths, set `PYTHONUNBUFFERED=1` for Python, log to **stderr** (stdout reserved for protocol).
```json
{ "command": "npx", "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path"] }
```

**SSE (Server-Sent Events)**: HTTP + streaming. Best for hosted services with OAuth (Asana `https://mcp.asana.com/sse`, GitHub). Claude Code handles OAuth flow automatically (browser → tokens stored → auto-refresh). Custom headers via `headers` field. Always HTTPS.

**HTTP (REST API)**: stateless request/response. Best for REST backends, microservices, serverless. Token-based auth via `Authorization: Bearer ${TOKEN}` or `X-API-Key: ${KEY}`. Handle 401/403/429/500 errors, retries, timeouts.

**WebSocket (`ws`)**: persistent bidirectional. WSS only (never `ws`). Best for real-time streaming, collaborative editing, low-latency tool calls, push notifications. Implement heartbeat/ping-pong, reconnection logic, message buffering during disconnect.

**Comparison matrix**:
| Feature | stdio | SSE | HTTP | WS |
|---|---|---|---|---|
| Direction | Bi | Server→Client | Req/Resp | Bi |
| State | Stateful | Stateful | Stateless | Stateful |
| Auth | env vars | OAuth/headers | headers | headers |
| Latency | Lowest | Medium | Medium | Low |
| Reconnect | Process respawn | Auto | N/A | Auto |

**Choosing**:
- Local tools/custom servers/lowest latency → stdio.
- Hosted services with OAuth → SSE.
- REST APIs with token auth → HTTP.
- Real-time/collaborative/push → WebSocket.

**Migration paths**: stdio → SSE (deploy server, change config). HTTP → WebSocket (real-time benefits).

**Multi-server config**: combine types in one `.mcp.json` (`local-db` stdio + `cloud-api` SSE + `internal-service` HTTP). Switch per env via `${API_URL}` env vars.

**Security**: validate command paths (stdio); never hardcode tokens; use env vars; rotate tokens; document scopes. HTTPS/WSS only; validate certs (don't skip).
