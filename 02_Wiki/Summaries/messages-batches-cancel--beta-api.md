---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/messages/batches/cancel.md
source_url: https://platform.claude.com/docs/en/api/beta/messages/batches/cancel
title: "Cancel Message Batch"
summarized_at: 2026-05-05
entities_referenced: [Batches-API]
concepts_referenced: []
---

`POST /v1/messages/batches/{message_batch_id}/cancel` — cancel an in-flight batch.

**Path param:** `message_batch_id`. The batch transitions to a cancelled state; already-completed sub-requests within it remain billable per Anthropic's batch policy. Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
