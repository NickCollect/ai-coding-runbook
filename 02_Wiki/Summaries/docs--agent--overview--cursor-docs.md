---
type: summary
source: 01_Raw/docs.cursor.com/docs--agent--overview.md
source_url: https://cursor.com/docs/agent/overview
title: "Cursor Agent 概述"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Cursor Agent 是能独立完成复杂编程任务的 AI 助手，通过 Cmd+I 在侧边栏访问。

**三大组成**：Instructions（系统提示 + Rules）、Tools（工具集）、Model（所选模型）。

**内置工具**：语义搜索（Semantic search）、文件/文件夹搜索、Web 搜索、Rules 获取、文件读写、Shell 命令执行、浏览器控制、图像生成、提问澄清。工具调用次数无限制。

**Checkpoints**：Agent 在重大修改前自动保存快照，可随时预览或恢复到历史状态，与 Git 独立存储，仅用于撤销 Agent 操作。

**排队消息（Queued messages）**：Agent 运行时可提前输入下一条指令排队等候。Enter 排队，Cmd+Enter 立即打断并发送。立即发送会将消息附加到最近的用户消息上即刻处理。
