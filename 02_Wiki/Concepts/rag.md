---
name: RAG
type: concept
aliases: [Retrieval-Augmented Generation, Contextual Retrieval, RAG Pipeline]
vendors: [Claude, OpenAI, Gemini]
created: 2026-05-05
---

# RAG（检索增强生成）

在生成回答前，先从外部知识库检索相关文档片段注入 context，从而让模型访问训练数据之外的最新或私有知识，同时降低幻觉。

## 核心机制

标准 RAG 流程：
1. **Indexing**：将文档切分为 chunk（数百 token），向量化后存入向量数据库；可选同步建 BM25 倒排索引用于精确匹配
2. **Retrieval**：用户查询向量化后与 index 做相似度搜索，取 top-k 个 chunk
3. **Augmentation**：将检索到的 chunk 拼入 prompt context
4. **Generation**：模型基于注入的 context 生成回答

**Contextual Retrieval（Anthropic 改进）**：标准 RAG 的 chunk 缺乏上下文（"公司营收增长 3%"——哪家公司？），导致检索不准。解决方案：用 Claude 为每个 chunk 自动生成 50–100 token 的情景说明并前置，再做向量化和 BM25 索引。结合 reranking 可将检索失败率降低 67%。利用 prompt caching 降低 context 生成成本（每百万文档 token 约 $1.02）。

**何时不需要 RAG**：知识库 <200K token（约 500 页）时，直接全文放入 prompt + prompt caching 更简单，延迟降低 >2x，成本降低达 90%。

## 跨厂商实现

**Claude**：无原生向量 DB，推荐与 Voyage AI 配合（Anthropic 推荐的 embedding 供应商）；Contextual Retrieval 是 Anthropic 工程团队推出的 RAG 增强方案。

**OpenAI**：Responses API 提供原生 `file_search` 工具，内置向量存储（`vector_stores`），无需自建 pipeline。

**Gemini**：*待确认* — Grounding with Google Search 提供实时检索；长上下文（1M token）可直接替代部分 RAG 场景。

## 关键参数 / API 表面

| 组件 | 说明 |
|---|---|
| Chunk size | 通常 256–1024 tokens；过小失去上下文，过大稀释相关性 |
| Top-k retrieval | 检索候选数量；增大召回率但增加 context 长度 |
| Reranker | 对初步检索结果重排，提升精度 |
| `input_type` | Voyage API：`"query"` vs `"document"` 分别触发不同 prompt prefix |

## 使用场景

**用**：私有/专有知识库问答、实时数据（新闻、文档变更频繁）、超出 context window 的大型语料。

**不用**：知识库小（<200K token）直接放 context；需要精确计算/逻辑推理（RAG 改善知识获取，不改善推理）。

## 相关

- [[embeddings-concept]] — RAG 的向量化基础
- [[grounding]] — RAG 是 grounding 的主要实现路径
- [[Context-window]] — RAG 的目标是在有限窗口内放置最相关内容
- [[Embeddings]] — Anthropic 推荐的 embedding entity
- [[Prompt-caching]] — Contextual Retrieval 利用 prompt caching 降成本

## 出现来源

- [[contextual-retrieval--anthropic-eng]]
- [[contextual-retrieval--anthropic-news]]
- [[embeddings--bwc]]
