---
type: summary
source: 01_Raw/github/anthropics/skills/skills/claude-api/shared/live-sources.md
title: "claude-api skill: live-sources reference"
summarized_at: 2026-05-05
entities_referenced: [Skill]
concepts_referenced: []
---

WebFetch URL registry inside the `claude-api` skill. Used when cached docs are insufficient or out of date.

**When to WebFetch**: user asks for "latest"/"current" info, cached data seems incorrect, feature not in cached content, need specific API details.

**URL categories** with extraction prompts:

**Models & Pricing**: `platform.claude.com/docs/en/about-claude/models/overview.md`, `migration-guide.md`, `pricing.md`.

**Core features**: extended-thinking, adaptive-thinking, effort, tool-use, streaming, prompt-caching.

**Media & files**: vision, pdf-support.

**API operations**: batch-processing, files (Files API), token-counting, rate-limits, errors.

**Tools**: code-execution, computer-use, bash-tool, text-editor-tool, memory-tool, tool-search-tool, programmatic-tool-calling, skills.

**Advanced**: structured-outputs, compaction, context-editing, citations, context-windows.

**Managed Agents** (extensive): overview, quickstart, agent-setup, define-outcomes, sessions, environments, events-and-streaming, tools, files, permission-policies, multi-agent, observability, github, mcp-connector, vaults, skills, memory, onboarding, cloud-containers, migration. Use these when bindings/behaviors not in cached `shared/managed-agents-*.md` files.

**Anthropic CLI (`ant`)**: `platform.claude.com/docs/en/api/sdks/cli.md` — terminal access to Claude API; useful for creating agents/environments/sessions from version-controlled YAML.

**SDK GitHub repos** (Python, TypeScript, Java, Go, Ruby, C#, PHP) — when a binding (class/method/namespace) isn't in cached `{lang}/` skill files. Search for `BetaManagedAgents`, `beta.agents`, `beta.sessions`, etc.

**Fallback**: if WebFetch fails — use cached content (note date), inform user, suggest checking platform.claude.com or GitHub directly.
