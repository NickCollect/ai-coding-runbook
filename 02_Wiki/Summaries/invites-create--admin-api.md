---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/admin/invites/create.md
source_url: https://platform.claude.com/docs/en/api/admin/invites/create
title: "Create"
summarized_at: 2026-05-05
entities_referenced: [Admin-API, Invite]
concepts_referenced: []
---

`POST /v1/organizations/invites` — create a new invitation to join the organization by email.

Body parameters:
- `email: string` (required) — destination email of the invitee.
- `role: "user" | "developer" | "billing" | "claude_code_user"` (required) — role to grant when the invite is accepted. The `admin` role is **explicitly not assignable** via this endpoint ("Cannot be 'admin'") — admin promotion happens via Console or by updating an existing User.

Returns an `Invite`:
- `id` — Invite ID.
- `type: "invite"`.
- `email` — invitee email.
- `role` — read enum (`user` / `developer` / `billing` / `admin` / `claude_code_user`).
- `status: "pending"` immediately after create.
- `invited_at` — RFC 3339 creation timestamp.
- `expires_at` — RFC 3339 timestamp when the invite expires if unaccepted.

Subsequent status transitions: `pending` → `accepted` (recipient creates an account or links existing → corresponding User entry appears) or `pending` → `expired` (if not accepted by `expires_at`) or `pending` → `deleted` (if the Delete endpoint is called).

Auth: `X-Api-Key: $ANTHROPIC_ADMIN_API_KEY` + `Content-Type: application/json` + `anthropic-version: 2023-06-01`. cURL example: `email: "user@emaildomain.com"`, `role: "user"`. Common automation: bulk-onboard developers by scripting Create calls with `claude_code_user` role for Claude-Code-only access.
