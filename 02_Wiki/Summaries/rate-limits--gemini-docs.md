---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/rate-limits.md
source_url: https://ai.google.dev/gemini-api/docs/rate-limits
title: "Gemini API — Rate Limits"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Gemini API Rate Limits

Source is in Arabic (crawler localization).

## How Rate Limits Work

Rate limits are measured across three dimensions simultaneously:
- **RPM** (Requests Per Minute)
- **TPM** (Tokens Per Minute, input)
- **RPD** (Requests Per Day)

Exceeding ANY single limit triggers a rate limit error (429 RESOURCE_EXHAUSTED). Rate limits are **per project**, not per API key. RPD quotas reset at midnight Pacific Time.

Limits vary by model and are more restrictive for experimental and preview models. Some models have additional metrics (e.g., IPM — Images Per Minute for Nano Banana).

## Tier Structure

| Tier | Qualification | Spend Cap |
|---|---|---|
| Free | Active project or free trial | N/A |
| Tier 1 | Link active billing account | $250 |
| Tier 2 | $100 paid + 3 days since first payment | $2,000 |
| Tier 3 | $1,000 paid + 30 days since first payment | $20,000–$100,000+ |

Higher tiers = higher rate limits. Tier qualification based on cumulative Google Cloud spend (including all services).

## Handling Rate Limits

- Implement exponential backoff on 429 errors
- Use Batch API for non-urgent, high-volume workloads
- Cache frequently-used large context to reduce token usage
- Monitor active rate limits: `aistudio.google.com/rate-limit`

## Requesting Limit Increases

For higher limits beyond tier quotas, request a rate limit increase through AI Studio or Google Cloud support.

## Model-Specific Limits

Exact RPM/TPM/RPD numbers depend on the specific model and billing tier. See current limits at: `aistudio.google.com/rate-limit`
