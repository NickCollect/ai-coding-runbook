---
type: summary
source: 01_Raw/github/modelcontextprotocol/typescript-sdk/packages/middleware/hono/README.md
source_url: https://github.com/modelcontextprotocol/typescript-sdk/blob/main/packages/middleware/hono/README.md
title: "@modelcontextprotocol/hono README"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Hono adapters for the MCP TypeScript server SDK. Thin integration layer.

**Helps you**: create a Hono app with sensible defaults; parse JSON request bodies and expose them as `c.get('parsedBody')` for Streamable HTTP transports; add DNS rebinding protection via Host header validation.

**Install**: `npm install @modelcontextprotocol/server @modelcontextprotocol/hono hono`.

**Exports**: `createMcpHonoApp(options?)`, `hostHeaderValidation(allowedHostnames)`, `localhostHostValidation()`.

Usage example shows wiring `WebStandardStreamableHTTPServerTransport` from `@modelcontextprotocol/server` to a Hono app.
