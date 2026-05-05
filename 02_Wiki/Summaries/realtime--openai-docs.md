---
type: summary
source: 01_Raw/docs.openai.com/docs/guides/realtime.md
source_url: https://platform.openai.com/docs/guides/realtime
title: "OpenAI — Realtime API"
summarized_at: 2026-05-05
entities_referenced: [Streaming-API]
concepts_referenced: []
---

## 核心要点

Realtime API 提供低延迟的语音到语音（speech-to-speech）和多模态交互能力，适合构建语音 AI 应用。

### 支持的连接方式

- **WebRTC**：浏览器/移动端原生低延迟音频（推荐 client-side 场景）
- **WebSocket**：服务端应用（Python/Node.js 等）
- **SIP**：传统电话系统集成（仅限 `gpt-realtime-1.5`）

### 可用模型

| 模型 | 说明 |
|---|---|
| `gpt-realtime-1.5` | 最佳语音模型，支持 WebRTC/WebSocket/SIP |
| `gpt-realtime-mini` | 低成本语音模型，仅 WebRTC/WebSocket |

### Session 创建示例（JavaScript）

```javascript
body: JSON.stringify({
  session: {
    type: "realtime",
    model: "gpt-realtime",
    audio: { output: { voice: "marin" } },
  },
})
```

### Beta → GA 事件名变更（迁移指南）

旧 Beta 版本事件名已改变（如 `output_item.done` → `output_item.completed`）。GA 版本事件命名更一致，迁移时需对照变更列表更新事件处理代码。

### 推荐入门路径

- 参见 Voice agents quickstart（文档另有专项）
- WebRTC 连接适合前端快速集成
- SIP 连接适合企业电话系统
