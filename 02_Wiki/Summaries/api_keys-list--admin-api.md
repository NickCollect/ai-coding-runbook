---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/admin/api_keys/list.md
source_url: https://platform.claude.com/docs/en/api/admin/api_keys/list
title: "List"
summarized_at: 2026-05-05
entities_referenced: [Admin-API, API-key, Workspace]
concepts_referenced: []
---

`GET /v1/organizations/api_keys` — list every API key in the organization.

Query parameters (all optional):
- `after_id`, `before_id` — cursor pagination.
- `limit: number` — items per page; default 20, range 1–1000.
- `status: "active" | "inactive" | "archived" | "expired"` — filter by lifecycle status.
- `workspace_id: string` — filter to keys belonging to a specific Workspace.
- `created_by_user_id: string` — filter by the User who originally created the key.

Returns:
- `data: array of APIKey` — each entry has `id`, `type:"api_key"`, `name`, `status` (same enum as the filter), `partial_key_hint` (redacted preview — never the full secret), `expires_at` (RFC 3339 or `null`), `created_at`, `created_by: {id, type}`, `workspace_id` (or `null` for the default workspace).
- `first_id`, `last_id`, `has_more` — pagination metadata.

Auth: `X-Api-Key: $ANTHROPIC_ADMIN_API_KEY` + `anthropic-version: 2023-06-01`. cURL example provided.

Common patterns: audit dashboards (group by `workspace_id`), key-rotation reviews (filter by `created_at` proxy via cursor + `status:"active"`), tracking down which user issued a leaked key (`created_by_user_id`). Pair with the Cost-report and Usage-report endpoints (which can group by `api_key_id`) for spend attribution.
