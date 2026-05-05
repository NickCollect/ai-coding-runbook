---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/agents/archive.md
source_url: https://platform.claude.com/docs/en/api/beta/agents/archive
title: "Archive Agent"
summarized_at: 2026-05-05
entities_referenced: [Managed-agent]
concepts_referenced: []
---

`POST /v1/agents/{agent_id}/archive` — soft-deletes an agent by setting its `archived_at` timestamp.

**Path param:** `agent_id`. No body. Returns the updated `BetaManagedAgentsAgent` with `archived_at` populated. Archived agents are excluded from `GET /v1/agents` unless `include_archived=true` is passed.

Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
