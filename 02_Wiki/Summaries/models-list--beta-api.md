---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/models/list.md
source_url: https://platform.claude.com/docs/en/api/beta/models/list
title: "List Models (Beta)"
summarized_at: 2026-05-05
entities_referenced: [Messages-API]
concepts_referenced: []
---

`GET /v1/models` — list available models, most-recently-released first.

**Query params:** `after_id`, `before_id` (cursor pagination), `limit` (default 20, range 1–1000).

**Returns:** `data: array of BetaModelInfo` plus `first_id`, `has_more`, `last_id`. Each `BetaModelInfo` includes `id`, `display_name`, `created_at`, `max_input_tokens`, `max_tokens`, `type: "model"`, and a `capabilities` block (batch, citations, code_execution, context_management, effort, image_input, pdf_input, structured_outputs, thinking). Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
