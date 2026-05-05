---
name: Cursor / Codex 实战工作流 QA
type: qa
topics: [Cursor, Codex CLI, Claude Code, AI IDE, 工作流]
created_at: 2026-05-06
---

# Cursor / Codex 实战工作流 Q&A

## 安装与配置

**Q: 三个工具分别怎么安装？**
- Claude Code：`npm i -g @anthropic-ai/claude-code`，首次运行 `claude` 完成 OAuth
- Cursor：从 cursor.com 下载 Desktop App 安装
- Codex CLI：`npm i -g @openai/codex` 或 `brew install --cask codex`，首次运行选择 ChatGPT 登录

**Q: 在 Cursor 里怎么配 Claude Code 的模型？**
Cursor 的 Agent 独立于 Claude Code，两者模型独立配置。Cursor 在 Settings → Models 选择模型（支持 Claude Sonnet/Opus）。Claude Code 在 `~/.claude/` 或环境变量配置。它们是两个独立 agent，不共享配置。

**Q: CLAUDE.md、AGENTS.md、.cursor/rules/ 三者关系是什么？**
- `CLAUDE.md`：Claude Code 原生项目指令，每次 session 自动加载
- `AGENTS.md`：通用 AI agent 指令格式，Claude Code 和 Cursor 都支持（Cursor 将其视为 `Always Apply` rule）
- `.cursor/rules/`：Cursor 专用，支持四种触发模式（Always/Intelligent/Glob/Manual）

**实践建议**：用 `CLAUDE.md`（symlink 到 `AGENTS.md`）存放项目级通用指令，`.cursor/rules/` 存放 Cursor 专用规则（如自定义 Tab 行为、UI 风格）。

---

## Hooks

**Q: Claude Code 的 hooks 在 Cursor 里能用吗？**
可以。Cursor 完全兼容 Claude Code 的 `hooks.json` 格式（通过 Third Party Hooks 机制）。把 `~/.cursor/hooks.json` 配置成 Claude Code 格式即可，Cursor 会自动识别。

**Q: Cursor Hooks 比 Claude Code Hooks 多了什么？**
Cursor 扩展了 Tab 专用 hooks：`beforeTabFileRead`、`afterTabFileEdit`，以及更细粒度的 `beforeShellExecution`、`beforeMCPExecution`、`subagentStart/Stop`。Claude Code 没有 Tab 机制，也没有 MCP 拦截 hook。

**Q: 怎么用 hooks 阻止危险的 shell 命令？**

Claude Code/Cursor 通用写法（`hooks.json`）：
```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Bash",
      "hooks": [{"type": "command", "command": "bash ~/.claude/hooks/block-dangerous.sh"}]
    }]
  }
}
```
脚本里检测 `rm -rf`、`sudo` 等，exit 2 阻止执行，exit 0 放行。

---

## MCP

**Q: 怎么在 Cursor 里配置 MCP server？**
创建 `.cursor/mcp.json`（项目级）或 `~/.cursor/mcp.json`（全局）：
```json
{
  "mcpServers": {
    "my-server": {
      "command": "node",
      "args": ["/path/to/server/index.js"]
    }
  }
}
```
支持 stdio（本地进程）、SSE、Streamable HTTP 三种传输方式。

**Q: Cursor 的 MCP 和 Claude Code 的 MCP 有什么区别？**
- Cursor 多支持 MCP Apps（交互式 UI 返回）和 Elicitation（server 主动问用户）
- Cursor 有官方 Marketplace（cursor.directory）和一键安装
- Cursor SSE/HTTP transport 原生支持 OAuth 认证
- Claude Code MCP 更聚焦于工具调用，UI 扩展较少

**Q: 能不能在 Cursor 里把 Claude Code 当 MCP server 用？**
可以。Claude Code 提供了 MCP server 模式，在 Cursor `mcp.json` 里配置 `claude-code` server，就能让 Cursor Agent 调用 Claude Code 的工具（Bash、Edit、Read 等）。这样可以在 Cursor IDE 里发挥 Claude Code 的工具能力。

