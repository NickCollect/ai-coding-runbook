# Structured Outputs

<!-- source: https://platform.openai.com/docs/guides/structured-outputs -->

JSON is one of the most widely used formats in the world for applications to exchange data.

Structured Outputs is a feature that ensures the model will always generate responses that adhere to your supplied JSON Schema, so you don't need to worry about the model omitting a required key, or hallucinating an invalid enum value.

## Benefits

1. **Reliable type-safety**: No need to validate or retry incorrectly formatted responses
2. **Explicit refusals**: Safety-based model refusals are now programmatically detectable
3. **Simpler prompting**: No need for strongly worded prompts to achieve consistent formatting

## Supported models

Structured Outputs is available starting with GPT-4o. Older models like `gpt-4-turbo` and earlier may use JSON mode instead.

## Two forms in the OpenAI API

1. **When using function calling** — best when building an application that bridges models and functionality (querying databases, interacting with UI)
2. **When using `json_schema` response format** (`text.format`) — best when you want to indicate a structured schema for use when the model responds to the user

## Structured Outputs vs JSON mode

| | Structured Outputs | JSON Mode |
|---|---|---|
| Outputs valid JSON | Yes | Yes |
| Adheres to schema | Yes | No |
| Compatible models | `gpt-4o-mini`, `gpt-4o-2024-08-06`, and later | `gpt-3.5-turbo`, `gpt-4-*` and `gpt-4o-*` models |
| Enabling | `text: { format: { type: "json_schema", "strict": true, "schema": ... } }` | `text: { format: { type: "json_object" } }` |

We recommend always using Structured Outputs instead of JSON mode when possible.

## Refusals with Structured Outputs

When using Structured Outputs with user-generated input, models may occasionally refuse for safety reasons. The API response will include a `refusal` field to indicate this. Check for `refusal` in your output object and handle it appropriately.

## Tips and best practices

- **Handling user-generated input**: Include instructions on how to handle situations where the input cannot result in a valid response
- **Handling mistakes**: Adjust instructions, provide examples in system instructions, or split tasks into simpler subtasks
- **Avoid JSON schema divergence**: Use native Pydantic/Zod SDK support to keep schemas in sync

## JSON mode

JSON mode ensures valid JSON output but does NOT guarantee schema adherence. When using JSON mode:
- Always instruct the model to produce JSON via some message in the conversation
- JSON mode will not guarantee the output matches any specific schema
