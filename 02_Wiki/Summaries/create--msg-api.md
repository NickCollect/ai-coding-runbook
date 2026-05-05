---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/messages/create.md
source_url: https://platform.claude.com/docs/en/api/messages/create
title: "Create"
summarized_at: 2026-05-05
entities_referenced: [Messages-API, Tool-use, Prompt-caching, Extended-thinking, Streaming-API]
concepts_referenced: []
---

`POST /v1/messages` — primary chat completion endpoint. Sends a structured list of input messages (text or image content) and returns the next assistant message; supports single queries or stateless multi-turn conversations.

Body parameters:
- `max_tokens: number` — absolute output cap. `max_tokens: 0` is a documented hack to populate the prompt cache without generating a response (pre-warming).
- `messages: array of MessageParam` — alternating `user`/`assistant` turns. Consecutive same-role turns are merged. If the final message is `assistant`, the response continues from that turn (output prefilling). Hard limit of 100,000 messages per request.
- `model` — same enum as Completions (Opus/Sonnet/Haiku family + Mythos preview).
- Optional: `system`, `temperature`, `top_p`, `top_k`, `stop_sequences`, `stream`, `tools`/`tool_choice`, `metadata.user_id`, `service_tier`, `mcp_servers`, `thinking` config (Extended-thinking), `container`, `context_management`.

Content blocks (`ContentBlockParam` union): TextBlock (with optional `cache_control: {type:"ephemeral", ttl:"5m"|"1h"}` for Prompt-caching breakpoints; optional `citations` array), ImageBlock (base64 jpeg/png/gif/webp or URL), DocumentBlock (PDF, plain text, custom-content), ToolUseBlock / ToolResultBlock, ServerToolUseBlock, SearchResultBlock, ThinkingBlock / RedactedThinkingBlock.

Citations sub-types: `char_location`, `page_location`, `content_block_location`, `web_search_result_location`, `search_result_location`.

Header `anthropic-beta` accepts the 24-value enum (caching, computer-use, pdfs, token-counting, files, mcp-client, interleaved-thinking, code-execution, extended-cache-ttl, context-1m, context-management, model-context-window-exceeded, skills, fast-mode, output-300k, user-profiles, advisor-tool, etc.).

Response: `Message` object with `id`, `type:"message"`, `role:"assistant"`, `content` array of ContentBlocks, `model`, `stop_reason` (`end_turn`, `max_tokens`, `stop_sequence`, `tool_use`, etc.), `stop_sequence`, `usage` (input_tokens, output_tokens, cache_creation_input_tokens, cache_read_input_tokens, server_tool_use). When `stream:true`, returns SSE event stream (Streaming-API). Auth: `X-Api-Key` + `anthropic-version: 2023-06-01`.
