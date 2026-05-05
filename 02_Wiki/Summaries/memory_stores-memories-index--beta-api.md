---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/memory_stores/memories.md
source_url: https://platform.claude.com/docs/en/api/beta/memory_stores/memories
title: "Memories"
summarized_at: 2026-05-05
entities_referenced: [Memory-store]
concepts_referenced: []
---

Sub-resource page for **Memories** inside a Memory Store, rooted at `/v1/memory_stores/{memory_store_id}/memories`.

**Endpoints on this page:**

- `POST .../memories` — Create (required `content` and `path`).
- `GET .../memories` — List.
- `GET .../memories/{memory_id}` — Retrieve.
- `POST .../memories/{memory_id}` — Update (`content?`, `path?`, `precondition?`).
- `DELETE .../memories/{memory_id}` — Delete.

A memory is a path-addressed UTF-8 text blob (≤100 kB / 102,400 bytes). `path` must start with `/`, contain at least one non-empty segment, ≤1024 bytes, no `.` or `..`, no empty segments or control/format characters, NFC-normalized; paths are case-sensitive. The memory's `id` survives renames. Updates support optimistic concurrency via a `precondition` of `{ type: "content_sha256" }` matching the stored SHA-256; on mismatch the server returns HTTP 409 `memory_precondition_failed_error`. A `view` query parameter (`basic` or `full`) controls the response shape on read/write endpoints.

Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
