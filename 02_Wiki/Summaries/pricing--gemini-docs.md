---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/pricing.md
source_url: https://ai.google.dev/gemini-api/docs/pricing
title: "Gemini API — Pricing"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Gemini API Pricing

Source is in Italian (crawler localization). All prices in USD per 1M tokens unless noted.

## Tiers

- **Free** (Senza costi): Limited model access, free input/output tokens, data used to improve products, access to Google AI Studio.
- **Paid** (A pagamento): Higher rate limits, context caching, Batch API (50% discount), advanced models, data NOT used to improve products.
- **Enterprise**: Via Gemini Enterprise Agent Platform — dedicated support, advanced security, reserved throughput, volume discounts.

## Model Pricing (Paid tier, per 1M tokens)

### Gemini 3.x Series

| Model | Input (≤200k / >200k) | Output (incl. thinking) |
|---|---|---|
| gemini-3.1-pro-preview | $2 / $4 | $12 / $18 |
| gemini-3.1-flash-lite-preview | $0.25 text/img/vid; $0.50 audio | $1.50 |
| gemini-3.1-flash-live-preview (Live API) | $0.75 text; $3 audio; $1 img/video | $4.50 text; $12 audio |
| gemini-3.1-flash-image-preview | $0.50 text/img input | $3 text; $60 image output |
| gemini-3.1-flash-tts-preview | $1.00 message | $20.00 audio |
| gemini-3-flash-preview | $0.50 text/img/vid; $1 audio | $3.00 |
| gemini-3-pro-image-preview | $2 text/img input | $12 text; $120 image output |

### Gemini 2.5 Series

| Model | Input | Output |
|---|---|---|
| gemini-2.5-pro | $1.25 / $2.50 (≤200k / >200k) | $10 / $15 |
| gemini-2.5-flash | $0.30 text/img/vid; $1 audio | $2.50 |
| gemini-2.5-flash-lite | $0.10 text/img/vid; $0.30 audio | $0.40 |
| gemini-2.5-flash-preview-tts | $0.50 text | $10.00 audio |
| gemini-2.5-pro-preview-tts | $1.00 text | $20.00 audio |
| gemini-2.5-flash-native-audio-preview (Live) | $0.50 text; $3 audio/video | $2 text; $12 audio |
| gemini-2.5-flash-image | $0.30 text/img | $0.039/image |

### Gemini 2.0 Series

| Model | Input | Output |
|---|---|---|
| gemini-2.0-flash | $0.10 text/img/vid; $0.70 audio | $0.40 |
| gemini-2.0-flash-lite | $0.075 | $0.30 |

### Specialized Models

| Model | Pricing |
|---|---|
| gemini-embedding-2 | $0.20/1M text; $0.45/1M image; $6.50/1M audio; $12/1M video |
| gemini-embedding-001 | $0.15/1M text |
| Imagen 4 Fast | $0.02/image |
| Imagen 4 Standard | $0.04/image |
| Imagen 4 Ultra | $0.06/image |
| Veo 3.1 (standard) | $0.40/sec (720p/1080p), $0.60/sec (4K) |
| Veo 3.1 Fast | $0.10/sec (720p), $0.12/sec (1080p), $0.30/sec (4K) |
| Veo 3.1 Lite | $0.05/sec (720p), $0.08/sec (1080p) |
| Veo 3 (standard) | $0.40/sec |
| Veo 2 | $0.35/sec |
| Lyria 3 Clip (30s) | $0.04/track |
| Lyria 3 Pro (full track) | $0.08/track |
| gemini-robotics-er-1.6-preview | $1 input; $5 output |
| gemini-2.5-computer-use-preview | $1.25/$2.50 input; $10/$15 output |
| Gemma 4 | Free only (no paid tier) |

## Inference Modes

- **Standard**: Full price, default.
- **Batch API**: ~50% of standard price. Async, higher latency acceptable.
- **Flex**: ~50% of standard price. Variable latency.
- **Priority**: ~180% of standard price. Higher throughput SLA.

## Context Caching Storage Cost

- Gemini 2.5 Pro / 3.1 Pro: $4.50/1M tokens/hour
- Gemini 2.5 Flash / 3 Flash: $1.00/1M tokens/hour
- Gemini 2.5 Flash-Lite: $1.00/1M tokens/hour

## Tool Pricing

| Tool | Free | Paid |
|---|---|---|
| Google Search Grounding (Gemini 2.5) | 500 RPD (Flash/Flash-Lite shared) | 1500 RPD free, then $35/1000 prompts |
| Google Search Grounding (Gemini 3) | — | 5000/month free, then $14/1000 queries |
| Google Maps Grounding | 500 RPD | 1500 RPD free (Flash), then $25/1000 prompts |
| Code Execution | Free | Billed as standard tokens |
| URL Context | Free | Billed as input tokens |
| File Search | Free | $0.15/1M tokens (embedding) + normal model tokens |

## Notes

- Free tier data is used to improve Google products; Paid tier data is NOT.
- Batch API saves 50% but is asynchronous.
- Dynamic retrieval: only charged for Search Grounding when at least one grounding URL appears in response.
- Google AI Studio usage is free in all available regions.
