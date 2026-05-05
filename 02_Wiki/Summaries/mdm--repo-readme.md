---
type: summary
source: 01_Raw/github/anthropics/claude-code/examples/mdm/README.md
title: "MDM Deployment Examples (anthropics/claude-code/examples/mdm)"
summarized_at: 2026-05-05
entities_referenced: [Settings, Permission-mode]
concepts_referenced: []
---

Example templates (community-maintained, may be incorrect — user is responsible) for deploying Claude Code managed settings via Jamf, Iru (Kandji), Intune, or Group Policy. All templates encode the same minimal example (`permissions.disableBypassPermissionsMode`).

**Templates provided**:
| File | Use with |
|---|---|
| `managed-settings.json` | Any platform; deploy to system config dir |
| `macos/com.anthropic.claudecode.plist` | Jamf or Iru (Kandji) Custom Settings payload. Preference domain: `com.anthropic.claudecode` |
| `macos/com.anthropic.claudecode.mobileconfig` | Full configuration profile for local testing or MDMs taking complete profile |
| `windows/Set-ClaudeCodePolicy.ps1` | Intune Platform scripts. Writes `managed-settings.json` to `C:\Program Files\ClaudeCode\` |
| `windows/ClaudeCode.admx` + `en-US/ClaudeCode.adml` | Group Policy or Intune Import ADMX. Writes `HKLM\SOFTWARE\Policies\ClaudeCode\Settings` (REG_SZ, single-line JSON) |

**Tips**:
- Replace placeholder `PayloadUUID` and `PayloadOrganization` in `.mobileconfig` with own values (`uuidgen`)
- Test on single machine; confirm `/status` lists source under "Setting sources" — `Enterprise managed settings (plist)` on macOS or `(HKLM)` on Windows
- Settings deployed this way are at top of precedence — cannot be overridden by users
