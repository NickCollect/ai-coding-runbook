---
name: Gemini API
type: entity
vendor: Gemini
aliases: ["Gemini API", "generateContent", "google-genai", "@google/genai"]
created: 2026-05-05
---

# Gemini API

Google 的大语言模型 API，核心方法为 `generateContent`；支持文本、图像、音视频等多模态输入，提供 Python、JavaScript、Go、Java、C# 多语言 SDK。

## 关键属性

| 属性 | 值 |
|---|---|
| Vendor | Google / Gemini |
| REST 端点 | `POST https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent` |
| Python 包 | `google-genai`（`pip install google-genai`） |
| JS 包 | `@google/genai`（`npm install @google/genai`） |
| 认证 | `GEMINI_API_KEY` 环境变量 |
| 当前默认模型 | `gemini-3-flash-preview` |

## 核心功能

### 主要模型系列（2026 年 5 月）

| 系列 | 旗舰模型 | 特点 |
|---|---|---|
| Gemini 3 | `gemini-3.1-pro-preview` | 最强推理，复杂问题求解，agentic 编程 |
| Gemini 3 Flash | `gemini-3-flash-preview` | 前沿性能，成本分数之一 |
| Gemini 2.5 Pro | `gemini-2.5-pro` | 最强 2.5 系列，复杂任务 |
| Gemini 2.5 Flash | `gemini-2.5-flash` | 最佳价格/性能比，低延迟大批量 |

### SDK 支持语言

| 语言 | 包名 | 最低版本要求 |
|---|---|---|
| Python | `google-genai` | 3.9+ |
| JavaScript | `@google/genai` | Node 18+ |
| Go | `google.golang.org/genai` | — |
| Java | `com.google.genai:google-genai:1.0.0` | Maven |
| C# | `Google.GenAI` | — |

### 模型版本命名规范

| 模式 | 说明 | 示例 |
|---|---|---|
| Stable | 固定快照，不会变 | `gemini-2.5-flash` |
| Preview | 可用于生产，≥2 周通知后 deprecate | `gemini-2.5-flash-preview-09-2025` |
| Latest | 自动更新别名 | `gemini-flash-latest` |
| Experimental | 不适合生产 | — |

### OpenAI 兼容端点

Gemini 提供 OpenAI 兼容端点，支持用 OpenAI SDK 向 Gemini 发送 Chat Completions 格式请求。

## API 示例

```python
from google import genai

client = genai.Client()  # 自动读取 GEMINI_API_KEY

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Explain how AI works in a few words"
)
print(response.text)
```

```bash
# REST 调用
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"contents":[{"parts":[{"text":"Hello"}]}]}'
```

## 与 Claude 对应物

[[Messages-API]] — Anthropic 的消息接口；`client.messages.create()` 对应 `client.models.generate_content()`。

## 出现来源

- [[quickstart--gemini-docs]]
- [[models--gemini-docs]]
- [[text-generation--gemini-docs]]
- [[openai--gemini-docs]]

## 相关

- [[Gemini-Thinking]] — generateContent + thinking-capable 模型 = 思考模式
- [[Gemini-Grounding]] — generateContent + Google Search tool = grounding
- [[Gemini-Code-Execution]] — generateContent + code execution tool
- [[Gemini-Context-Caching]] — 通过 `cached_content` 参数使用缓存
- [[Gemini-Files-API]] — 上传文件后在 generateContent 中引用
