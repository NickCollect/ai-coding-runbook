---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/music-generation.md
source_url: https://ai.google.dev/gemini-api/docs/music-generation
title: "Gemini API — Music Generation with Lyria 3"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Music Generation with Lyria 3

Source is in Hebrew (crawler localization).

## Overview

Lyria 3 is Google's music generation model family available via Gemini API. Generates high-quality 44.1kHz stereo audio from text or image prompts. Supports structural coherence including vocals, lyrics, and full instrumental arrangements.

## Models

| Model | ID | Best For | Duration | Output |
|---|---|---|---|---|
| Lyria 3 Clip | `lyria-3-clip-preview` | Short clips, loops, snippets | Always 30 seconds | MP3 |
| Lyria 3 Pro | `lyria-3-pro-preview` | Full songs (verses, chorus, bridge) | Minutes (prompt-controlled) | MP3 |

## Usage

Both models use standard `generateContent` method with multimodal input (text + images):

```python
from google import genai
client = genai.Client()

response = client.models.generate_content(
    model="lyria-3-clip-preview",
    contents="Create a 30-second cheerful acoustic folk song with guitar and harmonica.",
)

for part in response.parts:
    if part.text is not None:
        print(part.text)  # Generated lyrics/structure
    elif part.inline_data is not None:
        with open("clip.mp3", "wb") as f:
            f.write(part.inline_data.data)  # Audio bytes
```

## Response

- `text` part: Generated lyrics and song structure
- `inline_data` part: MP3 audio bytes

## Interactions API

Also supported via `client.interactions.create()` for agent-based music generation workflows.

## Pricing

- Lyria 3 Clip (30s): $0.04/track
- Lyria 3 Pro (full track): $0.08/track
- Free tier: Not available (Paid tier only)
