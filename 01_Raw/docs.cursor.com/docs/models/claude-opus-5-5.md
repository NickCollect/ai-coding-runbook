---
source_url: https://cursor.com/docs/models/claude-opus-5-5
fetched_at: 2026-10-05T06:27:21.507916+00:00
fetch_method: mintlify_md
---

Claude Opus 5.5 is Anthropic's latest Opus model and replaces [Opus 5](https://cursor.com/docs/models/claude-opus-5.md). It sets a new high score on [CursorBench](https://cursor.com/cursorbench), ahead of Fable 5.1, and costs 20% less than Opus 5 per token. We recommend the high thinking variant for the best results.

## Strengths

- Highest CursorBench score of any model in Cursor at launch, at standard Opus pricing rather than Fable pricing.
- Clearer communication than earlier Opus models. It explains what it did and why without over-elaborating, which makes long agent sessions easier to follow.
- Strong at front-end and UI work. Early testers used it to design and build complete interfaces from scratch.
- Works well as a coordinator for [subagents](https://cursor.com/docs/subagents.md). It delegates cleanly and keeps the parent task on track across long runs.
- Zero Data Retention compatible. Like earlier Opus models, and unlike Fable 5.1, Opus 5.5 has no data-retention requirements for general access. Teams using ZDR with Opus today can keep that setup with Opus 5.5.

## Limitations

- Still an Opus-tier price. It consumes the Other Models pool faster than [Sonnet 5.5](https://cursor.com/docs/models/claude-sonnet-5-5.md) or Composer.

## Tools

Opus 5.5 has access to all agent tools when used with Cursor including:

Learn more about [how tools work](https://cursor.com/docs/agent/overview.md#tools) and [tool calling fundamentals](https://cursor.com/learn/tool-calling.md).

## Pricing

Cursor [plans](https://cursor.com/docs/models-and-pricing.md) include two usage pools. Opus 5.5 draws from the third-party **Other Models** pool, which charges at the rates below. All prices are per million tokens.

Opus 5.5 bills at $4 per million input tokens and $20 per million output tokens, down from $5 and $25 for Opus 5. Prompt-cache reads are $0.20 per million tokens (0.05x the input rate), down from 0.10x on Opus 5.

A **Fast mode** tier (`claude-opus-5-5-fast`) is available at launch for higher-priority output. On legacy request-based plans, it requires Max Mode. It bills at $8/M input and $40/M output tokens. Use it selectively for time-sensitive or critical work.

Global endpoints use the rates above. Regional and US-only endpoints are priced 10% higher, at $4.40/M input and $22/M output tokens. See [Privacy and Data Governance](https://cursor.com/docs/enterprise/privacy-and-data-governance.md) for data residency details.

All Opus 5.5 prompts bill at the base per-token rates in the table above, including when context goes above 300k. There is no separate long-context multiplier for Opus 5.5. Context windows up to 1M tokens use the same rates.

Opus 5.5 supports a thinking variant for deeper reasoning. We recommend using the high thinking variant for the strongest results.


---

## Sitemap

[Overview of all docs pages](/llms.txt)
