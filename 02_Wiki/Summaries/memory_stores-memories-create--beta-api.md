---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/memory_stores/memories/create.md
source_url: https://platform.claude.com/docs/en/api/beta/memory_stores/memories/create
title: "Create Memory"
summarized_at: 2026-05-05
entities_referenced: [Memory-store]
concepts_referenced: []
---

`POST /v1/memory_stores/{memory_store_id}/memories` — create a single memory.

**Path param:** `memory_store_id`. **Query param:** optional `view` (`basic` | `full`).

**Body params:** `content` (UTF-8 text) and `path` (path-style key, must start with `/`, NFC-normalized, ≤1024 bytes, case-sensitive, no `.`/`..`/empty segments).

Returns the created memory object including its assigned `id`. Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
