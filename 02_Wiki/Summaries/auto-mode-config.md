---
type: summary
source: 01_Raw/code.claude.com/docs/en/auto-mode-config.md
source_url: https://code.claude.com/docs/en/auto-mode-config
title: "Configure auto mode"
summarized_at: 2026-05-05
entities_referenced: [Auto-mode, Permission-mode, Settings, Hooks, Memory]
concepts_referenced: []
---

Auto mode runs Claude Code without permission prompts by routing each tool call through a classifier that blocks irreversible/destructive/exfiltration-suspect actions. The `autoMode` settings block tells the classifier which infrastructure your org trusts.

**Plan availability**: Max, Team, Enterprise, and API plans (Anthropic API). NOT on Pro, Bedrock, Vertex, Foundry.

By default the classifier trusts only the cwd and the current repo's configured remotes. Pushes to your company's source-control org or writes to team buckets are blocked until added to `autoMode.environment`.

**Config scopes** (additive, no removal of stricter org rules):
- `~/.claude/settings.json` — single dev
- `.claude/settings.local.json` — per-project, gitignored
- Managed settings — org-wide
- `--settings` flag / Agent SDK — per-invocation

The classifier does NOT read `autoMode` from shared `.claude/settings.json` (so a checked-in repo cannot inject allow rules). Also reads CLAUDE.md content for behavioral rules ("never force push").

**Three fields**:
- `autoMode.environment` — prose descriptions of trusted infra (org, source control, cloud buckets, internal domains, key services, regulatory context)
- `autoMode.allow` — exception rules overriding blocks
- `autoMode.soft_deny` — additional block rules

Use the literal `"$defaults"` to splice in built-in entries; **omitting `$defaults` discards all built-in rules in that section** (dangerous — discards force-push protection, exfil blocks, `curl | bash` blocks, etc.).

**Precedence**: soft_deny → allow overrides matching blocks → explicit user intent overrides both (only if message specifically describes the action; "clean up the repo" doesn't authorize force-push, but "force-push this branch" does).

For absolute hard-blocks regardless of intent, use `permissions.deny` (runs before classifier).

**CLI inspection**:
- `claude auto-mode defaults` — print built-in rules JSON
- `claude auto-mode config` — effective config with `$defaults` expanded
- `claude auto-mode critique` — AI feedback on custom rules

**Denial review**: `/permissions` "Recently denied" tab; press `r` to mark for retry. Repeated denials usually mean missing context — extend `environment`. Programmatic reaction via `PermissionDenied` hook.
