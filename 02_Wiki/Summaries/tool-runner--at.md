---
type: summary
source: 01_Raw/platform.claude.com/docs/en/agents-and-tools/tool-use/tool-runner.md
source_url: https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-runner
title: "Tool Runner (SDK)"
summarized_at: 2026-05-05
entities_referenced: [Tool-runner, Tool-use, Compaction, Prompt-caching, Streaming-API, Anthropic-SDK-Python, Anthropic-SDK-TypeScript]
concepts_referenced: [Agentic-loop]
---

The [[Tool-runner]] is the SDK abstraction that handles the [[Agentic-loop]], error wrapping, and type safety automatically. Available in beta in Python, TypeScript, and Ruby SDKs. Use it for most tool-use implementations; use the manual loop only when you need human-in-the-loop approval, custom logging, or conditional execution.

The runner automatically: executes tools when Claude calls them, handles the request/response cycle, manages conversation state, provides type safety + validation. Supports automatic [[Compaction]]—generates summaries when token usage exceeds a threshold, allowing long-running agentic tasks to continue beyond context-window limits.

**Defining tools.**

- *Python*: `@beta_tool` decorator (or `@beta_async_tool` for async clients) inspects function arguments + docstring to extract a JSON Schema. Type hints become parameter types; docstring becomes the description; Args sections become per-parameter descriptions. Auto-adds `additionalProperties: false`. [[Anthropic-SDK-Python]].

- *TypeScript*: two approaches—`betaZodTool({name, description, inputSchema: z.object({...}), run: async (input) => ...})` (recommended; type-safe with Zod 3.25.0+; runtime validation) or `betaTool()` for JSON Schema without Zod (no runtime validation, validate inside `run`). [[Anthropic-SDK-TypeScript]].

- *Ruby*: subclass `Anthropic::BaseTool` with `doc "..."` + `input_schema MyInputClass` (which subclasses `Anthropic::BaseModel`).

Tool functions must return a content block or content block array (text, images, documents). Strings auto-convert to text content blocks. Structured JSON: encode to a string before returning. Numbers/booleans must be stringified.

**Iterating.** The runner is iterable, yielding messages from Claude. Each iteration: check if Claude requested a tool use; if so, run the tool, send result back, yield next message. Loops until Claude returns a message without tool use; you can `break` early.

For final-message-only:
- Python: `runner.until_done()`.
- TypeScript: `await runner` directly.
- Ruby: `runner.run_until_finished`.

**Advanced controls (within the loop).**
- `generate_tool_call_response()` / `generateToolResponse()`: optionally inspect the auto-appended tool result for logging or debugging.
- `set_messages_params(...)` / `setMessagesParams(...)`: customize the next API call's parameters (e.g., bump `max_tokens`).
- `append_messages(...)` / `pushMessages(...)`: inject extra messages between turns.
- Ruby: `next_message`, `feed_messages`, `params`.

**Debugging.** Tool exceptions are caught and returned to Claude as `tool_result` with `is_error: true`. Only the message is included by default. Set `ANTHROPIC_LOG=info` (or `=debug`) to log full stack traces via Python's `logging`, TypeScript's console, or Ruby's logger.

**Intercepting errors.** Iterate over the runner; check if `tool_response.content` blocks have `is_error`. Two options: raise/throw to stop the loop, or log and continue (let Claude handle it).

**Modifying tool results.** Useful for adding `cache_control: {"type": "ephemeral"}` to enable [[Prompt-caching]] on large tool outputs (e.g., document search results) for subsequent API calls. Python: re-append the modified `tool_response` via `runner.append_messages(message, tool_response)` to prevent auto-append of the original. TypeScript: mutate in place (the runner auto-appends the mutated response). Ruby: mutate `runner.params[:messages].last` blocks in place.

**Streaming.** Set `stream=true`; runner returns stream objects per iteration. Iterate events for incremental output; call `get_final_message()` / `finalMessage()` for the accumulated message. Supports the [[Streaming-API]] event types (text events, input_json events, etc.). Ruby uses `runner.each_streaming` with case-matching on `Anthropic::Streaming::TextEvent` / `InputJsonEvent`.

The doc's basic example: `get_weather` + `calculate_sum` tools; user asks "What's the weather like in Paris? Also, what's 15 + 27?"; runner handles both tool calls in one parallel turn, returns the final synthesized answer. With manual control, the same flow takes ~30 lines of agentic-loop code; with `tool_runner`, ~15 lines including tool definitions.
