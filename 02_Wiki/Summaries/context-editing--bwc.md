---
type: summary
source: 01_Raw/platform.claude.com/docs/en/build-with-claude/context-editing.md
source_url: https://platform.claude.com/docs/en/build-with-claude/context-editing
title: "Context editing"
summarized_at: 2026-05-05
entities_referenced: [Context-editing, Compaction, Messages-API, Prompt-caching, Tool-runner, Extended-thinking]
concepts_referenced: [Context-window]
---

Context editing selectively clears specific content from conversation history server-side as it grows, giving fine-grained runtime control over what Claude sees. Beta — header `anthropic-beta: context-management-2025-06-27`. ZDR-eligible. Available on all supported Claude models. For most cases server-side compaction is preferred; context editing is for scenarios needing finer control.

## Strategies

| Approach | Where | Strategy types |
|---|---|---|
| **Server-side** | API | `clear_tool_uses_20250919`, `clear_thinking_20251015` |
| **Client-side** | SDK | Compaction (Python, TypeScript, Ruby SDKs via `tool_runner`) — generates summary, replaces full history |

Server-side editing is applied **before** the prompt reaches Claude. **Client app keeps the full unmodified conversation history locally** — no need to sync with edited version.

## Tool result clearing (`clear_tool_uses_20250919`)

- Clears oldest tool results in chronological order when context grows beyond threshold.
- Replaces cleared result with placeholder text so Claude knows it was removed.
- Default: only tool results cleared. Set `clear_tool_inputs: true` to also clear tool calls (parameters).
- `clear_at_least` parameter — ensure minimum tokens cleared per pass to make cache invalidation worthwhile.

## Thinking block clearing (`clear_thinking_20251015`)

Manages `thinking` blocks; pick balance between reasoning continuity (keep more) vs context space (clear more).

**Default `keep` behavior by model class:**
- **Opus:** Opus 4.5+ keep ALL prior thinking blocks; Opus 4.1 and earlier keep only last assistant turn.
- **Sonnet:** Sonnet 4.6+ keep ALL; Sonnet 4.5 and earlier keep only last turn.
- **Haiku:** all Haiku through Haiku 4.5 keep only last turn.

If your code spans multiple model tiers, set `keep` explicitly rather than relying on per-model default.

## Prompt caching interaction

- **Tool result clearing:** invalidates cached prefix when content cleared. Use `clear_at_least` to make cache writes worthwhile.
- **Thinking block clearing:** when thinking blocks **kept**, cache preserved → cache hits, lower input cost. When cleared, cache invalidated at clearing point.

## Config example

```json
{
  "context_management": {
    "edits": [
      {"type": "clear_tool_uses_20250919"}
    ]
  }
}
```

Multiple edits can be combined.
