---
type: entity
name: Citations-API
aliases: [citations / cited responses / citation blocks]
category: api-feature
status: ga
created: 2026-05-05
---

## 一句话定义

让 Claude 回答自动 attach 可验证的 source 引用，锚定到提供的 documents（PDF / 纯文本 / 自定义 block）。

## 关键属性

- **启用**：document block 上 `citations.enabled: true`，**all-or-none**（同 request 所有 docs 同步） [[citations--bwc]]
- **Chunking 策略**：PDF / plain text → sentences；custom content → as-provided blocks [[citations--bwc]]
- **Response 格式**：text block 与 `citations[]` array 交替，每个 citation 指向 document span [[citations--bwc]]
- **Index 格式**：
  - PDF → page number range (1-indexed, exclusive end)
  - Plain text → character index range (0-indexed, exclusive end)
  - Custom content → content block index range
- Document indices 0-indexed across full request [[citations--bwc]]
- **可引用 vs 非引用**：`source` content 可引用；`title`、`context` 传给模型但不被引用；图像引用不支持（甚至 PDF 内的图像） [[citations--bwc]]
- **Token 成本**：
  - input 略增（system prompt + chunking 开销）
  - output 极省：`cited_text` 字段不计 output token，也不计后续 input token [[citations--bwc]]
- **兼容性**：
  - ✓ Prompt caching（顶层 document block 加 `cache_control` —— citation 本身不能 cache）
  - ✓ Token counting
  - ✓ Batch processing
  - ✗ **Structured outputs**（互斥 —— citations 需要 interleaved blocks vs 严格 JSON schema）
  - 模型支持：除 Haiku 3 外所有 active 模型 [[citations--bwc]]
- **RAG 替代**：[[Search-results]] block 提供结构化每条结果级 citation [[search-results--bwc]]
- **Bedrock Converse API**：`Claude PDF Chat` 模式必须 enable citations 才走 vision 路径 [[PDF-support]]
- **ZDR-eligible** [[citations--bwc]]

## 出现来源

_10 summaries reference this entity_ ——
- [[citations--bwc]] / [[create--msg-api]] / [[messages-create--beta-api]]
- [[pdf-support--bwc]] / [[search-results--bwc]] / [[structured-outputs--bwc]]
- [[batch-processing--bwc]] / [[token-counting--bwc]] / [[prompt-caching--bwc]]
- [[claude-in-amazon-bedrock--bwc]]

## 相关

- [[Messages-API]] / [[PDF-support]] / [[Prompt-caching]] / [[Token-counting]] / [[Batches-API]]
- [[Search-results]] —— RAG 场景下的 per-result citation 替代
- [[Structured-outputs]] —— 与 citations 互斥
- [[Enterprise-gateway]] —— Bedrock Converse 行为差异
