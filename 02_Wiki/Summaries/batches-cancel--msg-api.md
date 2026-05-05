---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/messages/batches/cancel.md
source_url: https://platform.claude.com/docs/en/api/messages/batches/cancel
title: "Cancel"
summarized_at: 2026-05-05
entities_referenced: [Batches-API]
concepts_referenced: []
---

`POST /v1/messages/batches/{message_batch_id}/cancel` — initiate cancellation of a Message Batch any time before processing ends.

Path parameter: `message_batch_id: string`.

Behavior: once cancellation is requested, the batch enters the `canceling` state. The system may complete already-in-progress, non-interruptible requests before fully transitioning to `ended`. Cancellation is therefore best-effort — the documented caveat is "Note that cancellation may not result in any canceled requests if they were non-interruptible." To find out which requests were actually canceled, inspect the per-request results in the `.jsonl` results file.

Returns the same `MessageBatch` object as Retrieve. Notable fields right after cancel:
- `processing_status: "canceling"` (eventually transitions to `"ended"`).
- `cancel_initiated_at`: set to the current RFC 3339 timestamp.
- `request_counts.canceled`: stays at 0 until processing of the entire batch ends, then reflects the final canceled count.

Auth: `X-Api-Key` + `anthropic-version: 2023-06-01`. No body or query parameters. cURL example uses `-X POST`.

Required step before deletion: a batch can only be deleted once it has finished processing, so an in-progress batch must be canceled first (then deleted via the Delete endpoint).
