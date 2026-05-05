---
type: summary
source: 01_Raw/github/modelcontextprotocol/typescript-sdk/.changeset/README.md
source_url: https://github.com/modelcontextprotocol/typescript-sdk/tree/main/.changeset
title: "TS SDK .changeset/ directory (61 release notes for v2 alpha)"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Consolidated summary of the `.changeset/` directory used by `@changesets/cli` — each `.md` file is a single release note. The `README.md` is just the auto-generated changesets-tool intro pointing to `github.com/changesets/changesets`. The other 61 files are pending v2 alpha changes affecting one or more of `@modelcontextprotocol/{core,client,server,express,fastify,hono,node,examples-server,test-integration}`.

**Themes covered (selection)**:

**Lifecycle / transport bug fixes**: abort in-flight request handlers when connection closes (`abort-handlers-on-close`); fix `InMemoryTransport.close()` firing onclose twice; prevent stack overflow in `StreamableHTTPServerTransport.close()` re-entrant; `try/finally` guards in shutdown paths; deferred callbacks check closed state; reverting `application/json` in notifications (`heavy-walls-swim`); fix StreamableHTTPClientTransport to handle SSE error responses; `body.cancel() → text()` to prevent hanging.

**Auth / OAuth**: `discoverOAuthServerInfo()` and unified discovery state caching (CIMD support across browser redirects); Express Resource-Server glue (`requireBearerAuth`, `mcpAuthMetadataRouter`, RFC 9728/8414 metadata); `validateClientMetadataUrl()` for early CIMD validation; OAuth error handling for servers returning errors with HTTP 200 (e.g., GitHub); continue OAuth metadata discovery on 502 from reverse proxies.

**Schema / protocol**: add missing `size` field to `ResourceSchema`; fix unknown-tool error code to `-32602`/-32002 per spec; replace zod-internals; drop `zod` from `peerDependencies` (kept as direct dep); ReDoS fix in `UriTemplate` regex (CVE-2026-0621); `setRequestHandler(method, schemas, handler)` 3-arg form for vendor-prefixed methods; `SdkError(InvalidResult)` instead of raw `ZodError`.

**Tasks / experimental**: extract task orchestration from `Protocol` into `TaskManager` (move `taskStore` etc. to `capabilities.tasks`); fix InMemoryTaskStore session isolation (was accepting but ignoring sessionId); fix `requestStream` to call `tasks/result` for failed tasks instead of yielding hardcoded `ProtocolError`; disallow null TTL.

**Middleware adapters**: add Fastify middleware adapter; fix Hono `getRequestListener()` overriding global Response (Next.js compat); make `hono` peer dep optional on `@modelcontextprotocol/node`; tsdown exports resolution fix across all packages; legacy `moduleResolution` types support (`types` field + `typesVersions`).

**Build/packaging**: stop bundling `@cfworker/json-schema` into main barrel (now only at `validators/cf-worker` subpath); export `InMemoryTransport` for in-process testing; expose AS discovery; `validateClientMetadataUrl` utility.

**Compatibility / DX**: `Mcp-Method`/`Mcp-Name` HTTP headers; remove deprecated `.tool`/`.prompt`/`.resource` method signatures; add `| undefined` to optional Transport interface properties (TS2420 fix for `exactOptionalPropertyTypes: true`); `wraphandler-hook` for middleware composition; standard JSON Schema support; spec-type-schema improvements.

**Stdio**: handle stdout EPIPE gracefully (no crash, surface via `onerror`, close); always set `windowsHide` on Windows (not just Electron); skip non-JSON lines on stdio.

**Notable file: `fix-unknown-tool-protocol-error.md`** — `core: minor` + `server: major`. Fixes per MCP spec: unknown/disabled tool calls now return JSON-RPC `-32602` (InvalidParams) instead of `CallToolResult { isError: true }`; unknown resource reads return `-32002` (ResourceNotFound) instead of `-32602`. Adds `ProtocolErrorCode.ResourceNotFound`. Callers checking `result.isError` for unknown tools must catch rejected promises instead.

Most files are 3-10 lines: a frontmatter listing affected packages and impact level (`major`/`minor`/`patch`), then a one-paragraph description. Several alphabetical changeset slugs are codenames: `brave-lions-glow`, `busy-rice-smoke`, `cyan-cycles-pump`, `funky-baths-attack`, etc.
