---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/files.md
source_url: https://platform.claude.com/docs/en/api/beta/files
title: "Files"
summarized_at: 2026-05-05
entities_referenced: [Files-API, Session-API]
concepts_referenced: []
---

Beta REST resource for **Files** under `/v1/files`. Files are persistent objects that can be uploaded once and then referenced by ID inside Messages, sessions (as resources), or other endpoints.

**Endpoints on this page:**

- `POST /v1/files` — Upload File (multipart/form-data, `file` field).
- `GET /v1/files` — List Files (`after_id`/`before_id`/`limit`/`scope_id` filter).
- `GET /v1/files/{file_id}/content` — Download File contents.
- `GET /v1/files/{file_id}` — Retrieve metadata.
- `DELETE /v1/files/{file_id}` — Delete File.

**Domain types:**
- `FileMetadata` — `id`, `created_at`, `filename`, `mime_type`, `size_bytes`, `type: "file"`, optional `downloadable`, optional `scope` (`BetaFileScope` with `id` + `type: "session"`).
- `BetaFileScope` — when a file was created in the context of a session, this scopes its visibility/lifetime to that session ID.
- `DeletedFile` — `{ id, type: "file_deleted" }` returned from delete.

Requires `anthropic-beta: files-api-2025-04-14` header plus standard Anthropic auth (`X-Api-Key`, `anthropic-version: 2023-06-01`).
