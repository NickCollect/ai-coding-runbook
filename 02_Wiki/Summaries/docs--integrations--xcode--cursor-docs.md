---
type: summary
source: 01_Raw/docs.cursor.com/docs--integrations--xcode.md
source_url: https://cursor.com/docs/integrations/xcode
title: "Xcode 集成"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Xcode 26.3+ 内置 MCP server（通过 `xcrun mcpbridge`），让 Cursor Agent 直接访问 Xcode 项目，可读写文件、触发构建、运行测试、捕获 SwiftUI 预览和搜索 Apple 文档。

**前提条件**：macOS + Xcode 26.3+；付费 Cursor 计划；Xcode 中已打开项目；在 Xcode Settings → Intelligence → Model Context Protocol 启用 Xcode Tools。

**配置方式**（三选一）：
1. Cursor Settings → Features → MCP → Add New MCP Server（stdio，命令 `xcrun mcpbridge`）
2. 在 `~/.cursor/mcp.json` 添加 `{"xcode-tools": {"command": "xcrun", "args": ["mcpbridge"]}}`
3. CLI：`agent mcp add xcode-tools -- xcrun mcpbridge`

**20 个内置工具（5 类）**：
- **文件操作**：Read/Write/Update/Grep/Glob/LS/MakeDir/RM/MV
- **构建与测试**：BuildProject、GetBuildLog、RunAllTests/RunSomeTests、GetTestList
- **诊断**：ListNavigatorIssues、RefreshCodeIssuesInFile
- **智能**：RenderPreview（SwiftUI 截图）、DocumentationSearch（Apple 文档语义搜索）、ExecuteSnippet（Swift 代码片段执行）
- **工作区**：XcodeListWindows

**典型流程**：在 Cursor 描述任务 → Agent 搜索/读取代码 → 编辑文件 → BuildProject 验证 → RunSomeTests → RenderPreview 确认 UI。全程不离开 Cursor。
