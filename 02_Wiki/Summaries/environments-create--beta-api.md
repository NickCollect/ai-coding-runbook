---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/environments/create.md
source_url: https://platform.claude.com/docs/en/api/beta/environments/create
title: "Create Environment"
summarized_at: 2026-05-05
entities_referenced: [Environment-API]
concepts_referenced: []
---

`POST /v1/environments` — create a new sandbox environment.

**Body params:** `name` (string, required); optional `description`, `config` (a `BetaCloudConfigParams` describing the cloud-side runtime), and `metadata` (KV map). Returns the persisted environment object.

Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
