---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/vaults/create.md
source_url: https://platform.claude.com/docs/en/api/beta/vaults/create
title: "Create Vault"
summarized_at: 2026-05-05
entities_referenced: [Vault]
concepts_referenced: []
---

`POST /v1/vaults` — create a new credential vault.

**Body params:** `display_name` (string, required); optional `metadata` (KV map). Returns the created vault object. Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
