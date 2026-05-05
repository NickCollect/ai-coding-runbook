---
type: summary
source: 01_Raw/code.claude.com/docs/en/quickstart.md
source_url: https://code.claude.com/docs/en/quickstart
title: "Claude Code — Quickstart（终端 CLI）"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced:
  - Agentic-loop.md
---

Claude Code 的 Quickstart 指南，带领用户在几分钟内开始使用 AI 编程助手，覆盖从安装到第一次代码变更的完整流程。本页专注于终端 CLI 入口；Claude Code 也可在 Web、Desktop、VS Code、JetBrains、Slack、GitHub Actions 等环境中使用。

## 前置条件

- 终端 / 命令提示符
- 一个代码项目目录
- Claude 订阅（Pro、Max、Team 或 Enterprise）或 Anthropic Console 账号（API 预充值），也支持 Amazon Bedrock / Google Vertex AI / Microsoft Foundry

## 步骤一：安装

```bash
# macOS / Linux / WSL（推荐，自动更新）
curl -fsSL https://claude.ai/install.sh | bash

# Homebrew（不自动更新，需手动 brew upgrade claude-code）
brew install --cask claude-code

# WinGet（不自动更新）
winget install Anthropic.ClaudeCode
```

也支持 Debian / Fedora / RHEL / Alpine 通过 apt、dnf、apk 安装。

## 步骤二：登录

首次运行 `claude` 时会提示登录。支持账号类型：
- Claude Pro / Max / Team / Enterprise（推荐）
- Claude Console（API key + 预充值）
- 三方云服务商（Bedrock / Vertex AI / Foundry）

登录后凭证本地持久化，后续无需重复登录。用 `/login` 切换账号。

## 步骤三：启动会话

```bash
cd /path/to/your/project
claude
```

进入 Claude Code 欢迎界面，显示会话信息、最近对话、最新更新。输入 `/help` 查看命令，`/resume` 继续上次对话。

## 步骤四：探索代码库

```
what does this project do?
what technologies does this project use?
where is the main entry point?
explain the folder structure
```

Claude 会自动读取所需文件，无需手动添加上下文。

## 步骤五：第一次代码修改

```
add a hello world function to the main file
```

Claude Code 会：找到目标文件 → 展示建议改动 → 请求用户确认 → 执行修改。每次修改文件都会请求确认（可开启"接受全部"模式）。

## 步骤六：Git 操作

```
what files have I changed?
commit my changes with a descriptive message
create a new branch called feature/quickstart
show me the last 5 commits
help me resolve merge conflicts
```

## 步骤七：修复 Bug / 添加功能

```
add input validation to the user registration form
there's a bug where users can submit empty forms - fix it
```

Claude Code 会定位相关代码、理解上下文、实现方案、运行测试。

## 常用命令速查

| 命令 | 用途 |
|------|------|
| `claude` | 启动交互模式 |
| `claude "task"` | 执行一次性任务 |
| `claude -p "query"` | 单次查询后退出 |
| `claude -c` | 继续当前目录最近对话 |
| `claude -r` | 恢复历史对话 |
| `/clear` | 清空对话历史 |
| `/help` | 查看可用命令 |
| `exit` / Ctrl+D | 退出 |

## 新手技巧

- **具体描述**：避免"fix the bug"，改用"fix the login bug where users see a blank screen after entering wrong credentials"
- **分步拆解**：将复杂任务拆成多个步骤再描述
- **先让 Claude 探索**：修改前先 `analyze the database schema` 或类似的探索性提示
- **快捷键**：`?` 查看快捷键、`Tab` 命令补全、`↑` 历史命令、`/` 查看所有命令和 Skills
