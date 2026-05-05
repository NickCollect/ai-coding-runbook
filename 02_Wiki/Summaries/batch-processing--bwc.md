---
type: summary
source: 01_Raw/platform.claude.com/docs/en/build-with-claude/batch-processing.md
source_url: https://platform.claude.com/docs/en/build-with-claude/batch-processing
title: "Batch processing"
summarized_at: 2026-05-05
entities_referenced: [Batches-API, Messages-API, Prompt-caching, Vision, Tool-use]
concepts_referenced: []
---

The Message Batches API processes large volumes of Messages requests asynchronously at **50% standard pricing** with most batches completing in under 1 hour. **Not ZDR-eligible** — async storage required.

## How it works

1. Submit list of requests (each with unique `custom_id` + `params`).
2. System processes asynchronously, each request handled independently.
3. Poll for status; retrieve results when complete (or after 24h).

## Limits

- Max **100,000 requests** OR **256 MB** per batch (whichever first).
- Results available after all complete OR after 24h, whichever first. Batches **expire if not done in 24h**.
- Results retained **29 days** post-creation; metadata persists longer but results no longer downloadable.
- Scoped to Workspace.
- Each request `max_tokens` must be ≥ 1; `max_tokens: 0` (cache pre-warming) **not supported**.
- Batches may slightly exceed Workspace spend limit due to throughput.
- Rate limits apply both to Batch HTTP requests and to in-flight requests-within-batch.

## Pricing (50% of standard)

| Model | Batch input ($/MTok) | Batch output ($/MTok) |
|---|---|---|
| Claude Opus 4.7 | 2.50 | 12.50 |
| Claude Opus 4.6 | 2.50 | 12.50 |
| Claude Opus 4.5 | 2.50 | 12.50 |
| Claude Opus 4.1 | 7.50 | 37.50 |
| Claude Sonnet 4.6 / 4.5 / 4 | 1.50 | 7.50 |
| Claude Haiku 4.5 | 0.50 | 2.50 |
| Claude Haiku 3.5 | 0.40 | 2.00 |
| Claude Haiku 3 | 0.125 | 0.625 |

## Supported

- All active models.
- All Messages API features: vision, tool use, system prompts, multi-turn, beta features.

## Workflow

- `custom_id` regex: `^[a-zA-Z0-9_-]{1,64}$`.
- Use **1-hour cache duration** with prompt caching for shared-context batches (default 5-min cache may expire mid-batch).

## Endpoint

- Create: `POST /v1/messages/batches` with `requests: [{custom_id, params}, ...]`.
