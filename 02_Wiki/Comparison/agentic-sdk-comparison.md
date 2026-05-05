---
name: Agentic Framework 跨厂商对比
type: comparison
created: 2026-05-05
vendors: [Claude, OpenAI, Gemini]
sources:
  - 01_Raw/code.claude.com/docs/en/agent-sdk/overview.md
  - 01_Raw/code.claude.com/docs/en/agent-sdk/subagents.md
  - 01_Raw/code.claude.com/docs/en/agent-sdk/sessions.md
  - 01_Raw/docs.openai.com/docs/guides/agents.md
  - 01_Raw/docs.openai.com/docs/guides/agents/quickstart.md
  - 01_Raw/docs.openai.com/docs/guides/agents/orchestration.md
  - 01_Raw/docs.openai.com/docs/guides/agents/running-agents.md
  - 01_Raw/ai.google.dev/gemini-api/docs/agents.md
---

# Agentic Framework 跨厂商对比

本文对比 Claude Agent SDK、OpenAI Agents SDK、Gemini 三套 agentic 框架的核心机制。

---

## 一、Claude Agent SDK

来源：`01_Raw/code.claude.com/docs/en/agent-sdk/overview.md`、`subagents.md`、`sessions.md`

> 原名 Claude Code SDK，已改名为 Claude Agent SDK（迁移指南：`/en/agent-sdk/migration-guide`）。

**定位**：在开发者自有进程中运行 agent loop，内置与 Claude Code 相同的工具集和上下文管理。

### 安装

```bash
npm install @anthropic-ai/claude-agent-sdk   # TypeScript
pip install claude-agent-sdk                 # Python
export ANTHROPIC_API_KEY=your-api-key
```

TypeScript SDK 自带平台原生 Claude Code binary，无需单独安装。支持 Bedrock / Vertex / Azure（环境变量切换）。

### 核心 API

```python
from claude_agent_sdk import query, ClaudeAgentOptions

async for message in query(
    prompt="Find and fix the bug in auth.py",
    options=ClaudeAgentOptions(allowed_tools=["Read", "Edit", "Bash"]),
):
    print(message)
```

`query()` 返回 async iterator，消息类型包括：`AssistantMessage`、`ToolUseBlock`、`ToolResultBlock`、`ResultMessage`（最终结果）。

### 内置工具

| 工具 | 用途 |
|------|------|
| Read / Write / Edit | 文件读写精确编辑 |
| Bash | 终端命令、脚本、git |
| Glob / Grep | 文件搜索 / 内容搜索 |
| WebSearch / WebFetch | 网络搜索 / 页面抓取 |
| Monitor | 监听后台脚本、逐行响应 |
| AskUserQuestion | 带选项的用户交互 |

### Subagents（子智能体）

来源：`01_Raw/code.claude.com/docs/en/agent-sdk/subagents.md`

三种定义方式：
1. **Programmatic**（推荐）：`agents={"name": AgentDefinition(...)}` 参数
2. **Filesystem-based**：`.claude/agents/*.md` 文件（SDK 启动时加载）
3. **Built-in general-purpose**：无需定义，`Agent` 在 `allowedTools` 中即可调用

```python
from claude_agent_sdk import query, ClaudeAgentOptions, AgentDefinition

async for message in query(
    prompt="Use the code-reviewer agent to review this codebase",
    options=ClaudeAgentOptions(
        allowed_tools=["Read", "Glob", "Grep", "Agent"],  # Agent tool 必需
        agents={
            "code-reviewer": AgentDefinition(
                description="Expert code reviewer for quality and security reviews.",
                prompt="Analyze code quality and suggest improvements.",
                tools=["Read", "Glob", "Grep"],
                model="sonnet",  # 可覆盖模型
            )
        },
    ),
):
    ...
```

