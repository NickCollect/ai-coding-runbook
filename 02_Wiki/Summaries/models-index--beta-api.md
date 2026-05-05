---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/models.md
source_url: https://platform.claude.com/docs/en/api/beta/models
title: "Models (Beta)"
summarized_at: 2026-05-05
entities_referenced: [Messages-API]
concepts_referenced: [Extended-thinking, Adaptive-thinking, Effort]
---

Beta variant of the **Models** endpoint under `/v1/models`. The Models API surfaces which models are available to the calling org and reports each model's capability matrix (more recently released models are listed first).

**Endpoints on this page:**

- `GET /v1/models` — List available models (`after_id`, `before_id`, `limit` 1–1000 default 20).
- `GET /v1/models/{model_id}` — Retrieve a specific model or resolve a model alias.

**Domain types:** `BetaModelInfo` carries `id`, `display_name`, `created_at`, `max_input_tokens`, `max_tokens`, `type: "model"`, plus a `capabilities: BetaModelCapabilities` block:
- `batch`, `citations`, `code_execution`, `image_input`, `pdf_input`, `structured_outputs` — each a `BetaCapabilitySupport { supported }`.
- `context_management: BetaContextManagementCapability` — supports `clear_thinking_20251015`, `clear_tool_uses_20250919`, `compact_20260112` strategies.
- `effort: BetaEffortCapability` — supports `low`, `medium`, `high`, `max`, `xhigh` reasoning_effort levels.
- `thinking: BetaThinkingCapability` with `types: { adaptive, enabled }` — covers `Adaptive-thinking` (auto) and explicit-`enabled` configurations.

Use this endpoint to drive model pickers, validate that the requested model supports a feature (e.g. `batch.supported`, `pdf_input.supported`), or resolve aliases (e.g. `claude-opus-4-7`) to a canonical model ID. Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
