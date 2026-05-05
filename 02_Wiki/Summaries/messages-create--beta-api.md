---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/messages/create.md
source_url: https://platform.claude.com/docs/en/api/beta/messages/create
title: "Create Message (Beta)"
summarized_at: 2026-05-05
entities_referenced: [Messages-API, Tool-use, MCP-server, User-profile]
concepts_referenced: [Extended-thinking, Prompt-caching, Streaming-API, Context-window]
---

`POST /v1/messages` — primary inference call, beta variant.

**Required body params:** `model`, `max_tokens`, `messages` (`array of BetaMessageParam`).

**Optional body params:**
- Sampling: `temperature`, `top_k`, `top_p`, `stop_sequences`.
- Output: `stream` (boolean for SSE), `system` (string or array of `BetaTextBlockParam`), `metadata`, `output_config` (`BetaOutputConfig`), `output_format` (`BetaJSONOutputFormat`).
- Caching: `cache_control` (`BetaCacheControlEphemeral`).
- Context: `context_management` (`BetaContextManagementConfig`).
- Inference routing/perf: `service_tier` (`auto` | `standard_only`), `speed` (`standard` | `fast`), `inference_geo`.
- Tools: `tools` (array of `BetaToolUnion` covering custom tools, server tools like bash/text-editor/computer/code-execution/web-search/web-fetch/memory/tool-search/advisor at various dated versions), `tool_choice` (`BetaToolChoice`).
- MCP: `mcp_servers` (array of `BetaRequestMCPServerURLDefinition` for the MCP-client beta).
- Thinking: `thinking` (`BetaThinkingConfigParam` — enabled or adaptive).
- Container: `container` (`BetaContainerParams` or container ID string).
- End-user: `user_profile_id` (binds the call to a previously-created `User-profile`).

Returns a `BetaMessage` (when not streaming) or an SSE stream of message events.

Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
