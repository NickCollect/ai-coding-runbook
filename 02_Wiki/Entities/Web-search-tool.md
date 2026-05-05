---
type: entity
name: Web-search-tool
aliases: [web search / web_search]
category: api-tool
status: ga
created: 2026-05-05
---

## 一句话定义

Anthropic-managed server tool —— 让 Claude 实时搜 web 内容（突破 knowledge cutoff），response 自带 [[Citations-API]]。

## 关键属性

- **Tool 版本**：
  - `web_search_20260209`：dynamic filtering（Claude Mythos Preview / Opus 4.7-4.6 / Sonnet 4.6）—— Claude 写 Python 在 [[Code-execution-tool]] sandbox 里 post-process search 结果，过滤后再加载 context（Web search 重 token，多 site full HTML 进 context 浪费 + 降质）
  - `web_search_20250305`：基础版，无 dynamic filtering [[web-search-tool--at]]
- **平台支持**：Claude API + Microsoft Foundry + Vertex AI（仅基础版）；**Bedrock 不支持 Mythos Preview** [[web-search-tool--at]]
- **ZDR**：基础版 ZDR-eligible；`_20260209` 默认非 ZDR（用 code execution 内部）；可设 `allowed_callers: ["direct"]` 关闭 dynamic filtering 换 ZDR [[web-search-tool--at]]
- **Citations 强制开启**（与 [[Web-fetch-tool]] 不同，那个 optional） [[web-search-tool--at]]
- **Setup**：组织 admin 必须在 Console privacy settings 启用 web search [[web-search-tool--at]]
- **Tool params**：`max_uses`（cap 搜次数）、`allowed_domains` / `blocked_domains`（互斥，无 scheme，wildcards 仅 path） [[web-search-tool--at]]
- **常用模式**：与 [[Web-fetch-tool]] 组合 —— search `max_uses: 3` 找 candidate URL，fetch `max_uses: 5` 全文回 + citations [[web-search-tool--at]]
- **Mechanism**：Claude 自决何时搜 → API 执行 → 可重复 → 最终带 citation 回答 [[web-search-tool--at]]
- **Pricing**：`usage.server_tool_use.web_search_requests` 计；search 结果进 context 计标准 input token [[web-search-tool--at]]
- **Streaming**：SSE `server_tool_use` block + result block，搜索时 stream 暂停 [[web-search-tool--at]]
- **Batches-API 兼容**：同价 [[web-search-tool--at]]
- **Dynamic filtering 适用场景**：technical docs / lit review + citation verification / response grounding [[web-search-tool--at]]

## 出现来源

_19 summaries reference this entity_ ——
- [[web-search-tool--at]] / [[web-fetch-tool--at]] / [[tool-use-overview--at]] / [[tool-reference--at]] / [[tool-combinations--at]]
- [[code-execution-tool--at]] / [[server-tools--at]] / [[advisor-tool--at]]
- [[adaptive-thinking--bwc]] / [[claude-on-vertex-ai--bwc]] / [[api-and-data-retention--bwc]]

## 相关

- [[Web-fetch-tool]] —— 配套使用
- [[Code-execution-tool]] —— dynamic filtering 后端
- [[Citations-API]] —— 强制开启
- [[Tool-use]] / [[Messages-API]] —— 接入入口
- [[Enterprise-gateway]] —— Bedrock 限制
