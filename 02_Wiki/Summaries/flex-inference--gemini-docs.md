---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/flex-inference.md
source_url: https://ai.google.dev/gemini-api/docs/flex-inference
title: "Gemini API — Flex Inference"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Gemini API Flex Inference

Source is in Indonesian (crawler localization).

## Overview

Flex is an inference tier offering **50% cost reduction** vs. standard rates, in exchange for variable latency and best-effort availability. Designed for: latency-tolerant workloads needing synchronous processing but not real-time performance.

## How to Use

Set `service_tier: "flex"` in the request config. Default is standard tier if omitted.

```python
from google import genai
client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents="Analyze this dataset for trends...",
        config={"service_tier": "flex"},
    )
    print(response.text)
except Exception as e:
    print(f"Flex request failed: {e}")
```

JavaScript: `config: { serviceTier: "flex" }`

## Key Characteristics

- **50% cost reduction** vs. standard
- **Variable latency**: Response time not guaranteed
- **Best-effort availability**: May occasionally fail → wrap in try/except and handle gracefully
- **Synchronous**: Unlike Batch API, you wait for the response (not async)

## When to Use

- Non-real-time analysis tasks
- Data processing pipelines with relaxed latency requirements
- Cost-sensitive workloads where occasional failures are acceptable
- Good alternative to Batch API when synchronous behavior is needed at lower cost

## vs. Other Tiers

| Tier | Cost | Latency | Availability |
|---|---|---|---|
| Standard | 1x | Guaranteed | High |
| Flex | 0.5x | Variable | Best-effort |
| Batch | 0.5x | 24h expected | Async |
| Priority | 1.8x | Low, prioritized | High |
