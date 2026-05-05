---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/completions.md
source_url: https://platform.claude.com/docs/en/api/completions
title: "Completions"
summarized_at: 2026-05-05
entities_referenced: [Completions-API, Messages-API]
concepts_referenced: []
---

Aggregate reference for the legacy Text Completions API. Single endpoint: `POST /v1/complete`. The doc explicitly marks the API as `[Legacy]` and recommends migrating to the Messages API; it states "Future models and features will not be compatible with Text Completions" and links to a migration guide.

Body parameters: `model` (the same model enum as Messages — `claude-opus-4-7`, `claude-mythos-preview`, `claude-opus-4-6`, `claude-sonnet-4-6`, `claude-haiku-4-5`/`-20251001`, `claude-opus-4-5`/`-20251101`, `claude-sonnet-4-5`/`-20250929`, `claude-opus-4-1`/`-20250805`, `claude-opus-4-0`/`-20250514`, `claude-sonnet-4-0`/`-20250514`, `claude-3-haiku-20240307`); `prompt: string` requiring the legacy `\n\nHuman: ...\n\nAssistant:` framing; `max_tokens_to_sample`; optional `metadata.user_id`, `stop_sequences` (built-in stop is `\n\nHuman:`), `stream` (SSE), `temperature` (default 1.0, range 0–1), `top_k`, `top_p`.

Header parameters include the standard `anthropic-version` and optional `anthropic-beta` (same 24-value enum as Messages).

Response shape: `Completion` object with `id`, `completion: string` (text up to but excluding the stop sequence), `model`, `stop_reason` (`stop_sequence` or `max_tokens`), `type:"completion"`.

cURL example uses `claude-2.1`, `max_tokens_to_sample: 256`, prompt `\\n\\nHuman: Hello, world!\\n\\nAssistant:`, and `--max-time 600` for the long-poll. Auth via `X-Api-Key`. Most modern features (tools, prompt caching, citations, vision, extended thinking, batches, files) are unavailable on this endpoint — Messages API is the supported path.
