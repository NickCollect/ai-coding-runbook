---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/models/lyria-3-pro-preview.md
source_url: https://ai.google.dev/gemini-api/docs/models/lyria-3-pro-preview
title: "Gemini API Model Spec — lyria-3-pro-preview"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Model: lyria-3-pro-preview

Source is in Turkish (crawler localization).

## Overview

Google's flagship music generation model. Optimized for generating full-length songs with complex structural coherence including multiple verses, choruses, and bridges. Generates high-quality 48 kHz stereo audio from text prompts or image inputs.

## Spec Sheet

| Property | Value |
|---|---|
| Model ID | `lyria-3-pro-preview` |
| Data types | **Input**: Text + image · **Output**: Audio (MP3), Text (lyrics) |
| Input token limit | 131,072 |
| Versions | Preview: `lyria-3-clip-preview`; Preview: `lyria-3-pro-preview` |
| Last updated | March 2026 |

## Capabilities

✓ Audio generation

✗ Batch API · ✗ Caching · ✗ Code execution · ✗ File search · ✗ Function calling · ✗ Image generation · ✗ Live API · ✗ Search grounding · ✗ Structured output · ✗ Thinking

## Notes

- Full-length songs (multiple verses, choruses, bridges)
- Contrast with `lyria-3-clip-preview` (30-second clips) and `lyria-realtime-exp` (real-time streaming)
- See `music-generation.md` for full documentation
