---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/environments/update.md
source_url: https://platform.claude.com/docs/en/api/beta/environments/update
title: "Update Environment"
summarized_at: 2026-05-05
entities_referenced: [Environment-API]
concepts_referenced: []
---

`POST /v1/environments/{environment_id}` — patch an environment.

**Path param:** `environment_id`. **Optional body params:** `config` (`BetaCloudConfigParams`), `description`, `metadata`, `name`. Returns the updated environment object.

Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
