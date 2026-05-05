# OpenAI API Pricing

<!-- source: https://openai.com/api/pricing -->

## Flagship models

| Model | Input | Cached input | Output |
|---|---|---|---|
| GPT-5.5 | $5.00/MTok | $0.50/MTok | $30.00/MTok |
| GPT-5.4 | $2.50/MTok | $0.25/MTok | $15.00/MTok |
| GPT-5.4 mini | $0.75/MTok | $0.075/MTok | $4.50/MTok |

Pricing above for context lengths under 270K tokens.

**Batch API**: -50% on inputs and outputs (async, 24h turnaround)
**Data residency**: +10%

## Multimodal models

### GPT-realtime-1.5 (voice)

| Modality | Input | Cached input | Output |
|---|---|---|---|
| Audio | $32.00/MTok | $0.40/MTok | $64.00/MTok |
| Text | $4.00/MTok | $0.40/MTok | $16.00/MTok |
| Image | $5.00/MTok | $0.50/MTok | — |

### GPT-image-2 (image generation)

| Modality | Input | Cached input | Output |
|---|---|---|---|
| Image | $8.00/MTok | $2.00/MTok | $30.00/MTok |
| Text | $5.00/MTok | $1.25/MTok | — |

## Built-in tools

| Tool | Price |
|---|---|
| Web search | $10.00 / 1k calls (search content tokens free) |
| Containers | $0.03/GB / $1.92 per 64GB per 20-min session |

## Service tiers

| Tier | Description |
|---|---|
| **Priority processing** | Reliable, high-speed, pay-as-you-go |
| **Batch API** | 50% savings, async over 24 hours |
| **Flex processing** | Lower cost, slower response, occasional unavailability. For non-production tasks. |
| **Reserved Capacity** | Enterprise, for large workloads |

## Pricing modifiers summary

- Cached input tokens: ~10% of regular input price
- Batch API: 50% off input + output
- Data residency: +10%
