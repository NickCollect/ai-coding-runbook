---
type: entity
name: Subagent
aliases: [sub-agent, sub agent, subagents]
category: feature
status: ga
created: 2026-05-05
---

## 一句话定义

Claude Code 内嵌的专用 agent，主 agent 可委派任务给 subagent 在隔离上下文里跑

## 关键属性

- 在隔离 context window 中运行的专用 AI assistant，主 agent 委派任务后只把"最终消息"原样回传，避免 tool calls / 文件内容污染主上下文 [[sub-agents]] [[subagents--agent-sdk]]
- 内置三种：`Explore`（Haiku，只读，做 codebase 搜索）、`Plan`（继承 model，只读，plan mode 用，防嵌套）、`general-purpose`（继承 model，全工具，复杂多步任务）；helper subagent 还包括 `statusline-setup` 和 `Claude Code Guide` [[sub-agents]]
- 创建走 `/agents` 命令或手写 `.md` + YAML frontmatter；scope 优先级（高→低）= managed settings → `--agents` CLI flag → `.claude/agents/` 项目级 → `~/.claude/agents/` 用户级 → plugin 的 `agents/` [[sub-agents]]
- Frontmatter 字段含 `name`（lowercase-hyphen，必填）、`description`（必填，决定何时委派）、`tools` allowlist、`disallowedTools` denylist（先应用）、`model`（sonnet/opus/haiku/全 ID/`inherit`，默认 `inherit`）、`permissionMode`、`maxTurns`、`skills`、`mcpServers`、`hooks`、`memory`、`background`、`effort`、`isolation`（`worktree` 走 git worktree）、`color`、`initialPrompt` [[sub-agents]]
- Plugin 来源的 subagent 中 `hooks` / `mcpServers` / `permissionMode` 字段被忽略（安全考虑） [[sub-agents]]
- Model resolution 顺序：`CLAUDE_CODE_SUBAGENT_MODEL` env > 调用时 `model` 参数 > frontmatter `model` > 主对话模型 [[sub-agents]]
- 调用方式：自然语言（Claude 自决）、`@"agent-name (agent)"` 强制指定、或 `claude --agent <name>` / `agent` 设置 session 级替换 system prompt [[sub-agents]]
- 父 agent 处于 `bypassPermissions` / `acceptEdits` / `auto` 模式时，subagent 强制继承且**无法 override**——结合 subagent 受约束更少的 system prompt，inheriting bypass 等于把完整自主系统访问权交给它 [[permissions]] [[sub-agents]]
- Subagent 不能再 spawn subagent——别把 `Agent` 工具放进 subagent 的 `tools`；`Agent` 必须出现在主 `allowedTools` 才能委派 [[subagents--agent-sdk]]
- Foreground vs background：foreground 阻塞主 session，permission prompts 透传；background 并发跑，启动前预批所有需要的权限、其余自动拒绝；`Ctrl+B` 切到 background；`CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1` 关闭 [[sub-agents]]
- Transcript 持久化在 `~/.claude/projects/{project}/{sessionId}/subagents/agent-{agentId}.jsonl`；保留期 `cleanupPeriodDays` 默认 30 天 [[sub-agents]]
- 主 → subagent 的唯一通道是 Agent tool 的 prompt 字符串，subagent 不继承父对话历史 / system prompt / 未列出的 skills——必须显式在 prompt 里包含文件路径 / 错误 / 决策 [[subagents--agent-sdk]]
- v2.1.63 起 `Task` 工具改名 `Agent`（SDK `system:init` 的 tools list 和 `result.permission_denials[].tool_name` 仍发 "Task"，检测时两者都查） [[sub-agents]] [[subagents--agent-sdk]]
- Forked subagent（v2.1.117+ 实验，`CLAUDE_CODE_FORK_SUBAGENT=1`）：fork 继承父全部对话、共享 prompt cache，比 fresh subagent 便宜，但 fork 不能再 spawn fork [[sub-agents]]
- Hooks 在 frontmatter 里只在 subagent 生命周期内生效，结束清理；`Stop` 事件自动转 `SubagentStop`；`SubagentStart` / `SubagentStop` 也可在主 `settings.json` 里配 [[sub-agents]]

## 出现来源

_104 summaries reference this entity_:

