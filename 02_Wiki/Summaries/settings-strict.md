---
type: summary
source: 01_Raw/github/anthropics/claude-code/examples/settings/settings-strict.json
title: "settings-strict.json example"
summarized_at: 2026-05-05
entities_referenced: [Settings, Permission-mode, Sandboxing, Hooks, Plugin-marketplace]
concepts_referenced: []
---

Example "strict" Claude Code settings file from the official repo. Demonstrates a fully locked-down configuration:

- `permissions.disableBypassPermissionsMode: "disable"` — kills `--dangerously-skip-permissions` / `bypassPermissions` mode.
- `permissions.ask: ["Bash"]` — Bash always prompts.
- `permissions.deny: ["WebSearch", "WebFetch"]` — block web tools entirely.
- `allowManagedPermissionRulesOnly: true` — only managed (admin-pushed) permission rules apply; user can't add their own.
- `allowManagedHooksOnly: true` — same idea for hooks.
- `strictKnownMarketplaces: []` — empty allowlist of plugin marketplaces (locks plugins out).
- `sandbox`:
  - `autoAllowBashIfSandboxed: false` — even sandboxed Bash needs approval.
  - `network.allowAllUnixSockets: false`, `allowLocalBinding: false`, `allowedDomains: []`, no allowlisted Unix sockets, no HTTP/SOCKS proxy ports — full network lockdown.
  - `enableWeakerNestedSandbox: false`.

Useful as a template for high-security enterprise deployment.
