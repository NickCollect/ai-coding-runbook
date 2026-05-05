---
name: Tool Use / Function Calling 跨厂商对比
type: comparison
created: 2026-05-05
vendors: [Claude, OpenAI, Gemini]
sources:
  - 01_Raw/docs.openai.com/docs/guides/function-calling.md
  - 01_Raw/ai.google.dev/gemini-api/docs/function-calling.md
  - 01_Raw/platform.claude.com/docs/en/agents-and-tools/tool-use/overview.md
  - 01_Raw/platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works.md
  - 01_Raw/platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls.md
  - 01_Raw/platform.claude.com/docs/en/agents-and-tools/tool-use/parallel-tool-use.md
  - 01_Raw/platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools.md
  - 01_Raw/platform.claude.com/docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming.md
---

# Tool Use / Function Calling 跨厂商对比

三家主流 AI 厂商（Anthropic Claude、OpenAI、Google Gemini）都支持 tool use / function calling，但 API 设计有显著差异。本文从机制、控制粒度、并行、streaming、响应结构等维度横向对比，并给出选型建议。

---

## 一、Schema 定义机制

### Claude

工具定义放在顶层 `tools` 数组，每个工具的结构：

```json
{
  "name": "get_weather",
  "description": "获取指定城市的当前天气...",
  "input_schema": {
    "type": "object",
    "properties": {
      "location": {"type": "string"},
      "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
    },
    "required": ["location"]
  }
}
```

- `input_schema` 是标准 JSON Schema 对象。
- 可选字段：`input_examples`（示例输入）、`strict`（强制 schema 合规）、`cache_control`（缓存控制）、`defer_loading`（延迟加载）。
- 工具名正则：`^[a-zA-Z0-9_-]{1,64}$`。
- API 会自动在 system prompt 里注入工具定义（Opus 4.x/Sonnet 4.x 约多 346 tokens）。

### OpenAI（Responses API）

工具定义放在 `tools` 数组，类型为 `"function"`：

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

- `parameters` 是 JSON Schema 对象；`strict: true` 时强制 schema 合规（类似 Structured Outputs），要求所有字段 `required` 且 `additionalProperties: false`。
- 额外支持 **custom tools**（自由文本输入，可配置 CFG grammar 约束输出格式）。
- 支持 **namespace** 分组，将相关工具聚合为一个命名空间对象。
- 工具定义本质上被注入 system message，计入输入 token。

### Gemini

工具定义放在 `tools[].functionDeclarations` 数组：

```python
# Python SDK
tools = types.Tool(function_declarations=[{
    "name": "set_light_values",
    "description": "Sets the brightness and color temperature of a light.",
    "parameters": {
        "type": "object",
        "properties": {
            "brightness": {"type": "integer"},
            "color_temp": {"type": "string", "enum": ["daylight", "cool", "warm"]}
        },
        "required": ["brightness", "color_temp"]
    }
}])
```

- `parameters` 使用 **OpenAPI 规范的子集**（非完整 JSON Schema）。
- Python SDK 支持 `types.FunctionDeclaration.from_callable()`，可直接从 Python 函数推断 schema。
- 工具定义和参数说明计入输入 token 限制。
- 注意：仅支持部分 OpenAPI schema 特性（不是完整 JSON Schema）。

---

## 二、Tool Choice（调用模式控制）

### Claude

通过顶层 `tool_choice` 对象控制：

| 值 | 含义 |
|---|---|
| `{"type": "auto"}` | 默认。Claude 自行决定是否调用工具 |
| `{"type": "any"}` | 必须调用某个工具（不指定具体哪个） |
| `{"type": "tool", "name": "xxx"}` | 强制调用指定工具 |
| `{"type": "none"}` | 禁止工具调用（等价于不传 `tools`） |

禁止并行：在 `tool_choice` 对象里加 `"disable_parallel_tool_use": true`。

### OpenAI

通过顶层 `tool_choice` 参数控制：

| 值 | 含义 |
|---|---|
| `"auto"` | 默认。模型自行决定 |
| `"required"` | 必须调用一个或多个工具 |
| `"none"` | 禁止工具调用 |
| `{"type": "function", "name": "xxx"}` | 强制调用指定工具 |
| `{"type": "allowed_tools", "mode": "auto", "tools": [...]}` | 限定可调用工具子集（用于缓存优化） |

禁止并行：`"parallel_tool_calls": false`。

### Gemini

通过 `tool_config.function_calling_config.mode` 控制：

