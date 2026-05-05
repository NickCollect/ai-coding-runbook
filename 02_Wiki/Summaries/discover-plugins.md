---
type: summary
source: 01_Raw/code.claude.com/docs/en/discover-plugins.md
source_url: https://code.claude.com/docs/en/discover-plugins
title: "Discover and install prebuilt plugins through marketplaces"
summarized_at: 2026-05-05
entities_referenced: [Plugin, Plugin-marketplace, Skill, Subagent, Hooks, MCP-server, Output-style]
concepts_referenced: []
---

How to find and install plugins via marketplaces. Plugins bundle skills, agents, hooks, MCP servers; marketplaces are catalogs that distribute them.

**Two-step flow**: add marketplace → install individual plugins. Marketplace registration is just browse access — no plugins are installed automatically.

**Official Anthropic marketplace** (`claude-plugins-official`) is auto-available. Install via `/plugin install <name>@claude-plugins-official` (e.g. `github@claude-plugins-official`). Browse via `/plugin` Discover tab or [claude.com/plugins](https://claude.com/plugins). Submit plugins via in-app forms at claude.ai or platform.claude.com.

If plugin "not found in any marketplace": `/plugin marketplace update claude-plugins-official` (or `add anthropics/claude-plugins-official` if missing).

**Official marketplace categories**:
- **Code intelligence** — LSP plugins enabling Claude's built-in language-server tool. Languages: C/C++, C#, Go, Java, Kotlin, Lua, PHP, Python, Rust, Swift, TypeScript. Each requires the language-server binary on PATH (e.g. `pyright-langserver` for `pyright-lsp`). Capabilities gained: automatic diagnostics after every edit (Ctrl+O for inline view) + code navigation (defs, refs, hover, symbols, call hierarchy).
- **External integrations** (pre-configured MCP servers): github, gitlab, atlassian, asana, linear, notion, figma, vercel, firebase, supabase, slack, sentry.
- **Development workflows**: commit-commands, pr-review-toolkit, agent-sdk-dev, plugin-dev.
- **Output styles**: explanatory-output-style, learning-output-style.

**Demo marketplace** (`claude-code-plugins`): `/plugin marketplace add anthropics/claude-code` to add. Manually added (vs official which is auto-available). Used for example plugins.

**`/plugin` UI** has 4 tabs (Tab to cycle): Discover, Installed, Marketplaces, Errors. Install scopes: User (across all projects) / Project (for collaborators on this repo) / Local (just you, this repo).

After install, run `/reload-plugins` to activate. Plugin skills are namespaced: `commit-commands` → `/commit-commands:commit`.

**Adding marketplaces** — `/plugin marketplace add` accepts:
- GitHub `owner/repo` (looks for `.claude-plugin/marketplace.json`)
- Git URLs (GitLab, Bitbucket, self-hosted)
- Local paths (directories or direct path to `marketplace.json`)
- Remote URLs (hosted `marketplace.json`)

Shortcuts: `/plugin market` instead of `/plugin marketplace`; `rm` instead of `remove`.

LSP gotcha: if `/plugin` Errors tab shows `Executable not found in $PATH`, install the language-server binary listed in the table.
