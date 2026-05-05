---
type: summary
source: 01_Raw/code.claude.com/docs/en/desktop-quickstart.md
source_url: https://code.claude.com/docs/en/desktop-quickstart
title: "Get started with the desktop app"
summarized_at: 2026-05-05
entities_referenced: [Native-interface, Permission-mode, Plugin, Skill, Slash-command, Scheduled-task]
concepts_referenced: []
---

Install and first-session walkthrough for Claude Code Desktop (macOS, Windows x64, Windows ARM64). Linux users use the CLI. Requires Pro/Max/Team/Enterprise subscription.

Three tabs in the desktop app:
- **Chat** — claude.ai-style conversation, no file access.
- **Cowork** — autonomous background agent in a cloud VM.
- **Code** — interactive coding assistant with local file access. This page focuses on Code.

Desktop bundles Claude Code internally — no separate Node.js or CLI install needed. To use `claude` from the terminal, install the CLI separately.

First-session steps:
1. Open the **Code** tab. (403 → see auth troubleshooting.)
2. Choose environment: **Local** (uses your files; needs Git on Windows), **Remote** (Anthropic cloud, persists if app closed; same infra as Claude Code on the web), or **SSH** (auto-installs Claude Code on remote first time).
3. Pick model from dropdown.
4. Type the task (e.g., "Find a TODO and fix it").
5. Default permission mode is **Ask** — diff view + Accept/Reject buttons per change.

Things to try after first edit:
- Interrupt + steer (stop button or just type correction + Enter).
- `@filename` to pull files; drag-drop or attachment button for images/PDFs.
- `/` or **+ → Slash commands** to browse built-in commands, custom skills, plugin skills.
- `+12 -1` indicator → opens diff view; click Review code for Claude self-review.
- Permission modes: Ask (default), Auto accept edits, Plan mode.
- **+ → Plugins** to install plugin marketplaces.
- Drag panes to rearrange (chat / diff / terminal / file / preview). `Ctrl+\`` opens terminal.
- **Preview** dropdown runs your dev server in-app; Claude can inspect logs, test endpoints.
- PR monitoring: Claude tracks CI checks after PR open, can auto-fix failures or auto-merge when green.
- Scheduled tasks (desktop) for recurring runs.
- Sidebar manages parallel sessions, each in its own git worktree. Tasks pane watches background subagents/commands. Side chat for off-thread questions. "Run remotely" sends long tasks to cloud. "Continue in another surface" hands off to web/IDE.

Desktop and CLI share configuration: CLAUDE.md, MCP servers, hooks, skills, settings. They can run simultaneously on the same project.
