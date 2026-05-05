---
name: Gemini Live API
type: entity
vendor: Gemini
aliases: ["Live API", "Gemini Live", "gemini-3.1-flash-live-preview"]
created: 2026-05-05
---

# Gemini Live API

Gemini 的低延迟实时语音和视觉交互接口，基于 WebSocket 持久连接实现双向流式传输；支持音频、视频帧和文本的同时处理，提供自然打断、工具调用和多语言对话能力。

## 关键属性

| 属性 | 值 |
|---|---|
| Vendor | Google / Gemini |
| 连接协议 | WebSocket（持久连接，双向流式） |
| 支持语言 | 70 种语言 |
| 主要用途 | 实时语音 AI、视频助手、交互式 NPC |
| Ephemeral tokens | 支持（短期认证 token，适合客户端安全连接） |

## 核心模型

| 模型 | 说明 |
|---|---|
| `gemini-3.1-flash-live-preview` | 高质量 A2A（audio-to-audio），低延迟，实时语音/对话 AI |
| `gemini-2.5-flash-native-audio-preview-12-2025` | 主力 Live API 模型，双向语音/视频 agent，原生音频推理 |

## 核心功能

### 架构

WebSocket 持久连接，双向流式：
- **客户端 → 服务端**：音频块、视频帧、文本
- **服务端 → 客户端**：音频输出、文本、tool calls

### 关键特性

| 特性 | 说明 |
|---|---|
| **打断（Interruption）** | 用户随时打断模型 |
| **工具调用** | 支持 Google Search、Maps、Code Execution、function calling |
| **Session 管理** | 上下文跨对话轮次保持 |
| **Ephemeral tokens** | 短期认证 token，适合安全的客户端直连 |
| **多语言** | 70 种语言支持 |

### 典型应用场景

- 电商零售：购物助手、客户支持
- 游戏：交互式 NPC、实时翻译
- 下一代界面：语音/视频机器人、智能眼镜、车载系统
- 医疗：患者护理和教育助手
- 金融服务：财富管理顾问
- 教育：AI 导师和个性化学习伙伴

## API 示例

```python
# SDK 方式（推荐）
from google import genai

client = genai.Client()
# 参见 live-api/get-started-sdk.md 获取完整示例

# WebSocket 方式（服务端）
# 参见 live-api/get-started-websocket.md
```

## 与 Claude 对应物

Claude 目前无直接等价的实时语音 API。[[OpenAI-Realtime-API]] 是 OpenAI 的对应能力，架构类似（WebRTC/WebSocket 双模）但增加了 SIP 支持。

## 出现来源

- [[live-api--gemini-docs]]

## 相关

- [[Gemini-API]] — 标准（非实时）generateContent 接口
- [[OpenAI-Realtime-API]] — OpenAI 的等价实时语音接口
- [[Gemini-Grounding]] — Live API 支持 Google Search tool
