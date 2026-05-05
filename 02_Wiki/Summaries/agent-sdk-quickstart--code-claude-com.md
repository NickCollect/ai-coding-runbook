---
type: summary
source: 01_Raw/code.claude.com/docs/en/agent-sdk/quickstart.md
source_url: https://code.claude.com/docs/en/agent-sdk/quickstart
title: "Claude Agent SDK — Quickstart（构建第一个 bug-fixing agent）"
summarized_at: 2026-05-05
entities_referenced:
  - Agent-SDK.md
  - Anthropic-SDK-Python.md
  - Anthropic-SDK-TypeScript.md
concepts_referenced:
  - Agentic-loop.md
  - Tool-use.md
---

Agent SDK Quickstart 通过构建一个自动查找并修复代码 bug 的 agent，演示了 SDK 的核心工作方式。

## 前置条件

- Node.js 18+ 或 Python 3.10+
- Anthropic 账号及 API key

## 安装

```bash
# TypeScript
npm install @anthropic-ai/claude-agent-sdk

# Python（uv，推荐）
uv init && uv add claude-agent-sdk

# Python（pip）
python3 -m venv .venv && source .venv/bin/activate
pip3 install claude-agent-sdk
```

TypeScript SDK 内置 Claude Code binary，无需单独安装 `claude`。

认证设置：

```bash
# .env 文件或 shell 环境
ANTHROPIC_API_KEY=your-api-key
# 三方云服务商：CLAUDE_CODE_USE_BEDROCK=1 / CLAUDE_CODE_USE_VERTEX=1 / CLAUDE_CODE_USE_FOUNDRY=1
```

## 核心代码结构

创建 `agent.py` 或 `agent.ts`：

```python
# Python
from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage, ResultMessage

async for message in query(
    prompt="Review utils.py for bugs that would cause crashes. Fix any issues you find.",
    options=ClaudeAgentOptions(
        allowed_tools=["Read", "Edit", "Glob"],   # 工具白名单
        permission_mode="acceptEdits",             # 自动批准文件编辑
    ),
):
    if isinstance(message, AssistantMessage):
        for block in message.content:
            if hasattr(block, "text"):
                print(block.text)   # Claude 的推理过程
    elif isinstance(message, ResultMessage):
        print(f"Done: {message.subtype}")
```

## 三个关键组件

1. **`query()`**：主入口，返回异步迭代器，流式输出 Claude 整个工作过程（思考、工具调用、结果）
2. **`prompt`**：自然语言任务描述，Claude 自主决定使用哪些工具
3. **`options`**：配置项，包括 `allowedTools`、`permissionMode`、`systemPrompt`、`mcpServers` 等

`async for` 循环持续运行直到 Claude 完成任务或遇到错误，SDK 自动处理工具执行、上下文管理和重试。

## Permission Modes

| 模式 | 行为 | 适用场景 |
|------|------|---------|
| `acceptEdits` | 自动批准文件编辑和常见文件系统命令，其他需确认 | 受信任开发工作流 |
| `dontAsk` | 拒绝所有不在 `allowedTools` 内的操作 | 锁定的无头 agent |
| `auto`（仅 TypeScript） | 模型分类器逐个批准/拒绝工具调用 | 带安全护栏的自主 agent |
| `bypassPermissions` | 无需确认运行所有工具 | 沙盒 CI，完全受信环境 |
| `default` | 需提供 `canUseTool` 回调处理审批 | 自定义审批流程 |

## 工具组合参考

| 工具组合 | agent 能力 |
|---------|-----------|
| `Read`, `Glob`, `Grep` | 只读分析 |
| `Read`, `Edit`, `Glob` | 分析并修改代码 |
| `Read`, `Edit`, `Bash`, `Glob`, `Grep` | 完全自动化 |

## 常见扩展示例

```python
# 添加 web 搜索
ClaudeAgentOptions(allowed_tools=["Read", "Edit", "Glob", "WebSearch"], permission_mode="acceptEdits")

# 自定义 system prompt
ClaudeAgentOptions(system_prompt="You are a senior Python developer. Always follow PEP 8.", ...)

# 允许执行终端命令
ClaudeAgentOptions(allowed_tools=["Read", "Edit", "Glob", "Bash"], ...)
```

## 故障排除

`API Error: "thinking.type.enabled" is not supported for this model`：升级到 Agent SDK v0.2.111 或更高版本（Opus 4.7 需要此版本以使用 `thinking.type.adaptive`）。