- [[2026-w15]]
- [[2026-w17]]
- [[README--explanatory-output-style]]
- [[README--plugin-dev]]
- [[SKILL--command-development]]
- [[advanced-plugin]]
- [[agent-creation-prompt]]
- [[agent-creation-system-prompt]]
- [[agent-creator--plugin-dev]]
- [[agent-development-skill--plugin-dev]]
- [[agent-loop]]
- [[agent-sdk-dev--readme]]
- [[agent-sdk-verifier-py]]
- [[agent-sdk-verifier-ts]]
- [[agent-teams]]
- [[analyzer--skill-creator]]
- [[best-practices]]
- [[changelog]]
- [[changelog--claude-code-repo]]
- [[claude-code-features]]
- [[claude-code-on-the-web]]
- [[claude-directory]]
- [[cli-reference]]
- [[code-architect]]
- [[code-explorer--plugin-agent]]
- [[code-review--plugin-command]]
- [[code-review--readme]]
- [[code-reviewer]]
- [[code-simplifier--plugin-agent]]
- [[command-development--readme]]
- [[commands]]
- [[comment-analyzer]]
- [[common-workflows]]
- [[comparator--skill-creator]]
- [[complete-agent-examples]]
- [[component-patterns--plugin-dev]]
- [[context-window]]
- [[conversation-analyzer--hookify]]
- [[costs]]
- [[create-plugin]]
- [[debug-your-config]]
- [[discover-plugins]]
- [[doc-coauthoring-skill]]
- [[editing--pptx]]
- [[env-vars]]
- [[errors]]
- [[feature-dev-cmd--feature-dev]]
- [[feature-dev-readme--feature-dev]]
- [[features-overview]]
- [[glossary]]
- [[grader--skill-creator-agent]]
- [[headless]]
- [[hook-development--SKILL]]
- [[hookify]]
- [[hooks]]
- [[hooks--agent-sdk]]
- [[hooks-guide]]
- [[how-claude-code-works]]
- [[interactive-mode]]
- [[manifest-reference--plugin-structure]]
- [[memory]]
- [[model-config]]
- [[model_behavior]]
- [[monitoring-usage]]
- [[new-sdk-app--agent-sdk-dev]]
- [[output-styles]]
- [[overview--agent-sdk]]
- [[overview--claude-code]]
- [[permission-modes]]
- [[permissions]]
- [[permissions--claude-code]]
- [[plugin-commands-examples--plugin-dev]]
- [[plugin-features-reference]]
- [[plugin-settings--skill]]
- [[plugin-structure-skill--plugin-dev]]
- [[plugin-validator]]
- [[plugins]]
- [[plugins--agent-sdk]]
- [[plugins-readme--claude-code-repo]]
- [[plugins-reference]]
- [[pptx-skill]]
- [[pr-review-toolkit-readme]]
- [[pr-test-analyzer--pr-review-toolkit]]
- [[real-world-examples]]
- [[review-pr]]
- [[settings]]
- [[silent-failure-hunter]]
- [[skill-reviewer--plugin-agent]]
- [[skills]]
- [[skills--agent-sdk]]
- [[slash-commands--agent-sdk]]
- [[standard-plugin]]
- [[statusline]]
- [[sub-agents]]
- [[subagents--agent-sdk]]
- [[system-prompt-design--plugin-dev]]
- [[todo-tracking]]
- [[tool-usage--mcp-integration]]
- [[tools-reference]]
- [[triggering-examples]]
- [[troubleshooting]]
- [[type-design-analyzer--plugin-agent]]
- [[typescript--agent-sdk]]
- [[user-input]]

## 相关

- [[Agent-team]] — agent teams 是 subagent 的"水平扩展"：teammates 互发消息 + 共享任务列表，subagent 只能向 main 汇报
- [[Agentic-loop]] — subagent 自己跑独立的 agentic loop，loop 终止后才把结果回传父 loop
- [[Context-window]] — subagent 的核心价值是新建一个独立 context window，避免污染主上下文
- [[Permission-mode]] — subagent 的权限模式继承自父，bypass / acceptEdits / auto 模式下子级不能 override
- [[Hooks]] — `SubagentStart` / `SubagentStop` 在主 session 触发；frontmatter 里的 hooks 限于 subagent 生命周期
- [[Skill]] — `skills` frontmatter 字段可预加载 skill（注入完整内容，不能预载 disable-model-invocation 类型）
- [[Agent-SDK]] — SDK 通过 `agents={}` 编程定义 subagent，行为对齐 CLI
