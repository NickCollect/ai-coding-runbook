---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/messages/batches/list.md
source_url: https://platform.claude.com/docs/en/api/beta/messages/batches/list
title: "List Message Batches"
summarized_at: 2026-05-05
entities_referenced: [Batches-API]
concepts_referenced: []
---

`GET /v1/messages/batches` — paginated list of message batches submitted by the calling org. Standard cursor pagination. Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
