---
type: summary
source: 01_Raw/docs.openai.com/docs/guides/tools-remote-mcp.md
source_url: https://platform.openai.com/docs/guides/tools-remote-mcp
title: "OpenAI — MCP 和 Connectors"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: [Tool-use]
---

## 核心要点

Responses API 支持通过 `mcp` tool 类型连接远程 MCP server 或 OpenAI 托管的 Connectors，赋予模型访问外部服务的能力。

### 两种类型

- **Connectors**：OpenAI 维护的 MCP wrapper，适配 Google Workspace、Dropbox 等主流服务
- **Remote MCP servers**：公网上任何实现 MCP 协议的服务器

### 快速示例

```python
resp = client.responses.create(
    model="gpt-5.5",
    tools=[{
        "type": "mcp",
        "server_label": "dmcp",
        "server_url": "https://dmcp-server.deno.dev/sse",
        "require_approval": "never",
    }],
    input="Roll 2d4+1",
)
```

### 工作流程

1. **列出工具**：API 向 MCP server 请求工具列表，生成 `mcp_list_tools` 输出 item
2. **调用工具**：模型决定调用时，API 代为发请求，返回 `mcp_call` item（含 `arguments` 和 `output`）

`mcp_list_tools` 存在于 context 中时，同一对话不会重复拉取工具列表。

### 审批控制（`require_approval`）

- 默认 `"always"` —— 每次 tool call 前需审批（`mcp_approval_request`）
- 设为 `"never"` —— 跳过审批
- 也可指定特定工具名列表

### 认证

通过 `authorization` 字段传入 OAuth access token（每次请求都需传入，API 不存储该值）。

### 可用 Connectors

Dropbox、Gmail、Google Calendar、Google Drive、Microsoft Teams、Outlook Calendar、Outlook Email、SharePoint

### 安全风险

- 恶意 MCP server 可通过 prompt injection 窃取数据
- 建议使用服务提供商官方 server（如 Stripe 官方 `mcp.stripe.com`）
- 建议日志记录所有发往 MCP server 的数据
- 审批敏感操作，谨慎使用 `require_approval: "never"`

### 速率限制

Tier 1: 200 RPM；Tier 2/3: 1000 RPM；Tier 4/5: 2000 RPM
