---
type: entity
name: Routine
aliases: [routines, scheduled routine]
category: feature
status: ga
created: 2026-05-05
---

## 一句话定义

Claude Code 在云端按 cron 跑的 scheduled agent

## 关键属性

- **Research preview**：Routine = 保存的 Claude Code 配置（prompt + repos + connectors），在 Anthropic 托管的云基础设施上自动跑（笔记本关了也能跑）；管理入口 `claude.ai/code/routines` 或 CLI `/schedule` [[routines]]
- 可用 plan：Pro / Max / Team / Enterprise，需启用 Claude Code on the web；属于个人 claude.ai 账户，**不**与 teammate 共享，计入个人日运行配额 [[routines]]
- 三种 trigger（可组合）：**Schedule**（每小时 / 每天 / 工作日 / 每周 / 一次性，最小 1 小时间隔；one-off 触发后自动 disable）、**API**（HTTPS endpoint + bearer token，POST `/fire` 带可选 `text` body）、**GitHub**（pull request / release 事件，filter 字段+操作符如 contains / matches regex） [[routines]]
- GitHub trigger regex 注意：**测试整个 field**，要 substring 用 `.*hotfix.*` 或换 `contains` 操作符 [[routines]]
- 每次 run = 完整 Claude Code 云 session，**完全自主**（无 permission-mode picker、无 mid-run 审批），可跑 shell、用 repo committed skill、调 connector 写入操作 [[routines]]
- 默认分支保护：默认 Claude 只能 push 到 `claude/`-前缀分支；按 repo 切换 "Allow unrestricted branch pushes" 才能 push 已有分支 [[routines]]
- 行为以 user 身份呈现：通过 GitHub identity / connector 的 commit / PR / Slack message / Linear ticket **以 you 出现** —— 后续可能触发其他 webhook 自动化（review repos before enabling） [[routines]] [[claude-code-on-the-web]]
- 环境配置：每个 routine 绑定一个 cloud env（network access level + env vars + setup script），setup script cached ~7 天，仅在 script 或 allowed hosts 变更时 re-run；每次 run 重新 clone repo（无本地文件） [[routines]] [[claude-code-on-the-web]]
- API trigger 调用（beta header `experimental-cc-routine-2026-04-01`）：`curl -X POST https://api.anthropic.com/v1/claude_code/routines/<id>/fire -H "Authorization: Bearer sk-ant-oat01-..."`；返回 `claude_code_session_id` + `claude_code_session_url`；token 仅生成时显示一次，CLI 不能创建 / 撤销 token [[routines]]
- GitHub trigger 前置：要安装 Claude GitHub App（`/web-setup` 仅授予 clone 权限，**不等于** 装 App）；研究预览期有每 routine + 每账号每小时 webhook 上限 [[routines]]
- CLI 用法：`/schedule "daily PR review at 9am"` 重复；`/schedule "tomorrow at 9am, summarize yesterday's merged PRs"` 一次性；`/schedule list/update/run`；CLI **只能创建 schedule trigger**，API / GitHub trigger 必须走 web UI [[routines]]
- 与 Desktop scheduled task / `/loop` 的对比：Routine 跑在 Anthropic cloud（不要求机器开），fresh clone（无本地文件），autonomous（无 permission prompt），最小 1 小时间隔 —— Desktop 跑本机要求 app 开 / 1 分钟最小，`/loop` 要求 session 开 / 1 分钟最小 [[routines]] [[scheduled-tasks]] [[desktop-scheduled-tasks]]
- 用量：与交互 session 一样消耗订阅额度，**额外**计入每日 routine-run 配额；one-off run 不计入日 cap 但仍消耗订阅；组织 "extra usage" 允许 routine 在计费 overage 上继续 [[routines]]
- 典型用例：backlog 维护、alert triage（POST stack trace → 开 draft PR）、bespoke code review（PR opened → checklist）、deploy verification（CD 调 API）、docs drift、library port（PR closed-merged → port 到平行 SDK） [[routines]]

## 出现来源

_11 summaries reference this entity_:

- [[2026-w16]]
- [[claude-code-on-the-web]]
- [[commands]]
- [[common-workflows]]
- [[desktop]]
- [[desktop-scheduled-tasks]]
- [[overview--claude-code]]
- [[platforms]]
- [[routines]]
- [[scheduled-tasks]]
- [[whats-new]]

## 相关

- [[Scheduled-task]] — Desktop / `/loop` 的本机定时与 Routine 的云端定时形成对照（最小间隔、是否需机器开、本地文件访问差异）
- [[Native-interface]] — Routine 通过 web (claude.ai/code/routines) 与 CLI (`/schedule`) 双入口管理；属 Claude Code on the web 体系
- [[CI-integration]] — Routine 的 GitHub trigger 与 GitHub Actions 都能基于 PR/release 事件触发，但 Routine 跑在 Anthropic 云
- [[MCP-server]] — Routine 可调用绑定 connector（基于 MCP）执行外部写入操作
- [[Permission-mode]] — Routine 完全自主、不走 permission picker，与本地 permission mode 体系不同
