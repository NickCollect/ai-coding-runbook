---
type: summary
source: 01_Raw/platform.claude.com/docs/en/build-with-claude/citations.md
source_url: https://platform.claude.com/docs/en/build-with-claude/citations
title: "Citations"
summarized_at: 2026-05-05
entities_referenced: [Citations-API, Messages-API, PDF-support, Prompt-caching, Token-counting, Batches-API, Structured-outputs, Search-results]
concepts_referenced: []
---

The Citations feature lets Claude attach verifiable source citations to claims in its responses, anchored to provided documents. ZDR-eligible. Supported on all active models **except Haiku 3**.

## How citations work

1. Provide one or more documents in user content with `citations.enabled: true`. Must be enabled on **all or none** of documents in a request.
2. Documents get chunked: PDFs and plain text → sentences; custom content → as-provided blocks.
3. Response interleaves text blocks with `citations` arrays, each pointing to specific document spans.

## Document types & citation index format

| Document type | Citation references |
|---|---|
| PDF | Page number range (1-indexed, exclusive end) |
| Plain text | Character index range (0-indexed, exclusive end) |
| Custom content | Content block index range (0-indexed, exclusive end) |

Document indices are 0-indexed across the full request (all messages).

## Citable vs non-citable

- `source` content → citable.
- `title` (length-limited) and `context` → passed to model but not cited.
- Image citations not supported (even within PDFs).

## Token costs

- Slight input token increase (system prompt + chunking).
- Very efficient on output: `cited_text` field is **not counted toward output tokens** and not toward input on subsequent turns.

## Compatibility

- Works with: prompt caching, token counting, batch processing.
- **Incompatible with Structured Outputs** — using `output_config.format` (or deprecated `output_format`) with citations enabled returns 400. Reason: citations require interleaved blocks vs strict JSON schema.
- **Prompt caching pattern:** apply `cache_control: {type: "ephemeral"}` to top-level document blocks. Citation blocks themselves cannot be cached but source documents can.

## Search results

For RAG with structured per-result citation, see Search results blocks (separate page).
