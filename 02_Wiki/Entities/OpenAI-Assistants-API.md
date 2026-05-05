---
name: OpenAI Assistants API
type: entity
vendor: OpenAI
aliases: ["Assistants API", "Thread-based API"]
created: 2026-05-05
---

# OpenAI Assistants API

OpenAI 基于 Thread（线程）的有状态助手接口，服务端自动管理对话历史；随着 [[OpenAI-Responses-API]] 的推出，已被定位为 legacy 方案。

## 关键属性

| 属性 | 值 |
|---|---|
| Vendor | OpenAI |
| 核心抽象 | Assistant + Thread + Run |
| 主要用途 | 有状态多轮对话、内置工具（File Search、Code Interpreter） |
| 状态管理 | 服务端自动管理（Thread 存储完整历史） |
| 定位 | *待确认*：是否已标注为 legacy |

## 核心功能

Assistants API 引入三个核心对象：

| 对象 | 说明 |
|---|---|
| **Assistant** | 配置了 instructions、model、tools 的 AI 助手实体 |
| **Thread** | 持久对话线程，服务端存储完整消息历史 |
| **Run** | 在特定 Thread 上执行 Assistant 的一次运行 |

### 内置工具

- **Code Interpreter**：沙箱化 Python 执行环境（类似 [[Gemini-Code-Execution]]）
- **File Search**：基于向量存储的文件检索
- **Function calling**：自定义工具调用

### 与 Responses API 的对比

| 维度 | Assistants API | Responses API |
|---|---|---|
| 状态管理 | 服务端 Thread，自动维护 | 手动 / `previous_response_id` / Conversations |
| 工具内置 | Code Interpreter、File Search 内置 | 工具按需接入 |
| 适用场景 | 重度有状态对话 | 更灵活的新应用 |
| OpenAI 推荐 | *待确认*：是否仍推荐 | ✅ 新应用首选 |

## API 示例

```python
# 创建 Assistant
assistant = client.beta.assistants.create(
    name="Math Tutor",
    instructions="You are a personal math tutor.",
    model="gpt-4o",
    tools=[{"type": "code_interpreter"}],
)

# 创建 Thread 并运行
thread = client.beta.threads.create()
client.beta.threads.messages.create(thread_id=thread.id, role="user", content="Solve x^2=4")
run = client.beta.threads.runs.create(thread_id=thread.id, assistant_id=assistant.id)
```

## 与 Claude 对应物

Claude 没有直接等价的 thread-based API。最接近的是通过 [[Messages-API]] + 手动历史管理，或借助 [[OpenAI-Agents-SDK]] 同类的 session 机制。

## 出现来源

*待确认*：当前 raw 文件中无专属 Assistants API 文档，本条目信息部分来自 Responses API 相关文档的对比语境。

## 相关

- [[OpenAI-Responses-API]] — 推荐的新版有状态接口
- [[OpenAI-Agents-SDK]] — 更高层的 agent 编排框架
