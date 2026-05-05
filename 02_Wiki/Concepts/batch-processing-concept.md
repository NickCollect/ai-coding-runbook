---
name: Batch Processing
type: concept
aliases: [Async Batch, Message Batches, Offline Batch, Bulk Inference]
vendors: [Claude, OpenAI, Gemini]
created: 2026-05-05
---

# Batch Processing（批量处理）

以异步方式提交大批量 LLM 请求，以换取显著价格折扣的 API 使用模式。适用于延迟不敏感的大规模任务（数据标注、评估、离线生成等）。

## 核心机制

与实时（同步）API 相对的异步批处理流程：

1. **提交**：一次性提交包含多个请求的批次（每个请求有唯一 `custom_id`）
2. **排队处理**：系统在闲时异步处理，每个请求独立执行
3. **轮询**：定期查询批次状态（`processing` → `ended`）
4. **获取结果**：批次完成后下载 JSONL 结果，通过 `custom_id` 对应原始请求

**为什么便宜**：批处理允许服务商在低峰期调度计算资源，利用率更高，因此按 50% 标准价格收费。

**关键限制**：
- 批次内请求数：最大 100,000 条 OR 256 MB（先达者为准）
- 处理时限：24 小时（超时的批次中未完成请求被取消）
- 结果保留：创建后 29 天内可下载结果
- **不支持 ZDR**（需要异步存储）

## 跨厂商实现

**Claude（Message Batches API）**：
- 50% 价格折扣；大多数批次 <1 小时完成
- 端点：`POST /v1/messages/batches`
- `custom_id` 格式：`^[a-zA-Z0-9_-]{1,64}$`
- 支持所有 Messages API 功能（vision、tool use、system prompt、multi-turn、beta）
- Prompt Caching 建议用 1 小时 cache duration（批次跨越 5 分钟默认 TTL）
- **不包含** Managed Agents 功能

**OpenAI（Batch API）**：
- 50% 价格折扣；24 小时处理窗口
- 请求通过 JSONL 文件上传（Files API）；每行一个请求
- 结果也以 JSONL 文件返回
- 支持 Chat Completions、Embeddings 等端点

**Gemini（Batch API）**：
- *待确认* 具体定价和限制

## 关键参数 / API 表面

| 参数 | 说明 |
|---|---|
| `requests` | 批次请求列表，每项含 `custom_id` + `params` |
| `custom_id` | 用于关联结果和原始请求的唯一标识符 |
| `processing_status` | `validating` / `in_progress` / `ended` |
| `request_counts` | 各状态请求计数（`succeeded`、`errored`、`canceled`） |
| `results_url` | 结果下载 URL |

**批次价格对照（Claude，截至 2026-05）**：

| 模型 | 批处理输入 ($/MTok) | 批处理输出 ($/MTok) |
|---|---|---|
| Opus 4.7 | $2.50 | $12.50 |
| Sonnet 4.6/4.5 | $1.50 | $7.50 |
| Haiku 4.5 | $0.50 | $2.50 |

## 使用场景

**适用**：
- 大规模数据标注（数千至数十万条）
- 评估集运行（eval pipeline）
- 离线文档处理（摘要、分类、提取）
- A/B 测试多个 prompt 变体

**不适用**：
- 实时用户交互（响应延迟要求 <5 秒）
- 需要流式输出的场景
- ZDR 合规要求的数据

## 相关

- [[Batches-API]] — Claude Message Batches API entity 档案
- [[streaming-concept]] — 实时流式的对立选择
- [[rate-limiting]] — 批处理有独立配额，不占 RPM/TPM
- [[cost-optimization]] — 批处理是最直接的 50% 成本折扣

## 出现来源

- [[batch-processing--bwc]]
- [[batches--msg-api]]
- [[batch-api--gemini-docs]]
