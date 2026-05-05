---
type: summary
source: 01_Raw/platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools.md
source_url: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools
title: "Define tools"
summarized_at: 2026-05-05
entities_referenced: [Tool-use, Structured-outputs, Prompt-caching, Tool-search-tool-API]
concepts_referenced: [Extended-thinking]
---

How to specify tool schemas, write effective descriptions, and control when Claude calls your tools.

**Model selection.** Use the latest Opus (4.7) for complex tools and ambiguous queries—it handles multiple tools better and seeks clarification. Haiku models are fine for straightforward tools but may infer missing parameters rather than asking.

**Tool definition shape.** Each entry in the top-level `tools` parameter has:
- `name`: matches `^[a-zA-Z0-9_-]{1,64}$`.
- `description`: detailed plaintext explaining what the tool does, when to use it, and how it behaves.
- `input_schema`: a JSON Schema object defining expected parameters.
- `input_examples` (optional): array of example input objects.

Optional properties (`cache_control`, `strict`, `defer_loading`, `allowed_callers`) live in the Tool reference.

**Tool-use system prompt.** When `tools` is provided, the API automatically constructs a system prompt that wraps the tool definitions in JSON Schema with formatting instructions, then appends the user-provided system prompt and tool configuration. Token overhead is documented per model.

**Best practices for descriptions.** *Most important factor in tool performance.* Aim for 3–4+ sentences covering: what the tool does, when (and when NOT) to use it, what each parameter means and how it affects behavior, important caveats and limitations. The doc contrasts a "good" `get_stock_price` description (explains what's returned, what `ticker` means, what isn't returned) vs. a "bad" one ("Gets the stock price for a ticker.") that leaves Claude guessing.

Other guidance: *prioritize descriptions* but use `input_examples` for complex/format-sensitive inputs; *consolidate related operations* into fewer tools with an `action` parameter (e.g., one tool with create/review/merge actions instead of three separate tools)—fewer, more capable tools reduce ambiguity; *use meaningful namespacing* in tool names when spanning services (`github_list_prs`, `slack_send_message`)—especially important with the [[Tool-search-tool-API]]; *design responses to return only high-signal information*—stable IDs (slugs/UUIDs) over opaque references; only fields Claude needs.

**`input_examples`.** Optional array of valid example inputs that gets included in the prompt to show concrete patterns. Useful for nested objects, optional parameters, format-sensitive inputs. Each example must be valid against the `input_schema`; invalid examples return 400 errors. Not supported on server-side tools (web search, code execution). Token cost: ~20–50 for simple examples, ~100–200 for complex nested ones.

**Controlling output via `tool_choice`.** Four options:
- `auto`: Claude decides (default when `tools` provided).
- `any`: must use one of the provided tools.
- `tool`: forces a specific named tool (`{"type": "tool", "name": "get_weather"}`).
- `none`: prevents tool use (default when no tools provided).

When `tool_choice` is `any` or `tool`, the API prefills the assistant message to force a tool call—**no natural-language preamble** even if asked. To get explanation + a tool call, use `auto` and prompt explicitly ("Use the `get_weather` tool in your response.").

**Constraints.** Changes to `tool_choice` invalidate cached message blocks under [[Prompt-caching]]; tool definitions and system prompts stay cached but messages reprocess. With [[Extended-thinking]], only `auto` and `none` are supported—`any`/`tool` return errors. Claude Mythos Preview also doesn't support forced tool use.

**Combining with strict.** `tool_choice: {"type": "any"}` plus [[Structured-outputs]]'s `strict: true` on tool definitions guarantees both that a tool will be called AND that inputs strictly match the schema (no missing params, no type mismatches).

**Model behavior.** Claude commonly emits a natural preamble ("I'll help you check the current weather and time in San Francisco.") before the `tool_use` block. Code should treat preamble text like any assistant text and not depend on specific phrasing.

Linked deeper guidance: anthropic.com/engineering/writing-tools-for-agents (consolidation, naming, response shaping). Next steps: Handle tool calls (parse `tool_use`, format `tool_result`), Tool Runner (SDK abstraction), Tool reference (directory).
