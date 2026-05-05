---
type: summary
source: 01_Raw/docs.openai.com/docs/guides/tools.md
source_url: https://platform.openai.com/docs/guides/tools
title: "OpenAI — Using Tools 概览"
summarized_at: 2026-05-05
entities_referenced: [MCP-server, Web-search-tool]
concepts_referenced: [Tool-use, Agentic-loop]
---

## 核心要点

工具扩展了模型的能力，通过 `tools` 参数配置，模型根据 prompt 自动决定是否使用。

### 可用工具一览

| 工具 | 描述 |
|---|---|
| Function calling | 调用自定义代码，访问数据或执行操作 |
| Web search | 在生成响应时从互联网获取最新数据 |
| Remote MCP | 通过 MCP server 连接外部服务 |
| Skills | 上传并复用版本化 skill bundle |
| Shell | 在托管容器或本地运行时中执行 shell 命令 |
| Computer use | 创建控制计算机界面的 agentic 工作流 |
| Image generation | 使用 GPT Image 生成或编辑图片 |
| File search | 搜索已上传文件内容 |
| Tool search | 动态加载相关工具，优化 token 用量 |

仅 `gpt-5.4` 及以上模型支持 `tool_search`。

### Agents SDK 中的工具

```python
from agents import function_tool

@function_tool
def get_weather(city: str) -> str:
    """Get the weather for a given city."""
    return f"The weather in {city} is sunny."
```

工具直接绑定在 agent 定义上；也可将 specialist agent 作为 tool 暴露给 manager agent。

### Tool search

当工具生态庞大时，避免全部前置加载（会占用 context window），用 `tool_search` 按需动态加载相关工具。
