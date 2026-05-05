---
type: summary
source: 01_Raw/code.claude.com/docs/en/desktop.md
source_url: https://code.claude.com/docs/en/desktop
title: "Use Claude Code Desktop"
summarized_at: 2026-05-05
entities_referenced: [Native-interface, IDE-integration, Computer-use, Permission-mode, Auto-mode, Plugin, Skill, MCP-server, Hooks, Memory, Settings, Routine, Scheduled-task, Headless-mode, Checkpointing, Enterprise-gateway]
concepts_referenced: [Channel, Agent-team, Context-window]
---

Reference for the **Code** tab in Claude Desktop (macOS/Windows; Linux uses CLI). Three tabs: Chat, Cowork (Dispatch + longer agentic work), Code.

**Sessions**: each Code tab session has its own chat history, project folder, and code changes. Sidebar lists sessions, can run multiple in parallel. For Git repos, each session gets isolated copy via **Git worktrees** (default `<project-root>/.claude/worktrees/`). Add `.worktreeinclude` to copy gitignored files like `.env`. Auto-archive after PR merge/close is opt-in.

**Session config (set before first message)**: Environment (Local / Remote / SSH), Project folder (multiple repos for remote), Model dropdown, Permission mode.

**Permission modes** in Desktop:
- *Ask permissions* (`default`) — prompts for everything
- *Auto accept edits* (`acceptEdits`) — auto-approve file edits + common FS commands
- *Plan mode* (`plan`) — read-only exploration + plan
- *Auto* (`auto`) — research preview, Max/Team/Enterprise/API only (NOT Pro/third-party); Sonnet 4.6 / Opus 4.6 / Opus 4.7 only on Team/Enterprise/API; Opus 4.7 only on Max
- *Bypass permissions* (`bypassPermissions`) — equivalent to `--dangerously-skip-permissions`; gated behind a Settings toggle; admin-disable possible
- `dontAsk` is **CLI-only**

Remote sessions: support Auto-accept-edits and Plan mode only (Ask not available since they auto-accept by default; Bypass not available because environment is already sandboxed).

**Workspace panes**: chat, diff, preview, terminal, file, plan, tasks, subagent. Drag to rearrange/resize. Cmd/Ctrl+\\ closes focused pane. Requires Desktop v1.2581.0+.

**Preview pane**: Claude can launch dev server (config in `.claude/launch.json`, supports JSON-with-comments), interact with embedded browser, screenshot/inspect/click. **`autoVerify: true`** by default — Claude verifies edits after every change. Configuration fields: `name`, `runtimeExecutable`, `runtimeArgs`, `port`, `cwd`, `env`, `autoPort` (true|false|unset = ask), `program`+`args` (for `node script.js` style).

**Diff view**: comment on lines (Cmd/Ctrl+Enter to submit batch). "Review code" button asks Claude to evaluate. Focus is high-signal: compile errors, logic bugs, security issues — not lint/style.

**PR monitoring**: GitHub CLI `gh` polls check results. **Auto-fix** + **Auto-merge** (squash; requires repo-side enablement) toggles. Desktop notification on CI completion.

**Other features**:
- **Side chat** (`Cmd/Ctrl+;` or `/btw`): question that uses session context but doesn't append to main thread
- **Tasks pane**: subagents, background shells, workflows
- **Continue in...**: send local session to web (Claude Code on Web; pushes branch + summary) or open in IDE
- **Dispatch sessions**: Cowork-spawned Code sessions appear with "Dispatch" badge; phone push notifications; computer-use approvals expire after 30 min instead of full session
- **Connectors**: MCP servers with graphical setup; manage via `+` button or Settings → Connectors
- **Skills + Plugins**: `+` button opens browsers; plugin manager UI; not available in remote sessions
- **`/desktop` slash command** in CLI moves the current session into Desktop

**Computer use**: macOS + Windows; Pro/Max only (not Team/Enterprise); off by default; toggle in Settings → General. macOS needs Accessibility + Screen Recording. Per-app session approval; tier table (View only / Click only / Full control). Denied apps list configurable; "unhide apps when finished" toggle.

**Environment configuration**:
- *Local* — desktop doesn't fully inherit shell env. macOS reads `~/.zshrc`/`~/.bashrc` for PATH + Claude Code vars only; Windows inherits user/system vars but not PowerShell profiles. Use **local environment editor** (env dropdown gear icon) to set encrypted vars for local sessions and dev servers.
- *Remote* — Anthropic-hosted; continues if app closes; no separate compute charge.
- *SSH* — connect to your own boxes (Linux/macOS only). Configure via "+ Add SSH connection" with name/host/port/identity. `sshConfigs` managed setting can pre-distribute connections; users can't edit/delete managed entries.

**Extended thinking** on by default; disable via `MAX_THINKING_TOKENS=0`. On Opus 4.6 / Sonnet 4.6 set `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING=1` for fixed budget; Opus 4.7 is always adaptive.

**Enterprise**: admin console controls (Code in Desktop / Web, Remote Control, Disable Bypass), managed settings (`permissions.disableBypassPermissionsMode`, `disableAutoMode`, `autoMode` (NOT read from checked-in `.claude/settings.json` — clones can't inject classifier rules), `sshConfigs`). MDM (`com.anthropic.Claude` macOS preference domain; `SOFTWARE\Policies\Claude` Windows registry).

**CLI vs Desktop**: same engine, shared CLAUDE.md / settings / MCP / hooks / skills. Not in Desktop: third-party providers (Bedrock/Foundry; Vertex via enterprise managed settings only), Linux, inline code suggestions, Agent teams (CLI/SDK only), `--print`/scripting.
