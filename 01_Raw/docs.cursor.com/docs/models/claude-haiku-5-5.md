---
source_url: https://cursor.com/docs/models/claude-haiku-5-5
fetched_at: 2026-10-12T06:49:42.140674+00:00
fetch_method: mintlify_md
---

Claude Haiku 5.5 is the fastest model in Anthropic's Claude 5.5 family and the successor to [Claude 4.5 Haiku](https://cursor.com/docs/models/claude-4-5-haiku.md). It scores 48.4% on [CursorBench](https://cursor.com/cursorbench) at max effort, on the same cost-performance curve as [Sonnet 5.5](https://cursor.com/docs/models/claude-sonnet-5-5.md) and [Opus 5.5](https://cursor.com/docs/models/claude-opus-5-5.md), at a tenth of Haiku 4.5's per-token price for requests up to 100k input tokens. Add it to the model picker from **Cursor Settings > Models**.

## Strengths

- Low cost for high-volume work. Requests up to 100k input tokens bill at $0.10/M input and $0.50/M output.
- The first Haiku with effort levels. With thinking on, its CursorBench score climbs from 30.9% at low effort to 48.4% at max.
- Thinking can be turned off at low, medium, and high effort for faster, cheaper responses.
- Supports context windows up to 1M tokens.

## Limitations

- Requests above 100k input tokens bill at 5x the standard rates. Long agent sessions with large contexts cost more per token once they cross that line.
- [Sonnet 5.5](https://cursor.com/docs/models/claude-sonnet-5-5.md) and [Opus 5.5](https://cursor.com/docs/models/claude-opus-5-5.md) score higher on CursorBench for harder tasks.
- Turning thinking off lowers quality. On CursorBench it scores 22.1% to 26.2% with thinking off, compared with 30.9% to 42.3% with thinking on at the same effort levels.

## Tools

Haiku 5.5 has access to all agent tools when used with Cursor including:

Learn more about [how tools work](https://cursor.com/docs/agent/overview.md#tools) and [tool calling fundamentals](https://cursor.com/learn/tool-calling.md).

## Pricing

Cursor [plans](https://cursor.com/docs/models-and-pricing.md) include two usage pools. Haiku 5.5 draws from the third-party **Other Models** pool, which charges at the rates below. All prices are per million tokens.

Requests up to 100k input tokens bill at $0.10/M input and $0.50/M output. Prompt-cache writes are $0.125/M and cache reads are $0.01/M.

Requests above 100k input tokens (long context) bill at 5x those rates: $0.50/M input, $0.625/M cache write, $0.05/M cache read, and $2.50/M output.

A thinking variant is available for deeper reasoning.


---

## Sitemap

[Overview of all docs pages](/llms.txt)
