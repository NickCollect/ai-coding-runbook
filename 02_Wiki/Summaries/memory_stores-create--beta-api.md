---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/memory_stores/create.md
source_url: https://platform.claude.com/docs/en/api/beta/memory_stores/create
title: "Create Memory Store"
summarized_at: 2026-05-05
entities_referenced: [Memory-store]
concepts_referenced: []
---

`POST /v1/memory_stores` — create a new memory store.

**Body params:** `name` (string, required); optional `description` and `metadata` (KV map). Returns the created memory-store object with `id`, `name`, timestamps. Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
