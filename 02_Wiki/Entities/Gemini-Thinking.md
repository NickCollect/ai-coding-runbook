---
name: Gemini Thinking
type: entity
vendor: Gemini
aliases: ["Gemini Thinking", "thinking mode", "ThinkingConfig", "thought summary"]
created: 2026-05-05
---

# Gemini Thinking

Gemini 2.5 和 3 系列模型内置的内部推理过程，在生成最终答案前进行多步骤思考；可控制思考预算级别（low / medium / high），并可选择性获取思考摘要。

## 关键属性

| 属性 | 值 |
|---|---|
| Vendor | Google / Gemini |
| 支持模型 | Gemini 3 系列（`gemini-3-flash-preview` 等）、Gemini 2.5 系列（`gemini-2.5-pro`、`gemini-2.5-flash`） |
| 默认状态 | 默认启用（thinking-capable 模型） |
| 思考预算控制 | `thinking_level`：`"low"` / `"medium"` / `"high"` |
| 计费 | 思考 token 计入 output token 计费 |

## 核心功能

### 适用场景

- 编程（复杂算法、debug）
- 高级数学
- 数据分析
- 需要多步规划的任务

### 思考预算控制

通过 `ThinkingConfig` 调节推理深度，成本和延迟随预算增加而增加：

```python
from google.genai import types

config = types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(thinking_level="low")  # low / medium / high
)
```

### 获取思考摘要

设置 `include_thoughts=True` 可接收模型的内部推理摘要（非原始思考，是摘要版本）：

```python
config = types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(include_thoughts=True)
)

for part in response.candidates[0].content.parts:
    if part.thought:
        print("思考摘要:", part.text)
    else:
        print("最终答案:", part.text)
```

### 关键注意事项

- 思考预算影响**原始思考内容**，**不**影响思考摘要
- `include_thoughts` 返回的是摘要版本，而非完整推理链
- Gemini 3 模型的每个 `functionCall` 返回唯一 `id`，需在 `functionResponse` 中带回该 `id`

## 与 Claude 对应物

[[Extended-thinking]] — Claude 的扩展思考模式，功能定位相同：在输出答案前进行内部推理，可控制思考 token 预算（`thinking.budget_tokens`），并可获取思考内容（`thinking` block）。

## 出现来源

- [[thinking--gemini-docs]]

## 相关

- [[Gemini-API]] — 通过标准 generateContent 调用，只需换用 thinking-capable 模型
- [[Extended-thinking]] — Claude 对应物
