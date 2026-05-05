---
type: summary
source: 01_Raw/platform.claude.com/docs/en/build-with-claude/extended-thinking.md
source_url: https://platform.claude.com/docs/en/build-with-claude/extended-thinking
title: "Building with extended thinking"
summarized_at: 2026-05-05
entities_referenced: [Extended-thinking, Adaptive-thinking, Effort, Messages-API, Streaming-API, Prompt-caching, Tool-use, Context-editing, Enterprise-gateway]
concepts_referenced: [Tool-use, Context-window]
---

Extended thinking gives Claude enhanced reasoning by emitting `thinking` content blocks (with internal step-by-step reasoning) before the final `text` response. ZDR-eligible.

## Mode availability

- **Opus 4.7 and later:** manual `thinking: {type: "enabled", budget_tokens: N}` is **rejected (400)**. Use [adaptive thinking] + [effort] instead.
- **Mythos Preview:** adaptive is default; manual `enabled` also accepted; `disabled` not supported; `display` defaults to `"omitted"`.
- **Opus 4.6 / Sonnet 4.6:** adaptive recommended; manual `enabled` deprecated but still functional. Sonnet 4.6 supports interleaved (deprecated path).
- **Older models (Sonnet 3.7, etc.):** manual mode only.

## Manual config (deprecated paths)

```json
{
  "thinking": {"type": "enabled", "budget_tokens": 10000},
  "max_tokens": 16000
}
```

`budget_tokens` is a subset of `max_tokens`; thinking tokens count as output tokens and are billed.

## Response shape

```json
{"content": [
  {"type": "thinking", "thinking": "...", "signature": "..."},
  {"type": "text", "text": "..."}
]}
```

## Key behaviors

- **Summarized thinking:** Claude 4 models return summary of full reasoning. Billed for full thinking tokens, not summary. Visible token count won't match billed count. Different model produces summary; thinking model doesn't see it.
- **`display` field:** `"summarized"` (default Opus 4.6/Sonnet 4.6, earlier Claude 4) | `"omitted"` (default Opus 4.7 and Mythos; faster TTFT for streaming, signature still returned).
- **Encryption / signature:** opaque; cryptographically verifies thinking blocks. Identical across `summarized`/`omitted`. Compatible across Anthropic, Bedrock, Vertex.
- For Sonnet 3.7: returns FULL thinking output (not summarized).

## Interleaved thinking

Claude can think between tool calls. Sonnet 4.6 manual mode requires `interleaved-thinking-2025-05-14` beta header. Adaptive mode auto-enables on Mythos / Opus 4.7 / Opus 4.6 / Sonnet 4.6. Opus 4.6 manual mode does NOT support interleaved.

## With tool use

- Pass thinking blocks back **unchanged** with corresponding `tool_result` (only required case). Modifying breaks signature → API error.
- Opus 4.5+ and Sonnet 4.6+ keep all thinking blocks in context by default; earlier Opus/Sonnet and all Haiku strip them. Use context editing to override.
- `tool_choice` limitations apply when thinking is active.

## Streaming

Thinking blocks stream via `thinking_delta` events; signature added via `signature_delta` just before `content_block_stop`.

## Pricing notes

- Billed for full original thinking tokens (input prior turns retained per model rules).
- Cache writes/hits: see prompt-caching interaction.
- A specialized system prompt is auto-included when thinking is enabled.

## Differences across model versions

API shape unchanged across Sonnet 3.7 → Claude 4. Behavior differs (summarization, defaults, interleaved support, etc.). See model-specific notes.
