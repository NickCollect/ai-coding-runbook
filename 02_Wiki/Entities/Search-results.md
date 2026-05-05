---
type: entity
name: Search-results
aliases: [search-result blocks / search_result content blocks / RAG citations]
category: api-feature
status: ga
created: 2026-05-05
---

## 一句话定义

`search_result` content block —— 给自定义 RAG 应用提供 web-search-quality 的自然 citation（per-result 级，比 document chunking 更结构化）。

## 关键属性

- **支持模型**：Opus 4.7 / Opus 4.6 / Sonnet 4.6 / Sonnet 4.5 / Opus 4.5 / Opus 4.1 / Sonnet 3.7（deprecated）/ Haiku 4.5 / Haiku 3.5（deprecated） [[search-results--bwc]]
- **两种 delivery 模式**：
  1. **From tool calls**（`tool_result`）—— custom tool 返回 `search_result` block → 动态 RAG + auto citation
  2. **As top-level user content** —— pre-fetched / cached 结果直接放 user message [[search-results--bwc]]
- **Schema**：
  ```json
  {
    "type": "search_result",
    "source": "https://...",
    "title": "Article Title",
    "content": [{"type": "text", "text": "..."}],
    "citations": {"enabled": true}
  }
  ```
- **Required**：`type` / `source` / `title` / `content`（非空 text block 数组） [[search-results--bwc]]
- **Optional**：`citations.enabled` / `cache_control: {type: "ephemeral"}` [[search-results--bwc]]
- **优势 vs document block**：
  - 自然 citation 格式匹配 web search 质量
  - 灵活（tool 返回或 top-level）
  - per-result source + title attribution
  - 无需 document block workaround [[search-results--bwc]]
- **ZDR-eligible** [[search-results--bwc]]

## 出现来源

_4 summaries reference this entity_ ——
- [[search-results--bwc]] / [[citations--bwc]] / [[create--msg-api]]
- [[api-and-data-retention--bwc]]

## 相关

- [[Citations-API]] —— 总体 citation framework；search_result 是其结构化变体
- [[Web-search-tool]] —— server-managed search（自带 citation）
- [[Messages-API]] / [[Tool-use]]
- [[Prompt-caching]] —— 可加 cache_control
