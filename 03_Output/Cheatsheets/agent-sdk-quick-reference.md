---
type: cheatsheet
topic: agent-sdk-quick-reference
last_updated: 2026-05-05
based_on:
  - 02_Wiki/Entities/Agent-SDK.md
  - 02_Wiki/Summaries/overview--agent-sdk.md
  - 02_Wiki/Summaries/python.md
  - 02_Wiki/Summaries/typescript--agent-sdk.md
  - 02_Wiki/Summaries/migration-guide.md
---

# Claude Agent SDK Quick Reference

> Anthropic Python SDK，让你用 Claude Code **同款 harness** 在自己的 app 里跑 agent。
> 完整 entity [[Agent-SDK]]。本 cheatsheet 是 import + 启动模板 + 主要 API 速查。

---

## 安装 + Import

```bash
pip install claude-agent-sdk
```

```python
from claude_agent_sdk import query, ClaudeAgentOptions
```

---

## Hello World

```python
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions

async def main():
    options = ClaudeAgentOptions(
        model="sonnet",
        allowed_tools=["Bash", "Read", "Edit"],
    )
    async for message in query(prompt="列出当前目录的文件并 grep 'TODO'", options=options):
        print(message)

asyncio.run(main())
```

---

## ClaudeAgentOptions 速查

| 字段 | 类型 | 说明 |
|---|---|---|
| `model` | `"sonnet"` / `"opus"` / `"haiku"` / 全 ID | 主对话模型 |
| `allowed_tools` | `list[str]` | tool name 白名单（含 `"Skill"` 才允许 skills） |
| `disallowed_tools` | `list[str]` | 黑名单（先应用） |
| `permission_mode` | 同 [[Permission-mode]] | `"default"` / `"acceptEdits"` / `"bypassPermissions"` / `"auto"` / `"plan"` |
| `system_prompt` | `str` | 自定义 system prompt（覆盖默认） |
| `setting_sources` | `list[str]` | 加载哪些 settings 文件，默认 `["user", "project"]` |
| `mcp_servers` | `dict` | inline MCP server 配置 |
| `hooks` | `dict` | in-process callback hooks（不同于 filesystem shell hooks） |
| `cwd` | `str` | working directory |
| `max_turns` | `int` | 最大对话轮次 |
| `effort` | `"low"` / `"medium"` / `"high"` | adaptive thinking budget |

---

## 重要行为差异（vs Claude Code CLI）

| 行为 | CLI | SDK |
|---|---|---|
| Skill 是否启用 | session 默认开 | 必须 `"Skill"` 在 `allowed_tools` |
| SKILL.md `allowed-tools` 字段 | honored | **忽略** |
| Hooks 加载 | `.claude/settings.json` 自动 | 需 `setting_sources` 指定 + 也可 in-process callback |
| Subagent 内置 | 全有（Explore / Plan / general-purpose） | 默认全有，但要在 prompt 里说 |
| Plugin 加载 | install 后全自动 | 仅支持 `type: "local"` + filesystem path（远程 marketplace 必须先下载） |

---

## In-process Hooks（SDK 独有）

不同于文件系统的 shell hooks，SDK 可以注册 Python callable：

```python
from claude_agent_sdk import query, ClaudeAgentOptions

async def pre_tool_hook(event):
    if event["tool_name"] == "Bash" and "rm -rf" in event["tool_input"].get("command", ""):
        return {"permissionDecision": "deny", "reason": "rm -rf 禁止"}
    return None

options = ClaudeAgentOptions(
    hooks={"PreToolUse": [pre_tool_hook]},
    setting_sources=["user", "project"],   # 还想叠加 filesystem hooks 就加这个
)
```

TS SDK 比 Python SDK 多支持 `SessionStart` / `SessionEnd` / `Setup` / `PostToolBatch` 等事件（见 [[Hooks]]）。

---

## Custom Tools

