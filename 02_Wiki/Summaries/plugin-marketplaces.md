---
type: summary
source: 01_Raw/code.claude.com/docs/en/plugin-marketplaces.md
source_url: https://code.claude.com/docs/en/plugin-marketplaces
title: "Create and distribute a plugin marketplace"
summarized_at: 2026-05-05
entities_referenced: [Plugin-marketplace, Plugin, Skill]
concepts_referenced: []
---

How to author and distribute a plugin marketplace. Marketplaces are catalogs that distribute plugins; users add a marketplace then `/plugin install` from it.

**Workflow**:
1. Author plugins (skills, agents, hooks, MCP servers, LSP servers).
2. Create a `marketplace.json` listing the plugins + their sources.
3. Host on git (GitHub, GitLab, etc.) or local path.
4. Share — users `/plugin marketplace add <ref>` then `/plugin install <name>@<marketplace-name>`. `/plugin marketplace update` to refresh.

**Walkthrough**: Local marketplace with one `quality-review-plugin` that adds `/quality-review` skill (`disable-model-invocation: true`). Directory structure:
```
my-marketplace/
  .claude-plugin/marketplace.json
  plugins/quality-review-plugin/
    .claude-plugin/plugin.json
    skills/quality-review/SKILL.md
```

**`marketplace.json` schema** — required: `name` (kebab-case identifier), `owner.name`, `plugins[]`. Optional: `description`, `version`, `metadata.pluginRoot` (base dir for relative source paths), `allowCrossMarketplaceDependenciesOn` (other marketplaces this one's plugins may depend on; missing entries blocked at install).

Reserved marketplace names (cannot use): `claude-code-marketplace`, `claude-code-plugins`, `claude-plugins-official`, `anthropic-marketplace`, `anthropic-plugins`, `agent-skills`, `knowledge-work-plugins`, `life-sciences`. Impersonating names also blocked.

**Plugin entry fields**: `name`, `source` (object or string) required. Plus marketplace-specific: `category`, `tags`, `strict`. Plus full plugin manifest fields (`description`, `version`, `author`, etc.) accepted at the marketplace level.

**Source types** for `source`:
- Inline path string `"./plugins/formatter"`
- GitHub: `{ "source": "github", "repo": "company/deploy-plugin" }`
- (Other source types covered in full plugin docs)

**Versioning gotcha**: if `plugin.json` sets `version`, users only get updates when you bump that field — bump on every release. If you OMIT `version` in a git-hosted marketplace, every commit counts as a new version (potentially noisy).

**Plugin caching note**: Claude Code copies plugin directory to a cache location at install. Cross-plugin file references like `../shared-utils` won't work — use symlinks for shared files (see plugins-reference doc).

**Hosting options**: any git host. After push, users update via `/plugin marketplace update <name>`.
