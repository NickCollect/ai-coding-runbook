---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/admin/api_keys.md
source_url: https://platform.claude.com/docs/en/api/admin/api_keys
title: "API Keys"
summarized_at: 2026-05-05
entities_referenced: [Admin-API, API-key, Workspace]
concepts_referenced: []
---

Aggregate Admin API reference for API key management. Three endpoints under `/v1/organizations/api_keys/...`. Auth via the **admin** key (`X-Api-Key: $ANTHROPIC_ADMIN_API_KEY` — distinct from a normal Messages API key) plus `anthropic-version: 2023-06-01`. There is no Create endpoint — keys must be created via the Anthropic Console.

1. **Retrieve** (`GET /v1/organizations/api_keys/{api_key_id}`) — fetch a single API key by ID.
2. **List** (`GET /v1/organizations/api_keys`) — paginated list. Filters: `status` (`active`/`inactive`/`archived`/`expired`), `workspace_id`, `created_by_user_id`. Cursor pagination via `after_id`/`before_id`/`limit` (1–1000, default 20).
3. **Update** (`POST /v1/organizations/api_keys/{api_key_id}`) — patch `name` and/or `status`. Status enum on update is the narrower `active` / `inactive` / `archived` (no setting to `expired` directly).

`APIKey` shape: `id`, `type:"api_key"`, `name`, `status` (`active` / `inactive` / `archived` / `expired`), `partial_key_hint` (redacted preview — full secret never exposed by Admin API), `expires_at` (RFC 3339 or `null` if never), `created_at`, `created_by` (`{id, type}` of the actor — user or service account that minted it), `workspace_id` (or `null` for the org's default workspace).

cURL examples provided for each endpoint. Common operations: rotating compromised keys (set `status:"inactive"`), archival, audit (List grouped by `workspace_id` or filtered by `created_by_user_id`), and cross-checking against the org's Cost-report and Usage-report by api_key_id.
