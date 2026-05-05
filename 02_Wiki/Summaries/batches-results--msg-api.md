---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/messages/batches/results.md
source_url: https://platform.claude.com/docs/en/api/messages/batches/results
title: "Results"
summarized_at: 2026-05-05
entities_referenced: [Batches-API, Messages-API]
concepts_referenced: []
---

`GET /v1/messages/batches/{message_batch_id}/results` — streams the per-request results of a completed Message Batch as a `.jsonl` file (one JSON object per line).

Path parameter: `message_batch_id: string`.

Each line is a `MessageBatchIndividualResponse`:
- `custom_id: string` — the unique ID supplied by the developer at batch creation. Critical because results are **not** guaranteed to be in the same order as input requests; the only reliable way to match a result to its source request is by `custom_id`.
- `result: MessageBatchResult` — a tagged union covering the four outcomes:
  1. `MessageBatchSucceededResult` (`type:"succeeded"`) — wraps a full `Message` object identical to what `POST /v1/messages` would have returned: `id`, `content` (array of ContentBlock — text, tool_use, server_tool_use, thinking, citations, etc.), `model`, `stop_reason`, `usage`, optional `container` (when the code execution tool ran).
  2. Errored — wraps an Anthropic API error response.
  3. Canceled — request was canceled before completion.
  4. Expired — request did not complete before the 24h batch expiry.

Streaming is the recommended consumption mode for large batches; the response can also be fetched from the `results_url` field exposed on the `MessageBatch` object once `processing_status == "ended"`.

Auth: `X-Api-Key` + `anthropic-version: 2023-06-01`. No body or query parameters. The endpoint should only be called once the batch has ended (Retrieve returns `processing_status:"ended"`).
