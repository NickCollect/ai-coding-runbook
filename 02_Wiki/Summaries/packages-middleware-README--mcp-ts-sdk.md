---
type: summary
source: 01_Raw/github/modelcontextprotocol/typescript-sdk/packages/middleware/README.md
source_url: https://github.com/modelcontextprotocol/typescript-sdk/blob/main/packages/middleware/README.md
title: "TS SDK middleware packages overview"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Index for the `packages/middleware/` group of thin integration adapters. These packages help expose an MCP server in a specific runtime, platform, or web framework — they intentionally do NOT add new MCP features or business logic.

Middleware packages should primarily: adapt request/response types to the SDK (e.g., Node `IncomingMessage`/`ServerResponse`); provide small framework helpers (wiring, body parsing); supply safe defaults for common deployment pitfalls (e.g., localhost DNS rebinding protection).

**Packages**:
- `@modelcontextprotocol/express` — Express helpers (defaults + Host header validation)
- `@modelcontextprotocol/hono` — Hono helpers (defaults + JSON body parsing hook + Host validation)
- `@modelcontextprotocol/node` — Node.js Streamable HTTP transport wrapper for `IncomingMessage`/`ServerResponse`

Typical usage: `@modelcontextprotocol/server` + one middleware package + (optionally) additional framework dependencies.
