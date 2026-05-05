---
type: entity
name: Code-execution-tool
aliases: [code execution / code_execution / Python sandbox / code interpreter]
category: api-tool
status: ga
created: 2026-05-05
---

## 一句话定义

Anthropic-managed sandbox（Python 3.11.12 + Linux x86_64），让 Claude 在 API 对话内跑 Python + bash + 创建/编辑文件 + 处理上传文件。

## 关键属性

- **Tool 版本**：
  - `code_execution_20250825`：Bash + file ops + Python（全模型）
  - `code_execution_20260120`：加 REPL state persistence + programmatic tool calling（仅 Opus 4.5+ / Sonnet 4.5+）
  - 老 `code_execution_20250522`：Python only（仍可用） [[code-execution-tool--at]]
- **可用平台**：Claude API + Microsoft Azure AI Foundry。**Bedrock / Vertex AI 不支持** [[code-execution-tool--at]]
- **Runtime**：5 GiB RAM、5 GiB disk、1 CPU、**完全无网络访问**（不能出站） [[code-execution-tool--at]]
- **预装库**：pandas / numpy / scipy / scikit-learn / matplotlib / seaborn / pyarrow / openpyxl / pillow / python-pptx / python-docx / pypdf / pdfplumber / sympy / tqdm / sqlite / ripgrep / fd 等 [[code-execution-tool--at]]
- **两个 sub-tools**：`bash_code_execution` + `text_editor_code_execution`（response 用 `bash_code_execution_tool_result` / `text_editor_code_execution_tool_result` 不同 result block） [[code-execution-tool--at]]
- **Container lifecycle**：scoped to API workspace，30 天后过期；通过 `container: <id>` 跨请求复用保持文件 [[code-execution-tool--at]]
- **Pricing**：免费 with [[Web-search-tool]] / [[Web-fetch-tool]]；独立用按时间计费（最低 5 分钟），免费 1,550 小时/月，超出 $0.05/h/container；如 request 含 file 即使没调用也按时间计费 [[code-execution-tool--at]]
- **Files API 集成**：用 `container_upload` block 引用 [[Files-API]] 上传的 CSV/Excel/JSON/XML/images/text [[code-execution-tool--at]] [[Files-API]]
- **Skill 接入**：Code execution 让 Claude 用 [[Skill]]（"Skills 是模块化能力 = instructions + scripts + resources"） [[code-execution-tool--at]]
- **Multi-environment 警告**：与 client-provided [[Bash-tool-API]] 同时启用 → 两个独立 sandbox，state 不共享，需 system prompt 说明区别 [[code-execution-tool--at]]
- **`pause_turn`**：长跑可能 `stop_reason: pause_turn`，原样回传让 Claude 继续 [[code-execution-tool--at]]
- **Streaming**：SSE `server_tool_use` block + `partial_json` for code → 暂停执行 → result block [[code-execution-tool--at]] [[Streaming-API]]
- **Batches-API 兼容**：同价 [[Batches-API]]
- **数据驻留**：**Not ZDR-eligible** [[code-execution-tool--at]]
- **常用 dynamic filtering 配套**：[[Web-search-tool]] / [[Web-fetch-tool]] 的 `_20260209` 版本用 code execution 内部 filter 结果

## 出现来源

_22 summaries reference this entity_ ——
- [[code-execution-tool--at]] / [[tool-use-overview--at]] / [[tool-reference--at]] / [[tool-combinations--at]]
- [[web-search-tool--at]] / [[web-fetch-tool--at]] / [[bash-tool--at]] / [[text-editor-tool--at]]
- [[server-tools--at]] / [[manage-tool-context--at]]
- [[adaptive-thinking--bwc]] / [[api-and-data-retention--bwc]] / [[skills-guide--bwc]]
- [[claude-in-microsoft-foundry--bwc]]

## 相关

- [[Tool-use]] —— code execution 是 server-managed tool 之一
- [[Web-search-tool]] / [[Web-fetch-tool]] —— bundle 免费 + dynamic filtering 共生
- [[Bash-tool-API]] —— client-side 等价物（state 隔离）
- [[Text-editor-tool]] —— client-side 等价物
- [[Files-API]] —— 通过 `container_upload` 接入
- [[Skill]] —— code execution enables skills
- [[Enterprise-gateway]] —— 仅 Foundry 支持，Bedrock/Vertex 不支持
