---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/skills/delete.md
source_url: https://platform.claude.com/docs/en/api/beta/skills/delete
title: "Delete Skill"
summarized_at: 2026-05-05
entities_referenced: [Skill-API]
concepts_referenced: []
---

`DELETE /v1/skills/{skill_id}` — delete a custom skill (and, transitively, its versions).

**Path param:** `skill_id`. **Returns:** `{ id, type }`. Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
