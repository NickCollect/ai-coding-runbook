---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/skills/versions/list.md
source_url: https://platform.claude.com/docs/en/api/beta/skills/versions/list
title: "List Skill Versions"
summarized_at: 2026-05-05
entities_referenced: [Skill-API]
concepts_referenced: []
---

`GET /v1/skills/{skill_id}/versions` — list every published version of a skill. **Path param:** `skill_id`. Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
