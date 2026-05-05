---
name: OpenAI Agents SDK
type: entity
vendor: OpenAI
aliases: ["Agents SDK", "openai-agents", "@openai/agents", "openai-agents-python"]
created: 2026-05-05
---

# OpenAI Agents SDK

OpenAI 官方 code-first agent 构建 SDK，支持多专家协作（handoffs）、工具调用、guardrails、human approval 和 MCP 集成；Python 和 TypeScript 双语言支持。

## 关键属性

| 属性 | 值 |
|---|---|
| Vendor | OpenAI |
| Python 包 | `openai-agents`（`pip install openai-agents`） |
| TypeScript 包 | `@openai/agents`（`npm install @openai/agents zod`） |
| 主要用途 | 多 agent 编排、工具调用、流程控制 |
| Traces 面板 | `https://platform.openai.com/traces` |

## 核心功能

### 何时选择 Agents SDK

| 场景 | 工具 |
|---|---|
| 直接调用模型 | OpenAI client libraries |
| 自有 orchestration / 工具 / 审批 / 状态管理 | **Agents SDK** |
| 托管 workflow editor + ChatKit 部署 | Agent Builder |

### 关键概念

| 概念 | 说明 |
|---|---|
| **Agent** | 配置了 instructions、model、tools 的执行单元 |
| **Handoffs** | 根据任务上下文将控制权转移给 specialist agent |
| **Agents as tools** | Manager 保留控制权，specialist 作为有界工具调用 |
| **Guardrails** | 输入/输出/tool 三层校验，阻断风险内容 |
| **Human review (approvals)** | 高风险操作前暂停等待人工确认 |
| **Runner** | 执行 agent loop 的核心组件 |
| **Sandbox agents** | 基于容器的执行环境（文件、命令、包、端口、快照） |

### Agent loop 步骤

1. 用准备好的 input 调用当前 agent 的模型
2. 检查模型输出
3. 有 tool call → 执行并继续
4. handoff → 切换 agent 并继续
5. 有最终回答且无更多 tool work → 返回结果

### Guardrail 类型

| 类型 | 作用时机 | 作用范围 |
|---|---|---|
| Input guardrails | 主模型运行前 | 链中**第一个** agent |
| Output guardrails | 输出离开系统前 | 产生**最终输出**的 agent |
| Tool guardrails | function tool 调用前后 | 绑定到具体工具 |

### 对话状态策略

| 策略 | 状态位置 | 适用场景 |
|---|---|---|
| Manual replay | 应用程序 | 小型对话循环 |
| `session` | 存储 + SDK | 持久对话、可恢复 run |
| `conversationId` | Conversations API | 跨 worker/服务的共享状态 |
| `previous_response_id` | Responses API | 最轻量服务端管理 |

## API 示例

```python
from agents import Agent, Runner

# 最简 agent
agent = Agent(
    name="History tutor",
    instructions="You answer history questions clearly and concisely.",
    model="gpt-5.5",
)
result = await Runner.run(agent, "When did the Roman Empire fall?")
print(result.final_output)

# Handoffs 多专家
triage_agent = Agent(
    name="Homework triage",
    instructions="Route each homework question to the right specialist.",
    handoffs=[history_tutor, math_tutor],
)

# Input guardrail
@input_guardrail
async def math_guardrail(ctx, agent, input):
    result = await Runner.run(guardrail_agent, input, context=ctx.context)
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.is_math_homework,
    )
```

## 与 Claude 对应物

[[Subagent]] — Claude Code 的子 agent 机制；[[MCP-server]] — Claude 通过 MCP 扩展工具能力，对应 SDK 的 MCP integration。Claude 无直接等价的官方 Agents SDK，但 Anthropic 有 `claude-agent-sdk-python`（见 [[claude-agent-sdk-python-greet--github-anthropics]]）。

## 出现来源

- [[agents--openai-docs]]
- [[agents-quickstart--openai-docs]]
- [[agents-orchestration--openai-docs]]
- [[agents-guardrails--openai-docs]]
- [[agents-running-agents--openai-docs]]

## 相关

- [[OpenAI-Responses-API]] — SDK 底层调用此 API
- [[OpenAI-Function-Calling]] — `@function_tool` 装饰器封装
- [[MCP-server]] — 通过 MCP server 扩展外部能力
- [[Agentic-loop]] — Agent loop 概念
- [[Agent-team]] — 多 agent 协作模式