---

## Cloud Agents（Cursor）

**Q: Cursor Cloud Agents 和本地 Agent 的主要区别？**
- Cloud Agents 在完全隔离的 VM 里运行，不需要本机联网
- 支持真正的并行（可以同时跑多个 agent）
- 通过 GitHub/GitLab 操作，产出 PR 而非直接修改本地文件
- 支持计算机控制（browser、desktop）
- 始终使用 Max Mode 模型

**Q: 怎么从 GitHub PR 触发 Cursor Cloud Agent？**
在 PR 评论里写 `@cursor [任务描述]`，Cursor 会自动 fork 分支、完成任务、提交新 commit。需要先在 Settings 里连接 GitHub 仓库。

**Q: Cloud Agents 能用 MCP 吗？**
可以。Cloud Agents 支持 MCP server，可以连接外部数据库、API、第三方服务。在项目的 `mcp.json` 配置即可，Cloud Agent 在 VM 里会加载。

---

## Codex CLI

**Q: Codex CLI 和 Claude Code 的最大区别是什么？**
- Codex CLI 使用 OpenAI 模型，Claude Code 使用 Anthropic 模型
- Codex CLI 安装极简（一行 npm），无需 API 配置（可用 ChatGPT 账号）
- Codex CLI 暂无 hooks 和 MCP 机制，扩展性弱于 Claude Code
- Codex CLI 有 macOS 原生沙箱（shell 层面），Claude Code 需要额外配置 Docker 沙箱
- Claude Code 的 CLAUDE.md 多层目录继承更灵活

**Q: Codex CLI 的三种自主模式有什么区别？**
- `Full Auto`（`--full-auto` / `-y`）：完全自动，无需确认，适合 CI/脚本
- `Auto Edit`（默认）：可自动读写文件，但 shell 命令需确认
- `Suggest Only`（`--suggest-only`）：只建议，所有操作需手动确认

**Q: 怎么让 Codex CLI 读取项目指令？**
在项目根目录创建 `AGENTS.md`，Codex 启动时自动读取（同时读取父目录的 AGENTS.md）。这和 Claude Code 的 `CLAUDE.md` 机制类似，但 Codex 用 `AGENTS.md` 作为文件名。

---

## 选型与协同

**Q: 我应该在什么时候用 Claude Code，什么时候用 Cursor Agent？**
- 需要 hooks 自动化（格式化、安全检查、日志）→ Claude Code 或 Cursor（两者 hooks 兼容）
- 需要 MCP 扩展接入外部系统 → 两者均可，Cursor 的 MCP Apps 更丰富
- 需要在 IDE 里写代码同时有 AI 辅助 → Cursor（Tab 补全 + Agent 在一个窗口）
- 需要大规模并行任务（多 PR 同时处理）→ Cursor Cloud Agents
- 纯 CLI 工作流，不需要 IDE → Claude Code 或 Codex CLI

**Q: 三个工具可以同时开着用吗？**
可以。常见组合：Cursor 做 IDE（Tab 补全 + 小任务 Agent），Claude Code 在另一个终端做复杂任务（hooks/MCP 驱动），互不干扰。Codex CLI 可以在第三个窗口做快速实验。

**Q: 怎么在多工具间共享项目知识？**
用 `AGENTS.md`（Cursor + Codex 都认识）放通用指令，`CLAUDE.md` symlink 到 `AGENTS.md` 保证 Claude Code 也读取。Cursor 专用规则放 `.cursor/rules/`。这样一份文档同时服务三个工具。

## 出现来源

- [[docs--agent--overview--cursor-docs]]
- [[docs--rules--cursor-docs]]
- [[docs--hooks--cursor-docs]]
- [[docs--mcp--cursor-docs]]
- [[docs--cloud-agent--cursor-docs]]
- [[README--codex-openai]]
- [[ai-coding-tools-guide]]
- [[ai-coding-tools-comparison]]
