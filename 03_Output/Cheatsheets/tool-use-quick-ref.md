---
type: cheatsheet
topic: tool-use
updated: 2026-05-05
---

# Tool Use / Function Calling Quick Reference

---

## Schema 格式差异

| 维度 | Claude | OpenAI | Gemini |
|---|---|---|---|
| **定义位置** | 顶层 `tools[]` | 顶层 `tools[]` | `tools[].functionDeclarations[]` |
| **参数字段名** | `input_schema` | `parameters` | `parameters` |
| **Schema 规范** | 标准 JSON Schema | 标准 JSON Schema | OpenAPI 子集（非完整 JSON Schema） |
| **strict 模式** | `"strict": true` per tool | `"strict": true` per tool | 不支持 |
| **工具名规则** | `^[a-zA-Z0-9_-]{1,64}$` | 同类似规则 | 同类似规则 |
| **arguments 格式（响应中）** | 对象 (`input` dict) | **JSON 字符串**（需 parse） | 字典 (`args` dict) |
| **工具调用位置（响应中）** | `content[].tool_use` | `output[].function_call` | `parts[n].function_call` |

### Claude schema 示例

```python
tools = [{
    "name": "get_weather",
    "description": "Get current weather for a city.",
    "input_schema": {
        "type": "object",
        "properties": {
            "location": {"type": "string"},
            "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
        },
        "required": ["location"]
    }
}]
```

### OpenAI schema 示例

```python
tools = [{
    "type": "function",
    "name": "get_weather",
    "description": "Get current weather for a city.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {"type": "string"},
            "units": {"type": "string", "enum": ["celsius", "fahrenheit"]}
        },
        "required": ["location", "units"],
        "additionalProperties": False
    },
    "strict": True
}]
```

### Gemini schema 示例

```python
from google.genai import types

tools = types.Tool(function_declarations=[{
    "name": "get_weather",
    "description": "Get current weather.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {"type": "string"},
            "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
        },
        "required": ["location"]
    }
}])
# 或：types.FunctionDeclaration.from_callable(my_python_func)  # 自动推断 schema
```

---

## tool_choice / toolConfig 语法

| 意图 | Claude | OpenAI | Gemini |
|---|---|---|---|
| **模型自行决定** | `{"type": "auto"}` | `"auto"` | `mode: AUTO` |
| **必须调用某个工具** | `{"type": "any"}` | `"required"` | `mode: ANY` |
| **强制调用指定工具** | `{"type": "tool", "name": "xxx"}` | `{"type": "function", "name": "xxx"}` | `mode: ANY` + `allowed_function_names: ["xxx"]` |
| **禁止工具调用** | `{"type": "none"}` | `"none"` | `mode: NONE` |
| **禁止并行** | `"disable_parallel_tool_use": true` | `"parallel_tool_calls": false` | not documented |

---

## 并行工具调用

| | Claude | OpenAI | Gemini |
|---|---|---|---|
| **默认行为** | ✅ 启用 | ✅ 启用 | ✅ 启用 |
| **响应格式** | 多个 `tool_use` blocks in `content[]` | 多个 `function_call` items in `output[]` | 多个 `functionCall` parts in `parts[]` |
| **结果回传** | **所有 tool_result 必须放同一条 user 消息** | 各 `function_call_output` 用 `call_id` 关联 | 各 `functionResponse` 用 `id` 关联，可乱序 |

**Claude 并行回传正确示例：**
```python
# ✅ 正确：所有结果合并进同一条 user 消息
messages.append({
    "role": "user",
    "content": [
        {"type": "tool_result", "tool_use_id": "tu_01", "content": "25°C"},
        {"type": "tool_result", "tool_use_id": "tu_02", "content": "10:30 AM"}
    ]
})
# ❌ 错误：分两条 user 消息 → Claude 会减少后续并行调用频率
```

---

## 返回 Tool Results

### Claude

```python
# tool_result 必须排在同一 user 消息的 text 之前
messages.append({
    "role": "user",
    "content": [
        {"type": "tool_result", "tool_use_id": "toolu_01", "content": "25°C"},
        # 错误时加 "is_error": True
    ]
})
```

### OpenAI

```python
# arguments 是 JSON 字符串，需先 parse
import json
tool_call = response.output[0]  # type: function_call
args = json.loads(tool_call.arguments)

messages.append({
    "type": "function_call_output",
    "call_id": tool_call.call_id,
    "output": json.dumps({"temperature": "25°C"})  # 错误：直接返回错误字符串
})
```

### Gemini

```python
function_call = response.candidates[0].content.parts[0].function_call
# function_call.name, function_call.args (dict), function_call.id (Gemini 3+)

contents.append(types.Content(
    role="user",
    parts=[types.Part.from_function_response(
        name=function_call.name,
        response={"result": "25°C"},
        id=function_call.id   # Gemini 3+ 必须带 id
    )]
))
```

---

## 关键差异速记

- **Claude**：`input_schema`（不是 `parameters`）；`is_error: true` 语义让模型自动重试；`stop_reason: "tool_use"` 检测
- **OpenAI**：`arguments` 是 JSON **字符串**，必须 `json.loads()`；支持 `strict: true` + `additionalProperties: false` 强格式
- **Gemini**：用 OpenAPI schema 子集（不是完整 JSON Schema）；`from_callable()` 自动推断；Gemini 3+ function call 带 `id`
- **最大工具数**：三家均建议 < 20；超量用 Claude Tool-search-tool-API / OpenAI `tool_search`（gpt-5.4+）/ Gemini 动态子集
