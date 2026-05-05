---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/live-api/get-started-sdk.md
source_url: https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk
title: "Gemini API — Live API Getting Started (SDK)"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Live API Getting Started with Google GenAI SDK

Source is in Vietnamese (crawler localization).

## Overview

Gemini Live API enables real-time bidirectional interactions with Gemini models. Supports audio, video, and text inputs + native audio output. This guide covers SDK integration for server-side apps.

## Key Concepts

- **Session**: Persistent connection to the model
- **Config**: Modalities (audio/text), voice, system instructions
- **Real-time input**: Audio/video frames sent as blobs

## Python SDK Connection

```python
import asyncio
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")
model = "gemini-3.1-flash-live-preview"
config = {"response_modalities": ["AUDIO"]}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        print("Session started")
        # Send content, receive audio response...

asyncio.run(main())
```

## JavaScript SDK

```javascript
import { GoogleGenAI, Modality } from '@google/genai';
const ai = new GoogleGenAI({ apiKey: process.env.API_KEY });
// Similar pattern with async session management
```

## Available Models

- `gemini-3.1-flash-live-preview` (latest)
- `gemini-2.5-flash-native-audio-preview-12-2025`

## Session API Methods

- `session.send_text()`: Send text to the model
- `session.send_realtime_input(audio=...)`: Send audio chunk
- `session.receive()`: Async iterator for server responses (audio chunks, text, tool calls)

## See Also

- `live-api.md`: Live API overview
- `live-api/capabilities.md`: Full capabilities comparison
- `live-api/best-practices.md`: Best practices
- `live-api/session-management.md`: Session lifetime and resumption
