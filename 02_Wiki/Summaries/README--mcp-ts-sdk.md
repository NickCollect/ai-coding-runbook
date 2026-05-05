---
type: summary
source: 01_Raw/github/modelcontextprotocol/typescript-sdk/README.md
source_url: https://github.com/modelcontextprotocol/typescript-sdk/blob/main/README.md
title: "MCP TypeScript SDK — main README (v2 in development)"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

The official MCP TypeScript SDK. README is for the **`main` branch which contains v2 (currently in development, pre-alpha)**. Stable v2 release expected Q1 2026; until then, **v1.x remains the recommended version for production**. v1.x will continue to receive bug fixes and security updates for at least 6 months after v2 ships.

**Runs on**: Node.js, Bun, Deno.

**Package structure** — v2 splits the monolithic `@modelcontextprotocol/sdk` into:
- `@modelcontextprotocol/server` — build MCP servers
- `@modelcontextprotocol/client` — build MCP clients
- `@modelcontextprotocol/core` — internal package (types, protocol, transports) used by both above

**Schema flexibility**: tool and prompt schemas use **Standard Schema** — bring Zod v4, Valibot, ArkType, or any compatible library.

**Optional middleware packages** (thin runtime/framework adapters, no MCP business logic):
- `@modelcontextprotocol/node` — Streamable HTTP transport for Node `IncomingMessage`/`ServerResponse`
- `@modelcontextprotocol/express` — Express helpers (defaults + Host header validation)
- `@modelcontextprotocol/hono` — Hono helpers (defaults + JSON body parsing + Host validation)

**Quick example**: an `McpServer` exposing one `greet` tool over stdio:
```typescript
import { McpServer } from '@modelcontextprotocol/server';
import { StdioServerTransport } from '@modelcontextprotocol/server/stdio';
import * as z from 'zod/v4';

const server = new McpServer({ name: 'greeting-server', version: '1.0.0' });
server.registerTool('greet', { description: 'Greet someone by name', inputSchema: z.object({ name: z.string() }) },
  async ({ name }) => ({ content: [{ type: 'text', text: `Hello, ${name}!` }] }));

const transport = new StdioServerTransport();
await server.connect(transport);
```

**Documentation**: server quickstart (build a weather server), client quickstart (build LLM-powered chatbot), full server/client guides, FAQ, hosted API docs at `ts.sdk.modelcontextprotocol.io`. v2 docs live at `/v2/`; v1 docs at the root.

License: Apache 2.0 for new contributions; existing code under MIT.
