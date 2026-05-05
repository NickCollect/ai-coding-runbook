---
type: summary
source: 01_Raw/platform.claude.com/docs/en/build-with-claude/compaction.md
source_url: https://platform.claude.com/docs/en/build-with-claude/compaction
title: "Compaction"
summarized_at: 2026-05-05
entities_referenced: [Compaction, Messages-API, Context-editing]
concepts_referenced: [Context-window]
---

Server-side context compaction extends effective context length by automatically summarizing older content when input tokens approach a threshold. Beta — requires header `anthropic-beta: compact-2026-01-12`. ZDR-eligible. Recommended over client-side strategies for managing context in long-running conversations and agentic workflows.

## Supported models

- Claude Mythos Preview (`claude-mythos-preview`)
- Claude Opus 4.7 (`claude-opus-4-7`)
- Claude Opus 4.6 (`claude-opus-4-6`)
- Claude Sonnet 4.6 (`claude-sonnet-4-6`)

## How it works

1. Detect input tokens exceed configured trigger threshold.
2. Generate a conversation summary.
3. Emit a `compaction` block containing the summary.
4. Continue response with compacted context.
5. On subsequent requests, append response to messages — **API automatically drops all message blocks prior to the `compaction` block** and continues from summary.

## Enabling

Add to Messages API request:

```json
{
  "context_management": {
    "edits": [
      {"type": "compact_20260112"}
    ]
  }
}
```

Plus header `anthropic-beta: compact-2026-01-12`.

## Use cases

- Multi-turn chat where one conversation runs for a long time.
- Task-oriented prompts with heavy follow-up tool use that may exceed context window.

## Why use compaction

Beyond just staying under token caps: long contexts degrade focus. Compaction replaces stale content with concise summaries to keep active context performant — addresses *context rot*.

## Related

- Combine with context editing for finer-grained tool result / thinking block clearing.
