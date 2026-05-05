---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/skills/versions.md
source_url: https://platform.claude.com/docs/en/api/beta/skills/versions
title: "Skill Versions"
summarized_at: 2026-05-05
entities_referenced: [Skill-API]
concepts_referenced: []
---

Sub-resource page for **Skill Versions** rooted at `/v1/skills/{skill_id}/versions`.

**Endpoints on this page:**

- `POST .../versions` — Create a new version (returns `id`, `skill_id`, `version`, `name`, `description`, `directory`, `type`, `created_at`).
- `GET .../versions` — List versions.
- `GET .../versions/{version}` — Retrieve a specific version.
- `DELETE .../versions/{version}` — Delete a specific version.

Skill versions are immutable snapshots; agents can pin to a specific `version` via the agent's `skills[].version` field, or omit it to track the latest. Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
