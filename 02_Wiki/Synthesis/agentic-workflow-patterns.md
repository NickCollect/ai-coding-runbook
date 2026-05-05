---
name: Agentic 工作流模式
type: synthesis
created: 2026-05-05
sources:
  - 01_Raw/platform.claude.com/docs/en/managed-agents/overview.md
  - 01_Raw/platform.claude.com/docs/en/managed-agents/multi-agent.md
  - 01_Raw/platform.claude.com/docs/en/agents-and-tools/agent-skills/overview.md
  - 01_Raw/platform.claude.com/docs/en/agents-and-tools/tool-use/overview.md
  - 01_Raw/code.claude.com/docs/en/agent-sdk/subagents.md
  - 01_Raw/code.claude.com/docs/en/agent-sdk/hooks.md
  - 01_Raw/code.claude.com/docs/en/agent-sdk/skills.md
  - 01_Raw/platform.claude.com/docs/en/intro.md
---

# Agentic 工作流模式

## 概览

本文梳理基于 Anthropic 文档（2026-05-04 抓取）的 agentic 工作流核心模式，包括 Messages API 与 Claude Managed Agents 两条路径下的常见架构选择。

---

## 模式总览

| 模式名 | 适用场景 | 关键组件 | 主要局限 |
|---|---|---|---|
| **单 Agent Loop（Messages API）** | 自定义控制流、细粒度工具调用、原型开发 | Messages API + client 自管理循环；`stop_reason: tool_use` 触发 | 需自己实现 agent loop、沙箱、工具执行层 |
| **Claude Managed Agents（单 session）** | 长时运行任务（分钟到小时级）、无需自建基础设施 | Session API + 内置工具（Bash / 文件操作 / Web search / MCP）+ 托管容器 | Research Preview 阶段；灵活度低于自建 |
| **Subagent 并行（Claude Code SDK）** | 可分解为多个独立子任务、需上下文隔离 | `agents` 参数 / `.claude/agents/` 文件 + `query()` 并发执行 | 每个 subagent 独立 context，无法共享中间状态；仅通过最终消息汇报结果 |
| **Multiagent Pipeline（Managed Agents）** | orchestrator 协调多专门 agent 分工（code review / testing / research） | `callable_agents` + `agent_toolset_20260401` + 线程隔离 session | Research Preview；各 agent 工具和 context 不共享 |
| **Skill 调用** | 复用领域专业知识、减少重复 system prompt；document 处理等标准化任务 | `Agent Skills`（filesystem-based YAML + 脚本）+ 三级渐进加载 | 依赖 VM 文件系统环境；必须在支持 Skills 的平台（Managed Agents / Claude Code）运行 |
| **MCP Tool 调用** | 连接外部系统（数据库 / API / 文件系统 / 专有工具） | MCP server + `mcp-connector`；client 侧或 server 侧连接 | 需部署和维护 MCP server；目前每个 session 工具数有上限 *需确认* |

**数据来源：**
- Messages API vs Managed Agents：`managed-agents/overview.md` 表格
- Multiagent / callable_agents：`managed-agents/multi-agent.md`
- Subagent 并行：`code.claude.com/docs/en/agent-sdk/subagents.md`
- Skills 三级加载：`agents-and-tools/agent-skills/overview.md`
- Tool use 基本流程：`agents-and-tools/tool-use/overview.md`

---

## 决策树

```
任务是否需要自定义控制流 / 精细工具集成？
├── 是 → Messages API 路径
│   ├── 任务是否可分解为独立子任务？
│   │   ├── 是，且子任务可并行 → Claude Code SDK subagent 并行
│   │   │       定义 agents: [] 参数 + 各子任务 description，让 Claude 自动委托
│   │   └── 否，单线程已够 → 单 agent loop（自管理 stop_reason: tool_use 循环）
│   └── 是否需要跨对话复用专业知识？
│       └── 是 → 在 Skills 中封装（.claude/agents/ 或 API Skills）
│
└── 否 → 是否可接受 Research Preview / 托管基础设施？
    ├── 是 → Claude Managed Agents 路径
    │   ├── 是否需要多专门 agent 协作？
    │   │   ├── 是 → Multiagent session（callable_agents）
    │   │   └── 否 → 单 session（Managed Agents + 内置工具）
    │   └── 是否需要专用领域技能？
    │       └── 是 → 挂载 Agent Skills（PowerPoint / Excel / PDF 或自定义）
    └── 否 → 等待 Managed Agents GA 或评估 Messages API 路径
```

