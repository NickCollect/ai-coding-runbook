---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/messages/batches/results.md
source_url: https://platform.claude.com/docs/en/api/beta/messages/batches/results
title: "Message Batch Results"
summarized_at: 2026-05-05
entities_referenced: [Batches-API, Messages-API]
concepts_referenced: []
---

`GET /v1/messages/batches/{message_batch_id}/results` — stream the JSONL results of a completed batch.

**Path param:** `message_batch_id`. Each result line is keyed by the `custom_id` supplied at Create time and contains either the successful Messages response or an error envelope. Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
