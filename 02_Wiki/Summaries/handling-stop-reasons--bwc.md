---
type: summary
source: 01_Raw/platform.claude.com/docs/en/build-with-claude/handling-stop-reasons.md
source_url: https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons
title: "Handling stop reasons"
summarized_at: 2026-05-05
entities_referenced: [Messages-API, Streaming-API, Tool-runner, Web-search-tool, Web-fetch-tool]
concepts_referenced: [Tool-use, Context-window]
---

Every successful Messages API response includes a `stop_reason` field explaining why generation ended. Distinct from HTTP errors. Robust apps must branch on it.

## Values

| Value | Meaning |
|---|---|
| `end_turn` | Most common — Claude finished naturally |
| `max_tokens` | Hit the request's `max_tokens` cap |
| `stop_sequence` | One of your `stop_sequences` matched (`response.stop_sequence` set) |
| `tool_use` | Claude is calling a tool; execute and return `tool_result` |
| `pause_turn` | Server-side sampling loop hit iteration limit (default 10) for server tools (web search/fetch). Send response back as-is to continue. |
| `refusal` | Refused for safety. Try Haiku 4.5 if frequent on Sonnet 4.5 / Opus 4.1 (different restrictions). |
| `model_context_window_exceeded` | Hit context window cap. Default in Sonnet 4.5+. For older models, beta header `model-context-window-exceeded-2025-08-26`. |

## Empty responses with `end_turn`

If Claude returns 2-3 tokens with no content and `end_turn`, common causes:
1. **Adding text blocks immediately after `tool_result`** — teaches Claude to expect user input after every tool use. Don't.
2. Re-sending Claude's completed response unchanged — Claude's already done.

**Fix:** send `tool_result` blocks **alone** (no extra text). If still empty, append a NEW `{role: "user", content: "Please continue"}` message — never just retry the empty assistant turn.

## Truncated tool use (`max_tokens` mid-tool)

If `stop_reason == "max_tokens"` and last block is incomplete `tool_use`, retry with higher `max_tokens` (e.g., 1024 → 4096).

## `pause_turn` pattern (server tools)

```python
while response.stop_reason == "pause_turn":
    messages = [
      {"role": "user", "content": original_query},
      {"role": "assistant", "content": response.content}
    ]
    response = client.messages.create(model="...", messages=messages, tools=tools)
```

## Streaming

`stop_reason` is:
- `null` in `message_start`
- Set in `message_delta` event
- Not in any other events

## Stop reasons vs errors

- **Stop reasons:** in response body, valid content, normal completion.
- **Errors:** HTTP 4xx/5xx, no valid content, request failed (catch via SDK exception, e.g., `anthropic.APIError`).

## Best practices

1. Always branch on `stop_reason`.
2. Handle `max_tokens` and `model_context_window_exceeded` separately (option to warn user vs continue).
3. Implement `pause_turn` continuation loop in any agent loop with server tools.
4. For tool use, prefer the `tool_runner` over manual loop.
