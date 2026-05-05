---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/files/retrieve_metadata.md
source_url: https://platform.claude.com/docs/en/api/beta/files/retrieve_metadata
title: "Get File Metadata"
summarized_at: 2026-05-05
entities_referenced: [Files-API]
concepts_referenced: []
---

`GET /v1/files/{file_id}` — fetch the metadata record for a file.

**Path param:** `file_id`. Returns a `FileMetadata` object: `id`, `created_at`, `filename`, `mime_type`, `size_bytes`, `type: "file"`, optional `downloadable`, optional `scope`. Requires `anthropic-beta: files-api-2025-04-14` header plus standard Anthropic auth (`X-Api-Key`, `anthropic-version: 2023-06-01`).
