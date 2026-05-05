---
type: entity
name: Hooks
aliases: [hook, hook system, session hooks]
category: feature
status: ga
created: 2026-05-05
---

## 一句话定义

Claude Code 在 session 生命周期各点执行的 user-defined shell command / HTTP endpoint / LLM prompt

## 关键属性

- 提供 **deterministic** 控制点（vs. 模型自主调用 tool），让 user-defined shell command / HTTP endpoint / MCP tool / LLM prompt / subagent 在 session 生命周期固定时刻自动执行 [[hooks]] [[hooks-guide]]
- 五种 handler `type`：`command`（shell，最常用，stdin/stdout/exit-code 协议）、`http`（POST event JSON）、`mcp_tool`（连接的 MCP 服务器工具）、`prompt`（单轮 LLM，默认 Haiku）、`agent`（多轮 subagent，60s 默认 timeout，**实验中**） [[hooks-guide]]
- 生命周期事件分组：session 级 `SessionStart` / `SessionEnd` / `Setup`；turn 级 `UserPromptSubmit` / `UserPromptExpansion` / `Stop` / `StopFailure`；tool 级 `PreToolUse` / `PermissionRequest` / `PermissionDenied` / `PostToolUse` / `PostToolUseFailure` / `PostToolBatch`；subagent 级 `SubagentStart` / `SubagentStop` / `TaskCreated` / `TaskCompleted`；其他 `Notification` / `TeammateIdle` / `InstructionsLoaded` / `ConfigChange` / `CwdChanged` / `FileChanged` / `WorktreeCreate` / `WorktreeRemove` / `PreCompact` / `PostCompact` / `Elicitation` / `ElicitationResult` [[hooks]] [[hooks-guide]]
- 配置嵌套三层：hook event → matcher group → hook handler；matcher 是字符串 / `|` 列表 / regex（事件不同 filter 字段不同，tool 事件 filter tool name，`SessionStart` filter start type） [[hooks]]
- `if` 字段（v2.1.85+）用 permission-rule 语法（`Bash(git *)`、`Edit(*.ts)`）做 handler 启动前细粒度过滤，避免 spawn process 开销；只在 tool 事件可用 [[hooks-guide]]
- 加载位置（scope）：`~/.claude/settings.json`（user）、`.claude/settings.json`（project committed）、`.claude/settings.local.json`（project gitignored）、managed policy（org）、plugin `hooks/hooks.json`、Skill / Subagent frontmatter（while active） [[hooks]] [[hooks-guide]]
- 通信协议：stdin 收 JSON（含 `session_id`、`cwd`、`hook_event_name`、event 专属字段如 `tool_name` / `tool_input`）；exit `0` 通过、`2` 阻塞（stderr → Claude）、其他 → 通过但记 error；或 stdout 写结构化 JSON（`permissionDecision: allow|deny|ask|defer`） [[hooks-guide]]
- **Hooks 只能 tighten 不能 loosen**：`PreToolUse` deny 即使在 `bypassPermissions` / `--dangerously-skip-permissions` 也生效；`allow` 不会绕过 settings/managed deny rule [[hooks-guide]]
- 多 hook 命中合并规则：最严胜出，**任意 deny 覆盖所有 allow**；`additionalContext` 全部拼接 [[hooks-guide]]
- 默认 hook timeout 10 分钟；`PostToolUse` 不能撤销（已执行）；`PermissionRequest` 在 headless `-p` 模式不触发，需用 `PreToolUse`；`updatedInput` 多次重写时最后完成的胜出（并行执行） [[hooks-guide]]
- 企业 lockdown：`allowManagedHooksOnly` 阻止 user/project/plugin 提供的 hooks，但 managed `enabledPlugins` 强制启用的 plugin 豁免（vetted-distribution 路径） [[hooks]]
- Agent SDK in-process callback hooks 与 filesystem shell hooks 并存：通过 `settingSources` 加载 shell hooks；TS SDK 比 Python SDK 多支持 `SessionStart` / `SessionEnd` / `Setup` / `PostToolBatch` 等事件 [[hooks--agent-sdk]]
- 常见 bug：`~/.zshrc` 里 `echo` 污染 stdin JSON（用 `[[ $- == *i* ]]` 守卫）；`Stop` hook 无限循环（要检查 `stop_hook_active` 早退）；matcher case-sensitive；`/hooks` UI 看是否生效 [[hooks-guide]]
- Plugin 范型：`hooks.json` 配 `${CLAUDE_PLUGIN_ROOT}` 路径前缀，在 plugin 安装 cache 路径下保持可移植性；`security-guidance` 例 `PreToolUse` matcher `Edit|Write|MultiEdit` → `python3 ${CLAUDE_PLUGIN_ROOT}/hooks/security_reminder_hook.py` [[security-guidance--hooks]]
- 高级模式：多阶段验证（`command` 5s 快速 + `prompt` 15s 智能分析在同 matcher group）；条件执行（`if [ -z "$CI" ]` 仅 CI 跑）；hook chain 通过 PID 后缀 temp 文件共享 state [[advanced--hook-development]]

