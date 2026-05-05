---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/migrate.md
source_url: https://ai.google.dev/gemini-api/docs/migrate
title: "Gemini API — Migration to Google GenAI SDK"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Migration to Google GenAI SDK

Source is in Korean (crawler localization).

## Background

Starting with Gemini 2.0 (late 2024), new library set called **Google Generative AI SDK** introduced. Now GA on all supported platforms. Recommended to migrate from legacy libraries.

## Package Changes

| Language | Old (Legacy) | New (Recommended) |
|---|---|---|
| Python | `google-generativeai` | `google-genai` |
| JavaScript | `@google/generative-ai` | `@google/genai` |
| Go | `github.com/google/generative-ai-go` | `google.golang.org/genai` |

## Key API Changes

- Client initialization: `genai.Client()` (instead of `genai.GenerativeModel()`)
- Model specification: pass as parameter to each method call
- `generate_content` method: `client.models.generate_content(model="...", contents="...")`
- Configuration: `GenerateContentConfig` class (instead of `GenerationConfig`)
- Tools: `types.Tool(...)` (similar but updated imports)

## Code Comparison (Python)

**Before:**
```python
import google.generativeai as genai
genai.configure(api_key="KEY")
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("Hello")
```

**After:**
```python
from google import genai
client = genai.Client()  # reads GEMINI_API_KEY from env
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Hello"
)
```

## Benefits of New SDK

- Unified client architecture
- Simplified migration between Developer API and Enterprise Agent Platform
- Better async support
- More consistent API surface across languages
