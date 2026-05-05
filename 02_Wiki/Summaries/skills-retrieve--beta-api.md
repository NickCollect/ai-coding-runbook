---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/skills/retrieve.md
source_url: https://platform.claude.com/docs/en/api/beta/skills/retrieve
title: "Retrieve Skill"
summarized_at: 2026-05-05
entities_referenced: [Skill-API]
concepts_referenced: []
---

`GET /v1/skills/{skill_id}` — fetch a single skill including its `latest_version`, `source`, `type`, `display_title`, `created_at`, `updated_at`. **Path param:** `skill_id`. Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
