---
type: summary
source: 01_Raw/docs.cursor.com/docs--hooks.md
source_url: https://cursor.com/docs/hooks
title: "Hooks（Agent 循环钩子）"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Hooks 是在 Agent 循环指定阶段前后运行的自定义脚本，通过 stdio JSON 双向通信，可观察、阻止或修改 Agent 行为，同时适用于 Cursor Agent 和 Tab 内联补全。

**典型用途**：编辑后自动格式化、添加审计日志、扫描 PII/密钥、拦截高风险操作（如 SQL 写入）、控制子 Agent 生成、在会话开始注入上下文。

**Agent 支持的 Hook 事件**：`sessionStart/End`、`preToolUse/postToolUse/postToolUseFailure`、`subagentStart/Stop`、`beforeShellExecution/afterShellExecution`、`beforeMCPExecution/afterMCPExecution`、`beforeReadFile/afterFileEdit`、`beforeSubmitPrompt`、`preCompact`、`stop`、`afterAgentResponse/afterAgentThought`。Tab 专属：`beforeTabFileRead`、`afterTabFileEdit`。

**Hook 类型**：Command-based（Shell 脚本，stdin/stdout JSON，exit 2 阻止操作）；Prompt-based（LLM 评估自然语言条件）。

**配置文件位置与优先级**（高→低）：Enterprise（系统级）→ Team（云端分发，Enterprise 专属）→ Project（`.cursor/hooks.json`）→ User（`~/.cursor/hooks.json`）。

**关键配置选项**：`timeout`（超时）、`loop_limit`（stop/subagentStop 最多循环次数，默认 5）、`failClosed`（失败时阻断而非放行，安全关键场景建议开启）、`matcher`（按工具类型/命令内容过滤触发条件）。

**合作伙伴生态**：MintMCP、Oasis Security、Runlayer（MCP 治理）；Corridor、Semgrep（代码安全）；Endor Labs（依赖安全）；Snyk（Agent 安全）；1Password（密钥管理）。
