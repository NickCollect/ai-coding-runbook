---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/models/gemini-embedding-001.md
source_url: https://ai.google.dev/gemini-api/docs/models/gemini-embedding-001
title: "Gemini API Model Spec — gemini-embedding-001"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Model: gemini-embedding-001

Source is in Brazilian Portuguese (crawler localization).

## Overview

Specialized engine for high-dimensional vector representation. Efficient numerical mapping of text and images. Ideal for semantic search, document retrieval, and recommendation systems requiring fast, scalable similarity calculations on large datasets.

## Spec Sheet

| Property | Value |
|---|---|
| Model ID | `gemini-embedding-001` |
| API | Gemini API |
| Data types | **Input**: Text · **Output**: Text embeddings |
| Input token limit | 2,048 |
| Output dimension | Flexible: 128–3,072 · Recommended: 768, 1,536, 3,072 |
| Versions | Stable: `gemini-embedding-001` |
| Last updated | June 2025 |

## Notes

- Text-only embedding model (does NOT support images, video, audio, PDF)
- See `gemini-embedding-2` for multimodal embedding support
- See `embeddings.md` for full feature documentation
