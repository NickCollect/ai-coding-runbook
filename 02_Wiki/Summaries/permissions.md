---
type: summary
source: 01_Raw/code.claude.com/docs/en/agent-sdk/permissions.md
source_url: https://code.claude.com/docs/en/agent-sdk/permissions
title: "Configure permissions (Agent SDK)"
summarized_at: 2026-05-05
entities_referenced: [Agent-SDK, Permission-mode, Hooks, Auto-mode, Subagent, Settings]
concepts_referenced: []
---

Defines the Agent SDK's permission system: modes, allow/deny rules, the runtime `canUseTool` callback, and the order in which they're evaluated.

**Evaluation order** (first match wins, top to bottom):
1. **Hooks** — can allow, deny, or pass through.
2. **Deny rules** (`disallowed_tools` + settings.json `permissions.deny`). Deny always wins, even in `bypassPermissions`.
3. **Permission mode**:
   - `bypassPermissions` approves everything reaching this step
   - `acceptEdits` approves file ops + filesystem commands
   - other modes fall through.
4. **Allow rules** (`allowed_tools` + settings.json allow).
5. **`canUseTool` callback** — runtime approval. Skipped in `dontAsk` mode (auto-deny).

**Allow/deny rules** (`allowed_tools`/`disallowed_tools`, TS: `allowedTools`/`disallowedTools`) control approval, NOT availability. `allowedTools=["Read","Grep"]` auto-approves those; everything else falls through. `disallowedTools=["Bash"]` blocks Bash absolutely. **Critical gotcha**: `allowed_tools` does NOT constrain `bypassPermissions` — pairing `allowed_tools=["Read"]` with `bypassPermissions` still approves every tool. To lock down, use `dontAsk` + `allowedTools` instead. To block specific tools under `bypassPermissions`, use `disallowedTools`.

Declarative rules also live in `.claude/settings.json` and apply when `project` settingSource is enabled (default for `query()`).

**Permission modes**:
| Mode | Behavior |
|------|----------|
| `default` | No auto-approvals; unmatched tools call `canUseTool` |
| `dontAsk` | Anything not pre-approved is denied; never calls `canUseTool` |
| `acceptEdits` | Auto-approve Edit/Write + `mkdir`, `touch`, `rm`, `rmdir`, `mv`, `cp`, `sed` (only inside cwd or `additionalDirectories`; protected paths still prompt) |
| `bypassPermissions` | Approve everything; hooks still run; cannot run as root on Unix |
| `plan` | No tool execution; Claude plans only; may use `AskUserQuestion` |
| `auto` (TS only) | Model classifier per call (see Auto-mode) |

**Subagent inheritance gotcha**: When the parent uses `bypassPermissions`, `acceptEdits`, or `auto`, all subagents inherit and **cannot override**. Combined with subagents potentially having less constrained system prompts, inheriting `bypassPermissions` grants subagents full autonomous system access.

Set the mode at query time via `permissionMode` option, or change mid-session via `setPermissionMode()` (TS) / `set_permission_mode()` (Python) — useful pattern: start strict, loosen after reviewing initial actions.
