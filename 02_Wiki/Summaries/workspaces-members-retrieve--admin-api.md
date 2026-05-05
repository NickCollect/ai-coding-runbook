---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/admin/workspaces/members/retrieve.md
source_url: https://platform.claude.com/docs/en/api/admin/workspaces/members/retrieve
title: "Retrieve"
summarized_at: 2026-05-05
entities_referenced: [Admin-API, Workspace]
concepts_referenced: []
---

`GET /v1/organizations/workspaces/{workspace_id}/members/{user_id}` — fetch one Workspace Member entry by composite key `(workspace_id, user_id)`.

Path parameters:
- `workspace_id: string` — ID of the Workspace.
- `user_id: string` — ID of the User.

Returns the `WorkspaceMember` object:
- `type: "workspace_member"`.
- `user_id`.
- `workspace_id`.
- `workspace_role: "workspace_user" | "workspace_developer" | "workspace_restricted_developer" | "workspace_admin" | "workspace_billing"`.

Auth: `X-Api-Key: $ANTHROPIC_ADMIN_API_KEY` + `anthropic-version: 2023-06-01`. No body or query parameters. cURL example provided.

Returns 404 if the User is not a member of the Workspace. Common patterns: confirm the current `workspace_role` of a User in a Workspace before Update; access-control checks in admin tooling (does this User actually belong to this Workspace?); audit scripts that walk Workspaces.list × Users.list and call Retrieve for each pair to build a complete (workspace, user, role) table. For bulk inspection of a single Workspace's roster prefer the List endpoint at `.../members`.
