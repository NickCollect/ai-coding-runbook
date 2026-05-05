---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/models/gemini-embedding-2-preview.md
source_url: https://ai.google.dev/gemini-api/docs/models/gemini-embedding-2-preview
title: "Gemini API Model Spec — gemini-embedding-2-preview"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Model: gemini-embedding-2-preview

Source is in Thai (crawler localization).

## Overview

Preview version of the first multimodal embedding model. Provides efficient numerical mapping of text, images, videos, audio, and PDFs into a single unified embedding space. Ideal for cross-modal semantic search, document retrieval, and recommendation systems.

## Spec Sheet

| Property | Value |
|---|---|
| Model ID | `gemini-embedding-2-preview` |
| API | Gemini API |
| Data types | **Input**: Text, image, video, audio, PDF · **Output**: Text embeddings |
| Input token limit | 8,192 |
| Output dimension | Flexible: 128–3,072 · Recommended: 768, 1,536, 3,072 |
| Versions | Preview: `gemini-embedding-2-preview` |
| Last updated | March 2026 |

## Notes

- Preview version of `gemini-embedding-2` (stable)
- See `embeddings.md` for full feature documentation
