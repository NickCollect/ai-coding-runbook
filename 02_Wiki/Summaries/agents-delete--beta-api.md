---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/agents/delete.md
source_url: https://platform.claude.com/docs/en/api/beta/agents/delete
title: "Delete Agent"
summarized_at: 2026-05-05
entities_referenced: [Managed-agent]
concepts_referenced: []
---

Page documenting `DELETE /v1/agents/{agent_id}` — hard delete of a Managed Agent.

The fetched markdown for this endpoint rendered as a stub ("Loading..." with title "API Reference - Claude API Docs") rather than the full schema. The endpoint exists at `https://platform.claude.com/docs/en/api/beta/agents/delete` but the static export captured here contains no parameter, body, or response detail.

By analogy with peer beta resources (sessions, environments, memory_stores, vaults), the route is `DELETE /v1/agents/{agent_id}` taking only the `agent_id` path parameter and the `anthropic-beta` header. Treat the official live docs as authoritative; do not invent a response shape from this raw file alone.

Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
