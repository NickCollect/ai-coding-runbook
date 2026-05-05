---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/skills/create.md
source_url: https://platform.claude.com/docs/en/api/beta/skills/create
title: "Create Skill"
summarized_at: 2026-05-05
entities_referenced: [Skill-API]
concepts_referenced: []
---

`POST /v1/skills` — create a new skill.

**Returns:** `id`, `display_title`, `latest_version`, `source`, `type`, `created_at`, `updated_at`. The newly-created skill becomes referenceable by ID from a Managed Agent's `skills` array (`type: "custom"`). Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
