---
type: summary
source: 01_Raw/docs.cursor.com/docs--integrations--linear.md
source_url: https://cursor.com/docs/integrations/linear
title: "Linear 集成"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

通过 Linear 直接将 Issue 委托给 Cursor Cloud Agent，支持实时状态更新和自动 PR 创建。

**安装**：Dashboard → Integrations → Connect Linear → 连接 Linear 工作区并选择团队 → Authorize → 完成 GitHub 连接和计费设置。

**使用方式**：
- **委托 Issue**：在 Linear 打开 Issue → 点击 assignee 字段 → 选择"Cursor"
- **评论触发**：在评论中 `@Cursor fix the auth bug described above`

**配置选项（在 Issue 描述/评论中）**：`[repo=owner/repo]`、`[branch=feature-branch]`、`[model=claude-3.5-sonnet]`；也可通过 Linear 标签配置（parent 标签为 key，child 标签为 value，如 group "repo" 下子标签 "owner/repo"）。

**仓库选择优先级**：Issue 描述/评论 `[repo=]` → Issue 标签 → Project 标签 → Dashboard 默认仓库。

**高级**：Triage Rules（Linear 项目设置中配置自动化规则，自动委托给 Cursor）；注意：目前 Linear 要求必须有人类 assignee 才能触发规则（限制可能移除）。

Cloud Agent 完成后在 Linear 创建 PR 并显示实时状态，可在 Dashboard → Cloud Agents 追踪进度。
