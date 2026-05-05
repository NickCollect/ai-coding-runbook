---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/environments/retrieve.md
source_url: https://platform.claude.com/docs/en/api/beta/environments/retrieve
title: "Retrieve Environment"
summarized_at: 2026-05-05
entities_referenced: [Environment-API]
concepts_referenced: []
---

`GET /v1/environments/{environment_id}` — fetch a single environment by ID. Returns the full environment object including any `config`, `description`, and `metadata`.

Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
