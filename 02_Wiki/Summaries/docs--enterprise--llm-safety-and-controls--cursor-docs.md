---
type: summary
source: 01_Raw/docs.cursor.com/docs--enterprise--llm-safety-and-controls.md
source_url: https://cursor.com/docs/enterprise/llm-safety-and-controls
title: "Enterprise LLM 安全与控制"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

LLM 行为不可完全预测，需要结合确定性安全控制和非确定性引导机制共同管理 AI Agent 风险。

**安全控制（确定性）**：
- **终端命令限制**：默认每次命令需审批；auto-approval 有风险（可被 prompt injection 绕过），Enterprise 可配置白名单；白名单是尽力保护非安全边界
- **Enforcement Hooks**：在 prompt 提交前扫描 PII/API Key、文件读取前拦截敏感文件、代码生成后扫描安全漏洞/凭证、终端执行前阻断危险命令（附有 git 拦截和密钥检测的 Shell 脚本示例）
- **文件保护**：`.cursorignore` 从 AI 处理中排除文件（非安全边界，用户仍可手动读取）；`.cursor 目录保护`（Enterprise）防止 Agent 修改项目设置
- **浏览器 Origin 控制**（Enterprise）：限制 Agent 可访问的域名白名单
- **DLP 集成**：端点 DLP 监控 `*.cursor.sh` 流量；通过 Hooks 实现内联 DLP 或调用第三方 DLP API

**LLM 引导（非确定性）**：
- **Rules**：在上下文窗口中注入代码标准、架构模式、安全要求（User/Project/Team 三层）
- **Commands**：标准化可复用工作流（如 `/security-review`）
- **MCP**：向 Agent 提供公司文档/内部 API/知识库等额外上下文

**核心原则**：安全控制提供安全网，引导机制减少 Agent 首次尝试有问题操作的频率；两者必须结合使用。
