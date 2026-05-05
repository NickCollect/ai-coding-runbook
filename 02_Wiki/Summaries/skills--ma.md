---
type: summary
source: 01_Raw/platform.claude.com/docs/en/managed-agents/skills.md
source_url: https://platform.claude.com/docs/en/managed-agents/skills
title: "Skills"
summarized_at: 2026-05-05
entities_referenced: [Skill, Skill-API, Managed-agent, Session-API]
concepts_referenced: [Context-window]
---

How to attach reusable, filesystem-based [[Skill]] s to a [[Managed-agent]] for domain-specific expertise (workflows, context, best practices that turn a general-purpose agent into a specialist). Unlike prompts (conversation-level instructions for one-off tasks), skills load on demand and only impact the [[Context-window]] when needed. **Requires `managed-agents-2026-04-01` beta header.**

**Two skill types** (both invoked automatically when relevant):
- **Pre-built Anthropic skills**: common document tasks—PowerPoint (`pptx`), Excel (`xlsx`), Word (`docx`), PDF (`pdf`).
- **Custom skills**: skills your organization authors and uploads via the [[Skill-API]].

For authoring custom skills, see the agent-skills overview and best-practices documentation.

**Attaching at agent creation.** Add a `skills` array to the agent definition. **Maximum 20 skills per session**, including across all agents in a multi-agent session.

```json
{
  "name": "Financial Analyst",
  "model": "claude-opus-4-7",
  "system": "You are a financial analysis agent.",
  "skills": [
    {"type": "anthropic", "skill_id": "xlsx"},
    {"type": "custom", "skill_id": "skill_abc123", "version": "latest"}
  ]
}
```

**Skill entry fields.**

| Field | Description |
|---|---|
| `type` | `anthropic` (pre-built) or `custom` (org-authored). |
| `skill_id` | For Anthropic skills: short name (e.g., `xlsx`). For custom: the `skill_*` ID returned at creation. |
| `version` | Custom skills only. Pin to a specific version or use `latest`. |

**How skills work in the [[Session-API]].** The skill metadata (name + description) is preloaded into the system prompt at session start. When the agent's task matches a skill, Claude reads the skill's `SKILL.md` from the container's filesystem on demand. Bundled scripts and reference files are loaded only as referenced—the standard progressive-disclosure pattern.

This means you can attach many skills to an agent (up to 20 per session) without paying full token cost upfront—only metadata costs are paid until a skill is actually triggered.

**Pairing.** Skills compose with the rest of the agent's tools (the pre-built `agent_toolset_20260401` provides the bash/file ops needed to read and execute the skill content). Skills don't replace tools—they add structured, reusable expertise that the agent can invoke when appropriate.

The page focuses on the attach-to-agent step. Skill authoring (writing SKILL.md, structuring reference files, packaging executable scripts) is covered separately in the Agent Skills documentation under agents-and-tools.
