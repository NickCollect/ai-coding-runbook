---
type: summary
source: 01_Raw/code.claude.com/docs/en/agent-sdk/overview.md
source_url: https://code.claude.com/docs/en/agent-sdk/overview
title: "Claude Agent SDK — 概览"
summarized_at: 2026-05-05
entities_referenced:
  - Agent-SDK.md
  - Anthropic-SDK-Python.md
  - Anthropic-SDK-TypeScript.md
  - Hooks.md
concepts_referenced:
  - Agentic-loop.md
  - Tool-use.md
  - Agent-team.md
---

Claude Agent SDK（原名 Claude Code SDK）是一个可编程库，让开发者能够以 Python 或 TypeScript 构建自主 AI agent，这些 agent 内置了 Claude Code 所有的工具执行能力。

> 注：如正在从旧版 SDK 迁移，参见 Migration Guide。Opus 4.7 需要 Agent SDK v0.2.111 或更高版本。

## 安装

```bash
# TypeScript（内置 Claude Code binary，无需额外安装 claude）
npm install @anthropic-ai/claude-agent-sdk

# Python
pip install claude-agent-sdk
```

## 核心用法

`query()` 函数是主入口，返回异步迭代器，流式输出 Claude 工作过程中的所有消息：

```python
# Python
from claude_agent_sdk import query, ClaudeAgentOptions
async for message in query(
    prompt="Find and fix the bug in auth.py",
    options=ClaudeAgentOptions(allowed_tools=["Read", "Edit", "Bash"]),
):
    print(message)
```

```typescript
// TypeScript
import { query } from "@anthropic-ai/claude-agent-sdk";
for await (const message of query({
    prompt: "Find and fix the bug in auth.ts",
    options: { allowedTools: ["Read", "Edit", "Bash"] }
})) { console.log(message); }
```

## 内置工具

| 工具 | 功能 |
|------|------|
| Read | 读取工作目录内任意文件 |
| Write | 创建新文件 |
| Edit | 精确编辑现有文件 |
| Bash | 运行 shell 命令、脚本、git 操作 |
| Monitor | 监听后台脚本输出，逐行响应 |
| Glob | 按模式查找文件（如 `**/*.ts`）|
| Grep | 用正则搜索文件内容 |
| WebSearch | 搜索网络获取最新信息 |
| WebFetch | 抓取并解析网页内容 |
| AskUserQuestion | 向用户提问（多选题形式）|

## 主要能力

- **Hooks**：在 agent 生命周期关键节点运行自定义代码（`PreToolUse`、`PostToolUse`、`Stop`、`SessionStart` 等），用于校验、日志、阻断或转换 agent 行为
- **Subagents**：主 agent 可派生专业子 agent 处理聚焦子任务，子 agent 消息中含 `parent_tool_use_id` 字段用于追踪
- **MCP**：通过 `mcpServers` 选项连接数据库、浏览器、外部 API 等（支持数百种 MCP 服务器）
- **Permissions**：通过 `allowedTools` / `disallowedTools` 精确控制工具访问权限
- **Sessions**：跨多次 `query()` 调用保持对话上下文；支持 resume（按 ID 恢复）和 fork（分支探索）
- **Claude Code 配置加载**：默认从 `.claude/` 和 `~/.claude/` 加载 Skills、slash commands、CLAUDE.md 等配置

## 与其他工具对比

| 对比维度 | Agent SDK | 原生 Client SDK | Managed Agents |
|---------|-----------|----------------|---------------|
| 工具执行 | 内置，自动处理 | 需自行实现 tool loop | Anthropic 托管 |
| 运行环境 | 自己的进程/基础设施 | 自己的进程 | Anthropic 托管 sandbox |
| 适用场景 | 本地原型、直接操作文件系统 | 完全自定义 | 生产级无需自运维 sandbox |

典型路径：用 Agent SDK 本地原型开发，再迁移至 Managed Agents 生产部署。

## 品牌指引

合作伙伴可选择是否使用 Claude 品牌。允许：`"Claude Agent"`、`"Claude"`（在已标记 Agents 的菜单内）、`"{YourName} Powered by Claude"`。**不允许**：`"Claude Code"` 或任何模仿 Claude Code 的视觉元素。
