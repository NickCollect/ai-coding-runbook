---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/sessions/resources/delete.md
source_url: https://platform.claude.com/docs/en/api/beta/sessions/resources/delete
title: "Delete Session Resource"
summarized_at: 2026-05-05
entities_referenced: [Session-API]
concepts_referenced: []
---

`DELETE /v1/sessions/{session_id}/resources/{resource_id}` — detach a resource from a session. **Path params:** `session_id`, `resource_id`. Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
