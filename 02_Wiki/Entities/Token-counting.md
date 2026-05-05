---
type: entity
name: Token-counting
aliases: [count_tokens / token counter / pre-flight token estimate]
category: api-feature
status: ga
created: 2026-05-05
---

## 一句话定义

Pre-flight 估算 Messages API 请求的 input token 数 —— `POST /v1/messages/count_tokens`。

## 关键属性

- **Endpoint**：`POST /v1/messages/count_tokens` [[token-counting--bwc]] [[count_tokens--msg-api]]
- **Input shape**：和 Messages create 同 —— `model` / `system` / `messages` / `tools` / images / PDFs 等都接受 [[token-counting--bwc]]
- **Response**：`{"input_tokens": 14}` —— 极简 [[token-counting--bwc]]
- **Estimate ≠ exact**：实际生成时 token count 可能小幅差异；可能含 Anthropic 系统优化 token（**不计费**） [[token-counting--bwc]]
- **Server tool**（如 web search）token 仅计第一次 sampling call [[token-counting--bwc]]
- **Use cases**：rate-limit / cost 预估、smart routing（小模型 first）、prompt 长度优化 [[token-counting--bwc]]
- **支持**：所有 active models；ZDR-eligible [[token-counting--bwc]]
- **Beta endpoint**：`/v1/beta/messages/count_tokens` 同 schema [[messages-count_tokens--beta-api]]
- **Citations 兼容**：`cited_text` 不计 input/output 但 system prompt 增量算入 [[Citations-API]]
- **Advisor-tool 交互**：返回仅 executor 第一次 iteration tokens；advisor 估算需单独 call count_tokens with advisor model [[advisor-tool--at]]

## 出现来源

_13 summaries reference this entity_ ——
- [[token-counting--bwc]] / [[count_tokens--msg-api]] / [[messages-count_tokens--beta-api]]
- [[create--msg-api]] / [[messages-create--beta-api]] / [[citations--bwc]] / [[advisor-tool--at]]
- [[overview--bwc]] / [[task-budgets--bwc]] / [[api-and-data-retention--bwc]]

## 相关

- [[Messages-API]] —— same input shape
- [[Rate-limit-API]] —— pre-flight 用于 rate-limit 控制
- [[Vision]] / [[PDF-support]] / [[Tool-use]] —— content block 含这些时 token 算上
