---
type: summary
source: 01_Raw/code.claude.com/docs/en/overview.md
source_url: https://code.claude.com/docs/en/overview
title: "Claude Code — Overview"
summarized_at: 2026-05-05
entities_referenced:
  - Agent-SDK.md
  - Hooks.md
  - Headless-mode.md
concepts_referenced:
  - Agentic-loop.md
  - Tool-use.md
  - Channel.md
---

Claude Code 是 Anthropic 推出的 AI 驱动编程助手，能够读取代码库、编辑文件、执行命令，并与开发工具深度集成。它可在终端（Terminal CLI）、IDE 插件（VS Code / JetBrains）、桌面应用（Desktop app）、浏览器（Web）等多种环境中使用。

## 安装方式

- **macOS/Linux/WSL**：`curl -fsSL https://claude.ai/install.sh | bash`
- **Windows PowerShell**：`irm https://claude.ai/install.ps1 | iex`
- **Homebrew**：`brew install --cask claude-code`（不自动更新）
- **WinGet**：`winget install Anthropic.ClaudeCode`（不自动更新）
- 也支持通过 apt / dnf / apk 在 Debian、Fedora、RHEL、Alpine 上安装

Native 安装方式会在后台自动更新至最新版本。

## 支持平台

| 平台 | 说明 |
|------|------|
| Terminal CLI | 全功能命令行，直接在终端中编辑文件、执行命令 |
| VS Code | 扩展形式，支持 inline diff、@-mention、对话历史 |
| JetBrains | 插件形式，适用于 IntelliJ、PyCharm、WebStorm 等 |
| Desktop App | 独立桌面应用（macOS / Windows），支持多 session 并行 |
| Web | 浏览器端，无需本地安装，支持长时间异步任务 |
| Slack | 在 Slack 频道中 @Claude，可接收 bug 报告并产出 PR |
| GitHub Actions / GitLab CI | CI/CD 中自动化代码审查和 issue triage |

认证支持：Claude 订阅（Pro/Max/Team/Enterprise）、Anthropic Console（API key）、Amazon Bedrock、Google Vertex AI、Microsoft Foundry 三方云服务商。

## 核心能力

- **自动化繁琐任务**：写测试、修 lint 错误、解决 merge conflict、更新依赖、写 release notes
- **构建功能 / 修复 Bug**：用自然语言描述需求，Claude 自动规划、跨文件写代码并验证结果
- **Git 操作**：stage 变更、写 commit message、创建分支、开 PR；也支持 GitHub Actions / GitLab CI/CD 自动化
- **MCP 集成**：通过 Model Context Protocol 连接 Google Drive、Jira、Slack、自定义工具等外部数据源
- **CLAUDE.md / Skills / Hooks**：持久化编码规范和架构决策；Skills 打包可复用工作流；Hooks 在 Claude 行动前后执行 shell 命令
- **Agent Teams / Agent SDK**：派生多个并行子 agent；或通过 Agent SDK 构建完全自定义的 agent
- **CLI 管道**：支持 Unix 哲学的 pipe 操作，可与 CI/CD 链式组合
- **定时任务**：Routines（托管基础设施）、Desktop scheduled tasks、`/loop` 命令

## 跨平台联动

所有平台共用同一个 Claude Code 引擎，CLAUDE.md 文件、设置和 MCP servers 在各平台间通用。支持 Remote Control（从手机继续本地会话）、Dispatch（从手机发起任务）、`--teleport` 将 web 任务拉回终端等跨设备工作流。
