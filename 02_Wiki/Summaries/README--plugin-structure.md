---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/plugin-dev/skills/plugin-structure/README.md
title: "Plugin Structure Skill (plugin-dev)"
summarized_at: 2026-05-05
entities_referenced: [Plugin, Skill, MCP-server, Hooks]
concepts_referenced: []
---

Index README for the `plugin-structure` skill inside the `plugin-dev` toolkit. The skill teaches plugin architecture, directory layout, manifest configuration, component organization, auto-discovery, `${CLAUDE_PLUGIN_ROOT}` usage, and naming conventions.

**SKILL.md** (~1,619 words) covers: directory structure overview, `plugin.json` fields, component organization, `${CLAUDE_PLUGIN_ROOT}` patterns, naming conventions, auto-discovery, best practices, troubleshooting.

**References**:
- `manifest-reference.md` — every `plugin.json` field, path resolution rules, validation, minimal vs complete examples
- `component-patterns.md` — component lifecycle (discovery, activation), per-component organization patterns (commands, agents, skills, hooks, scripts), cross-component patterns, scalability

**Examples** (three complete plugin layouts):
- `minimal-plugin.md` — single command, minimal manifest
- `standard-plugin.md` — multi-component (commands, agents, skills, hooks), complete manifest with metadata
- `advanced-plugin.md` — enterprise: multi-level org, MCP integration, shared libs, config management, security automation, monitoring

**Trigger phrases**: create/scaffold a plugin, understand plugin structure, organize components, set up `plugin.json`, `${CLAUDE_PLUGIN_ROOT}` usage, add commands/agents/skills/hooks, configure auto-discovery.

Uses three-level **progressive disclosure**: SKILL.md (~1.6k words) → references (~6k words) → examples (~8k words). Claude loads deeper material only when needed.

Maintenance principles: keep SKILL.md lean; move detail to references; use imperative/infinitive form throughout.
