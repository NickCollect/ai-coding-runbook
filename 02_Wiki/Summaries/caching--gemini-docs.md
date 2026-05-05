---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/caching.md
source_url: https://ai.google.dev/gemini-api/docs/caching
title: "Gemini API — Context Caching"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Gemini API Context Caching

Source is in Vietnamese (crawler localization).

## Overview

Two caching mechanisms to avoid re-sending the same tokens repeatedly:

1. **Implicit caching** — auto-enabled on Gemini 2.5+ and newer models. Cost savings not guaranteed (depends on cache hit).
2. **Explicit caching** — manually configured, guarantees cost savings when cache is hit.

## Implicit Caching

- Automatically enabled for Gemini 2.5 and later models.
- Google passes savings automatically if request accesses the cache.
- No developer action required to enable.
- Minimum token thresholds for implicit caching:

| Model | Min tokens |
|---|---|
| Gemini 3 Flash preview | 1024 |
| Gemini 3 Pro preview | 4096 |
| Gemini 2.5 Flash | 1024 |
| Gemini 2.5 Pro | 4096 |

- To maximize cache hits: place large, repeated content at the **beginning** of the prompt; send requests with similar prefixes within a short time window.
- Check `usage_metadata` in response for `cached_token_count`.

## Explicit Caching

Pass content to the model once → cache the input tokens → reference cached tokens in subsequent requests. Cost for cached tokens is lower than standard input token cost.

### Creating a Cache

```python
from google.genai import types
cache = client.caches.create(
    model="models/gemini-3-flash-preview",
    config=types.CreateCachedContentConfig(
        display_name="my cache",
        system_instruction="You are an expert video analyzer...",
        contents=[video_file],  # or document, text, etc.
        ttl="300s",  # TTL, default is 1 hour
    )
)
```

### Using a Cache

```python
response = client.models.generate_content(
    model=model,
    contents="Describe the characters.",
    config=types.GenerateContentConfig(cached_content=cache.name)
)
```

## TTL and Storage Cost

- TTL (time-to-live): how long the cache lives before auto-deletion. Default: 1 hour.
- Storage cost: billed per 1M tokens per hour (see pricing — $1.00–$4.50/1M tokens/hour depending on model).
- Cache is invalidated after TTL expires.

## Supported Content Types

- Video files (uploaded via Files API)
- PDFs and documents
- Text files
- System instructions
- Any content that would otherwise be re-sent each request

## Notes

- Explicit caching requires paying tier (not available in Free tier for most models).
- Cached content cannot be modified — create a new cache for updated content.
- Cache names are returned from `caches.create()` and used in subsequent requests.
