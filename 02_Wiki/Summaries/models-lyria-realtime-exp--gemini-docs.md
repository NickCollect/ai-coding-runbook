---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/models/lyria-realtime-exp.md
source_url: https://ai.google.dev/gemini-api/docs/models/lyria-realtime-exp
title: "Gemini API Model Spec — lyria-realtime-exp"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Model: lyria-realtime-exp

Source is in Vietnamese (crawler localization).

## Overview

Experimental tool for high-fidelity music synthesis. Provides enhanced features for creating and transforming audio content. Best for AI-assisted songwriting, unique instrumental creation, and creative audio workflows requiring deep control over melody and rhythm. **No vocals**.

## Spec Sheet

| Property | Value |
|---|---|
| Model ID | `lyria-realtime-exp` |
| Data types | **Input**: Text (weighted prompts) · **Output**: Audio (raw 16-bit PCM) |
| Streaming | 48kHz stereo · Control latency: up to 2 seconds |
| Versions | Experimental: `lyria-realtime-exp` |
| Last updated | May 2025 |

## Notes

- Real-time streaming via WebSocket (bidirectional) — different from Lyria 3 Clip/Pro batch generation
- Output is raw PCM (not MP3) — requires client-side processing for playback
- No vocals — instrumental music only
- See `realtime-music-generation.md` for full documentation
