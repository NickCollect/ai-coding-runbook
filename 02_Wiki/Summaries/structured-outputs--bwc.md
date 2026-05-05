---
type: summary
source: 01_Raw/platform.claude.com/docs/en/build-with-claude/structured-outputs.md
source_url: https://platform.claude.com/docs/en/build-with-claude/structured-outputs
title: "Structured outputs"
summarized_at: 2026-05-05
entities_referenced: [Structured-outputs, Messages-API, Tool-use, Citations-API, Enterprise-gateway]
concepts_referenced: []
---

Structured outputs constrain Claude's responses to follow a JSON schema via constrained decoding — guarantees parseable, schema-compliant output. ZDR-eligible (qualified — JSON schemas cached up to 24h since last use, separate from prompts/outputs).

## Two complementary features

- **JSON outputs** (`output_config.format`): Claude's response is constrained to a JSON schema.
- **Strict tool use** (`strict: true`): tool name + input validation guaranteed.

Independent or combinable in same request.

## Migration

`output_format` parameter has moved to `output_config.format`. Old beta header `structured-outputs-2025-11-13` and `output_format` keep working in transition. New API shape: GA — no beta header needed.

## Availability

| Platform | GA models | Other |
|---|---|---|
| Claude API | Mythos Preview, Opus 4.7, Opus 4.6, Sonnet 4.6, Sonnet 4.5, Opus 4.5, Haiku 4.5 | — |
| Amazon Bedrock | Opus 4.6, Sonnet 4.6, Sonnet 4.5, Opus 4.5, Haiku 4.5 | Opus 4.7, Mythos via "Claude in Amazon Bedrock" Messages-API endpoint |
| Microsoft Foundry | beta | — |
| Vertex AI | not supported for Mythos Preview | other models? — |

## JSON outputs request shape

```json
{
  "output_config": {
    "format": {
      "type": "json_schema",
      "schema": {
        "type": "object",
        "properties": {...},
        "required": [...],
        "additionalProperties": false
      }
    }
  }
}
```

## Strict tool use

Add `strict: true` on tool definition; same JSON schema grammar pipeline.

## Why use it

- No `JSON.parse()` errors (always valid)
- Type-safe / required-field guarantees
- No retries for schema violations

## Limitations

- **Incompatible with Citations** — using `output_config.format` while citations are enabled on any user document → 400. Citations need interleaved blocks; strict JSON forbids that.
- **PHI restriction (HIPAA):** do not put PHI in JSON schema property names, `enum`, `const`, or `pattern` — schemas cached separately without full PHI safeguards.

## Data retention

Prompts and outputs are not stored. Only the JSON schema is cached for grammar compilation, **up to 24 hours since last use**. Same pipeline used by strict tool use.
