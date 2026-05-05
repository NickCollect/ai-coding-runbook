---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/admin/users/list.md
source_url: https://platform.claude.com/docs/en/api/admin/users/list
title: "List"
summarized_at: 2026-05-05
entities_referenced: [Admin-API]
concepts_referenced: []
---

`GET /v1/organizations/users` — paginated list of Users in the organization.

Query parameters (all optional):
- `after_id: string` — cursor returning the page after this User ID.
- `before_id: string` — cursor returning the page before this User ID.
- `email: string` — filter by exact user email (e.g. for email-based lookup).
- `limit: number` — items per page; default 20, range 1–1000.

Returns:
- `data: array of User` — each entry has `id`, `type:"user"`, `email`, `name`, `role` (`user`/`developer`/`billing`/`admin`/`claude_code_user`), `added_at` (RFC 3339 — when the User joined the Organization, typically via accepted Invite).
- `first_id`, `last_id`, `has_more` — pagination metadata.

Auth: `X-Api-Key: $ANTHROPIC_ADMIN_API_KEY` + `anthropic-version: 2023-06-01`. cURL example provided.

Common patterns: monthly user audits (paginate the full list and group by `role`), email-to-id resolution (`email=foo@bar.com`, then read `data[0].id`) before calling Update or Delete, joining against Workspace Members via `user_id` to compute "users without any workspace membership", and onboarding/offboarding reconciliation against an external IdP (compare email lists, generate Invite/Delete diff).
