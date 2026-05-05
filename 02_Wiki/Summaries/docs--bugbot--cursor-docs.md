---
type: summary
source: 01_Raw/docs.cursor.com/docs--bugbot.md
source_url: https://cursor.com/docs/bugbot
title: "Bugbot（PR 代码审查）"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Bugbot 自动分析 PR diff，发现 Bug、安全问题和代码质量问题，并留下带说明和修复建议的评论，支持 GitHub 和 GitLab。

**工作方式**：每次 PR 更新自动运行；也可评论 `cursor review` 或 `bugbot run` 手动触发；读取现有 PR 评论作为上下文避免重复建议；"Fix in Cursor"链接直接在 IDE 中修复，"Fix in Web"在 cursor.com/agents 修复。

**规则体系**（优先级由高到低）：Team Rules → Repository rules（已学习规则 + 手动规则）→ 项目 `.cursor/BUGBOT.md`（支持嵌套目录）→ User Rules。可在 PR 评论 `@cursor remember [fact]` 实时教授新规则。

**Autofix**：发现 Bug 后自动生成 Cloud Agent 修复，可推送到新分支（推荐）或现有分支（最多 3 次防止循环）。需开启 usage-based pricing 和 Storage。

**计费**：免费层（每月限量 PR 评审）+ Pro 层（$40/月/用户）。Pro：个人 200 PR/月上限；团队按活跃用户数计费，每许可 200 PR/月上限。

**规则配置**：`name`、`rule_content`（指令）、`scoped_paths`（可选 glob 模式）。规则分析面板显示 Issues Found、PRs Reviewed、Accepted Issues、Acceptance Rate 等指标。

**Admin API**：管理员可通过 `/bugbot/repo/update`、`/bugbot/repos`、`/bugbot/user/update` 等 REST 端点自动化管理仓库和用户访问（速率限制 60 RPM）。
