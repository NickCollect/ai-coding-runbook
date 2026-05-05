---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/memory_stores/memories/retrieve.md
source_url: https://platform.claude.com/docs/en/api/beta/memory_stores/memories/retrieve
title: "Retrieve Memory"
summarized_at: 2026-05-05
entities_referenced: [Memory-store]
concepts_referenced: []
---

`GET /v1/memory_stores/{memory_store_id}/memories/{memory_id}` — fetch a single memory.

**Path params:** `memory_store_id`, `memory_id`. **Query param:** optional `view` (`basic` | `full`) controlling the response detail. Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
