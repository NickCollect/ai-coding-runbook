---
name: 结构化输出指南
type: synthesis
created: 2026-05-05
sources:
  - 01_Raw/platform.claude.com/docs/en/build-with-claude/structured-outputs.md
  - 01_Raw/docs.openai.com/docs/guides/structured-outputs.md
  - 02_Wiki/Summaries/structured-outputs--bwc.md
  - 02_Wiki/Summaries/structured-outputs--openai-docs.md
  - 02_Wiki/Summaries/structured-output--gemini-docs.md
---

# 结构化输出指南

跨 Claude / OpenAI / Gemini 三家厂商的结构化 JSON 输出能力对比，包括 schema 保证等级、API 形态、最佳实践与常见坑。

---

## 1. Claude 结构化输出

### 能力概述

Claude 提供**两个互补功能**，可独立使用或组合：

1. **JSON outputs**（`output_config.format`）：通过 constrained decoding，强制响应遵循 JSON schema，保证输出可解析且符合 schema
2. **Strict tool use**（`strict: true`）：保证 tool name + input 的 schema 验证

底层均使用同一套 constrained decoding pipeline（grammar compilation），不依赖 prompt 约束，**硬保证**。

### API 形态

```json
{
  "model": "claude-opus-4-7",
  "max_tokens": 1024,
  "messages": [...],
  "output_config": {
    "format": {
      "type": "json_schema",
      "schema": {
        "type": "object",
        "properties": {
          "name": {"type": "string"},
          "email": {"type": "string"},
          "priority": {"type": "string", "enum": ["low", "medium", "high"]}
        },
        "required": ["name", "email", "priority"],
        "additionalProperties": false
      }
    }
  }
}
```

Strict tool use：

```json
{
  "tools": [{
    "name": "extract_info",
    "description": "...",
    "input_schema": { ... },
    "strict": true
  }]
}
```

### 支持模型（GA）

| 平台 | 支持模型 |
|------|----------|
| Claude API | Claude Mythos Preview、Opus 4.7、Opus 4.6、Sonnet 4.6、Sonnet 4.5、Opus 4.5、Haiku 4.5 |
| Amazon Bedrock | Opus 4.6、Sonnet 4.6、Sonnet 4.5、Opus 4.5、Haiku 4.5；Opus 4.7/Mythos 须通过 "Claude in Amazon Bedrock" Messages-API 端点 |
| Microsoft Foundry | Beta |
| Google Vertex AI | 不支持 Claude Mythos Preview；其他模型 not documented in detail |

### 迁移提示

旧 beta 参数（`output_format` + `structured-outputs-2025-11-13` header）仍可用于过渡期，新参数为 `output_config.format`，无需 beta header。

### 限制与注意事项

- **与 Citations 不兼容**：同一请求中若任意 user document 启用了 citations，再使用 `output_config.format` 会返回 400 错误（citations 需要 interleaved blocks，严格 JSON 禁止这种结构）
- **PHI 限制（HIPAA 场景）**：不要把 PHI 放入 JSON schema 的 property names、`enum`、`const`、`pattern` 字段—schema 单独缓存，不受完整 PHI 保护
- **ZDR 资格**：部分符合——prompts 和 outputs 不存储，仅 JSON schema 缓存用于 grammar compilation（最长 24 小时）

---

## 2. OpenAI 结构化输出

### 能力概述

OpenAI 提供三个层次：

1. **Structured Outputs（`json_schema` + `strict: true`）**：强保证，模型响应**一定**符合 schema，不允许额外字段
2. **JSON mode（`json_object`）**：只保证输出是合法 JSON，**不保证**符合任何 schema
3. **Function calling（`strict: true`）**：工具调用场景，函数参数 schema 强保证

> 建议：能用 Structured Outputs 就不用 JSON mode。

### API 形态

**Structured Outputs（json_schema 方式）**：

