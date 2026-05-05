---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/structured-output.md
source_url: https://ai.google.dev/gemini-api/docs/structured-output
title: "Gemini API — Structured Output"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Gemini API Structured Output

Source is in Italian (crawler localization).

## Overview

Configure Gemini models to generate responses that conform to a JSON schema. Ensures predictable, type-safe outputs. Simplifies extracting structured data from unstructured text.

## Use Cases

- **Data extraction**: Extract names, dates, entities from text
- **Structured classification**: Classify text into predefined categories
- **Agentic workflows**: Generate structured inputs for tools/APIs

## Configuration

Set `response_mime_type` to `"application/json"` and provide `response_json_schema`.

```python
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=prompt,
    config={
        "response_mime_type": "application/json",
        "response_json_schema": Recipe.model_json_schema(),  # Pydantic schema
    },
)
recipe = Recipe.model_validate_json(response.text)
```

## SDK Schema Helpers

| Language | Library | Method |
|---|---|---|
| Python | Pydantic (`BaseModel`) | `MyModel.model_json_schema()` |
| JavaScript | Zod + `zod-to-json-schema` | `zodToJsonSchema(mySchema)` |

## Schema Support

- Supported JSON Schema types: `object`, `array`, `string`, `integer`, `number`, `boolean`
- Supports optional fields, nested objects, recursive structures
- `enum` type supported for constrained string values

## Content Moderation Example Pattern

Use `array` of classified items with `enum` severity field.

## Recursive Structures

Schemas can reference themselves (e.g., a nested category tree). Define recursive `$defs` in raw JSON Schema.

## Notes

- The model always returns valid JSON conforming to the schema when this mode is enabled.
- If output does not parse, the model still attempted to conform — check schema complexity.
- Works with REST API (pass raw JSON Schema) and all SDKs.
