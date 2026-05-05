---
type: summary
source: 01_Raw/docs.cursor.com/docs--cloud-agent--settings.md
source_url: https://cursor.com/docs/cloud-agent/settings
title: "Cloud Agent Settings"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Cloud Agent dashboard 设置供管理员配置默认模型、仓库、网络访问和安全策略。

**默认设置**：Default model（默认模型，需支持 Max Mode）、Default repository（省略仓库选择步骤）、Base branch（PR 分叉基准分支，默认使用仓库默认分支）。

**网络访问设置**：三种模式（Allow all / Default + allowlist / Allowlist only），用户设置优先于团队默认，除非管理员锁定。

**安全设置**（需管理员权限）：
- Display agent summary：控制是否在侧边栏显示 Agent 的文件差异图像和代码片段
- Display agent summary in external channels：延伸到 Slack 等外部渠道
- Team follow-ups：控制团队成员是否可以向其他用户创建的 Agent 发送追加消息（三选项：Disabled / Service accounts only / All）

**团队功能**：Long running agents（长时运行控制）、Computer use（计算机操控，仅 Enterprise）。

**Team follow-ups 安全警告**：启用后，成员可影响另一用户的 Agent 执行，该 Agent 持有原始创建者的密钥和凭证，存在横向移动和密钥泄露风险，需与共享 SSH 密钥同等谨慎对待。
