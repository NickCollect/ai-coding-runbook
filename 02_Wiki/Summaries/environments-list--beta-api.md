---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/environments/list.md
source_url: https://platform.claude.com/docs/en/api/beta/environments/list
title: "List Environments"
summarized_at: 2026-05-05
entities_referenced: [Environment-API]
concepts_referenced: []
---

`GET /v1/environments` — paginated list of environments. Standard cursor/limit pagination consistent with peer beta resources. Returns an array of environment objects.

Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
