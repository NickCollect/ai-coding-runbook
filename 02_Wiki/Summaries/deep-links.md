---
type: summary
source: 01_Raw/code.claude.com/docs/en/deep-links.md
source_url: https://code.claude.com/docs/en/deep-links
title: "Launch sessions from links"
summarized_at: 2026-05-05
entities_referenced: [Native-interface, IDE-integration, Settings]
concepts_referenced: []
---

`claude-cli://` is a custom URL scheme registered with the OS the first time you start an interactive `claude` session. Clicking a link launches Claude Code in a new terminal window with cwd set and prompt pre-filled. **Requires Claude Code v2.1.91+.** The prompt is **typed but NOT sent** until you press Enter.

**URL form**: only path accepted is `claude-cli://open?...`. Parameters:
- `q` — pre-fill prompt text. URL-encoded; `%0A` for newlines. Max 5,000 chars.
- `cwd` — absolute working dir path. Network/UNC paths rejected.
- `repo` — `owner/name` GitHub slug. Resolves to a local clone Claude Code has previously seen (most recently used). If no match → opens home dir.

If both `cwd` and `repo` passed → `cwd` wins. Use `cwd` for standardized paths (devcontainers); `repo` for shared links across teammates.

**Banner** above input shows it was launched externally + which dir was selected. Long prompts (>1,000 chars) get a "scroll and review" warning.

**Use cases**: incident runbooks, monitoring alerts, READMEs, CI failure notifications.

**GitHub-rendered Markdown strips `claude-cli://`** — only label shows, URL hidden. Workaround: put the link in a code block so users can copy-paste.

**Open from shell**:
- macOS: `open "claude-cli://open?repo=acme/payments&q=review%20open%20PRs"`
- Linux: `xdg-open "claude-cli://..."`
- Windows PowerShell: `Start-Process "claude-cli://..."`; `cmd.exe`: `start "" "claude-cli://..."`

**Handler locations**:
- macOS: `~/Applications/Claude Code URL Handler.app`
- Linux: `claude-code-url-handler.desktop` under `$XDG_DATA_HOME/applications`
- Windows: `HKEY_CURRENT_USER\Software\Classes\claude-cli`

**Terminal selection**: macOS remembers most recent (iTerm2, Ghostty, kitty, Alacritty, WezTerm, Terminal.app). Linux honors `$TERMINAL` → `x-terminal-emulator` → fallbacks. Windows: Windows Terminal → PowerShell → cmd.exe.

**Disable registration**: set `disableDeepLinkRegistration: "disable"` in settings.json (or managed settings to enforce org-wide).

**VS Code extension** has its own scheme `vscode://anthropic.claude-code/open` for opening a tab instead of terminal.

**Troubleshooting**: link does nothing → handler not registered, run `claude` once. Wrong terminal → see selection rules. Session opens in home dir → `repo` slug never seen by Claude Code, run `claude` inside the clone once or use `cwd`.
