---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/text-generation.md
source_url: https://ai.google.dev/gemini-api/docs/text-generation
title: "Gemini API — Text Generation"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Gemini API Text Generation

Source is in Turkish (crawler localization).

## Overview

The Gemini API can generate text from text, image, video, and audio inputs using the `generateContent` method.

## Basic Example

```python
from google import genai
client = genai.Client()
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="How does AI work?"
)
print(response.text)
```

Available in: Python, JavaScript, Go, Java, REST, Apps Script.

## Thinking Integration

Gemini 2.5 and 3 series models enable "thinking" by default. Thinking improves reasoning quality before responding. Configurable via `ThinkingConfig`:

```python
from google.genai import types
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="How does AI work?",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="low")
    ),
)
```

- `thinking_level`: `"low"`, `"medium"`, `"high"` — controls cost, latency, and intelligence tradeoff.

## Streaming

Use `generate_content_stream()` for streaming responses. Useful for long outputs where you want to display incrementally.

## Multimodal Inputs

Same `generateContent` method supports passing images, video, audio, and documents alongside text prompts (via the Files API or inline).

## System Instructions

Set behavior via `system_instruction` parameter in `GenerateContentConfig`.

## Key Config Options

- `temperature` — creativity/randomness
- `max_output_tokens` — response length limit
- `stop_sequences` — custom stop strings
- `response_mime_type` — e.g. `"application/json"` for structured output
