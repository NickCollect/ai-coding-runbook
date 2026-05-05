---
type: summary
source: 01_Raw/code.claude.com/docs/en/terminal-config.md
source_url: https://code.claude.com/docs/en/terminal-config
title: "Configure your terminal for Claude Code"
summarized_at: 2026-05-05
entities_referenced: [Hooks, Settings, Status-line]
concepts_referenced: []
---

Per-terminal-emulator config recipes for Claude Code. Default install works; this is symptom-driven.

**Multiline input**: Enter submits. `Ctrl+J` or `\` then Enter always works for newline. `Shift+Enter` support varies:
- Works out of box: Ghostty, Kitty, iTerm2, WezTerm, Warp, Apple Terminal.
- Run `/terminal-setup` once: VS Code, Cursor, Windsurf, Alacritty, Zed (writes config files; in VS Code/Cursor/Windsurf also tunes `terminal.integrated.mouseWheelScrollSensitivity`).
- Not available: Windows Terminal, gnome-terminal, JetBrains IDEs (use `Ctrl+J`).
- Inside tmux: needs tmux config (below) even if outer terminal supports it.
- Remap `chat:newline` / `chat:submit` actions in keybindings file to swap.

**macOS Option key**: most terminals don't send Option as Meta by default — Option+Enter / Option+P shortcuts dead.
- Apple Terminal: Settings → Profiles → Keyboard → "Use Option as Meta Key". (`/terminal-setup` does this + flips audio bell to visual.)
- iTerm2: Settings → Profiles → Keys → General → Left/Right Option = "Esc+". `/terminal-setup` also enables clipboard access for `/copy`. Restart needed.
- VS Code: `"terminal.integrated.macOptionIsMeta": true`.

**Notifications / terminal bell**:
- Default: desktop notifications in Ghostty/Kitty/iTerm2 only. Other terminals → set `preferredNotifChannel: "terminal_bell"`.
- iTerm2 needs forwarding: Settings → Profiles → Terminal → "Notification Center Alerts" + Filter Alerts → "Send escape sequence-generated alerts".
- Notifications travel over SSH so remote sessions still alert.
- For custom sounds: `Notification` hook (e.g. `afplay /System/Library/Sounds/Glass.aiff` on macOS).

**tmux config** (`~/.tmux.conf`):
```
set -g allow-passthrough on
set -s extended-keys on
set -as terminal-features 'xterm*:extkeys'
```
Then `tmux source-file ~/.tmux.conf`. `allow-passthrough` lets notifications/progress reach outer terminal; `extended-keys` enables Shift+Enter distinction.

**Themes**: `/theme` or `/config` theme picker. Auto detects OS light/dark. Custom themes (v2.1.118+) live in `~/.claude/themes/<slug>.json` with optional `name`, `base` (`dark`/`light`/`dark-daltonized`/`light-daltonized`/`dark-ansi`/`light-ansi`), `overrides` map. Hot-reloaded.
- Color values: `#rrggbb`, `#rgb`, `rgb(r,g,b)`, `ansi256(n)`, `ansi:<name>`.
- Token categories: text/accent (`claude`, `text`, `inactive`, etc.), status (`success`/`error`/`warning`/`merged`), input/mode (`promptBorder`, `planMode`, `autoAccept`, `bashBorder`, `ide`, `fastMode`), diff rendering (`diffAdded`/`diffRemoved`/word variants), fullscreen backgrounds, usage meter, speaker labels. Shimmer variants for spinners. Subagent named colors `<name>_FOR_SUBAGENTS_ONLY`. Rainbow tokens for `ultrathink`/`ultraplan`.

**Fullscreen rendering** (`/tui fullscreen` or `CLAUDE_CODE_NO_FLICKER=1`): dedicated screen buffer prevents flicker / scrollback jumps. Adds mouse scroll/select. Use PageUp inside Claude Code instead of terminal scrollback.

**Large pastes**: >10,000 chars collapsed to `[Pasted text]`. VS Code integrated terminal can drop chars on huge pastes — write to file and ask Claude to read instead.

**Vim editor mode**: enable via `/config` → Editor mode, or `editorMode: "vim"`. NORMAL/VISUAL mode subset (`hjkl`, `v`/`V`, `d`/`c`/`y` with text objects). Enter still submits in INSERT; use `o`/`O` in NORMAL or `Ctrl+J` for newline. Not remappable through keybindings file.
