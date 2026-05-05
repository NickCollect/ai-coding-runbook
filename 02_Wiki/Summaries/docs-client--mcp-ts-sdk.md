---
type: summary
source: 01_Raw/github/modelcontextprotocol/typescript-sdk/docs/client.md
source_url: https://github.com/modelcontextprotocol/typescript-sdk/blob/main/docs/client.md
title: "TS SDK Client Guide"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Guide to building MCP clients in TypeScript. A client connects to a server, discovers tools/resources/prompts, and invokes them. Beyond the core loop, covers: authentication, error handling, responding to server-initiated requests (sampling, elicitation).

**Streamable HTTP**: `new StreamableHTTPClientTransport(new URL('http://localhost:3000/mcp'))` then `await client.connect(transport)`.

**stdio**: `new StdioClientTransport({ command: 'node', args: ['server.js'] })` from `@modelcontextprotocol/client/stdio` — spawns server process and communicates over stdin/stdout.

Imports also include OAuth helpers (`AuthProvider`, `ClientCredentialsProvider`, `CrossAppAccessProvider`, `discoverAndRequestJwtAuthGrant`, `PrivateKeyJwtProvider`), client middleware composition (`applyMiddlewares`, `createMiddleware`), error types (`ProtocolError`, `SdkError`, `SdkErrorCode`), and SSE transport for legacy compat (`SSEClientTransport`).

Other sections cover: discovering capabilities via `client.listTools()`/`listResources()`/`listPrompts()`; calling tools with arguments; reading resources; getting prompts; OAuth flows (browser-redirect for interactive, M2M client credentials, Cross App Access for enterprise IdP); responding to server-initiated sampling and elicitation requests; error handling patterns.

Linked: `simpleStreamableHttp.ts` and other examples in `examples/client/` directory.
