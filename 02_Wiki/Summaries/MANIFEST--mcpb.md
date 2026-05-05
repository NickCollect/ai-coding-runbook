---
type: summary
source: 01_Raw/github/modelcontextprotocol/mcpb/MANIFEST.md
source_url: https://github.com/modelcontextprotocol/mcpb/blob/main/MANIFEST.md
title: "MCPB manifest.json spec (v0.3)"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Full schema reference for the `manifest.json` file at the root of every MCP Bundle. Current version `0.3` (last updated 2025-12-02).

**Required fields:** `manifest_version`, `name` (machine-readable), `version` (semver), `description` (localizable), `author` (object with `name` required, `email`/`url` optional), `server` (config object).

**Optional fields:** `display_name` (UI label), `long_description` (markdown), `repository`, `homepage`, `documentation`, `support`, `icon` (single PNG path or URL), `icons` (array with `src`/`size`/`theme` for light/dark/size variants), `screenshots`, `tools` (declared tool list), `tools_generated` (bool — server creates more at runtime), `prompts`, `prompts_generated`, `keywords`, `license`, `privacy_policies` (required when extension talks to external services that handle user data), `compatibility`, `user_config`, `_meta` (reverse-DNS namespaced platform-specific metadata, e.g., `com.microsoft.windows` `package_family_name`), `localization`.

**Localization:** point `localization.resources` to a per-locale JSON file path containing `${locale}` placeholder (default `mcpb-resources/${locale}.json`); `default_locale` uses BCP 47 (default `en-US`). Localizable fields marked with 🌎. Per-locale files only need overrides; clients should apply locale fallbacks (e.g., `es-UY` → `es-MX`/`es-ES` → manifest defaults).

**Compatibility object:** `claude_desktop` (semver constraint), arbitrary `<client>` semver constraints, `platforms` (`darwin`/`win32`/`linux`), `runtimes.python` and `runtimes.node` semver. All optional.

**Server types:**
- `node` — JS entry point, bundle `node_modules`
- `python` — Python entry point, bundle deps in `server/lib/` or `server/venv/`
- `binary` — pre-compiled platform-specific executable
- `uv` (v0.4+) — cross-platform Python without bundling: deps declared in `pyproject.toml`, host installs via UV. Small bundle (~100 KB vs 5–10 MB), handles compiled deps, no user Python install needed; must NOT include `server/lib/` or `server/venv/`; `mcp_config` optional.

**`mcp_config`** defines how the host runs the server: `command`, `args`, `env`, optional `platform_overrides` (per-platform `command`/`args`/`env` overrides; Windows auto-appends `.exe` to binaries).

**Variable substitution in `mcp_config`:** `${__dirname}` (extension install path), `${HOME}`, `${DESKTOP}`, `${DOCUMENTS}`, `${DOWNLOADS}`, `${pathSeparator}`/`${/}`, `${user_config.KEY}` (user-provided values).

**`user_config`** — host-collected config presented to end users via UI. Each entry has `type` (`string`/`number`/`boolean`/`directory`/`file`), `title`, `description`, `required`, `default` (supports `${HOME}` etc.), `multiple` (for dir/file pickers), `sensitive` (mask + secure storage for strings), `min`/`max` (number bounds). Arrays (multi-selection) expand as separate args. Examples cover filesystem dir picker, API key + base URL, SQLite database path with read-only and timeout.

**Tools and prompts** — static declaration lists `name`/`description`; for prompts also `arguments` and `text` with `${arguments.X}` placeholders. Resources are intentionally NOT declarable in the manifest because they're inherently runtime-dynamic. `tools_generated`/`prompts_generated` flags signal additional capabilities discoverable only at runtime.
