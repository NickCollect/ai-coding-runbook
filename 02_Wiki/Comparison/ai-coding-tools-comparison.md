---
name: AI 编程工具对比
type: comparison
topics: [Claude Code, Cursor, Codex CLI, AI IDE]
created_at: 2026-05-06
---

# AI 编程工具对比：Claude Code vs Cursor vs Codex CLI

## 安装与入口

| 维度 | Claude Code | Cursor | Codex CLI |
|---|---|---|---|
| 安装方式 | `npm i -g @anthropic-ai/claude-code` | 下载 Desktop App | `npm i -g @openai/codex` / `brew install --cask codex` |
| 主要入口 | 终端 `claude` / Desktop App | IDE 窗口（Cmd+I Agent / Cmd+K） | 终端 `codex` / `codex app` |
| Cloud 入口 | 无（本地） | cursor.com/agents / Slack / GitHub | chatgpt.com/codex（Codex Web，独立产品） |
| IDE 集成 | VS Code extension（有限）/ 终端 | 原生 IDE | VS Code / Cursor / Windsurf 插件 |

## Context 系统

| 维度 | Claude Code | Cursor | Codex CLI |
|---|---|---|---|
| 项目指令文件 | `CLAUDE.md`（多层目录）| `.cursor/rules/` 或 `AGENTS.md` | `AGENTS.md` |
| 指令触发方式 | 始终加载（CLAUDE.md）| Always/Intelligent/Glob/Manual 四种 | 始终加载 |
| 向量检索 | ❌ | ✅ Codebase Index | ❌ |
| 动态 context | MCP server | MCP server + Codebase Index | ❌ |
| 团队共享规则 | CLAUDE.md 版控 | Team Rules（dashboard 管理） | AGENTS.md 版控 |

## Hooks 事件对比

| 事件 | Claude Code | Cursor | Codex CLI |
|---|---|---|---|
| 会话生命周期 | Stop, Notification | sessionStart, sessionEnd, stop | ❌ |
| 工具前后 | PreToolUse, PostToolUse | preToolUse, postToolUse, postToolUseFailure | ❌ |
| Shell 执行 | PreToolUse (Bash) | beforeShellExecution, afterShellExecution | ❌ |
| 文件操作 | PreToolUse (Edit/Write) | beforeReadFile, afterFileEdit | ❌ |
| MCP 调用 | ❌ | beforeMCPExecution, afterMCPExecution | ❌ |
| Subagent | ❌ | subagentStart, subagentStop | ❌ |
| Tab 专用 | ❌ | beforeTabFileRead, afterTabFileEdit | ❌ |
| 跨工具兼容 | Claude Code 格式 | 兼容 Claude Code hooks.json | ❌ |

## 权限与安全模型

| 维度 | Claude Code | Cursor | Codex CLI |
|---|---|---|---|
| 自主模式 | bypassPermissions / default / acceptEdits | 本地 Agent（继承权限）+ hooks 拦截 | Full Auto / Auto Edit / Suggest Only |
| 沙箱 | Docker 可选 / 无默认沙箱 | Cloud Agents（完全隔离 VM） | macOS Sandbox（本地） |
| 网络隔离 | `--disableNetworking` flag | Cloud Agents 隔离 / 本地无 | 可选隔离 |
| 企业级强制 | ❌（需 hooks 自建） | Enterprise Managed Hooks | ❌ |

## MCP 支持

| 维度 | Claude Code | Cursor | Codex CLI |
|---|---|---|---|
| 作为 MCP Client | ✅ | ✅ | ❌ |
| 传输方式 | stdio / SSE | stdio / SSE / Streamable HTTP | — |
| MCP Apps（交互 UI）| ❌ | ✅ | — |
| Marketplace | ❌ | ✅（cursor.directory） | — |
| OAuth 认证 | 手动 | ✅（SSE/HTTP 原生支持） | — |

## 多 Agent / 并行

| 维度 | Claude Code | Cursor | Codex CLI |
|---|---|---|---|
| 并行机制 | Subagents（Task tool，本地） | Cloud Agents（云端，无限并行）| ❌ |
| 触发方式 | 代码内调用 Task | Cursor Web / Slack / GitHub / Linear / API | — |
| 工作产物 | 直接修改文件 | Push 独立分支 + PR | — |
| 机器控制 | ❌ | ✅（Cloud Agents：browser + desktop）| ❌ |

## 模型支持

| Claude Code | Cursor | Codex CLI |
|---|---|---|
| Claude Sonnet 4.5 / Opus 4.7（默认）| Claude 4.6/4.7, GPT-5.5, Gemini 3.1, Grok, Cursor Composer | Codex（基于 GPT-4o / o4-mini）|

## 计费模式

| Claude Code | Cursor | Codex CLI |
|---|---|---|
| API token 按量 / Max 订阅（含 CC）| Seat 订阅 + Max Mode premium | ChatGPT Plus/Pro/Team 计划 / API key |

## 出现来源

- [[docs--agent--overview--cursor-docs]]
- [[docs--rules--cursor-docs]]
- [[docs--hooks--cursor-docs]]
- [[docs--mcp--cursor-docs]]
- [[docs--cloud-agent--cursor-docs]]
- [[README--codex-openai]]
- [[Hooks]] — Claude Code hooks
- [[MCP-server]]
