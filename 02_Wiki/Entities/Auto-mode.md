---
type: entity
name: Auto-mode
aliases: [auto mode, auto-mode-config]
category: feature
status: ga
created: 2026-05-05
---

## 一句话定义

Claude Code 的自动批准模式配置

## 关键属性

- 一种 permission mode（v2.1.83+，**research preview**）：每个 tool call 由 classifier model 审核，自动批准多数操作，仅 block 不可逆 / 破坏性 / 疑似 exfiltration 行为，避免人工 prompt [[permission-modes]] [[auto-mode-config]]
- **Plan 限制**：仅 Max / Team / Enterprise / API（Anthropic API）；**不**可用于 Pro、Bedrock、Vertex、Foundry；Team / Enterprise 需 admin 启用 [[auto-mode-config]] [[permission-modes]]
- 模型限制：限定 Sonnet 4.6 / Opus 4.6 / Opus 4.7（Max plan 仅 Opus 4.7） [[permission-modes]]
- 默认信任：cwd + 当前 repo 的 configured remotes；外延（公司 source-control org、team buckets、internal domain）需在 `autoMode.environment` 显式描述 [[auto-mode-config]]
- 三个配置字段：`autoMode.environment`（散文描述可信基础设施）、`autoMode.allow`（覆盖 block 的例外）、`autoMode.soft_deny`（额外 block 规则）；用字面量 `"$defaults"` 拼入内置规则，**遗漏 `$defaults` 会丢弃所有内置规则**（含 force-push 防护、exfil block、`curl|bash` block） [[auto-mode-config]]
- 决策优先级：soft_deny → allow override → 用户对话中的明确意图覆盖（"force-push this branch" 算授权，"clean up the repo" 不算） [[auto-mode-config]]
- 默认 block：`curl | bash`、外发敏感数据、生产 deploy/migrations、批量 cloud 删除、IAM 改动、共享基础设施修改、不可逆销毁 pre-session 文件、force push、push 到 `main` [[permission-modes]]
- 默认允许：本地文件操作、lock file 内的依赖、`.env` 读到对应 API、只读 HTTP、push 到 current branch [[permission-modes]]
- **`autoMode` 不读 shared `.claude/settings.json`** —— 防止 checked-in repo 注入允许规则；可读 user / local / managed / `--settings` flag / Agent SDK 入参；同时读 CLAUDE.md 的行为规则（如 "never force push"） [[auto-mode-config]]
- 退化机制：3 次连续 block 或累计 20 次 → 模式暂停回到 prompt；headless `-p` 模式则中止（无人可问） [[permission-modes]]
- 进入 auto 时：blanket `Bash(*)` / `PowerShell(*)`、wildcard interpreter、`Agent` 规则被暂时丢弃；离开恢复 [[permission-modes]]
- Subagent 行为：classifier 在 spawn 时检查任务、每个 subagent 动作时检查、完成时检查全 history；**subagent frontmatter 的 `permissionMode` 在 auto 模式下被忽略** [[permission-modes]]
- Classifier 输入：user msg + tool calls + CLAUDE.md，**不看 tool results**（避免被注入操纵）；server 端额外扫描 incoming tool result 中的可疑内容 [[permission-modes]] [[glossary]]
- "对话中说的边界" 视作 block 信号，**每次都重读 transcript**（compaction 会丢；要硬保证用 `permissions.deny`） [[permission-modes]]
- CLI 检视：`claude auto-mode defaults`（打印内置 JSON）、`claude auto-mode config`（展开 `$defaults` 后的 effective config）、`claude auto-mode critique`（AI 反馈自定义规则） [[auto-mode-config]]
- Denial 复盘：`/permissions` 的 "Recently denied" tab，按 `r` 标记重试；重复 denial 通常是 environment 缺上下文；可用 `PermissionDenied` hook 程序化反应（返回 `{retry: true}`） [[auto-mode-config]] [[hooks]]
- 安全护栏：硬 block 用 `permissions.deny`（在 classifier 之前执行）；server-managed 可下发 `autoMode.environment` 给整个组织 [[auto-mode-config]] [[server-managed-settings]]

## 出现来源

_24 summaries reference this entity_:

- [[2026-w13]]
- [[2026-w14]]
- [[2026-w16]]
- [[2026-w17]]
- [[agent-loop]]
- [[auto-mode-config]]
- [[best-practices]]
- [[changelog]]
- [[changelog--claude-code-repo]]
- [[cli-reference]]
- [[commands]]
- [[desktop]]
- [[devcontainer]]
- [[env-vars]]
- [[errors]]
- [[glossary]]
- [[hooks]]
- [[how-claude-code-works]]
- [[permission-modes]]
- [[permissions]]
- [[permissions--claude-code]]
- [[server-managed-settings]]
- [[settings]]
- [[whats-new]]

## 相关

- [[Permission-mode]] — auto 是六种 permission mode 之一，与 `default` / `acceptEdits` / `plan` / `dontAsk` / `bypassPermissions` 并列
- [[Settings]] — `autoMode.{environment,allow,soft_deny}` / `disableAutoMode` 在 settings.json 配置；read scope 受限
- [[Hooks]] — `PermissionDenied` hook 可对 classifier 阻断做程序化反应；`autoMode` 不读 tool results 但 hook 可介入
- [[Subagent]] — auto 模式下 classifier 检查 subagent spawn / 每个动作 / 完成 history；subagent 自己的 `permissionMode` 被忽略
- [[Sandboxing]] — auto 模式与 sandbox 互补，sandbox 提供 OS 级硬隔离 vs classifier 的语义判断
- [[Memory]] — classifier 读 CLAUDE.md（行为规则如 "never force push"），不读 auto-memory 写出的内容
