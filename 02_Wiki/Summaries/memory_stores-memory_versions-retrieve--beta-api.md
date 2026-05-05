---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/retrieve.md
source_url: https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/retrieve
title: "Retrieve Memory Version"
summarized_at: 2026-05-05
entities_referenced: [Memory-store]
concepts_referenced: []
---

`GET /v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}` — fetch a single historical version.

**Path params:** `memory_store_id`, `memory_version_id`. **Query param:** optional `view` (`basic` | `full`). Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
