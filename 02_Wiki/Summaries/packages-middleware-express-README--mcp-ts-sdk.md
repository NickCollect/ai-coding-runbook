---
type: summary
source: 01_Raw/github/modelcontextprotocol/typescript-sdk/packages/middleware/express/README.md
source_url: https://github.com/modelcontextprotocol/typescript-sdk/blob/main/packages/middleware/express/README.md
title: "@modelcontextprotocol/express README"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Express adapters for the MCP TypeScript server SDK. Thin integration layer — does NOT implement MCP itself.

**Helps you**: create an Express app with sensible defaults; add DNS rebinding protection via Host header validation (recommended for localhost servers); protect routes with `requireBearerAuth` (validates `Authorization: Bearer ...` via your `OAuthTokenVerifier`); serve OAuth Protected Resource Metadata (RFC 9728) via `mcpAuthMetadataRouter`.

**Install**: `npm install @modelcontextprotocol/server @modelcontextprotocol/express express` (plus `@modelcontextprotocol/node` for Node Streamable HTTP).

**Exports**: `createMcpExpressApp(options?)`, `hostHeaderValidation(allowedHostnames)`, `localhostHostValidation()`, `requireBearerAuth(options)`, `mcpAuthMetadataRouter(options)`, `getOAuthProtectedResourceMetadataUrl(serverUrl)`.
