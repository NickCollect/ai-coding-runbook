---
source_url: https://cursor.com/docs/models/muse-wonder
fetched_at: 2026-10-19T05:32:46.321733+00:00
fetch_method: mintlify_md
---

Teams and Enterprise admins who configured
[model access](https://cursor.com/docs/enterprise/model-and-integration-management.md#model-access-control)
before Meta was available need to enable the Meta provider before Muse
Wonder appears for their members.

Muse Wonder is Meta's flagship model and the successor to [Muse Spark 1.3](https://cursor.com/docs/models/muse-spark-1-3.md) in Cursor. It is built for agentic coding: long tool-use chains, multi-step debugging, and large-repository work.

## Strengths

- Six effort levels: minimal, low, medium, high (the default), extra high, and max. Higher efforts spend more reasoning tokens per step and score higher on [CursorBench](https://cursor.com/cursorbench); drop to low or minimal for faster, cheaper responses on simpler tasks.
- 300k token context window, or 1M in Max Mode at the same per-token rates.
- Image input, including screenshots returned by tools.

## Tools

Muse Wonder has access to all agent tools when used with Cursor including:

Learn more about [how tools work](https://cursor.com/docs/agent/overview.md#tools) and [tool calling fundamentals](https://cursor.com/learn/tool-calling.md).

## Pricing

Muse Wonder is a third-party model, so it isn't part of the usage included with Cursor [plans](https://cursor.com/docs/models-and-pricing.md#third-party-models). On The X Subscription it's billed at the rates below from your prepaid credit. On legacy Cursor plans it draws from the **Other Models** pool. All prices are per million tokens.

Prompts bill at the base per-token rates above, including in Max Mode above 300k tokens. Cached input is billed at $0.20 per million tokens; there is no long-context multiplier and no cache-write charge.

## Data retention

Muse Wonder runs under Cursor's standard provider terms. See Meta's [zero data retention policy](https://dev.meta.ai/help/policies-and-privacy/zero-data-retention) and Cursor's [data use overview](https://cursor.com/data-use).


---

## Sitemap

[Overview of all docs pages](/llms.txt)
