---
type: summary
source: 01_Raw/code.claude.com/docs/en/fullscreen.md
source_url: https://code.claude.com/docs/en/fullscreen
title: "Fullscreen rendering"
summarized_at: 2026-05-05
entities_referenced: [Settings]
concepts_referenced: []
---

**Research-preview** opt-in alternate rendering path for the Claude Code CLI. v2.1.89+. Eliminates flicker, keeps memory flat in long conversations, adds mouse support. Draws on terminal's alternate screen buffer (like vim/htop) — only renders visible messages.

Most noticeable in VS Code integrated terminal, tmux, iTerm2 (rendering throughput bottlenecks).

**Enable**: `/tui fullscreen` mid-session (relaunches with conversation intact). Or env `CLAUDE_CODE_NO_FLICKER=1` (equivalent to the `tui` setting). `/tui` alone prints active renderer. Disable: `/tui default` or unset env var.

**What changes**:
- Input box stays fixed at bottom (signal that fullscreen is active)
- Only visible messages in render tree → constant memory regardless of conversation length
- Conversation lives in alt screen buffer, NOT terminal scrollback — so `Cmd+f` and tmux search don't see it

**Mouse capture**:
- Click in prompt → cursor positioning
- Click collapsed tool result → expand/collapse (tool call + result expand together)
- Click URL/file path → open in default app (file paths from Edit/Write tool output open in default app, http(s) in browser)
- Click+drag → in-app text selection; auto-copies on mouse release. Double-click = word (iTerm2 word boundaries; file path = one unit). Triple-click = line.
- Mouse wheel → scroll
- VS Code/xterm.js: `Cmd`-click defers to terminal's link handler to avoid double-open
- `Ctrl+Shift+c` for manual copy. Kitty-protocol terminals (kitty/WezTerm/Ghostty/iTerm2) also support `Cmd+c`. With selection active, `Ctrl+c` copies instead of cancelling.
- Selection extension: `Shift+arrows`, `Shift+Home/End`. `Shift+↑/↓` scrolls viewport at edge.

**Scrolling**: `PgUp/PgDn` (half-screen), `Ctrl+Home` (start), `Ctrl+End` (latest + re-enable auto-follow), wheel. Mac without dedicated keys: `Fn+arrows`. Auto-follow pauses when you scroll up; resume with `Ctrl+End` or scroll-to-bottom. Disable entirely via `/config` → Auto-scroll off (permission prompts still scroll into view).

Mouse wheel requires terminal forwarding; iTerm2 needs Settings → Profiles → Terminal → Enable mouse reporting (also required for click-to-expand and selection). Slow wheel? Set `CLAUDE_CODE_SCROLL_SPEED=3` (1-20; 3 matches vim).

**Search & review**: `Ctrl+o` toggles transcript mode. `/focus` quieter view (your last prompt + one-line tool summaries with diffstats + final response — persists across sessions, toggle off by re-running). Transcript mode uses `less`-style nav: `/` (search), `n`/`N`, `j`/`k`/arrows, `g`/`G`/Home/End, `Ctrl+u`/`Ctrl+d`, `Ctrl+b`/`Ctrl+f`/Space/`b`. Exit: `Ctrl+o`/`Esc`/`q`.

**Hand conversation back to terminal**: in transcript mode press `[` (writes full convo with all tool output expanded into native scrollback — usable by `Cmd+f`/tmux/etc, lasts until exit), or `v` (writes to temp file, opens in `$VISUAL`/`$EDITOR`).

**Clear**: `Ctrl+L` twice within 2s = `/clear`. macOS: double `Cmd+K` also.

**tmux**: works with caveats. Need `set -g mouse on` in `~/.tmux.conf` for wheel. **Incompatible with `tmux -CC`** (iTerm2 integration mode) — alt screen + mouse tracking break, mouse wheel does nothing, double-click can corrupt terminal state. Regular tmux inside iTerm2 (no `-CC`) works fine.

**Native selection workaround**: hold terminal's bypass modifier (Option in iTerm2, Shift in most Linux/Windows terminals) for one-off native selection. For permanent: `CLAUDE_CODE_DISABLE_MOUSE=1` keeps flicker-free + flat memory but loses click-to-position, click-to-expand, URL clicks, wheel scrolling. Selection clipboard path varies (tmux paste buffer / OSC 52 over SSH; iTerm2 needs Settings → General → Selection → Applications may access clipboard, or run `/terminal-setup`). Toast after each copy reports which path was used.
