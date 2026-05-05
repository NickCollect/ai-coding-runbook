---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/sessions/resources/update.md
source_url: https://platform.claude.com/docs/en/api/beta/sessions/resources/update
title: "Update Session Resource"
summarized_at: 2026-05-05
entities_referenced: [Session-API]
concepts_referenced: []
---

`POST /v1/sessions/{session_id}/resources/{resource_id}` — update a session resource.

**Path params:** `session_id`, `resource_id`. **Body param:** `authorization_token` (string, required) — supplies a fresh access token for resources that need OAuth-scoped credentials (e.g. when a token has expired). Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
