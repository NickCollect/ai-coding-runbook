---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/audio.md
source_url: https://ai.google.dev/gemini-api/docs/audio
title: "Gemini API — Audio Understanding"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Gemini API Audio Understanding

Source is in German (crawler localization).

## Overview

Gemini can analyze audio inputs and generate text responses. Understands audio content, including speech, music, and ambient sounds. First LLM family to natively understand audio without a separate speech-to-text step.

## Basic Usage

Upload audio file via Files API, then pass to `generateContent`:

```python
from google import genai
client = genai.Client()
myfile = client.files.upload(file="path/to/sample.mp3")
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=["Describe this audio clip", myfile]
)
print(response.text)
```

## Supported Audio Formats

MP3, WAV, AIFF, AAC, OGG, FLAC, and more.

## Audio Token Rate

Audio is billed at **25 tokens per second** of audio content.

## Use Cases

- Transcription and translation (real-time or batch)
- Podcast / video Q&A
- Meeting transcription and summarization
- Voice assistant understanding
- Audio content analysis and classification

## Inline Audio

For small audio clips, can pass bytes inline without Files API (total request < 20MB):

```python
audio_bytes = open("sample.mp3", "rb").read()
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[
        types.Part.from_bytes(data=audio_bytes, mime_type="audio/mpeg"),
        "Transcribe this audio"
    ]
)
```
