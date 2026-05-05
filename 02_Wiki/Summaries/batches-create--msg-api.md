---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/messages/batches/create.md
source_url: https://platform.claude.com/docs/en/api/messages/batches/create
title: "Create"
summarized_at: 2026-05-05
entities_referenced: [Batches-API, Messages-API, Prompt-caching]
concepts_referenced: []
---

`POST /v1/messages/batches` — creates a Message Batch for asynchronous bulk processing of Messages API requests. Once submitted, processing starts immediately and can take up to 24 hours.

Body parameters:
- `requests: array of {custom_id, params}` — list of individual Messages API requests bundled into one batch.
  - `custom_id: string` — developer-supplied unique ID per request inside this batch. Used to match results back to inputs because the result file is **not** guaranteed to preserve request order.
  - `params: object` — full Messages API creation payload (same `messages`, `model`, `max_tokens`, `system`, `tools`, `tool_choice`, `temperature`, `top_p`, `top_k`, `stop_sequences`, `stream`, `metadata`, `service_tier`, `mcp_servers`, `thinking`, `context_management`, etc.). Each item is treated as if posted individually to `/v1/messages`.

Same content-block expressivity as Messages API: text (with optional `cache_control` ephemeral 5m/1h breakpoints for Prompt-caching), image, document/PDF, tool_use/tool_result, search results, citations.

Hard cap of 100,000 messages within a single inner request and the documented batch-level limits (number of requests per batch, total payload size — set by org rate limits, see Admin Rate-limit-API `batch` group).

Returns the same `MessageBatch` object as Retrieve: `id`, `processing_status:"in_progress"`, `request_counts` (only `processing` is non-zero on creation), `created_at`, `expires_at` (24h horizon), and other lifecycle timestamps as `null` until ended.

Auth: `X-Api-Key` + `anthropic-version`. Optional `anthropic-beta` flags accepted (same 24-value enum as Messages create). Batches are billed at the discounted batch service tier.
