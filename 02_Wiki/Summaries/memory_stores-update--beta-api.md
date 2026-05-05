---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/memory_stores/update.md
source_url: https://platform.claude.com/docs/en/api/beta/memory_stores/update
title: "Update Memory Store"
summarized_at: 2026-05-05
entities_referenced: [Memory-store]
concepts_referenced: []
---

`POST /v1/memory_stores/{memory_store_id}` — patch a memory store.

**Path param:** `memory_store_id`. **Optional body params:** `description`, `metadata`, `name`. Returns the updated memory-store object. Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
