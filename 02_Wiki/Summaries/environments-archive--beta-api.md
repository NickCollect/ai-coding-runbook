---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/environments/archive.md
source_url: https://platform.claude.com/docs/en/api/beta/environments/archive
title: "Archive Environment"
summarized_at: 2026-05-05
entities_referenced: [Environment-API]
concepts_referenced: []
---

`POST /v1/environments/{environment_id}/archive` — soft-delete by setting `archived_at`. **Path param:** `environment_id`. Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
