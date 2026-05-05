---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/plugin-dev/commands/create-plugin.md
title: "/plugin-dev:create-plugin (slash command)"
summarized_at: 2026-05-05
entities_referenced: [Plugin, Skill, Slash-command, Subagent, Hooks, MCP-server, Plugin-marketplace]
concepts_referenced: []
---

Frontmatter: `description: Guided end-to-end plugin creation workflow with component design, implementation, and validation`. `allowed-tools: ["Read", "Write", "Grep", "Glob", "Bash", "TodoWrite", "AskUserQuestion", "Skill", "Task"]`. Optional `$ARGUMENTS` = plugin description.

Command instructs Claude to walk the user through an **8-phase guided workflow** building a Claude Code plugin from concept to tested implementation.

**Core principles** told to Claude: ask clarifying questions (not assumptions), load `plugin-dev` skills as needed via the Skill tool, leverage specialized agents (`agent-creator`, `plugin-validator`, `skill-reviewer`), apply best practices, use progressive disclosure, track via TodoWrite.

**Phases**:
1. **Discovery**: confirm plugin purpose; ask "what problem", "who uses", "what should it do", "similar plugins"; classify (integration / workflow / analysis / toolkit).
2. **Component planning**: load `plugin-structure` skill first; decide skills / commands / agents / hooks / MCP / settings; present plan as table; user confirms.
3. **Detailed design + clarifying questions** (CRITICAL — DO NOT SKIP): per component identify under-specified aspects (skills: triggers + scope, commands: args + tools + interactivity, agents: proactive vs reactive + tools + output, hooks: events + validation, MCP: type + auth + tools, settings: fields + defaults). Wait for user answers before implementing.
4. **Structure creation**: kebab-case name, location prompt, `mkdir` directory layout, `Write` `plugin.json` manifest (`name`, `version: "0.1.0"`, `description`, `author`), README template, `.gitignore` for `.local.md`, optional `git init`.
5. **Component implementation**: load matching skill before each component type. For agents specifically, use `agent-creator` subagent (auto-generates identifier, `whenToUse` with examples, system prompt). For each skill, use `skill-reviewer` subagent post-creation.
6. **Validation**: run `plugin-validator` agent → fix critical → run skill-reviewer per skill → run `validate-agent.sh` per agent → run `validate-hook-schema.sh` + `test-hook.sh` per hook. Present findings.
7. **Testing**: `cc --plugin-dir /path/to/plugin-name` instructions + verification checklist (skills load on triggers, commands appear in `/help`, agents trigger, hooks fire on events, MCP servers connect, settings work). Use `claude --debug` for hooks; `/mcp` for servers.
8. **Documentation**: README completeness (overview, install, prereqs, env vars for MCP, hook activation), marketplace.json entry if publishing, summary, suggested improvements.

**Decision points where Claude must wait for user**: after Phase 1 (purpose), Phase 2 (component plan), Phase 3 (proceed to implement), Phase 6 (fix vs proceed), Phase 7 (continue to docs).

Closes with example workflow ("Create a plugin for managing database migrations"). Final instruction: **Begin with Phase 1: Discovery**.
