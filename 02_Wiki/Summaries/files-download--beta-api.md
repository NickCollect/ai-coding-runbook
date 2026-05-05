---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/files/download.md
source_url: https://platform.claude.com/docs/en/api/beta/files/download
title: "Download File"
summarized_at: 2026-05-05
entities_referenced: [Files-API]
concepts_referenced: []
---

`GET /v1/files/{file_id}/content` — stream back the raw bytes of an uploaded file.

**Path param:** `file_id`. The response body is the file's binary content (no JSON envelope). Requires `anthropic-beta: files-api-2025-04-14` header plus standard Anthropic auth (`X-Api-Key`, `anthropic-version: 2023-06-01`).
