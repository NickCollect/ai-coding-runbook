---
type: summary
source: 01_Raw/platform.claude.com/docs/en/build-with-claude/pdf-support.md
source_url: https://platform.claude.com/docs/en/build-with-claude/pdf-support
title: "PDF support"
summarized_at: 2026-05-05
entities_referenced: [PDF-support, Messages-API, Files-API, Vision, Citations-API, Enterprise-gateway]
concepts_referenced: [Context-window]
---

PDF support lets Claude process text, charts, tables, and images in PDFs (relies on Claude's vision capabilities — same limitations apply). ZDR-eligible.

## Requirements / limits

| Requirement | Limit |
|---|---|
| Max request size | 32 MB (varies by platform) |
| Max pages per request | 600 (100 for 200k-token-window models) |
| Format | Standard PDF, no passwords/encryption |

Both limits cover entire request payload. For large PDFs use Files API + `file_id` to keep payload small. Dense PDFs (small fonts, complex tables, heavy graphics) may fill context window before reaching page limit; split or downsample embedded images.

## Platform support

- **Direct API:** all active models support PDF.
- **Vertex AI:** supported.
- **Bedrock:** supported with caveats (see below).

### Bedrock-specific (Converse API)

Two modes:
1. **Converse Document Chat** — text extraction only; ~1k tokens for 3-page PDF; default when citations not enabled.
2. **Claude PDF Chat** — full visual understanding (charts, layouts); processes each page as text + image; ~7k tokens for 3-page PDF; **requires citations enabled** in Converse API.

If users say Claude isn't seeing PDF images on Converse, they probably forgot the citations flag. **InvokeModel API** has full control without forced citations.

## Three ways to send PDFs

1. **URL reference:** `{type: "document", source: {type: "url", url: "..."}}`
2. **Base64-encoded:** `{type: "document", source: {type: "base64", media_type: "application/pdf", data: "..."}}`
3. **Files API `file_id`:** `{type: "document", source: {type: "file", file_id: "file_..."}}`

## Notes

- Non-PDF text-y formats (.csv, .xlsx, .docx, .md, .txt) → see "Working with other file formats" in Files page; convert to plain text or PDF first.
