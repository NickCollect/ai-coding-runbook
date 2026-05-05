---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/admin/users/update.md
source_url: https://platform.claude.com/docs/en/api/admin/users/update
title: "Update"
summarized_at: 2026-05-05
entities_referenced: [Admin-API]
concepts_referenced: []
---

`POST /v1/organizations/users/{user_id}` — update a User's organization-level role. Currently the only mutable field is `role`.

Path parameter: `user_id: string`.

Body parameters:
- `role: "user" | "developer" | "billing" | "claude_code_user"` (required) — new organization role. The `admin` role is **explicitly not assignable** here ("Cannot be 'admin'") — admin promotion is gated to the Anthropic Console UI. The narrower write-side enum mirrors the same restriction in Invites.create.

Returns the updated `User`:
- `id`, `type:"user"`, `email`, `name`, `role` (read enum includes `admin` and `claude_code_user`), `added_at`.

Auth: `X-Api-Key: $ANTHROPIC_ADMIN_API_KEY` + `Content-Type: application/json` + `anthropic-version: 2023-06-01`. cURL example posts `{"role":"user"}`.

Common patterns: bulk role downgrades (List → filter `role:"developer"` → Update to `user` for inactive accounts), promoting users from generic `user` to `developer` (allowing API key creation), or moving a billing-only contact's role to `billing`. Note the distinction with Workspace Members: this endpoint changes org-wide role; per-Workspace permissions are managed via `/v1/organizations/workspaces/{workspace_id}/members/{user_id}` (Workspace Member Update) with the `workspace_role` enum.
