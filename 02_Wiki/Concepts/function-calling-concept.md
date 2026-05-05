---
name: Function Calling
type: concept
aliases: [Tool Calling, Tool Use, Function Use, Structured Tool Invocation]
vendors: [Claude, OpenAI, Gemini]
created: 2026-05-05
---

# Function Calling（函数调用）

让 LLM 通过输出结构化 JSON 来触发外部函数/工具调用的机制，实现模型与代码、API、数据库的标准化交互。是 agentic 系统的核心能力之一。

## 核心机制

Function calling 的本质：**将"决定调用哪个工具、传什么参数"的问题转化为"生成结构化 JSON"的文本生成问题**。

**五步工作流**：
1. **定义工具**：将函数描述为 JSON schema（name、description、parameters）
2. **模型决策**：模型分析用户意图，决定是否调用工具及调用哪个
3. **生成调用**：输出 `tool_use` 内容块（含 tool name + JSON arguments）
4. **执行工具**：开发者代码在自己的环境中执行（可并行多个调用）
5. **返回结果**：将 `tool_result` 发回模型，模型整合结果生成最终答案

**工具调用 vs 普通生成**：工具调用时，模型不直接回答用户，而是生成中间调用；执行结果回传后，模型再基于实际数据回答。这实现了"从知识生成"到"从数据生成"的转变。

**并行工具调用**：模型可在一次响应中输出多个独立工具调用，让应用层并行执行，提高效率。

## 跨厂商实现

**Claude**：
- `tools` 数组（JSON schema 格式） + `tool_use` / `tool_result` content block 类型
- `tool_choice: "auto"/"any"/"none"/{name}` 控制调用策略
- 与 Extended Thinking 结合：Interleaved thinking 让模型在工具调用之间推理
- MCP（Model Context Protocol）：标准化的远程工具注册协议

**OpenAI**：
- `tools` 数组 + `function` 类型 + `tool_calls` / `tool_call_outputs`
- `tool_choice: "auto"/"required"/"none"/指定工具名`
- `parallel_tool_calls: true/false`（默认 true）
- `strict: true`：强制 JSON schema 严格合规（类似 Structured Outputs）
- Tool Search：工具太多时动态检索相关工具，降低 context 消耗（gpt-5.4+）

**Gemini**：
- `tools` 数组 + `function_declarations`；响应含 `functionCall` / `functionResponse`
- 支持 `tool_config.function_calling_mode: ANY/AUTO/NONE`
- Code Execution tool、Google Search tool 为内置工具

## 关键参数 / API 表面

| 参数 | 说明 |
|---|---|
| `tools` | 工具定义数组（JSON schema） |
| `tool_choice` | 调用策略：auto/required/none/指定 |
| `parallel_tool_calls` (OpenAI) | 是否允许并行调用 |
| `strict` (OpenAI) | 强制参数 schema 合规 |
| `input_schema` (Claude) | 工具参数的 JSON schema 定义 |

**最简工具定义（Claude 格式）**：
```json
{
  "name": "get_weather",
  "description": "获取指定城市的当前天气",
  "input_schema": {
    "type": "object",
    "properties": {
      "city": {"type": "string", "description": "城市名称"}
    },
    "required": ["city"]
  }
}
```

## 使用场景

**适用**：
- 实时数据获取（天气、股价、搜索）
- 数据库读写操作
- 代码执行（计算、文件操作）
- 外部 API 集成
- 多步骤任务自动化（agentic loop）

**注意**：
- 工具 description 质量直接影响模型是否正确选择工具
- 工具过多会占用大量 context token（考虑 Tool Search 动态加载）
- 工具执行发生在开发者代码中，模型无法直接控制执行环境

## 相关

- [[Tool-use]] — Claude tool use concept + 整体工作流
- [[Agentic-loop]] — function calling 驱动的 agent 循环
- [[MCP-server]] — 远程工具的标准协议
- [[Structured-outputs]] — function calling 的参数输出是结构化输出的应用
- [[extended-thinking-concept]] — Interleaved thinking 与 tool call 结合

## 出现来源

- [[function-calling--openai-docs]]
- [[function-calling--gemini-docs]]
- [[Tool-use]]
