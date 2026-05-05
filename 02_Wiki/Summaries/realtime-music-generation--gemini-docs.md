---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/realtime-music-generation.md
source_url: https://ai.google.dev/gemini-api/docs/realtime-music-generation
title: "Gemini API — Lyria RealTime (Real-Time Music Generation)"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Lyria RealTime — Real-Time Music Generation

Source is in Korean (crawler localization).

## Overview

Lyria RealTime provides real-time streaming music generation via WebSocket. Enables developers to build applications where users can interactively create, continuously manipulate, and "perform" instrumental music.

## Architecture

Similar to Live API: WebSocket-based persistent bidirectional low-latency streaming connection.

## Core API Pattern

```python
import asyncio
from google import genai
from google.genai import types

client = genai.Client(http_options={'api_version': 'v1alpha'})

async def main():
    async def receive_audio(session):
        while True:
            async for message in session.receive():
                audio_data = message.server_content.audio_chunks[0].data
                # Process audio chunks

    async with client.aio.live.music.connect(
        model="lyria-realtime-exp"
    ) as session:
        await session.set_weighted_prompts(prompts=[...])
        await session.set_music_generation_config(config=types.LiveMusicGenerationConfig(...))
        await session.play()
        await receive_audio(session)

asyncio.run(main())
```

## Key Operations

- `session.set_weighted_prompts()`: Set initial music generation prompt with weights
- `session.set_music_generation_config()`: Configure generation parameters (BPM, style, etc.)
- `session.play()`: Start music generation
- `session.receive()`: Receive streaming audio chunks

## Try in AI Studio

Available in two demo apps on AI Studio:
- **Prompt DJ**: Text-based prompt control
- **MIDI DJ**: MIDI-based control

## Notes

- Uses `v1alpha` API version
- Distinct from Lyria 3 Clip/Pro which generate complete audio files; RealTime is for live interactive streaming
- Low-latency bidirectional — suitable for interactive music performance applications
