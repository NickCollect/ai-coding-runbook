---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/models/imagen.md
source_url: https://ai.google.dev/gemini-api/docs/models/imagen
title: "Gemini API Model Spec — Imagen 4"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Model: Imagen 4

Source is in French (crawler localization).

## Overview

High-performance engine for advanced visual synthesis. Sophisticated creative control and photorealistic output. Use for professional branding, complex scene composition, and high-fidelity design tasks requiring precise text rendering and complex lighting.

## Spec Sheet

| Property | Value |
|---|---|
| Model IDs | `imagen-4.0-generate-001` (Standard) · `imagen-4.0-ultra-generate-001` (Ultra) · `imagen-4.0-fast-generate-001` (Fast) |
| API | Gemini API |
| Data types | **Input**: Text · **Output**: Images |
| Input token limit | 480 tokens (text) |
| Output | 1–4 images (Ultra/Standard/Fast) |
| Last updated | June 2025 |

## Notes

- Uses `generate_images()` method (not `generate_content()` like Nano Banana)
- SynthID digital watermarks embedded in all generated images
- Three tiers: Standard (balanced), Ultra (highest quality), Fast (lowest latency/cost)
- See `imagen.md` for full documentation
