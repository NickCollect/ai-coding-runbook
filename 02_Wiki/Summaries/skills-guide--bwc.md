---
type: summary
source: 01_Raw/platform.claude.com/docs/en/build-with-claude/skills-guide.md
source_url: https://platform.claude.com/docs/en/build-with-claude/skills-guide
title: "Using Agent Skills with the API"
summarized_at: 2026-05-05
entities_referenced: [Skill, Skill-API, Messages-API, Code-execution-tool, Files-API]
concepts_referenced: []
---

Agent Skills extend Claude's capabilities via organized folders of instructions/scripts/resources. Integrate through the Messages API + code execution tool. **NOT ZDR-eligible.** Up to **8 Skills per request** via the `container` parameter.

## Two sources

| Aspect | Anthropic Skills | Custom Skills |
|---|---|---|
| `type` value | `anthropic` | `custom` |
| `skill_id` | Short name: `pptx`, `xlsx`, `docx`, `pdf` | Generated `skill_01...` |
| Version | Date-based: `20251013` or `latest` | Epoch timestamp: `1759178010641129` or `latest` |
| Mgmt | Pre-built by Anthropic | Upload via Skills API |
| Scope | All users | Workspace-private |

Both share identical integration shape and execution environment. List via `/v1/skills` (filter by `source`).

## Required beta headers

- `code-execution-2025-08-25` — code execution (required for all Skills)
- `skills-2025-10-02` — Skills API
- `files-api-2025-04-14` — for upload/download to/from container

Plus the `code_execution_20250825` tool must be enabled in your request.

## Container schema

```json
{
  "container": {
    "skills": [
      {"type": "anthropic", "skill_id": "pptx", "version": "latest"}
    ]
  },
  "tools": [{"type": "code_execution_20250825", "name": "code_execution"}]
}
```

## Related

- Skill Management API (CRUD): `/docs/en/api/skills/list-skills`
- Skill Versions API: list/manage version history
