---
type: summary
source: 01_Raw/code.claude.com/docs/en/plugins-reference.md
source_url: https://code.claude.com/docs/en/plugins-reference
title: "Plugins reference"
summarized_at: 2026-05-05
entities_referenced: [Plugin, Plugin-marketplace, Skill, Subagent, Hooks, MCP-server, Output-style, Settings, Channel, Slash-command]
concepts_referenced: [Channel]
---

Complete technical reference for the Claude Code plugin system: schemas, CLI commands, and component specifications.

**Plugin = self-contained directory of components**: skills, agents, hooks, MCP servers, LSP servers, and **monitors** (background watchers).

**Components and locations**:
- **Skills**: `skills/<name>/SKILL.md` (with optional reference.md, scripts/) or `commands/*.md` (legacy flat). Auto-discovered, namespaced as `plugin-name:skill-name`.
- **Agents**: `agents/*.md` with frontmatter. Supports `name`, `description`, `model`, `effort`, `maxTurns`, `tools`, `disallowedTools`, `skills`, `memory`, `background`, `isolation` (only `"worktree"`). **NOT supported for plugin agents (security)**: `hooks`, `mcpServers`, `permissionMode`.
- **Hooks**: `hooks/hooks.json` or inline. Hook types: `command`, `http`, `mcp_tool`, `prompt` (uses `$ARGUMENTS`), `agent`. Same lifecycle events as user hooks (PreToolUse / PostToolUse / SessionStart / etc).
- **MCP servers**: `.mcp.json` or inline. Supports `${CLAUDE_PLUGIN_ROOT}` and `${CLAUDE_PLUGIN_DATA}` substitution.
- **LSP servers**: `.lsp.json` or inline. Required `command` + `extensionToLanguage`. Optional `args`, `transport` (`stdio`/`socket`), `env`, `initializationOptions`, `settings`, `workspaceFolder`, `startupTimeout`, `shutdownTimeout`, `restartOnCrash`, `maxRestarts`. **Language server binary must be installed separately.** Available LSP plugins: `pyright-lsp`, `typescript-lsp`, `rust-lsp`.
- **Monitors** (v2.1.105+): `monitors/monitors.json`. Persistent background processes, stdout lines → notifications. Required: `name`, `command`, `description`. Optional `when`: `"always"` (default) or `"on-skill-invoke:<skill-name>"`. Run unsandboxed at hooks trust level. Don't stop when plugin disabled mid-session.
- **Themes**: `themes/*.json` with `base` (`dark`/`light`/preset) + `overrides` color tokens map. Read-only; `Ctrl+E` in `/theme` copies to `~/.claude/themes/` for editing.

**Installation scopes**: `user` (default, `~/.claude/settings.json`), `project` (`.claude/settings.json`), `local` (`.claude/settings.local.json`, gitignored), `managed` (read-only, update-only).

**Manifest schema** (`.claude-plugin/plugin.json`, optional — auto-discovers from default locations if omitted):
- Required if present: `name` (kebab-case)
- Metadata: `$schema`, `version`, `description`, `author`, `homepage`, `repository`, `license`, `keywords`
- Component paths: `skills`, `commands`, `agents`, `hooks`, `mcpServers`, `outputStyles`, `themes`, `lspServers`, `monitors`
- `userConfig` declares user-prompted values at enable time. Types: `string|number|boolean|directory|file`. Optional `sensitive` (masks input, stores in keychain ~2KB limit), `required`, `default`, `multiple`, `min/max`. Substituted as `${user_config.KEY}` in MCP/LSP/hook/monitor commands; non-sensitive can substitute in skills/agents. Exported as `CLAUDE_PLUGIN_OPTION_<KEY>` env vars.
- `channels` declares MCP-bound channel(s) with optional per-channel `userConfig`
- `dependencies` array (`["lib"]` or `[{"name":"lib","version":"~2.1.0"}]`) for inter-plugin deps with semver constraints

**Path behavior**: paths must be relative starting with `./`. For `skills`, `commands`, `agents`, `outputStyles`, `themes`, `monitors`: custom path REPLACES default — to keep default + add more, include default in array (`["./skills/", "./extras/"]`). Hooks, MCP, LSP have different multi-source semantics. Skill at plugin root: `name` frontmatter determines invocation name (else basename).

**Env vars**: `${CLAUDE_PLUGIN_ROOT}` (changes per-update; bundled files), `${CLAUDE_PLUGIN_DATA}` (`~/.claude/plugins/data/{id}/`, persists across updates — use for `node_modules`, virtualenvs, caches). Both substituted inline AND exported to subprocesses. Pattern: SessionStart hook diffs bundled vs cached `package.json` and reinstalls when changed; deleted on full uninstall (use `--keep-data` to preserve).

**Caching/file resolution**: marketplace plugins are copied to `~/.claude/plugins/cache` (each version separate). Old versions marked orphaned 7 days after update/uninstall (lets concurrent sessions finish). Glob/Grep skip orphaned dirs. **Path traversal blocked** — `../shared-utils` won't work after install (those files aren't copied). Workaround: symlinks IN plugin root (preserved in cache, resolved at runtime).

**Standard layout**: `.claude-plugin/plugin.json`, then `skills/`, `commands/`, `agents/`, `output-styles/`, `themes/`, `monitors/`, `hooks/`, `bin/` (added to Bash PATH — invokable as bare command), `settings.json` (only `agent` and `subagentStatusLine` keys currently supported), `.mcp.json`, `.lsp.json`, `scripts/`, LICENSE, CHANGELOG.md.

**CLI commands**: `claude plugin install <plugin>[@marketplace] [-s scope]`, `uninstall` (aliases `remove`/`rm`; flags `--keep-data`, `--prune`, `-y`), `prune` (alias `autoremove`; v2.1.121+), `enable`, `disable`, `update [-s scope incl. managed]`, `list [--json --available]`, `tag [--push --dry-run -f]` (creates release git tag for plugin in cwd).

**Versioning**: resolution order — `version` in plugin.json → `version` in marketplace entry → git commit SHA (for github/url/git-subdir/relative-path sources in git-hosted marketplaces) → `unknown` (npm or non-git local). **Set `version` = explicit version mode (must bump for users to update — pushing commits without bumping leaves cache untouched). Omit = commit-SHA mode (every commit triggers update).**

**Common debug issues**: invalid plugin.json (run `claude plugin validate` or `/plugin validate`), components inside `.claude-plugin/` (must be at root), script not executable (`chmod +x`), missing `${CLAUDE_PLUGIN_ROOT}`, absolute paths used.