```python
text = {
    "format": {
        "type": "json_schema",
        "strict": True,
        "schema": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "age": {"type": "integer"}
            },
            "required": ["name", "age"],
            "additionalProperties": False
        }
    }
}
```

**JSON mode（json_object 方式）**：

```python
text = {
    "format": {
        "type": "json_object"
    }
}
```

**Function calling（strict mode）**：

```python
tools = [{
    "type": "function",
    "function": {
        "name": "get_user",
        "strict": True,
        "parameters": { ... }
    }
}]
```

### 支持模型

- Structured Outputs：**GPT-4o**（gpt-4o-2024-08-06）及以后所有前沿模型
- JSON mode：`gpt-3.5-turbo`、`gpt-4-*`、`gpt-4o-*` 均支持（更宽泛）

### Refusal 机制

使用 Structured Outputs 处理用户输入时，模型可能因安全原因拒绝。API 响应中会有 `refusal` 字段，需程序侧检查并处理。

---

## 3. Gemini 结构化输出

### 能力概述

通过两个参数联合配置，让模型输出严格符合 JSON schema 的响应：

- `response_mime_type: "application/json"`
- `response_json_schema: { ... }`（或 SDK 层直接传 Pydantic/Zod schema）

当启用后，模型**总是**返回符合 schema 的合法 JSON。

### API 形态

```python
from google import genai
from pydantic import BaseModel

class Recipe(BaseModel):
    name: str
    ingredients: list[str]
    steps: list[str]

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="给我一个番茄炒蛋的食谱",
    config={
        "response_mime_type": "application/json",
        "response_json_schema": Recipe.model_json_schema(),
    },
)
recipe = Recipe.model_validate_json(response.text)
```

### SDK Schema 辅助

| 语言 | 库 | 方法 |
|------|----|------|
| Python | Pydantic (`BaseModel`) | `MyModel.model_json_schema()` |
| JavaScript | Zod + `zod-to-json-schema` | `zodToJsonSchema(mySchema)` |

### Schema 支持范围

- 支持类型：`object`、`array`、`string`、`integer`、`number`、`boolean`
- 支持 optional fields、嵌套对象、递归结构（通过 `$defs`）
- 支持 `enum` 约束字符串值

---

## 4. 横向对比表

| 特性 | Claude | OpenAI (Structured Outputs) | OpenAI (JSON mode) | Gemini |
|------|--------|-----------------------------|--------------------|--------|
| **机制** | Constrained decoding | Constrained decoding | Prompt 约束（软保证） | Constrained decoding |
| **Schema 保证** | ✅ 硬保证 | ✅ 硬保证 | ❌ 仅保证合法 JSON | ✅ 硬保证 |
| **API 参数** | `output_config.format.type: "json_schema"` | `text.format.type: "json_schema"` | `text.format.type: "json_object"` | `response_mime_type: "application/json"` + `response_json_schema` |
| **`strict` 选项** | 无此字段（默认就是严格） | 需显式 `"strict": true` | 无 | 无 |
| **`required` 字段** | 显式在 schema 中声明 | strict 模式下**所有字段必须 required** | 无保证 | 可选字段支持 |
| **`additionalProperties`** | 推荐设为 `false` | strict 模式下**禁止 `true`** | 无保证 | 不适用（按 schema 严格） |
| **`enum` 支持** | ✅ | ✅ | 无保证 | ✅ |
| **Streaming 支持** | not documented in raw | not documented in raw | ✅ | not documented in raw |
| **支持 tool use + structured output 同时** | ✅（可组合） | ✅ | ✅ | ✅ |
| **Refusal / 拒绝机制** | 返回 stop_reason 异常 | `refusal` 字段 | 无 | not documented |
| **Schema 缓存/编译延迟** | 首次有轻微延迟，后续缓存 24h | 首次有轻微延迟（"schema 编译"） | 无 | not documented |
| **最低支持模型** | Haiku 4.5 + | GPT-4o（2024-08-06）+ | GPT-3.5-turbo+ | Gemini 系列 |

