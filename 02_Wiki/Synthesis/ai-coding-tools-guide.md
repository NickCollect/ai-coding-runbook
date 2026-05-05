---
name: AI 编程工具全景指南
type: synthesis
topics: [Claude Code, Cursor, Codex CLI, AI IDE, 编程工具]
created_at: 2026-05-06
---

# AI 编程工具全景指南

> **适用场景**：你同时使用 Claude Code desktop、Codex CLI/desktop、Cursor 三个工具，本文帮你厘清各工具的定位、核心能力与协同方式。

---

## 一、三个工具的定位矩阵

| 维度 | Claude Code | Cursor | Codex CLI |
|---|---|---|---|
| **形态** | 终端 CLI / desktop app | VS Code-based IDE | 终端 CLI / desktop app |
| **主要厂商** | Anthropic | Cursor Inc | OpenAI |
| **核心模型** | Claude 系列（可选 Sonnet/Opus） | 多模型（Claude/GPT/Gemini/Cursor Composer） | Codex 模型（基于 GPT-4o/o4-mini） |
| **运行环境** | 本地 + Sandbox | 本地 IDE + Cloud Agents | 本地 Sandbox |
| **主要场景** | 自主完成复杂任务、CLI 工作流 | 代码补全 + Agent 任务 + 团队协作 | 开源、低摩擦本地编程 agent |
| **Context 来源** | CLAUDE.md + hooks + MCP + 文件 | Rules + MCP + Codebase Index + 文件 | README/AGENTS.md + shell env |
| **Hooks/扩展** | hooks.json（Claude Code 原生） | hooks.json（兼容 Claude Code 格式） | 暂无 hook 机制 |
| **MCP 支持** | ✅ 原生（server-side） | ✅ 原生（stdio/SSE/HTTP） | ❌ 暂无 |
| **多 Agent 并行** | Subagents（Task tool） | Cloud Agents（多并行） | 无内置并行机制 |
| **权限模型** | Permission mode（bypassPermissions/default/strict） | 通过 hooks 控制 / Cloud 隔离 | 全自动/询问/仅手动三档 |
| **计费** | 按 token（API key 或 Max 订阅） | 按 seat（请求量 + Max Mode premium） | 按 ChatGPT 计划 / API key |

---

## 二、核心能力深度对比

### Context 管理

**Claude Code**：
- `CLAUDE.md` 作为项目级持久指令（每个目录可有独立 CLAUDE.md）
- Hooks 在特定事件注入 context（如 `sessionStart`、`preToolUse`）
- `/compact` 和 Compaction API 管理长会话 context 压缩
- MCP 服务器可动态提供 context

**Cursor**：
- Rules（`.cursor/rules/`）= Claude Code 的 hooks + CLAUDE.md 混合体
  - `Always Apply`：类似 CLAUDE.md
  - `Apply Intelligently`：按描述智能注入
  - `Apply to Specific Files`：按文件 glob 注入
  - `Apply Manually`：@-mention 触发
- `AGENTS.md` = Cursor 的轻量 CLAUDE.md 替代
- Codebase Index（语义向量索引）：在 context 受限时自动检索相关代码
- Team Rules（企业级，跨 seat 共享）

**Codex CLI**：
- `AGENTS.md` 作为项目指令（自动读取根目录和父目录）
- 读取 shell 环境变量（gitconfig、编辑器等）
- 无向量索引，依赖模型的长 context 能力

### Hooks / 扩展性

**Claude Code**（原生）：
- `PreToolUse`、`PostToolUse`、`Stop`、`Notification` 四类事件
- JSON-in/JSON-out stdio 通信
- 可 block（exit 2）、修改 tool 调用、中止 session

**Cursor**（兼容 Claude Code + 扩展）：
- **完全兼容** Claude Code 的 `hooks.json` 格式（Third Party Hooks）
- 额外扩展：`beforeShellExecution`、`subagentStart/Stop`、`beforeTabFileRead`、`afterTabFileEdit` 等 Tab 专用 hook
- Cloud Agents 也运行 repo/team/enterprise hooks

**Codex CLI**：
- 暂无 hook 机制，通过 `AGENTS.md` 指令影响行为

### 沙箱 / 权限控制

**Claude Code**：
- Permission modes：`default`（按类询问）、`acceptEdits`、`bypassPermissions`（完全自动）
- 网络访问：`--disableNetworking` flag 隔离
- Docker 沙箱可选

