---
type: summary
source: 01_Raw/docs.cursor.com/docs--enterprise--model-and-integration-management.md
source_url: https://cursor.com/docs/enterprise/model-and-integration-management
title: "Enterprise 模型与集成管理"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Enterprise 可控制团队成员可使用的 AI 模型和 MCP 服务器，防止未授权使用和成本失控。

**模型访问控制**（Enterprise 专属）：在 Dashboard → Settings → Model Access Control 配置；新模型发布时 Enterprise 团队可选择是否为组织启用（而非自动推送）。

**BYOK 限制**：Enterprise 可禁止成员使用自己的 API Key（OpenAI/Anthropic/Azure/AWS Bedrock），所有用量统一走 Cursor 用量池。

**MCP 白名单管理**：
- Dashboard → MCP Configuration 配置 MCP 白名单
- 支持通过 MDM 部署 `~/.cursor/permissions.json` 文件管理自动运行允许列表
- 白名单语法 `server:tool`（支持 `*` 通配符）
- stdio 服务器：白名单匹配完整命令字符串（含路径，建议用 `*npx -y @acme/*` 格式）
- HTTP/URL 服务器：白名单匹配完整 URL
- 优先级：Dashboard > permissions.json > 编辑器设置（高优先级替换低优先级，不合并）

**仓库 Blocklist**（Enterprise）：Dashboard → Repository Blocklist 禁止 Agent 访问特定仓库。

**集成管理**：Slack/GitHub/GHES/GitLab/Linear 集成文档参见对应集成页面。
