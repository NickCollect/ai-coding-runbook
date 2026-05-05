---
type: summary
source: 01_Raw/platform.claude.com/docs/en/build-with-claude/streaming.md
source_url: https://platform.claude.com/docs/en/build-with-claude/streaming
title: "Streaming Messages"
summarized_at: 2026-05-05
entities_referenced: [Streaming-API, Messages-API, Anthropic-SDK-Python, Anthropic-SDK-TypeScript]
concepts_referenced: []
---

Set `"stream": true` on a Messages create call to incrementally receive the response via **Server-Sent Events (SSE)**.

## SDK helpers

- **Python SDK** — sync + async streams. Idiom: `with client.messages.stream(...) as stream: for text in stream.text_stream: ...`. Also `stream.get_final_message()` to accumulate into a complete `Message` (useful for large `max_tokens` requests where SDKs require streaming to avoid HTTP timeouts).
- **TypeScript SDK** — `.stream(...).on("text", cb)`, `await stream.finalMessage()`.
- **PHP SDK** — `createStream()`.
- All major SDKs (Go, Java, C#, Ruby) expose streaming primitives.
- CLI: `ant messages create --stream --format jsonl`.

## Why use streaming

- Show response progressively to users (latency-sensitive UX).
- Required for large `max_tokens` requests via SDK to avoid HTTP timeouts (Opus 4.7 supports up to 128k with streaming; non-streaming practical ceiling is 64k).

## Event types (high-level)

The full event sequence (covered later in raw doc) includes:
- `message_start` (initial Message metadata; `stop_reason` is `null`)
- `content_block_start` (per block)
- `content_block_delta` (deltas: `text_delta`, `thinking_delta`, `signature_delta`, `input_json_delta`)
- `content_block_stop` (per block)
- `message_delta` (carries final `stop_reason`, `usage` updates)
- `message_stop`

## Notes

- Get the complete final message without manual event handling: use SDK helpers (`get_final_message()` / `finalMessage()` / accumulator pattern).
- For `stop_reason` semantics during streaming, see [handling-stop-reasons].
