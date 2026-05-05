---
type: summary
source: 01_Raw/github/anthropics/skills/skills/mcp-builder/reference/node_mcp_server.md
title: "Node/TypeScript MCP server implementation guide"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Reference inside the `mcp-builder` skill (in `anthropics/skills`). Best practices for implementing MCP servers in Node/TypeScript using `@modelcontextprotocol/sdk` + Zod + Express.

**API rule**: use **modern register methods only** (`server.registerTool`, `server.registerResource`, `server.registerPrompt`). Do NOT use deprecated `server.tool()` or `server.setRequestHandler(ListToolsRequestSchema, ...)`. The `register*` methods provide better type safety.

**Naming**: server `{service}-mcp-server` (lowercase + hyphens). Tool names `snake_case`, prefixed with service to avoid conflicts (`slack_send_message`, `github_create_issue`).

**Project layout**:
```
{service}-mcp-server/
├── package.json
├── tsconfig.json
├── README.md
├── src/{index.ts, types.ts, tools/, services/, schemas/, constants.ts}
└── dist/  (entry: dist/index.js)
```

**Tool registration**: pass full `{title, description, inputSchema, annotations}` (no JSDoc auto-extraction); `inputSchema` MUST be a Zod schema (not JSON schema). Annotations: `readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`.

**Description requirements**: include explicit input/output types, return schema, when-to-use examples, when-NOT-to-use, error messages.

**Zod patterns**: `.strict()` to forbid extra fields, `.describe()` for parameter docs, `.default()` for defaults, `z.nativeEnum(MyEnum)`.

**Response formats**: support both `markdown` (human-readable) and `json` (machine-readable) via `response_format` enum. Markdown uses headers/lists, human-readable timestamps. JSON returns full structured data.

**Pagination**: every list tool returns `{total, count, offset, items, has_more, next_offset}`.

**CHARACTER_LIMIT** constant (e.g. 25000): if response exceeds, truncate dataset by half, set `truncated: true`, include `truncation_message` with how to get more.

**Error handling**: typed handler returning friendly strings — 404 ("Resource not found"), 403 ("Permission denied"), 429 ("Rate limit exceeded"), `ECONNABORTED` ("Request timed out"), generic fallback.

**Shared utilities**: extract `makeApiRequest<T>(endpoint, method, data, params)` to centralize axios config. Don't duplicate.

**TypeScript best practices**: strict mode, define interfaces for all data, no `any` (use `unknown`), typed `Promise<T>` returns, runtime validation via `Schema.parse(data)`, type guards (`axios.isAxiosError`, `z.ZodError`), optional chaining + nullish coalescing.

**Package config**: `"type": "module"`, `"main": "dist/index.js"`, `"engines": {"node": ">=18"}`, deps `@modelcontextprotocol/sdk`, `axios`, `zod`. tsconfig `target: ES2022`, `module: Node16`, `strict: true`.

**Two transports**:
- **Streamable HTTP** (recommended for remote): `StreamableHTTPServerTransport` with Express. Create new transport per request (stateless, prevents request-ID collisions).
- **stdio** (local): `StdioServerTransport`. For CLI / local subprocess.

**Resources**: register with URI templates (`file://documents/{name}`), implement loader function. Use resources for simple URI-based data; tools for complex operations with side effects.

**Notifications**: `server.notification({ method: "notifications/tools/list_changed" })` — use sparingly when capabilities genuinely change.

**Quality checklist** (long, ~50 items): strategic design, implementation quality, TypeScript quality, advanced features, project config, code quality, testing/build. Build success (`npm run build` produces working `dist/index.js`) is required before considering implementation complete.
