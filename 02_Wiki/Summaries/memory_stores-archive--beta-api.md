---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/memory_stores/archive.md
source_url: https://platform.claude.com/docs/en/api/beta/memory_stores/archive
title: "Archive Memory Store"
summarized_at: 2026-05-05
entities_referenced: [Memory-store]
concepts_referenced: []
---

`POST /v1/memory_stores/{memory_store_id}/archive` — soft-delete by setting `archived_at`. **Path param:** `memory_store_id`. Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
