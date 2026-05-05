---
type: summary
source: 01_Raw/code.claude.com/docs/en/interactive-mode.md
source_url: https://code.claude.com/docs/en/interactive-mode
title: "Interactive mode (keyboard shortcuts + UX)"
summarized_at: 2026-05-05
entities_referenced: [Native-interface, Slash-command, Skill, Plugin, MCP-server, Subagent, Permission-mode, Fast-mode, Checkpointing]
concepts_referenced: [Extended-thinking]
---

Reference for keyboard shortcuts, input modes, and interactive features in Claude Code sessions. Press `?` for environment-specific shortcut help. macOS Option-key shortcuts require terminal config (iTerm2/Terminal.app/VS Code) to map Option as Meta.

**General controls** (selected):
- `Ctrl+C` cancel, `Ctrl+D` exit, `Ctrl+L` redraw, `Ctrl+O` toggle transcript viewer, `Ctrl+R` reverse search history, `Ctrl+B` background tasks (tmux: twice), `Ctrl+T` toggle task list.
- `Esc Esc` rewind/summarize.
- `Shift+Tab` (or `Alt+M`) cycle permission modes.
- `Option+P` switch model, `Option+T` toggle extended thinking, `Option+O` toggle fast mode.
- `Ctrl+X Ctrl+K` (twice in 3s) kill all background agents.
- `Ctrl+G` / `Ctrl+X Ctrl+E` open in `$EDITOR`. Toggle "Show last response in external editor" in `/config` to prepend Claude's previous reply as `#`-comment context.
- `Ctrl+V` paste image as `[Image #N]` chip.

**Text editing**: standard readline (`Ctrl+A`/`E`/`K`/`U`/`W`/`Y`, `Alt+B`/`F` word nav, `Alt+Y` cycle paste history).

**Multiline**: `\` + Enter (universal), `Option+Enter` (macOS w/ Meta), `Shift+Enter` (iTerm2/WezTerm/Ghostty/Kitty/Warp/Apple Terminal native; others run `/terminal-setup`), `Ctrl+J` (universal control sequence).

**Quick prefixes**: `/` command/skill, `!` shell mode, `@` file path autocomplete.

**Vim editor mode**: enable via `/config` → Editor mode. Full vim grammar: NORMAL/INSERT/VISUAL modes, motions (`hjkl`, `wbe`, `0$^`, `ggG`, `f/F/t/T`, `;,`), edits (`x`, `dd`, `D`, `dw/de/db`, `cc/C`, `yy/Y`, `p/P`, `>>/<<`, `J`, `u`, `.`), text objects (`iw/aw`, `i"/a"`, `i(/a(`, etc.). Block-wise `Ctrl+V` NOT supported. At top/bottom edge, `j/k`/arrows navigate command history.

**Reverse search (`Ctrl+R`)**: search session history, `Ctrl+R` again for older matches, `Ctrl+S` cycle scope (session/project/all-projects), Tab/Esc accept-and-edit, Enter accept-and-execute.

**Background bash**: long commands run async, output to file Claude can Read, unique IDs, auto-cleaned on exit, terminated if output > 5GB. Disable with `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1`.

**Shell mode `!`**: prefix runs shell directly, command + output added to context, supports `Ctrl+B` background, autocomplete from previous `!` commands. Pasting text starting with `!` into empty prompt auto-enters shell mode. Exit with Esc/Backspace/`Ctrl+U`.

**Prompt suggestions**: grayed-out example from project git history; after responses, follow-up suggestions reuse parent prompt cache (low cost). Tab/Right to accept, Enter to accept+submit. Skipped after first turn, in non-interactive, in plan mode. Disable: `CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION=false`.

**`/btw` side questions**: ephemeral overlay, sees full conversation but NO tool access, single response, never enters history. Available even while Claude is processing. Inverse of subagent (full context, no tools — vs subagent: empty context, all tools).

**Task list**: created for complex multi-step work. `Ctrl+T` toggle (shows up to 5). Ask "show me all tasks" / "clear all tasks" for full mgmt. Persists across compactions. Share across sessions: `CLAUDE_CODE_TASK_LIST_ID=my-project claude` (uses named dir in `~/.claude/tasks/`).

**Session recap**: one-line summary auto-generated when terminal unfocused for 3+ min and session has 3+ turns. `/recap` on demand. Disable via `/config`. Skipped in non-interactive.

**PR review status**: footer shows clickable "PR #446" link with colored underline (green=approved, yellow=pending, red=changes requested, gray=draft, purple=merged). Cmd/Ctrl-click to open. Updates every 60s. Requires `gh` CLI authenticated.
