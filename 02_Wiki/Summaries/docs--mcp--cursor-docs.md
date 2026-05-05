---
type: summary
source: 01_Raw/docs.cursor.com/docs--mcp.md
source_url: https://cursor.com/docs/mcp
title: "Model Context Protocol (MCP)"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

MCP（Model Context Protocol）使 Cursor 能连接外部工具和数据源，支持三种传输方式：stdio（本地单用户）、SSE（本地/远程多用户）、Streamable HTTP（本地/远程多用户）。

**支持的协议能力**：Tools、Prompts、Resources、Roots、Elicitation、Apps（交互式 UI 扩展）。MCP Apps 支持渐进增强，不支持 UI 的 host 仍可正常使用工具。

**安装方式**：Cursor Marketplace 一键安装（官方插件）；cursor.directory 社区插件；或手动编写 `mcp.json`。

**`mcp.json` 配置**：项目级放 `.cursor/mcp.json`，全局放 `~/.cursor/mcp.json`。支持 stdio（command + args + env）和远程（url + headers）两种格式，支持变量插值（`${env:NAME}`、`${workspaceFolder}` 等）。

**OAuth 支持**：远程服务器可配置静态 OAuth 凭证（CLIENT_ID/CLIENT_SECRET），固定 redirect URL 为 `cursor://anysphere.cursor-mcp/oauth/callback`。

**工具审批**：默认每次调用需审批；可开启 auto-run 自动执行；可通过 `~/.cursor/permissions.json` 配置白名单。

**图片支持**：MCP 工具可返回 base64 图片，Cursor 自动附加到 chat；若模型支持视觉则分析图片内容。

**调试**：Output panel → MCP Logs 查看连接/工具调用/错误信息；Settings → Features → MCP 可随时启用/禁用各服务器。
