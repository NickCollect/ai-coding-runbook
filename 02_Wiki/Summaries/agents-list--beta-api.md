---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/agents/list.md
source_url: https://platform.claude.com/docs/en/api/beta/agents/list
title: "List Agents"
summarized_at: 2026-05-05
entities_referenced: [Managed-agent]
concepts_referenced: []
---

`GET /v1/agents` — paginated list of Managed Agents.

**Query params:** `created_at[gte]` / `created_at[lte]` (inclusive RFC 3339 bounds), `include_archived` (default false), `limit` (default 20, max 100), `page` (opaque cursor from previous response).

**Returns** `data: array of BetaManagedAgentsAgent` (full agent objects with `id`, `model`, `name`, `description`, `system`, `mcp_servers`, `skills`, `tools`, `metadata`, `version`, timestamps) plus `next_page` cursor (null when no more results).

Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
