---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/messages.md
source_url: https://platform.claude.com/docs/en/api/beta/messages
title: "Messages (Beta)"
summarized_at: 2026-05-05
entities_referenced: [Messages-API, Batches-API, Token-counting, Tool-use, MCP-server]
concepts_referenced: [Extended-thinking, Prompt-caching, Streaming-API, Context-window]
---

Beta variant of the **Messages** API under `/v1/messages`, plus its `count_tokens` companion and the full Batches sub-resource. This is the primary chat-completion entry point with all current beta features (caching, MCP, thinking, output formats, fast mode, user-profile binding) exposed.

**Messages endpoints on this page:**

- `POST /v1/messages` — Create message (full inference call).
- `POST /v1/messages/count_tokens` — Token-counting dry-run (no inference, returns token estimate).

**Batches sub-resource (`/v1/messages/batches`):**
- `POST .../batches` — Create batch (`requests: array of { custom_id, params }`).
- `GET .../batches/{message_batch_id}` — Retrieve batch status.
- `GET .../batches` — List batches.
- `POST .../batches/{message_batch_id}/cancel` — Cancel.
- `DELETE .../batches/{message_batch_id}` — Delete.
- `GET .../batches/{message_batch_id}/results` — Stream results.

**Key request fields on `POST /v1/messages`:** required `model`, `max_tokens`, `messages`; optional `system`, `temperature`, `top_k`, `top_p`, `stop_sequences`, `stream`, `tools`, `tool_choice`, `metadata`, `service_tier` (`auto` | `standard_only`), `speed` (`standard` | `fast`), `thinking` (`BetaThinkingConfigParam`), `cache_control` (`BetaCacheControlEphemeral` for prompt caching), `context_management` (`BetaContextManagementConfig`), `mcp_servers`, `container`, `inference_geo`, `output_config`, `output_format` (`BetaJSONOutputFormat`), and `user_profile_id` (links the call to a `User-profile`).

`count_tokens` accepts the same shape minus inference-only knobs (no `max_tokens`, `temperature`, `stream`, etc.) and returns a token count.

Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies. The set of beta tokens this stack honors covers `prompt-caching-2024-07-31`, `mcp-client-2025-11-20`, `interleaved-thinking-2025-05-14`, `context-management-2025-06-27`, `context-1m-2025-08-07`, `output-300k-2026-03-24`, `fast-mode-2026-02-01`, `user-profiles-2026-03-24`, `skills-2025-10-02`, and others.
