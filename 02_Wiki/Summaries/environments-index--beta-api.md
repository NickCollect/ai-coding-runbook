---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/environments.md
source_url: https://platform.claude.com/docs/en/api/beta/environments
title: "Environments"
summarized_at: 2026-05-05
entities_referenced: [Environment-API]
concepts_referenced: []
---

Beta REST resource for **Environments** under `/v1/environments`. An environment is a sandboxed execution context (e.g., a `BetaCloudConfig`) that Managed Agents can run inside.

**Endpoints on this page:**

- `POST /v1/environments` — Create Environment (`name` required; optional `config`, `description`, `metadata`).
- `GET /v1/environments` — List Environments.
- `GET /v1/environments/{environment_id}` — Retrieve Environment.
- `POST /v1/environments/{environment_id}` — Update Environment.
- `DELETE /v1/environments/{environment_id}` — Delete Environment.
- `POST /v1/environments/{environment_id}/archive` — Archive Environment.

The resource stores `id`, `name`, optional `description`, optional `config` (e.g. `BetaCloudConfigParams`), `metadata`, plus `created_at`/`archived_at` timestamps. Environments are referenced by sessions and agents to provide a consistent execution sandbox.

Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
