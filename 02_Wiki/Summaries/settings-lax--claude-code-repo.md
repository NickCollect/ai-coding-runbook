---
type: summary
source: 01_Raw/github/anthropics/claude-code/examples/settings/settings-lax.json
title: "claude-code-repo: examples/settings/settings-lax.json"
summarized_at: 2026-05-05
entities_referenced: [Settings, Permission-mode, Plugin-marketplace]
concepts_referenced: []
---

Tiny example settings file from the claude-code repo. Two keys:
```json
{
  "permissions": {
    "disableBypassPermissionsMode": "disable"
  },
  "strictKnownMarketplaces": []
}
```

- `permissions.disableBypassPermissionsMode: "disable"` — explicitly disables the protection that prevents `--dangerously-skip-permissions`. (i.e., bypass permissions IS allowed in this "lax" example config.) Note: the value `"disable"` here turns off the disabler — read carefully.
- `strictKnownMarketplaces: []` — empty allowlist; combined with absent `extraKnownMarketplaces`, no marketplace restriction is enforced.

Demonstrates a lenient configuration suitable for personal/dev use; not for orgs.
