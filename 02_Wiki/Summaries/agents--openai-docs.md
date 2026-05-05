---
type: summary
source: 01_Raw/docs.openai.com/docs/guides/agents.md
source_url: https://platform.openai.com/docs/guides/agents
title: "OpenAI — Agents SDK 概览"
summarized_at: 2026-05-05
entities_referenced: [MCP-server, Subagent]
concepts_referenced: [Agentic-loop, Tool-use, Agent-team]
---

## 核心要点

OpenAI Agents SDK 是用于构建 code-first agent 应用的官方 SDK，支持多专家协作、工具调用、状态管理。

### 何时选择什么

| 场景 | 工具 |
|---|---|
| 直接调用模型 | OpenAI client libraries |
| 应用自有 orchestration / 工具 / 审批 / 状态 | **Agents SDK** |
| 托管 workflow editor + ChatKit 部署 | Agent Builder |

### SDK 安装

- TypeScript: `openai/openai-agents-js`
- Python: `openai/openai-agents-python`

### 关键概念

- **Orchestration**：manager agent 委托给 specialist，控制用户侧回复
- **Handoffs**：根据任务上下文转移控制权
- **Guardrails**：输入/输出校验，阻断风险内容
- **Human review (approvals)**：在高风险操作前暂停等待人工确认
- **MCP integration**：通过 MCP server 扩展外部能力

### Sandbox agents

Python Agents SDK 支持 sandbox agents，提供基于容器的执行环境（文件、命令、包、端口、快照、内存）。

### Agent Builder（托管路径）

用于 OpenAI 托管的 workflow 创建与发布。**不支持语音工作流**（语音场景请用 SDK）。
