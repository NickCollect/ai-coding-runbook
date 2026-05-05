---
type: summary
source: 01_Raw/platform.claude.com/docs/en/build-with-claude/prompt-caching.md
source_url: https://platform.claude.com/docs/en/build-with-claude/prompt-caching
title: "Prompt caching"
summarized_at: 2026-05-05
entities_referenced: [Prompt-caching, Messages-API, Batches-API]
concepts_referenced: []
---

Prompt caching reuses prompt prefixes between requests to cut latency and cost. ZDR-eligible (only KV cache representations + cryptographic hashes held in memory for cache TTL, not your prompts/outputs).

## Two enablement modes

- **Automatic caching** — single top-level `cache_control: {type: "ephemeral"}` field. System auto-applies the cache breakpoint to last cacheable block and advances it as conversations grow. Best for multi-turn chat.
- **Explicit cache breakpoints** — place `cache_control` on individual content blocks for fine-grained control.

Caching covers the full prefix in this order: `tools` → `system` → `messages`, up to and including the block with `cache_control`.

## Cache lifetime

- **5-minute** default. Refreshed at no cost on each cache hit.
- **1-hour** option at higher cache-write price.

## Pricing (per MTok)

| Model | Base input | 5m write | 1h write | Cache hit/refresh | Output |
|---|---|---|---|---|---|
| Opus 4.7 / 4.6 / 4.5 | $5 | $6.25 | $10 | $0.50 | $25 |
| Opus 4.1 / Opus 4 | $15 | $18.75 | $30 | $1.50 | $75 |
| Sonnet 4.6 / 4.5 / 4 / 3.7 (deprecated) | $3 | $3.75 | $6 | $0.30 | $15 |
| Haiku 4.5 | $1 | $1.25 | $2 | $0.10 | $5 |
| Haiku 3.5 | $0.80 | $1 | $1.6 | $0.08 | $4 |
| Opus 3 (deprecated) | $15 | $18.75 | $30 | $1.50 | $75 |
| Haiku 3 | $0.25 | $0.30 | $0.50 | $0.03 | $1.25 |

**Multipliers** (pricing structure):
- 5m cache write: 1.25× base input
- 1h cache write: 2× base input
- Cache read: 0.1× base input

Multipliers stack with Batch API (50% off) and data residency (1.1× US).

## Use cases

- Many examples in prompt
- Large background context
- Repetitive tasks with consistent instructions
- Long multi-turn conversations
- Cache pre-warming via `max_tokens: 0` (NOT supported inside Batch API, since cache might expire before the follow-up runs)
