---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/image-generation.md
source_url: https://ai.google.dev/gemini-api/docs/image-generation
title: "Gemini API — Image Generation (Nano Banana)"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Gemini API Image Generation (Nano Banana)

Source is in Brazilian Portuguese (crawler localization).

## Models

| Model | Internal Name | Characteristics |
|---|---|---|
| Nano Banana 2 | `gemini-3.1-flash-image-preview` | Fast, efficient, high-volume production, interleaved text+image generation |
| Nano Banana Pro | `gemini-3-pro-image-preview` | Professional design engine, reasoning core, 4K studio-quality, complex layouts, precise text rendering |

## Generation Capabilities

- Magazine covers with text overlays
- Product mockups and commercial photography
- Cityscapes and architectural visualizations
- Photo restoration
- Image editing and composition
- Grounding with Google Image Search for accurate visual references

## API Usage

Use standard `generateContent` method with `response_modalities` including images:

```python
from google import genai
from google.genai import types

client = genai.Client()
response = client.models.generate_content(
    model="gemini-3.1-flash-image-preview",
    contents="Create a professional product photo of a blue ceramic mug on a marble surface",
    config=types.GenerateContentConfig(
        response_modalities=["TEXT", "IMAGE"]
    )
)
for part in response.candidates[0].content.parts:
    if hasattr(part, 'inline_data'):
        # Save image
        with open("output.png", "wb") as f:
            f.write(part.inline_data.data)
```

## Image Search Grounding

Nano Banana 2 supports grounding with Google Image Search for photo-accurate subject rendering (e.g., specific bird species, architectural landmarks).

## Notes

- Both models support context-aware editing (input image + text prompt for edits)
- Images billed per token (see pricing for rates by model and resolution)
- Nano Banana Pro supports higher resolution outputs (up to 4K)
