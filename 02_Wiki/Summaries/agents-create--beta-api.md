---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/agents/create.md
source_url: https://platform.claude.com/docs/en/api/beta/agents/create
title: "Create Agent"
summarized_at: 2026-05-05
entities_referenced: [Managed-agent, Skill-API, MCP-server, Tool-use]
concepts_referenced: [Permission-mode]
---

`POST /v1/agents` — creates a new Managed Agent definition.

**Required body params:** `model` (a model ID string such as `claude-opus-4-7`, `claude-opus-4-6`, `claude-sonnet-4-6`, `claude-haiku-4-5`, etc., or a `BetaManagedAgentsModelConfigParams` object with `id` plus optional `speed: "standard"|"fast"`) and `name` (1–256 chars).

**Optional body params:** `description` (≤2048 chars), `system` (system prompt, ≤100,000 chars), `metadata` (≤16 KV pairs, key ≤64 chars, value ≤512 chars), `mcp_servers` (≤20 URL MCP servers with unique names), `skills` (≤20 entries; each Anthropic-managed `{ skill_id, type: "anthropic", version? }` or custom `{ skill_id, type: "custom", version? }`), and `tools` (≤128 across all toolsets) selecting from:
- `agent_toolset_20260401` — built-in agent tools (`bash`, `edit`, `read`, `write`, `glob`, `grep`, `web_fetch`, `web_search`) with per-tool `enabled` and `permission_policy` (`always_allow` | `always_ask`) or a `default_config`;
- `mcp_toolset` — tools sourced from a previously named MCP server, same per-tool config;
- `custom` — client-executed tools defined by `name`, `description`, and JSON-Schema `input_schema`. When called, the platform emits an `agent.custom_tool_use` event and the session goes idle until the client returns a `user.custom_tool_result`.

**Returns** the full `BetaManagedAgentsAgent` resource including `id`, `created_at`, `updated_at`, `archived_at`, and starting `version: 1`.

Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies. The example uses `anthropic-beta: managed-agents-2026-04-01`.
