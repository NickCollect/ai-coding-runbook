---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/admin/workspaces/members/update.md
source_url: https://platform.claude.com/docs/en/api/admin/workspaces/members/update
title: "Update"
summarized_at: 2026-05-05
entities_referenced: [Admin-API, Workspace]
concepts_referenced: []
---

`POST /v1/organizations/workspaces/{workspace_id}/members/{user_id}` — change a Workspace Member's role.

Path parameters:
- `workspace_id: string`.
- `user_id: string`.

Body parameter:
- `workspace_role: "workspace_user" | "workspace_developer" | "workspace_restricted_developer" | "workspace_admin" | "workspace_billing"` (required) — the **full** five-value enum is allowed here, including `workspace_billing` (which Create rejects).

Returns the updated `WorkspaceMember`:
- `type:"workspace_member"`, `user_id`, `workspace_id`, `workspace_role`.

Auth: `X-Api-Key: $ANTHROPIC_ADMIN_API_KEY` + `Content-Type: application/json` + `anthropic-version: 2023-06-01`. cURL example posts `{"workspace_role":"workspace_user"}`.

Common patterns: promote a `workspace_developer` to `workspace_admin` after a team lead change; demote `workspace_admin` to `workspace_user` post-handover; assign `workspace_billing` (only via Update — Create can't set it) so a finance contact can manage spend without engineering access; restrict a contractor's access by moving them from `workspace_developer` to `workspace_restricted_developer`. The endpoint is idempotent — repeating with the same `workspace_role` is a safe no-op. To remove a User from a Workspace entirely, use Delete instead.
