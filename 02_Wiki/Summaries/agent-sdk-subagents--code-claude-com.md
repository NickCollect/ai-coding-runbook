---
type: summary
source: 01_Raw/code.claude.com/docs/en/agent-sdk/subagents.md
source_url: https://code.claude.com/docs/en/agent-sdk/subagents
title: "Claude Agent SDK — Subagents（子 agent）"
summarized_at: 2026-05-05
entities_referenced:
  - Agent-SDK.md
  - Anthropic-SDK-Python.md
  - Anthropic-SDK-TypeScript.md
concepts_referenced:
  - Agent-team.md
  - Agentic-loop.md
  - Tool-use.md
---

Subagents 是主 agent 可以派生的独立 agent 实例，用于处理聚焦子任务。通过 Subagents 实现上下文隔离、并行执行和专业化指令，而不会膨胀主 agent 的 context。

## 三种创建方式

1. **编程方式（推荐）**：在 `query()` 的 `agents` 参数中定义——本文档主要介绍此方式
2. **文件系统方式**：在 `.claude/agents/` 目录中以 Markdown 文件定义
3. **内置通用 subagent**：Claude 在 `allowedTools` 包含 `Agent` 时可自动派生 `general-purpose` subagent

## 核心优势

- **上下文隔离**：子 agent 运行在独立的新对话中，中间工具调用不累积到主 agent；主 agent 只收到子 agent 的最终消息
- **并行化**：多个子 agent 可并发运行，大幅加速复杂工作流
- **专业化指令**：每个子 agent 有自己的 system prompt，包含领域专业知识
- **工具限制**：子 agent 只能访问指定工具，减少意外操作风险

## 定义 Subagents

```python
from claude_agent_sdk import query, ClaudeAgentOptions, AgentDefinition

async for message in query(
    prompt="Review the authentication module for security issues",
    options=ClaudeAgentOptions(
        allowed_tools=["Read", "Grep", "Glob", "Agent"],  # 必须包含 Agent 工具
        agents={
            "code-reviewer": AgentDefinition(
                description="Expert code review specialist. Use for quality, security, and maintainability reviews.",
                prompt="You are a code review specialist...",
                tools=["Read", "Grep", "Glob"],   # 只读权限
                model="sonnet",                   # 模型 override
            ),
            "test-runner": AgentDefinition(
                description="Runs and analyzes test suites.",
                prompt="You are a test execution specialist...",
                tools=["Bash", "Read", "Grep"],   # 允许执行命令
            ),
        },
    ),
):
    if hasattr(message, "result"):
        print(message.result)
```

## `AgentDefinition` 配置参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `description` | string | 是 | Claude 据此决定何时调用该 subagent |
| `prompt` | string | 是 | Subagent 的 system prompt，定义角色和行为 |
| `tools` | string[] | 否 | 允许的工具列表；省略则继承所有父工具 |
| `disallowedTools` | string[] | 否 | 从工具集中移除的工具 |
| `model` | string | 否 | 模型 override（`'sonnet'`/`'opus'`/`'haiku'`/完整模型 ID）|
| `skills` | string[] | 否 | 可用的 skill 名称列表 |
| `memory` | string | 否 | 内存来源（`'user'`/`'project'`/`'local'`）|
| `mcpServers` | array | 否 | 子 agent 可访问的 MCP servers |
| `maxTurns` | number | 否 | 最大 agentic turns 数 |
| `background` | boolean | 否 | 以非阻塞后台任务方式运行 |
| `effort` | string/number | 否 | 推理 effort 级别 |
| `permissionMode` | PermissionMode | 否 | 工具执行权限模式 |

> 子 agent 不能派生自己的子 agent，不要在 `tools` 中包含 `Agent`。

## Subagent 的上下文继承

子 agent 以全新对话开始，但不是空的：

| 子 agent **获得** | 子 agent **不获得** |
|-----------------|-------------------|
| 自己的 system prompt + Agent 工具的 prompt 字符串 | 父 agent 的对话历史或工具结果 |
| 项目 CLAUDE.md（通过 `settingSources` 加载）| Skills（除非在 `skills` 中列出）|
| 工具定义（继承自父或 `tools` 子集）| 父 agent 的 system prompt |

**唯一从父到子的传递渠道**是 Agent 工具的 prompt 字符串——所有子 agent 所需的文件路径、错误信息、决策都必须包含在这个字符串中。

## 调用方式

- **自动调用**：Claude 根据任务和 `description` 自动决定调用哪个 subagent
- **显式调用**：在 prompt 中点名："Use the code-reviewer agent to check the authentication module"

## 检测 Subagent 调用

Subagents 通过 Agent 工具调用（旧版 SDK 为 `Task` 工具）。消息中含 `parent_tool_use_id` 字段表示来自子 agent 上下文：

```python
for block in message.content:
    if getattr(block, "type", None) == "tool_use" and block.name in ("Task", "Agent"):
        print(f"Subagent invoked: {block.input.get('subagent_type')}")
if hasattr(message, "parent_tool_use_id") and message.parent_tool_use_id:
    print("  (running inside subagent)")
```

## Resume Subagents

子 agent 可以被恢复。需要：
1. 从第一次 query 中捕获 `session_id`
2. 解析 `agentId`（出现在 Agent 工具结果文本中）
3. 在第二次 query 中传入 `resume: sessionId` 并在 prompt 中提及 `agentId`

子 agent transcript 独立存储，主对话压缩不影响子 agent 历史，默认保留 30 天（`cleanupPeriodDays`）。

## 工具限制常用组合

| 场景 | 工具 |
|------|------|
| 只读分析 | `Read`, `Grep`, `Glob` |
| 运行测试 | `Bash`, `Read`, `Grep` |
| 代码修改 | `Read`, `Edit`, `Write`, `Grep`, `Glob` |
| 完全访问 | 省略 `tools` 字段（继承父工具）|