## 出现来源

_102 summaries reference this entity_:

- [[2026-w13]]
- [[2026-w14]]
- [[2026-w15]]
- [[2026-w16]]
- [[2026-w17]]
- [[README--examples-settings]]
- [[README--explanatory-output-style]]
- [[README--hookify]]
- [[README--plugin-dev]]
- [[README--plugin-structure]]
- [[SKILL--command-development]]
- [[admin-setup]]
- [[advanced--hook-development]]
- [[advanced-plugin]]
- [[agent-loop]]
- [[agent-teams]]
- [[auto-mode-config]]
- [[best-practices]]
- [[champion-kit]]
- [[changelog]]
- [[changelog--claude-code-repo]]
- [[claude-code-features]]
- [[claude-code-on-the-web]]
- [[claude-directory]]
- [[cli-reference]]
- [[command-development--readme]]
- [[commands]]
- [[communications-kit]]
- [[component-patterns--plugin-dev]]
- [[configure--hookify]]
- [[console-log-warning]]
- [[context-window]]
- [[conversation-analyzer--hookify]]
- [[costs]]
- [[create-plugin]]
- [[dangerous-rm--hookify-example]]
- [[debug-your-config]]
- [[desktop]]
- [[discover-plugins]]
- [[env-vars]]
- [[example-settings--plugin-dev]]
- [[features-overview]]
- [[glossary]]
- [[help--hookify]]
- [[help--ralph-wiggum]]
- [[hook-development--SKILL]]
- [[hook-development-scripts--readme]]
- [[hook-patterns--plugin-dev]]
- [[hookify]]
- [[hookify--plugin-manifest]]
- [[hooks]]
- [[hooks--agent-sdk]]
- [[hooks--explanatory-output-style]]
- [[hooks--hookify]]
- [[hooks--ralph-wiggum]]
- [[hooks-guide]]
- [[how-claude-code-works]]
- [[learning-output-style--hooks]]
- [[learning-output-style--readme]]
- [[list--hookify]]
- [[manifest-reference--plugin-structure]]
- [[memory]]
- [[migration--hook-development]]
- [[monitoring-usage]]
- [[observability]]
- [[overview--agent-sdk]]
- [[overview--claude-code]]
- [[parsing-techniques--plugin-settings]]
- [[permission-modes]]
- [[permissions]]
- [[permissions--claude-code]]
- [[plugin-features-reference]]
- [[plugin-settings--skill]]
- [[plugin-structure-skill--plugin-dev]]
- [[plugin-validator]]
- [[plugins]]
- [[plugins--agent-sdk]]
- [[plugins-readme--claude-code-repo]]
- [[plugins-reference]]
- [[python]]
- [[ralph-loop]]
- [[ralph-wiggum-readme]]
- [[real-world-examples]]
- [[require-tests-stop.local]]
- [[security]]
- [[security-guidance--hooks]]
- [[security-guidance-plugin-json]]
- [[sensitive-files-warning--hookify]]
- [[server-managed-settings]]
- [[settings]]
- [[settings-strict]]
- [[skills]]
- [[standard-plugin]]
- [[statusline]]
- [[streaming-vs-single-mode]]
- [[sub-agents]]
- [[terminal-config]]
- [[testing-strategies--plugin-dev]]
- [[tools-reference]]
- [[typescript--agent-sdk]]
- [[user-input]]
- [[writing-rules--SKILL]]

## 相关

- [[Settings]] — hooks 在 settings.json 各 scope 配置，`disableAllHooks` / `allowManagedHooksOnly` 在 settings 控制
- [[Permission-mode]] — hooks 与 permission mode 协同，`PreToolUse` deny 即使 bypass mode 也生效；`PermissionRequest` / `PermissionDenied` 是专属 hook 事件
- [[Plugin]] — plugin 通过 `hooks/hooks.json` 打包发布 hook，使用 `${CLAUDE_PLUGIN_ROOT}` 引用脚本
- [[MCP-server]] — `mcp_tool` 类型 hook 调用 MCP 工具；`Elicitation` / `ElicitationResult` 事件来自 MCP server 请求 user 输入
- [[Subagent]] — `agent` 类型 hook 用 subagent 实现需要 codebase 检查的验证；`SubagentStart` / `SubagentStop` 是专属事件
- [[Agent-SDK]] — Agent SDK 提供 in-process callback hooks，与 filesystem shell hooks 互补
- [[Auto-mode]] — `PermissionDenied` hook 可对 auto-mode classifier 阻断做程序化反应（返回 `{retry: true}`）
