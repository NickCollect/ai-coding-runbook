---
type: summary
source: 01_Raw/docs.cursor.com/docs--integrations--slack.md
source_url: https://cursor.com/docs/integrations/slack
title: "Slack 集成"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

在 Slack 中通过 `@cursor` 触发 Cloud Agent 执行开发任务，支持线程上下文和多种配置选项。

**安装**：Dashboard → Integrations → Connect Slack → 在 Slack 工作区安装 → 完成 GitHub 连接、开启按需计费、确认隐私设置。

**基本用法**：`@Cursor [提示词]`（新建 Agent 或在现有 Agent 线程追加）；在消息中包含仓库名自动路由；`@Cursor with opus, fix bug` 指定模型。

**高级选项**：
- `branch=main`（指定基础分支）、`autopr=false`（禁用自动 PR 创建）
- 线程上下文：Agent 读取整个线程作为背景信息
- `@Cursor agent [prompt]`：在有现有 Agent 的线程中强制新建独立 Agent
- 上下文菜单（⋯）：Add follow-up、Delete、View request ID、Give feedback

**仓库路由优先级**：消息内容 → 近期 Agent 活动 → Routing Rules（关键词映射）→ 频道默认 → 个人默认。Routing Rules 在 Dashboard → Cloud Agents 配置。

**频道设置**：`@Cursor settings` 在频道设置默认仓库，对该频道所有成员生效，优先于个人默认。

**隐私**：支持 Privacy Mode；Display agent summary（侧边栏显示文件差异，含代码片段）；Display agent summary in external channels（Slack Connect 跨工作区场景）。
