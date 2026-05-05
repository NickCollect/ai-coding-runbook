---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/admin/workspaces/members/delete.md
source_url: https://platform.claude.com/docs/en/api/admin/workspaces/members/delete
title: "Delete"
summarized_at: 2026-05-05
entities_referenced: [Admin-API, Workspace]
concepts_referenced: []
---

`DELETE /v1/organizations/workspaces/{workspace_id}/members/{user_id}` — remove a User from a single Workspace, leaving the User in the org.

Path parameters:
- `workspace_id: string`.
- `user_id: string`.

Returns a `MemberDeleteResponse`:
- `type: "workspace_member_deleted"` — fixed deletion marker.
- `user_id`.
- `workspace_id`.

Auth: `X-Api-Key: $ANTHROPIC_ADMIN_API_KEY` + `anthropic-version: 2023-06-01`. No body or query parameters. cURL example uses `-X DELETE`.

After the call: the User no longer appears in `.../{workspace_id}/members` List responses, and they lose any access that was scoped to this Workspace. The User's org-level account, org-level role, and other Workspace memberships are unaffected.

Common patterns: project-end cleanup (remove temp Workspace contributors); off-team transfers (delete from old Workspace, create in new one with appropriate `workspace_role`); compliance-driven least-privilege enforcement (periodic audit removes anyone who hasn't generated usage in the last N days, cross-referenced via Usage-report grouped by `workspace_id` and `account_id`). To fully offboard a User from the org, call `DELETE /v1/organizations/users/{user_id}` instead — that cascades the removal across all their Workspace memberships.
