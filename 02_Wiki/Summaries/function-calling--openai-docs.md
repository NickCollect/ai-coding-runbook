---
type: summary
source: 01_Raw/docs.openai.com/docs/guides/function-calling.md
source_url: https://platform.openai.com/docs/guides/function-calling
title: "OpenAI — Function Calling（工具调用）"
summarized_at: 2026-05-05
entities_referenced: [Tool-use]
concepts_referenced: [Tool-use, Agentic-loop]
---

## 核心要点

Function calling（即 Tool calling）让模型通过 JSON schema 描述的接口与外部系统交互，实现数据获取和操作执行。

### 三个核心概念

- **Tools**：模型可调用的 function 声明（含 name、description、parameters JSON schema）
- **Tool calls**：模型决定调用某工具时生成的对象（含 id、name、arguments）
- **Tool call outputs**：开发者执行工具后返回给模型的结果

### 五步工作流

1. **定义工具**：传入 `tools` 数组
2. **模型决策**：模型决定是否调用、调用哪些工具
3. **执行工具**：在应用代码中执行（可并行）
4. **返回输出**：将 `tool_call_output` 发回模型
5. **生成响应**：模型整合工具输出返回最终答案

### 函数定义示例（JSON schema）

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

### 高级配置

- **`tool_choice`**：`"auto"`（默认）/ `"required"` / `"none"` / 指定工具名
- **`parallel_tool_calls`**：默认 `true`，设为 `false` 强制串行
- **`strict` mode**：强制 JSON schema 合规（类似 Structured Outputs）；所有 required 字段必须有值，不允许 additionalProperties
- **Namespaces**：用于区分来自不同来源的工具

### Tool search

工具很多时用 `tool_search` 按需动态加载，降低 context 消耗（需 `gpt-5.4` 及以上）。

### Custom tools（CFG grammars）

自定义工具支持 CFG（context-free grammar），适合需要自由文本的非结构化输出（如 shell 命令、Markdown 格式内容）。
