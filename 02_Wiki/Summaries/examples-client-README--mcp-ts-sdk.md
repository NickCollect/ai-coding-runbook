---
type: summary
source: 01_Raw/github/modelcontextprotocol/typescript-sdk/examples/client/README.md
source_url: https://github.com/modelcontextprotocol/typescript-sdk/blob/main/examples/client/README.md
title: "TS SDK examples/client README"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Index of runnable MCP client examples built with `@modelcontextprotocol/client`. Run via `pnpm --filter @modelcontextprotocol/examples-client exec tsx src/<name>.ts`.

**Examples** (10 entries):
- Interactive Streamable HTTP client (`simpleStreamableHttp.ts`) — exercises tools/resources/prompts, notifications, elicitation, tasks
- Backwards-compatible client (`streamableHttpWithSseFallbackClient.ts`) — tries Streamable HTTP first, falls back to legacy SSE on 4xx
- SSE polling client (legacy)
- Parallel tool calls (`parallelToolCallsClient.ts`) — runs multiple tool calls in parallel
- Multiple clients in parallel — connect multiple clients concurrently to same server
- OAuth client (interactive) — dynamic registration + auth flow
- OAuth provider helper — reusable OAuth providers
- Client credentials (M2M) — machine-to-machine OAuth
- URL elicitation client — drives URL-mode elicitation flows (sensitive input in browser)
- Task interactive client — task-based execution + interactive server→client requests

The README also documents the URL elicitation server+client end-to-end flow.
