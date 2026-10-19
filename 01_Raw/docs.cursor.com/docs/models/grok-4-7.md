---
source_url: https://cursor.com/docs/models/grok-4-7
fetched_at: 2026-10-19T05:32:46.271420+00:00
fetch_method: mintlify_md
---

Grok 4.7 is a frontier model from Cursor and SpaceXAI for coding and knowledge work. It builds on Grok 4.6 with a larger base, longer training on harder multi-hour tasks, and stronger self-verification.

## Strengths

- Stays with difficult, long-running work and checks its own results more carefully than Grok 4.6.
- Manages longer context more reliably, with a 256k standard window and 500k long context.
- Stronger on complex coding and multi-hour knowledge work.

## Effort levels

Grok 4.7 supports four effort levels: xhigh, high (default), medium, and low. Higher effort gives the model more time to work through difficult tasks. Effort levels are more separated than in Grok 4.6, so harder tasks spend more time thinking.

Fast is the default speed tier on Premium and higher, and on the legacy Pro, Pro+, and Ultra plans. On Plus and on the legacy [Start plan](https://cursor.com/docs/account/pricing/legacy-cursor-plans.md#start-india-only) (India only), Grok 4.7 is fixed at medium effort at standard speed.

## Tools

Grok 4.7 has access to all agent tools when used with Cursor, including:

Learn more about [how tools work](https://cursor.com/docs/agent/overview.md#tools) and [tool calling fundamentals](https://cursor.com/learn/tool-calling.md).

## Pricing

Grok 4.7 draws from the weekly pool of [Cursor models](https://cursor.com/docs/models-and-pricing.md#cursor-models) included with every paid plan, alongside Grok 4.6, Grok 4.5, and Composer 2.5. On [legacy Cursor plans](https://cursor.com/docs/account/pricing/legacy-cursor-plans.md), it draws from the monthly Cursor Models pool.

Additional usage beyond the pool at standard speed is priced at $2/M input tokens, $0.50/M cached input tokens, and $6/M output tokens. Fast is $4/M input, $1/M cached, and $12/M output. When input exceeds 256k tokens, standard requests bill at 2x those rates and Fast requests bill at 3x the standard rates, up to a 500k context window. Long-context billing uses the input length only: if input is at or below 256k tokens, the full request uses the standard or Fast rates. All prices are per million tokens.


---

## Sitemap

[Overview of all docs pages](/llms.txt)
