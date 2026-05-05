---
type: summary
source: 01_Raw/platform.claude.com/docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming.md
source_url: https://platform.claude.com/docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming
title: "Fine-grained tool streaming"
summarized_at: 2026-05-05
entities_referenced: [Tool-use, Streaming-API]
concepts_referenced: []
---

Fine-grained tool streaming streams tool-use parameter values **without buffering or JSON validation**, reducing latency to begin receiving large parameters. Generally available on all models and all platforms (Claude API, Amazon Bedrock, Google Vertex AI, Microsoft Foundry). **ZDR-eligible.**

> "When using fine-grained tool streaming, you may potentially receive invalid or partial JSON inputs. Make sure to account for these edge cases in your code."

**Enabling.** Set `eager_input_streaming: true` on a user-defined tool definition AND enable [[Streaming-API]] (`"stream": true` or use SDK stream methods). The flag is per-tool—you can mix eager and non-eager tools in the same request.

**Behavior difference.** Without fine-grained streaming, chunks arrive in many small JSON-validating fragments (`'{"'`, `'query": "Ty'`, `'peScri'`, ...) over ~15s. With fine-grained streaming, the same content arrives in fewer, longer chunks (`'{"query": "TypeScript 5.0 5.1 5.2 5.3'`, `' new features comparison'`) over ~3s. Useful when the model emits a long parameter (a poem, a long file body) where buffering for JSON validation is the latency bottleneck.

**Risk.** Because parameters are sent without buffering or JSON validation, the resulting stream is not guaranteed to be valid JSON. Particularly: if `stop_reason: "max_tokens"` is hit, the stream may end mid-parameter and leave incomplete JSON. Specific handling for the `max_tokens` case is recommended.

**Accumulating tool input deltas.** When a `tool_use` content block streams, the initial `content_block_start` event contains `input: {}` (empty placeholder object). The actual input arrives as a series of `input_json_delta` events, each carrying a `partial_json` string fragment. Concatenate the fragments and parse on `content_block_stop`. The contract:

1. On `content_block_start` with `type: "tool_use"`, initialize `input_json = ""`.
2. For each `content_block_delta` with `type: "input_json_delta"`, do `input_json += event.delta.partial_json`.
3. On `content_block_stop`, parse: `json.loads(input_json)`.

The type mismatch between the initial `input: {}` (object) and the `partial_json` string fragments is intentional—the empty object marks the slot in the content array; the deltas build the real value.

**SDK helpers.** Python and TypeScript SDKs offer higher-level helpers (`stream.get_final_message()`, `stream.finalMessage()`) that perform accumulation automatically. Use the manual pattern only when you need to react to partial input *before* the block closes—e.g., rendering a progress indicator, starting a downstream request early, or streaming a long generated file to disk as it arrives.

**Handling invalid JSON in tool results.** If you receive invalid/incomplete JSON from the model and need to pass it back as an error response, wrap it in a JSON object with a clear key like `{"INVALID_JSON": "<your invalid json string>"}`. This signals to the model that the content is malformed while preserving the original data for debugging. Properly escape any quotes and special characters in the wrapped string.

**Examples shown.** A `make_file` tool with a `lines_of_text` array parameter for "Can you write a long poem and make a file called poem.txt?"—Claude streams each line as it's generated rather than buffering the entire poem before emitting the tool call. A `get_weather` tool with a `city` string parameter showing the manual delta-accumulation pattern in Python and TypeScript.

**Why it matters.** For latency-sensitive applications (live UIs, progressive file generation, downstream pipelines that benefit from early bytes), fine-grained streaming can cut perceived latency dramatically when parameters are long. Trade-off: your code must handle malformed/incomplete JSON robustly.
