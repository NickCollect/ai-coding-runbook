---
type: summary
source: 01_Raw/docs.cursor.com/docs--integrations--jetbrains.md
source_url: https://cursor.com/docs/integrations/jetbrains
title: "JetBrains 集成"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

通过 ACP（Agent Client Protocol）在 JetBrains IDE（IntelliJ、PyCharm、WebStorm 等）中使用 Cursor AI Agent，无需离开 JetBrains 工作环境。

**前提条件**：付费 Cursor 计划；JetBrains IDE 安装 AI Assistant 插件（2025.1+）。

**安装步骤**：打开 AI Chat 面板 → 在 agent provider 列表中选择"Add Agent from Registry" → 搜索"Cursor"并安装 → 认证 → 使用。

**提供的能力**：模型选择（可切换不同 frontier model）、代码库语义搜索、文件读写（变更直接反映在编辑器）、终端命令执行。

**工作原理**：JetBrains IDE 作为 ACP 客户端，Cursor Agent 作为服务端；发送 prompt 后，AI Chat 插件通过 ACP 转发给 Cursor Agent，Agent 处理后将编辑和命令流式返回 IDE。

**计费**：使用与 Cursor 订阅相同的按量定价。
