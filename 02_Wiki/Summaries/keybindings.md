---
type: summary
source: 01_Raw/code.claude.com/docs/en/keybindings.md
source_url: https://code.claude.com/docs/en/keybindings
title: "Customize keyboard shortcuts"
summarized_at: 2026-05-05
entities_referenced: [Permission-mode, Fast-mode, Plugin]
concepts_referenced: [Extended-thinking]
---

Customizable keyboard shortcuts. Requires Claude Code v2.1.18+. Run `/keybindings` to create/open `~/.claude/keybindings.json`. **Changes auto-applied without restart**.

**File schema**: `bindings` array; each block has `context` + `bindings` map of keystroke → action (or `null` to unbind). Optional `$schema` and `$docs`.

```json
{
  "$schema": "https://www.schemastore.org/claude-code-keybindings.json",
  "bindings": [{
    "context": "Chat",
    "bindings": {
      "ctrl+e": "chat:externalEditor",
      "ctrl+u": null
    }
  }]
}
```

**Contexts** (where bindings apply): `Global`, `Chat`, `Autocomplete`, `Settings`, `Confirmation`, `Tabs`, `Help`, `Transcript`, `HistorySearch`, `Task`, `ThemePicker`, `Attachments`, `Footer`, `MessageSelector`, `DiffDialog`, `ModelPicker`, `Select`, `Plugin`, `Scroll` (fullscreen mode), `Doctor`.

**Action namespaces**: `app:*`, `history:*`, `chat:*`, `autocomplete:*`, `confirm:*`, `permission:*`, `transcript:*`, `historySearch:*`, `task:*`, `theme:*`, `help:*`, `tabs:*`, `attachments:*`, `footer:*`, `messageSelector:*`, `diff:*`, `modelPicker:*`, `select:*`, `plugin:*`, `settings:*`, `doctor:*`, `voice:*`, `scroll:*`, `selection:*`.

**Notable defaults**:
- `Global`: `app:interrupt`=Ctrl+C, `app:exit`=Ctrl+D, `app:toggleTodos`=Ctrl+T, `app:toggleTranscript`=Ctrl+O
- `Chat`: `chat:cancel`=Esc, `chat:cycleMode`=Shift+Tab (Win pre-VT-mode: Meta+M), `chat:modelPicker`=Meta+P, `chat:fastMode`=Meta+O, `chat:thinkingToggle`=Meta+T, `chat:submit`=Enter, `chat:newline`=Ctrl+J, `chat:externalEditor`=Ctrl+G or Ctrl+X Ctrl+E (chord), `chat:stash`=Ctrl+S, `chat:imagePaste`=Ctrl+V (Alt+V on Windows), `chat:clearInput`=Ctrl+L (twice within 2s in fullscreen → `/clear`), `chat:clearScreen`=Cmd+K
- `History`: `history:search`=Ctrl+R, `history:previous/next`=Up/Down
- `HistorySearch`: `historySearch:cycleScope`=Ctrl+S (session/project/everywhere)
- `Task`: `task:background`=Ctrl+B
- `Doctor`: `doctor:fix`=F (sends diagnostics to Claude)
- Voice (when enabled): `voice:pushToTalk`=Space (hold or tap depending on `/voice` mode)

**Keystroke syntax**:
- Modifiers: `ctrl`/`control`, `shift`, `alt`/`opt`/`option`/`meta` (Alt on Win/Linux, Option on macOS), `cmd`/`command`/`super`/`win` (only sent by Kitty-protocol or `modifyOtherKeys` terminals — use `ctrl`/`meta` for portability)
- Standalone uppercase letter implies Shift (e.g., `K` = `shift+k`); with modifiers stylistic only (`ctrl+K` ≡ `ctrl+k`)
- **Chords**: space-separated (e.g., `ctrl+x ctrl+s` = press Ctrl+X release then Ctrl+S)
- Special: `escape`/`esc`, `enter`/`return`, `tab`, `space`, arrows, `backspace`, `delete`

**Unbinding chords**: set every chord with same prefix to `null` to free the prefix for single-key use. Partial unbinding still enters chord-wait mode.

**Reserved (cannot rebind)**: Ctrl+C (interrupt), Ctrl+D (exit), Ctrl+M (= Enter in terminals), Caps Lock (not delivered).

**Terminal multiplexer conflicts** (warned): Ctrl+B (tmux prefix — press twice to send), Ctrl+A (GNU screen prefix), Ctrl+Z (Unix SIGTSTP).

**Vim mode interaction** (when enabled in `/config` → Editor mode): vim handles input-level (cursor/modes/motions); keybindings handle component-level (toggle todos, submit). Esc switches INSERT→NORMAL, does NOT trigger `chat:cancel`. Most Ctrl-key shortcuts pass through. In NORMAL mode `?` shows help (vim behavior).

**Validation**: `/doctor` shows warnings for parse errors, invalid contexts, reserved conflicts, multiplexer conflicts, duplicates.

**Scroll context** (only active in fullscreen rendering): `scroll:lineUp/Down` (mouse wheel triggers), `scroll:pageUp/Down`=PageUp/Down, `scroll:top`=Ctrl+Home, `scroll:bottom`=Ctrl+End, plus `scroll:halfPageUp/Down` and `scroll:fullPageUp/Down` (vi-style, unbound by default), and `selection:*` actions for keyboard selection extension.
