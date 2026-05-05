---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/priority-inference.md
source_url: https://ai.google.dev/gemini-api/docs/priority-inference
title: "Gemini API — Priority Inference"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Priority Inference

Source is in Japanese (crawler localization).

## Overview

Priority inference is a premium tier designed for business-critical workloads requiring low latency and highest reliability. Priority tier traffic is routed before standard API and Flex tier traffic.

## Availability

Available for **Tier 2 and Tier 3** users on `GenerateContent` and `Interactions` API endpoints.

## Usage

Set `service_tier: "priority"` in request config:

```python
from google import genai
client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents="Triage this critical customer support ticket immediately.",
        config={"service_tier": "priority"},
    )

    # Validate for graceful downgrade
    if response.sdk_http_response.headers.get("x-gemini-service-tier") == "standard":
        print("Warning: Priority limit exceeded, processed at Standard tier.")

    print(response.text)

except Exception as e:
    print(f"Error during API call: {e}")
```

## Graceful Downgrade

If priority capacity limit is exceeded, the request gracefully downgrades to standard tier (no error thrown). Check the `x-gemini-service-tier` response header to confirm which tier was used.

## Pricing

Priority tier costs ~75–100% premium above standard pricing. See `pricing.md` for current rates.

## Comparison with Other Tiers

| Tier | Cost | Latency | Reliability | Interface |
|---|---|---|---|---|
| Standard | Full price | Normal | High | Sync |
| Flex | 50% discount | Variable | Preemptible | Sync |
| Priority | 75–100% premium | Low | Highest | Sync |
| Batch | 50% discount | Up to 24h | High | Async |
