---
type: summary
source: 01_Raw/github/modelcontextprotocol/servers/src/everything/docs/startup.md
source_url: https://github.com/modelcontextprotocol/servers/blob/main/src/everything/docs/startup.md
title: "Everything server startup process"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Walks through the Everything server's startup process step-by-step.

**Step 1 — launcher**: `node dist/index.js [stdio|sse|streamableHttp]`. Default `stdio`. Routes to: `transports/stdio.js` / `transports/sse.js` / `transports/streamableHttp.js`.

**Step 2 — transport manager**: creates a server instance via `createServer()` (from `server/index.ts`), connects it to the chosen transport from the MCP SDK, handles communication per the chosen transport's spec.

- **STDIO**: one process-bound connection. Calls `clientConnect()` on connection. Closes and calls `cleanup()` on `SIGINT`.
- **SSE**: multiple client connections; client transports mapped to `sessionId`. Calls `clientConnect(sessionId)` on connection. Hooks server's `onclose` to clean and remove session. Exposes `/sse` GET (SSE stream) and `/message` POST (JSON-RPC).
- **Streamable HTTP**: multiple client connections; mapped to `sessionId`. Calls `clientConnect(sessionId)` on connection. Exposes `/mcp` for both POST and GET.

(Doc continues with step 3 — `clientConnect()` registering session-scoped state etc. — beyond this summary's coverage.)
