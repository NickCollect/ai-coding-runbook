---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/messages/batches/list.md
source_url: https://platform.claude.com/docs/en/api/messages/batches/list
title: "List"
summarized_at: 2026-05-05
entities_referenced: [Batches-API]
concepts_referenced: []
---

`GET /v1/messages/batches` — lists all Message Batches within the calling Workspace, most recently created first.

Query parameters (all optional):
- `after_id: string` — cursor returning the page immediately after this object.
- `before_id: string` — cursor returning the page immediately before this object.
- `limit: number` — items per page; default 20, range 1–1000.

Returns:
- `data: array of MessageBatch` — same shape as the Retrieve response: `id`, `type:"message_batch"`, `processing_status` (`in_progress` / `canceling` / `ended`), `request_counts` (`processing`, `succeeded`, `errored`, `canceled`, `expired`), lifecycle timestamps (`created_at`, `expires_at`, `ended_at`, `cancel_initiated_at`, `archived_at`), and `results_url` once processing has ended.
- `first_id: string` — for paging backwards (use as `before_id`).
- `last_id: string` — for paging forwards (use as `after_id`).
- `has_more: boolean` — true if more results exist in the current direction.

Auth: standard `X-Api-Key` (Messages API key, not admin) plus `anthropic-version: 2023-06-01`. Scoping is by Workspace — using a key from a different workspace returns that workspace's batches only. cURL example provided.
