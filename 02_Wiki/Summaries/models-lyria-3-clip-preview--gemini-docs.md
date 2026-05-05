---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/models/lyria-3-clip-preview.md
source_url: https://ai.google.dev/gemini-api/docs/models/lyria-3-clip-preview
title: "Gemini API Model Spec — lyria-3-clip-preview"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Model: lyria-3-clip-preview

Source is in Traditional Chinese (crawler localization).

## Overview

Google's model specifically designed for generating short music clips, loops, and previews. Generates 30-second, 48 kHz stereo high-quality audio from text prompts or images.

## Spec Sheet

| Property | Value |
|---|---|
| Model ID | `lyria-3-clip-preview` |
| Data types | **Input**: Text + image · **Output**: Audio (MP3), Text (lyrics) |
| Input token limit | 131,072 |
| Versions | Preview: `lyria-3-clip-preview`; also `lyria-3-pro-preview` |
| Last updated | March 2026 |

## Capabilities

✓ Audio generation

✗ Batch API · ✗ Caching · ✗ Code execution · ✗ File search · ✗ Function calling · ✗ Google Maps grounding · ✗ Image generation · ✗ Live API · ✗ Search grounding · ✗ Structured output · ✗ Thinking · ✗ URL context

## Notes

- 30-second clips at 48kHz stereo
- Contrast with `lyria-3-pro-preview` (full-length songs) and `lyria-realtime-exp` (real-time streaming)
- See `music-generation.md` for full documentation
