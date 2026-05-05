---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/admin/users.md
source_url: https://platform.claude.com/docs/en/api/admin/users
title: "Users"
summarized_at: 2026-05-05
entities_referenced: [Admin-API]
concepts_referenced: []
---

Aggregate Admin API reference for User management. Four endpoints under `/v1/organizations/users/...`:

1. **Retrieve** (`GET /v1/organizations/users/{user_id}`) — fetch one User.
2. **List** (`GET /v1/organizations/users`) — paginated. Filters: `email`. Cursor pagination via `after_id`/`before_id`/`limit` (1–1000, default 20).
3. **Update** (`POST /v1/organizations/users/{user_id}`) — body: `role` (`user` / `developer` / `billing` / `claude_code_user`; cannot be set to `admin` via this endpoint — admin promotion happens via Console).
4. **Delete** (`DELETE /v1/organizations/users/{user_id}`) — remove a User from the org. Returns a small `UserDeleteResponse` (`id`, `type:"user_deleted"`).

`User` shape: `id`, `type:"user"`, `email`, `name`, `role` (read enum: `user` / `developer` / `billing` / `admin` / `claude_code_user`), `added_at` (RFC 3339 — when the User joined the org via accepted invite or initial setup).

There is no Create endpoint — Users are created indirectly via accepted Invites. To onboard a user programmatically, post to `/v1/organizations/invites` with the desired `email` + `role`, then poll the Invite's `status` until `accepted`.

Auth: `X-Api-Key: $ANTHROPIC_ADMIN_API_KEY` + `anthropic-version: 2023-06-01`. cURL examples for each verb. Common flows: bulk role updates (List → filter → Update each), offboarding (Delete by ID), email-based lookup (List with `email=foo@bar.com`).
