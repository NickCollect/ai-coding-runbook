---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/messages/batches.md
source_url: https://platform.claude.com/docs/en/api/beta/messages/batches
title: "Message Batches"
summarized_at: 2026-05-05
entities_referenced: [Batches-API, Messages-API]
concepts_referenced: []
---

Sub-resource page for **Message Batches** rooted at `/v1/messages/batches`. Batches let clients submit many Messages requests as a single asynchronous job and retrieve results when complete (typically at lower price/SLA than synchronous calls).

**Endpoints on this page:**

- `POST .../batches` — Create (body `requests: array of { custom_id, params }` where each `params` is a full Messages request).
- `GET .../batches/{message_batch_id}` — Retrieve (status / counts / processing window).
- `GET .../batches` — List.
- `POST .../batches/{message_batch_id}/cancel` — Cancel an in-flight batch.
- `DELETE .../batches/{message_batch_id}` — Delete (after completion).
- `GET .../batches/{message_batch_id}/results` — Fetch the JSONL results stream for a completed batch (each line keyed by `custom_id`).

Gated by the `message-batches-2024-09-24` beta header. Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
