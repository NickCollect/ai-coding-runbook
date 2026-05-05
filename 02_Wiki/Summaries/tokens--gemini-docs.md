---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/tokens.md
source_url: https://ai.google.dev/gemini-api/docs/tokens
title: "Gemini API — Understanding and Counting Tokens"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Gemini API Tokens

Source is in Vietnamese (crawler localization).

## Token Basics

- Gemini processes input and output at the granularity of *tokens*.
- **1 token ≈ 4 characters**; **100 tokens ≈ 60–80 English words**.
- Tokens can be single characters (`z`) or whole words (`cat`); long words split into multiple tokens.
- All API costs are determined partly by input + output token counts.

## Counting Tokens (Two Methods)

### Method 1: Pre-request count (input only)
```python
total_tokens = client.models.count_tokens(
    model="gemini-3-flash-preview",
    contents=prompt
)
print(total_tokens)
```
Returns `total_tokens` in input. Use before sending to check request size.

### Method 2: Post-response usage_metadata
```python
response = client.models.generate_content(model=..., contents=...)
print(response.usage_metadata)
```

Returns:
- `prompt_token_count`: input token count
- `candidates_token_count`: output token count
- `total_token_count`: combined
- `thoughts_token_count`: tokens used during thinking (for thinking models)
- `cached_content_token_count`: tokens served from cache

## Multi-turn / Chat Token Counting

Pass the full conversation history to `count_tokens` to get cumulative count. Append the next user turn to estimate size of next request before sending.

## Media Token Counts

All input types are tokenized:

| Media Type | Token Calculation |
|---|---|
| Text | ~4 chars/token |
| Images | Fixed tokens per image (depends on resolution/detail setting) |
| Video | Tokens per frame (depends on fps sampling) |
| Audio | 25 tokens per second of audio |
| PDFs | Tokens per page (similar to image) |

## Counting Multi-modal Inputs

`count_tokens` supports full multimodal inputs (images, video, audio, files) to get a complete pre-request estimate.

## Thinking Token Accounting

For thinking models, `thoughts_token_count` is billed as output tokens even though the user doesn't see the raw thinking text (unless `include_thoughts=True` is set). Budget this when cost planning.

## Context Window Limits

Each model has a maximum context window (input tokens). Check `model.input_token_limit` for the model you're using. Exceeding this limit causes an error.

## Notes

- Token counting is free (no charge for `count_tokens` calls).
- System instructions and cached content both count toward input tokens.
- The tokenizer is model-specific; different models may tokenize the same text differently.
