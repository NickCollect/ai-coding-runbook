---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/speech-generation.md
source_url: https://ai.google.dev/gemini-api/docs/speech-generation
title: "Gemini API — Text-to-Speech Generation (TTS)"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Gemini API TTS (Text-to-Speech)

Source is in Japanese (crawler localization).

## Overview

Gemini API TTS converts text to single-speaker or multi-speaker audio. Controllable via natural language: guide voice style, accent, pace, and tone. Designed for precise text narration (podcasts, audiobooks, etc.) — distinct from Live API audio which handles dynamic conversation.

## Models

- `gemini-2.5-flash-preview-tts`: Fast, controllable, low-latency TTS
- `gemini-2.5-pro-preview-tts`: High-fidelity speech synthesis
- `gemini-3.1-flash-tts-preview`: Advanced low-latency TTS with expressive audio tags

## Single-Speaker TTS

```python
from google import genai
from google.genai import types
import wave

def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(sample_width)
        wf.setframerate(rate)
        wf.writeframes(pcm)

client = genai.Client()
response = client.models.generate_content(
    model="gemini-2.5-flash-preview-tts",
    contents="Hello, welcome to the Gemini API text-to-speech demo.",
    config=types.GenerateContentConfig(
        response_modalities=["AUDIO"],
        speech_config=types.SpeechConfig(
            voice_config=types.VoiceConfig(
                prebuilt_voice_config=types.PrebuiltVoiceConfig(voice_name="Aoede")
            )
        )
    )
)
audio_data = response.candidates[0].content.parts[0].inline_data.data
wave_file("output.wav", audio_data)
```

## Multi-Speaker TTS

Support for multiple voices in a single response. Configure separate `SpeakerVoiceConfig` for each speaker.

## Voice Selection

Pre-built voices available (e.g., "Aoede", "Puck", "Charon", etc.). See docs for full voice list.

## Controllable Aspects

- **Style**: Formal, casual, narrative, dramatic, etc.
- **Accent**: Guide via natural language in prompt or style instructions
- **Pace**: Slow, normal, fast
- **Tone**: Cheerful, serious, empathetic, etc.

## TTS vs. Live API Audio

| Aspect | TTS (this doc) | Live API |
|---|---|---|
| Use case | Pre-scripted text, audiobooks, podcasts | Real-time conversation |
| Latency | Batch | Sub-second |
| Control | Fine-grained style | Dynamic |
| Input | Text only | Text, audio, video |
