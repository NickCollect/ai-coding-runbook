---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/files/list.md
source_url: https://platform.claude.com/docs/en/api/beta/files/list
title: "List Files"
summarized_at: 2026-05-05
entities_referenced: [Files-API]
concepts_referenced: []
---

`GET /v1/files` — list uploaded files.

**Query params:** `after_id` and `before_id` (cursor pagination), `limit` (default 20, range 1–1000), and `scope_id` (filter to files associated with a specific scope, e.g. a session ID).

Returns `data: array of FileMetadata` plus `first_id`, `has_more`, and `last_id` for paging.

Requires `anthropic-beta: files-api-2025-04-14` header plus standard Anthropic auth (`X-Api-Key`, `anthropic-version: 2023-06-01`).
