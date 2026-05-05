---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/plugin-dev/README.md
title: "Plugin Development Toolkit"
summarized_at: 2026-05-05
entities_referenced: [Plugin, Skill, Hooks, MCP-server, Slash-command, Subagent, Plugin-marketplace]
concepts_referenced: []
---

Plugin (MIT, Daisy Hollman, v0.1.0) bundling **seven specialized skills + three validation agents + a guided workflow command** for building Claude Code plugins.

**Bundled skills** (each ~1,200-2,000 word `SKILL.md` plus references / examples / utility scripts):
1. **hook-development** — prompt-based vs command hooks, all events (PreToolUse, PostToolUse, Stop, SubagentStop, SessionStart, SessionEnd, UserPromptSubmit, PreCompact, Notification), output formats, security, `${CLAUDE_PLUGIN_ROOT}` portability. Ships `validate-hook-schema.sh`, `test-hook.sh`, `hook-linter.sh`.
2. **mcp-integration** — `.mcp.json` vs `plugin.json`, all server types (stdio/SSE/HTTP/WebSocket), env var expansion, naming, OAuth/token/env auth. References: server-types (~3.2k words), authentication (~2.8k), tool-usage (~2.6k).
3. **plugin-structure** — directory layout, `plugin.json` manifest, auto-discovery, `${CLAUDE_PLUGIN_ROOT}`, naming, minimal/standard/advanced patterns.
4. **plugin-settings** — `.claude/plugin-name.local.md` config pattern, YAML frontmatter parsing techniques (sed/awk/grep), temporarily-active hooks (flag files + quick-exit), real-world examples from `multi-agent-swarm` and `ralph-wiggum`. Ships `validate-settings.sh`, `parse-frontmatter.sh`.
5. **command-development** — slash-command frontmatter (description, argument-hint, allowed-tools), dynamic args, file refs, bash execution for context, namespacing.
6. **agent-development** — full subagent file structure, frontmatter (name, description, model, color, tools), `<example>` blocks for reliable triggering, system-prompt design patterns (analysis/generation/validation/orchestration), AI-assisted agent generation via Claude Code's own prompt. Ships `validate-agent.sh`.
7. **skill-development** — based on skill-creator methodology adapted for plugins. Progressive disclosure (metadata → SKILL.md → resources), strong triggers, imperative/third-person writing.

**Three-level progressive disclosure** is the standard pattern: metadata always loaded → SKILL.md when triggered → references/examples on demand.

**`/plugin-dev:create-plugin`** (8-phase guided workflow):
1. Discovery → understand purpose
2. Component Planning → which skills/commands/agents/hooks/MCP are needed
3. Detailed Design → resolve ambiguities (CRITICAL phase)
4. Structure Creation → directories + `plugin.json`
5. Component Implementation → load relevant skill per type
6. Validation → run plugin-validator + skill-reviewer + utilities
7. Testing → installation + verification checklist
8. Documentation → README + marketplace entry

Uses `agent-creator`, `plugin-validator`, `skill-reviewer` subagents. Loads relevant skills via the Skill tool at each phase. TodoWrite-tracked.

**Quality standards** enforced: third-person skill descriptions, imperative form bodies, commands written FOR Claude (not the user), strong trigger phrases, `${CLAUDE_PLUGIN_ROOT}` portability, security-first (no hardcoded creds, HTTPS/WSS).

**Install**: `/plugin install plugin-dev@claude-code-marketplace` (or `cc --plugin-dir /path/to/plugin-dev` for dev).

Total content: ~11k words core skills, ~10k+ words refs, 12+ working examples, 6 production utility scripts.
