---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/plugin-dev/skills/plugin-structure/references/manifest-reference.md
title: "Plugin Manifest Reference (plugin.json)"
summarized_at: 2026-05-05
entities_referenced: [Plugin, MCP-server, Hooks, Subagent, Slash-command]
concepts_referenced: []
---

Complete reference for `.claude-plugin/plugin.json`. Required path is exactly `.claude-plugin/plugin.json` at plugin root — Claude Code won't recognize plugins missing this.

**Required field**:
- `name` (string, kebab-case) — must match `/^[a-z][a-z0-9]*(-[a-z0-9]+)*$/`. Used for ID, conflict detection, namespacing.

**Metadata fields** (all optional):
- `version` (semver MAJOR.MINOR.PATCH; default `0.1.0`). Pre-releases like `1.0.0-alpha.1`/`-beta.2`/`-rc.1`.
- `description` — 50–200 chars recommended.
- `author` — object `{name, email?, url?}` or single string `"Name <email> (url)"`.
- `homepage` (URL to docs/landing page; NOT for source code).
- `repository` (URL string or `{type, url, directory?}` object).
- `license` (SPDX identifier: `MIT`, `Apache-2.0`, `GPL-3.0`, `BSD-3-Clause`, `ISC`, `UNLICENSED`; multiples via `(MIT OR Apache-2.0)`).
- `keywords` (array — recommended 5–10).

**Component path fields** — all default to standard locations (`./commands`, `./agents`, `./hooks/hooks.json`, `./.mcp.json`):
- `commands` — string or array of paths to additional command dirs.
- `agents` — same.
- `hooks` — string path to JSON file OR inline object (full `hooks.json` schema).
- `mcpServers` — string path OR inline object.

**Path rules**:
- Must be RELATIVE; must start with `./`; cannot use `../`; forward slashes only (even on Windows).
- Examples: ✅ `./commands`, `./src/commands`, ❌ `commands` (missing `./`), `/abs/path`, `../shared`, `.\\commands`.

**Resolution order**: defaults scanned first, then manifest custom paths. Components from all locations merge (no overwriting). Name conflicts cause errors.

**Common validation errors**: spaces in name (use kebab-case), absolute paths (use relative), missing `./` prefix, non-semver version (`1.0` → `1.0.0`).

**Three example tiers**:
- **Minimal**: just `{"name": "hello-world"}` — relies on default discovery.
- **Recommended for distribution**: name + version + description + author + homepage + repository + license + keywords.
- **Complete**: all metadata + custom commands/agents arrays + external hooks/mcpServers paths.

**Best practices**: bump version on changes; keep description current; complete metadata before publishing; test on clean install; include README + LICENSE; validate manifest.
