---
type: summary
source: 01_Raw/code.claude.com/docs/en/plugins.md
source_url: https://code.claude.com/docs/en/plugins
title: "Create plugins"
summarized_at: 2026-05-05
entities_referenced: [Plugin, Skill, Subagent, Hooks, MCP-server, Plugin-marketplace, Slash-command, Settings, Output-style]
concepts_referenced: []
---

How to create Claude Code plugins. Plugins package skills, agents, hooks, MCP servers, LSP servers, and background monitors so they can be shared across projects/teams via marketplaces.

**Plugin vs standalone trade-off**:
| Approach | Skill name shape | Best for |
|---|---|---|
| Standalone (`.claude/`) | `/hello` | Personal/project work, quick experiments |
| Plugin (`.claude-plugin/plugin.json`) | `/plugin-name:hello` | Sharing, versioning, reuse, marketplaces |

Skills inside plugins are **always namespaced** (`/my-plugin:hello`) to prevent collisions.

**Plugin manifest** (`.claude-plugin/plugin.json`):
```json
{
  "name": "my-first-plugin",
  "description": "...",
  "version": "1.0.0",
  "author": { "name": "Your Name" }
}
```
Without `version`, the git commit SHA is used and every commit counts as a new version. Additional fields (`homepage`, `repository`, `license`) in the full schema.

**Plugin directory structure** (everything except `plugin.json` is at the plugin **root**, NOT inside `.claude-plugin/` — common mistake):
| Directory / file | Purpose |
|---|---|
| `.claude-plugin/plugin.json` | manifest (only thing in `.claude-plugin/`) |
| `skills/<name>/SKILL.md` | skills (preferred for new plugins) |
| `commands/` | slash commands as flat Markdown files (legacy) |
| `agents/` | subagent definitions |
| `hooks/hooks.json` | hook configurations |
| `.mcp.json` | MCP servers |
| `.lsp.json` | LSP servers (code intelligence) |
| `monitors/monitors.json` | background monitors (auto-start when plugin enabled) |
| `bin/` | executables added to Bash PATH while plugin is enabled |
| `settings.json` | default settings; only `agent` + `subagentStatusLine` keys supported |
| `output-styles/` | bundled output styles |
| `themes/` | bundled themes |

**Skill arguments**: `$ARGUMENTS` placeholder captures user-provided text after the skill name. Frontmatter `disable-model-invocation: true` makes the skill user-only.

**Background monitors** (`monitors.json`): array of `{name, command, description}`. Each stdout line from `command` is delivered to Claude as a notification during the session. Plugin-declared monitors auto-start with the plugin.

**Plugin `settings.json`**: only `agent` and `subagentStatusLine` keys. `agent` activates one of the plugin's custom agents as the main thread (system prompt, tool restrictions, model). Settings here override `settings` declared in `plugin.json`. Unknown keys silently ignored.

**Local testing**: `claude --plugin-dir ./my-plugin` (can be repeated for multiple plugins). Local `--plugin-dir` plugin overrides installed marketplace plugin of the same name (except force-enabled by managed settings). `/reload-plugins` to pick up changes without restart.

**Migration from standalone**:
| Standalone | Plugin |
|---|---|
| `.claude/commands/` | `<plugin>/commands/` |
| Hooks in `settings.json` | `hooks/hooks.json` |
| One project | Marketplace-shareable |

After migration, remove the originals from `.claude/` to avoid duplicates (plugin version takes precedence).

**Submit to official marketplace**: `claude.ai/settings/plugins/submit` or `platform.claude.com/plugins/submit`. Use Plugin Hints to recommend your plugin from your CLI to Claude Code users.
