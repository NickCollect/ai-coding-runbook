---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/memory_stores/memories/list.md
source_url: https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list
title: "List Memories"
summarized_at: 2026-05-05
entities_referenced: [Memory-store]
concepts_referenced: []
---

`GET /v1/memory_stores/{memory_store_id}/memories` — list all memories within a store. Standard pagination cursors apply. Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
