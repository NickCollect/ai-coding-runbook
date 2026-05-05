---
type: entity
name: PDF-support
aliases: [pdf / pdf documents / PDF input]
category: api-feature
status: ga
created: 2026-05-05
---

## 一句话定义

Messages API 接受 PDF document block 输入（base64 / URL / Files API），基于 [[Vision]] 能力理解图表 + 表格。

## 关键属性

- **限制**：max 32 MB request；600 pages（200k-window 模型 100 pages）；标准 PDF（无密码 / 加密） [[pdf-support--bwc]]
- **大 PDF 用 Files API**：`file_id` 而非 base64 减小 request payload [[Files-API]] [[pdf-support--bwc]]
- **三种 source**：URL / base64 / file_id [[pdf-support--bwc]]
- **Document block schema**：`{type: "document", source: {...}}` content block [[pdf-support--bwc]]
- **平台支持**：直 API 全模型支持；Vertex AI 支持；Bedrock 有 caveat（见下） [[pdf-support--bwc]]
- **Bedrock Converse API 两模式**：
  - **Converse Document Chat** —— text-only 提取（~1k token / 3-page PDF），未启用 citations 时默认
  - **Claude PDF Chat** —— 完整 vision（charts / layout），每页 text + image，~7k token / 3-page；**必须启用 citations**
  - **InvokeModel API**（非 Converse）—— 不强制 citations [[pdf-support--bwc]] [[Enterprise-gateway]]
- **Dense PDF 注意**：小字 / 复杂表 / 图密 → context window 可能在 page limit 之前耗尽，应 split 或 downsample [[pdf-support--bwc]]
- **非 PDF 文档**（.csv / .xlsx / .docx / .md / .txt）：先转纯文本或 PDF [[files--bwc]]
- **ZDR-eligible** [[pdf-support--bwc]]
- **Citations 兼容**：PDF 引用 page number range（1-indexed, exclusive end） [[Citations-API]]

## 出现来源

_10 summaries reference this entity_ ——
- [[pdf-support--bwc]] / [[vision--bwc]] / [[citations--bwc]]
- [[create--msg-api]] / [[files--bwc]] / [[files-upload--beta-api]]
- [[claude-in-amazon-bedrock--bwc]] / [[claude-on-vertex-ai--bwc]]

## 相关

- [[Messages-API]] / [[Vision]] / [[Files-API]] / [[Citations-API]]
- [[Enterprise-gateway]] —— Bedrock 模式差异
