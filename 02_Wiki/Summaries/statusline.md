---
type: summary
source: 01_Raw/code.claude.com/docs/en/statusline.md
source_url: https://code.claude.com/docs/en/statusline
title: "Customize your status line"
summarized_at: 2026-05-05
entities_referenced: [Status-line, Settings, Hooks, Subagent, Plugin]
concepts_referenced: []
---

Status line is a customizable bottom bar that runs **any shell script** you configure. Receives JSON session data on stdin, displays whatever your script prints. Runs locally — no API tokens consumed.

**Configure** via `/statusline <natural language>` (Claude generates the script + updates settings) OR manually in any settings file:
```json
{
  "statusLine": {
    "type": "command",
    "command": "~/.claude/statusline.sh",
    "padding": 2,
    "refreshInterval": 5,
    "hideVimModeIndicator": false
  }
}
```
Inline command also works (`"command": "jq -r '...'"` style). `padding` adds horizontal spacing chars. `refreshInterval` re-runs every N sec for time-based content (min 1) — needed because event triggers go quiet during idle (e.g., waiting on subagents). `hideVimModeIndicator` suppresses built-in `-- INSERT --` if your script renders `vim.mode` itself.

**Update triggers**: after each new assistant message, on permission mode change, on vim mode toggle. **Debounced 300ms** — rapid changes batch. In-flight script cancelled if a new trigger arrives. Edits to script don't apply until next trigger.

**Output**: multi-line via multiple `echo` statements. ANSI color codes (`\033[32m` etc) work in supporting terminals. **OSC 8 hyperlinks** make text clickable (Cmd/Ctrl+click) — requires iTerm2/Kitty/WezTerm. Use `printf '%b'` for reliable escape interpretation across shells.

**JSON fields delivered on stdin** (selected — full list in raw):
- `model.id`, `model.display_name`
- `cwd`, `workspace.{current_dir, project_dir, added_dirs, git_worktree}`
- `cost.{total_cost_usd, total_duration_ms, total_api_duration_ms, total_lines_added, total_lines_removed}`
- `context_window.{total_input_tokens, total_output_tokens, context_window_size, used_percentage, remaining_percentage, current_usage}` — `current_usage.{input_tokens, output_tokens, cache_creation_input_tokens, cache_read_input_tokens}`. **`used_percentage` excludes output tokens** (input + cache only).
- `exceeds_200k_tokens` — fixed 200k threshold regardless of actual context size
- `effort.level`, `thinking.enabled`
- `rate_limits.{five_hour, seven_day}.{used_percentage, resets_at}` — Claude.ai subscribers only, after first API response
- `session_id` (use for cache file naming — stable per session, unique across), `session_name`, `transcript_path`, `version`
- `output_style.name`, `vim.mode`, `agent.name`
- `worktree.{name, path, branch, original_cwd, original_branch}` — present only during `--worktree` sessions

**Common patterns**: progress bars (`▓░` or `█░`), git branch + staged/modified counts, cost + duration, color thresholds (green/yellow/red at 70%/90%), clickable GitHub repo links via OSC 8.

**Cache slow ops** (e.g. `git status` in large repos): cache file in `/tmp/statusline-git-cache-${session_id}`, refresh every 5 sec. Don't use `$$` / `os.getpid()` / `process.pid` (changes per invocation, defeats cache).

**Windows**: status line runs through Git Bash if installed, else PowerShell. Run a `.ps1` via `powershell -NoProfile -File ...`. With Git Bash present, `.sh` works directly.

**Subagent status lines** via `subagentStatusLine` setting — same format. Receives all visible subagent rows in one JSON object: base hook fields + `columns` + `tasks` array (each task: `id, name, type, status, description, label, startTime, tokenCount, tokenSamples, cwd`). Output one JSON line per row to override: `{"id": "<task id>", "content": "<row body>"}`. Empty `content` hides; omit `id` to keep default.

**Trust gate**: status line requires workspace trust acceptance (same as hooks). Not accepted → notification "statusline skipped · restart to fix". `disableAllHooks: true` also disables status line.

**Mock test**: `echo '{"model":{...},"workspace":{...}}' | ./statusline.sh`.
