---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/environments/delete.md
source_url: https://platform.claude.com/docs/en/api/beta/environments/delete
title: "Delete Environment"
summarized_at: 2026-05-05
entities_referenced: [Environment-API]
concepts_referenced: []
---

`DELETE /v1/environments/{environment_id}` — hard-delete an environment.

**Path param:** `environment_id`. Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
