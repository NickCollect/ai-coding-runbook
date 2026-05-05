---
name: OpenAI Realtime API
type: entity
vendor: OpenAI
aliases: ["Realtime API", "gpt-realtime", "Voice API"]
created: 2026-05-05
---

# OpenAI Realtime API

OpenAI 的低延迟实时音视频交互接口，支持 speech-to-speech 对话；提供 WebRTC（客户端）、WebSocket（服务端）和 SIP（电话系统）三种连接方式。

## 关键属性

| 属性 | 值 |
|---|---|
| Vendor | OpenAI |
| 连接协议 | WebRTC / WebSocket / SIP |
| 主要用途 | 实时语音对话、多模态交互、电话系统集成 |
| 相关模型 | `gpt-realtime-1.5`（最佳）、`gpt-realtime-mini`（低成本） |

## 核心功能

### 三种连接方式对比

| 方式 | 适用场景 | 说明 |
|---|---|---|
| **WebRTC** | 浏览器 / 移动端 | 原生低延迟音频，推荐 client-side |
| **WebSocket** | 服务端（Python/Node.js） | 适合后端应用 |
| **SIP** | 传统电话系统 | 仅 `gpt-realtime-1.5` 支持 |

### 可用模型

| 模型 | 特点 | 支持协议 |
|---|---|---|
| `gpt-realtime-1.5` | 最佳语音质量 | WebRTC / WebSocket / SIP |
| `gpt-realtime-mini` | 低成本 | WebRTC / WebSocket |

### 迁移注意事项

Beta → GA 版本事件名已更改（如 `output_item.done` → `output_item.completed`），迁移时需对照变更列表更新事件处理代码。

## API 示例

```javascript
// Session 创建（WebRTC）
const body = JSON.stringify({
  session: {
    type: "realtime",
    model: "gpt-realtime",
    audio: { output: { voice: "marin" } },
  },
});
```

```python
# Python SDK 实时连接
from openai import OpenAI

client = OpenAI()
# 使用 client.beta.realtime 或 client.realtime（取决于 SDK 版本）
# 详见 openai-python-realtime-api 文档
```

## 与 Claude 对应物

Claude 目前无直接等价的实时语音 API。[[Gemini-Live-API]] 是 Google 的对应能力，也是 WebSocket 架构的实时多模态接口。

## 出现来源

- [[realtime--openai-docs]]
- [[openai-node-realtime-api--github-openai]]
- [[openai-python-realtime-api--github-openai]]

## 相关

- [[Gemini-Live-API]] — Google 的等价实时多模态接口
- [[Streaming-API]] — 标准流式（非实时）接口
