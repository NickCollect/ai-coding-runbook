---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/completions/create.md
source_url: https://platform.claude.com/docs/en/api/completions/create
title: "Create"
summarized_at: 2026-05-05
entities_referenced: [Completions-API, Messages-API, Streaming-API]
concepts_referenced: []
---

`POST /v1/complete` — `[Legacy]` Create a Text Completion. The doc explicitly marks this as the legacy API and recommends migrating to the Messages API: "Future models and features will not be compatible with Text Completions." A migration guide is linked.

Body parameters:
- `model` — same enum as Messages API (Opus/Sonnet/Haiku families plus `claude-mythos-preview` and the legacy `claude-3-haiku-20240307`).
- `prompt: string` — must use the legacy `\n\nHuman: ...\n\nAssistant:` framing. Improper framing fails prompt validation.
- `max_tokens_to_sample: number` — output cap.
- `metadata.user_id: string` — optional opaque user identifier (uuid/hash, no PII) used by Anthropic for abuse detection.
- `stop_sequences: array of string` — additional stop strings beyond the built-in `\n\nHuman:`.
- `stream: boolean` — server-sent events (Streaming-API).
- `temperature: number` — default 1.0, range 0.0–1.0.
- `top_k: number` and `top_p: number` — advanced sampling controls.

Header parameters: optional `anthropic-beta` accepting the standard 24-value enum (caching, computer-use, pdfs, token-counting, files, mcp-client, thinking, code-execution, context management, skills, fast-mode, output-300k, etc.). Most of these features do not actually apply to Text Completions in practice.

Response: `Completion` object — `id`, `type:"completion"`, `completion: string` (the generated text up to but excluding the stop sequence), `model`, `stop_reason` (`stop_sequence` or `max_tokens`).

cURL example uses `claude-2.1`, `max_tokens_to_sample: 256`, prompt `\\n\\nHuman: Hello, world!\\n\\nAssistant:`, and `--max-time 600`. Auth: `X-Api-Key` + `anthropic-version: 2023-06-01`.
