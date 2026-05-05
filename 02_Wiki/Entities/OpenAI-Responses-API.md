---
name: OpenAI Responses API
type: entity
vendor: OpenAI
aliases: ["Responses API", "client.responses"]
created: 2026-05-05
---

# OpenAI Responses API

OpenAI 推荐用于新应用的文本生成接口，取代旧版 Chat Completions API；支持有状态对话、工具调用、流式输出，并是推理模型的首选接入点。

## 关键属性

| 属性 | 值 |
|---|---|
| Vendor | OpenAI |
| SDK 方法 | `client.responses.create()` |
| 主要用途 | 文本生成、多轮对话、工具调用 |
| 相关模型 | gpt-5.5、gpt-5.4、gpt-5.4-mini 等所有前沿模型 |
| 数据保留 | 默认 30 天（可用 `store: false` 关闭） |

## 核心功能

OpenAI 文档明确建议新应用使用 Responses API 而非旧版 Chat Completions API，推理模型（reasoning models）尤其受益。

### 消息角色

- `developer`：高优先级指令（应用开发者定义）
- `user`：终端用户输入
- `assistant`：模型生成内容
- `instructions` 参数：当前请求级系统指令，优先级高于 `developer` 消息

### 三种对话状态管理方式

| 方式 | 机制 | 特点 |
|---|---|---|
| 手动传入历史 | 每次把 messages 数组完整传入 | 客户端管理，灵活 |
| `previous_response_id` | 传上一次 response 的 id | 最轻量的服务端管理 |
| Conversations API | 创建持久 `conversation` 对象 | 无 30 天 TTL，跨 session/设备复用 |

### Reusable prompts

通过 dashboard 创建含变量占位符的模板，API 中用 `prompt` 参数（`id`、`version`、`variables`）引用。

## API 示例

```python
# 基本调用
response = client.responses.create(
    model="gpt-4o-mini",
    input=[{"role": "user", "content": "Hello"}],
)

# 使用 previous_response_id 链接上下文
second_response = client.responses.create(
    model="gpt-4o-mini",
    previous_response_id=response.id,
    input=[{"role": "user", "content": "Explain why."}],
)

# 使用 Conversations API
conversation = openai.conversations.create()
response = openai.responses.create(
    model="gpt-4.1",
    input=[{"role": "user", "content": "What are the 5 Ds of dodgeball?"}],
    conversation="conv_689667905b048191b4740501625afd940c7533ace33a2dab"
)
```

## 与 Claude 对应物

[[Messages-API]] — Anthropic 的核心消息接口，类似 Responses API 的定位；Claude 的 `messages.create()` 对应 OpenAI 的 `responses.create()`。

## 出现来源

- [[conversation-state--openai-docs]]
- [[text-generation--openai-docs]]
- [[openai-node-responses-api--github-openai]]
- [[openai-python-responses-api--github-openai]]

## 相关

- [[OpenAI-Chat-Completions-API]] — 被 Responses API 取代的旧版接口
- [[OpenAI-Function-Calling]] — 在 Responses API 内使用工具调用
- [[OpenAI-Agents-SDK]] — 在 SDK 层封装 Responses API 实现 agentic loop
- [[Streaming-API]] — Responses API 原生支持流式输出
