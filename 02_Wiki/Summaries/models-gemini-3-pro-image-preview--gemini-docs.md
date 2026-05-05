---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/models/gemini-3-pro-image-preview.md
source_url: https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image-preview
title: "Gemini API Model Spec — gemini-3-pro-image-preview (Nano Banana Pro)"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Model: gemini-3-pro-image-preview (Nano Banana Pro)

Source is in Vietnamese (crawler localization).

## Overview

**Nano Banana Pro** — sophisticated reasoning-based engine for professional-grade image editing and creation. Studio-level precision with advanced creative control. Best for complex graphic design, high-fidelity product mockups, and data visualizations requiring accurate text rendering and real-world linkage via Google Search.

## Spec Sheet

| Property | Value |
|---|---|
| Model ID | `gemini-3-pro-image-preview` |
| Data types | **Input**: Images + Text · **Output**: Images + Text |
| Input token limit | 65,536 |
| Output token limit | 32,768 |
| Versions | Preview: `gemini-3-pro-image-preview` |
| Last updated | November 2025 |
| Knowledge cutoff | January 2025 |

## Capabilities

✓ Batch API · ✓ Flex inference · ✓ Image generation · ✓ Priority inference · ✓ Search grounding · ✓ Structured output · ✓ Thinking

✗ Audio generation · ✗ Caching · ✗ Code execution · ✗ File search · ✗ Function calling · ✗ Google Maps grounding · ✗ Live API · ✗ URL context

## Notes

- Nano Banana Pro is distinct from Nano Banana (`gemini-2.5-flash-image`) — Pro uses reasoning for complex image tasks
- Uses `generate_content()` with `response_modalities=["IMAGE"]`
- See `nanobanana.md` and `image-generation.md` for documentation
