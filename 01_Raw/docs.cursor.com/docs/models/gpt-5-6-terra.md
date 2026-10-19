---
source_url: https://cursor.com/docs/models/gpt-5-6-terra
fetched_at: 2026-10-19T05:32:46.156807+00:00
fetch_method: mintlify_md
---

GPT-5.6 Terra is the mid-tier model in OpenAI's GPT-5.6 family. It sits between Sol and Luna on intelligence and price, making it a strong pick for everyday agentic coding when you want more capability than Luna without Sol's cost.

## Strengths

- Solid multi-step coding and tool use at well under Sol's per-token price.
- Faster and cheaper than Sol for routine agent workflows.
- Same GPT-5.6 family behavior: reasoning, tool calling, and agent loops.

## Limitations

- Not the peak of the GPT-5.6 family. For the hardest long-running tasks, [GPT-5.6 Sol](https://cursor.com/docs/models/gpt-5-6-sol.md) is the stronger pick.
- Less capacity for open-ended reasoning chains than Sol.

## Tools

GPT-5.6 Terra has access to all agent tools when used with Cursor including:

Learn more about [how tools work](https://cursor.com/docs/agent/overview.md#tools) and [tool calling fundamentals](https://cursor.com/learn/tool-calling.md).

## Pricing

GPT-5.6 Terra is a third-party model, so it isn't part of the usage included with Cursor [plans](https://cursor.com/docs/models-and-pricing.md#third-party-models). On The X Subscription it's billed at the rates below from your prepaid credit. On legacy Cursor plans it draws from the **Other Models** pool. All prices are per million tokens.

A **Fast mode** tier (`gpt-5.6-terra-fast`) is available for priority processing at 2x the standard rates.

When input exceeds 272k tokens (long context), input pricing doubles and output pricing is 1.5x the standard rate. The same multipliers apply in Fast mode: long-context requests bill at 2x the Fast input, cache write, and cache read rates, and 1.5x the Fast output rate.


---

## Sitemap

[Overview of all docs pages](/llms.txt)
