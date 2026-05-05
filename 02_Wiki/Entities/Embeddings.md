---
type: entity
name: Embeddings
aliases: [text embeddings / Voyage AI / embedding API]
category: api-feature
status: external
created: 2026-05-05
---

## 一句话定义

**Anthropic 不提供自家 embedding 模型** —— 文档主要推荐 Voyage AI 作为 embedding 供应商之一。

## 关键属性

- **Anthropic 立场**：no own embedding model；推荐 Voyage AI（Anthropic 投资）+ 其他第三方 [[embeddings--bwc]]
- **Voyage 4 模型**（latest，all 32K context，default dim 1024）：
  - `voyage-4-large` —— 通用 / 多语言检索最佳
  - `voyage-4` —— 平衡
  - `voyage-4-lite` —— latency / cost 优化
  - `voyage-4-nano` —— open-weight (Apache 2.0) on Hugging Face [[embeddings--bwc]]
- **Voyage 3 系列**：`voyage-3-large` / `voyage-3.5` / `voyage-3.5-lite` / `voyage-code-3`（代码） / `voyage-finance-2`（金融） / `voyage-law-2`（法律 16K context） [[embeddings--bwc]]
- **多模态**：`voyage-multimodal-3.5` (text+image+video, 32K) / `voyage-multimodal-3` (text+image, 32K) [[embeddings--bwc]]
- **Getting started**：
  ```bash
  export VOYAGE_API_KEY=...
  pip install -U voyageai
  ```
  ```python
  voyageai.Client().embed(texts, model="voyage-4", input_type="document")
  ```
  HTTP：`POST https://api.voyageai.com/v1/embeddings` + `Authorization: Bearer $VOYAGE_API_KEY` [[embeddings--bwc]]
- **AWS Marketplace** 也有 [[embeddings--bwc]]
- **Usage tip**：retrieval 总是设 `input_type` = `"query"` / `"document"`（Voyage 内部加 task-specific prompt） [[embeddings--bwc]]
- **数学性质**：Voyage embeddings 标准化到长度 1 → cosine == dot product；cosine 和 Euclidean 排名一致 [[embeddings--bwc]]
- **Quantization**：`output_dtype` = `float`（默认） / `int8` / `uint8` / `binary` / `ubinary` —— 4× / 32× 存储节省 [[embeddings--bwc]]
- **Matryoshka truncation**：保 leading subset of dimensions（如 1024 → 256） [[embeddings--bwc]]
- **选型 factors**：dataset size + domain、inference perf（lookup + e2e latency）、customization（continued training / domain specialization） [[embeddings--bwc]]

## 出现来源

_3 summaries reference this entity_ ——
- [[embeddings--bwc]] / [[overview--bwc]]

## 相关

- [[Messages-API]] —— RAG 应用的 retrieval 配 Messages 生成
- [[Search-results]] —— RAG 替代方案（不需 embedding 也可 citation）
