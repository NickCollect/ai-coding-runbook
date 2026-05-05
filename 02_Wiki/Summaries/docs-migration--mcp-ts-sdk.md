---
type: summary
source: 01_Raw/github/modelcontextprotocol/typescript-sdk/docs/migration.md
source_url: https://github.com/modelcontextprotocol/typescript-sdk/blob/main/docs/migration.md
title: "TS SDK v1 → v2 migration guide (human-readable)"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Comprehensive v1 → v2 migration guide for the MCP TypeScript SDK with before/after code examples.

**The big change**: the single `@modelcontextprotocol/sdk` package is split into:
- `@modelcontextprotocol/core` (types, protocol, transports — installed automatically as a dependency)
- `@modelcontextprotocol/client` (client implementation)
- `@modelcontextprotocol/server` (server implementation)

`npm uninstall @modelcontextprotocol/sdk` and install only what you need. Imports must change accordingly:
- `@modelcontextprotocol/sdk/client/index.js` → `@modelcontextprotocol/client`
- `@modelcontextprotocol/sdk/server/mcp.js` → `@modelcontextprotocol/server`
- `@modelcontextprotocol/sdk/types.js` → types are now in `@modelcontextprotocol/core/public` (re-exported from client/server)
- `@modelcontextprotocol/sdk/client/streamableHttp.js` → `@modelcontextprotocol/client`
- `@modelcontextprotocol/sdk/server/streamableHttp.js` → `@modelcontextprotocol/node` (`NodeStreamableHTTPServerTransport`) for Node-style HTTP, OR `@modelcontextprotocol/server` (`WebStandardStreamableHTTPServerTransport`) for Cloudflare Workers/Deno/Bun
- stdio paths move under `/stdio` subpath (e.g., `@modelcontextprotocol/server/stdio`)

Other v2 changes covered (per CLAUDE.md and changesets):
- WebSocket transport removed
- Standard Schema support — bring Zod v4 / Valibot / ArkType / etc. for tool/prompt schemas
- Auth: AS helpers removed (use external IdP/OAuth library); RS helpers (`requireBearerAuth`, `mcpAuthMetadataRouter`, `OAuthTokenVerifier`) live in `@modelcontextprotocol/express`
- Deprecated `.tool()/.prompt()/.resource()` method signatures removed (use `registerTool`/`registerPrompt`/`registerResource`)
- Unknown tool errors return JSON-RPC `-32602` instead of `CallToolResult { isError: true }`
- Tasks moved to `capabilities.tasks` on `ClientOptions`/`ServerOptions` instead of `ProtocolOptions`
- Custom (non-spec) method support via 3-arg `setRequestHandler(method, schemas, handler)`

For a mechanical mapping table optimized for AI-assisted migration, see `docs-migration-SKILL--mcp-ts-sdk` summary.
