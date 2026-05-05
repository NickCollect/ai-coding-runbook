---
type: summary
source: 01_Raw/docs.cursor.com/docs--account--teams--analytics.md
source_url: https://cursor.com/docs/account/teams/analytics
title: "Usage Analytics（使用分析）"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Teams/Enterprise 专属的使用分析 dashboard，帮助管理员了解团队使用 Cursor 的方式，支持按用户/目录组/日期筛选（最多 10 用户、90 天）。

**AI 产出指标**：AI Share of Committed Code（提交代码中 AI 占比）、Agent Edits（Agent/Cmd+K 建议和接受量）、Tab Completions（内联补全数量）、Messages Sent（按模式/模型分类）。

**活跃用户**：追踪使用了 Tab、Agent、Background Agent、CLI 任一 AI 功能的独立用户数。

**AI 代码追踪**：对每行 AI 建议生成签名，与后续 git commit 签名比对，在设备本地完成，零 PII 外泄。限制：格式化工具改行可能导致签名失效；暂不支持 Background Agent 和 CLI。

**Conversation Insights**（Enterprise 默认开启）：在设备上分析 Agent 会话，分类工作类型（Category、Work Type、Complexity、Specificity），无需问卷或 ticket 分析即可了解团队工程工作构成。自定义分类维度需 Enterprise。

**Cloud Agent 指标**：Agents Created（按来源）、Pull Requests（开启和合并）、Lines of Code（写入和合并）、Top Repositories、Top Users。

**数据访问**：各图表支持 CSV 下载；Enterprise 可通过 Admin API 编程访问；管理员可见所有成员数据，普通成员可见个人数据和 Leaderboard。
