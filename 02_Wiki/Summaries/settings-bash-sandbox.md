---
type: summary
source: 01_Raw/github/anthropics/claude-code/examples/settings/settings-bash-sandbox.json
title: "Example settings: settings-bash-sandbox.json"
summarized_at: 2026-05-05
entities_referenced: [Settings, Sandboxing, Permission-mode]
concepts_referenced: []
---

Example managed-settings file from `anthropics/claude-code/examples/settings/`. Locks Bash to run inside the sandbox with everything denied by default — minimum-privilege starting point.

Schema:
```json
{
  "allowManagedPermissionRulesOnly": true,
  "sandbox": {
    "enabled": true,
    "autoAllowBashIfSandboxed": false,
    "allowUnsandboxedCommands": false,
    "excludedCommands": [],
    "network": {
      "allowUnixSockets": [],
      "allowAllUnixSockets": false,
      "allowLocalBinding": false,
      "allowedDomains": [],
      "httpProxyPort": null,
      "socksProxyPort": null
    },
    "enableWeakerNestedSandbox": false
  }
}
```

**What it enforces**:
- `allowManagedPermissionRulesOnly: true` — user/project allow/ask/deny rules are ignored, only managed rules apply
- `sandbox.enabled: true` — sandbox is on
- `autoAllowBashIfSandboxed: false` — sandboxed bash still requires the regular permission flow (no auto-allow)
- `allowUnsandboxedCommands: false` — disables the `dangerouslyDisableSandbox` escape hatch entirely; commands MUST run sandboxed or be in `excludedCommands`
- `excludedCommands: []` — nothing escapes
- All network sockets denied (no Unix sockets, no local binding, no allowed domains)
- `enableWeakerNestedSandbox: false` — Linux sandbox uses strong namespace mode (won't fall back to weak Docker-compatible mode)

Effect: Bash runs sandboxed without escape, no network reachable until an admin adds an `allowedDomains` entry, and users cannot loosen any permission/sandbox rules. Pair with deny rules for WebFetch/WebSearch in a stricter file (see `settings-strict.json`).
