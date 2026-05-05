---
type: summary
source: 01_Raw/docs.openai.com/docs/guides/tools-web-search.md
source_url: https://platform.openai.com/docs/guides/tools-web-search
title: "OpenAI — Web Search 工具"
summarized_at: 2026-05-05
entities_referenced: [Web-search-tool]
concepts_referenced: [Tool-use]
---

## 核心要点

Web search 工具让模型访问互联网获取最新信息，并提供带来源引用的回答。

### 三种模式

1. **Non-reasoning web search**：快速查询，模型向搜索工具发送查询，基于 top 结果返回
2. **Agentic search（推理模型）**：模型在推理链中主动管理多轮搜索，更灵活但较慢
3. **Deep research**：长时间 agent 驱动的深度调研，可查阅数百个来源，运行数分钟；使用 `gpt-5.5` + `high`/`xhigh` reasoning + background mode

### 集成路径选择

| 场景 | 推荐方式 |
|---|---|
| 新集成 | Responses API + `web_search` + `gpt-5.5` |
| 已有 Chat Completions 搜索 | `gpt-5-search-api` |
| 多步研究 / 长时任务 | `gpt-5.5` + `high`/`xhigh` reasoning + background mode |

### 输出结构

- `web_search_call` item：search call ID，action（`search`/`open_page`/`find_in_page`）
- `message` item：文本结果 + 带 URL 的 annotation 引用

内联引用默认包含，**必须在 UI 中清晰可见且可点击**。

### 关键参数

- `search_context_size`：`low`/`medium`/`high`，控制可用 web search context 量
- `filters`：最多 100 个 `allowed_domains` 或 `blocked_domains`
- `user location`：`country`（ISO 2位）、`city`、`region`、`timezone`
- `external_web_access: false`：仅使用缓存/索引结果

### 限制

- Web search context window 上限 128K（即使模型 context 更大）
- 不支持 `gpt-5` + `minimal` reasoning
- Preview 搜索模型（`gpt-4o-search-preview` 等）于 2026-07-23 下线，请迁移到 `web_search`
