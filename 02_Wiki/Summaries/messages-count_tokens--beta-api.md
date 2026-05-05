---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/messages/count_tokens.md
source_url: https://platform.claude.com/docs/en/api/beta/messages/count_tokens
title: "Count Tokens (Beta)"
summarized_at: 2026-05-05
entities_referenced: [Messages-API, Token-counting, Tool-use, MCP-server]
concepts_referenced: [Extended-thinking, Prompt-caching]
---

`POST /v1/messages/count_tokens` — token-counting dry-run that does **not** consume model inference, useful for budget/cache estimation.

**Required body params:** `messages` (`array of BetaMessageParam`), `model`.

**Optional body params (subset of Create):** `system`, `tools` (full union of beta tools — `BetaTool`, `BetaToolBash20241022`, `BetaToolBash20250124`, plus 20+ more dated server-tool variants), `tool_choice`, `mcp_servers`, `cache_control`, `context_management`, `output_config`, `output_format`, `speed`, `thinking`. Notably **omits** `max_tokens`, `temperature`, `top_k`, `top_p`, `stop_sequences`, `stream`, `metadata`, `user_profile_id`, `service_tier`, `container`, `inference_geo` — those are inference-only knobs.

Returns the input token count for the supplied request shape. Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
