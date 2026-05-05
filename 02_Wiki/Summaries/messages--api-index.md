---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/messages.md
source_url: https://platform.claude.com/docs/en/api/messages
title: "Messages"
summarized_at: 2026-05-05
entities_referenced: [Messages-API, Batches-API, Token-counting, Streaming-API, Tool-use, Prompt-caching, Extended-thinking]
concepts_referenced: []
---

Aggregate API reference for the Messages stack. Wraps three top-level endpoint groups under one document: `## Create` (`POST /v1/messages`), `## Count Tokens` (`POST /v1/messages/count_tokens`), and the Batches sub-API rooted at `## Create` (`POST /v1/messages/batches`) plus its lifecycle operations (Retrieve, List, Cancel, Delete, Results).

The Create endpoint sends a structured list of input messages (text or image content) and returns the next assistant message; supports single queries or stateless multi-turn conversations. Body parameters include `max_tokens`, `messages` (alternating user/assistant turns, hard cap 100,000 messages), `model`, plus optional `system`, `temperature`, `top_p`, `top_k`, `stop_sequences`, `stream`, `tools`/`tool_choice`, `metadata`, `service_tier`, and beta features (cache_control breakpoints with 5m/1h TTL for Prompt-caching, citations, thinking config for Extended-thinking, mcp_servers).

Setting `max_tokens: 0` is documented as a way to pre-warm the prompt cache without generating output. Final `assistant`-role messages cause the response to continue from that turn (output prefilling).

Content blocks span text, image (base64 or URL), document/PDF, tool_use/tool_result, server_tool_use, search results, citations (char_location, page_location, content_block_location, web_search_result_location, search_result_location), and thinking blocks. The Tool-use surface includes both client tools (custom JSON-schema) and server-managed tools.

Header parameters carry `anthropic-version` and the `anthropic-beta` header (24+ beta flags enumerated, e.g. `message-batches-2024-09-24`, `prompt-caching-2024-07-31`, `extended-cache-ttl-2025-04-11`, `interleaved-thinking-2025-05-14`, `context-1m-2025-08-07`, `context-management-2025-06-27`, `skills-2025-10-02`, `fast-mode-2026-02-01`, `output-300k-2026-03-24`).

Response shape: `Message` with `id`, `type:"message"`, `role:"assistant"`, `content` array, `model`, `stop_reason`, `stop_sequence`, `usage` (input/output tokens, cache read/creation, server_tool_use). Auth uses `X-Api-Key`. Rate limits visible via the Admin Rate-limit-API per model_group/batch/token_count/files/skills/web_search categories.
