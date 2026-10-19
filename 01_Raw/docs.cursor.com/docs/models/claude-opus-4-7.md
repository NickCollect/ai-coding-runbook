---
source_url: https://cursor.com/docs/models/claude-opus-4-7
fetched_at: 2026-10-19T05:32:45.136325+00:00
fetch_method: mintlify_md
---

We recommend using [Claude Opus 5.5](https://cursor.com/docs/models/claude-opus-5-5.md). It is Anthropic's latest Opus release with lower pricing and stronger agentic capabilities.

Opus 4.7 is Anthropic's strongest model and a meaningful jump over Opus 4.6 on [CursorBench](https://cursor.com/blog/cursorbench). It excels at autonomous, multi-step work: it holds intent across long sessions, self-corrects when it hits friction, and writes production-ready code without hand-holding. We recommend the high thinking variant for the best results.

## Strengths

- Autonomous and self-directed. Opus 4.7 drives multi-step tasks to completion without losing track of the goal, even across large codebases and long conversations.
- Creative reasoning. It approaches problems from unexpected angles, explores alternative solutions, and produces more inventive code than its predecessor.
- Strong at planning. It maps out work before executing, catches edge cases early, and builds coherent architectures across many files.
- Reliable tool use. It calls tools purposefully, chains tool results into follow-up actions, and adapts when tool output surprises it.

## Limitations

- Most expensive model. Consumes usage limits faster than alternatives.
- Can over-elaborate in long sessions where brevity matters more than depth.

## Tools

Opus 4.7 has access to all agent tools when used with Cursor including:

Learn more about [how tools work](https://cursor.com/docs/agent/overview.md#tools) and [tool calling fundamentals](https://cursor.com/learn/tool-calling.md).

## Pricing

Opus 4.7 is a third-party model, so it isn't part of the usage included with Cursor [plans](https://cursor.com/docs/models-and-pricing.md#third-party-models). On The X Subscription it's billed at the rates below from your prepaid credit. On legacy Cursor plans it draws from the **Other Models** pool. All prices are per million tokens.

All Opus 4.7 prompts bill at the base per-token rates in the table above, including when context goes above 300k. There is no separate long-context multiplier for Opus 4.7. Context windows up to 1M tokens use the same rates.

Opus 4.7 supports a thinking variant for deeper reasoning. We recommend using the high thinking variant for the strongest results.


---

## Sitemap

[Overview of all docs pages](/llms.txt)
