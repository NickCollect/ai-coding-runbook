---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/messages/batches.md
source_url: https://platform.claude.com/docs/en/api/messages/batches
title: "Batches"
summarized_at: 2026-05-05
entities_referenced: [Batches-API, Messages-API]
concepts_referenced: []
---

Aggregate reference for the Message Batches sub-API. Six lifecycle endpoints under `/v1/messages/batches`:

1. **Create** (`POST /v1/messages/batches`) — body: `requests: array of {custom_id, params}` where `params` is the full Messages API creation payload. `custom_id` must be unique per request within the batch and is used to match results (results are returned out of order). Batches begin processing immediately and may take up to 24h.
2. **Retrieve** (`GET /v1/messages/batches/{message_batch_id}`) — idempotent; safe to poll. Returns `MessageBatch` (see below).
3. **List** (`GET /v1/messages/batches`) — cursor pagination via `after_id`/`before_id`/`limit` (default 20, max 1000). Most recent first, scoped to Workspace.
4. **Cancel** (`POST /v1/messages/batches/{message_batch_id}/cancel`) — moves batch to `canceling`; in-flight non-interruptible requests may still complete.
5. **Delete** (`DELETE /v1/messages/batches/{message_batch_id}`) — only allowed once processing has ended; cancel first if needed.
6. **Results** (`GET /v1/messages/batches/{message_batch_id}/results`) — streams a `.jsonl` file. Each line is a `MessageBatchIndividualResponse` with `custom_id` and `result` (one of: succeeded with full `Message`, errored, canceled, or expired).

`MessageBatch` shape: `id`, `type:"message_batch"`, `processing_status` (`in_progress` / `canceling` / `ended`), `request_counts` (`processing`, `succeeded`, `errored`, `canceled`, `expired` — non-`processing` values stay zero until the entire batch ends), `created_at`, `expires_at` (24h after creation), `ended_at`, `cancel_initiated_at`, `archived_at`, `results_url` (set when ended).

Auth: standard `X-Api-Key`. Beta-flag history: `message-batches-2024-09-24` (now generally available; flag still recognized for back-compat).
