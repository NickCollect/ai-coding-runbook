---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/agents.md
source_url: https://platform.claude.com/docs/en/api/beta/agents
title: "Agents"
summarized_at: 2026-05-05
entities_referenced: [Managed-agent, Skill-API, MCP-server, Tool-use]
concepts_referenced: [Permission-mode]
---

Beta REST resource for **Managed Agents** under `/v1/agents`. The index page documents the full lifecycle of a server-side agent definition that the platform persists and versions on the user's behalf.

**Endpoints listed on this page:**

- `POST /v1/agents` — Create Agent (model, name, optional description/system, MCP servers, skills, tools, metadata).
- `GET /v1/agents` — List Agents (filterable by `created_at[gte|lte]`, `include_archived`, paginated).
- `GET /v1/agents/{agent_id}` — Retrieve Agent.
- `POST /v1/agents/{agent_id}` — Update Agent (requires current `version` for optimistic concurrency).
- `POST /v1/agents/{agent_id}/archive` — Archive Agent (soft-deletes; `archived_at` timestamp set).
- `GET /v1/agents/{agent_id}/versions` — List Versions (every update increments `version`).

**Domain model.** A `BetaManagedAgentsAgent` carries `id`, `type: "agent"`, `name`, `description`, `system` (system prompt up to 100k chars), `model` (a `BetaManagedAgentsModel` ID such as `claude-opus-4-7`/`claude-opus-4-6`/`claude-sonnet-4-6`/`claude-haiku-4-5` or a `model_config` object with `id` + `speed: "standard"|"fast"`), `mcp_servers` (max 20 URL-typed MCP servers, unique names), `skills` (max 20, each `anthropic` or `custom` with optional version pin), `tools` (max 128 across toolsets, mixing `agent_toolset_20260401` built-ins like bash/edit/read/write/glob/grep/web_fetch/web_search, `mcp_toolset` references, and client-executed `custom` tools), `metadata` (≤16 KV pairs), `created_at`/`updated_at`/`archived_at` and a monotonically-increasing `version`.

**Permission policies** for both built-in toolsets and MCP toolsets are `always_allow` or `always_ask`, set per-tool or via a `default_config`.

Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
