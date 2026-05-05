---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/billing.md
source_url: https://ai.google.dev/gemini-api/docs/billing
title: "Gemini API — Billing"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Gemini API Billing

Source is in Vietnamese (crawler localization).

## Billing Tiers

| Tier | Qualification | Spend Cap |
|---|---|---|
| Free | Active project or free trial | N/A |
| Tier 1 | Link an active billing account | HKD amount (initial) |
| Tier 2 | $100 paid + 3 days since first successful payment | $2,000 |
| Tier 3 | $1,000 paid + 30 days since first successful payment | $20,000–$100,000+ |

- New accounts start at Free tier with access to limited models up to Free tier rate limits.
- Paid tier: higher rate limits, advanced models, prompts/responses NOT used to improve Google products.

## Setup Process

1. Go to AI Studio API Keys or Projects page.
2. Find the free project to upgrade → click "Set up billing".
3. Link a billing account (new or existing Google billing account).
4. Prepay minimum $10 (or equivalent currency) to activate Tier 1.

## Billing Plans

- **Prepay**: Add credits to account; API only processes requests with positive credit balance.
- **Postpay**: Available at Tier 3; pay after usage.

## Tier Upgrade

Automatic when spending/account age criteria are met (with processing time).

## Monitoring Usage

Track via Google AI Studio → Dashboard → Usage. Also visible in Google Cloud Console billing.

## Spend Caps

Account-level spending limits per tier to prevent unexpected charges. Can be adjusted.

## Payment Methods

- Standard Google Cloud payment methods (credit card, bank account, etc.).
- Prepay credits work like a balance — reduce as you use the API.

## Notes

- Billing is at the Cloud billing account level, not per project.
- Free tier data used to improve Google products; paid tier data is NOT.
- Processing times for tier upgrades may vary.
