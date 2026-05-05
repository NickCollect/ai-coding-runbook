---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/skills.md
source_url: https://platform.claude.com/docs/en/api/beta/skills
title: "Skills"
summarized_at: 2026-05-05
entities_referenced: [Skill-API]
concepts_referenced: []
---

Beta REST resource for **Skills** under `/v1/skills`. The Skill-API lets clients upload, list, and version custom skills that Managed Agents can be wired to via the agent's `skills` array.

**Skill endpoints on this page:**

- `POST /v1/skills` — Create skill (returns `id`, `display_title`, `latest_version`, `source`, `type`, `created_at`, `updated_at`).
- `GET /v1/skills` — List skills.
- `GET /v1/skills/{skill_id}` — Retrieve.
- `DELETE /v1/skills/{skill_id}` — Delete (returns `{ id, type }`).

**Versions sub-resource:**
- `POST /v1/skills/{skill_id}/versions` — Create new version (returns `id`, `skill_id`, `version`, `name`, `description`, `directory`, `type`, `created_at`).
- `GET /v1/skills/{skill_id}/versions` — List versions.
- `GET /v1/skills/{skill_id}/versions/{version}` — Retrieve a specific version.
- `DELETE /v1/skills/{skill_id}/versions/{version}` — Delete a version.

This is the **remote skill management API** (canonical name `Skill-API`), distinct from the local Claude Code `Skill` artifact that ships in plugins. Pin a Managed Agent to a specific skill version via the agent's `skills[].version` field at create or update time. Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies. The skills feature also requires the `skills-2025-10-02` beta header.
