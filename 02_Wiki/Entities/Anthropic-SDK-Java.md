---
type: entity
name: Anthropic-SDK-Java
aliases: [anthropic Java SDK / anthropic-sdk-java]
category: sdk
status: ga
created: 2026-05-05
---

## 一句话定义

Anthropic Java 客户端 SDK —— P2 仅 stub（仅 2 source 支撑）；详见 `platform.claude.com/docs/en/api/java/`。

## 关键属性

- **官方支持** —— 出现在 streaming、get-started 文档中作为可用 SDK 列表 [[streaming--bwc]] [[get-started--platform]]
- **Repo**：`anthropics/anthropic-sdk-java`（GHA crawler 未深度采集 docs；P2 deferred deeper enrichment）
- **Streaming**：基础支持
- **vs [[Anthropic-SDK-Python]] / [[Anthropic-SDK-TypeScript]]**：等价 client，Java 生态
- **Per-language API ref**：`platform.claude.com/docs/en/api/java/{messages,beta,completions,models}/*`（auto-generated from OpenAPI；canonical concept docs 在 `/api/messages/*` 等通用位置）

## 出现来源

_2 summaries reference this entity_ ——
- [[streaming--bwc]] / [[get-started--platform]]

## 相关

- [[Anthropic-SDK-Python]] / [[Anthropic-SDK-TypeScript]] —— 同级别 SDK
- [[Messages-API]] —— 主要使用 endpoint
