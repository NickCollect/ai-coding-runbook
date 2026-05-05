---
type: summary
source: 01_Raw/code.claude.com/docs/en/permission-modes.md
source_url: https://code.claude.com/docs/en/permission-modes
title: "Choose a permission mode"
summarized_at: 2026-05-05
entities_referenced: [Permission-mode, Auto-mode, Settings, Hooks, Subagent, Sandboxing, Headless-mode]
concepts_referenced: []
---

Permission modes control when Claude Code prompts before file edits, shell commands, network requests. Six modes:

| Mode | What runs without asking | Best for |
|---|---|---|
| `default` | Reads only | Sensitive work, getting started |
| `acceptEdits` | Reads, edits, common FS bash (`mkdir`, `touch`, `mv`, `cp`, `rm`, `rmdir`, `sed`) | Iterating on code |
| `plan` | Reads only (plus exploration) — no edits | Exploring before changing |
| `auto` | Everything, with classifier safety checks | Long tasks, fewer prompts |
| `dontAsk` | Only pre-approved tools | Locked CI / scripts |
| `bypassPermissions` | Everything | Containers / VMs |

**Switch modes**:
- CLI: `Shift+Tab` cycles `default → acceptEdits → plan` (with `bypassPermissions`/`auto` slotting in if enabled). Status bar shows current. `--permission-mode <mode>` at startup. `defaultMode` in settings for persistent default.
- VS Code: bottom-of-prompt indicator. `claudeCode.initialPermissionMode` setting (does NOT accept `auto`).
- JetBrains: same as CLI (terminal-based).
- Desktop: mode selector next to send button.
- Web/mobile: Cloud sessions limited to "Auto accept edits" + "Plan mode". Remote Control sessions have Ask/Auto-accept/Plan; no Auto/Bypass.

**Plan mode** specifics: research + propose, no edits. Enter via `Shift+Tab`, prefix `/plan`, or `--permission-mode plan`. Approval menu offers: approve→auto, approve→accept edits, approve→manual review, keep planning, refine via Ultraplan. `Ctrl+G` opens plan in editor for direct edit. Accepting auto-names the session from plan content (unless renamed).

**`acceptEdits` mode** auto-approves common FS bash incl. with safe wrappers (`LANG=C`, `NO_COLOR=1`, `timeout`, `nice`, `nohup`). Only paths in working dir or `additionalDirectories`. Protected paths still prompt. Also auto-approves PowerShell `Set-Content`/`Add-Content`/`Clear-Content`/`Remove-Item` if PowerShell tool enabled.

**Auto mode** (v2.1.83+, research preview):
- Requirements: Max/Team/Enterprise/API plan (NOT Pro); admin-enabled on Team/Enterprise; specific models — Sonnet 4.6/Opus 4.6/Opus 4.7 (Max only Opus 4.7); Anthropic API only (NOT Bedrock/Vertex/Foundry).
- Classifier model reviews every action; trusts working dir + repo's configured remotes.
- Blocked by default: `curl|bash`, sending sensitive data externally, prod deploys/migrations, mass cloud delete, IAM changes, shared infra modify, irreversible destruction of pre-session files, force push, push to `main`.
- Allowed by default: local file ops, deps in lock files, `.env` reads → matching API, read-only HTTP, push to current branch.
- "Boundaries you state in conversation" act as block signals — re-read from transcript on each check (so compaction can lose them; use deny rules for hard guarantees).
- Fallback: 3 consecutive blocks or 20 total → mode pauses and prompting resumes. Headless `-p` aborts on repeated blocks (no user to prompt).
- Decision order: allow/deny rules → reads/in-scope edits (auto-approved unless protected path) → classifier → if blocked, Claude tries alternative.
- On entering auto: drops blanket `Bash(*)`/`PowerShell(*)`, wildcarded interpreters, `Agent` rules. Restored on leaving.
- Subagents: classifier checks delegated task at spawn, each subagent action, full action history at completion. Subagent `permissionMode` frontmatter is **ignored** in auto mode.
- Classifier sees user msgs + tool calls + CLAUDE.md (NOT tool results) — tool result content can't manipulate it directly. Server-side probe scans incoming tool results for suspicious content.

**`dontAsk`** = auto-deny everything not in `permissions.allow` + read-only bash. Fully non-interactive. `ask` rules become deny.

**`bypassPermissions`** = no checks. Entry-flag-gated: must launch with `--permission-mode bypassPermissions` / `--dangerously-skip-permissions` / `--allow-dangerously-skip-permissions`. v2.1.126+ skips even protected paths. `rm -rf /` and `rm -rf ~` still prompt as circuit breaker.

**Protected paths** (never auto-approved except in bypass): `.git`, `.vscode`, `.idea`, `.husky`, `.claude` (except `commands`/`agents`/`skills`/`worktrees`), and files: `.gitconfig`, `.gitmodules`, shell rc files, `.ripgreprc`, `.mcp.json`, `.claude.json`.
