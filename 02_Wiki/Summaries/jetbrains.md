---
type: summary
source: 01_Raw/code.claude.com/docs/en/jetbrains.md
source_url: https://code.claude.com/docs/en/jetbrains
title: "JetBrains IDEs"
summarized_at: 2026-05-05
entities_referenced: [IDE-integration, Permission-mode]
concepts_referenced: []
---

Claude Code JetBrains plugin: works with IntelliJ IDEA, PyCharm, Android Studio, WebStorm, PhpStorm, GoLand. Install from JetBrains Marketplace ([Claude Code plugin page](https://plugins.jetbrains.com/plugin/27310-claude-code-beta-)), restart IDE.

Features:
- Quick launch: `Cmd+Esc` (Mac) / `Ctrl+Esc` (Windows/Linux).
- Diff viewing in IDE diff viewer (set via `/config` diff tool = `auto` vs `terminal`).
- Selection / current tab automatically shared with Claude Code.
- File reference shortcut: `Cmd+Option+K` / `Alt+Ctrl+K` inserts `@src/auth.ts#L1-99`.
- Diagnostic sharing: lint / syntax errors flow to Claude automatically.

Usage: Run `claude` from IDE integrated terminal, OR run `claude` in any external terminal then `/ide` to connect.

Settings (Settings → Tools → Claude Code [Beta]):
- **Claude command** — custom path, e.g. `claude`, `/usr/local/bin/claude`, `npx @anthropic-ai/claude-code`. WSL: `wsl -d Ubuntu -- bash -lic "claude"`.
- Suppress missing-command notification.
- Option+Enter for multiline (macOS only; needs terminal restart).
- Auto-update plugin on restart.
- ESC key fix: if ESC doesn't interrupt, go to Settings → Tools → Terminal and uncheck "Move focus to the editor with Escape" or remove that keybinding.

Special configurations:
- **Remote Development**: install plugin on the remote host, NOT the local client (Settings → Plugin (Host)).
- **WSL2**: "No available IDEs detected" usually = NAT networking or Windows Firewall blocking WSL2↔IDE on Windows host. WSL1 unaffected. Two fixes: (a) Windows Firewall rule allowing internal traffic on your WSL2 subnet (`hostname -I` to find subnet, `New-NetFirewallRule -DisplayName "Allow WSL2 Internal Traffic" -Direction Inbound -Protocol TCP -Action Allow ...`); (b) switch WSL2 to mirrored networking (Win 11 22H2+) by adding `[wsl2]\nnetworkingMode=mirrored` to `.wslconfig` and `wsl --shutdown`.

Security note: in JetBrains IDEs with auto-edit enabled, Claude can modify IDE config files which may be auto-executed by the IDE — potentially bypassing Bash permission prompts. Use manual approval mode for sensitive prompts; only use trusted prompts.

Troubleshooting: plugin not working → restart IDE multiple times, run from project root. IDE not detected → restart, run from integrated terminal. Command not found → verify `claude --version`, set Claude command path, use WSL format.
