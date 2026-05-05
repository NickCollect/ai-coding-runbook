---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/models.md
source_url: https://platform.claude.com/docs/en/api/models
title: "Models"
summarized_at: 2026-05-05
entities_referenced: [Messages-API]
concepts_referenced: []
---

Aggregate Models API reference. Two endpoints:

- `GET /v1/models` (List) — returns paginated `data: array of ModelInfo`, ordered most-recent first; query params `after_id`, `before_id`, `limit` (default 20, max 1000); cursor-style pagination via `first_id` / `last_id` / `has_more`.
- `GET /v1/models/{model_id}` (Retrieve) — accepts a model ID or alias and returns the same `ModelInfo` shape; useful for resolving an alias (e.g. `claude-opus-4-7`) to its canonical ID.

Both endpoints accept the optional `anthropic-beta` header listing the beta flags supported across the API (24 enumerated values including `message-batches-2024-09-24`, `prompt-caching-2024-07-31`, `computer-use-2025-01-24`, `pdfs-2024-09-25`, `token-counting-2024-11-01`, `files-api-2025-04-14`, `mcp-client-2025-11-20`, `interleaved-thinking-2025-05-14`, `code-execution-2025-05-22`, `extended-cache-ttl-2025-04-11`, `context-1m-2025-08-07`, `context-management-2025-06-27`, `skills-2025-10-02`, `fast-mode-2026-02-01`, `output-300k-2026-03-24`, `user-profiles-2026-03-24`, `advisor-tool-2026-03-01`).

`ModelInfo` includes `id`, `display_name`, `created_at` (RFC 3339, may be epoch if unknown), `max_input_tokens`, `max_tokens` (max value for the request `max_tokens` parameter), `type:"model"`, and a rich `capabilities` object: `batch`, `citations`, `code_execution`, `image_input`, `pdf_input`, `structured_outputs`, `context_management` (with `clear_thinking_20251015`, `clear_tool_uses_20250919`, `compact_20260112` strategies), `effort` (low/medium/high/max/xhigh), and `thinking` (with `adaptive` and `enabled` types). Each capability is a `CapabilitySupport` object with a `supported: boolean`.

Auth: `X-Api-Key` header with `anthropic-version: 2023-06-01`. Models endpoints belong conceptually to the Messages stack (used for model discovery prior to a `messages.create` call). cURL examples are provided for both endpoints.
