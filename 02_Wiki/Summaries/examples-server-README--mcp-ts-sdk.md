---
type: summary
source: 01_Raw/github/modelcontextprotocol/typescript-sdk/examples/server/README.md
source_url: https://github.com/modelcontextprotocol/typescript-sdk/blob/main/examples/server/README.md
title: "TS SDK examples/server README"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Index of runnable MCP server examples built with `@modelcontextprotocol/server` plus framework adapters (Express, Hono). Run via `pnpm --filter @modelcontextprotocol/examples-server exec tsx src/<name>.ts`.

**Examples** (10 entries):
- Streamable HTTP server (stateful) — tools/resources/prompts, logging, tasks, sampling, optional OAuth
- Streamable HTTP server (stateless) — no session tracking; simple API-style servers
- Resource-Server-only auth — minimal OAuth RS using `mcpAuthMetadataRouter` + `requireBearerAuth`
- JSON response mode (no SSE)
- Server notifications over Streamable HTTP — server-initiated via GET+SSE
- Output schema server — tool output validation via structured output schemas
- Form elicitation server — non-sensitive user input via schema-driven forms
- URL elicitation server — secure browser-based flows for sensitive input (API keys, OAuth, payments)
- Sampling + tasks server — sampling and experimental task-based execution
- Task interactive server — task-based execution with interactive server→client requests
- Hono Streamable HTTP server — built with Hono instead of Express
