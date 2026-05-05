---
type: summary
source: 01_Raw/github/anthropics/claude-code/examples/settings/README.md
title: "Settings Examples (claude-code repo)"
summarized_at: 2026-05-05
entities_referenced: [Settings, Plugin-marketplace, Hooks, Permission-mode, Sandboxing]
concepts_referenced: []
---

Index of community-maintained example `settings.json` files in `anthropics/claude-code/examples/settings/`. Intended primarily as starting points for organization-wide deployments. Authors marked these explicitly as community-maintained, may be unsupported or incorrect.

Three example configs differ along these axes:
| Setting | `settings-lax.json` | `settings-strict.json` | `settings-bash-sandbox.json` |
|---|---|---|---|
| Disable `--dangerously-skip-permissions` | ✓ | ✓ | |
| Block plugin marketplaces | ✓ | ✓ | |
| Block user/project-defined permission allow/ask/deny | | ✓ | ✓ |
| Block user/project-defined hooks | | ✓ | |
| Deny WebFetch and WebSearch tools | | ✓ | |
| Bash tool requires approval | | ✓ | |
| Bash tool must run inside sandbox | | | ✓ |

Files apply at any settings-hierarchy level, but enterprise-only properties (`strictKnownMarketplaces`, `allowManagedHooksOnly`, `allowManagedPermissionRulesOnly`) only take effect when set in **enterprise/managed** settings.

**Tips**: snippets are merge-and-match, files must be valid JSON, test locally first by dropping into `managed-settings.json` / `settings.json` / `settings.local.json` before MDM rollout. **`sandbox` property only applies to Bash tool** — does not apply to Read/Write/WebSearch/WebFetch/MCPs/hooks/internal commands.

For MDM (Jamf, Iru/Kandji, Intune, Group Policy) deployment templates see `../mdm` in the same repo.
