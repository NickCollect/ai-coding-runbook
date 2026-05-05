---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/models/retrieve.md
source_url: https://platform.claude.com/docs/en/api/beta/models/retrieve
title: "Retrieve Model (Beta)"
summarized_at: 2026-05-05
entities_referenced: [Messages-API]
concepts_referenced: []
---

`GET /v1/models/{model_id}` — fetch a single model or resolve a model alias to a canonical ID.

**Path param:** `model_id` (model identifier or alias). Returns a `BetaModelInfo` with full capability matrix (batch, citations, code_execution, context_management strategies, effort levels low/medium/high/max/xhigh, image_input, pdf_input, structured_outputs, thinking with adaptive/enabled types) plus `display_name`, `created_at`, `max_input_tokens`, `max_tokens`, `type: "model"`. Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
