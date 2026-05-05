---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/memory_stores/memories/update.md
source_url: https://platform.claude.com/docs/en/api/beta/memory_stores/memories/update
title: "Update Memory"
summarized_at: 2026-05-05
entities_referenced: [Memory-store]
concepts_referenced: []
---

`POST /v1/memory_stores/{memory_store_id}/memories/{memory_id}` — update a memory's content and/or path.

**Path params:** `memory_store_id`, `memory_id`. **Query param:** optional `view` (`basic` | `full`).

**Body params (all optional):**
- `content` — new UTF-8 text, ≤100 kB. Omit to leave content unchanged (e.g. for rename-only).
- `path` — new path; same validation as Create (starts with `/`, no `.`/`..`/empty segments, NFC-normalized, ≤1024 bytes, case-sensitive). The memory's `id` is preserved across renames.
- `precondition` — `BetaManagedAgentsPrecondition` of `{ type: "content_sha256", value: <sha> }`. The update applies only if the stored `content_sha256` equals the supplied value; on mismatch returns `memory_precondition_failed_error` (HTTP 409). If the precondition fails but stored state already exactly matches the requested `content` and `path`, the server returns 200 instead of 409 (idempotent no-op).

Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
