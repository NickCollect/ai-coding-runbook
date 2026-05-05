---
type: summary
source: 01_Raw/code.claude.com/docs/en/admin-setup.md
source_url: https://code.claude.com/docs/en/admin-setup
title: "Set up Claude Code for your organization"
summarized_at: 2026-05-05
entities_referenced: [Settings, Permission-mode, Sandboxing, MCP-server, Plugin-marketplace, Hooks, Memory, Enterprise-gateway]
concepts_referenced: []
---

Decision-map page for admins deploying Claude Code. Walks through provider choice → settings delivery → enforcement → usage visibility → data handling.

**Provider choice**: Claude for Teams/Enterprise (default), Claude Console (pay-as-you-go), Amazon Bedrock, Google Vertex AI, Microsoft Foundry. Provider determines billing and inherited compliance posture. Network/proxy requirements (`network-config`) apply regardless.

**Settings delivery — four mechanisms, first one found wins** (priority high→low):
1. Server-managed (admin console, refreshes hourly, Teams/Enterprise only)
2. plist (macOS `com.anthropic.claudecode`) / Windows `HKLM\SOFTWARE\Policies\ClaudeCode`
3. File-based: macOS `/Library/Application Support/ClaudeCode/managed-settings.json`, Linux/WSL `/etc/claude-code/managed-settings.json`, Windows `C:\Program Files\ClaudeCode\managed-settings.json`
4. Windows user registry `HKCU` (writable without elevation — convenience only, not enforcement)

Managed values override user/project. Array settings (`permissions.allow`, `permissions.deny`) merge across sources — devs can extend but not remove. WSL reads only Linux path by default; set `wslInheritsWindowsSettings: true` to extend Windows policy.

**Enforcement controls**:
- `permissions.allow` / `permissions.deny` — allow/ask/deny tools and commands
- `allowManagedPermissionRulesOnly`, `permissions.disableBypassPermissionsMode` — lockdown that disables `--dangerously-skip-permissions`
- `sandbox.enabled`, `sandbox.network.allowedDomains` — OS-level FS/network isolation with domain allowlist
- Managed policy `CLAUDE.md` — org-wide instructions, cannot be excluded
- `allowedMcpServers`, `deniedMcpServers`, `allowManagedMcpServersOnly` — MCP control
- `strictKnownMarketplaces`, `blockedMarketplaces` — plugin marketplace control
- `allowManagedHooksOnly`, `allowedHttpHookUrls` — hook restrictions
- `minimumVersion` — version floor

Permissions and sandboxing are different layers: denying WebFetch blocks Claude's tool, but if Bash is allowed, `curl`/`wget` can still reach any URL — sandboxing closes that gap at OS level.

**Visibility**: OpenTelemetry export (all providers), per-user analytics dashboard at `claude.ai/analytics/claude-code` (Anthropic only), cost tracking via cloud billing or native cost tracking.

**Data handling**: On Team/Enterprise/API/cloud-provider plans, Anthropic does not train on code/prompts. Zero Data Retention available on Enterprise. LLM gateway can centralize request-level audit logging.

**Verify**: Developer runs `/status`; output includes `Enterprise managed settings (remote|plist|HKLM|HKCU|file)`. Common login fixes: `/logout` + `/login`, `claude update`, restart terminal.
