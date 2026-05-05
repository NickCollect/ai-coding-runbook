---
type: summary
source: 01_Raw/code.claude.com/docs/en/remote-control.md
source_url: https://code.claude.com/docs/en/remote-control
title: "Continue local sessions from any device with Remote Control"
summarized_at: 2026-05-05
entities_referenced: [Native-interface, MCP-server, IDE-integration, Sandboxing, Permission-mode]
concepts_referenced: []
---

Remote Control lets you drive a local Claude Code session from claude.ai/code or the Claude mobile app. Session keeps running on your machine — nothing moves to cloud. Research preview, available on all plans (off by default on Team/Enterprise; admin-enabled). Requires Claude Code v2.1.51+.

Key benefit vs Claude Code on the web: your local filesystem, MCP servers, tools, project config all stay available. `@` autocompletes from local project. The web/mobile is just a window.

**Requirements**: Pro/Max/Team/Enterprise (no API keys), claude.ai login (`/login`), workspace trust accepted at least once.

**Start sessions** (3 CLI modes + VS Code):
- **Server mode**: `claude remote-control` — long-running server, displays URL + spacebar shows QR. Flags:
  - `--name "..."` custom title
  - `--remote-control-session-name-prefix <prefix>` (default = hostname → `myhost-graceful-unicorn`)
  - `--spawn same-dir|worktree|session` — default same-dir; worktree gives each session a git worktree; session = single-session mode rejecting additional connections. Press `w` at runtime to toggle same-dir↔worktree.
  - `--capacity <N>` (default 32; not with `--spawn=session`)
  - `--verbose`, `--sandbox`/`--no-sandbox`
- **Interactive session**: `claude --remote-control` (or `--rc`) — full interactive terminal session that's ALSO available remotely.
- **From existing session**: `/remote-control` (or `/rc`) — carries over conversation. No `--verbose`/`--sandbox` flags here.
- **VS Code**: `/remote-control` in prompt box (v2.1.79+). Banner shows status; click "Open in browser".

**Connect from another device**: open session URL, scan QR, or find by name in claude.ai/code session list (computer icon + green dot).

**Session title precedence**: explicit `--name` > `/rename` > last meaningful message > auto-generated `myhost-foo-bar`.

**Enable for ALL sessions**: `/config` → "Enable Remote Control for all sessions" → true. Each interactive process registers one remote session. Multiple instances → multiple sessions. For multi-session from one process, use server mode.

**Connection model**: outbound HTTPS only, no inbound ports. Polls for work via Anthropic API. Multiple short-lived credentials, each scoped/expiring independently. All TLS.

**Mobile push notifications** (v2.1.110+): Claude decides when to push (typically long task done or needs decision). Can request via "notify me when tests finish". `/config` → "Push when Claude decides".

**Limitations**:
- One remote session per interactive process (use server mode for multi).
- Local process must keep running (close terminal = session ends).
- ~10 min network outage → session times out + process exits.
- Ultraplan disconnects Remote Control (both occupy claude.ai/code).
- Local-only commands: `/mcp`, `/plugin`, `/resume` (interactive pickers).

**Troubleshooting**:
- "requires claude.ai subscription" → unset `ANTHROPIC_API_KEY`, use `claude auth login`.
- "requires full-scope login token" → `claude setup-token` / `CLAUDE_CODE_OAUTH_TOKEN` are inference-only; need `claude auth login`.
- "disabled by org policy" → 3 causes: API-key login, admin hasn't enabled, or DLP/compliance config blocking (admin toggle grayed out → contact Anthropic).
- Telemetry disablers (`CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`, `DISABLE_TELEMETRY`) and 3rd-party providers (`CLAUDE_CODE_USE_BEDROCK`/`VERTEX`/`FOUNDRY`) block Remote Control.

**Comparison table** vs Dispatch / Channels / Slack / Scheduled tasks: Remote Control's distinctive trait = drive an in-progress local session from another device.
