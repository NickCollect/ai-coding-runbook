---
type: summary
source: 01_Raw/code.claude.com/docs/en/server-managed-settings.md
source_url: https://code.claude.com/docs/en/server-managed-settings
title: "Configure server-managed settings"
summarized_at: 2026-05-05
entities_referenced: [Settings, Hooks, Permission-mode, Auto-mode, MCP-server, Enterprise-gateway]
concepts_referenced: []
---

Centrally configure Claude Code via web UI on Claude.ai — no MDM required. Settings deliver from Anthropic's servers at authentication time + hourly polling.

**Requirements**: Teams or Enterprise plan, CC v2.1.38+ (Teams) or v2.1.30+ (Enterprise), network access to `api.anthropic.com`.

**Server-managed vs endpoint-managed**:
- Server-managed: orgs without MDM / users on unmanaged devices; Anthropic-server delivered
- Endpoint-managed: orgs with MDM/endpoint mgmt; OS-level configuration profiles, registry, managed settings files. Stronger security (settings file protected from user mod at OS level).

**Configure**: Claude.ai → Admin Settings → Claude Code → Managed settings. All `settings.json` keys supported including hooks, env vars, and managed-only keys (`allowManagedPermissionRulesOnly` etc.).

**Sample config** (deny list + bypass disable + restrict to managed rules):
```json
{
  "permissions": {
    "deny": ["Bash(curl *)", "Read(./.env)", "Read(./.env.*)", "Read(./secrets/**)"],
    "disableBypassPermissionsMode": "disable"
  },
  "allowManagedPermissionRulesOnly": true
}
```

Hook example (audit script after every Edit/Write):
```json
{"hooks": {"PostToolUse": [{"matcher": "Edit|Write", "hooks": [{"type": "command", "command": "/usr/local/bin/audit-edit.sh"}]}]}}
```

Auto-mode classifier env (tells classifier which infra is trusted):
```json
{"autoMode": {"environment": ["Source control: github.example.com/acme-corp and all repos under it", "Trusted cloud buckets: s3://acme-build-artifacts", "Trusted internal domains: *.corp.example.com"]}}
```

**Roles** (Primary Owner, Owner) can manage. Settings apply uniformly to all users (no per-group yet). **MCP server configs CANNOT be distributed via server-managed settings.**

**Verification**: ask user to restart, check `/permissions` to see effective rules, security approval dialog prompts on startup if hooks/env-vars/shell-cmds present.

**Managed-only keys**: most settings work in any scope, but a handful only effective from managed (see permissions doc).

**Settings precedence**: Server-managed AND endpoint-managed both at the highest tier. **Within tier: server-managed checked first, then endpoint-managed. Sources do NOT merge — if server-managed delivers any keys, endpoint-managed is ignored entirely.** Run `/status` to see which is active. Cleared server config falls back to cached settings until next successful fetch.

**Fetch/cache**:
- First launch: async fetch, brief unenforced window if fetch fails (continues without managed)
- Subsequent: cached applies immediately, fresh fetch in background, persists through network failures
- Most updates apply without restart (OpenTelemetry config requires restart)

**Fail-closed startup**: `forceRemoteSettingsRefresh: true` blocks startup until fresh fetch; CLI exits if fetch fails. Self-perpetuates (cached so subsequent startups enforce). Ensure `api.anthropic.com` is reachable before enabling, else users locked out.

**Security approval dialogs** for risky settings: shell command settings, custom env vars not in safe allowlist, hook configurations. User must approve or CC exits. **In `-p` non-interactive mode, dialogs are SKIPPED — settings auto-apply.**

**Platform availability**: NOT available with Bedrock / Vertex / Foundry / `ANTHROPIC_BASE_URL` (LLM gateways) — server-managed requires direct connection to `api.anthropic.com`.

**Audit logging** via compliance API / audit log export. Action type, account, device, prev/new value references.

**Security caveats** (client-side control on unmanaged devices):
| Scenario | Behavior |
|---|---|
| User edits cached settings file | Tampered applies at startup, restored on next server fetch |
| User deletes cached file | First-launch behavior (brief unenforced window) |
| API unavailable | Cached applies; `forceRemoteSettingsRefresh: true` exits instead |
| Different org auth | Settings not delivered for accounts outside managed org |
| User configures third-party model provider | **Server-managed settings BYPASSED** (Bedrock/Mantle/Vertex/Foundry/non-default base URL) |

For stronger guarantees: endpoint-managed settings on MDM-enrolled devices. Use `ConfigChange` hooks to log/block runtime config changes.
