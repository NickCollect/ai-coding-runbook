---
type: entity
name: Scheduled-task
aliases: [scheduled task, scheduled tasks]
category: feature
status: ga
created: 2026-05-05
---

## 一句话定义

Claude Code 桌面端的定时任务

## 关键属性

- 桌面端 Routines 页面创建本地定时任务，**只在 app 打开 + 电脑唤醒**时运行；最小间隔 1 分钟 [[desktop-scheduled-tasks]] [[scheduled-tasks]]
- 创建表单：Name（kebab-case，做文件夹名）、Description、Instructions（含 model + permission mode 选择 + working folder + worktree toggle）、Schedule [[desktop-scheduled-tasks]]
- Schedule 预设：Manual（仅手动跑）/ Hourly / Daily（默认 9am 本地时间） / Weekdays（跳 Sat/Sun）/ Weekly；其他 cadence 用对话写自然语言（"每 6 小时跑一次所有测试"） [[desktop-scheduled-tasks]]
- 每分钟检查一次 schedule，到点起新 session；每个 task 加小幅 deterministic delay 错峰；本地通知 + 在 sidebar "Scheduled" section 显示新 session [[desktop-scheduled-tasks]]
- 默认对当前 working directory 状态（含未提交改动）跑；创建时勾 worktree toggle 可让每次跑在独立 git worktree 里 [[desktop-scheduled-tasks]]
- Missed runs：app 启动 / 唤醒后查 7 天内 missed，最多跑**一次** catch-up（最近一次的）；建议在 prompt 里加时间 guardrail（"只 review 今天的 commit"） [[desktop-scheduled-tasks]]
- Permission：Ask 模式 + 未 pre-approved 的 tool 会**stall** 等批准；建议创建后手动跑一次并 always-allow 各项 prompt [[desktop-scheduled-tasks]]
- 任务文件路径：`~/.claude/scheduled-tasks/<task-name>/SKILL.md`（或 `CLAUDE_CONFIG_DIR`），YAML frontmatter `name`/`description` + body prompt；schedule/folder/model/enabled 不在文件中只能 GUI 修改 [[desktop-scheduled-tasks]]
- 与 CLI session-scoped 的 `/loop` 区别：CLI session 任务在 `--resume` 时恢复，桌面任务跨重启持久；最小 1min vs `/loop` 1min [[scheduled-tasks]] [[desktop-scheduled-tasks]]
- CLI 也有 session-scoped 的 cron tools — `CronCreate` / `CronList` / `CronDelete`（每 session ≤50）；触发器跑 5-field cron 表达式，本地时区 [[scheduled-tasks]] [[tools-reference]]
- One-time reminders 用自然语言："remind me at 3pm to push the release branch"；single-fire，自动删除 [[scheduled-tasks]] [[desktop-scheduled-tasks]]
- Recurring 任务**七天后**最后跑一次再自动删除；要更长 cadence 用 Routines（cloud）/ GitHub Actions [[scheduled-tasks]]
- Jitter：recurring 最多 10% 周期延迟（≤15min），整点 one-shot 最多提前 90s；要避免 jitter 用非 `:00`/`:30` 的分钟字段 [[scheduled-tasks]]
- 关闭电脑（合上盖子）会让任务被 skip — Settings → Desktop app → General 开"Keep computer awake"缓解 [[desktop-scheduled-tasks]]
- 与 cloud Routines / `/loop` 三者比较表见 raw：本地任务最适合需要本地文件 / tool 访问的场景 [[desktop-scheduled-tasks]] [[scheduled-tasks]]
- 全局禁用 scheduler：`CLAUDE_CODE_DISABLE_CRON=1` [[scheduled-tasks]]

## 出现来源

_8 summaries reference this entity_:

- [[common-workflows]]
- [[desktop]]
- [[desktop-quickstart]]
- [[desktop-scheduled-tasks]]
- [[overview--claude-code]]
- [[platforms]]
- [[scheduled-tasks]]
- [[tools-reference]]

## 相关

- [[Routine]] — Anthropic 云端等价物，不需要本机开机
- [[Native-interface]] — Routines 页面是 Desktop 的功能
- [[CI-integration]] — GitHub Actions 提供另一种 repo-event 触发的定时机制
- [[Permission-mode]] — 每个任务可独立选 permission mode；未授权 tool 会 stall
- [[Slash-command]] — `/loop` 是 session 内更轻量的轮询替代
- [[MCP-server]] — 任务可调用配置好的 MCP server 完成外部操作
