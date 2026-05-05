---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/agents/retrieve.md
source_url: https://platform.claude.com/docs/en/api/beta/agents/retrieve
title: "Retrieve Agent"
summarized_at: 2026-05-05
entities_referenced: [Managed-agent]
concepts_referenced: []
---

`GET /v1/agents/{agent_id}` — fetch a single Managed Agent.

**Path param:** `agent_id`. Returns the full `BetaManagedAgentsAgent` object (id, type, model, name, description, system, mcp_servers, skills, tools, metadata, version, created_at/updated_at/archived_at).

Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
