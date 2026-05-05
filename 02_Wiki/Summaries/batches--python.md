---
type: summary
source: 01_Raw/github/anthropics/skills/skills/claude-api/python/claude-api/batches.md
title: "Message Batches API — Python"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: [Prompt-caching]
---

Anthropic Messages Batches API (`POST /v1/messages/batches`) for asynchronous Messages API processing at **50% of standard pricing**.

**Key facts**: up to 100,000 requests OR 256 MB per batch; most complete within 1 hour (max 24h); results available 29 days after creation; supports all Messages features (vision, tools, caching, etc.).

**Create a batch** with `client.messages.batches.create(requests=[Request(custom_id="...", params=MessageCreateParamsNonStreaming(model="claude-opus-4-7", max_tokens=16000, messages=[{...}]))])`. Each request needs a `custom_id` for later correlation.

**Poll for completion**: `client.messages.batches.retrieve(batch_id)` → check `batch.processing_status == "ended"`. While processing, `batch.request_counts` exposes `processing` count.

**Retrieve results**: `client.messages.batches.results(batch_id)` returns iterator. Result types: `succeeded` (read `result.result.message`), `errored` (`result.result.error.type` distinguishes `invalid_request` (don't retry) vs server errors (safe to retry)), `canceled`, `expired`.

**Cancel** in-flight: `client.messages.batches.cancel(batch_id)` → status becomes `"canceling"`.

**Prompt caching with batches**: shared system prompt with `cache_control: {type: "ephemeral"}` on the cached portion. The cached prefix is shared across all requests in the batch.

End-to-end example shown: classify list of strings using `claude-haiku-4-5` (cheap + fast model for batch classification).
