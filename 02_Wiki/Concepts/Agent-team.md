---
type: concept
name: Agent-team
aliases: [agent teams, subagent team]
category: concept
status: ga
created: 2026-05-05
---

## 一句话定义

多个 subagent 协作组成的 team

## 关键属性

- 实验性功能（Claude Code v2.1.32+），开关 `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`；协调多个 Claude Code 实例：1 lead + 多 teammate，各自独立 context window [[agent-teams]] [[glossary]]
- 与 Subagent 的根本区别：subagent 只把结果汇总回主线；teammate 之间可直接 message，共享 task list，自主认领工作；用户也能直接 message 任意 teammate [[agent-teams]] [[sub-agents]]
- 适合场景：研究/审查需要多视角、并行模块开发、调试相互竞争的假设、跨层（前端+后端+测试）协调；不适合顺序工作 / 同文件编辑 / 强依赖任务 [[agent-teams]]
- 显示模式两种：**in-process**（Shift+Down 切换 teammate，Ctrl+T 切 task list）/ **split-pane**（要求 tmux 或 iTerm2 + `it2` CLI）；`teammateMode` setting 控制，`auto` 在 tmux 中自动选 split [[agent-teams]]
- CLI flag `--teammate-mode in-process|tmux|auto` 覆盖 setting [[cli-reference]] [[agent-teams]]
- 架构存储：team config 在 `~/.claude/teams/{team-name}/config.json`（自动管理，不要手编）；task list 在 `~/.claude/tasks/{team-name}/`（file locking 防 race）；**无 project-level config** [[agent-teams]]
- Teammate 用 subagent definition 实例化（project / user / plugin / CLI 任一 scope）：继承 `tools` allowlist + `model`，body 拼到 system prompt 后；**`skills` 与 `mcpServers` frontmatter 被忽略**，teammate 像普通 session 一样从 project+user settings 加载；`SendMessage` 与 task tool 始终可用 [[agent-teams]]
- Permission：teammate 起始 mode 同 lead；spawn 后可单独切换，但 spawn 时不能预设 [[agent-teams]]
- 质量门 hooks：`TeammateIdle` / `TaskCreated` / `TaskCompleted`，exit code 2 把 feedback 送回 [[agent-teams]]
- Plan 审批模式：让 lead 要求 teammate 先出 plan，teammate 留在 plan mode 直到 lead 批/拒 [[agent-teams]]
- 最佳实践：3-5 teammate；每 teammate 5-6 task；任务设计成 self-contained 单元；预批 permission；告诉 lead 等 teammate；先用研究/审查类；避开文件冲突 [[agent-teams]]
- 主要限制：in-process teammate 不能用 `/resume`/`/rewind` 恢复；task status 有滞后；**一 session 一 team**；不支持 nested team；lead 固定；split pane 在 VS Code / Windows Terminal / Ghostty 内置终端不可用 [[agent-teams]]
- Token 成本对比：subagent 较便宜（结果摘要回返）；agent team 更贵（每 teammate 是完整实例） [[agent-teams]]
- 在 Web (`claude.ai/code`) 上默认关，需 `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` 才启 [[claude-code-on-the-web]]
- 与 `/ultrareview` 的关系：ultrareview 是基于 web 基建跑的多 agent fleet code review，是 agent team 思路在云端的一个产品化形态 [[ultrareview]]

## 出现来源

_21 summaries reference this entity_:

- [[2026-w17]]
- [[agent-teams]]
- [[best-practices]]
- [[changelog]]
- [[claude-code-features]]
- [[claude-code-on-the-web]]
- [[cli-reference]]
- [[code-review]]
- [[costs]]
- [[desktop]]
- [[features-overview]]
- [[glossary]]
- [[hooks]]
- [[hooks-guide]]
- [[overview--claude-code]]
- [[real-world-examples]]
- [[review-pr]]
- [[sub-agents]]
- [[subagents--agent-sdk]]
- [[tools-reference]]
- [[ultrareview]]

## 相关

- [[Subagent]] — Agent team 用 subagent definition 作 teammate；二者通信模型与成本结构不同
- [[Hooks]] — `TeammateIdle` / `TaskCreated` / `TaskCompleted` 是 agent team 专属事件
- [[Settings]] — `teammateMode` 决定显示形式
- [[Agentic-loop]] — 每个 teammate 都跑独立的 agentic loop
- [[Context-window]] — 每 teammate 独立 context 是 agent team vs subagent 的关键差异
- [[Permission-mode]] — teammate 起始 mode 继承 lead，但 spawn 后可单独调整
