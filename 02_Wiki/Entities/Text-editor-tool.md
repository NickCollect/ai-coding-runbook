---
type: entity
name: Text-editor-tool
aliases: [text editor / str_replace_based_edit_tool / file editor]
category: api-tool
status: ga
created: 2026-05-05
---

## 一句话定义

Anthropic API 的 client-side 文件编辑工具 —— Claude 通过预定义 schema 查看 + 修改文件，执行由 client 应用负责。

## 关键属性

- **Tool 版本**：
  - `text_editor_20250728`：Claude 4 模型，加 `max_characters` 参数（view 大文件截断控制）
  - `text_editor_20250124`：Sonnet 3.7 [[text-editor-tool--at]]
- **Schema-less**：内置模型 [[text-editor-tool--at]]
- **Commands**：
  - `view`：path + 可选 `view_range: [start, end]`（1-indexed，-1 = EOF）；强烈建议 client 在 view 输出加 line number prefix
  - `str_replace`：`old_str` exact match（含 whitespace + 缩进），1 match 严格；0 match 报错；多 match 报错要求加 context
  - `create`：`path` + `file_text`
  - `insert`：`insert_text` after `insert_line`（0 = beginning）
  - **`undo_edit` 已在 `text_editor_20250429` 移除** [[text-editor-tool--at]]
- **典型 workflow**：用户报 bug → Claude `view` → app 回带行号内容 → Claude `str_replace` → "Successfully replaced text at exactly one location" → Claude end_turn [[text-editor-tool--at]]
- **Error 格式**：`tool_result` + `is_error: true`；canonical strings 如 "Error: File not found" / "Error: Found 3 matches for replacement text. Please provide more context to make a unique match." [[text-editor-tool--at]]
- **Best practices**：edit 前 .backup 备份、path traversal 防（禁 `..` / `/etc/`）、unique replacement helper、edit 后 syntax check（如 `ast.parse(content)`） [[text-editor-tool--at]]
- **Pricing**：每请求 +**700 input tokens**（4.x 和 3.7 同价） [[text-editor-tool--at]]
- **配对**：[[Bash-tool-API]] —— inspect → edit → test → repeat 是 canonical 软件开发 loop [[text-editor-tool--at]]
- **Memory-tool 用同样 commands**：[[Memory-tool]] 的 view/create/str_replace/insert 同 schema，不同语义 [[memory-tool--at]]
- **Code-execution-tool 内置版**：`text_editor_code_execution` 子 tool（响应 `text_editor_code_execution_tool_result`）和此 client-side tool 不同 [[code-execution-tool--at]]
- **ZDR-eligible** [[text-editor-tool--at]]

## 出现来源

_14 summaries reference this entity_ ——
- [[text-editor-tool--at]] / [[bash-tool--at]] / [[tool-use-overview--at]] / [[tool-reference--at]] / [[tool-combinations--at]]
- [[code-execution-tool--at]] / [[memory-tool--at]] / [[computer-use-tool--at]] / [[server-tools--at]]
- [[manage-tool-context--at]] / [[strict-tool-use--at]]

## 相关

- [[Bash-tool-API]] —— canonical 配对
- [[Memory-tool]] —— 同样 commands 不同语义
- [[Code-execution-tool]] —— Anthropic-managed 等价物
- [[Tool-use]] / [[Messages-API]]
