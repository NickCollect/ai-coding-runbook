---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/sessions/events/list.md
source_url: https://platform.claude.com/docs/en/api/beta/sessions/events/list
title: "List Session Events"
summarized_at: 2026-05-05
entities_referenced: [Session-API]
concepts_referenced: []
---

`GET /v1/sessions/{session_id}/events` — list events in a session.

**Path param:** `session_id`. **Query params:** `limit`, `order` (`asc` | `desc`), `page` (opaque cursor).

Returns `data: array of BetaManagedAgentsSessionEvent` plus `next_page`. Use this to reconstruct conversation state without holding an open SSE stream. Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
