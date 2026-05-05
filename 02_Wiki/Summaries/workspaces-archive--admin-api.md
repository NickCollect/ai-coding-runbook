---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/admin/workspaces/archive.md
source_url: https://platform.claude.com/docs/en/api/admin/workspaces/archive
title: "Archive"
summarized_at: 2026-05-05
entities_referenced: [Admin-API, Workspace]
concepts_referenced: []
---

`POST /v1/organizations/workspaces/{workspace_id}/archive` — archive a Workspace. Archive is the soft-delete equivalent for Workspaces (there is no hard `DELETE /workspaces/{id}` endpoint).

Path parameter: `workspace_id: string`.

Effect: sets `archived_at` to the current RFC 3339 timestamp on the Workspace. Archived workspaces are hidden from List responses by default — to see them, call List with `include_archived:true`. API keys still bound to an archived workspace stop authorizing new requests.

Returns the updated `Workspace`:
- `id`, `type:"workspace"`, `name`, `display_color`, `data_residency` (`workspace_geo`, `allowed_inference_geos`, `default_inference_geo`), `created_at`, and now-set `archived_at`.

Auth: `X-Api-Key: $ANTHROPIC_ADMIN_API_KEY` + `anthropic-version: 2023-06-01`. No body or query parameters. cURL example uses `-X POST`.

Common patterns: end-of-project cleanup (archive once team is offboarded), compliance-driven retirement of EU-only Workspaces ahead of switching to a different geo (since `workspace_geo` is immutable, archive + recreate is the only path), bulk-archive scripts that walk List and archive Workspaces with no recent usage (cross-reference Cost-report or Usage-report by `workspace_id`). Note: the doc does not document an Unarchive endpoint — treat archive as one-way absent further confirmation.
