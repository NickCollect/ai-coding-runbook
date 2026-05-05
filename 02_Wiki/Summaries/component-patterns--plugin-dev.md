---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/plugin-dev/skills/plugin-structure/references/component-patterns.md
title: "plugin-dev: plugin-structure component-patterns reference"
summarized_at: 2026-05-05
entities_referenced: [Plugin, Slash-command, Subagent, Skill, Hooks, MCP-server]
concepts_referenced: []
---

Reference inside `plugin-dev`'s `plugin-structure` skill. Advanced patterns for organizing plugin components.

**Component lifecycle**:
- Discovery phase: at CC startup — read `.claude-plugin/plugin.json` per plugin → discover components in default + custom paths → parse YAML/configs → register → init MCP servers + hooks.
- Activation phase: commands invoked by user, agents selected by capability, skills loaded by context match, hooks called on events, MCP servers receive matching tool calls.

**Command organization**:
- Flat (`commands/*.md`) — best for 5-15 commands, no clear categories.
- Categorized (multiple top-level dirs `commands/`, `admin-commands/`, `workflow-commands/` listed in manifest) — best for 15+, clear functional categories.
- Hierarchical (nested `commands/ci/`, `commands/deployment/`) — Claude Code doesn't auto-discover nested; must list each in manifest's `commands` array. Best for 20+ commands, multi-level categorization.

**Agent organization**:
- Role-based (one role per file — `code-reviewer.md`, `test-generator.md`).
- Capability-based (tech-specific — `python-expert.md`, `api-specialist.md`).
- Workflow-based (stage-aligned — `planning-agent.md`, `testing-agent.md`).

**Skill organization**:
- Topic-based (`api-design/`, `error-handling/`).
- Tool-based (`docker/`, `kubernetes/`, `terraform/` with references/scripts/examples).
- Workflow-based (`code-review-workflow/`, `deployment-workflow/`).
- Skill with rich resources: `SKILL.md` (overview), `references/` (detailed guides loaded on demand), `examples/` (copy-paste), `scripts/` (executables), `assets/` (templates).

**Hook organization**:
- Monolithic (single `hooks.json` for 5-10 hooks).
- Event-based (separate JSON per event type — combined via build script; CC doesn't support file references natively).
- Purpose-based (script subdirs `security/`, `quality/`, `workflow/`).

**Script organization**: flat / categorized (`build/`, `test/`, `deploy/`) / language-based (`bash/`, `python/`, `javascript/`).

**Cross-component patterns**:
- **Shared resources**: `lib/` dir with utility scripts sourced via `source "${CLAUDE_PLUGIN_ROOT}/lib/test-utils.sh"`.
- **Layered architecture**: `commands/` (UI), `agents/` (orchestration), `skills/` (knowledge), `lib/core|integrations|utils` for large plugins.
- **Plugin within plugin**: nested `core/` + `extensions/extension-a/`, `extensions/extension-b/` with manifest listing all paths.

**Best practices**: consistent naming, descriptive (avoid abbrev), start simple (flat → reorganize when needed), group related, separate concerns, plan for growth, refactor early, document structure in README, follow community standards, minimize nesting (impacts discovery time), minimize custom paths (defaults faster), keep configs small.
