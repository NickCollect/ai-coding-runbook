---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/models/gemini-embedding-2.md
source_url: https://ai.google.dev/gemini-api/docs/models/gemini-embedding-2
title: "Gemini API Model Spec — gemini-embedding-2"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Model: gemini-embedding-2

Source is in French (crawler localization).

## Overview

Google's first **multimodal** embedding model. Provides efficient numerical mapping of text, images, videos, audio, and PDFs into a single unified embedding space. Ideal for cross-modal semantic search, document retrieval, and recommendation systems requiring fast, scalable similarity calculations on large multimodal datasets.

## Spec Sheet

| Property | Value |
|---|---|
| Model ID | `gemini-embedding-2` |
| API | Gemini API |
| Data types | **Input**: Text, image, video, audio, PDF · **Output**: Text embeddings |
| Input token limit | 8,192 |
| Output dimension | Flexible: 128–3,072 · Recommended: 768, 1,536, 3,072 |
| Versions | Stable: `gemini-embedding-2` |
| Last updated | April 2026 |

## Comparison with gemini-embedding-001

| Feature | gemini-embedding-001 | gemini-embedding-2 |
|---|---|---|
| Modalities | Text only | Text + Image + Video + Audio + PDF |
| Input token limit | 2,048 | 8,192 |
| Status | Stable | Stable |

- See `embeddings.md` for full feature documentation
