---
type: summary
source: 01_Raw/docs.cursor.com/docs--cloud-agent--best-practices.md
source_url: https://cursor.com/docs/cloud-agent/best-practices
title: "Cloud Agent 最佳实践"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

提升 Cloud Agent 运行可靠性的四条核心建议：

1. **先配置环境**：用 Cloud Agent Setup 让 Cursor 有正确配置的开发环境，就像人类开发者需要本地环境一样。

2. **确保 Agent 能访问所需资源**：运行前验证密钥（通过 Secrets tab）、网络出口控制（白名单必要 URL）、本地可测试性（Agent 和人类开发者一样难以测试在 VM 里跑不起来的服务）。

3. **用 Skills 和 AGENTS.md 配置 Agent**：把 Agent 视为聪明但缺乏上下文的开发者，给它所需的上下文。例如 Cursor 内部的 agents.md 列出常用微服务的运行调试技巧，各 Skill 包含特定服务的深度调试指南，明确说明何时使用。

4. **给 Agent 合适的工具**：Agent 的能力上限来自它能访问的工具，建议通过 MCP 创建自定义工具，使 Agent 有与人类开发者相同的系统访问权。工具设计要根据 Agent 的实际使用方式迭代优化（如自定义 CLI 替代 package.json 命令，避免 Agent 忘记参数或被噪声日志分心）。
