---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/skills/versions/create.md
source_url: https://platform.claude.com/docs/en/api/beta/skills/versions/create
title: "Create Skill Version"
summarized_at: 2026-05-05
entities_referenced: [Skill-API]
concepts_referenced: []
---

`POST /v1/skills/{skill_id}/versions` — publish a new version of a skill.

**Path param:** `skill_id`. **Returns:** `id`, `skill_id`, `version`, `name`, `description`, `directory`, `type`, `created_at`. Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
