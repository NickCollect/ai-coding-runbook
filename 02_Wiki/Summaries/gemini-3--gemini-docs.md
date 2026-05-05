---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/gemini-3.md
source_url: https://ai.google.dev/gemini-api/docs/gemini-3
title: "Gemini API — Gemini 3 Developer Guide"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Gemini 3 Developer Guide

Source is in Vietnamese (crawler localization).

## Overview

Gemini 3 is Google's most intelligent model family, built on advanced reasoning foundations. Pro is designed for agentic workflows, vibe coding, and complex multimodal tasks.

## Models

- `gemini-3.1-pro-preview`: Complex problem solving, agentic workflows, vibe coding, advanced coding
- `gemini-3-flash-preview`: Frontier-class performance at lower cost
- `gemini-3.1-flash-lite-preview`: Most cost-efficient in the Gemini 3 family
- Image models: Nano Banana 2 (`gemini-3.1-flash-image-preview`), Nano Banana Pro (`gemini-3-pro-image-preview`)

## Key Capabilities

- **Advanced reasoning**: Handles complex multi-step reasoning tasks
- **Agentic coding**: Automated programming and vibe coding
- **Complex multimodal**: Handles complex tasks involving multiple modalities
- **Function call IDs**: Gemini 3 always returns unique `id` on every `functionCall`
- **Image-based code execution**: Gemini 3 Flash can write/run Python on images (zoom, inspect, annotate)

## Quick Start

```python
from google import genai
client = genai.Client()
response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="Find the race condition in this multi-threaded C++ snippet: [code]",
)
print(response.text)
```

## Developer Resources

- Try apps: aistudio.google.com/app/apps (Gemini 3 showcase collection)
- All Gemini 3 models support the same SDK patterns as previous models
