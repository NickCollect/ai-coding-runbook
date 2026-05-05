---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/admin/users/retrieve.md
source_url: https://platform.claude.com/docs/en/api/admin/users/retrieve
title: "Retrieve"
summarized_at: 2026-05-05
entities_referenced: [Admin-API]
concepts_referenced: []
---

`GET /v1/organizations/users/{user_id}` — fetch one User by ID.

Path parameter: `user_id: string`.

Returns the `User` object:
- `id` — User ID.
- `type: "user"`.
- `email` — User's email address.
- `name` — display name.
- `role` — read enum: `user` / `developer` / `billing` / `admin` / `claude_code_user`.
- `added_at` — RFC 3339 timestamp of when the User joined the Organization (typically via accepted Invite).

Auth: `X-Api-Key: $ANTHROPIC_ADMIN_API_KEY` + `anthropic-version: 2023-06-01`. No body or query parameters. cURL example provided.

Common patterns: confirming the current `role` of a User before issuing an Update (e.g. promoting a `user` to `developer`); verifying a User's `email` matches an external IdP record before attempting Delete; lookups during incident response when an `api_key.created_by.id` points to a User and you need their email/name. For email-based lookup use the List endpoint with `email=foo@bar.com` instead — there is no `email` path parameter on Retrieve.
