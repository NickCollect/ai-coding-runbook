---
source_url: https://cursor.com/docs/models/muse-spark-1-3
fetched_at: 2026-09-14T05:36:11.054229+00:00
fetch_method: mintlify_md
---

Meta is a new model provider in Cursor. Teams and Enterprise admins who
configured [model access](https://cursor.com/docs/enterprise/model-and-integration-management.md#model-access-control)
before Meta was available need to enable the Meta provider before Muse Spark
1.3 appears for their members.

Muse Spark 1.3 is Meta's flagship model and the first Meta model available in Cursor. It is built for agentic coding: long tool-use chains, multi-step debugging, and large-repository work.

## Strengths

- Six effort levels: minimal, low, medium, high (the default), extra high, and max. Higher efforts spend more reasoning tokens per step and score higher on [CursorBench](https://cursor.com/cursorbench); drop to low or minimal for faster, cheaper responses on simpler tasks.
- 300k token context window, or 1M in Max Mode at the same per-token rates.
- Low per-token price for a flagship model: $1.25 per million input tokens and $4.25 per million output tokens.

## Tools

Muse Spark 1.3 has access to all agent tools when used with Cursor including:

Learn more about [how tools work](https://cursor.com/docs/agent/overview.md#tools) and [tool calling fundamentals](https://cursor.com/learn/tool-calling.md).

## Pricing

Cursor [plans](https://cursor.com/docs/models-and-pricing.md) include two usage pools. Muse Spark 1.3 draws from the third-party **Other Models** pool, which charges at the rates below. All prices are per million tokens.

Prompts bill at the base per-token rates above, including in Max Mode above 300k tokens. Cached input is billed at $0.15 per million tokens; there is no long-context multiplier and no cache-write charge.

## Data retention

Muse Spark 1.3 runs under Cursor's standard provider terms. See Meta's [zero data retention policy](https://dev.meta.ai/help/policies-and-privacy/zero-data-retention) and Cursor's [data use overview](https://cursor.com/data-use).


---

## Sitemap

[Overview of all docs pages](/llms.txt)