---

## 5. 旧版方式对比（无 native structured outputs 时）

Claude 在推出 `output_config.format` 之前，推荐的结构化输出做法是**用 tool use 伪造 schema**：

```python
# 旧方案（仍有效，但不如 native structured outputs 严格）
tools = [{
    "name": "output_result",
    "description": "Output the structured result",
    "input_schema": {
        "type": "object",
        "properties": { ... },
        "required": [...]
    }
}]
tool_choice = {"type": "tool", "name": "output_result"}
```

这种方式通过强制 Claude 调用特定 tool 来"隐式"返回 JSON，但底层不是 constrained decoding，偶有 schema 违反情况。**现在应优先使用 `output_config.format`**。

---

## 6. 最佳实践

### 通用

- **Schema 尽量简单**：嵌套层级越深，constrained decoding 计算成本越高，首次编译越慢
- **善用 `enum`**：把固定选项的字段改成 `enum`，而非 free-form string
- **`additionalProperties: false`**：防止模型输出未定义字段
- **全字段 `required`**（OpenAI strict 模式强制要求；Claude 建议也这样做）
- **SDK 原生 schema 帮助**：用 Pydantic（Python）或 Zod（JS）生成 schema，避免手写 JSON Schema 出错

### Claude 专用

- 若请求里有 citations（document blocks 且 citations 开启），**不能同时用** `output_config.format`
- PHI 场景：不要把 PHI 放进 schema 的 property names / enum / const / pattern
- Schema 会被单独缓存（24h），可以跨多次请求复用而无需重新编译

### OpenAI 专用

- JSON mode 必须在 prompt 里明确要求输出 JSON，否则模型可能产生额外文字前缀
- Structured Outputs 不需要在 prompt 里写格式要求，schema 本身已足够约束
- 首次用新 schema 时有延迟（编译），后续缓存

### Gemini 专用

- `response_mime_type: "application/json"` 必须搭配 `response_json_schema` 使用，否则输出 JSON 但不保证结构
- 可以与 structured output 模式同时使用 `generate_content` 的其他 config 参数（不像 Claude 有 citations 限制）

---

## 7. 常见失败模式与缓解

| 失败模式 | 原因 | 缓解方案 |
|----------|------|----------|
| 模型输出 `null` 而非合法值 | Schema 中字段未设为 `required` | 把所有必须字段加入 `required` 数组 |
| 模型拒绝输出（Claude）或 `refusal`（OpenAI） | 输入内容触发安全规则 | System prompt 里加说明"如果无法提取则返回空字符串/默认值" |
| Schema 过于复杂导致编译失败 | 递归/深嵌套 schema | 拆分 schema，先输出顶层结构，再逐步提取子结构 |
| Claude: 400 "Incompatible with citations" | `output_config.format` 与 citations 共存 | 要么关闭 citations，要么用 tool use 方式而非 JSON outputs |
| OpenAI JSON mode 输出不符合期望格式 | JSON mode 不保证 schema | 升级到 Structured Outputs（`json_schema`）或切换支持的模型 |
| Gemini schema 字段不被支持 | 使用了 `string` 以外的复杂 JSON Schema 关键字 | 仅使用已支持类型（object/array/string/integer/number/boolean/enum） |
| 首次调用延迟明显 | Schema 编译 | 预热（pre-warm）：先发一次请求触发编译；高频调用时延迟会消失 |

---

## 出现来源

- `01_Raw/platform.claude.com/docs/en/build-with-claude/structured-outputs.md`
- `01_Raw/docs.openai.com/docs/guides/structured-outputs.md`
- `02_Wiki/Summaries/structured-outputs--bwc.md`
- `02_Wiki/Summaries/structured-outputs--openai-docs.md`
- `02_Wiki/Summaries/structured-output--gemini-docs.md`
