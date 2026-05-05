---
type: summary
source: 01_Raw/github/modelcontextprotocol/servers/src/everything/AGENTS.md
source_url: https://github.com/modelcontextprotocol/servers/blob/main/src/everything/AGENTS.md
title: "Everything server: AI agent dev guidelines"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Development guidelines for AI agents (Claude Code etc.) editing the Everything server.

**Build/test/run**: `npm run build` (TS→JS), `npm run watch` (auto-rebuild), `npm run start:stdio`/`start:sse`/`start:streamableHttp` (run with chosen transport), `npm run prepare` (build for publishing).

**Code style**: ES modules with `.js` extension in import paths; strict TS typing for all functions/vars; Zod schemas for tool input validation; async/await over callbacks/Promise chains; imports at top, grouped external then internal; descriptive names; cleanup timers/resources on shutdown; try/catch with clear errors; 2-space indent, trailing commas; camelCase vars/functions, PascalCase types/classes, UPPER_CASE constants, kebab-case files and registered names; **verbs for tool names** (`get-annotated-message` not `annotated-message`).

**Extension points** (high-level): tools live under `src/everything/tools/` registered via `registerTools(server)`; resources under `resources/` via `registerResources(server)`; prompts under `prompts/` via `registerPrompts(server)`. The server factory at `src/everything/server/index.ts` registers all features during startup and handles post-connection setup. Detailed extension docs at `docs/extension.md`.
