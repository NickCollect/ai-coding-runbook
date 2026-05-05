---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/video-understanding.md
source_url: https://ai.google.dev/gemini-api/docs/video-understanding
title: "Gemini API — Video Understanding"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Gemini API Video Understanding

Source is in Brazilian Portuguese (crawler localization).

## Overview

Gemini models can process videos enabling developer use cases that historically required domain-specific models. Capabilities: describe, segment, extract information, Q&A about video content, reference specific timestamps.

## Input Methods

| Method | Max Size | Recommended For |
|---|---|---|
| Files API | 20 GB (paid) / 2 GB (free) | Large files (>100MB), long videos (>10 min), reusable files |
| Cloud Storage registration | 2 GB per file, no storage limit | Large files, persistent and reusable |
| Inline data | <100 MB | Small files (<100MB), short (<1 min), one-time use |
| YouTube URL | N/A | Public YouTube videos |

## Files API (Recommended)

```python
from google import genai
client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp4")

# Wait for processing
while myfile.state.name == 'PROCESSING':
    import time; time.sleep(5)
    myfile = client.files.get(name=myfile.name)

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=["Summarize this video", myfile]
)
print(response.text)
```

## YouTube URL

Pass YouTube URL directly as URL reference (no upload needed):
```python
contents = [
    types.Part.from_uri(uri="https://www.youtube.com/watch?v=...", mime_type="video/*"),
    "Describe the main topics in this video."
]
```

## Video Token Rates

Videos are tokenized as frames (sampled at 1 fps typically). Long videos = many tokens. Use `count_tokens` to estimate costs.

## Capabilities

- Video description and summarization
- Segment and scene identification
- Timestamp-specific Q&A ("What happens at 2:30?")
- Multi-video comparison
- Subtitle generation
- Content moderation
