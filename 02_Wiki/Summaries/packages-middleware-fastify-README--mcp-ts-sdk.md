---
type: summary
source: 01_Raw/github/modelcontextprotocol/typescript-sdk/packages/middleware/fastify/README.md
source_url: https://github.com/modelcontextprotocol/typescript-sdk/blob/main/packages/middleware/fastify/README.md
title: "@modelcontextprotocol/fastify README"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Fastify adapters for the MCP TypeScript server SDK. Thin integration layer — does NOT implement MCP itself.

**Helps you**: create a Fastify app with sensible defaults; add DNS rebinding protection via Host header validation (recommended for localhost servers).

**Install**: `npm install @modelcontextprotocol/server @modelcontextprotocol/fastify fastify` (plus `@modelcontextprotocol/node` for Node Streamable HTTP).

**Exports**: `createMcpFastifyApp(options?)`, `hostHeaderValidation(allowedHostnames)`, `localhostHostValidation()`.
