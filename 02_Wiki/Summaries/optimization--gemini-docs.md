---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/optimization.md
source_url: https://ai.google.dev/gemini-api/docs/optimization
title: "Gemini API — Inference and Optimization"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Gemini API Inference and Optimization

Source is in Italian (crawler localization).

## Overview

Gemini API offers multiple optimization mechanisms to balance speed, cost, and reliability for different workload needs.

## Comparison Table

| Feature | Standard | Flex | Priority | Batch | Caching |
|---|---|---|---|---|---|
| **Price** | Full price | 50% discount | 75–100% premium | 50% discount | 90% discount + proportional storage |
| **Latency** | Seconds–minutes | Minutes (target 1–15 min) | Seconds | Up to 24 hours | Faster TTFT |
| **Reliability** | High/medium-high | Best-effort (preemptible) | High (non-preemptible) | High (throughput) | N/A |
| **Interface** | Synchronous | Synchronous | Synchronous | Asynchronous | Saved state |
| **Ideal for** | General app workflows | Non-urgent sequential chains | User-facing production apps | Large datasets, offline evaluations | Recurring queries on same file |

## Service Tiers

### Standard (Default)
Full price, normal response times, standard reliability. Most interactive applications.

### Flex (Cost-optimized)
50% discount. Variable latency, preemptible (may fail). Set `service_tier: "flex"`. For latency-tolerant batch-like synchronous work.

### Priority (Latency-optimized)
75–100% premium. Routes to high-priority compute queues, non-preemptible. Highest reliability. If over dynamic priority limits, gracefully downgrades to standard (no error). For: customer chatbots, real-time fraud detection, mission-critical copilots.

### Batch (Async, cost-optimized)
50% discount, asynchronous, up to 24h response time. For offline processing.

### Context Caching (Repeated-context optimization)
~90% discount on cached tokens + storage cost. For repeated queries reusing the same large context.

## Choosing the Right Tier

- **Conversational apps**: Standard or Priority
- **Data pipelines, non-urgent**: Flex or Batch
- **Same document queried repeatedly**: Context Caching
- **Cost-sensitive real-time**: Flex (with fallback handling)
