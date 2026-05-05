---
type: summary
source: 01_Raw/github/anthropics/anthropic-sdk-typescript/helpers.md
source_url: https://github.com/anthropics/anthropic-sdk-typescript/blob/main/helpers.md
title: "Anthropic SDK TypeScript — helpers.md (streaming, structured outputs, tools, MCP)"
summarized_at: 2026-05-05
entities_referenced: [Anthropic-SDK-TypeScript, Streaming-API, Structured-outputs, Tool-runner, MCP-server]
concepts_referenced: [Tool-use]
---

Higher-level helpers in the TypeScript SDK across four areas: streaming, structured outputs, tools, and MCP integration.

**Streaming.** `anthropic.messages.stream({ ... })` returns a `MessageStream` that emits events, has an async iterator, and exposes accumulator helpers. As a lower-memory alternative, `anthropic.messages.create({ stream: true, ... })` returns an async iterable of raw chunks without accumulating a Message. Cancel by `break`ing a `for await` loop or calling `stream.abort()`. Event handlers via `.on(...)`: `connect`, `streamEvent` (with running snapshot), `text` (delta + textSnapshot), `inputJson` (partialJson + jsonSnapshot), `message` (corresponds to `message_stop`), `contentBlock` (corresponds to `content_block_stop`), `finalMessage` (fired after `message`), `error` (`AnthropicError`), `abort` (`APIUserAbortError`), `end`. Methods/fields: `.abort()` (also aborts in-flight requests), `await .done()`, `.currentMessage`, `await .finalMessage()`, `await .finalText()`, `.messages` (mutable conversation array), `.controller` (underlying `AbortController`).

**Structured outputs.** `client.messages.parse({ ..., output_config: { format: ... } })` enforces JSON schema. Two helpers:

- `zodOutputFormat(zodObject)` — accepts a Zod schema; the response is parsed and validated with Zod. Result is typed and accessible via `message.parsed_output?.field`.
- `jsonSchemaOutputFormat(schema, options?)` — accepts a raw JSON Schema (`as const` for type inference). `options.transform: boolean` (default `true`) controls whether the schema is transformed for Claude compatibility.

Example files: `examples/structured-outputs-zod.ts`, `examples/structured-outputs-json-schema.ts`, `examples/structured-outputs-streaming.ts`, `examples/structured-outputs-raw.ts`.

**Tool helpers.** Helpers create runnable tools that `.toolRunner()` will auto-invoke. Two flavors:

- `betaZodTool({ name, inputSchema (Zod), description, run })` — runs the tool with Zod-validated input.
- A JSON-Schema variant (`betaTool` from `@anthropic-ai/sdk/helpers/beta/json-schema`) for non-Zod users.

Pass the tools into `anthropic.beta.messages.toolRunner({ model, max_tokens, messages, tools, max_iterations })`. The runner handles successive tool-call rounds and returns the final message when no more tool calls remain.

**MCP helpers.** Convert MCP types to Anthropic API types so MCP tools/prompts/resources can be wired into `messages.create` and `toolRunner` without boilerplate. The Claude API also accepts a top-level `mcp_servers` parameter for connecting Claude directly to remote MCP servers via URL (tool-only); use the helpers when you need local MCP servers, prompts/resources, or tighter connection control. Helpers parallel the Python SDK's `mcp_message`, `mcp_resource_to_content`, `mcp_resource_to_file`, etc., and integrate with `@modelcontextprotocol/sdk`'s `Client` for the MCP transport. Errors raised by conversion include the equivalent of Python's `UnsupportedMCPValueError` for unconvertible content types or unsupported MIME types.

The file is the canonical reference for ergonomic high-level usage of the TS SDK beyond the raw `messages.create` call.
