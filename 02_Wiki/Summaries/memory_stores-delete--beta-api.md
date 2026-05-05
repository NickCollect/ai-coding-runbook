---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/memory_stores/delete.md
source_url: https://platform.claude.com/docs/en/api/beta/memory_stores/delete
title: "Delete Memory Store"
summarized_at: 2026-05-05
entities_referenced: [Memory-store]
concepts_referenced: []
---

`DELETE /v1/memory_stores/{memory_store_id}` — hard-delete a memory store and (transitively) its memories and version history. **Path param:** `memory_store_id`. Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
