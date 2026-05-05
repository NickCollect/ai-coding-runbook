---
type: summary
source: 01_Raw/platform.claude.com/docs/en/build-with-claude/search-results.md
source_url: https://platform.claude.com/docs/en/build-with-claude/search-results
title: "Search results"
summarized_at: 2026-05-05
entities_referenced: [Search-results, Citations-API, Messages-API, Tool-use, Prompt-caching]
concepts_referenced: [Tool-use]
---

Search-result content blocks bring web-search-quality natural citations to custom RAG applications. ZDR-eligible.

## Supported models

Opus 4.7, Opus 4.6, Sonnet 4.6, Sonnet 4.5, Opus 4.5, Opus 4.1, Opus 4 (deprecated), Sonnet 4 (deprecated), Sonnet 3.7 (deprecated), Haiku 4.5, Haiku 3.5 (deprecated).

## Two delivery modes

1. **From tool calls (`tool_result`):** custom tools return `search_result` blocks → dynamic RAG with auto-citations.
2. **As top-level user content:** pre-fetched/cached search results provided directly in user messages.

## Schema

```json
{
  "type": "search_result",
  "source": "https://example.com/article",
  "title": "Article Title",
  "content": [
    {"type": "text", "text": "..."}
  ],
  "citations": {"enabled": true}
}
```

### Required fields

| Field | Type | Description |
|---|---|---|
| `type` | string | Must be `"search_result"` |
| `source` | string | Source URL or identifier |
| `title` | string | Descriptive title |
| `content` | array | Array of text blocks (each `{type: "text", text: "..."}`, non-empty) |

### Optional fields

| Field | Notes |
|---|---|
| `citations` | `{enabled: bool}` |
| `cache_control` | e.g., `{type: "ephemeral"}` |

## Benefits

- Natural citation format matching web search quality.
- Flexible: tool returns OR top-level content.
- Per-result source + title attribution.
- No document-block workarounds needed.
