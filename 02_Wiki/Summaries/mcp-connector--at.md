---
type: summary
source: 01_Raw/platform.claude.com/docs/en/agents-and-tools/mcp-connector.md
source_url: https://platform.claude.com/docs/en/agents-and-tools/mcp-connector
title: "MCP connector"
summarized_at: 2026-05-05
entities_referenced: [MCP-server, Messages-API, Tool-use, Tool-search-tool-API, Tool-runner, Files-API, Anthropic-SDK-TypeScript]
concepts_referenced: []
---

The MCP connector lets Claude connect to remote [[MCP-server]]s directly from the [[Messages-API]] without writing a separate MCP client. Current beta header: `mcp-client-2025-11-20`. The previous header (`mcp-client-2025-04-04`) is deprecated. **Not eligible for ZDR.**

**Key features.** Direct API integration; tool calling support (only the MCP spec's tool-call surface is currently supported—not prompts, resources, etc.); flexible enable-all / allowlist / denylist tool configuration; per-tool config; OAuth Bearer authentication; multiple servers per request.

**Limitations.** Server must be publicly exposed via HTTP (Streamable HTTP or SSE transport); local STDIO servers cannot be connected directly. Not supported on Amazon Bedrock or Google Vertex.

**Two-component model.** A request now uses (1) `mcp_servers` array—server connection details (URL, auth) and (2) `tools` array containing one `mcp_toolset` object per server—configures which tools to enable.

Server fields: `type` ("url"), `url` (must start with `https://`), `name` (unique identifier referenced by exactly one MCPToolset), `authorization_token` (optional OAuth token).

Toolset fields: `type` ("mcp_toolset"), `mcp_server_name` (must match a server), `default_config` (defaults applied to all tools), `configs` (per-tool overrides keyed by tool name), `cache_control` (cache breakpoint). Each tool config supports `enabled` (default `true`) and `defer_loading` (default `false`, used with the [[Tool-search-tool-API]] for large tool sets).

**Configuration merging precedence (high → low):** tool-specific `configs` → set-level `default_config` → system defaults.

**Common patterns:**
- *Enable all*: bare MCPToolset with no overrides.
- *Allowlist*: `default_config.enabled: false`, then per-tool `enabled: true`.
- *Denylist*: leave defaults, add specific `enabled: false` for unwanted tools (e.g. `delete_all_events`, `share_calendar_publicly`).
- *Mixed*: allowlist + per-tool `defer_loading` overrides.

**Validation rules.** Server must exist (referenced name must match); every server in `mcp_servers` must be referenced by exactly one MCPToolset; each server can be referenced by only one toolset; unknown tool names in `configs` log a backend warning but don't error (MCP servers may have dynamic tool availability).

**Response content types.** Two new block types:
- `mcp_tool_use`: `{ id, name, server_name, input }` (id starts with `mcptoolu_`).
- `mcp_tool_result`: `{ tool_use_id, is_error, content: [...] }`.

**Multiple servers.** Include multiple server defs and a corresponding MCPToolset per server. Each can have independent tool configs (e.g., one with `defer_loading: true`).

**Authentication.** API consumers handle the OAuth flow externally and pass the access token via `authorization_token`. For testing, use the MCP Inspector (`npx @modelcontextprotocol/inspector`) to walk through the OAuth flow and capture an access token.

**Client-side TypeScript helpers.** When managing your own MCP client (for local stdio servers, prompts, or resources), the [[Anthropic-SDK-TypeScript]] provides converters in `@anthropic-ai/sdk/helpers/beta/mcp`:
- `mcpTools(tools, mcpClient)`: convert MCP tools for use with the [[Tool-runner]] (`client.beta.messages.toolRunner()`).
- `mcpMessages(messages)`: convert MCP prompt messages to Claude API message format.
- `mcpResourceToContent(resource)`: convert MCP resource to a content block.
- `mcpResourceToFile(resource)`: convert MCP resource to a file object for upload (via the [[Files-API]]).

These throw `UnsupportedMCPValueError` for unsupported content/MIME types or non-HTTP resource links. Helpers exist in TypeScript only.

**Migration from `mcp-client-2025-04-04`.** Tool configuration moved from the server definition's `tool_configuration` field into MCPToolset objects in the `tools` array. Old `tool_configuration.allowed_tools: [...]` becomes a toolset with `default_config.enabled: false` plus per-tool `enabled: true` in `configs`.
