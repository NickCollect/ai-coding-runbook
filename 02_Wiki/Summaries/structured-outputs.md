---
type: summary
source: 01_Raw/code.claude.com/docs/en/agent-sdk/structured-outputs.md
source_url: https://code.claude.com/docs/en/agent-sdk/structured-outputs
title: "Get structured output from agents"
summarized_at: 2026-05-05
entities_referenced: [Agent-SDK]
concepts_referenced: []
---

Pass a JSON Schema to the Agent SDK and the agent returns validated JSON matching that shape after multi-turn tool use. Set `outputFormat` (TS) / `output_format` (Python) to `{type: "json_schema", schema}`. Read `result.structured_output` from the result message; check `result.subtype` to detect failure.

Behavior:
- Agent uses any tools it needs to gather data, then produces JSON conforming to the schema.
- SDK validates output against the schema; on mismatch, re-prompts up to a retry limit.
- If retry limit exhausted: `subtype = "error_max_structured_output_retries"`, no `structured_output`.
- On success: `subtype = "success"`, `structured_output` is a typed object.

Type-safe schema authoring:
- TypeScript: define with **Zod**, convert via `z.toJSONSchema(MySchema)`, parse return with `MySchema.safeParse(...)` for full type inference.
- Python: define with **Pydantic** `BaseModel`, convert via `MyModel.model_json_schema()`, parse with `MyModel.model_validate(...)` for type hints.

Supported JSON Schema features: object/array/string/number/boolean/null, `enum`, `const`, `required`, nested objects, `$ref`. Limitations documented at platform.claude.com.

Use cases:
- Recipe extractor (string/number fields, ingredient list).
- Feature plan generator (steps array with `enum` complexity).
- TODO tracker — agent uses Grep + Bash (git blame), returns array of `{text, file, line, author?, date?}` plus `total_count`.

Tips for success:
- Keep schemas focused; avoid deep nesting + many required fields.
- Mark fields optional if the underlying data may be absent.
- Use clear, unambiguous prompts.

Distinction from API-level structured outputs: the SDK version supports multi-turn tool use before producing the final JSON; the platform structured outputs feature is single-turn.