| 值 | 含义 |
|---|---|
| `AUTO` | 默认（仅有 function_declarations 时）。模型自行决定 |
| `VALIDATED` | 默认（启用内置工具或 structured outputs 时）。只能生成函数调用或自然语言，格式更严格 |
| `ANY` | 强制调用（可配合 `allowed_function_names` 限定范围） |
| `NONE` | 禁止工具调用 |

---

## 三、并行工具调用

### Claude

默认启用，模型可能在一次响应里返回**多个 `tool_use` 块**。

- 响应里的 `content` 数组包含多个 `{type: "tool_use", id, name, input}` 块。
- **关键规则**：所有 `tool_result` 必须合并进**同一条 user 消息**，顺序任意。分成多条 user 消息会导致 Claude 减少后续的并行调用频率。

```json
// 正确：并行结果放同一条消息
{"role": "user", "content": [
  {"type": "tool_result", "tool_use_id": "tu_01", "content": "25°C"},
  {"type": "tool_result", "tool_use_id": "tu_02", "content": "10:30 AM"}
]}
```

### OpenAI

默认启用，模型可能在 `output` 数组里返回多个 `function_call` 对象。

- 每个 `function_call` 有唯一 `call_id`。
- 提交结果时，每个 `function_call_output` 通过 `call_id` 关联。
- 内置工具（built-in tools）不支持并行函数调用。

### Gemini

支持**并行函数调用**（Parallel Function Calling）。

- 模型在单次响应里返回多个 `functionCall` 对象（每个有唯一 `id`）。
- Gemini 3 系列起，每次 `functionCall` 必返回唯一 `id`；`functionResponse` 里需带上对应 `id` 才能正确关联。
- 可乱序返回 `functionResponse`，API 用 `id` 匹配。

---

## 四、Streaming 下的工具调用

### Claude

支持。通过 `"stream": true` 开启，工具调用相关 SSE 事件：

1. `content_block_start`（`type: "tool_use"`）：出现时 `input: {}` 占位。
2. `content_block_delta`（`type: "input_json_delta"`）：每条 delta 携带 `partial_json` 片段，需串接。
3. `content_block_stop`：在此解析完整 JSON。

**Fine-grained tool streaming**（精细流式）：在工具定义上设 `"eager_input_streaming": true`，参数不等 JSON 验证通过就实时输出，延迟更低但可能收到不完整 JSON（若遇 `max_tokens`），调用方需自行处理。

### OpenAI

支持。设 `"stream": true`，工具调用相关事件：

| 事件 | 含义 |
|---|---|
| `response.output_item.added` | 新工具调用出现，含 `name`、`arguments`（初始）、`id` |
| `response.function_call_arguments.delta` | 参数片段 delta |
| `response.function_call_arguments.done` | 完整工具调用完毕 |

### Gemini

raw 文档中**未明确说明** streaming 下工具调用的具体事件格式，not documented in the reviewed source。

---

## 五、Max Tools 限制

| | Claude | OpenAI | Gemini |
|---|---|---|---|
| 硬性上限 | 未文档化 | 未文档化 | 未文档化 |
| 最佳实践上限 | 首次请求 < 20 | 初始 < 20（软建议） | 建议 10–20 |
| 超量处理方案 | `Tool-search-tool-API`（延迟加载） | `tool_search`（gpt-5.4+ 支持） | 动态按上下文选择工具子集 |

---

## 六、响应结构

### Claude

- `stop_reason: "tool_use"`，响应 `content` 数组含一或多个 `tool_use` 块。

```json
{
  "stop_reason": "tool_use",
  "content": [
    {"type": "text", "text": "I'll check the weather for you."},
    {
      "type": "tool_use",
      "id": "toolu_01AbCd",
      "name": "get_weather",
      "input": {"location": "Paris", "unit": "celsius"}
    }
  ]
}
```

回传工具结果时，在新 user 消息的 content 数组里用 `tool_result` 块，且 **`tool_result` 必须排在 text 之前**：

```json
{"role": "user", "content": [
  {"type": "tool_result", "tool_use_id": "toolu_01AbCd", "content": "25°C"},
  {"type": "text", "text": "Anything else?"}
]}
```

### OpenAI（Responses API）

工具调用出现在 `output` 数组：

```json
{
  "output": [
    {
      "type": "function_call",
      "call_id": "call_abc123",
      "name": "get_weather",
      "arguments": "{\"location\": \"Paris\", \"units\": \"celsius\"}"
    }
  ]
}
```

回传时用 `function_call_output` item（`call_id` 关联）。注意：`arguments` 是 JSON **字符串**，需自行 parse。

### Gemini