**AgentDefinition 关键字段**：`description`（触发条件）、`prompt`（system prompt）、`tools`、`disallowedTools`、`model`（alias 或 full ID）、`skills`、`memory`、`mcpServers`、`maxTurns`、`background`（非阻塞后台执行）、`effort`、`permissionMode`。

**上下文隔离**：每个 subagent 启动全新对话窗口，不继承父会话历史。父收到子的最终消息（verbatim）作为 Agent tool result。子的 `parent_tool_use_id` 字段可追踪来源。

**限制**：subagents 不能嵌套（不能在子 agent 的 tools 中包含 `Agent`）。

### Sessions（会话持久化）

来源：`01_Raw/code.claude.com/docs/en/agent-sdk/sessions.md`

| 场景 | 用法 |
|------|------|
| 一次性任务 | 单次 `query()` 调用，无需额外处理 |
| 同进程多轮对话 | Python: `ClaudeSDKClient`；TS: `continue: true` |
| 进程重启后继续 | `continue_conversation=True` / `continue: true`（最近一次 session）|
| 恢复指定历史 session | 捕获 `session_id`，`resume=session_id` |
| 分叉尝试不同路径 | `fork` 选项，原 session 不变 |

Session 持久化为 JSONL 文件，保存对话历史（不是文件系统快照）。TypeScript 支持 `persistSession: false` 内存模式，Python 始终写盘。

### Hooks

`PreToolUse`、`PostToolUse`、`Stop`、`SessionStart`、`SessionEnd`、`UserPromptSubmit` 等生命周期回调，使用 `HookMatcher` 按工具名过滤：

```python
hooks={
    "PostToolUse": [HookMatcher(matcher="Edit|Write", hooks=[log_file_change])]
}
```

### Slash Commands / Skills / Memory / Plugins

从 `.claude/` 和 `~/.claude/` 加载（可通过 `setting_sources` 限制）：
- **Skills**：`.claude/skills/*/SKILL.md`，Markdown 定义的专项能力
- **Slash commands**：`.claude/commands/*.md`
- **Memory**：`CLAUDE.md`，项目级上下文
- **Plugins**：编程方式注入自定义 commands / agents / MCP servers

### MCP 集成

```python
options=ClaudeAgentOptions(
    mcp_servers={
        "playwright": {"command": "npx", "args": ["@playwright/mcp@latest"]}
    }
)
```

支持 stdio / SSE transport；可对接数百个现有 MCP server。

### Observability

当前 raw 文档中记录有 `observability.md`，具体内容在当前 session 未完整读取。

---

## 二、OpenAI Agents SDK

来源：`01_Raw/docs.openai.com/docs/guides/agents.md`、`quickstart.md`、`orchestration.md`、`running-agents.md`

**定位**：code-first agent 框架，应用自有 orchestration / 工具执行 / 审批 / 状态管理。

### 安装

```bash
npm install @openai/agents zod   # TypeScript
pip install openai-agents         # Python
export OPENAI_API_KEY=sk-...
```

### 核心 API

```python
from agents import Agent, Runner

agent = Agent(
    name="History tutor",
    instructions="You answer history questions clearly and concisely.",
    model="gpt-5.5",
)

result = await Runner.run(agent, "When did the Roman Empire fall?")
print(result.final_output)
```

### 工具类型

1. **Function tools**：用 `@function_tool` 装饰器注册 Python 函数
2. **Hosted tools**：OpenAI 托管的能力（file search、code interpreter、web search 等）
3. **Agents as tools**：`agent.as_tool()` 把 agent 变为可调用 tool

```python
@function_tool
def history_fun_fact() -> str:
    """Return a short history fact."""
    return "Sharks are older than trees."
```

### 多智能体：Handoffs vs Agents as Tools

来源：`01_Raw/docs.openai.com/docs/guides/agents/orchestration.md`

两种多 agent 模式：

| 模式 | 用法 | 控制权归属 |
|------|------|----------|
| **Handoffs** | `handoffs=[specialist_agent]` | 移交给 specialist |
| **Agents as tools** | `specialist.as_tool(...)` | manager 保持控制 |

