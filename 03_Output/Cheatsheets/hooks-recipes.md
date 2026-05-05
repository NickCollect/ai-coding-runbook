---
type: cheatsheet
topic: hooks-recipes
last_updated: 2026-05-05
based_on:
  - 02_Wiki/Entities/Hooks.md
  - 02_Wiki/Summaries/hooks.md
  - 02_Wiki/Summaries/hooks-guide.md
  - 02_Wiki/Summaries/security-guidance--hooks.md
  - 02_Wiki/Summaries/advanced--hook-development.md
---

# Hooks Recipes & Lifecycle Quick Reference

> Hooks 是 Claude Code 唯一的 **deterministic 控制点** —— 在 session lifecycle 固定时刻自动跑 user-defined 命令。
> 
> 全文档详细 [[Hooks]]。本 cheatsheet 是常用 pattern + lifecycle 速查。

---

## Lifecycle Events 速查表

按触发频率分组（详见 [[Hooks]]）：

| 频率 | 事件 | 何时触发 |
|---|---|---|
| **每 session** | `SessionStart` | 进 session 时（对话首条 message 之前） |
| | `SessionEnd` | 退 session |
| | `Setup` | session 启动配置阶段 |
| **每轮** | `UserPromptSubmit` | 用户按 enter 后、Claude 看到 prompt 前 |
| | `UserPromptExpansion` | slash command 展开后 |
| | `Stop` / `StopFailure` | Claude 准备结束本轮 / 异常结束 |
| **每 tool 调用** | `PreToolUse` | tool 实际跑之前（可 deny）|
| | `PermissionRequest` | 弹权限框前 |
| | `PermissionDenied` | auto-mode 拒绝时 |
| | `PostToolUse` | tool 跑完（无法撤销） |
| | `PostToolUseFailure` | tool 失败 |
| | `PostToolBatch` | 批量 tool 调用结束 |
| **subagent** | `SubagentStart` / `SubagentStop` | subagent 开始 / 结束 |
| | `TaskCreated` / `TaskCompleted` | Agent tool 调用包装 |
| **其他** | `Notification` / `TeammateIdle` / `InstructionsLoaded` / `ConfigChange` / `CwdChanged` / `FileChanged` / `WorktreeCreate` / `WorktreeRemove` / `PreCompact` / `PostCompact` / `Elicitation` / `ElicitationResult` | 见名知意 |

---

## Handler 5 种类型

| `type` | 用途 | 协议 |
|---|---|---|
| `command` | shell 命令（最常用） | stdin 收 event JSON，stdout 写 JSON 决策，exit 0/2/其他 |
| `http` | POST 到 URL | request body = event JSON，response = JSON 决策 |
| `mcp_tool` | 调用已连接的 MCP tool | event 自动转 tool input |
| `prompt` | 单轮 LLM（默认 Haiku） | 适合"智能"判断（如 PR 文案审查） |
| `agent` | 多轮 subagent（**实验中**，60s timeout） | 长链路任务 |

---

## Recipe 1 · 阻止 commit 前没跑测试

```json
// .claude/settings.json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "if": "Bash(git commit *)",
        "hooks": [
          { "type": "command", "command": "npm test" }
        ]
      }
    ]
  }
}
```

`if` 是 v2.1.85+，permission-rule 语法。test 失败 → exit 非 0 → hook 阻塞 commit。

---

## Recipe 2 · 自动 format 写入的文件

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write|MultiEdit",
        "hooks": [
          { "type": "command", "command": "prettier --write \"$CLAUDE_TOOL_INPUT_PATH\"" }
        ]
      }
    ]
  }
}
```

`PostToolUse` 不能撤销，但可以"事后"补救（如 format / lint）。

---

## Recipe 3 · 读 Edit 操作前注入安全提醒

参考 `security-guidance` plugin（[[security-guidance--hooks]]）：

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write|MultiEdit",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PLUGIN_ROOT}/hooks/security_reminder_hook.py"
          }
        ]
      }
    ]
  }
}
```

