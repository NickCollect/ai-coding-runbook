---
type: summary
source: 01_Raw/code.claude.com/docs/en/agent-sdk/plugins.md
source_url: https://code.claude.com/docs/en/agent-sdk/plugins
title: "Plugins in the SDK"
summarized_at: 2026-05-05
entities_referenced: [Plugin, Agent-SDK, Skill, Subagent, Hooks, MCP-server, Slash-command, Plugin-marketplace]
concepts_referenced: []
---

Plugins package Claude Code extensions (skills, agents, hooks, MCP servers) for sharing across projects. The Agent SDK loads plugins from local filesystem paths only — `type: "local"` is the only supported value. Marketplace/remote plugins must be downloaded first.

**Loading**:
```ts
plugins: [
  { type: "local", path: "./my-plugin" },
  { type: "local", path: "/abs/path/to/another" }
]
```
Path must point to the plugin root (directory containing `.claude-plugin/plugin.json`). Relative paths resolve from cwd; CLI-installed plugins live under `~/.claude/plugins/`.

**Verification**: when init message arrives (`message.type === "system"`, `subtype === "init"`), `message.plugins` lists loaded plugins and `message.slash_commands` lists available commands.

**Namespacing**: plugin skills are exposed as slash commands using `plugin-name:skill-name`. Note: the `commands/` directory is legacy; new plugins should use `skills/`.

**Plugin structure**:
```
my-plugin/
├── .claude-plugin/plugin.json   # required manifest
├── skills/<skill-name>/SKILL.md # agent skills
├── commands/                     # legacy
├── agents/                       # custom subagents
├── hooks/hooks.json              # event handlers
└── .mcp.json                     # MCP server defs
```

**Troubleshooting**: validate `plugin.json` JSON, check path points to plugin root, confirm skills appear in `slash_commands` with namespace prefix, ensure each skill has its own subdir under `skills/`. Use absolute paths if relative path resolution is unreliable.
