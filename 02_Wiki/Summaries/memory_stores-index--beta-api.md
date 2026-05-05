---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/memory_stores.md
source_url: https://platform.claude.com/docs/en/api/beta/memory_stores
title: "Memory Stores"
summarized_at: 2026-05-05
entities_referenced: [Memory-store]
concepts_referenced: []
---

Beta REST resource for **Memory Stores** under `/v1/memory_stores` plus its child resources `memories` and `memory_versions`. A memory store is a persistent, path-keyed collection of UTF-8 text "memories" with optimistic-concurrency updates and a versioned history.

**Memory-store endpoints on this page:**

- `POST /v1/memory_stores` — Create (required `name`; optional `description`, `metadata`).
- `GET /v1/memory_stores` — List.
- `GET /v1/memory_stores/{memory_store_id}` — Retrieve.
- `POST /v1/memory_stores/{memory_store_id}` — Update (`name`, `description`, `metadata`).
- `DELETE /v1/memory_stores/{memory_store_id}` — Delete.
- `POST /v1/memory_stores/{memory_store_id}/archive` — Archive.

**Memories sub-resource (per memory store):**
- `POST .../memories` — Create a memory (`content`, `path`).
- `GET .../memories` — List memories.
- `GET .../memories/{memory_id}` — Retrieve.
- `POST .../memories/{memory_id}` — Update (`content?`, `path?`, `precondition?`).
- `DELETE .../memories/{memory_id}` — Delete.

**Memory-versions sub-resource:**
- `GET .../memory_versions` — List versions.
- `GET .../memory_versions/{memory_version_id}` — Retrieve a single version.
- `POST .../memory_versions/{memory_version_id}/redact` — Redact a version's content.

Memories are addressed by `path` (must start with `/`, NFC-normalized, no `.`/`..`/empty segments, ≤1024 bytes, case-sensitive). Content is UTF-8, ≤100 kB. Updates accept a `precondition` of `{ type: "content_sha256", value }` for optimistic concurrency; mismatch returns `memory_precondition_failed_error` HTTP 409. A `view` query parameter (`basic` | `full`) governs how much detail is returned.

Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
