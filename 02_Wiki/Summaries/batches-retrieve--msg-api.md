---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/messages/batches/retrieve.md
source_url: https://platform.claude.com/docs/en/api/messages/batches/retrieve
title: "Retrieve"
summarized_at: 2026-05-05
entities_referenced: [Batches-API]
concepts_referenced: []
---

`GET /v1/messages/batches/{message_batch_id}` — fetch the current state of a Message Batch. The endpoint is **idempotent** and safe to call repeatedly, making it the canonical way to poll for completion.

Path parameter: `message_batch_id: string`.

Returns `MessageBatch`:
- `id`, `type:"message_batch"`.
- `processing_status: "in_progress" | "canceling" | "ended"`.
- `request_counts`: tally of `processing`, `succeeded`, `errored`, `canceled`, `expired`. The non-`processing` counters remain zero until the batch as a whole ends; their sum then equals the total number of requests.
- Lifecycle timestamps (RFC 3339): `created_at`, `expires_at` (24h after creation — batch ends if not finished by then), `ended_at` (set once processing ends), `cancel_initiated_at` (set only if cancellation was requested), `archived_at` (set when results become unavailable).
- `results_url`: pointer to the `.jsonl` results file; `null` until processing ends. To consume results, hit the Results endpoint (which streams that same `.jsonl`).

Polling pattern documented in the description: poll Retrieve until `processing_status == "ended"`, then GET the `results_url` (or the Results endpoint).

Auth: `X-Api-Key` + `anthropic-version: 2023-06-01`. cURL example provided. No body or query parameters.
