---
type: summary
source: 01_Raw/github/modelcontextprotocol/typescript-sdk/CLAUDE.md
source_url: https://github.com/modelcontextprotocol/typescript-sdk/blob/main/CLAUDE.md
title: "TS SDK: Claude Code agent instructions"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Repo-level operating instructions for AI agents working in the TS SDK monorepo.

**Build & test** (pnpm + vitest): `pnpm install`, `pnpm build:all`, `pnpm lint:all`, `pnpm typecheck:all`, `pnpm test:all`, `pnpm check:all` (typecheck + lint). Single package via filter: `pnpm --filter @modelcontextprotocol/core test -- path/to/file.test.ts`.

**Breaking changes** documented in **both** `docs/migration.md` (human-readable with before/after) AND `docs/migration-SKILL.md` (LLM-optimized mapping tables for mechanical migration).

**Code style**: strict TS, ES modules, explicit return types; PascalCase classes/types, camelCase functions/vars; lowercase-with-hyphens filenames; tests under each package's `test/` (vitest only includes `test/**/*.test.ts`); 2-space indent, semicolons required, single quotes preferred. JSDoc `@example` tags pull type-checked code from companion `.examples.ts` files via `` ```ts source="./file.examples.ts#regionName" `` fences. Run `pnpm sync:snippets` to sync example content.

**Architecture** — three layers:
1. **Types layer** (`packages/core/src/types/types.ts`) — protocol types from MCP spec, all JSON-RPC types/schemas/constants in Zod v4
2. **Protocol layer** (`packages/core/src/shared/protocol.ts`) — abstract `Protocol` class handles JSON-RPC routing, request/response correlation, capability negotiation, transport management. Both `Client` and `Server` extend it.
3. **High-level APIs**: `Client`, `Server` (low-level), `McpServer` (high-level wrapper around Server with simplified resource/tool/prompt registration)

**Public API exports** — two-layer export structure: `@modelcontextprotocol/core` is internal (private:true; exports everything); `@modelcontextprotocol/core/public` is the curated public API (only TS types, error classes, constants, guards) re-exported by `@modelcontextprotocol/{client,server}`. Use explicit named exports (not `export *`); package root entry must stay runtime-neutral so browser/CF Workers bundlers work — modules using Node builtins live at named subpath exports (e.g., `./stdio`) covered by a `barrelClean` test.

**Transports** in `packages/core/src/shared/transport.ts`: Streamable HTTP (recommended, supports SSE), SSE (legacy backward-compat), stdio (local process-spawned).

**Server-side features**: `McpServer.tool()`/`.resource()`/`.prompt()`; full OAuth 2.0 server in `packages/server/src/server/auth/`; auto-completion via `completable.ts`. **Client-side**: OAuth client, request middleware, sampling/elicitation handlers, roots.

**Middleware packages** (`packages/middleware/`): thin integration layers for Express, Hono, Node — should NOT add new MCP functionality.

**Experimental** in `packages/*/src/experimental/`: tasks (long-running with polling/resumption).

**Validation**: pluggable JSON Schema validation (`packages/core/src/validators/`) — `ajvProvider.ts` (default), `cfWorkerProvider.ts` (Cloudflare Workers).

**Message flow** (bidirectional): both Client and Server can send requests. Outbound: high-level method → `Protocol.request()` (assigns ID, capability check, response handler promise, `transport.send()`). Inbound: `transport.onmessage()` → `_onrequest`/`_onresponse`/`_onnotification` → handler from `_requestHandlers` map. Handler context (`BaseContext`): `sessionId`, `mcpReq` (id/method/_meta/signal/send/notify), `http?` (`authInfo`), `task?`. `ServerContext` adds `mcpReq.log()/.elicitInput()/.requestSampling()` and `http?.req`/`closeSSE`/`closeStandaloneSSE`. Capabilities checked via `assertCapabilityForMethod()`.

**Adding a new request type**: define schema in `src/types.ts` → add capability → implement sender method → add capability check → register handler on receiving side → optionally add high-level wrapper on `McpServer`.
