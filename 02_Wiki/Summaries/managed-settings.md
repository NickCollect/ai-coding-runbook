---
type: summary
source: 01_Raw/github/anthropics/claude-code/examples/mdm/managed-settings.json
title: "Example managed-settings.json (MDM template)"
summarized_at: 2026-05-05
entities_referenced: [Settings, Permission-mode]
concepts_referenced: []
---

Minimal example of Claude Code managed-settings file shipped in `examples/mdm/`. Drop-in template for any platform; deploy to OS-level managed-settings path.

**Content**:
```json
{
  "permissions": {
    "disableBypassPermissionsMode": "disable"
  }
}
```

**Effect**: prevents users from invoking `--dangerously-skip-permissions` / bypass mode. Single most common policy starting point for MDM deployments.

**Where to put it** (per the examples/mdm/README): `/Library/Application Support/ClaudeCode/managed-settings.json` (macOS), `/etc/claude-code/managed-settings.json` (Linux/WSL), `C:\Program Files\ClaudeCode\managed-settings.json` (Windows).

For a fuller list of policy settings users can override, see managed-only settings in the permissions doc summary (`allowManagedHooksOnly`, `allowManagedMcpServersOnly`, etc.).
