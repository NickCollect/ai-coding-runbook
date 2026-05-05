---
type: summary
source: 01_Raw/code.claude.com/docs/en/agent-sdk/custom-tools.md
source_url: https://code.claude.com/docs/en/agent-sdk/custom-tools
title: "Claude Agent SDK — 自定义工具（in-process MCP server）"
summarized_at: 2026-05-05
entities_referenced:
  - Agent-SDK.md
  - Anthropic-SDK-Python.md
  - Anthropic-SDK-TypeScript.md
concepts_referenced:
  - Tool-use.md
---

Custom tools 通过 Agent SDK 内置的 in-process MCP server 扩展 agent 能力，让 Claude 可以调用开发者定义的函数，访问数据库、外部 API 或领域逻辑，无需运行单独的服务器进程。

## 定义工具

一个工具由四部分组成：

1. **Name**：唯一标识符，Claude 用它来调用工具
2. **Description**：工具功能描述，Claude 据此决定何时调用
3. **Input schema**：TypeScript 用 Zod schema（自动推导 args 类型）；Python 用 `{"param": type}` 字典（SDK 转换为 JSON Schema），或直接传完整 JSON Schema（支持 enum、range、嵌套对象）
4. **Handler**：async 函数，接收验证后的参数，必须返回 `{ content: [...], isError?: bool }`

```python
# Python
from claude_agent_sdk import tool, create_sdk_mcp_server

@tool("get_temperature", "Get the current temperature at a location",
      {"latitude": float, "longitude": float})
async def get_temperature(args):
    # ... 调用 API
    return {"content": [{"type": "text", "text": f"Temperature: 72°F"}]}

weather_server = create_sdk_mcp_server(name="weather", version="1.0.0", tools=[get_temperature])
```

```typescript
// TypeScript
import { tool, createSdkMcpServer } from "@anthropic-ai/claude-agent-sdk";
import { z } from "zod";

const getTemperature = tool("get_temperature", "Get the current temperature at a location",
  { latitude: z.number(), longitude: z.number() },
  async (args) => ({
    content: [{ type: "text", text: `Temperature: 72°F` }]
  })
);

const weatherServer = createSdkMcpServer({ name: "weather", version: "1.0.0", tools: [getTemperature] });
```

## 注册并使用工具

将 MCP server 传入 `query()` 的 `mcpServers` 选项；工具名格式为 `mcp__{server_name}__{tool_name}`；在 `allowedTools` 中列出以跳过权限提示：

```python
options = ClaudeAgentOptions(
    mcp_servers={"weather": weather_server},
    allowed_tools=["mcp__weather__get_temperature"],  # 或用通配符 mcp__weather__*
)
```

## 工具注解（Tool Annotations）

可选元数据，第五个参数传入（TypeScript）或 `annotations` 关键字参数（Python）：

| 字段 | 默认值 | 含义 |
|------|-------|------|
| `readOnlyHint` | `false` | 工具不修改环境，可与其他只读工具并行调用 |
| `destructiveHint` | `true` | 工具可能有破坏性更新（仅参考） |
| `idempotentHint` | `false` | 相同参数重复调用无额外效果（仅参考） |
| `openWorldHint` | `true` | 工具访问进程外系统（仅参考） |

注解是元数据，不强制执行。`readOnlyHint: true` 的工具依然可以写磁盘（若 handler 这样做）。

## 工具访问控制

两层控制独立工作：

| 选项 | 层级 | 效果 |
|------|------|------|
| `tools: ["Read", "Grep"]` | 可用性 | 只有列出的内置工具出现在 Claude 上下文中，MCP 工具不受影响 |
| `allowedTools` | 权限 | 列出的工具无需权限提示即可运行 |
| `disallowedTools` | 权限 | 每次调用都被拒绝，但工具仍在上下文中（Claude 可能尝试调用后被拒）|

建议用 `tools` 而非 `disallowedTools` 来限制内置工具，前者将工具从上下文移除，后者仅拒绝调用但浪费一次 turn。

## 错误处理

| 行为 | 结果 |
|------|------|
| Handler 抛出未捕获异常 | Agent loop 停止，Claude 不会看到错误 |
| Handler 返回 `isError: true` | Agent loop 继续，Claude 将错误视为数据，可重试或向用户说明 |

始终在 handler 内捕获异常并返回 `isError: true`，避免意外终止 loop。

## 返回图片和资源

`content` 数组支持三种 block 类型，可混合使用：

- **text**：文本内容
- **image**：`{ type: "image", data: "<base64>", mimeType: "image/png" }`（inline base64，无 URL 字段）
- **resource**：`{ type: "resource", resource: { uri, text/blob, mimeType } }`（URI 是标签，实际内容在 text 或 blob 字段）

## 大规模工具集

每个工具定义都会消耗 context window。工具数量超过约 10 个时，建议启用 [Tool Search](https://code.claude.com/en/agent-sdk/tool-search) 按需加载，而非全量预加载。
