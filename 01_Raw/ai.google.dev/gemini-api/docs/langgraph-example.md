---
source_url: https://ai.google.dev/gemini-api/docs/langgraph-example?hl=zh-CN
fetched_at: 2026-05-05T20:45:38.780273+00:00
title: "\u4f7f\u7528 Gemini \u548c LangGraph \u4ece\u5934\u5f00\u59cb\u6784\u5efa ReAct \u667a\u80fd\u4f53 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-cn) 现已推出预览版，支持协作规划、可视化、MCP 等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 使用 Gemini 和 LangGraph 从头开始构建 ReAct 智能体

LangGraph 是一个用于构建有状态 LLM 应用的框架，因此非常适合构建 ReAct（推理和行动）智能体。

ReAct 智能体将 LLM 推理与行动执行相结合。它们会迭代思考、使用工具并根据观察结果采取行动，以实现用户目标，并动态调整其方法。这种模式在[“ReAct：在语言模型中协同推理和行动”](https://arxiv.org/abs/2210.03629) (2023) 中首次提出，旨在模仿人类般的灵活问题解决方式，而不是僵化的工作流。

LangGraph 提供了一个预构建的 ReAct 智能体 ([`create_react_agent`](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent))，
当您需要对 ReAct 实现进行更多控制和自定义时，它会大放异彩。本指南将向您展示一个简化版本。

LangGraph 使用三个关键组件将智能体建模为图：

- `State`：共享数据结构（通常为 `TypedDict` 或 `Pydantic BaseModel`），表示应用的当前快照。
- `Nodes`：对智能体的逻辑进行编码。它们接收当前状态作为输入，执行一些计算或副作用，并返回更新后的状态，例如 LLM 调用或工具调用。
- `Edges`：根据当前 `State` 定义要执行的下一个 `Node`，从而实现条件逻辑和固定转换。

如果您还没有 API 密钥，可以从 [Google AI
Studio](https://aistudio.google.com/app/apikey?hl=zh-cn) 获取一个。

```
pip install langgraph langchain-google-genai geopy requests
```

在环境变量 `GEMINI_API_KEY` 中设置您的 API 密钥。

```
import os

# Read your API key from the environment variable or set it manually
api_key = os.getenv("GEMINI_API_KEY")
```

为了更好地了解如何使用 LangGraph 实现 ReAct 智能体，本指南将介绍一个实际示例。您将创建一个智能体，其目标是使用工具查找指定位置的当前天气。

对于此天气智能体，`State` 将维护正在进行的对话历史记录（作为消息列表）和一个计数器（作为整数），用于说明已采取的步骤数。

LangGraph 提供了一个辅助函数 `add_messages`，用于更新状态消息列表。它充当 [reducer](https://langchain-ai.github.io/langgraph/concepts/low_level/#reducers)，
接收当前列表以及新消息，并返回合并后的列表。它通过消息 ID 处理更新，并默认为新消息和未见消息采用“仅追加”行为。

```
from typing import Annotated,Sequence, TypedDict

from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages  # helper function to add messages to the state

class AgentState(TypedDict):
    """The state of the agent."""
    messages: Annotated[Sequence[BaseMessage], add_messages]
    number_of_steps: int
```

接下来，定义您的天气工具。

```
from langchain_core.tools import tool
from geopy.geocoders import Nominatim
from pydantic import BaseModel, Field
import requests

geolocator = Nominatim(user_agent="weather-app")

class SearchInput(BaseModel):
    location:str = Field(description="The city and state, e.g., San Francisco")
    date:str = Field(description="the forecasting date for when to get the weather format (yyyy-mm-dd)")

@tool("get_weather_forecast", args_schema=SearchInput, return_direct=True)
def get_weather_forecast(location: str, date: str):
    """Retrieves the weather using Open-Meteo API.

    Takes a given location (city) and a date (yyyy-mm-dd).

    Returns:
        A dict with the time and temperature for each hour.
    """
    # Note that Colab may experience rate limiting on this service. If this
    # happens, use a machine to which you have exclusive access.
    location = geolocator.geocode(location)
    if location:
        try:
            response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={location.latitude}&longitude={location.longitude}&hourly=temperature_2m&start_date={date}&end_date={date}")
            data = response.json()
            return dict(zip(data["hourly"]["time"], data["hourly"]["temperature_2m"]))
        except Exception as e:
            return {"error": str(e)}
    else:
        return {"error": "Location not found"}

tools = [get_weather_forecast]
```

现在，初始化模型并将工具绑定到模型。

```
from datetime import datetime
from langchain_google_genai import ChatGoogleGenerativeAI

# Create LLM class
llm = ChatGoogleGenerativeAI(
    model= "gemini-3-flash-preview",
    temperature=1.0,
    max_retries=2,
    google_api_key=api_key,
)

# Bind tools to the model
model = llm.bind_tools([get_weather_forecast])

# Test the model with tools
res=model.invoke(f"What is the weather in Berlin on {datetime.today()}?")

print(res)
```

在运行智能体之前，最后一步是定义节点和边缘。在此示例中，您有两个节点和一个边缘。

- 执行工具方法的 `call_tool` 节点。LangGraph 为此提供了一个名为
  [ToolNode](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/)的预构建节点
  。
- 使用 `model_with_tools` 调用模型的 `call_model` 节点。
- 决定是调用工具还是模型的 `should_continue` 边缘。

节点和边缘的数量不是固定的。您可以根据需要在图中添加任意数量的节点和边缘。例如，您可以添加一个用于添加结构化输出的节点，或者添加一个自我验证/反思节点，以便在调用工具或模型之前检查模型输出。

```
from langchain_core.messages import ToolMessage
from langchain_core.runnables import RunnableConfig

tools_by_name = {tool.name: tool for tool in tools}

# Define our tool node
def call_tool(state: AgentState):
    outputs = []
    # Iterate over the tool calls in the last message
    for tool_call in state["messages"][-1].tool_calls:
        # Get the tool by name
        tool_result = tools_by_name[tool_call["name"]].invoke(tool_call["args"])
        outputs.append(
            ToolMessage(
                content=tool_result,
                name=tool_call["name"],
                tool_call_id=tool_call["id"],
            )
        )
    return {"messages": outputs}

def call_model(
    state: AgentState,
    config: RunnableConfig,
):
    # Invoke the model with the system prompt and the messages
    response = model.invoke(state["messages"], config)
    # This returns a list, which combines with the existing messages state
    # using the add_messages reducer.
    return {"messages": [response]}

# Define the conditional edge that determines whether to continue or not
def should_continue(state: AgentState):
    messages = state["messages"]
    # If the last message is not a tool call, then finish
    if not messages[-1].tool_calls:
        return "end"
    # default to continue
    return "continue"
```

准备好所有智能体组件后，您现在可以组装它们了。

```
from langgraph.graph import StateGraph, END

# Define a new graph with our state
workflow = StateGraph(AgentState)

# 1. Add the nodes
workflow.add_node("llm", call_model)
workflow.add_node("tools",  call_tool)
# 2. Set the entrypoint as `agent`, this is the first node called
workflow.set_entry_point("llm")
# 3. Add a conditional edge after the `llm` node is called.
workflow.add_conditional_edges(
    # Edge is used after the `llm` node is called.
    "llm",
    # The function that will determine which node is called next.
    should_continue,
    # Mapping for where to go next, keys are strings from the function return,
    # and the values are other nodes.
    # END is a special node marking that the graph is finish.
    {
        # If `tools`, then we call the tool node.
        "continue": "tools",
        # Otherwise we finish.
        "end": END,
    },
)
# 4. Add a normal edge after `tools` is called, `llm` node is called next.
workflow.add_edge("tools", "llm")

# Now we can compile and visualize our graph
graph = workflow.compile()
```

您可以使用 `draw_mermaid_png` 方法可视化图。

```
from IPython.display import Image, display

display(Image(graph.get_graph().draw_mermaid_png()))
```

![png](https://ai.google.dev/static/gemini-api/docs/images/langgraph-react-agent_16_0.png?hl=zh-cn)

现在运行智能体。

```
from datetime import datetime
# Create our initial message dictionary
inputs = {"messages": [("user", f"What is the weather in Berlin on {datetime.today()}?")]}

# call our graph with streaming to see the steps
for state in graph.stream(inputs, stream_mode="values"):
    last_message = state["messages"][-1]
    last_message.pretty_print()
```

您现在可以继续对话，询问另一个城市的天气，或请求比较。

```
state["messages"].append(("user", "Would it be warmer in Munich?"))

for state in graph.stream(state, stream_mode="values"):
    last_message = state["messages"][-1]
    last_message.pretty_print()
```

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-04-29。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-04-29。"],[],[]]
