---
type: summary
source: 01_Raw/platform.claude.com/docs/en/build-with-claude/effort.md
source_url: https://platform.claude.com/docs/en/build-with-claude/effort
title: "Effort"
summarized_at: 2026-05-05
entities_referenced: [Effort, Adaptive-thinking, Extended-thinking, Tool-use, Messages-API]
concepts_referenced: []
---

The `effort` parameter controls how eager Claude is to spend tokens — trades thoroughness vs token efficiency with one model. GA, no beta header. ZDR-eligible. Set inside `output_config.effort`. Affects **all output tokens**: text, tool calls, and extended thinking. Replaces deprecated `budget_tokens` for thinking on Opus 4.6 / Sonnet 4.6.

## Supported models

Claude Mythos Preview, Claude Opus 4.7, Claude Opus 4.6, Claude Sonnet 4.6, Claude Opus 4.5.

## Effort levels

| Level | Notes |
|---|---|
| `max` | Max capability, no cost constraint. (Mythos, Opus 4.7, Opus 4.6, Sonnet 4.6) |
| `xhigh` | Long-horizon agentic / coding (>30 min, millions of tokens). **Opus 4.7 only**. |
| `high` (default) | Same as omitting parameter. |
| `medium` | Balanced. |
| `low` | Most efficient; some capability reduction. |

Effort is a **behavioral signal, not a strict budget** — Claude still thinks on hard problems at low effort, just less.

## Recommended for Sonnet 4.6

Default is `high`. Set explicitly to avoid latency surprises.
- **Medium** (recommended default): balance for agentic coding, tool-heavy workflows.
- **Low:** high-volume, latency-sensitive (chat, non-coding).
- **High:** max intelligence for Sonnet 4.6.
- **Max:** absolute highest with no cost cap.

## Recommended for Opus 4.7

Default `high`. Set `xhigh` explicitly.
- **xhigh** is the recommended starting point for coding and agentic work, repeated tool calling, detailed web/KB search.
- **high:** balance of intelligence and tokens — often the sweet spot.
- **medium:** drop-in for average workflow with cost reduction.
- **low:** short scoped tasks; pair with explicit checklists for multi-section tasks.
- **max:** reserve for frontier problems — risk of overthinking on structured outputs / less-intelligence-sensitive tasks.

Opus 4.7 respects effort more strictly than Opus 4.6 (especially low/medium): scopes work to what's asked. If shallow reasoning seen, raise effort rather than prompting around. At `xhigh`/`max`, set large `max_tokens` (start ~64k) for room across subagents/tool calls.

## Why effort over thinking-only knobs

1. Doesn't require thinking enabled.
2. Affects all token spend including tool-call frequency.
