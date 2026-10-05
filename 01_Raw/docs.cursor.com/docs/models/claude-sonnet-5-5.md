---
source_url: https://cursor.com/docs/models/claude-sonnet-5-5
fetched_at: 2026-10-05T06:27:21.559028+00:00
fetch_method: mintlify_md
---

Claude Sonnet 5.5 is Anthropic's latest medium-tier model and the successor to [Sonnet 5](https://cursor.com/docs/models/claude-sonnet-5.md). It scores 55.5% on [CursorBench](https://cursor.com/cursorbench) at max effort, second only to [Opus 5.5](https://cursor.com/docs/models/claude-opus-5-5.md), and keeps Sonnet 5's per-token price. Add it to the model picker from **Cursor Settings > Models**.

## Strengths

- Frontier-level CursorBench results at Sonnet pricing. It sits on the same cost-performance frontier as Opus 5.5.
- Scales with effort. Its score climbs from 35.8% at low effort to 55.5% at max, so you can trade tokens for quality on harder tasks.
- Supports thinking mode and context windows up to 1M tokens.

## Limitations

- For peak quality on the hardest tasks, [Opus 5.5](https://cursor.com/docs/models/claude-opus-5-5.md) remains the stronger choice.
- Higher effort levels use many more tokens. On CursorBench, max effort costs about 6x more per task than the default high effort.

## Tools

Sonnet 5.5 has access to all agent tools when used with Cursor including:

Learn more about [how tools work](https://cursor.com/docs/agent/overview.md#tools) and [tool calling fundamentals](https://cursor.com/learn/tool-calling.md).

## Pricing

Cursor [plans](https://cursor.com/docs/models-and-pricing.md) include two usage pools. Sonnet 5.5 draws from the third-party **Other Models** pool, which charges at the rates below. All prices are per million tokens.

Sonnet 5.5 bills at $2 per million input tokens and $10 per million output tokens, the same as Sonnet 5. Prompt-cache reads are $0.20 per million tokens.

Global endpoints use the rates above. US-only endpoints are priced 10% higher, at $2.20/M input and $11/M output tokens. See [Privacy and Data Governance](https://cursor.com/docs/enterprise/privacy-and-data-governance.md) for data residency details.

All Sonnet 5.5 prompts bill at the base per-token rates in the table above, including when context goes above 200k. There is no separate long-context multiplier for Sonnet 5.5.

A thinking variant is available for deeper reasoning.


---

## Sitemap

[Overview of all docs pages](/llms.txt)
