---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/sessions/retrieve.md
source_url: https://platform.claude.com/docs/en/api/beta/sessions/retrieve
title: "Retrieve Session"
summarized_at: 2026-05-05
entities_referenced: [Session-API]
concepts_referenced: []
---

`GET /v1/sessions/{session_id}` — fetch a single session by ID. Returns the session object including `title`, `metadata`, linked `vault_ids`, and timestamps. Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
