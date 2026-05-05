---
name: OpenAI Chat Completions API
type: entity
vendor: OpenAI
aliases: ["Chat Completions", "/v1/chat/completions"]
created: 2026-05-05
---

# OpenAI Chat Completions API

OpenAI 的经典聊天接口，以 `messages` 数组为核心，是生态系统中最广泛兼容的 API；OpenAI 官方建议新应用改用 [[OpenAI-Responses-API]]。

## 关键属性

| 属性 | 值 |
|---|---|
| Vendor | OpenAI |
| REST 端点 | `POST /v1/chat/completions` |
| 主要用途 | 文本生成、多轮对话、工具调用（旧版） |
| 状态管理 | 无状态，客户端自行传入完整 messages 历史 |
| 兼容性 | 众多第三方平台（含 Gemini）提供兼容端点 |

## 核心功能

Chat Completions API 采用无状态设计：每次请求需传入完整的对话历史（`messages` 数组），服务端不保留上下文。

### 消息角色

- `system`：系统提示词（对应 Responses API 的 `developer`/`instructions`）
- `user`：用户输入
- `assistant`：模型输出

### 主要参数

| 参数 | 说明 |
|---|---|
| `model` | 模型名称（如 `gpt-4o`、`gpt-5.4`） |
| `messages` | 对话历史数组 |
| `temperature` | 随机性控制（0–2） |
| `max_tokens` | 最大输出 token 数 |
| `stream` | 是否流式输出 |
| `tools` | 工具定义数组（function calling） |
| `response_format` | 输出格式（json_schema 等） |

### 与 Responses API 的关系

OpenAI 文档明确：新应用推荐 Responses API（推理模型尤其受益）。Chat Completions 仍被支持，主要为向后兼容和生态系统互操作性保留。Gemini API 等提供 `openai` 兼容端点，接受 Chat Completions 格式的请求。

## API 示例

```python
from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"},
    ]
)
print(response.choices[0].message.content)
```

## 与 Claude 对应物

[[Messages-API]] — Claude 的消息接口，结构高度相似（也使用 messages 数组 + system 参数）。

## 出现来源

- [[text-generation--openai-docs]]
- [[openai--gemini-docs]]

## 相关

- [[OpenAI-Responses-API]] — 官方推荐的新版接口，取代 Chat Completions
- [[OpenAI-Function-Calling]] — Chat Completions 支持的工具调用机制
- [[Structured-outputs]] — 可通过 `response_format` 参数配置
