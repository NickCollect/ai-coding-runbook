---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/plugin-dev/skills/plugin-structure/SKILL.md
title: "plugin-dev: plugin-structure skill"
summarized_at: 2026-05-05
entities_referenced: [Skill, Plugin, Slash-command, Subagent, Hooks, MCP-server]
concepts_referenced: []
---

Skill from `plugin-dev` plugin teaching standardized Claude Code plugin directory layout and `${CLAUDE_PLUGIN_ROOT}` portable path mechanism. Triggers on "create a plugin", "scaffold a plugin", "plugin structure", "plugin.json", "auto-discovery", etc.

**Standard layout**:
```
plugin-name/
├── .claude-plugin/
│   └── plugin.json          # required manifest
├── commands/                 # .md files, slash commands
├── agents/                   # .md files, subagent defs
├── skills/<skill-name>/SKILL.md  # subdirs per skill
├── hooks/hooks.json          # event handlers
├── .mcp.json                 # MCP servers
└── scripts/                  # helpers
```

**Critical rules**:
1. Manifest MUST be in `.claude-plugin/`.
2. Component directories (commands/agents/skills/hooks) MUST be at plugin root, NOT inside `.claude-plugin/`.
3. Only create dirs for components actually used.
4. kebab-case naming for all dirs/files.

**Manifest fields** (`.claude-plugin/plugin.json`):
- Required: `name` (kebab-case, unique).
- Recommended: `version` (semver), `description`, `author` (object with name/email/url), `homepage`, `repository`, `license`, `keywords`.
- Custom paths (supplement defaults, don't replace): `commands`, `agents`, `hooks`, `mcpServers`. Must be relative starting `./`.

**Components**:
- **Commands**: `.md` in `commands/`, auto-discovered. Frontmatter: `name`, `description`. Body = command instructions.
- **Agents**: `.md` in `agents/`, auto-discovered. Frontmatter: `description`, `capabilities`. Body = system prompt.
- **Skills**: each in own subdir under `skills/`, requires `SKILL.md`. Can include scripts/, references/, examples/, assets/. Frontmatter: `name`, `description`, `version`. Auto-activated by Claude when description matches context.
- **Hooks**: `hooks/hooks.json` or inline in plugin.json. Events: PreToolUse, PostToolUse, Stop, SubagentStop, SessionStart, SessionEnd, UserPromptSubmit, PreCompact, Notification.
- **MCP servers**: `.mcp.json` or inline. Auto-start when plugin enables.

**`${CLAUDE_PLUGIN_ROOT}`**: env var for portable intra-plugin paths. Use in: hook command paths, MCP server commands, script execution refs, resource files. **NEVER**: hardcoded absolute paths, relative paths from cwd, `~/...`.

**Naming conventions**: kebab-case for commands (`code-review.md` → `/code-review`), agents (`test-generator.md`), skill dirs (`api-testing/`), scripts (`validate-input.sh`), docs (`api-reference.md`). Standard names: `hooks.json`, `.mcp.json`, `plugin.json`.

**Auto-discovery timing**: at plugin install (registers) and enable (becomes available). No restart required for changes — takes effect on next session.

**Best practices**: logical grouping, minimal manifest (rely on auto-discovery), include READMEs, consistent naming across components, use `${CLAUDE_PLUGIN_ROOT}` always, test on multiple OSes, semver, document breaking changes.

**Common patterns**: minimal (just commands), full-featured (all component types), skill-focused (just skills).

**Troubleshooting**: component not loading → check dir + extension + YAML + SKILL.md naming + plugin enabled; path errors → use `${CLAUDE_PLUGIN_ROOT}`; auto-discovery not working → directories at root not in `.claude-plugin/`, kebab-case, restart Claude Code.
