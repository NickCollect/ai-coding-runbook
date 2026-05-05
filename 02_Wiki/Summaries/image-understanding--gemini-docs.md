---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/image-understanding.md
source_url: https://ai.google.dev/gemini-api/docs/image-understanding
title: "Gemini API — Image Understanding"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Gemini API Image Understanding

Source is in Brazilian Portuguese (crawler localization).

## Overview

Gemini models are natively multimodal. Wide range of image processing and computer vision tasks — captioning, classification, visual question answering — without requiring specialized ML model training.

Enhanced precision via additional training for specific use cases like **object detection**.

## Input Methods

### 1. Inline Image Data (< 20 MB total request)

```python
from google import genai
from google.genai import types

with open('path/to/image.jpg', 'rb') as f:
    image_bytes = f.read()

client = genai.Client()
response = client.models.generate_content(
    model='gemini-3-flash-preview',
    contents=[
        types.Part.from_bytes(data=image_bytes, mime_type='image/jpeg'),
        'Caption this image.'
    ]
)
print(response.text)
```

### 2. Files API (Large or Reused Images)

Upload with `client.files.upload()` → reference URI in multiple requests.

## Capabilities

- Image captioning
- Classification
- Visual Q&A
- Object detection (with bounding boxes)
- OCR (text extraction from images)
- Image comparison
- Diagram/chart interpretation
- Multi-image analysis

## Supported Formats

JPEG, PNG, WEBP, HEIC, HEIF, GIF, BMP.

## Image Token Counts

Image token count depends on resolution. Smaller images use fewer tokens. Use `count_tokens` to estimate cost.

## Object Detection

Returns bounding box coordinates normalized to [0,1]. Requires post-processing to map to pixel coordinates.
