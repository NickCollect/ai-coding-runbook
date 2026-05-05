---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/video.md
source_url: https://ai.google.dev/gemini-api/docs/video
title: "Gemini API — Video Generation with Veo 3.1"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Video Generation with Veo 3.1

Source is in Indonesian (crawler localization).

## Overview

Veo 3.1 is Google's latest video generation model. Creates 8-second videos at 720p, 1080p, or 4K with high fidelity, cinematic realism, and natively generated audio.

## Models

| Model ID | Variant | Price |
|---|---|---|
| `veo-3.1-generate-preview` | Standard with audio | $0.40/sec (720p/1080p), $0.60/sec (4K) |
| `veo-3.1-fast-generate-preview` | Fast with audio | $0.10/sec (720p), $0.12/sec (1080p), $0.30/sec (4K) |
| `veo-3.1-lite-generate-preview` | Lite with audio | $0.05/sec (720p), $0.08/sec (1080p) |
| `veo-3.0-generate-001` | Stable Veo 3 | $0.40/sec |

## New Veo 3.1 Capabilities

- **Portrait video**: Choose landscape (16:9) or portrait (9:16) aspect ratio
- **Video extension**: Extend previously generated videos
- **Frame-specific generation**: Specify first and/or last frame
- **Image-based guidance**: Use up to 3 reference images to guide content

## Async Generation Pattern (Required)

Video generation is async — use background operations:

```python
import time
from google import genai
from google.genai import types

client = genai.Client()

operation = client.models.generate_videos(
    model="veo-3.1-generate-preview",
    prompt="A close up of two people at a cave wall. Man murmurs 'This must be it.' Woman whispers excitedly.",
    config=types.GenerateVideosConfig(
        aspect_ratio="16:9",
        number_of_videos=1,
    )
)

# Poll until done
while not operation.done:
    time.sleep(10)
    operation = client.operations.get(operation)

# Save video
for video in operation.result.generated_videos:
    with open("output.mp4", "wb") as f:
        f.write(video.video.video_bytes)
```

## Notes

- Paid tier only (not available in Free tier).
- Audio is generated natively (not added separately).
- `veo-3.0-generate-001` is the stable non-preview model.
