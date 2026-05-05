---
name: Gemini Grounding
type: entity
vendor: Gemini
aliases: ["Google Search Grounding", "grounding", "GoogleSearch tool", "dynamic retrieval"]
created: 2026-05-05
---

# Gemini Grounding

将 Gemini 模型连接到实时 Google Search 网页内容的工具；通过在 generateContent 中传入 `google_search` tool 启用，模型自动决定是否触发搜索，结果以 `groundingMetadata` 返回。

## 关键属性

| 属性 | 值 |
|---|---|
| Vendor | Google / Gemini |
| 启用方式 | `tools=[Tool(google_search=GoogleSearch())]` |
| 支持语言 | 所有可用语言 |
| 返回数据 | `groundingMetadata`（含查询词、来源 URL、text-to-source 映射） |
| ToS 要求 | 必须在 UI 中渲染 `searchEntryPoint` 组件 |

## 核心功能

### 三大优势

1. **减少幻觉**：以真实世界信息为依据
2. **实时信息**：回答当前事件、最新数据
3. **可引用来源**：`groundingChunks` 提供可验证的 source URL

### 工作流程（自动）

1. 应用发送 prompt + `google_search` tool 启用
2. 模型分析 prompt，判断 Search 是否能改善答案
3. 模型自动生成并执行一个或多个搜索查询
4. 模型处理搜索结果，合成信息，生成响应
5. API 返回最终响应 + `groundingMetadata`

### groundingMetadata 结构

```json
{
  "groundingMetadata": {
    "webSearchQueries": ["UEFA Euro 2024 winner"],
    "searchEntryPoint": { "renderedContent": "<!-- HTML/CSS for Search widget -->" },
    "groundingChunks": [
      {"web": {"uri": "https://...", "title": "aljazeera.com"}}
    ],
    "groundingSupports": [
      {
        "segment": {"startIndex": 0, "endIndex": 85, "text": "Spain won Euro 2024..."},
        "groundingChunkIndices": [0]
      }
    ]
  }
}
```

### Dynamic Retrieval

仅当模型判断 Search 会改善答案时才触发，优化成本。计费规则：只有收到至少一个 grounding URL 的请求才收取 Search Grounding 费用。

### 与 URL Context 组合

Google Search Grounding 可与 URL Context tool 同时使用，同时 ground 在实时网页数据和指定 URL 上。

### 定价

| 层级 | 费率 |
|---|---|
| 免费（Gemini 2.5 Flash/Flash-Lite） | 500 RPD 免费（共享） |
| 付费（Gemini 2.5） | 1500 RPD 免费后 $35/1000 prompts |
| 付费（Gemini 3） | 5000 prompts/月免费后 $14/1000 queries |

## API 示例

```python
from google import genai
from google.genai import types

client = genai.Client()
grounding_tool = types.Tool(google_search=types.GoogleSearch())

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Who won Euro 2024?",
    config=types.GenerateContentConfig(tools=[grounding_tool]),
)
print(response.text)
```

```javascript
// JavaScript
tools: [{ googleSearch: {} }]
```

## 与 Claude 对应物

[[Web-search-tool]] — Claude 的网页搜索工具，功能定位相似（实时网络搜索、减少幻觉），但无类似 grounding metadata 的 text-to-source 映射机制。

## 出现来源

- [[google-search--gemini-docs]]

## 相关

- [[Gemini-API]] — 通过 tools 参数启用
- [[Gemini-Code-Execution]] — 可与 grounding 组合使用
- [[Web-search-tool]] — Claude 对应物
