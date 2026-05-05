---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/nanobanana.md
source_url: https://ai.google.dev/gemini-api/docs/nanobanana
title: "Gemini API — Nano Banana (Native Image Generation)"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Nano Banana (Native Image Generation)

Source is in Latin American Spanish (crawler localization).

## Overview

**Nano Banana** is the name for Gemini's native image generation capabilities — two models available via the `generate_content` endpoint (unlike Imagen which uses `generate_images`).

## Models

| Name | Model ID | Description |
|---|---|---|
| Nano Banana | `gemini-2.5-flash-image` | Speed + efficiency; optimized for high-volume, low-latency |
| Nano Banana Pro | `gemini-3-pro-image-preview` | Professional-grade output; advanced "Thinking" for complex instructions, high-fidelity text rendering |

## Usage

```python
from google import genai
from PIL import Image

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash-image",
    contents="Create a picture of a futuristic banana with neon lights in a cyberpunk city.",
)

for part in response.parts:
    if part.inline_data:
        image = part.as_image()
        image.show()
```

Also works with `response_modalities=["IMAGE"]` config.

## Key Differentiators vs Imagen

| Aspect | Nano Banana | Imagen |
|---|---|---|
| API method | `generate_content` (text+image unified) | `generate_images` (dedicated) |
| Text rendering | High fidelity (Pro) | High quality |
| Image editing | Supports image-to-image | Image-to-image support |
| Context | Multimodal context (text+image) | Text-to-image |
| Grounding | Image search grounding supported | Not supported |

## SynthID Watermarking

Generated images include SynthID digital watermarks per Google policy.

## See Also

- `image-generation.md` for combined image generation guide
- `imagen.md` for Imagen model details