**补充**：外部系统集成始终可以通过 MCP server 叠加在上述任何路径上（`mcp-connector`）。

---

## Claude Code 专用模式

以下模式基于 `01_Raw/code.claude.com/docs/en/agent-sdk/` 文档：

### Hooks — 拦截和控制 agent 行为

Hooks 是注册在 agent 生命周期事件上的回调，用于安全控制、审计和输入/输出转换。

**可用事件（来自 hooks.md）：**
- `PreToolUse`：工具调用前触发；可 `deny`（阻止）、`allow`（放行）或修改输入
- `PostToolUse`：工具调用后触发；可 inject 上下文到对话
- 其他：session 开始/停止、subagent 启动/停止、agent idle 等（*需确认* 完整列表）

**典型 hook 用途：**
- 阻止危险操作（如写入 `.env` 文件）
- 合规审计 — 记录每次工具调用
- 数据清洗 — 注入凭证、重定向路径
- 人工审批门控 — 敏感操作前等待人工确认

**配置方式**：通过 `options.hooks` 参数（代码注册）或 settings 文件（shell command hooks，当 `settingSources` / `setting_sources` 启用时自动加载）。

### Skills — 可复用域专业知识

Skills（`agent-sdk/skills.md`）是 filesystem-based 的模块，封装指令、元数据和可选资源（脚本、模板）。

**三级渐进加载（来自 agent-skills/overview.md）：**
1. **Level 1 — Metadata（始终加载）**：YAML frontmatter（name / description / trigger 等），用于发现
2. **Level 2 — Instructions（按需加载）**：详细步骤指令，触发时加载
3. **Level 3 — Resources（执行时加载）**：脚本、模板等，实际运行时才消耗 context

**最佳适用场景：**
- 跨多个对话的标准化工作流（PowerPoint 生成、PDF 分析等）
- 组合多个 Skill 构建复杂 pipeline（Skills 可 compose）

### MCP — 外部工具接入

通过 `mcp-connector` 或 remote MCP server 连接外部系统。在 Claude Code 中：
- 支持 local MCP server（`code.claude.com/docs/en/mcp.md`）
- `tools` 参数中声明 MCP server；Claude 自动选择工具

### Subagent 并行模式

来自 `code.claude.com/docs/en/agent-sdk/subagents.md`：

| 方式 | 说明 |
|---|---|
| **代码声明** | `query()` 的 `agents` 参数，推荐用于 SDK 应用 |
| **文件声明** | `.claude/agents/*.md` 文件，可被 Claude Code CLI 自动发现 |
| **内置通用 subagent** | `general-purpose` 内置 agent，Claude 可随时调用无需显式定义 |

**Subagent 原则（来自 subagents.md）：**
- 每个 subagent 独立 context，中间 tool call 不污染 parent；仅最终消息返回
- 多 subagent 可并发运行，极大缩短并行工作流耗时
- 可给每个 subagent 限制特定工具集（如只读 subagent）

### Hook + Skill + MCP 组合建议

| 场景 | 推荐组合 |
|---|---|
| 自动化代码审查 | subagent（style-checker + security-scanner 并行）+ Hook（PreToolUse 限制写权限） |
| 文档批量处理 | Skill（PDF/Word/Excel）+ MCP（外部存储系统）|
| 长任务安全加固 | Hook（PostToolUse 审计日志）+ Hook（PreToolUse 人工审批敏感操作） |
| 多系统数据集成 | MCP server（数据库 / API）+ Managed Agents session（内置 web search） |
