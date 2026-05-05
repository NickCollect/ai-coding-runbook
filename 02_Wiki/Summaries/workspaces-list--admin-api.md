---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/admin/workspaces/list.md
source_url: https://platform.claude.com/docs/en/api/admin/workspaces/list
title: "List"
summarized_at: 2026-05-05
entities_referenced: [Admin-API, Workspace]
concepts_referenced: []
---

`GET /v1/organizations/workspaces` — paginated list of Workspaces in the organization.

Query parameters (all optional):
- `after_id: string` — cursor returning the page after this Workspace ID.
- `before_id: string` — cursor returning the page before this Workspace ID.
- `include_archived: boolean` — when true, archived Workspaces (those with non-null `archived_at`) are included. Default behavior excludes them.
- `limit: number` — items per page; default 20, range 1–1000.

Returns:
- `data: array of Workspace` — each entry has `id`, `type:"workspace"`, `name`, `display_color` (hex), `data_residency` (`workspace_geo`, `allowed_inference_geos`, `default_inference_geo`), `created_at`, `archived_at` (RFC 3339 or `null`).
- `first_id`, `last_id`, `has_more` — pagination metadata.

Auth: `X-Api-Key: $ANTHROPIC_ADMIN_API_KEY` + `anthropic-version: 2023-06-01`. cURL example provided.

Common patterns: monthly audit of all active Workspaces (omit `include_archived`), discovery of stale archived Workspaces awaiting cleanup (`include_archived:true` then filter `archived_at != null`), routing decisions based on `data_residency.workspace_geo` (e.g. select EU-resident workspace for EU customer data). Pair with `/v1/organizations/workspaces/{workspace_id}/rate_limits` to inspect per-workspace overrides for each listed Workspace.
