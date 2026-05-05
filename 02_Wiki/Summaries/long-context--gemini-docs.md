---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/long-context.md
source_url: https://ai.google.dev/gemini-api/docs/long-context
title: "Gemini API — Long Context"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Gemini API Long Context

Source is in Vietnamese (crawler localization).

## Overview

Many Gemini models support 1M+ token context windows, enabling entirely new use cases without complex retrieval pipelines.

## Scale Reference

1 million tokens ≈:
- 50,000 lines of code (80 chars/line)
- All text messages sent over 5 years
- 8 average-length English novels
- Transcripts of 200+ average-length podcasts

## No-Code-Change Required

Existing `generateContent` code works unchanged with long context. No special API calls needed — just pass more content.

## Use Cases

### Long Text
- Summarization of large document sets (no sliding window needed)
- Q&A over large knowledge bases (often replaces RAG for single-user scenarios)
- AI assistant workflows with full history
- **Many-shot learning**: hundreds to thousands of examples in-context → similar performance to fine-tuning for specific tasks

### Long Video
- Video Q&A
- Video memory (see Google Project Astra)
- Subtitle generation
- Video recommendation enrichment
- Content moderation
- Real-time video processing

### Long Audio
- Real-time transcription and translation
- Podcast / video Q&A
- Meeting transcription and summarization
- Voice assistants

## Key Principle

Gemini was purpose-built for large context → strong in-context learning. Example: learned to translate English to Kalamang (a Papua language with <200 speakers) using only a 500-page reference grammar, a dictionary, and ~400 parallel sentences in context.

## Optimization: Context Caching

For repeated large context sets, use context caching to:
- Reduce per-request cost (cached input tokens cost ~4x less than standard input tokens for Flash)
- Reduce latency on subsequent requests
- Enable "chat with your data" patterns economically

## Limitations

- **Multiple needle problem**: High accuracy (~99%) for single target fact retrieval. Performance degrades when retrieving many specific facts simultaneously.
- Longer context = higher latency (time to first token).
- Very long contexts cost more — use caching when reusing same context.

## Best Practices

- Place the query/question **at the end** of the prompt (after all context) for best performance.
- Use context caching when the same large context will be queried multiple times.
- For 100 independent facts, consider 100 separate requests with caching for 99% accuracy per fact.
