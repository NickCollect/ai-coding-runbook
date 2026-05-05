---
type: entity
name: Batches-API
aliases: [message batches / batch processing / batch API / Message Batches API]
category: api-feature
status: ga
created: 2026-05-05
---

## 一句话定义

Anthropic 异步批量 Messages 处理 API（`POST /v1/messages/batches`），50% 标准价格，多数 1 小时内完成。

## 关键属性

- **价格**：50% 标准 Messages 价格（叠加 prompt caching multiplier、data residency 1.1×） [[batch-processing--bwc]] [[Prompt-caching]]
- **限制**：单 batch 最多 100,000 requests 或 256 MB（whichever first）；24h 未完成自动 expire；结果保留 29 天 [[batch-processing--bwc]]
- **数据驻留**：**not ZDR-eligible** —— async 存储要求 [[batch-processing--bwc]]
- **Endpoint**：`POST /v1/messages/batches` body = `{requests: [{custom_id, params}, ...]}` [[batches-create--msg-api]] [[batch-processing--bwc]]
- **`custom_id` regex**：`^[a-zA-Z0-9_-]{1,64}$` —— 调用方提供，结果按此 key 关联 [[batch-processing--bwc]]
- **Workflow**：submit → poll status → retrieve results when complete or 24h（whichever first）[[batches-retrieve--msg-api]] [[batches-results--msg-api]]
- **Operations**：`POST /create`、`GET /retrieve`、`GET /list`、`POST /cancel`、`DELETE /delete`、`GET /results` [[batches-cancel--msg-api]] [[batches-delete--msg-api]] [[batches-list--msg-api]]
- **支持的 Messages features**：vision、tool use、system prompts、multi-turn、beta features 全部支持 [[batch-processing--bwc]]
- **`max_tokens: 0` 不支持**（缓存预热模式不可用 in batch，因为 cache 可能在后续运行前过期） [[batch-processing--bwc]]
- **Workspace-scoped**：每 workspace 独立 batch；可能略超 spend limit（throughput 开销） [[batch-processing--bwc]]
- **Rate limits**：HTTP request 和 in-flight requests-within-batch 都受限 [[batch-processing--bwc]]
- **缓存策略**：长 batch 用 1h cache duration（5m default 可能 batch 期间过期） [[batch-processing--bwc]] [[Prompt-caching]]
- **Beta endpoint**：`/v1/beta/messages/batches` 同 schema [[messages-batches-index--beta-api]] [[messages-batches-create--beta-api]]
- **Pricing table** (per MTok, batch input / batch output)：Opus 4.7 $2.50 / $12.50；Sonnet 4.6 $1.50 / $7.50；Haiku 4.5 $0.50 / $2.50 [[batch-processing--bwc]]

## 出现来源

_33 summaries reference this entity_ —— 主要：
- [[batch-processing--bwc]] / [[batches--msg-api]] / [[batches-create--msg-api]] / [[batches-retrieve--msg-api]] / [[batches-list--msg-api]] / [[batches-cancel--msg-api]] / [[batches-delete--msg-api]] / [[batches-results--msg-api]]
- [[messages-batches-create--beta-api]] / [[messages-batches-cancel--beta-api]] / [[messages-batches-delete--beta-api]] / [[messages-batches-list--beta-api]] / [[messages-batches-results--beta-api]] / [[messages-batches-retrieve--beta-api]] / [[messages-batches-index--beta-api]]
- [[citations--bwc]] / [[prompt-caching--bwc]] / [[token-counting--bwc]] / [[advisor-tool--at]] / [[adaptive-thinking--bwc]]

## 相关

- [[Messages-API]] —— batch 是 Messages 的异步模式
- [[Prompt-caching]] —— 长 batch 推荐 1h cache
- [[Workspace]] —— batch 按 workspace 隔离 + 计费
- [[Rate-limit-API]] —— batch 也受 rate limit
