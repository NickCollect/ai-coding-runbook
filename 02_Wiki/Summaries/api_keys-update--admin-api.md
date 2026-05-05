---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/admin/api_keys/update.md
source_url: https://platform.claude.com/docs/en/api/admin/api_keys/update
title: "Update"
summarized_at: 2026-05-05
entities_referenced: [Admin-API, API-key]
concepts_referenced: []
---

`POST /v1/organizations/api_keys/{api_key_id}` — patch an existing API key. The only mutable fields are `name` and `status`.

Path parameter: `api_key_id: string`.

Body parameters (both optional — empty body `{}` is valid as shown in the cURL example):
- `name: string` — rename the key.
- `status: "active" | "inactive" | "archived"` — narrower than the read enum (you cannot set `expired` directly; expiry is system-managed via `expires_at`).

Common transitions:
- `active` → `inactive` — temporarily disable a key (rotation, suspected leak).
- `inactive` → `active` — re-enable.
- `active`/`inactive` → `archived` — soft-delete (the key remains visible in List with `status:"archived"` filter but no longer authorizes requests).

Returns the updated `APIKey` (full shape: `id`, `type:"api_key"`, `name`, `status`, `partial_key_hint`, `expires_at`, `created_at`, `created_by`, `workspace_id`). The full secret is never returned — only the `partial_key_hint` redacted preview.

Auth: `X-Api-Key: $ANTHROPIC_ADMIN_API_KEY` + `Content-Type: application/json` + `anthropic-version: 2023-06-01`. cURL example provided. There is no separate Delete endpoint for API keys — `archived` status is the closest equivalent, contrasted with Users / Invites which have explicit Delete endpoints.
