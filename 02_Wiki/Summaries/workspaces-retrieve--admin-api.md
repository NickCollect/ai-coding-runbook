---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/admin/workspaces/retrieve.md
source_url: https://platform.claude.com/docs/en/api/admin/workspaces/retrieve
title: "Retrieve"
summarized_at: 2026-05-05
entities_referenced: [Admin-API, Workspace]
concepts_referenced: []
---

`GET /v1/organizations/workspaces/{workspace_id}` — fetch one Workspace by ID.

Path parameter: `workspace_id: string`.

Returns the `Workspace` object:
- `id` — Workspace ID.
- `type: "workspace"`.
- `name` — display name.
- `display_color` — hex color code used to represent the Workspace in the Anthropic Console UI.
- `data_residency`:
  - `workspace_geo: string` — geographic region for workspace data storage. Immutable after creation.
  - `allowed_inference_geos: array of string | "unrestricted"` — permitted inference geos.
  - `default_inference_geo: string` — applied when requests omit the parameter.
- `created_at` — RFC 3339 timestamp of Workspace creation.
- `archived_at` — RFC 3339 archive timestamp, or `null` if not archived.

Auth: `X-Api-Key: $ANTHROPIC_ADMIN_API_KEY` + `anthropic-version: 2023-06-01`. No body or query parameters. cURL example provided.

Common patterns: confirming a Workspace's `data_residency` configuration before routing requests through it (e.g. EU-only flows need `workspace_geo:"eu"`); checking `archived_at` to skip dead workspaces in audit scripts; verifying `display_color` for branding consistency. For listing all Workspaces use the List endpoint (which supports `include_archived` to filter archived ones).
