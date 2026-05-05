---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/admin/api_keys/retrieve.md
source_url: https://platform.claude.com/docs/en/api/admin/api_keys/retrieve
title: "Retrieve"
summarized_at: 2026-05-05
entities_referenced: [Admin-API, API-key, Workspace]
concepts_referenced: []
---

`GET /v1/organizations/api_keys/{api_key_id}` — fetch one API key's metadata by ID.

Path parameter: `api_key_id: string`.

Returns an `APIKey` object:
- `id` — key ID (the Admin API never returns the full secret value; only Console reveals it at creation time).
- `type: "api_key"`.
- `name` — human-friendly label.
- `status: "active" | "inactive" | "archived" | "expired"`.
- `partial_key_hint: string` — redacted preview (e.g. last few chars) used to identify the secret in Console UI without exposing it.
- `expires_at` — RFC 3339 expiration timestamp, or `null` if the key never expires.
- `created_at` — RFC 3339 creation timestamp.
- `created_by: {id, type}` — actor (user / service account) that created the key.
- `workspace_id` — owning Workspace, or `null` if it belongs to the default Workspace.

Auth: `X-Api-Key: $ANTHROPIC_ADMIN_API_KEY` + `anthropic-version: 2023-06-01`. No body or query parameters. cURL example provided. Useful for inspecting a specific key's status during incident response (e.g. before calling Update to set `status:"inactive"`), or for confirming `workspace_id` ownership before rotating.
