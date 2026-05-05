---
name: Grounding
type: concept
aliases: [Factual Grounding, Source Grounding, Anti-hallucination, Knowledge Grounding]
vendors: [Claude, OpenAI, Gemini]
created: 2026-05-05
---

# Grounding（事实锚定）

将 LLM 输出锚定到可验证外部信息源（文档、数据库、搜索结果、工具调用）的技术，目的是减少模型依赖训练权重中可能过时或错误的知识而产生的幻觉。

## 核心机制

LLM 的幻觉来源于：训练数据过时、知识截止日期后的新信息缺失、模型对低频知识的不确定性被过度自信地生成。Grounding 通过以下方式解决：

**1. 检索增强（RAG）**：在生成前检索相关文档注入 context，让模型"引用"而非"记忆"
**2. 工具调用**：在线检索（Web Search）、数据库查询、API 调用，获取实时或精确数据
**3. 引用机制**：要求模型输出时标注信息来源，支持事后验证
**4. 上下文约束**：在 system prompt 中明确"只基于提供的文档回答，无法找到答案时说不知道"

## 跨厂商实现

**Claude**：
- 内置 Web Search 工具（`web_search`）：实时搜索互联网，返回带 URL 的结果
- Citations API（beta）：自动为引用加注来源，支持文档级别的精确引用
- 原则上鼓励在 system prompt 中要求模型区分"文档中的事实"和"自身知识"

**OpenAI**：
- Responses API 内置 `web_search` 工具（基于 Bing）；可配置搜索范围
- `file_search` 工具：从 vector stores 中检索文档（内置 RAG）
- 支持 grounding 来源引用（`annotations` 字段返回 URL 和页面标题）

**Gemini**：
- **Grounding with Google Search**：内置 Google 搜索集成，返回时附带 `groundingMetadata`（搜索查询、检索 chunk、来源 URI）
- **Maps Grounding**：地理位置相关的 grounding（Google Maps 数据源）
- `dynamicRetrievalConfig`：控制何时触发检索（threshold 参数）
- `groundingChunks` + `groundingSupports` 字段：精确标注哪段文本基于哪个来源

## 关键参数 / API 表面

| 工具/字段 | 说明 |
|---|---|
| `web_search` tool | Claude/OpenAI：实时 Web 搜索工具 |
| `file_search` tool (OpenAI) | 向量库检索 |
| `google_search_retrieval` (Gemini) | Google Search grounding 配置 |
| `groundingMetadata` (Gemini) | 返回的来源元数据 |
| `annotations` (OpenAI) | 引用来源列表 |
| Citations API (Claude) | 自动引用标注 |

## 使用场景

**必须 grounding**：
- 需要实时/最新信息（新闻、股价、天气）
- 精确事实查询（法律条款、医疗数据）
- 企业内部知识库问答（私有数据）
- 高风险应用（医疗、法律建议）——hallucination 代价高

**不需要 grounding**：
- 创意写作（hallucination 反而有益）
- 代码生成（逻辑验证比来源引用更重要）
- 通用对话（低风险）

## 相关

- [[rag]] — grounding 的主要实现技术
- [[Web-search-tool]] — Claude Web 搜索工具 entity
- [[safety-and-guardrails]] — grounding 是减少有害幻觉的安全手段
- [[embeddings-concept]] — RAG grounding 的向量检索基础

## 出现来源

- [[contextual-retrieval--anthropic-eng]]
- [[maps-grounding--gemini-docs]]
- [[safety-guidance--gemini-docs]]
