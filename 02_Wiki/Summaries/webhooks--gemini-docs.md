---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/webhooks.md
source_url: https://ai.google.dev/gemini-api/docs/webhooks
title: "Gemini API — Webhooks"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Gemini API Webhooks

Source is in Simplified Chinese (crawler localization).

## Overview

Webhooks allow Gemini API to push real-time notifications to your server when async or long-running operations (LRO) complete. Eliminates need for polling `GET /operations`.

Applicable to: Batch API jobs, Interactions API, Video generation.

## Two Webhook Types

### Static Webhooks
Project-level endpoints registered via the Gemini `WebhookService` API. Fire for all matching events globally.

**Key constraint**: The signing key is only returned once at creation. Store it securely (e.g., env variable). If lost, must rotate.

```python
from google import genai
client = genai.Client()
# Create via client.webhooks.create(url=..., display_name=...)
```

### Dynamic Webhooks
Request-level overrides — pass webhook URL in the config payload of a specific job. Routes specific jobs to dedicated endpoints.

## How Webhooks Work

1. Register webhook URL (static or dynamic per-request).
2. Gemini sends HTTP POST to your listener URL when event fires.
3. Payload includes operation state and result.
4. Validate signature using your stored signing key.

## Signature Validation

Each POST includes a signature header. Validate to ensure the request is from Gemini (not a spoofed request).

## Use Cases

- Batch API: Get notified when large batch jobs complete.
- Interactions API: Notification on long conversation tasks.
- Video generation: Notification when async `generate_videos` completes.