`${CLAUDE_PLUGIN_ROOT}` plugin 安装路径前缀，跨 update 持久。Python 脚本 stdout 写 `{"additionalContext": "...安全提醒..."}` → Claude 看到后再决定要不要继续。

---

## Recipe 4 · session 开始时拉最新文档

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "cd $CLAUDE_PROJECT_DIR && git pull --rebase"
          }
        ]
      }
    ]
  }
}
```

注意：`SessionStart` matcher 是 start type（不是 tool name）；`*` 匹配所有进入方式。

---

## Recipe 5 · 多阶段验证（快速 + 智能）

参考 `advanced--hook-development`（[[advanced--hook-development]]）。同 matcher group 配两个 hook：

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          { "type": "command", "command": "scripts/quick-syntax-check.sh", "timeout": 5 },
          { "type": "prompt", "model": "haiku", "prompt": "审查这条 Bash 命令是否合理：${tool_input}", "timeout": 15 }
        ]
      }
    ]
  }
}
```

第一个 5s 内做语法 / shellcheck；第二个用 LLM 做语义 review。多 hook 命中时**任意 deny 覆盖所有 allow**。

---

## Recipe 6 · CI vs 本地差别行为

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          { "type": "command", "command": "[ -z \"$CI\" ] && bash scripts/local-only-check.sh || exit 0" }
        ]
      }
    ]
  }
}
```

仅本地跑额外检查；CI 跳过。

---

## 决策协议

stdout 写 JSON 决策（最 expressive 的方式）：

```json
{
  "permissionDecision": "deny",
  "reason": "本仓不允许直接 push origin main，请走 PR",
  "additionalContext": "可选的额外信息塞进 Claude context"
}
```

`permissionDecision` 取值：
- `"allow"` —— 通过（**注意：不能绕过 settings/managed deny rule**）
- `"deny"` —— 阻塞，stderr 内容传给 Claude
- `"ask"` —— 弹权限框（默认行为）
- `"defer"` —— 让下一个 hook 决定

或者只用 exit code（简单场景）：
- `0` —— 通过
- `2` —— deny + stderr → Claude
- 其他 —— 通过但记 error

---

## 配置 scope 与优先级

加载顺序（高优先后覆盖低优先）：
1. managed policy（org，企业 lockdown）
2. `~/.claude/settings.json`（user）
3. `.claude/settings.json`（project，commit 进 repo）
4. `.claude/settings.local.json`（project，gitignored）
5. plugin 的 `hooks/hooks.json`
6. Skill / Subagent frontmatter（while active）

企业 lockdown：`allowManagedHooksOnly: true` 阻止 user/project/plugin hooks，但 managed `enabledPlugins` 强制启用的 plugin 豁免（vetted-distribution 路径）。

---

## 易踩的坑

- **`~/.zshrc` 里 `echo` 污染 stdin JSON** —— `command` hook 会被 shell 加载 rc 文件污染。守卫：`[[ $- == *i* ]] && return` 在 rc 顶部
- **`Stop` hook 无限循环** —— `Stop` hook 自己也会触发 `Stop`，必须检查 `stop_hook_active` JSON 字段早退
- **matcher case-sensitive** —— `bash` 不等于 `Bash`
- **headless `-p` 模式不触发 `PermissionRequest`** —— 用 `PreToolUse` 替代
- **`updatedInput` 多次重写时最后完成的胜出**（并行执行）—— 依赖顺序的逻辑要避开
- **`PostToolUse` 不能撤销已执行的 tool** —— 想 deny 用 `PreToolUse`

---

## 调试

- `/hooks` slash command 看哪些 hook 加载了、是否生效
- 在 hook handler 里 `env > /tmp/hook-env.log` 看完整 env / stdin
- exit code 大于 0 但不是 2 → silently 通过但 log error，要看 `~/.claude/logs/`

---

## 详细引用

- [[Hooks]] —— 完整 entity
- [[Settings]] —— 配置存放位置
- [[Plugin]] —— 通过 plugin 分发 hook 的 pattern
- [[Subagent]] —— `SubagentStart` / `SubagentStop` 事件相关
- [[Agent-SDK]] —— SDK 内 in-process callback hooks
