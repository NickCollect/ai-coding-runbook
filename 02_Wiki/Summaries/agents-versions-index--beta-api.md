---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/agents/versions.md
source_url: https://platform.claude.com/docs/en/api/beta/agents/versions
title: "Agents Versions"
summarized_at: 2026-05-05
entities_referenced: [Managed-agent]
concepts_referenced: []
---

Beta sub-resource page under `/v1/agents/{agent_id}/versions` listing the version history of a Managed Agent.

**Endpoint listed on this page:**

- `GET /v1/agents/{agent_id}/versions` — List Versions for the given agent.

Each agent's `version` field starts at 1 on Create and increments on every Update. This sub-resource lets clients page through the history of a single agent's edits to inspect what changed and when.

Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
