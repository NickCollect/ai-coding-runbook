---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/admin/workspaces/members/list.md
source_url: https://platform.claude.com/docs/en/api/admin/workspaces/members/list
title: "List"
summarized_at: 2026-05-05
entities_referenced: [Admin-API, Workspace]
concepts_referenced: []
---

`GET /v1/organizations/workspaces/{workspace_id}/members` — paginated list of all Members of one Workspace.

Path parameter: `workspace_id: string`.

Query parameters (all optional):
- `after_id: string` — cursor returning the page after this User ID.
- `before_id: string` — cursor returning the page before this User ID.
- `limit: number` — items per page; default 20, range 1–1000.

Returns:
- `data: array of WorkspaceMember` — each entry has `type:"workspace_member"`, `user_id`, `workspace_id` (echoed from the path), `workspace_role` (`workspace_user` / `workspace_developer` / `workspace_restricted_developer` / `workspace_admin` / `workspace_billing`).
- `first_id`, `last_id`, `has_more` — pagination metadata.

No filters by `workspace_role` or `email` are exposed — callers iterate and filter client-side. To resolve `user_id` → email/name, cross-reference against the Users.retrieve endpoint or a cached Users.list.

Auth: `X-Api-Key: $ANTHROPIC_ADMIN_API_KEY` + `anthropic-version: 2023-06-01`. cURL example provided.

Common patterns: monthly access reviews per Workspace, building a cross-Workspace permission matrix (loop Workspaces.list → for each, call this List), discovering orphaned Members (Users who have no other access in the org), generating exports for compliance audits. Bulk-update a role for everyone with `workspace_user` by iterating this list and calling Update.
