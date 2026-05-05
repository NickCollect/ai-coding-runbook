---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/admin/workspaces/members.md
source_url: https://platform.claude.com/docs/en/api/admin/workspaces/members
title: "Members"
summarized_at: 2026-05-05
entities_referenced: [Admin-API, Workspace]
concepts_referenced: []
---

Aggregate Admin API reference for Workspace Members — the join table linking Users to Workspaces with a per-Workspace role. Five endpoints under `/v1/organizations/workspaces/{workspace_id}/members/...`:

1. **Create** (`POST .../members`) — body: `user_id` (Users must already exist via accepted Invite), `workspace_role` (one of `workspace_user`, `workspace_developer`, `workspace_restricted_developer`, `workspace_admin`; the read enum also includes `workspace_billing` which is **not** assignable here).
2. **Retrieve** (`GET .../members/{user_id}`).
3. **List** (`GET .../members`) — cursor pagination via `after_id`/`before_id`/`limit` (1–1000, default 20).
4. **Update** (`POST .../members/{user_id}`) — body: `workspace_role` (full read enum including `workspace_billing` allowed here).
5. **Delete** (`DELETE .../members/{user_id}`) — returns `MemberDeleteResponse` (`type:"workspace_member_deleted"`, `user_id`, `workspace_id`).

`WorkspaceMember` shape: `type:"workspace_member"`, `user_id`, `workspace_id`, `workspace_role` (one of the 5 enum values).

Distinction with org-level User role: a User has a single org-wide `role` on the User object (`user`/`developer`/`billing`/`admin`/`claude_code_user`), and additionally a per-Workspace `workspace_role` for each Workspace they're a member of. Workspace permissions are scoped to that Workspace; org permissions are global.

Auth: `X-Api-Key: $ANTHROPIC_ADMIN_API_KEY` + `anthropic-version: 2023-06-01`. cURL examples for every verb. Common patterns: bulk-add a team to a new Workspace (List org Users → loop Create Member), promote a `workspace_developer` to `workspace_admin`, offboard a User from one specific Workspace without removing them from the org.
