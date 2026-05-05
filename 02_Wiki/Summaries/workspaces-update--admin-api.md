---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/admin/workspaces/update.md
source_url: https://platform.claude.com/docs/en/api/admin/workspaces/update
title: "Update"
summarized_at: 2026-05-05
entities_referenced: [Admin-API, Workspace]
concepts_referenced: []
---

`POST /v1/organizations/workspaces/{workspace_id}` — update a Workspace's mutable fields. Notably, `workspace_geo` is **not** mutable here (it's immutable after creation).

Path parameter: `workspace_id: string`.

Body parameters:
- `name: string` (required) — new display name for the Workspace.
- `data_residency: object` (optional) — only the geo policy fields are mutable here:
  - `allowed_inference_geos: array of string | "unrestricted"` — list of permitted inference geos, or `"unrestricted"`.
  - `default_inference_geo: string` — applied when requests omit `inference_geo`. Must be in `allowed_inference_geos` unless that is `"unrestricted"`.

Returns the updated `Workspace`:
- `id`, `type:"workspace"`, `name`, `display_color`, `data_residency` (with the unchanged `workspace_geo`), `created_at`, `archived_at`.

Auth: `X-Api-Key: $ANTHROPIC_ADMIN_API_KEY` + `Content-Type: application/json` + `anthropic-version: 2023-06-01`. cURL example posts `{"name":"x"}`.

Common patterns: renaming a Workspace post-reorganization, tightening `allowed_inference_geos` for compliance (e.g. removing `global` and locking to `us` only), promoting a previously-`global` `default_inference_geo` to `us` for audit-required workloads. For `workspace_geo` changes (which are not allowed) the only path is to Archive the existing Workspace and Create a new one with the desired geo.
