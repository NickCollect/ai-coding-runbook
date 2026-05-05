---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/imagen.md
source_url: https://ai.google.dev/gemini-api/docs/imagen
title: "Gemini API — Imagen Image Generation"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Gemini API Imagen

Source is in Hebrew (crawler localization).

## Overview

Imagen is Google's dedicated text-to-image model family, available through the Gemini API. Generates high-quality, photorealistic images from text prompts. All generated images include **SynthID watermarks**.

## Models (Imagen 4)

| Model ID | Variant | Price |
|---|---|---|
| `imagen-4.0-generate-001` | Standard | $0.04/image |
| `imagen-4.0-ultra-generate-001` | Ultra (highest quality) | $0.06/image |
| `imagen-4.0-fast-generate-001` | Fast (lower latency) | $0.02/image |

## Usage

Uses dedicated `generate_images` method (not `generateContent`):

```python
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_images(
    model='imagen-4.0-generate-001',
    prompt='Robot holding a red skateboard',
    config=types.GenerateImagesConfig(
        number_of_images=4,
    )
)
for generated_image in response.generated_images:
    generated_image.image.show()
```

JavaScript: `ai.models.generateImages({ model: "imagen-4.0-generate-001", prompt: "...", config: { numberOfImages: 4 } })`

## Key Differences vs. Nano Banana

| Aspect | Imagen 4 | Nano Banana (gemini-3.x-image) |
|---|---|---|
| Method | `generate_images` | `generateContent` |
| Context | Text-to-image only | Multimodal (text+image in, text+image out) |
| Price | Per image ($0.02–$0.06) | Per token ($60–$120/1M image output tokens) |
| Interleaving | No | Yes (interleaved text+image) |
| Use case | Pure image gen | Context-aware editing, conversational |

## Notes

- Available in Paid tier only (not Free tier).
- All images include SynthID watermark for provenance.
- Supports aspect ratio configuration.
- See `models/imagen.md` for model-specific capability details.
