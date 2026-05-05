---
type: entity
name: Compaction
aliases: [compact / context compaction / message compaction]
category: api-feature
status: beta
created: 2026-05-05
---

## 一句话定义

Server-side 上下文压缩 —— input token 超阈值时自动总结历史，扩展有效 context 长度，对抗"context rot"。

## 关键属性

- **Beta header**：`anthropic-beta: compact-2026-01-12` [[compaction--bwc]]
- **支持模型**：Mythos Preview / Opus 4.7 / Opus 4.6 / Sonnet 4.6 [[compaction--bwc]]
- **Mechanism**：
  1. 检测 input token 超 trigger threshold
  2. 生成对话总结
  3. 发出 `compaction` block 含总结
  4. 用压缩后 context 继续响应
  5. 后续请求 append response → API **自动 drop `compaction` block 之前所有 message blocks**，从总结继续 [[compaction--bwc]]
- **Config**：
  ```json
  {"context_management": {"edits": [{"type": "compact_20260112"}]}}
  ```
  + header [[compaction--bwc]]
- **Use cases**：长 multi-turn chat、heavy follow-up tool use 可能爆 context window 的任务 [[compaction--bwc]]
- **优于 client-side 压缩**：1) Anthropic 推荐用此而非自己写；2) 不仅省 token 还防 context rot（长 context 降 focus） [[compaction--bwc]]
- **配对**：[[Context-editing]] 提供更细粒度的 tool result / thinking block 清理；[[Memory-tool]] 跨 compaction boundary 持久化关键事实 [[compaction--bwc]] [[memory-tool--at]] [[context-editing--bwc]]
- **SDK 抽象**：[[Tool-runner]]（Python/TS/Ruby）也支持 client-side compaction（生成总结替换 full history） [[tool-runner--at]]
- **ZDR-eligible** [[compaction--bwc]]

## 出现来源

_13 summaries reference this entity_ ——
- [[compaction--bwc]] / [[context-editing--bwc]] / [[memory-tool--at]]
- [[adaptive-thinking--bwc]] / [[extended-thinking--bwc]] / [[handling-stop-reasons--bwc]]
- [[create--msg-api]] / [[messages-create--beta-api]] / [[manage-tool-context--at]]
- [[tool-runner--at]] / [[task-budgets--bwc]] / [[api-and-data-retention--bwc]]

## 相关

- [[Context-editing]] —— 互补（更细粒度选择性清理）
- [[Memory-tool]] —— 跨 compaction 持久化
- [[Tool-runner]] —— SDK 客户端等价物
- [[Messages-API]] / [[Context-window]]
