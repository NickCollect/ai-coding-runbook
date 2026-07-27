---
source_url: https://ai.google.dev/gemini-api/docs/temporal-example?hl=zh-CN
fetched_at: 2026-07-27T04:33:24.395702+00:00
title: "\u4f7f\u7528 Gemini \u548c Temporal \u6784\u5efa\u6301\u4e45\u578b AI \u667a\u80fd\u4f53 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn) 现已正式发布。我们建议使用此 API 来访问所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 使用 Gemini 和 Temporal 构建持久型 AI 智能体

本教程将引导您构建一个 [ReAct 风格](https://arxiv.org/abs/2210.03629)的智能体循环，该循环使用 Gemini API 进行推理，并使用 [Temporal](https://temporal.io/) 实现耐用性。[GitHub](https://github.com/temporal-community/durable-react-agent-gemini) 上提供了本教程的完整源代码。

智能体可以调用工具，例如查找天气警报或对 IP 地址进行地理定位，并且会循环调用，直到有足够的信息来做出回答。

与典型的代理演示不同的是，此演示具有**持久性**。每次 LLM 调用、每次工具调用和代理循环的每个步骤都会由 Temporal 持久保存。如果进程崩溃、网络中断或 API 超时，Temporal 会自动重试并从上次完成的步骤继续执行。不会丢失任何对话历史记录，也不会错误地重复任何工具调用。

## 架构

该架构包含三个部分：

- **工作流**：编排执行逻辑的智能体循环。
- **活动**：Temporal 使之持久化的各个工作单元（LLM 调用、工具调用）。
- **工作器**：执行工作流和活动的进程。

在此示例中，您会将这三个部分全部放在一个文件 (`durable_agent_worker.py`) 中。在实际实现中，您会将其分开，以便获得各种部署和可伸缩性优势。您将把向代理提供提示的代码放在第二个文件 (`start_workflow.py`) 中。

## 前提条件

如需完成本指南，您需要：

- Gemini API 密钥。您可以在 [Google AI Studio](https://aistudio.google.com/apikey?hl=zh-cn) 中免费创建 API 密钥。
- [Python](https://www.python.org/downloads/) 3.10 版或更高版本。
- 用于运行本地开发服务器的 [Temporal CLI](https://docs.temporal.io/cli)。

## 设置

开始之前，请确保您已在本地运行 [Temporal 开发服务器](https://docs.temporal.io/cli#start-dev-server)：

```
temporal server start-dev
```

接下来，安装所需的依赖项：

```
pip install temporalio google-genai httpx pydantic python-dotenv
```

在项目目录中创建一个包含 Gemini API 密钥的 `.env` 文件。您可以从 [Google AI Studio](https://aistudio.google.com/apikey?hl=zh-cn) 获取 API 密钥。

```
echo "GOOGLE_API_KEY=your-api-key-here" > .env
```

## 实现

本教程的其余部分将从上到下逐步介绍 `durable_agent_worker.py`，逐步构建代理。创建文件并继续操作。

### 导入和沙盒设置

首先定义必须预先定义的导入。`workflow.unsafe.imports_passed_through()` 块会告知 Temporal 的工作流沙盒允许某些模块不受限制地通过。这是必需的，因为多个库（尤其是 `urllib.request.Request` 的子类 `httpx`）使用的模式会被沙盒阻止。

```
from temporalio import workflow

with workflow.unsafe.imports_passed_through():
    import pydantic_core  # noqa: F401
    import annotated_types  # noqa: F401

    import httpx
    from pydantic import BaseModel, Field
    from google import genai
    from google.genai import types
```

### 系统指令

接下来，定义智能体的个性。系统指令会告知模型如何行动。此智能体已收到指令，在不需要任何工具的情况下以俳句形式回答问题。

```
SYSTEM_INSTRUCTIONS = """
You are a helpful agent that can use tools to help the user.
You will be given an input from the user and a list of tools to use.
You may or may not need to use the tools to satisfy the user ask.
If no tools are needed, respond in haikus.
"""
```

### 工具定义

现在，定义智能体可以使用的工具。每个工具都是一个具有描述性文档字符串的异步函数。接受参数的工具使用 Pydantic 模型作为其唯一实参。这是 Temporal 最佳实践，可确保在您随着时间的推移添加可选字段时，活动签名保持稳定。

```
import json

NWS_API_BASE = "https://api.weather.gov"
USER_AGENT = "weather-app/1.0"

class GetWeatherAlertsRequest(BaseModel):
    """Request model for getting weather alerts."""

    state: str = Field(description="Two-letter US state code (e.g. CA, NY)")

async def get_weather_alerts(request: GetWeatherAlertsRequest) -> str:
    """Get weather alerts for a US state.

    Args:
        request: The request object containing:
            - state: Two-letter US state code (e.g. CA, NY)
    """
    headers = {"User-Agent": USER_AGENT, "Accept": "application/geo+json"}
    url = f"{NWS_API_BASE}/alerts/active/area/{request.state}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, timeout=5.0)
        response.raise_for_status()
        return json.dumps(response.json())
```

接下来，定义 IP 地址地理定位工具：

```
class GetLocationRequest(BaseModel):
    """Request model for getting location info from an IP address."""

    ipaddress: str = Field(description="An IP address")

async def get_ip_address() -> str:
    """Get the public IP address of the current machine."""
    async with httpx.AsyncClient() as client:
        response = await client.get("https://icanhazip.com")
        response.raise_for_status()
        return response.text.strip()

async def get_location_info(request: GetLocationRequest) -> str:
    """Get the location information for an IP address including city, state, and country.

    Args:
        request: The request object containing:
            - ipaddress: An IP address to look up
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://ip-api.com/json/{request.ipaddress}")
        response.raise_for_status()
        result = response.json()
        return f"{result['city']}, {result['regionName']}, {result['country']}"
```

### 工具注册表

接下来，创建一个将工具名称映射到处理函数的注册表。`get_tools()` 函数使用 `FunctionDeclaration.from_callable_with_api_option()` 从可调用对象生成与 Gemini 兼容的 `FunctionDeclaration` 对象。

```
from typing import Any, Awaitable, Callable

ToolHandler = Callable[..., Awaitable[Any]]

def get_handler(tool_name: str) -> ToolHandler:
    """Get the handler function for a given tool name."""
    if tool_name == "get_location_info":
        return get_location_info
    if tool_name == "get_ip_address":
        return get_ip_address
    if tool_name == "get_weather_alerts":
        return get_weather_alerts
    raise ValueError(f"Unknown tool name: {tool_name}")

def get_tools() -> types.Tool:
    """Get the Tool object containing all available function declarations.

    Uses FunctionDeclaration.from_callable_with_api_option() from the Google GenAI SDK
    to generate tool definitions from the handler functions.
    """
    return types.Tool(
        function_declarations=[
            types.FunctionDeclaration.from_callable_with_api_option(
                callable=get_weather_alerts, api_option="GEMINI_API"
            ),
            types.FunctionDeclaration.from_callable_with_api_option(
                callable=get_location_info, api_option="GEMINI_API"
            ),
            types.FunctionDeclaration.from_callable_with_api_option(
                callable=get_ip_address, api_option="GEMINI_API"
            ),
        ]
    )
```

### LLM 活动

现在，定义调用 Gemini API 的 activity。`GeminiChatRequest` 和 `GeminiChatResponse` 数据类定义了协定。

您将停用自动函数调用，以便将大语言模型调用和工具调用作为单独的任务来处理，从而提高智能体的持久性。您还将停用 SDK 的内置重试机制 (`attempts=1`)，因为 Temporal 会持久地处理重试。

```
import os
from dataclasses import dataclass

from temporalio import activity

@dataclass
class GeminiChatRequest:
    """Request parameters for a Gemini chat completion."""

    model: str
    system_instruction: str
    contents: list[types.Content]
    tools: list[types.Tool]

@dataclass
class GeminiChatResponse:
    """Response from a Gemini chat completion."""

    text: str | None
    function_calls: list[dict[str, Any]]
    raw_parts: list[types.Part]

@activity.defn
async def generate_content(request: GeminiChatRequest) -> GeminiChatResponse:
    """Execute a Gemini chat completion with tool support."""
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY environment variable is not set")
    client = genai.Client(
        api_key=api_key,
        http_options=types.HttpOptions(
            retry_options=types.HttpRetryOptions(attempts=1),
        ),
    )

    config = types.GenerateContentConfig(
        system_instruction=request.system_instruction,
        tools=request.tools,
        automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True),
    )

    response = await client.aio.models.generate_content(
        model=request.model,
        contents=request.contents,
        config=config,
    )

    function_calls = []
    raw_parts = []
    text_parts = []

    if response.candidates and response.candidates[0].content:
        for part in response.candidates[0].content.parts:
            raw_parts.append(part)
            if part.function_call:
                function_calls.append(
                    {
                        "name": part.function_call.name,
                        "args": dict(part.function_call.args) if part.function_call.args else {},
                    }
                )
            elif part.text:
                text_parts.append(part.text)

    text = "".join(text_parts) if text_parts and not function_calls else None

    return GeminiChatResponse(
        text=text,
        function_calls=function_calls,
        raw_parts=raw_parts,
    )
```

### 动态工具活动

接下来，定义执行工具的 activity。这使用了 Temporal 的动态 activity 功能：通过 `get_handler` 函数从工具注册表中获取工具处理程序（可调用对象）。这样一来，只需提供不同的工具和系统指令，即可定义不同的代理；实现代理循环的工作流无需更改。

该 activity 会检查处理程序的签名，以确定如何传递实参。如果处理程序需要 Pydantic 模型，它会处理 Gemini 生成的嵌套输出格式（例如 `{"request": {"state": "CA"}}` 而不是扁平的 `{"state": "CA"}`）。

```
import inspect
from collections.abc import Sequence

from temporalio.common import RawValue

@activity.defn(dynamic=True)
async def dynamic_tool_activity(args: Sequence[RawValue]) -> dict:
    """Execute a tool dynamically based on the activity name."""
    tool_name = activity.info().activity_type
    tool_args = activity.payload_converter().from_payload(args[0].payload, dict)
    activity.logger.info(f"Running dynamic tool '{tool_name}' with args: {tool_args}")

    handler = get_handler(tool_name)

    if not inspect.iscoroutinefunction(handler):
        raise TypeError("Tool handler must be async (awaitable).")

    sig = inspect.signature(handler)
    params = list(sig.parameters.values())

    if len(params) == 0:
        result = await handler()
    else:
        param = params[0]
        param_name = param.name
        ann = param.annotation

        if isinstance(ann, type) and issubclass(ann, BaseModel):
            nested_args = tool_args.get(param_name, tool_args)
            result = await handler(ann(**nested_args))
        else:
            result = await handler(**tool_args)

    activity.logger.info(f"Tool '{tool_name}' result: {result}")
    return result
```

### 智能体循环工作流

现在，您已具备完成代理构建的所有条件。`AgentWorkflow` 类实现了包含智能体循环的工作流。在该循环中，系统会通过 activity（使其持久化）调用 LLM，检查输出，如果 LLM 已选择某个工具，则通过 `dynamic_tool_activity` 调用该工具。

在这个简单的 ReAct 风格的代理中，一旦 LLM 选择不使用工具，循环就会被视为完成，并返回最终的 LLM 结果。

```
from datetime import timedelta

@workflow.defn
class AgentWorkflow:
    """Agentic loop workflow that uses Gemini for LLM calls and executes tools."""

    @workflow.run
    async def run(self, input: str) -> str:
        contents: list[types.Content] = [
            types.Content(role="user", parts=[types.Part.from_text(text=input)])
        ]

        tools = [get_tools()]

        while True:
            result = await workflow.execute_activity(
                generate_content,
                GeminiChatRequest(
                    model="gemini-3.5-flash",
                    system_instruction=SYSTEM_INSTRUCTIONS,
                    contents=contents,
                    tools=tools,
                ),
                start_to_close_timeout=timedelta(seconds=60),
            )

            if result.function_calls:
                # Sending the complete raw_parts here ensures Gemini 3 thought
                # signatures are propagated correctly.
                contents.append(types.Content(role="model", parts=result.raw_parts))

                for function_call in result.function_calls:
                    tool_result = await self._handle_function_call(function_call)

                    contents.append(
                        types.Content(
                            role="user",
                            parts=[
                                types.Part.from_function_response(
                                    name=function_call["name"],
                                    response={"result": tool_result},
                                )
                            ],
                        )
                    )
            else:
                return result.text
            # Leave this in place. You will un-comment it during a durability
            # test later on.
            # await asyncio.sleep(10)

    async def _handle_function_call(self, function_call: dict) -> str:
        """Execute a tool via dynamic activity and return the result."""
        tool_name = function_call["name"]
        tool_args = function_call.get("args", {})

        result = await workflow.execute_activity(
            tool_name,
            tool_args,
            start_to_close_timeout=timedelta(seconds=30),
        )

        return result
```

代理循环完全持久。如果代理工作器在多次循环迭代后崩溃，Temporal 将从其停止的位置继续运行，而无需重新调用已执行的 LLM 调用或工具调用。

### 工作器启动

最后，将所有设备连接在一起。虽然该代码以使其看起来像是在单个进程中运行的方式实现了必要的业务逻辑，但使用 Temporal 使其成为一个事件驱动型系统（具体来说，是事件源型系统），其中工作流和 activity 之间的通信通过 Temporal 提供的消息传递机制进行。

Temporal 工作器连接到 Temporal 服务，并充当工作流和 activity 任务的调度程序。工作器注册工作流和两个 activity，然后开始监听任务。

```
import asyncio
from concurrent.futures import ThreadPoolExecutor

from dotenv import load_dotenv
from temporalio.client import Client
from temporalio.contrib.pydantic import pydantic_data_converter
from temporalio.envconfig import ClientConfig
from temporalio.worker import Worker

async def main():
    config = ClientConfig.load_client_connect_config()
    config.setdefault("target_host", "localhost:7233")
    client = await Client.connect(
        **config,
        data_converter=pydantic_data_converter,
    )

    worker = Worker(
        client,
        task_queue="gemini-agent-python-task-queue",
        workflows=[
            AgentWorkflow,
        ],
        activities=[
            generate_content,
            dynamic_tool_activity,
        ],
        activity_executor=ThreadPoolExecutor(max_workers=10),
    )
    await worker.run()

if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())
```

## 客户端脚本

创建客户端脚本 (`start_workflow.py`)。该脚本会提交查询并等待结果。请注意，它连接到代理工作器中引用的同一任务队列，`start_workflow` 脚本会将包含用户提示的工作流任务调度到该任务队列，从而启动代理的执行。

```
import asyncio
import sys
import uuid

from temporalio.client import Client
from temporalio.contrib.pydantic import pydantic_data_converter

async def main():
    client = await Client.connect(
        "localhost:7233",
        data_converter=pydantic_data_converter,
    )

    query = sys.argv[1] if len(sys.argv) > 1 else "Tell me about recursion"

    result = await client.execute_workflow(
        "AgentWorkflow",
        query,
        id=f"gemini-agent-id-{uuid.uuid4()}",
        task_queue="gemini-agent-python-task-queue",
    )
    print(f"\nResult:\n{result}")

if __name__ == "__main__":
    asyncio.run(main())
```

## 运行代理

如果尚未启动，请启动 Temporal 开发服务器：

```
temporal server start-dev
```

在新终端窗口中，启动代理工作器：

```
python -m durable_agent_worker
```

在第三个终端窗口中，向您的代理提交查询：

```
python -m start_workflow "are there any weather alerts for where I am?"
```

请注意终端中 `durable_agent_worker` 的输出，其中显示了代理循环每次迭代中发生的动作。LLM 能够通过调用其可用的各种工具来满足用户请求。您可以通过 Temporal 界面 (`http://localhost:8233/namespaces/default/workflows`) 查看已执行的步骤。

尝试使用几个不同的提示，看看智能体如何推理和调用工具：

```
python -m start_workflow "are there any weather alerts for New York?"
python -m start_workflow "where am I?"
python -m start_workflow "what is my ip address?"
python -m start_workflow "tell me a joke"
```

最后一个提示不需要任何工具，因此智能体根据 `SYSTEM_INSTRUCTIONS` 以俳句的形式回答。

## 测试耐用性（可选）

基于 Temporal 构建可确保您的代理能够顺利应对故障。您可以使用两个不同的实验来测试这一点。

### 模拟网络中断

在此测试中，您将暂时停用计算机的网络连接，提交工作流，观察 Temporal 自动重试，然后恢复网络以查看其恢复情况。

1. 断开计算机与互联网的连接（例如，关闭 Wi-Fi）。
2. 提交工作流：

   ```
   python -m start_workflow "tell me a joke"
   ```
3. 检查 Temporal 界面 (`http://localhost:8233`)。您会看到 LLM 活动失败，而 Temporal 会在后台自动管理重试。
4. 重新连接到互联网。
5. 下一次自动重试将成功访问 Gemini API，并且您的终端将打印最终结果。

### 在工作器崩溃后继续运行

在此测试中，您将在执行过程中终止工作器并重新启动它。Temporal 会重放工作流历史记录（事件源），并从上次完成的 activity 继续执行，已完成的 LLM 调用和工具调用不会重复执行。

1. 为了给自己留出时间来终止 worker，请打开 `durable_agent_worker.py` 并暂时取消 `AgentWorkflow`
   `run` 循环内的 `await asyncio.sleep(10)` 的注释。
2. 重启工作器：

   ```
   python -m durable_agent_worker
   ```
3. 提交会触发多种工具的查询：

   ```
   python -m start_workflow "are there any weather alerts where I am?"
   ```
4. 在完成之前随时终止工作器进程（在工作器终端中按 `Ctrl-C`，或者如果工作器在后台运行，则使用 `kill %1`）。
5. 重启工作器：

   ```
   python -m durable_agent_worker
   ```

Temporal 会重放工作流历史记录。已完成的 LLM 调用和工具调用**不会**重新执行，其结果会立即从历史记录（事件日志）中重放。工作流成功完成。

## 更多资源

- [Temporal 文档](https://docs.temporal.io/)
- [Temporal Python SDK](https://docs.temporal.io/develop/python)
- [Google GenAI SDK](https://googleapis.github.io/python-genai/)
- [本教程的源代码](https://github.com/temporal-community/durable-react-agent-gemini)

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-06-22。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-06-22。"],[],[]]
