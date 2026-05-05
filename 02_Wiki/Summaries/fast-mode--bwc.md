---
type: summary
source: 01_Raw/platform.claude.com/docs/en/build-with-claude/fast-mode.md
source_url: https://platform.claude.com/docs/en/build-with-claude/fast-mode
title: "Fast mode (beta: research preview)"
summarized_at: 2026-05-05
entities_referenced: [Fast-mode, Messages-API, Prompt-caching]
concepts_referenced: []
---

Fast mode is a beta research-preview feature delivering **up to 2.5× higher output tokens per second** for the same Claude Opus 4.6 model at premium pricing. Same model weights, same intelligence, faster inference config. Waitlist gated. ZDR-eligible.

## Supported model

Claude Opus 4.6 (`claude-opus-4-6`) only.

## Enabling

- Header: `anthropic-beta: fast-mode-2026-02-01`
- Body: `speed: "fast"`

## Behavior

- Speed gain focused on **output tokens per second (OTPS)**, not time-to-first-token (TTFT).
- Response `usage.speed` reports `"fast"` or `"standard"`.

## Pricing

| Input | Output |
|---|---|
| $30 / MTok | $150 / MTok |

= 6× standard Opus 4.6 rates across the full context window (including >200k input requests).

Stacks with:
- Prompt caching multipliers
- Data residency multipliers

## Rate limits

Dedicated, separate from standard Opus rate limits. 429 with `retry-after` when exceeded. Headers:
- `anthropic-fast-input-tokens-{limit, remaining, reset}`
- `anthropic-fast-output-tokens-{limit, remaining, reset}`
