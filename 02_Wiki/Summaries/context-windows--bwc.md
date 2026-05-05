---
type: summary
source: 01_Raw/platform.claude.com/docs/en/build-with-claude/context-windows.md
source_url: https://platform.claude.com/docs/en/build-with-claude/context-windows
title: "Context windows"
summarized_at: 2026-05-05
entities_referenced: [Compaction, Context-editing, Extended-thinking, Adaptive-thinking, Token-counting, Memory-tool, PDF-support, Vision]
concepts_referenced: [Context-window, Tool-use]
---

The context window is Claude's working memory — all text the model can reference (input + output). ZDR-eligible. Bigger isn't automatically better: as token count grows, accuracy and recall degrade (*context rot*), so curating context matters as much as capacity.

## Sizes

- **1M tokens:** Claude Mythos Preview, Claude Opus 4.7, Claude Opus 4.6, Claude Sonnet 4.6.
- **200k tokens:** other models (e.g., Sonnet 4.5, Sonnet 4 deprecated).
- Per-request limits: up to **600 images or PDF pages** (1M models); **100** for 200k models. Request-size limits may bite before token limit.

## Standard window behavior

- Linear growth: each turn's full input + output is preserved in subsequent input phase.
- Newer models (Sonnet 3.7+) **return validation error** when input+output exceed window — no silent truncation.

## Extended thinking interaction

- All input/output, including thinking tokens, count toward the window.
- Thinking budget is a subset of `max_tokens` and billed as output tokens; counts toward rate limits.
- Adaptive thinking → variable per request.
- **Previous-turn thinking blocks are auto-stripped from context** by API — you don't need to strip them yourself if you pass them back. They are billed as output tokens only at generation time.
- Effective window: `(input_tokens − previous_thinking_tokens) + current_turn_tokens`.

## Extended thinking + tool use

- During tool-use cycle, thinking block **must** be returned with the corresponding tool result (only case where you must return thinking).
- Effective window: `input_tokens + current_turn_tokens`.
- Cryptographic signatures verify thinking authenticity — modifying breaks reasoning continuity → API error.
- Claude 4 supports interleaved thinking; Sonnet 3.7 does not.

## Context awareness (Sonnet 4.6, Sonnet 4.5, Haiku 4.5)

These models track their remaining token budget. At conversation start:

```xml
<budget:token_budget>1000000</budget:token_budget>
```

After each tool call:

```xml
<system_warning>Token usage: 35000/1000000; 965000 remaining</system_warning>
```

Image tokens included in budget. Useful for long-running agent sessions, multi-context-window workflows, careful token management.

## Management strategies

- **Compaction (recommended):** server-side summarization (beta on Opus 4.7 / Opus 4.6 / Sonnet 4.6).
- **Context editing:** tool result clearing, thinking block clearing.
- **Token counting API** — estimate before sending.
