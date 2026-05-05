---
type: summary
source: 01_Raw/github/modelcontextprotocol/typescript-sdk/packages/middleware/node/README.md
source_url: https://github.com/modelcontextprotocol/typescript-sdk/blob/main/packages/middleware/node/README.md
title: "@modelcontextprotocol/node README"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Node.js adapters for the MCP TypeScript server SDK. Provides a Streamable HTTP transport that works with Node `IncomingMessage` / `ServerResponse`.

For web-standard runtimes (Cloudflare Workers, Deno, Bun, etc.), use `WebStandardStreamableHTTPServerTransport` from `@modelcontextprotocol/server` directly.

**Install**: `npm install @modelcontextprotocol/server @modelcontextprotocol/node`.

**Exports**: `NodeStreamableHTTPServerTransport`, `StreamableHTTPServerTransportOptions` (alias for `WebStandardStreamableHTTPServerTransportOptions`).

Sample usage shown wiring `NodeStreamableHTTPServerTransport` to an Express app via `createMcpExpressApp()`.
