---
type: summary
source: 01_Raw/code.claude.com/docs/en/agent-sdk/custom-tools.md
source_url: https://code.claude.com/docs/en/agent-sdk/custom-tools
title: "Give Claude custom tools"
summarized_at: 2026-05-05
entities_referenced: [Agent-SDK, MCP-server, Permission-mode]
concepts_referenced: [Agentic-loop, Tool-use, Context-window]
---

How to define custom tools using the Claude Agent SDK's **in-process MCP server** (no separate process). A tool has four parts: name, description, input schema, async handler.

**Defining a tool**:
- TypeScript: `tool(name, description, zodSchema, handler, {annotations?})`
- Python: `@tool(name, description, schema_dict_or_full_json_schema, annotations=...)`
- TS uses Zod (handler args auto-typed). Python dict schema is converted to JSON Schema; for enums/optional/nested, pass full JSON Schema dict.
- Optional params: TS `.default()`; Python omit from schema, document in description, read via `args.get()`.

**Handler return**: object with `content` (array of `text`/`image`/`resource` blocks) and optional `isError` / `is_error`.

**Bundling**: wrap tool list in `createSdkMcpServer` (TS) / `create_sdk_mcp_server` (Python). Pass to `query()` via `mcpServers` option. Server key becomes `{server_name}` in fully qualified tool name `mcp__{server_name}__{tool_name}`. List that name in `allowedTools` (or wildcard `mcp__weather__*`) to skip permission prompts.

**Tool annotations** (optional booleans): `readOnlyHint` (default false; lets Claude batch parallel calls with other read-only tools), `destructiveHint` (default true), `idempotentHint`, `openWorldHint`. Annotations are metadata, not enforcement.

**Permission layers**:
- `tools: ["Read", "Grep"]` — availability layer; only listed built-ins in context (MCP unaffected). `tools: []` removes all built-ins.
- allowedTools / disallowedTools — permission layer; disallowed leaves tool visible (Claude may waste a turn). Prefer omitting from `tools` over disallowing.

**Error handling**: Uncaught throw → agent loop stops, `query` fails. Returning `isError: true` → loop continues, Claude sees error and can retry.

**Non-text returns**: `image` blocks carry base64 bytes inline + required `mimeType` (no URL field; fetch + encode in handler). `resource` blocks embed URI + `text` or `blob`; URI is just a label, SDK doesn't read from it.

**Scaling**: every tool consumes context every turn. For dozens of tools use [tool search](https://code.claude.com/en/agent-sdk/tool-search) for on-demand loading.

Examples: weather (`get_temperature`, `get_precipitation_chance`), HTTP fetcher with error handling, unit converter showing enum schemas + unsupported-input handling via `isError`.
