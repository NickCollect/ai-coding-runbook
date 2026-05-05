---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/models/list.md
source_url: https://platform.claude.com/docs/en/api/models/list
title: "List"
summarized_at: 2026-05-05
entities_referenced: [Messages-API]
concepts_referenced: []
---

`GET /v1/models` — lists every model available to the calling API key, most recently released first. Used for runtime model discovery, capability inspection, and resolving aliases programmatically before sending a Messages API request.

Query parameters (all optional, cursor pagination):
- `after_id: string` — return the page after this model ID.
- `before_id: string` — return the page before this model ID.
- `limit: number` — items per page; default 20, range 1–1000.

Header parameters: standard `anthropic-version: 2023-06-01` plus optional `anthropic-beta` accepting the 24-value beta-flag enum (e.g. `message-batches-2024-09-24`, `prompt-caching-2024-07-31`, `pdfs-2024-09-25`, `files-api-2025-04-14`, `interleaved-thinking-2025-05-14`, `code-execution-2025-05-22`, `extended-cache-ttl-2025-04-11`, `context-1m-2025-08-07`, `skills-2025-10-02`, `fast-mode-2026-02-01`, `output-300k-2026-03-24`).

Response:
- `data: array of ModelInfo` — each entry has `id`, `display_name`, `created_at` (RFC 3339; may be epoch if release date unknown), `max_input_tokens`, `max_tokens`, `type:"model"`, plus a structured `capabilities` object (`batch`, `citations`, `code_execution`, `image_input`, `pdf_input`, `structured_outputs`, `context_management` with strategies `clear_thinking_20251015`/`clear_tool_uses_20250919`/`compact_20260112`, `effort` with `low`/`medium`/`high`/`max`/`xhigh`, `thinking` with `adaptive`/`enabled` types). Each capability is a `CapabilitySupport` object with a `supported: boolean`.
- `first_id`, `last_id`, `has_more` — pagination metadata.

Auth: `X-Api-Key`. cURL example provided.
