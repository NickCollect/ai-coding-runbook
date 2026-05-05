---
type: summary
source: 01_Raw/code.claude.com/docs/en/computer-use.md
source_url: https://code.claude.com/docs/en/computer-use
title: "Let Claude use your computer from the CLI"
summarized_at: 2026-05-05
entities_referenced: [Computer-use, MCP-server, IDE-integration, Sandboxing, Native-interface, Enterprise-gateway, Headless-mode]
concepts_referenced: []
---

Computer use in the **CLI** (research preview, **macOS only**, requires Pro/Max plan, Claude Code v2.1.85+, interactive mode only — no `-p`). Implemented as a built-in MCP server named `computer-use`, off by default. NOT available via Bedrock/Vertex/Foundry. Cross-platform (macOS + Windows) availability exists in the Desktop app.

**When Claude reaches for it**: it's the broadest and slowest interaction tier. Tier order Claude tries: MCP server for the service → Bash → Chrome (if enabled) → Computer use. Reserved for native apps, simulators, and tools without an API/CLI.

**Enable steps**: `/mcp` → find `computer-use` (per-project setting) → Enable. First use prompts for macOS Accessibility (click/type/scroll) and Screen Recording (see screen) permissions. Restart Claude Code may be needed after Screen Recording grant.

**Per-app session approval**: enabling the server doesn't grant access to every app. First time Claude needs an app in a session, terminal prompts list which apps are needed, extra perms (clipboard, etc.), and how many other apps will be hidden. Approvals last for current session only.

Apps with broad reach show extra warnings:
- "Equivalent to shell access" → Terminal, iTerm, VS Code, Warp, etc.
- "Can read or write any file" → Finder
- "Can change system settings" → System Settings

App tier control (matches Desktop): browsers and trading platforms = view-only, terminals/IDEs = click-only, everything else = full control.

**Operational details**:
- Machine-wide lock (one Claude session at a time controls computer). Crashed sessions auto-release.
- While Claude works, other apps are hidden so it interacts only with approved ones; restored on turn end. Terminal stays visible AND is excluded from screenshots — Claude never sees its own output.
- Screenshots automatically downscaled (16" MBP Retina 3456×2234 → ~1372×887). No setting to change target. If text/controls too small for Claude to read, increase in-app size, not display res.
- macOS notification "Claude is using your computer · press Esc to stop" appears. **Esc** (anywhere) or **Ctrl+C** (terminal) aborts immediately, releases lock, restores hidden apps. Escape key press is consumed so prompt injection can't use it to dismiss dialogs.

**Trust boundary** different from sandboxed Bash: runs on real desktop, no sandbox. Per-app approval, sentinel warnings, terminal screenshot exclusion, global escape, and lock file are the built-in guardrails.

**CLI vs Desktop differences**:
| Feature | Desktop | CLI |
|---|---|---|
| Platforms | macOS + Windows | macOS only |
| Enable | Settings > General | `/mcp` Enable |
| Denied apps list | Configurable | Not yet |
| Auto-unhide | Optional | Always on |
| Dispatch integration | Yes | N/A |

**Troubleshooting**: lock-held messages, persistent permission re-prompts (restart Claude Code, check System Settings), `computer-use` missing from `/mcp` (not macOS, old version, wrong plan, third-party provider, non-interactive mode).
