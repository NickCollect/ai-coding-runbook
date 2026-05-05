---
name: Vector Embeddings
type: concept
aliases: [Vector Embeddings, Text Embeddings, Semantic Vectors, Dense Vectors]
vendors: [Claude, OpenAI, Gemini]
created: 2026-05-05
---

# Embeddings（向量嵌入）

将文本（或图片、代码等）映射为高维实数向量的技术，使语义相似的内容在向量空间中距离相近，从而支持语义搜索、相似度计算、RAG 等应用。

## 核心机制

Embedding 模型将任意长度的文本编码为固定维度的稠密向量（通常 256–4096 维）。训练目标是使语义相关的文本对（如问题与答案、文档与查询）向量距离小，不相关的文本对距离大。

**相似度计算**：
- **Cosine 相似度**：最常用，对向量长度不敏感（若向量已归一化，等价于点积）
- **Euclidean 距离**：对向量长度敏感
- 多数 embedding 模型输出已归一化向量 → cosine ≈ 点积，性能更高

**检索流程（Vector Search）**：
1. 离线：文档向量化 → 存入向量数据库（Pinecone、Weaviate、pgvector 等）
2. 在线：查询向量化 → ANN（近似最近邻）搜索 → 返回 top-k

**Matryoshka Representation Learning（MRL）**：新一代 embedding 支持截断维度（如 1024 维截取前 256 维仍有效），允许用户在精度和存储之间灵活权衡。

## 跨厂商实现

**Claude/Anthropic**：不提供自有 embedding 模型；官方推荐 **Voyage AI**（与 Anthropic 合作的专门 embedding 服务商）。
- 通用模型：`voyage-4-large`（最高质量）、`voyage-4`（平衡）、`voyage-4-lite`（低延迟）
- 领域专用：`voyage-code-3`（代码）、`voyage-finance-2`（金融）、`voyage-law-2`（法律）
- 多模态：`voyage-multimodal-3.5`（文本+图片+视频）
- 所有 Voyage 4 系列默认 1024 维，支持 256/512/2048 可选

**OpenAI**：`text-embedding-3-large`（3072 维，最高质量）、`text-embedding-3-small`（1536 维，高效率）；支持 MRL 截断；通过 `/v1/embeddings` 调用。

**Gemini**：`text-embedding-004`（768 维）；`gemini-embedding-exp-03-07`（3072 维实验版）；通过 `embedContent` API 调用；支持 `task_type` 区分检索/分类等任务。

## 关键参数 / API 表面

| 参数 | 说明 |
|---|---|
| `input_type` | Voyage：`"query"` / `"document"`；区分触发不同前置 prompt |
| `output_dtype` | Voyage：`float` / `int8` / `binary`；量化节省存储 4x–32x |
| `output_dimension` | 截断维度（MRL 支持的模型） |
| `task_type` | Gemini：`RETRIEVAL_QUERY` / `RETRIEVAL_DOCUMENT` / `CLASSIFICATION` 等 |

## 使用场景

**适用**：
- 语义搜索（超越关键词匹配）
- RAG 的向量检索阶段
- 文档相似度 / 去重
- 推荐系统（内容相似度）
- 聚类分析

**注意**：
- Embedding 模型有 context 上限（通常 8k–32k tokens），超长文档需分块
- 不同模型/版本的向量空间不兼容，升级模型需重新建索引
- 检索和文档用同一模型，且要区分 `input_type`（影响精度）

## 相关

- [[rag]] — embeddings 是 RAG 向量检索的基础
- [[Embeddings]] — Anthropic embeddings entity 档案
- [[grounding]] — embeddings 支持通过检索实现 grounding
- [[multimodal-concept]] — 多模态 embedding（文本+图像）

## 出现来源

- [[embeddings--bwc]]
- [[embeddings--openai-docs]]
- [[embeddings--gemini-docs]]
