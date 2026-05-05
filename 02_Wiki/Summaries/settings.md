---
type: summary
source: 01_Raw/code.claude.com/docs/en/settings.md
source_url: https://code.claude.com/docs/en/settings
title: "Claude Code settings"
summarized_at: 2026-05-05
entities_referenced: [Settings, Memory, Hooks, MCP-server, Plugin, Plugin-marketplace, Permission-mode, Auto-mode, Sandboxing, Subagent, Status-line, Skill, Output-style, Enterprise-gateway, Headless-mode, Native-interface, IDE-integration]
concepts_referenced: [Channel, Extended-thinking]
---

Reference for `settings.json` and the scope/precedence system. The settings file has dozens of keys (full list ~600+ lines in raw). This summary covers the structural model and notable keys; refer to raw for exhaustive enumeration.

**Scope system** — five layers, highest first:
1. **Managed** — can't be overridden. Sources (any of):
   - **Server-managed** via Claude.ai admin console (Teams/Enterprise)
   - **plist** (macOS `com.anthropic.claudecode`) / **registry** (Windows `HKLM\SOFTWARE\Policies\ClaudeCode\Settings`, REG_SZ JSON; or `HKCU\...` lowest-priority user-level)
   - **File-based** `managed-settings.json` + `managed-mcp.json`:
     - macOS: `/Library/Application Support/ClaudeCode/`
     - Linux/WSL: `/etc/claude-code/`
     - Windows: `C:\Program Files\ClaudeCode\` (legacy `C:\ProgramData\ClaudeCode\` removed in v2.1.75)
   - **Drop-in directory** `managed-settings.d/` (systemd convention): base merged first, then alphabetically sorted overlays. Numeric prefixes (`10-`, `20-`) control order.
2. **CLI args** — temporary session
3. **Local** (`.claude/settings.local.json`, gitignored)
4. **Project** (`.claude/settings.json`, committed)
5. **User** (`~/.claude/settings.json`)

Array values like `permissions.allow`/`deny`, `sandbox.filesystem.allowWrite` **merge across scopes**; scalars are overridden.

**File map by feature**:
| Feature | User | Project | Local |
|---|---|---|---|
| Settings | `~/.claude/settings.json` | `.claude/settings.json` | `.claude/settings.local.json` |
| Subagents | `~/.claude/agents/` | `.claude/agents/` | — |
| MCP servers | `~/.claude.json` | `.mcp.json` | `~/.claude.json` (per-project) |
| Plugins | `~/.claude/settings.json` | `.claude/settings.json` | `.claude/settings.local.json` |
| CLAUDE.md | `~/.claude/CLAUDE.md` | `CLAUDE.md` or `.claude/CLAUDE.md` | `CLAUDE.local.md` |

`~/.claude.json` is **separate** from `~/.claude/settings.json` — holds OAuth session, MCP user/local config, per-project state (allowed tools, trust), caches. Permissions/hooks/env do NOT belong here.

`$schema` field (`https://json.schemastore.org/claude-code-settings.json`) enables editor autocomplete + validation.

Auto backups: 5 most recent timestamped backups retained.

**Notable keys** (selection — full list in raw):
- **Permissions**: `permissions.{allow,deny,ask}`, `allowManagedPermissionRulesOnly` (managed-only lockdown), `permissions.disableBypassPermissionsMode`, `disableAutoMode`
- **Auto mode**: `autoMode.{environment, allow, soft_deny}` arrays of prose rules; `"$defaults"` literal inherits built-ins. **Not read from shared project settings** (clones can't inject classifier rules)
- **Sandbox**: `sandbox.{enabled, failIfUnavailable, filesystem.{allowWrite, denyWrite, allowRead, denyRead}, network.{allowedDomains, deniedDomains, httpProxyPort, socksProxyPort, allowManagedDomainsOnly}, excludedCommands, allowUnsandboxedCommands, allowUnixSockets, enableWeakerNestedSandbox}`
- **MCP**: `enableAllProjectMcpServers`, `enabledMcpjsonServers`, `disabledMcpjsonServers`, `allowedMcpServers`, `deniedMcpServers`, `allowManagedMcpServersOnly`
- **Plugins**: `enabledPlugins`, `blockedMarketplaces`, `strictKnownMarketplaces`
- **Hooks**: `hooks` (object with event names → array of matchers); `disableAllHooks`, `allowedHttpHookUrls`, `allowManagedHooksOnly`
- **Status line**: `statusLine.{type, command, padding, refreshInterval, hideVimModeIndicator}`, `subagentStatusLine`
- **Models**: `model`, `availableModels`, `effortLevel`, `alwaysThinkingEnabled`
- **Channels**: `channelsEnabled` (managed-only), `allowedChannelPlugins` (managed-only)
- **Memory**: `autoMemoryDirectory` (NOT accepted from project/local — repo could redirect writes to sensitive paths)
- **CLI/UI**: `editorMode` (normal|vim), `autoScrollEnabled`, `awaySummaryEnabled`, `autoUpdatesChannel` (stable|latest), `companyAnnouncements`
- **Auth**: `apiKeyHelper`, `awsAuthRefresh`, `awsCredentialExport`
- **Cleanup**: `cleanupPeriodDays` (default 30, min 1, sweeps session/tasks/shell-snapshots/backups)
- **Misc**: `agent` (run main thread as named subagent), `defaultShell` (bash|powershell), `attribution.commit/pr` (git commit/PR templates), `disableDeepLinkRegistration`, `disableSkillShellExecution`

`/config` slash command opens a tabbed Settings UI for interactive editing. Most settings can also be edited there.
