---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/agents/versions/list.md
source_url: https://platform.claude.com/docs/en/api/beta/agents/versions/list
title: "List Agent Versions"
summarized_at: 2026-05-05
entities_referenced: [Managed-agent]
concepts_referenced: []
---

`GET /v1/agents/{agent_id}/versions` — list every historical version of a Managed Agent.

**Path param:** `agent_id`. Standard pagination headers/cursor apply per the parent resource conventions. Returns each historical `BetaManagedAgentsAgent` snapshot keyed by its `version` integer (starts at 1, increments on every Update).

Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
