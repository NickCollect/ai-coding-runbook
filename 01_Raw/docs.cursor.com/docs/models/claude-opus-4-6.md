---
source_url: https://cursor.com/docs/models/claude-opus-4-6
fetched_at: 2026-05-05T19:55:41.109718+00:00
fetch_method: mintlify_md
---

We recommend using [Claude 4.7 Opus](https://cursor.com/docs/models/claude-opus-4-7.md). It scores higher on [CursorBench](https://cursor.com/blog/cursorbench), offers stronger autonomous capabilities, and is priced the same.

Opus 4.6 is Anthropic's previous flagship model. It tracks conversation intent across many turns and maintains coherent reasoning throughout long sessions. It plans before it acts, produces concrete fixes, and writes idiomatic code with strong style.

## Strengths

- Plans upfront and reasons coherently across many conversation turns. Strong for system design, complex refactors, and code reviews.
- Handles log-heavy, multi-project troubleshooting across CI, Docker, and monitoring.
- Writes idiomatic code with strong architecture decisions. Preferred for code reviews and production-critical changes.
- Tracks your intent across the full conversation. Strongest when prior context matters.
- Produces concrete bugfixes and feature work that spans multiple components.

## Limitations

- Most expensive model. Consumes usage limits faster than alternatives.
- Can over-elaborate or drift context in long sessions.
- Sometimes overconfident when given limited context.

## Tools

Opus 4.6 has access to all agent tools when used with Cursor including:

Learn more about [how tools work](https://cursor.com/docs/agent/overview.md#tools) and [tool calling fundamentals](https://cursor.com/learn/tool-calling.md).

## Pricing

Cursor [plans](https://cursor.com/docs/models-and-pricing.md) include two usage pools. Opus 4.6 draws from the **API** pool, which charges at the rates below. Individual plans include at least $20 of API usage each month (more on higher tiers). All prices are per million tokens.

All Opus 4.6 prompts bill at the base per-token rates in the table above, including when you use Max Mode and context goes above 200k. Anthropic no longer applies a separate long-context multiplier for Opus 4.6.

Opus 4.6 supports a thinking variant for deeper reasoning.


---

## Sitemap

[Overview of all docs pages](/llms.txt)
