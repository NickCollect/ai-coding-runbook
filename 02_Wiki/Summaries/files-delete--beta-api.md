---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/files/delete.md
source_url: https://platform.claude.com/docs/en/api/beta/files/delete
title: "Delete File"
summarized_at: 2026-05-05
entities_referenced: [Files-API]
concepts_referenced: []
---

`DELETE /v1/files/{file_id}` — permanently delete an uploaded file.

**Path param:** `file_id`. Returns `DeletedFile = { id, type: "file_deleted" }`. Requires `anthropic-beta: files-api-2025-04-14` header plus standard Anthropic auth (`X-Api-Key`, `anthropic-version: 2023-06-01`).