```python
# Handoffs（控制权移交）
triage_agent = Agent(
    name="Triage",
    handoffs=[history_tutor, math_tutor],
)

# Agents as tools（manager 保持控制）
main_agent = Agent(
    name="Research assistant",
    tools=[
        summarizer.as_tool(
            tool_name="summarize_text",
            tool_description="Generate a concise summary.",
        )
    ],
)
```

**原则**：尽量从单 agent 开始，只有在能力隔离、策略隔离、prompt 清晰度或 trace 可读性有实质改善时才拆分。

### Agent Loop

来源：`01_Raw/docs.openai.com/docs/guides/agents/running-agents.md`

一次 SDK run = 一次应用层 turn，runner 循环直到真实停止点：

1. 调用当前 agent 模型
2. 检查模型输出
3. 有 tool calls → 执行并继续
4. Handoff → 切换 agent 并继续
5. 有最终答案 + 无更多工具 → 返回结果

### 状态管理

| 策略 | 状态存储位置 | 适用场景 |
|------|------------|---------|
| Manual replay | 应用自有 | 小型 chat loop，最大控制权 |
| `session` | 自有存储 + SDK | 持久对话、可恢复 run |
| `conversationId` | OpenAI Conversations API | 跨 worker/service 共享状态 |
| `previous_response_id` | OpenAI Responses API | 最轻量服务端托管延续 |

### Streaming

```python
from agents import Agent, Runner
from openai.types.responses import ResponseTextDeltaEvent

stream = Runner.run_streamed(agent, "Give me three short facts about Saturn.")
async for event in stream.stream_events():
    if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
        print(event.data.delta, end="", flush=True)
print(f"\nFinal: {stream.final_output}")
```

### Guardrails & Human Review（Approvals）

来源：`01_Raw/docs.openai.com/docs/guides/agents/guardrails-approvals.md`（raw 文件存在）

- **Guardrails**：输入/输出校验，阻断风险内容
- **Human review**：在高风险操作前暂停等待人工确认；resumption 从 `state` 继续，不是新 turn

### Observability

