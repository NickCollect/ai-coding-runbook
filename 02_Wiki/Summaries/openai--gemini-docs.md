---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/openai.md
source_url: https://ai.google.dev/gemini-api/docs/openai
title: "Gemini API — OpenAI Compatibility"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Gemini API OpenAI Compatibility

Source is in Polish (crawler localization).

## Overview

Gemini models are accessible via OpenAI client libraries (Python and TypeScript/JavaScript) and REST API. Only 3 lines of code need to change. Use your Gemini API key.

If you're not already using OpenAI libraries, use the native Gemini API directly.

## Usage

```python
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain how AI works"}
    ]
)
print(response.choices[0].message)
```

JavaScript: Same pattern with `OpenAI` constructor, pass `apiKey` and `baseURL`.

## REST Compatibility

Base URL: `https://generativelanguage.googleapis.com/v1beta/openai/`

Endpoints follow OpenAI REST schema (e.g., `/chat/completions`, `/embeddings`, `/models`).

## Supported OpenAI Features

- `chat.completions.create`
- `embeddings.create`
- Function calling (tool_calls format)
- Streaming
- System messages

## Notes

- Not all OpenAI parameters are supported — check docs for gaps.
- Recommended approach for migration from OpenAI to Gemini with minimal code changes.
- For new projects, native `google-genai` SDK is preferred.
