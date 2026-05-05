---
type: summary
source: 01_Raw/github/modelcontextprotocol/typescript-sdk/docs/server.md
source_url: https://github.com/modelcontextprotocol/typescript-sdk/blob/main/docs/server.md
title: "TS SDK Server Guide"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Comprehensive guide to building MCP servers in TypeScript. Three steps: (1) create `McpServer` and register tools/resources/prompts; (2) create a transport (Streamable HTTP for remote, stdio for local); (3) connect via `server.connect(transport)`.

**Imports** drawn from companion `serverGuide.examples.ts` (type-checked code blocks via region tags).

**Streamable HTTP transport**: `NodeStreamableHTTPServerTransport` (from `@modelcontextprotocol/node`) with `sessionIdGenerator: () => randomUUID()` for stateful sessions, or `undefined` for stateless mode (no resumability). `enableJsonResponse: true` returns plain JSON instead of SSE streams. For Cloudflare Workers / Deno / Bun, use `WebStandardStreamableHTTPServerTransport` from `@modelcontextprotocol/server` directly.

**stdio transport**: `StdioServerTransport` from `@modelcontextprotocol/server/stdio` for local process-spawned integrations (Claude Desktop, CLI tools).

Other sections (per the guide structure) cover: tools registration via `registerTool`/`tool`; resources (static + templates with `ResourceTemplate`); prompts; server-initiated requests (sampling, elicitation); auth/OAuth (Resource Server with `requireBearerAuth` + `mcpAuthMetadataRouter`); deployment patterns mounted on Express (or Hono adapter); completion support via `completable.ts`.

Linked resource: `simpleStreamableHttp.ts` in `examples/server/` for a complete server with sessions, logging, CORS mounted on Express.
