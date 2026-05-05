---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/plugin-dev/agents/plugin-validator.md
title: "plugin-validator subagent (plugin-dev plugin)"
summarized_at: 2026-05-05
entities_referenced: [Subagent, Plugin, Hooks, MCP-server, Skill]
concepts_referenced: []
---

Subagent definition from the `plugin-dev` plugin. Validates Claude Code plugin structure, manifest, and components. `model: inherit`, `color: yellow`, tools: `Read`, `Grep`, `Glob`, `Bash`. Triggers on phrases like "validate my plugin", "check plugin structure", or proactively after plugin file changes.

**10-step validation process**:
1. Locate plugin root (`.claude-plugin/plugin.json`); note project vs marketplace location.
2. Validate manifest: JSON syntax (jq), required `name` (kebab-case, no spaces), optional `version` (semver X.Y.Z), `description`, `author`, `mcpServers`. Warn on unknown fields, don't fail.
3. Validate directory structure: `commands/`, `agents/`, `skills/`, `hooks/hooks.json`. Verify auto-discovery.
4. Validate commands (`commands/**/*.md`): YAML frontmatter, `description`, `argument-hint` format, `allowed-tools` array, markdown body, no name conflicts.
5. Validate agents (`agents/**/*.md`): name (lowercase, hyphens, 3–50 chars), description with `<example>` blocks, model (`inherit`/`sonnet`/`opus`/`haiku`), color (blue/cyan/green/yellow/magenta/red), substantive system prompt (>20 chars). Use `validate-agent.sh` from agent-development skill if available.
6. Validate skills (`skills/*/SKILL.md`): existence, frontmatter `name`+`description`, references/examples/scripts subdirs, validate referenced files.
7. Validate hooks (`hooks/hooks.json`): valid JSON, valid event names, each hook has `matcher` + `hooks` array, type `command` or `prompt`, commands use `${CLAUDE_PLUGIN_ROOT}` for portability. Use `validate-hook-schema.sh` if available.
8. Validate MCP config (`.mcp.json` or inline): JSON syntax, type-specific fields (stdio→`command`, sse/http/ws→`url`), `${CLAUDE_PLUGIN_ROOT}` for portability.
9. File organization: README.md exists/comprehensive, no `node_modules`/`.DS_Store`, .gitignore present, LICENSE present.
10. Security: no hardcoded credentials anywhere, MCP servers use HTTPS/WSS not HTTP/WS, hooks lack obvious security holes, no secrets in examples.

Report sections: Critical Issues (file path + issue + fix), Warnings, Component Summary (counts found vs valid), Positive Findings, Recommendations (prioritized), Overall Assessment (PASS/FAIL with reasoning). Quality: include file path + specific issue, distinguish errors from warnings, fix suggestion per issue, severity (critical/major/minor).

Edge cases: minimal plugin (just plugin.json) is valid if manifest correct; empty dirs warn but don't fail; corrupted files skip + report and continue.
