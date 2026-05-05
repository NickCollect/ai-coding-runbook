---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/messages/batches/delete.md
source_url: https://platform.claude.com/docs/en/api/messages/batches/delete
title: "Delete"
summarized_at: 2026-05-05
entities_referenced: [Batches-API]
concepts_referenced: []
---

`DELETE /v1/messages/batches/{message_batch_id}` — permanently delete a Message Batch.

Precondition: a batch can only be deleted once it has **finished processing** (`processing_status == "ended"`). If the batch is still in progress, the caller must first call the Cancel endpoint and wait for it to transition to ended, then call Delete. The doc is explicit: "If you'd like to delete an in-progress batch, you must first cancel it."

Path parameter: `message_batch_id: string`.

Returns a small `DeletedMessageBatch` object:
- `id: string` — the deleted batch's ID.
- `type: "message_batch_deleted"` — fixed deletion marker type.

After deletion, the batch and its associated results file (`results_url`) become unavailable.

Auth: `X-Api-Key` + `anthropic-version: 2023-06-01`. No body or query parameters. cURL example uses `-X DELETE`.

Use cases: housekeeping for completed batches once results have been downloaded and persisted client-side, or proactive removal for compliance/data-residency reasons. Note that batches also have an `archived_at` lifecycle field — once archived, results become unavailable even without explicit deletion (controlled by Anthropic's retention policy, not this endpoint).
