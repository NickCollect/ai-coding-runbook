---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/admin/workspaces/members/create.md
source_url: https://platform.claude.com/docs/en/api/admin/workspaces/members/create
title: "Create"
summarized_at: 2026-05-05
entities_referenced: [Admin-API, Workspace]
concepts_referenced: []
---

`POST /v1/organizations/workspaces/{workspace_id}/members` — add an existing User to a Workspace with a specific role. The User must already exist in the org (created via accepted Invite or initial setup).

Path parameter: `workspace_id: string`.

Body parameters:
- `user_id: string` (required) — ID of an existing User.
- `workspace_role: "workspace_user" | "workspace_developer" | "workspace_restricted_developer" | "workspace_admin"` (required) — initial Workspace role. The `workspace_billing` value is **not** assignable on Create (the read enum and Update both expose it, but Create restricts to four values).

Returns the new `WorkspaceMember`:
- `type: "workspace_member"`.
- `user_id`.
- `workspace_id`.
- `workspace_role` — full read enum (5 values: 4 above + `workspace_billing`).

Auth: `X-Api-Key: $ANTHROPIC_ADMIN_API_KEY` + `Content-Type: application/json` + `anthropic-version: 2023-06-01`. cURL example posts `{"user_id":"user_01WCz1FkmYMm4gnmykNKUu3Q","workspace_role":"workspace_user"}`.

Common patterns: scripted onboarding (after the org-level Invite is accepted, loop over relevant Workspaces and Create a Member with the appropriate role per Workspace), default-role expansion (every new developer gets `workspace_developer` on the engineering Workspace and `workspace_user` elsewhere), and team-bootstrap (List Users in the org → filter by some criterion → Create a Member in a fresh Workspace for each).
