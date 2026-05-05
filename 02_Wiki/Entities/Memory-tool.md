---
type: entity
name: Memory-tool
aliases: [memory_20250818 / agent memory tool]
category: api-tool
status: ga
created: 2026-05-05
---

## 一句话定义

Anthropic API 的 client-side persistent memory tool —— Claude 在 `/memories` 目录里 view/create/edit/delete/rename 文件，跨 session 保留（**与 Claude Code 的 [[Memory]] 和 API beta [[Memory-store]] 区分**）。

## 关键属性

- **Tool definition**：`{"type": "memory_20250818", "name": "memory"}`；SDK helpers `BetaAbstractMemoryTool` (Python) / `betaMemoryTool` (TS) 接 file/DB/cloud backend [[memory-tool--at]]
- **Client-side**：你 app 控制存储位置 + 实现 commands；Claude 只发指令 [[memory-tool--at]]
- **强制 `/memories` 目录**：所有 memory 操作限于此 dir [[memory-tool--at]]
- **Commands**：
  - `view`：dir listing（2 levels deep, 人读 size, 排除 hidden + node_modules）或 file content（带 1-indexed 行号 + tab 分隔）；>999,999 行 error
  - `create`：file_text；已存在 error
  - `str_replace`：in-place 替换；old_str 不存在 / 多 match 都 error 列行号
  - `insert`：在 insert_line 处插入
  - `delete`：file or dir（recursive）
  - `rename`：destination 已存在 error（不覆盖） [[memory-tool--at]]
- **Auto system prompt**：tool 启用时自动 inject —— "ALWAYS VIEW YOUR MEMORY DIRECTORY BEFORE DOING ANYTHING ELSE. MEMORY PROTOCOL: 1. view check earlier progress 2. work on task ... ASSUME INTERRUPTION..." [[memory-tool--at]]
- **Security**：strip secrets、file size guardrails、memory expiration、**path traversal 关键防护**（验证 `/memories` 起点、resolve canonical、reject `../` / `..\\` / `%2e%2e%2f`，用 `pathlib.Path.resolve()` + `relative_to()`） [[memory-tool--at]]
- **错误模式**：mirror [[Text-editor-tool]] —— file not found / permission / invalid path / duplicate match [[memory-tool--at]]
- **配对**：
  - [[Context-editing]] trim 旧 `tool_result`，memory 持久化关键事实
  - [[Compaction]] server-side 总结，memory 跨 compaction 保留 critical info [[memory-tool--at]]
- **Multi-session 模式**：initializer session bootstrap memory（progress log + checklist）→ subsequent sessions 读取秒恢复 → end-of-session 写完成 + remaining；一 feature at a time，end-to-end verify 后再 mark complete [[memory-tool--at]]
- **ZDR-eligible**（数据 client-side） [[memory-tool--at]]
- **Cluttered memory addendum**：可加 system prompt "Always try to keep its content up-to-date, coherent and organized. You can rename or delete files that are no longer relevant." [[memory-tool--at]]

## 出现来源

_12 summaries reference this entity_ ——
- [[memory-tool--at]] / [[tool-use-overview--at]] / [[tool-reference--at]] / [[server-tools--at]]
- [[manage-tool-context--at]] / [[context-editing--bwc]] / [[compaction--bwc]]
- [[api-and-data-retention--bwc]]

## 相关

- [[Memory]] —— Claude Code 的 memory（不同概念）
- [[Memory-store]] —— API beta `/v1/beta/memory_stores`（不同概念，server-managed 持久存储）
- [[Text-editor-tool]] —— 同样 commands 不同语义
- [[Context-editing]] / [[Compaction]] —— canonical 配对
- [[Tool-use]] / [[Messages-API]]
