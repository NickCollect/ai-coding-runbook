---
type: summary
source: 01_Raw/platform.claude.com/docs/en/build-with-claude/adaptive-thinking.md
source_url: https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking
title: "Adaptive thinking"
summarized_at: 2026-05-05
entities_referenced: [Adaptive-thinking, Extended-thinking, Effort, Messages-API, Streaming-API, Prompt-caching, Tool-use, Context-editing, Enterprise-gateway]
concepts_referenced: [Context-window]
---

Adaptive thinking lets Claude dynamically decide whether and how much extended thinking to use per request. ZDR-eligible. The recommended thinking mode on Claude Opus 4.7, Opus 4.6, and Sonnet 4.6, and the default on Claude Mythos Preview when `thinking` is unset. No beta header required.

## Key facts

- **Config:** `thinking: {type: "adaptive"}` in the Messages API body.
- **Opus 4.7:** adaptive is the **only** supported thinking mode. Manual `thinking: {type: "enabled", budget_tokens: N}` returns 400. Thinking is off unless `adaptive` is set explicitly.
- **Mythos Preview:** adaptive is default; `{type: "disabled"}` not supported.
- **Opus 4.6 / Sonnet 4.6:** manual `enabled`+`budget_tokens` still works but is **deprecated**.
- **Older models (Sonnet 4.5, Opus 4.5, etc.):** require manual `enabled` mode.
- Adaptive **automatically enables interleaved thinking** (think between tool calls) — useful for agentic workflows. On Mythos Preview / Opus 4.7, inter-tool reasoning always lives in thinking blocks.

## Effort levels (soft guidance)

| Effort | Behavior |
|---|---|
| `max` | Always thinks, no depth constraint (Mythos, Opus 4.7, Opus 4.6, Sonnet 4.6) |
| `xhigh` | Always thinks deeply with extended exploration (Opus 4.7 only) |
| `high` (default) | Always thinks |
| `medium` | Moderate; may skip simple queries |
| `low` | Minimizes thinking; skips for simple tasks |

## Mode comparison

| Mode | Config | Notes |
|---|---|---|
| Adaptive | `{type: "adaptive"}` | Mythos default; Opus 4.7 only mode |
| Manual | `{type: "enabled", budget_tokens: N}` | Rejected on Opus 4.7; deprecated on Opus/Sonnet 4.6 |
| Disabled | omit / `{type: "disabled"}` | All except Mythos |

## Considerations

- **Validation:** previous assistant turns don't need to start with thinking blocks (more flexible than manual).
- **Prompt caching:** consecutive adaptive requests preserve cache breakpoints; switching between adaptive and enabled/disabled breaks message cache breakpoints (system prompts and tools remain cached).
- **Tunable via system prompt** — can steer Claude to think less/more.
- **Cost control:** `max_tokens` is hard cap on thinking + text; high/max effort may exhaust budget — watch for `stop_reason: "max_tokens"`.
- **Streaming:** thinking blocks stream via `thinking_delta` events.

## Thinking display & encryption

- `display: "summarized"` — returns a summary (default on Opus 4.6, Sonnet 4.6).
- `display: "omitted"` — empty `thinking` field; only `signature` returned. Default on Opus 4.7 and Mythos Preview. Faster TTFT when streaming. Still billed for full thinking tokens.
- `signature` is opaque, encrypted, identical across `summarized`/`omitted`, and compatible across Anthropic API, Bedrock, Vertex.
- Pass thinking blocks back unchanged for tool-use multi-turn. Opus 4.5+ and Sonnet 4.6+ keep them in context by default; older Opus/Sonnet and all Haiku strip them — see context editing.

## Pricing

- Billed for full original thinking tokens, not summary tokens.
- Visible token count won't match billed count.
- Summary generation itself is free; summarization runs on a different model.
