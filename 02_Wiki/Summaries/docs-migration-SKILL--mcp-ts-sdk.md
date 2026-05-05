---
type: summary
source: 01_Raw/github/modelcontextprotocol/typescript-sdk/docs/migration-SKILL.md
source_url: https://github.com/modelcontextprotocol/typescript-sdk/blob/main/docs/migration-SKILL.md
title: "TS SDK v1 → v2 migration SKILL (LLM-optimized mapping tables)"
summarized_at: 2026-05-05
entities_referenced: [MCP-server, Skill]
concepts_referenced: []
---

LLM-optimized companion to `docs/migration.md`. Frontmatter declares `name: migrate-v1-to-v2` and a description triggering on user requests to migrate, upgrade, or port MCP TypeScript code from v1 to v2. Mechanical mapping tables for find-and-replace style migration.

**Order**: dependencies → imports → API calls → type aliases.

**Environment**: Node.js 20+ required (v18 dropped). ESM only (CJS dropped) — convert `require()` to `import`/`export` or use dynamic `import()`.

**Dependencies install table**: client only / server only / server + Node HTTP / server + Express / server + Hono. `@modelcontextprotocol/core` is installed automatically.

**Import mapping tables** (extensive):
- Client imports: all `@modelcontextprotocol/sdk/client/...` → `@modelcontextprotocol/client` (or `/stdio` subpath); `websocket.js` REMOVED
- Server imports: `mcp.js`/`index.js`/`stdio.js` → `@modelcontextprotocol/server` (and `/stdio` subpath); `streamableHttp.js` → `@modelcontextprotocol/node` (`NodeStreamableHTTPServerTransport`) OR `@modelcontextprotocol/server` (`WebStandardStreamableHTTPServerTransport`); `sse.js` REMOVED (migrate to Streamable HTTP); `auth/*` → RS helpers go to `@modelcontextprotocol/express`, AS helpers REMOVED (use external OAuth library); `middleware.js` → `@modelcontextprotocol/express` (signature changed)
- Types/shared imports: schemas no longer suffixed with `Schema` in many cases; `types.js` → `@modelcontextprotocol/core/public` re-exported from client/server packages

The full SKILL covers API call differences (renamed methods, signature changes, removed parameters), type alias renames, and post-migration verification steps. Designed to be invoked by AI assistants when users say "migrate my MCP TS code from v1 to v2" or similar phrases.
