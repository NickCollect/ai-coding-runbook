---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/admin/invites/delete.md
source_url: https://platform.claude.com/docs/en/api/admin/invites/delete
title: "Delete"
summarized_at: 2026-05-05
entities_referenced: [Admin-API, Invite]
concepts_referenced: []
---

`DELETE /v1/organizations/invites/{invite_id}` — revoke an outstanding invite.

Path parameter: `invite_id: string`.

Returns a small `InviteDeleteResponse` object:
- `id: string` — the deleted invite's ID.
- `type: "invite_deleted"` — fixed deletion marker type.

After deletion, the invite no longer appears as `pending` in subsequent List calls; it surfaces with `status:"deleted"` (or is hidden, depending on Anthropic's retention policy). The recipient can no longer accept the invitation. If the invite had already been `accepted`, the corresponding User entry is unaffected — to remove a User, call the Users Delete endpoint instead.

Auth: `X-Api-Key: $ANTHROPIC_ADMIN_API_KEY` + `anthropic-version: 2023-06-01`. No body or query parameters. cURL example uses `-X DELETE`.

Common use: revoking a mistakenly-sent invite, cleaning up stale pending invites for departed prospects, or bulk-cleanup scripts that expire invites older than N days. Pairs with the List endpoint (filter to `status:"pending"`, sort by `invited_at`) for batch cleanup.
