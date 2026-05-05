---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/messages/count_tokens.md
source_url: https://platform.claude.com/docs/en/api/messages/count_tokens
title: "Count Tokens"
summarized_at: 2026-05-05
entities_referenced: [Messages-API, Token-counting]
concepts_referenced: []
---

`POST /v1/messages/count_tokens` — counts the tokens that a hypothetical Messages API request would consume, **without** creating the message or charging for inference. Designed for cost estimation, pre-flight context budgeting, and prompt sizing.

Body parameters mirror a real `messages.create` request: `messages` (alternating user/assistant turns, same `MessageParam` shape with text/image/document/tool_use/tool_result content blocks, including PDFs and tools), plus optional `model`, `system`, `tools`, `tool_choice`, `mcp_servers`, `thinking`, `context_management`. The endpoint accepts the same 24 `anthropic-beta` flags as the Create endpoint, since beta features (PDFs, prompt caching, extended thinking, computer use, MCP, files) can change the token count.

Same 100,000-message-per-request hard cap. Image content can be Base64 (jpeg/png/gif/webp) or URL. Document content can be base64-encoded PDF, plain text, or custom content blocks.

Returns a small object: `input_tokens: number` — total tokens that would be billed as input for the request. No output count (the response is not generated).

Auth: `X-Api-Key` + `anthropic-version: 2023-06-01`. Useful before sending large prompts or batched requests, or before triggering Prompt-caching breakpoints (since cache writes/reads cost different rates per token). Linked from the Build-with-Claude token-counting guide.
