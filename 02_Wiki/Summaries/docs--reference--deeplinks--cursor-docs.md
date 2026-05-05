---
type: summary
source: 01_Raw/docs.cursor.com/docs--reference--deeplinks.md
source_url: https://cursor.com/docs/reference/deeplinks
title: "Deeplinks（深度链接）"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Deeplinks 允许共享 prompts、命令和规则，点击链接后在 Cursor 中预填内容，用户必须审查确认后才执行，不会自动触发。

**三种类型**：
- **Prompts**：`cursor://anysphere.cursor-deeplink/prompt?text=...`，在 Agent chat 预填 prompt
- **Commands**：`cursor://anysphere.cursor-deeplink/command?name=...&text=...`，创建新命令
- **Rules**：`cursor://anysphere.cursor-deeplink/rule?name=...&text=...`，创建新规则

**Web 格式**：将 `cursor://anysphere.cursor-deeplink/` 替换为 `https://cursor.com/link/`，适用于 Web 场景。cursor.com 的 `/link/...` 路由会重定向到 Cursor 应用。

**URL 长度限制**：最长 8,000 字符（URL 编码后）。

**注意**：共享前检查链接中是否含 API Keys、密码或专有代码等敏感信息。