首次 run 后可在 [Traces dashboard](https://platform.openai.com/traces) 检查模型调用、tool calls、handoffs、guardrails。

---

## 三、Gemini Agentic 能力

来源：`01_Raw/ai.google.dev/gemini-api/docs/agents.md`

**注意**：当前 raw 文档以土耳其语爬取（crawler localization 问题），核心内容已从 summary 提取。

**定位**：Gemini 本身提供 reasoning（"大脑"）和基础工具（"双手"），复杂 orchestration 依赖第三方框架。

### 核心组件

- **Gemini 模型**：推理与语言理解
- **工具**：内置（Google Search、Maps、Code Execution）+ 自定义（function calling）
- **Function calling**：定义并接入自定义工具/API
- **Thinking**：复杂任务的多步规划与推理（多数模型默认开启）
- **Long context**：跨长交互保持状态

### 可用 Agent 产品

- **Gemini Deep Research Agent**：自主多步研究 agent，自动规划、执行、综合（市场分析、尽职调查、文献综述）

### 支持的 Orchestration 框架

| 框架 | 用途 |
|------|------|
| LangChain / LangGraph | 有状态复杂流程、多 agent 图结构 |
| LlamaIndex | 结合 RAG 接入自定义数据 |
| CrewAI | 协作式角色扮演自主 agents |
| Vercel AI SDK | JS/TS AI UI 和 agent |
| Google ADK | 官方开源框架，构建可互操作的 agents |

Gemini **没有官方 Agentic SDK**（类比 Claude Agent SDK 或 OpenAI Agents SDK）；agentic 能力通过第三方框架或原生 API 组合实现。

---

## 四、横向对比表

| 维度 | Claude Agent SDK | OpenAI Agents SDK | Gemini |
|------|-----------------|-------------------|--------|
| **官方 SDK 存在** | ✅ Python + TypeScript | ✅ Python + TypeScript | ❌ 依赖第三方框架（LangChain/ADK/等） |
| **运行模式** | 开发者自有进程 | 开发者自有进程 | 第三方框架 / 原生 API |
| **Orchestration 模型** | 主 agent → subagents（通过 Agent tool 派发） | Manager 通过 handoffs 或 agents-as-tools 委托 | 模型自身 reasoning + 外部框架 |
| **内置工具** | Read/Write/Edit/Bash/Glob/Grep/WebSearch/WebFetch/Monitor/AskUserQuestion | Function tools + hosted tools（file search、code interpreter 等）| Google Search、Maps、Code Execution（built-in）；自定义 via function calling |
| **Multi-agent 机制** | Subagents（上下文隔离、可并行、可恢复） | Handoffs（控制权移交）+ Agents-as-tools（保持控制权）| 需借助外部框架（LangGraph/CrewAI 等） |
| **状态/Memory** | Session 持久化为 JSONL；continue / resume / fork | Session / conversationId / previous_response_id / manual replay | 依赖框架实现；long context 为原生支持 |
| **MCP 集成** | 原生内置（`mcpServers` 参数） | 内置（`Using tools` 文档提及 MCP）| Deep Research 声称支持 MCP（preview） |
| **Observability** | `observability.md` 存在（当前 session 未详细读取） | Traces dashboard（openai.com）| 依赖框架；无官方 tracing |
| **Approvals / Human-in-loop** | Permission mode + AskUserQuestion hook | Guardrails + Human review（approvals） | 通过框架实现 |
| **Sandbox / 隔离执行** | 文件操作在 Agent 进程本地；可通过 Bash 调用容器 | Sandbox agents（Python SDK，基于容器的执行环境） | Code Execution tool（Gemini 托管） |
| **托管 / Serverless 路径** | Managed Agents（REST API，Anthropic infra） | Agent Builder（托管 workflow editor + ChatKit）| Gemini API 直接调用 |

---

## 五、何时选哪个

### 选 Claude Agent SDK

- 需要在代码库中直接工作（读/写文件、运行 bash 命令）的 agent
- 想要开箱即用的 coding agent 能力（与 Claude Code 同底层）
- 需要上下文隔离的 subagents + 并行执行
- 已有 `.claude/skills/` 或 CLAUDE.md 等 Claude Code 生态配置
- 原型阶段想快速跑起来，之后再迁移到 Managed Agents 生产化

### 选 OpenAI Agents SDK

- 已深度使用 OpenAI 生态（GPT 模型、file search、code interpreter 等）
- 需要 handoffs 模式（多专家互相移交控制权）
- 需要 OpenAI Traces dashboard 做内置 observability
- 需要 Sandbox agents（容器化执行环境）
- 要与 Agent Builder（托管 workflow）集成

### 选 Gemini（+ 第三方框架）

- 已在 Google Cloud 生态（Vertex AI、Workspace 等）
- 需要 Google Search / Maps 等 native 集成
- 偏好 LangGraph / CrewAI / ADK 等框架，想以 Gemini 模型为 backend
- 需要极长 context window 场景

---

## 六、互操作性

三套框架**不直接互操作**，但可以通过以下方式组合：

1. **MCP 作为中立层**：Claude Agent SDK 和 OpenAI Agents SDK 均支持 MCP；可将工具发布为 MCP server，被任一 framework 调用。
2. **API 层互调**：理论上可在 Claude Agent SDK 的 Bash 工具里调用 OpenAI API，或在 LangGraph 的节点里调用 Claude API，但这些是临时 workaround，非官方设计路径。
3. **会话状态**：三家的 session / conversation state 格式不兼容，跨框架迁移需重构。

当前 raw 文档中均未描述官方的跨框架 interop 方案。
