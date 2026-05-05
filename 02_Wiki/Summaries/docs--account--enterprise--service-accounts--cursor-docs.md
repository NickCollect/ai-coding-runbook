---
type: summary
source: 01_Raw/docs.cursor.com/docs--account--enterprise--service-accounts.md
source_url: https://cursor.com/docs/account/enterprise/service-accounts
title: "Service Accounts（服务账号）"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Enterprise 专属功能，为自动化工作流提供非人类账号，可调用 API、认证 CLI、触发 Cloud Agent，不与个人开发者账号绑定。

**核心特性**：不消耗席位许可证（无额外成本）；用量从团队用量池消耗（与普通用户一致）；触发的 Cloud Agent 运行对所有团队管理员可见；可访问团队 GitHub App 授权的任意仓库。

**创建流程**：Dashboard → Settings → Service Accounts → New Service Account，填写名称和描述。API Key 仅在创建时显示一次，需立即保存。

**使用方式**：
- **API**：`Authorization: Bearer YOUR_SERVICE_ACCOUNT_API_KEY` 请求 Cloud Agents API
- **CLI**：`export CURSOR_API_KEY=your_key` 后运行 `agent` 命令，适合 CI/CD 管道

**API Key 管理**：支持轮换（立即失效旧 key）、归档服务账号（撤销所有 key 但保留审计记录）。

**安全最佳实践**：定期轮换密钥；按功能命名（如"Linear Integration"）；不同自动化流程用独立服务账号；在 analytics dashboard 监控使用情况；归档不再使用的账号。
