---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/sessions/create.md
source_url: https://platform.claude.com/docs/en/api/beta/sessions/create
title: "Create Session"
summarized_at: 2026-05-05
entities_referenced: [Session-API, Managed-agent]
concepts_referenced: []
---

`POST /v1/sessions` — create a new conversation session bound to a Managed Agent.

The body accepts the agent reference plus optional metadata and vault associations. Returns the new session object including `id` and timestamps; the session can then accept event sends, file/MCP resource attachments, and SSE streaming. Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
