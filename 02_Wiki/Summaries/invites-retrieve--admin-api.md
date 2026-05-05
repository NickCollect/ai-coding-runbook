---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/admin/invites/retrieve.md
source_url: https://platform.claude.com/docs/en/api/admin/invites/retrieve
title: "Retrieve"
summarized_at: 2026-05-05
entities_referenced: [Admin-API, Invite]
concepts_referenced: []
---

`GET /v1/organizations/invites/{invite_id}` — fetch a single Invite by ID.

Path parameter: `invite_id: string`.

Returns the `Invite` object:
- `id` — Invite ID.
- `type: "invite"`.
- `email` — invitee email address.
- `role` — read enum: `user` / `developer` / `billing` / `admin` / `claude_code_user` (note: write-side Create restricts to four values, excluding `admin`).
- `status: "pending" | "accepted" | "expired" | "deleted"`.
- `invited_at` — RFC 3339 creation timestamp.
- `expires_at` — RFC 3339 expiry timestamp.

Auth: `X-Api-Key: $ANTHROPIC_ADMIN_API_KEY` + `anthropic-version: 2023-06-01`. No body or query parameters. cURL example provided.

Use cases: confirming the current `status` of an invite before re-sending or deleting; checking `expires_at` to decide whether to resend; verifying the `role` originally configured before an acceptance event. For bulk inspection use the List endpoint instead.
