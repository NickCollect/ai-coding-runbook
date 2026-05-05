---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/admin/invites.md
source_url: https://platform.claude.com/docs/en/api/admin/invites
title: "Invites"
summarized_at: 2026-05-05
entities_referenced: [Admin-API, Invite]
concepts_referenced: []
---

Aggregate Admin API reference for Invites — invitations sent to email addresses to join the organization. Four endpoints under `/v1/organizations/invites/...`:

1. **Create** (`POST /v1/organizations/invites`) — body: `email`, `role` (`user` / `developer` / `billing` / `claude_code_user`; `admin` is **not** assignable here).
2. **Retrieve** (`GET /v1/organizations/invites/{invite_id}`).
3. **List** (`GET /v1/organizations/invites`) — cursor pagination via `after_id`/`before_id`/`limit` (1–1000, default 20).
4. **Delete** (`DELETE /v1/organizations/invites/{invite_id}`) — returns a small `InviteDeleteResponse` (`id`, `type:"invite_deleted"`).

`Invite` shape: `id`, `type:"invite"`, `email`, `role` (read enum: `user` / `developer` / `billing` / `admin` / `claude_code_user`), `status` (`pending` / `accepted` / `expired` / `deleted`), `invited_at`, `expires_at` (RFC 3339).

Lifecycle: an Invite starts as `pending`. When the recipient accepts, status moves to `accepted` and a corresponding User is added to the org (visible via `/v1/organizations/users`). Unaccepted invites eventually become `expired` per Anthropic's retention policy. `Delete` revokes a pending or expired invite — the resulting status surface in subsequent reads is `deleted`.

Auth: `X-Api-Key: $ANTHROPIC_ADMIN_API_KEY` + `anthropic-version: 2023-06-01`. cURL examples for each verb. Note the role discrepancy: write side rejects `admin` (admins are promoted via existing User Update or via Console), while the read side may surface `admin` for roles that came in via other paths.
