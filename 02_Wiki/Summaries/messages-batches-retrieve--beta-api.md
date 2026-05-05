---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/messages/batches/retrieve.md
source_url: https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve
title: "Retrieve Message Batch"
summarized_at: 2026-05-05
entities_referenced: [Batches-API]
concepts_referenced: []
---

`GET /v1/messages/batches/{message_batch_id}` — fetch a single batch's status, request counts, processing-end ETA, and (when ready) results URL. **Path param:** `message_batch_id`. Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