**Cursor**：
- 本地 Agent：继承用户权限，通过 hooks 拦截危险操作
- Cloud Agents：完全隔离 VM，clone repo 并 push 结果
- 企业级：可配置 managed hooks 强制合规

**Codex CLI**：
- `Full Auto` / `Auto Edit` / `Suggest Only` 三档自主模式
- macOS Sandbox（沙盒化 shell）本地执行
- 网络隔离可选

---

## 三、MCP 集成

### Claude Code MCP
Claude Code 本身是 MCP client，可以连接任意 MCP server；同时通过 `claude-code-action` 也可作为 GitHub Actions 的 MCP server 被其他工具调用。

### Cursor MCP
支持三种传输：`stdio`（本地进程）、`SSE`（远程服务）、`Streamable HTTP`（远程服务）。支持 Tools、Prompts、Resources、Roots、Elicitation、MCP Apps（交互 UI）六类能力。配置文件：`mcp.json`（项目级）或 `~/.cursor/mcp.json`（全局）。

### 在 Cursor 里使用 Claude Code 作为 MCP Server
Cursor 可以将 Claude Code 的工具通过 MCP 接入，让 Cursor Agent 能调用 Claude Code 的 Bash、Edit、Read 等能力。配置方式：在 `mcp.json` 中添加 `claude-code` server。

---

## 四、Cloud Agents（Cursor 独有）

Cursor Cloud Agents 在云端隔离 VM 中运行，与本地环境完全分离：

- **触发入口**：Cursor Web、Desktop、Slack `@cursor`、GitHub PR/Issue `@cursor`、Linear `@cursor`、API
- **工作模式**：clone repo → 独立分支工作 → push + PR
- **并行能力**：无数量限制，适合大规模并行任务
- **模型**：始终使用 Max Mode，支持所有 Cursor 模型
- **差异化**：计算机控制（browser/desktop）、MCP 支持、Enterprise hooks

---

## 五、工具选型建议

| 场景 | 推荐工具 | 原因 |
|---|---|---|
| 复杂多步 CLI 任务，需要 hooks/MCP | Claude Code | 最成熟的 hooks 体系，MCP 原生集成 |
| 日常代码补全 + 小任务 | Cursor Tab | 最低摩擦，不需要配置 |
| 中等复杂 agent 任务（在 IDE 里） | Cursor Agent | Rules 系统强，IDE 集成好 |
| 大规模并行任务，无需本机在线 | Cursor Cloud Agents | 唯一真正云端并行方案 |
| 开源项目贡献，轻量无配置 | Codex CLI | 安装简单（npm/brew），开箱即用 |
| 需要 OpenAI 最新模型优先支持 | Codex CLI | OpenAI 官方工具，模型优先 |
| 团队统一 AI 工作流 | Cursor（Team Rules + Enterprise hooks） | 跨 seat 规则/hooks 集中管理 |

---

## 六、协同工作流

### 工作流 A：Cursor + Claude Code MCP
在 Cursor 里配置 Claude Code 为 MCP server，让 Cursor Agent 能用 Claude Code 的文件操作能力。适合在 IDE 里需要 Claude Code 特定工具的场景。

### 工作流 B：Claude Code 主导 + Cursor Tab 辅助
用 Claude Code 完成架构级任务（hooks/MCP），用 Cursor Tab 做行级补全。两者互不干扰，Cursor 同样能读 `CLAUDE.md` 的 `AGENTS.md` 兼容格式。

### 工作流 C：Cloud Agent 批量 + 本地审查
用 Cursor Cloud Agents 并行处理多个 PR，在本地 IDE 做 Agent Review（diff 审查）。

### 工作流 D：Codex CLI 快速迭代
对开源仓库做快速实验，Codex CLI `Full Auto` 模式直接跑，不需要任何配置文件。

## 出现来源

- [[docs--agent--overview--cursor-docs]] — Cursor Agent 核心机制
- [[docs--rules--cursor-docs]] — Cursor Rules 系统
- [[docs--hooks--cursor-docs]] — Cursor Hooks
- [[docs--mcp--cursor-docs]] — Cursor MCP 集成
- [[docs--cloud-agent--cursor-docs]] — Cursor Cloud Agents
- [[README--codex-openai]] — OpenAI Codex CLI
- [[github-actions]] — Claude Code GitHub Actions
- [[Hooks]] — Claude Code hooks entity
- [[MCP-server]] — MCP 协议 entity
