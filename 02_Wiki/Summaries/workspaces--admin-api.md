---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/admin/workspaces.md
source_url: https://platform.claude.com/docs/en/api/admin/workspaces
title: "Workspaces"
summarized_at: 2026-05-05
entities_referenced: [Admin-API, Workspace, Rate-limit-API]
concepts_referenced: []
---

Aggregate Admin API reference covering Workspaces (5 endpoints), Workspace Members (5 endpoints), and Workspace Rate Limits (1 endpoint). All under `/v1/organizations/workspaces/...`. Auth: `X-Api-Key: $ANTHROPIC_ADMIN_API_KEY` + `anthropic-version: 2023-06-01`.

**Workspaces:**
- **Create** (`POST /v1/organizations/workspaces`) — body: `name`, optional `data_residency` (`workspace_geo` immutable after creation, defaults `"us"`; `allowed_inference_geos` defaults `"unrestricted"`; `default_inference_geo` defaults `"global"`).
- **Retrieve / List / Update / Archive** — standard CRUDish pattern. List supports `include_archived: boolean`. Update permits `name` and `data_residency` (geo), but **not** `workspace_geo`.

`Workspace` shape: `id`, `type:"workspace"`, `name`, `display_color` (hex), `data_residency`, `created_at`, `archived_at` (or `null`).

**Members** (workspace-scoped, under `/{workspace_id}/members`):
- **Create / Retrieve / List / Update / Delete** — links a User to a Workspace with a `workspace_role`: `workspace_user`, `workspace_developer`, `workspace_restricted_developer`, `workspace_admin` (and the read enum also includes `workspace_billing`, which is **not** assignable on Create). Distinct from the org-level role on the User object.

`WorkspaceMember` shape: `type:"workspace_member"`, `user_id`, `workspace_id`, `workspace_role`. Delete returns `MemberDeleteResponse` with `type:"workspace_member_deleted"`.

**Rate Limits** (per-workspace overrides):
- **List** (`GET /{workspace_id}/rate_limits`) — returns only groups with at least one workspace-level override. Each override row carries `org_limit` (the parent org value, for reference) plus the new `value`. Groups without overrides inherit org limits and aren't listed (use `/v1/organizations/rate_limits` for those).

Cursor pagination on Workspaces list and Members list (`after_id`/`before_id`/`limit` 1–1000, default 20). cURL examples for every verb.
