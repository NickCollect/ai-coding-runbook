---
type: summary
source: 01_Raw/github/modelcontextprotocol/servers/src/everything/docs/structure.md
source_url: https://github.com/modelcontextprotocol/servers/blob/main/src/everything/docs/structure.md
title: "Everything server project structure"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

ASCII tree of the `src/everything` package layout.

**Top level**: `index.ts` (entry point), `AGENTS.md`, `package.json`.

**`docs/`**: architecture.md, extension.md, features.md, how-it-works.md, instructions.md, startup.md, structure.md.

**`prompts/`**: `index.ts` (registers all prompts), `args.ts`, `completions.ts`, `simple.ts`, `resource.ts`.

**`resources/`**: `index.ts`, `files.ts`, `session.ts`, `subscriptions.ts`, `templates.ts`.

**`server/`**: `index.ts` (server factory + transport-agnostic setup), `logging.ts`, `roots.ts`.

**`tools/`**: `index.ts` (registers all tools), plus per-tool files (echo.ts, get-annotated-message.ts, get-env.ts, get-resource-links.ts, etc. — see features.md for the catalog).

The pattern across `tools/`, `prompts/`, `resources/` is consistent: each subdirectory has an `index.ts` exporting a `register*(server)` function, which the server factory calls during startup. Individual files implement single capabilities and are registered from the per-directory `index.ts`.
