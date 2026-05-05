---
type: summary
source: 01_Raw/docs.cursor.com/docs--cloud-agent--capabilities.md
source_url: https://cursor.com/docs/cloud-agent/capabilities
title: "Cloud Agent Capabilities"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Cloud Agent 运行在带完整桌面环境的独立 VM 中，具备计算机操控能力和 MCP 工具集成，并能自动修复 CI 失败。

**Computer Use（计算机使用）**：可用鼠标键盘控制桌面和浏览器，像人类开发者一样启动 dev server、在浏览器点击 UI 流程、验证改动正确性后再推 PR。

**Demos and Artifacts**：Agent 创建截图、视频、日志引用等制品附到 PR，方便审查者无需本地检出即可验证。可在 Cloud Agents dashboard 开启"Allow posting artifacts to GitHub"将制品嵌入 PR 描述（使用 unguessable 公开 URL）。

**MCP 工具**：通过 cursor.com/agents 的 MCP 下拉框添加和管理，支持 OAuth（每用户独立）。HTTP 传输（推荐）：工具调用通过后端代理，Agent 无法访问凭证；stdio 传输：服务器在 VM 内运行，Agent 可访问配置和环境变量。MCP 配置加密存储，敏感字段（env/headers/CLIENT_SECRET）不可读回。

**自动修复 CI 失败**：Cloud Agent 创建的 PR 上若 GitHub Actions CI 失败，自动尝试修复。跳过条件：人工推送了新 commit、发送了追加消息、基础 commit 上该 check 本已失败、已有 10 次 CI 修复尝试。可在 dashboard 或 PR 评论 `@cursor autofix off/on` 控制。