工具调用出现在 `response.candidates[0].content.parts` 数组中，每个 part 的 `function_call` 字段：

```python
function_call = response.candidates[0].content.parts[0].function_call
# function_call.id, function_call.name, function_call.args (dict)
```

回传时创建 `functionResponse` part（含 `name`、`response`、`id`）放入 `user` 角色的 `contents`。

---

## 七、错误处理

### Claude

在 `tool_result` 里设 `"is_error": true` + 错误描述：

```json
{
  "type": "tool_result",
  "tool_use_id": "toolu_01AbCd",
  "content": "ConnectionError: weather service unavailable (HTTP 500)",
  "is_error": true
}
```

- 描述性错误信息（如"Rate limit exceeded. Retry after 60 seconds."）能让 Claude 决定重试策略。
- 参数无效/缺失时，Claude 会自动重试 2–3 次后再向用户道歉。
- 开启 `strict: true` 可从根源消除格式错误的工具调用。

### OpenAI

将错误字符串放入 `function_call_output` 的 `output` 字段，模型自行解读。没有专用的 `is_error` 标志，格式自定（JSON、纯文本均可）。

### Gemini

raw 文档建议在函数内部实现健壮的错误处理，返回包含错误信息的响应字典。无专用 `is_error` 标志。建议检查响应中的 `finishReason` 字段以处理模型无法生成有效工具调用的情况。

---

## 八、决策矩阵（汇总对比）

| 维度 | Claude | OpenAI | Gemini |
|---|---|---|---|
| **schema 格式** | 标准 JSON Schema（`input_schema`） | 标准 JSON Schema（`parameters`） | OpenAPI schema 子集（`functionDeclarations`） |
| **工具定义位置** | 顶层 `tools` 数组 | 顶层 `tools` 数组 | `tools[].functionDeclarations` |
| **tool_choice: auto** | `{"type": "auto"}` | `"auto"` | `mode: AUTO` |
| **tool_choice: force any** | `{"type": "any"}` | `"required"` | `mode: ANY` |
| **tool_choice: force specific** | `{"type": "tool", "name": "..."}` | `{"type": "function", "name": "..."}` | `mode: ANY` + `allowed_function_names: [...]` |
| **tool_choice: none** | `{"type": "none"}` | `"none"` | `mode: NONE` |
| **禁止并行** | `disable_parallel_tool_use: true` | `parallel_tool_calls: false` | not documented |
| **并行支持** | ✅ 多 `tool_use` 块 | ✅ 多 `function_call` items | ✅ 多 `functionCall` parts |
| **Streaming** | ✅ SSE delta events（含 eager mode） | ✅ SSE delta events | ⚠️ not documented in source |
| **响应中的工具调用位置** | `content[].tool_use` | `output[].function_call` | `parts[n].function_call` |
| **结果回传方式** | user 消息的 `tool_result` block | `function_call_output` item | user turn 的 `functionResponse` part |
| **arguments 格式** | 对象（`input`） | JSON 字符串（需 parse） | 字典（`args`） |
| **error 信号** | `is_error: true` flag | 无专用标志，返回错误字符串 | 无专用标志，返回错误字典 |
| **strict 模式** | `strict: true` per tool | `strict: true` per tool | 不支持（仅 ANY 模式近似） |
| **最大工具数** | < 20（最佳实践） | < 20（软建议），超量用 tool_search | 10–20（建议） |
| **超量工具方案** | Tool-search-tool-API | `tool_search`（gpt-5.4+） | 动态子集选择 |

---

## 九、选型建议

**选 Claude 当：**
- 需要 `is_error` 语义让模型自动重试；
- 使用 extended thinking 的场景（OpenAI/Gemini 对应能力有限制）；
- 需要精细 streaming（`eager_input_streaming`）处理长参数；
- 工具集有 Anthropic 预置 schema（Bash、Text Editor、Computer Use），可获得更可靠调用。

**选 OpenAI 当：**
- 需要 `strict: true` + `additionalProperties: false` 的强 schema 合规；
- 工具数量极多（支持 `tool_search` 动态加载，gpt-5.4+）；
- 需要 custom tools + CFG grammar 约束非结构化输出；
- Namespace 分组对复杂系统有组织优势。

**选 Gemini 当：**
- 从 Python 函数自动推断 schema（`from_callable`）节省编写 schema 的成本；
- 与 Google 生态（Search、Code Execution、Live API）深度结合；
- 需要 **compositional / sequential function calling**（Gemini 原生支持多轮链式调用）；
- 利用 Auto Function Calling（Python SDK 自动执行函数并循环）降低 agentic 样板代码。
