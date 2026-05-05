---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/admin/workspaces/create.md
source_url: https://platform.claude.com/docs/en/api/admin/workspaces/create
title: "Create"
summarized_at: 2026-05-05
entities_referenced: [Admin-API, Workspace]
concepts_referenced: []
---

`POST /v1/organizations/workspaces` — create a new Workspace within the organization.

Body parameters:
- `name: string` (required) — display name for the Workspace.
- `data_residency: object` (optional) — defaults: `workspace_geo:"us"`, `allowed_inference_geos:"unrestricted"`, `default_inference_geo:"global"`.
  - `workspace_geo: string` — geographic region for workspace data storage. **Immutable after creation.**
  - `allowed_inference_geos: array of string | "unrestricted"` — permitted inference geos. Use `"unrestricted"` to allow all, or a specific list.
  - `default_inference_geo: string` — applied when requests omit the `inference_geo` parameter. Must be a member of `allowed_inference_geos` unless that field is `"unrestricted"`.

Returns the new `Workspace`:
- `id`, `type:"workspace"`, `name`, `display_color` (hex string for Console UI), `data_residency` (echoed config), `created_at` (RFC 3339), `archived_at: null`.

Auth: `X-Api-Key: $ANTHROPIC_ADMIN_API_KEY` + `Content-Type: application/json` + `anthropic-version: 2023-06-01`. cURL example posts `{"name":"x"}`.

Important: `workspace_geo` cannot be changed via Update — getting data residency wrong at creation requires deleting (archiving) the Workspace and re-creating it. Plan ahead if you have specific compliance requirements (EU, US-only, etc.). After creation, add Members via `POST /v1/organizations/workspaces/{workspace_id}/members` and configure rate-limit overrides via `POST /v1/organizations/workspaces/{workspace_id}/rate_limits` (where supported — Admin API only exposes List for workspace rate limits in this slice).
