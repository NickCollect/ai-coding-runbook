---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/thinking.md
source_url: https://ai.google.dev/gemini-api/docs/thinking
title: "Gemini API — Thinking"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Gemini API Thinking

Source is in Thai (crawler localization).

## Overview

Gemini 3 and 2.5 series models support an internal "thinking" process that significantly improves reasoning and multi-step planning. Useful for: coding, advanced math, data analysis.

## Supported Models

Gemini 3 series (`gemini-3-flash-preview`, etc.) and Gemini 2.5 series (`gemini-2.5-pro`, `gemini-2.5-flash`, etc.).

## Basic Usage

Thinking is typically enabled by default. Use same `generateContent` call — just specify a thinking-capable model.

```python
from google import genai
client = genai.Client()
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Explain Occam's Razor with a simple example."
)
print(response.text)
```

## Controlling Thinking Budget

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

`thinking_level` options: `"low"`, `"medium"`, `"high"` (or equivalent budget values). Cost and latency scale with thinking budget.

## Accessing Thought Summaries

Set `include_thoughts=True` to receive the model's internal reasoning summary. Check `part.thought` boolean to distinguish thought parts from answer parts.

```python
config=types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(include_thoughts=True)
)

for part in response.candidates[0].content.parts:
    if part.thought:
        print("Thought summary:", part.text)
    else:
        print("Answer:", part.text)
```

## Streaming Thought Summaries

Use `generate_content_stream()` with the same `include_thoughts=True` config. Thought chunks arrive before the final answer.

## Key Points

- Thinking budget affects raw thoughts, NOT the thought summary.
- `include_thoughts` surfaces a summarized version of the model's reasoning.
- Thought tokens count toward billing (output tokens).
- Gemini 3 models return unique `id` on every `functionCall`; include that exact `id` in `functionResponse`.
