---
type: entity
name: Status-line
aliases: [statusline, status line]
category: feature
status: ga
created: 2026-05-05
---

## 一句话定义

Claude Code 终端底部的可定制状态栏

## 关键属性

- 终端底部可定制的状态栏，本质是跑**任意 shell 脚本**：从 stdin 拿一份 JSON session 数据，把 stdout 显示出来；本地执行不消耗 API tokens [[statusline]]
- 配置：`/statusline <自然语言>` 让 Claude 自动写脚本 + 写入 settings；或手动 `statusLine: { type: "command", command: "...", padding: 2, refreshInterval: 5, hideVimModeIndicator: false }` [[statusline]]
- Update triggers：每次新 assistant message 后、permission mode 切换、vim mode 切换；**debounce 300ms** 批量；in-flight 脚本被新触发取消；脚本文件改动只在下一次触发后生效 [[statusline]]
- `refreshInterval`（min 1）每 N 秒重跑用于时间相关内容——event triggers 在 idle（如等 subagent）会安静下来，需要它顶上 [[statusline]]
- 输出：多行用多次 `echo`；ANSI 颜色代码（`\033[32m` 等）支持的终端可用；OSC 8 hyperlink 让文本 Cmd/Ctrl+click 可点（需 iTerm2 / Kitty / WezTerm）；推荐 `printf '%b'` 跨 shell 处理 escape [[statusline]]
- stdin JSON 关键字段：`model.{id, display_name}`、`cwd`、`workspace.{current_dir, project_dir, added_dirs, git_worktree}`、`cost.{total_cost_usd, total_duration_ms, total_lines_added/removed}`、`context_window.{used_percentage, remaining_percentage, current_usage}`、`exceeds_200k_tokens`、`effort.level`、`thinking.enabled`、`rate_limits.{five_hour, seven_day}`、`session_id`、`output_style.name`、`vim.mode`、`agent.name` [[statusline]]
- **`used_percentage` 仅算 input + cache，不含 output tokens**；`exceeds_200k_tokens` 是固定 200k 阈值，与实际 context window 大小无关 [[statusline]]
- Subagent status line 通过 `subagentStatusLine` 配置——格式相同，stdin 多了 `columns` + `tasks[]`（每条含 `id, name, type, status, description, label, startTime, tokenCount, tokenSamples, cwd`）；输出每行一个 JSON `{"id":"...", "content":"..."}` 覆盖默认；空 content 隐藏，省略 id 保留默认 [[statusline]]
- 缓存慢操作（如大 repo `git status`）：用 `/tmp/statusline-git-cache-${session_id}` 作 cache file，5 秒刷新；**禁止用 `$$` / `os.getpid()` / `process.pid`**——每次调用变化导致 cache 失效 [[statusline]]
- Windows 下 status line 走 Git Bash（如装了），否则 PowerShell；`.ps1` 用 `powershell -NoProfile -File ...` 调；装了 Git Bash 后 `.sh` 可直接跑 [[statusline]]
- Trust gate：status line 与 hooks 同样要求 workspace trust；未接受 → "statusline skipped · restart to fix"；`disableAllHooks: true` 也会同时禁 status line [[statusline]]
- Mock 测试：`echo '{"model":{...},"workspace":{...}}' | ./statusline.sh` [[statusline]]
- `worktree.{name, path, branch, original_cwd, original_branch}` 仅在 `--worktree` session 出现，可用于显示当前 worktree 上下文 [[statusline]]

## 出现来源

_7 summaries reference this entity_:

- [[2026-w15]]
- [[changelog]]
- [[claude-directory]]
- [[commands]]
- [[settings]]
- [[statusline]]
- [[terminal-config]]

## 相关

- [[Settings]] — `statusLine` / `subagentStatusLine` 字段在 settings.json 配置
- [[Hooks]] — status line 与 hooks 共用 trust gate 与 `disableAllHooks` 总开关
- [[Subagent]] — 通过 `subagentStatusLine` 自定义每个 subagent 在 tasks pane 的显示行
- [[Plugin]] — plugins 可以打包 status line 脚本随安装分发
- [[Context-window]] — stdin 直接暴露 `context_window.used_percentage` 等字段，是状态栏最常显示的数据
