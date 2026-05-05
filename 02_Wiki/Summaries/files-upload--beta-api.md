---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/files/upload.md
source_url: https://platform.claude.com/docs/en/api/beta/files/upload
title: "Upload File"
summarized_at: 2026-05-05
entities_referenced: [Files-API]
concepts_referenced: []
---

`POST /v1/files` — upload a file using `multipart/form-data` with a `file` field.

Returns `FileMetadata`: `id`, `created_at` (RFC 3339), `filename`, `mime_type`, `size_bytes`, `type: "file"`, optional `downloadable`, and optional `scope` (`BetaFileScope` with `id` + `type: "session"`) when the file is bound to a specific session.

Requires `anthropic-beta: files-api-2025-04-14` header plus standard Anthropic auth (`X-Api-Key`, `anthropic-version: 2023-06-01`).
