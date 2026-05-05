---
type: summary
source: 01_Raw/platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use.md
source_url: https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use
title: "Strict tool use"
summarized_at: 2026-05-05
entities_referenced: [Tool-use, Structured-outputs]
concepts_referenced: []
---

Setting `strict: true` on a tool definition uses **grammar-constrained sampling** to guarantee Claude's tool inputs match your JSON Schema. Same pipeline as [[Structured-outputs]]. Use when you need to validate tool parameters, build agentic workflows, ensure type-safe function calls, or handle complex tools with nested properties.

**Why it matters for agents.** Without strict mode, Claude might return incompatible types (`"2"` instead of `2`) or omit required fields—breaking your functions and causing runtime errors. With strict mode, functions receive correctly-typed arguments every time; no validate-and-retry needed. Concrete example: a booking system needs `passengers: int`. Without strict, Claude might emit `passengers: "two"` or `passengers: "2"`. With `strict: true`, the response always contains `passengers: 2`.

**Enabling.** Add `"strict": true` as a top-level property in the tool definition alongside `name`, `description`, `input_schema`. Schema must use the supported JSON Schema subset (see Structured outputs JSON Schema limitations doc). Typical pattern: include `additionalProperties: false` to lock down the shape.

```json
{
  "name": "get_weather",
  "description": "Get the current weather in a given location",
  "strict": true,
  "input_schema": {
    "type": "object",
    "properties": {
      "location": {"type": "string", "description": "..."},
      "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
    },
    "required": ["location"],
    "additionalProperties": false
  }
}
```

**Guarantees.** Tool `input` strictly follows `input_schema`; tool `name` is always valid (from provided tools or server tools).

**Use cases shown.**
- *Validated tool inputs*: a `search_flights` tool with `passengers: integer enum [1..10]`, `departure_date: string format date`. Output guaranteed to be a valid integer in range and a valid date string.
- *Agentic workflow with multiple validated tools*: trip planner with `search_flights` + `search_hotels`, each `strict: true`, each with `additionalProperties: false`. All multi-step tool calls have guaranteed type safety.

**Combine with `tool_choice` for guaranteed agent steps.** Pair `strict: true` with `tool_choice: {"type": "any"}` to guarantee both that one of your tools will be called AND that the inputs strictly match the schema—eliminating both missing parameters and type mismatches in a single mechanism.

**Data retention.** Strict tool use compiles tool `input_schema` definitions into grammars using the same pipeline as [[Structured-outputs]]. Tool schemas are temporarily cached for **up to 24 hours since last use**. Prompts and responses are not retained beyond the API response.

**HIPAA caveat.** Strict tool use is HIPAA-eligible, but **PHI must NOT be included in tool schema definitions**. The API caches compiled schemas separately from message content, and these cached schemas do not receive the same PHI protections as prompts and responses. Specifically, do not include PHI in:
- `input_schema` property names
- `enum` values
- `const` values
- `pattern` regular expressions

PHI should only appear in message content (prompts and responses), where it is protected under HIPAA safeguards.

**Quick start examples.** Provided in cURL, ant CLI, Python, TypeScript, C#, Go, Java, PHP, Ruby. All show the same pattern: add `strict: true` and `additionalProperties: false` to the tool definition, send the request, receive a `tool_use` block with guaranteed schema-conforming `input`.
