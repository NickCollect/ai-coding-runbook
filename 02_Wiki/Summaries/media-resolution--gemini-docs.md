---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/media-resolution.md
source_url: https://ai.google.dev/gemini-api/docs/media-resolution
title: "Gemini API — Media Resolution"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Gemini API Media Resolution

Source is in Latin American Spanish (crawler localization).

## Overview

The `media_resolution` parameter controls how the API processes media inputs (images, video, PDFs) by setting the **maximum token count** allocated to media. Balance response quality vs. latency and cost.

## Two Configuration Scopes

### Per-Part (Gemini 3 only, v1alpha API)

Set resolution for individual media objects within a request. Mix resolution levels in a single request (e.g., high for complex diagram, low for contextual image).

```python
client = genai.Client(http_options={'api_version': 'v1alpha'})

image_part_high = types.Part.from_bytes(
    data=image_bytes,
    mime_type='image/jpeg',
    media_resolution=types.MediaResolution.MEDIA_RESOLUTION_HIGH
)
image_part_low = types.Part.from_bytes(
    data=image_bytes_2,
    mime_type='image/jpeg',
    media_resolution=types.MediaResolution.MEDIA_RESOLUTION_LOW
)
```

Per-part overrides global setting for that specific part.

### Global (All multimodal models)

Apply to entire `generateContent` request:

```python
config = types.GenerateContentConfig(
    media_resolution=types.MediaResolution.MEDIA_RESOLUTION_LOW
)
```

## Resolution Settings

| Setting | Tokens | Use When |
|---|---|---|
| `MEDIA_RESOLUTION_HIGH` | More tokens | Fine details matter (diagrams, text in image) |
| `MEDIA_RESOLUTION_MEDIUM` | Default | General purpose |
| `MEDIA_RESOLUTION_LOW` | Fewer tokens | Cost/latency optimization, simple visuals |

## When to Use

- High: Complex diagrams, screenshots with text, detailed images where accuracy matters
- Low: Thumbnail context, approximate content, when speed/cost is priority
- Mixed: Single request with both detailed and contextual images