```python
from claude_agent_sdk import query, ClaudeAgentOptions, tool

@tool(
    name="get_weather",
    description="查指定城市天气",
    input_schema={"type": "object", "properties": {"city": {"type": "string"}}, "required": ["city"]},
)
async def get_weather(input: dict) -> str:
    city = input["city"]
    # 调真实 API
    return f"{city} 今天 22°C 晴"

options = ClaudeAgentOptions(
    allowed_tools=["get_weather"],
    custom_tools=[get_weather],
)
```

---

## MCP Server 接入

```python
options = ClaudeAgentOptions(
    mcp_servers={
        "github": {
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-github"],
            "env": {"GITHUB_TOKEN": "${GITHUB_TOKEN}"},
        }
    },
    allowed_tools=["mcp__github__*"],   # wildcard 放过整 server
)
```

详见 [[MCP-server]]。

---

## Sessions（持久对话）

```python
from claude_agent_sdk import query, ClaudeAgentOptions

session_id = "user-123-thread-abc"

options = ClaudeAgentOptions(
    session_id=session_id,
    setting_sources=["user", "project"],
)

# 第一轮
async for msg in query(prompt="记住我喜欢 Python", options=options):
    pass

# 第二轮（同 session）
async for msg in query(prompt="用我喜欢的语言写一个 fib", options=options):
    print(msg)
```

session 持久化路径在 `~/.claude/projects/{project}/{session_id}/`。

---

## Cost Tracking

```python
from claude_agent_sdk import query, ClaudeAgentOptions

async for msg in query(prompt="...", options=ClaudeAgentOptions()):
    if msg.type == "result":
        usage = msg.usage  # input_tokens / output_tokens / cache_read / cache_creation
        cost = msg.cost_usd
        print(f"This turn cost ${cost:.4f}")
```

---

## Streaming Output

```python
async for msg in query(...):
    if msg.type == "stream":
        print(msg.delta, end="", flush=True)   # token-by-token
    elif msg.type == "tool_use":
        print(f"\n→ calling {msg.tool_name}...")
```

---

## Model Migration（旧 model ID）

`claude-3-5-sonnet-*` / `claude-3-7-sonnet-*` 等老 ID 已 deprecated。最新（2026-05）映射：

| 用途 | 推荐 |
|---|---|
| 主对话 / 复杂任务 | `claude-opus-4-7` |
| 平衡 | `claude-sonnet-4-6` |
| 廉价 / fast | `claude-haiku-4-5-20251001` |

迁移用 `migration-guide` summary（见 [[Agent-SDK]]）。Claude Code CLI 跑 `migrate-claude-opus-4-5` 命令自动改 hard-code 的 model ID。

---

## TypeScript SDK?

⚠️ **`anthropics/claude-code-sdk-typescript` 已 deprecated（404）**。当前 Agent SDK 仅 Python。

要在 Node 里跑 agent，可选方案：
1. 用 Anthropic SDK TypeScript（`@anthropic-ai/sdk`）—— 但你得自己实现 agent loop / tool use / hooks
2. 调 Python SDK 经 IPC
3. 等 Anthropic 出 TS Agent SDK

---

## 易踩的坑

- **Skill 不在 `allowed_tools` 就完全失效** —— 即使文件存在 + `disable-model-invocation: false`
- **Hooks 不会自动加载** —— 必须 `setting_sources=["user", "project"]` 或在 options.hooks 里 in-process 注册
- **`max_turns` 默认无限** —— 长跑可能花光 budget，加显式 `max_turns=20`
- **subagent 不能再 spawn subagent** —— 别把 `Agent` 工具放进 subagent 的 `tools`
- **`bypassPermissions` 模式 + subagent = 危险**：subagent 强制继承父模式
- **session_id 持久化在 filesystem** —— 多进程并发同 session_id 会冲突

---

## 详细引用

- [[Agent-SDK]] · [[Skill]] · [[Hooks]] · [[MCP-server]] · [[Subagent]] · [[Permission-mode]]
- [[Plugin]] —— SDK 加载 plugin 限制
- 完整 cookbook：见 raw `01_Raw/github/anthropics/claude-cookbooks/`
