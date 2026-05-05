---
type: entity
name: Structured-outputs
aliases: [structured outputs / output_config.format / json_schema mode / strict tool use]
category: api-feature
status: ga
created: 2026-05-05
---

## 一句话定义

通过 constrained decoding 强制 Claude 响应符合 JSON schema —— 永远 parseable + type-safe + 无 retry。

## 关键属性

- **两个互补 features**（独立或组合用）：
  - **JSON outputs** —— `output_config.format`：response 受 JSON schema 约束
  - **Strict tool use** —— tool definition 上 `strict: true`：tool name + input 验证保证 [[structured-outputs--bwc]]
- **Migration**：旧 `output_format` 参数移到 `output_config.format`；旧 beta header `structured-outputs-2025-11-13` 仍可用；新 API shape **GA 无 beta header** [[structured-outputs--bwc]]
- **平台支持**：
  - Claude API：Mythos Preview / Opus 4.7 / Opus 4.6 / Sonnet 4.6 / Sonnet 4.5 / Opus 4.5 / Haiku 4.5
  - Bedrock：Opus 4.6 / Sonnet 4.6 / Sonnet 4.5 / Opus 4.5 / Haiku 4.5；Opus 4.7 + Mythos via "Claude in Amazon Bedrock" Messages-API endpoint
  - Microsoft Foundry：beta
  - Vertex AI：**不支持 Mythos Preview** [[structured-outputs--bwc]] [[Enterprise-gateway]]
- **Request shape**：
  ```json
  {"output_config": {"format": {
    "type": "json_schema",
    "schema": {"type": "object", "properties": {...}, "required": [...], "additionalProperties": false}
  }}}
  ```
- **Strict tool use**：tool definition 上 `strict: true`，同 JSON schema grammar pipeline [[structured-outputs--bwc]] [[strict-tool-use--at]]
- **Limitations**：
  - **与 [[Citations-API]] 互斥** —— 任何 user document 启用 citations 同时设 `output_config.format` → 400（citations 需 interleaved blocks，strict JSON 禁止）
  - **PHI 限制 (HIPAA)**：勿在 schema 的 property name / `enum` / `const` / `pattern` 放 PHI（schema cache 24h 不含 prompt-level PHI 防护）
- **Data retention**：prompts/outputs 不存；仅 JSON schema cache for grammar compilation **up to 24h since last use**；strict tool use 用同 pipeline [[structured-outputs--bwc]]
- **价值**：no `JSON.parse()` errors、type-safe、no retries for schema violation [[structured-outputs--bwc]]
- **ZDR-eligible** (qualified) [[structured-outputs--bwc]]

## 出现来源

_12 summaries reference this entity_ ——
- [[structured-outputs--bwc]] / [[strict-tool-use--at]] / [[tool-use-overview--at]] / [[tool-reference--at]]
- [[create--msg-api]] / [[messages-create--beta-api]] / [[citations--bwc]]
- [[handling-stop-reasons--bwc]] / [[api-and-data-retention--bwc]] / [[manage-tool-context--at]]

## 相关

- [[Citations-API]] —— 互斥
- [[Tool-use]] —— strict 模式应用
- [[Messages-API]] —— `output_config.format` 字段
- [[Enterprise-gateway]] —— Bedrock / Vertex / Foundry 跨平台支持矩阵
