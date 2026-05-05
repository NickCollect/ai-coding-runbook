---
name: OpenAI Function Calling
type: entity
vendor: OpenAI
aliases: ["Function Calling", "Tool calling", "tools", "function_tool"]
created: 2026-05-05
---

# OpenAI Function Calling

让 OpenAI 模型通过 JSON Schema 描述的接口与外部系统交互的机制；支持并行调用、strict 模式强制 schema 合规，以及动态 tool search。

## 关键属性

| 属性 | 值 |
|---|---|
| Vendor | OpenAI |
| 参数名 | `tools`（数组）、`tool_choice` |
| strict 模式 | 支持，强制 JSON schema 合规 |
| 并行调用 | 默认开启（`parallel_tool_calls: true`） |
| Tool search | 支持（需 `gpt-5.4` 及以上） |

## 核心功能

### 三个核心概念

- **Tools**：模型可调用的 function 声明（含 name、description、parameters JSON schema）
- **Tool calls**：模型决定调用某工具时生成的对象（含 id、name、arguments）
- **Tool call outputs**：开发者执行工具后返回给模型的结果

### 五步工作流

1. **定义工具**：传入 `tools` 数组
2. **模型决策**：模型决定是否调用、调用哪些工具
3. **执行工具**：在应用代码中执行（可并行）
4. **返回输出**：将 `tool_call_output` 发回模型
5. **生成响应**：模型整合工具输出，返回最终答案

### 高级配置

| 参数 | 说明 |
|---|---|
| `tool_choice` | `"auto"`（默认）/ `"required"` / `"none"` / 指定工具名 |
| `parallel_tool_calls` | 默认 `true`，设为 `false` 强制串行 |
| `strict: true` | 强制 JSON schema 合规；所有 required 字段必须有值，禁止 additionalProperties |
| `tool_search` | 工具很多时按需动态加载，降低 context 消耗（需 gpt-5.4+） |

### Custom tools（CFG grammars）

自定义工具支持 CFG（context-free grammar），适合需要自由文本的非结构化输出（如 shell 命令、Markdown 格式内容）。

## API 示例

```json
{
  "type": "function",
  "name": "get_weather",
  "description": "Retrieves current weather for the given location.",
  "parameters": {
    "type": "object",
    "properties": {
      "location": {"type": "string"},
      "units": {"type": "string", "enum": ["celsius", "fahrenheit"]}
    },
    "required": ["location", "units"],
    "additionalProperties": false
  },
  "strict": true
}
```

```python
response = client.responses.create(
    model="gpt-5.4",
    tools=[weather_tool],
    input=[{"role": "user", "content": "What's the weather in Tokyo?"}],
)
```

## 与 Claude 对应物

[[Tool-use]] — Anthropic 的工具调用机制，概念高度相似（JSON schema 定义、多工具并行、tool_choice 等价配置）。

## 出现来源

- [[function-calling--openai-docs]]

## 相关

- [[OpenAI-Responses-API]] — function calling 通过 Responses API 使用
- [[OpenAI-Agents-SDK]] — SDK 层的 `@function_tool` 装饰器封装此机制
- [[Structured-outputs]] — strict mode 与 Structured Outputs 共享相同约束
- [[Tool-use]] — Claude 对应物
