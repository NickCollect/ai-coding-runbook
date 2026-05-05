---
type: summary
source: 01_Raw/platform.claude.com/docs/en/agents-and-tools/tool-use/troubleshooting-tool-use.md
source_url: https://platform.claude.com/docs/en/agents-and-tools/tool-use/troubleshooting-tool-use
title: "Troubleshooting tool use"
summarized_at: 2026-05-05
entities_referenced: [Tool-use, Structured-outputs, Tool-search-tool-API, Prompt-caching]
concepts_referenced: []
---

Symptom-to-fix tables for the most common tool-use errors.

**Claude calls the wrong tool.**
- *Calls A when you wanted B*: description ambiguity—differentiate tools by **WHEN to use them**, not only WHAT they do.
- *Never calls your tool*: tool name collision or overly-generic schema. Check for duplicates; add `input_examples` to make intended use concrete.
- *Wrong parameter types*: model guessing at ambiguous schema. Add `strict: true` (if your schema is in the [[Structured-outputs]] supported subset) or add `input_examples`.

**Claude invents tool parameters.**
- *Parameter that doesn't exist*: model over-generation without strict mode. Add `strict: true`.
- *Parameter values outside your enum*: missing strict mode or too-large enum. Shrink the enum or add `input_examples` showing valid choices.

**Parallel tool calls don't work.**
- *Sequential when parallel would be better*: message-history formatting bug. Send multiple `tool_result` blocks in **ONE user message**, not one per turn.
- *`disable_parallel_tool_use` ignored*: set too late. Must be set on the request that returns `tool_use`; setting it on a later request has no effect.

**Cache keeps invalidating ([[Prompt-caching]]).**
- *Every request is a cache miss*: `tool_choice` varying between requests. Keep `tool_choice` stable, or place the `cache_control` breakpoint **before** the variation point.
- *Adding a tool mid-conversation breaks cache*: tool prepended to the array head. Use `defer_loading: true` with [[Tool-search-tool-API]] to append the tool inline instead of modifying the array head.

**Errors at request time.**
- `"tool_use ids were found without tool_result blocks immediately after"`: missing `tool_result` for some `tool_use` ids, or `tool_result` is not the first content block in the user message. Return one `tool_result` for every `tool_use` block; put `tool_result` blocks before any text.
- `"Input schema is not compatible with strict mode: string patterns are not supported"`: using `pattern` with `strict: true`. Remove the pattern or drop strict—`pattern` is not in the supported JSON Schema subset yet.
- `"All tools have defer_loading: true"`: no tools visible to the model. At least one tool must be immediately loaded; the tool search tool itself must never have `defer_loading: true`.

**JSON escaping differences (Opus 4.6+).** Unicode and forward-slash escaping differs between model versions. *Symptom:* string comparison on tool inputs fails with newer models. *Fix:* parse with `json.loads()` or `JSON.parse()`—**never do raw string matching on serialized input**.
