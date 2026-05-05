---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/agents/update.md
source_url: https://platform.claude.com/docs/en/api/beta/agents/update
title: "Update Agent"
summarized_at: 2026-05-05
entities_referenced: [Managed-agent, Skill-API, MCP-server, Tool-use]
concepts_referenced: []
---

`POST /v1/agents/{agent_id}` — modify an existing Managed Agent.

**Path param:** `agent_id`. **Required body param:** `version` (the agent's current `version` — supplies optimistic-concurrency check; the update fails if the stored version has advanced).

**Optional body params** (only fields you wish to change): `name`, `description`, `system`, `model` (model string or `model_config` with `id` + optional `speed`), `mcp_servers`, `skills`, `tools` (same shape as Create — built-in `agent_toolset_20260401`, `mcp_toolset`, or `custom`), `metadata`.

Returns the updated `BetaManagedAgentsAgent` with an incremented `version` and a refreshed `updated_at`.

Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
