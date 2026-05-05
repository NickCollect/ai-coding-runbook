---
type: entity
name: Web-fetch-tool
aliases: [web fetch / web_fetch]
category: api-tool
status: ga
created: 2026-05-05
---

## 一句话定义

Anthropic-managed server tool —— Claude 抓 URL 全文（含 PDF），可选 [[Citations-API]]，server-executed。

## 关键属性

- **Tool 版本**：
  - `web_fetch_20260209`：dynamic filtering 通过 [[Code-execution-tool]]（Claude Mythos Preview / Opus 4.7-4.6 / Sonnet 4.6）
  - `web_fetch_20250910`：基础版 [[web-fetch-tool--at]]
- **平台支持**：Claude API + Microsoft Azure（含 Mythos Preview）；**Bedrock / Vertex AI 不支持** [[web-fetch-tool--at]]
- **ZDR**：基础版 eligible；`_20260209` 默认非 ZDR，可 `allowed_callers: ["direct"]` 关 dynamic filtering 换 ZDR [[web-fetch-tool--at]]
- **安全防护**：Claude 不能 dynamically construct URL —— 只能 fetch 用户提供的 URL 或 web search/fetch 之前结果中的 URL；container-tool（如 code execution）回的 URL 不算 [[web-fetch-tool--at]]
- **Tool params**：`max_uses` / `allowed_domains` / `blocked_domains` / `citations.enabled`（optional） / `max_content_tokens`（cap content） [[web-fetch-tool--at]]
- **Response**：`server_tool_use` → `web_fetch_tool_result` 内 `content` = `document` block（text / PDF source、title、retrieved_at 时间戳） [[web-fetch-tool--at]]
- **PDF 处理**：base64 `application/pdf` 返回；自动文本抽取 [[web-fetch-tool--at]]
- **Caching**：fetch 缓存结果（性能），可能不是 latest [[web-fetch-tool--at]]
- **不支持 JS 动态渲染** 的网站 [[web-fetch-tool--at]]
- **Errors**（200 status, error in body）：`url_too_long` (>250 chars) / `url_not_allowed` / `url_not_accessible` / `unsupported_content_type`（仅 text + PDF） / `max_uses_exceeded` 等 [[web-fetch-tool--at]]
- **Pricing**：无额外费，按 fetched content token 计；avg web page (10KB) ≈ 2.5K tokens；large doc (100KB) ≈ 25K；research PDF (500KB) ≈ 125K [[web-fetch-tool--at]]
- **Streaming + Batches-API 兼容** [[web-fetch-tool--at]]
- **数据外泄风险**：处理 untrusted input + 敏感数据时启用要谨慎 → `allowed_domains` 限制 + `max_uses` cap [[web-fetch-tool--at]]
- **法律**：用户直接看到 API output 必须显示 citation [[web-fetch-tool--at]]

## 出现来源

_15 summaries reference this entity_ ——
- [[web-fetch-tool--at]] / [[web-search-tool--at]] / [[tool-use-overview--at]] / [[tool-reference--at]] / [[tool-combinations--at]]
- [[code-execution-tool--at]] / [[server-tools--at]]
- [[adaptive-thinking--bwc]] / [[api-and-data-retention--bwc]]

## 相关

- [[Web-search-tool]] —— 配套使用（search 找 URL，fetch 取全文）
- [[Code-execution-tool]] —— dynamic filtering 后端
- [[Citations-API]] —— optional 开启
- [[PDF-support]] —— PDF 自动文本抽取
- [[Tool-use]] / [[Messages-API]]
