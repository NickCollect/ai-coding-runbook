---
source_url: https://ai.google.dev/gemini-api/docs/temporal-example?hl=zh-TW
fetched_at: 2026-11-02T07:10:41.556603+00:00
title: "\u4f7f\u7528 Gemini \u548c Temporal \u6253\u9020\u6301\u4e45\u578b AI \u4ee3\u7406 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon 現已推出，[立即試用](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=zh-tw)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google 會運用 AI 技術將內容翻譯成你偏好的語言，但可能會出錯。

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 使用 Gemini 和 Temporal 打造持久型 AI 代理

本教學課程將逐步說明如何建構 [ReAct 樣式](https://arxiv.org/abs/2210.03629)的代理功能迴圈，使用 Gemini API 進行推論，並使用 [Temporal](https://temporal.io/) 確保持久性。您可以在 [GitHub](https://github.com/temporal-community/durable-react-agent-gemini) 上取得本教學課程的完整原始碼。

代理程式可以呼叫工具，例如查詢天氣警報或 IP 位址的地理位置，並會重複執行，直到取得足夠資訊來回應。

這與一般代理程式試用版不同之處在於**耐用性**。Temporal 會保存每次 LLM 呼叫、每次工具叫用，以及代理程式迴圈的每個步驟。如果程序當機、網路中斷或 API 超時，Temporal 會自動重試，並從上次完成的步驟繼續執行。不會遺失任何對話記錄，也不會錯誤地重複工具呼叫。

## 架構

這個架構包含三個部分：

- **工作流程：**調度管理執行邏輯的代理迴圈。
- **活動：**Temporal 持久化的個別工作單元 (LLM 呼叫、工具呼叫)。
- **工作站：**執行工作流程和活動的程序。

在本範例中，您會將這三個部分全部放在單一檔案 (`durable_agent_worker.py`) 中。在實際導入作業中，您會將這些部分分開，以享有各種部署和擴充性優勢。您會在第二個檔案 (`start_workflow.py`) 中，放置向代理程式提供提示的程式碼。

## 必要條件

如要完成本指南，您需要：

- Gemini API 金鑰。您可以在 [Google AI Studio](https://aistudio.google.com/apikey?hl=zh-tw) 中免費建立。
- [Python](https://www.python.org/downloads/) 3.10 以上版本。
- [Temporal CLI](https://docs.temporal.io/cli)，用於執行本機開發伺服器。

## 設定

開始前，請先確認您已在本機執行 [Temporal 開發伺服器](https://docs.temporal.io/cli#start-dev-server)：

```
temporal server start-dev
```

接著，請安裝必要的依附元件：

```
pip install temporalio google-genai httpx pydantic python-dotenv
```

在專案目錄中建立 `.env` 檔案，並加入 Gemini API 金鑰。您可以從 [Google AI Studio](https://aistudio.google.com/apikey?hl=zh-tw) 取得 API 金鑰。

```
echo "GOOGLE_API_KEY=your-api-key-here" > .env
```

## 導入作業

本教學課程的其餘部分會從上到下逐步說明 `durable_agent_worker.py`，逐步建構代理程式。建立檔案並逐步操作。

### 匯入和沙箱設定

首先，請定義必須預先定義的匯入項目。`workflow.unsafe.imports_passed_through()` 區塊會告知 Temporal 的工作流程沙箱，允許特定模組通過，不受限制。這是必要步驟，因為有幾個程式庫 (特別是 `httpx`，這是 `urllib.request.Request` 的子類別) 使用沙箱會封鎖的模式。

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

### 系統指示

接著，定義代理的個性。系統指令會告訴模型應如何運作。如果不需要任何工具，這個代理程式會以俳句回覆。

```
SYSTEM_INSTRUCTIONS = """
You are a helpful agent that can use tools to help the user.
You will be given an input from the user and a list of tools to use.
You may or may not need to use the tools to satisfy the user ask.
If no tools are needed, respond in haikus.
"""
```

### 工具定義

現在定義代理可使用的工具。每項工具都是具有說明性文件字串的非同步函式。採用參數的工具會使用 Pydantic 模型做為單一引數。這是 Temporal 最佳做法，可確保活動簽章穩定，方便您隨時間新增選用欄位。

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

接下來，請定義 IP 位址地理位置的工具：

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

### 工具儲存庫

接著，建立將工具名稱對應至處理常式函式的登錄。`get_tools()` 函式會使用 `FunctionDeclaration.from_callable_with_api_option()`，從可呼叫項產生與 Gemini 相容的 `FunctionDeclaration` 物件。

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

### LLM 活動

現在請定義呼叫 Gemini API 的活動。`GeminiChatRequest` 和 `GeminiChatResponse` 資料類別會定義合約。

您將停用自動函式呼叫功能，讓 LLM 叫用和工具叫用以個別工作處理，進一步提升代理的耐用性。您也會停用 SDK 的內建重試機制 (`attempts=1`)，因為 Temporal 會以耐久方式處理重試。

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

### 動態工具活動

接著，定義執行工具的活動。這項功能會使用 Temporal 的動態活動功能：工具處理常式 (可呼叫的項目) 是透過 `get_handler` 函式從工具登錄檔取得。只要提供不同的工具和系統指令，就能定義不同的代理程式，實作代理程式迴圈的工作流程不需要任何變更。

活動會檢查處理常式的簽章，判斷如何傳遞引數。如果處理常式預期會收到 Pydantic 模型，就會處理 Gemini 產生的巢狀輸出格式 (例如 `{"request": {"state": "CA"}}`，而非平面 `{"state": "CA"}`)。

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

### 代理迴圈工作流程

現在您已掌握所有元素，可以完成建構代理程式。`AgentWorkflow` 類別會實作包含代理程式迴圈的工作流程。在該迴圈中，系統會透過活動叫用 LLM (使其成為耐久活動)、檢查輸出內容，如果 LLM 選擇了工具，系統就會透過 `dynamic_tool_activity` 叫用該工具。

在這個簡單的 ReAct 樣式代理程式中，一旦 LLM 選擇不使用工具，系統就會視為迴圈完成，並傳回最終的 LLM 結果。

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
                    model="gemini-3.6-flash",
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

代理循環完全耐用。如果代理程式工作人員在多次疊代迴圈後當機，Temporal 會從中斷處繼續執行，不需要重新叫用已執行的 LLM 叫用或工具呼叫。

### 啟動工作站

最後，將所有裝置接在一起。雖然程式碼會以看似在單一程序中執行的形式，實作必要的商業邏輯，但使用 Temporal 會讓程式碼成為事件驅動系統 (具體來說，是事件來源系統)，工作流程和活動之間的通訊會透過 Temporal 提供的訊息傳遞。

Temporal 工作站會連線至 Temporal 服務，並做為工作流程和活動工作的排程器。工作站會註冊工作流程和這兩項活動，然後開始接聽工作。

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

## 用戶端指令碼

建立用戶端指令碼 (`start_workflow.py`)。這個指令碼會提交查詢並等待結果。請注意，這會連線至代理程式工作站中參照的相同工作佇列，`start_workflow` 指令碼會將含有使用者提示的工作流程工作分派至該工作佇列，啟動代理程式的執行作業。

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

## 執行代理程式

如果尚未啟動 Temporal 開發伺服器，請執行下列操作：

```
temporal server start-dev
```

在新的終端機視窗中，啟動代理程式工作人員：

```
python -m durable_agent_worker
```

在第三個終端機視窗中，向代理程式提交查詢：

```
python -m start_workflow "are there any weather alerts for where I am?"
```

請注意 `durable_agent_worker` 終端機中的輸出內容，當中會顯示代理程式迴圈每次疊代時執行的動作。LLM 可以透過呼叫一系列可用工具，滿足使用者要求。您可以在 `http://localhost:8233/namespaces/default/workflows` 的 Temporal UI 中查看執行的步驟。

嘗試幾個不同的提示詞，看看代理的理由和可用的工具：

```
python -m start_workflow "are there any weather alerts for New York?"
python -m start_workflow "where am I?"
python -m start_workflow "what is my ip address?"
python -m start_workflow "tell me a joke"
```

最後一個提示不需要任何工具，因此代理會根據 `SYSTEM_INSTRUCTIONS`，以俳句形式回覆。

## 測試耐用性 (選用)

以 Temporal 為基礎建構代理程式，可確保代理程式順暢地從失敗中復原。您可以透過兩項不同的實驗進行測試。

### 模擬網路中斷

在這項測試中，您會暫時停用電腦的網際網路連線、提交工作流程、觀察 Temporal 自動重試，然後還原網路，看看系統是否會復原。

1. 中斷電腦的網際網路連線 (例如關閉 Wi-Fi)。
2. 提交工作流程：

   ```
   python -m start_workflow "tell me a joke"
   ```
3. 檢查 Temporal UI (`http://localhost:8233`)。您會看到 LLM 活動失敗，而 Temporal 會在背景自動管理重試作業。
4. 重新連上網際網路。
5. 下一次自動重試時，系統會成功連上 Gemini API，而終端機也會列印最終結果。

### 在工作站當機後繼續作業

在這項測試中，您會在執行作業期間終止並重新啟動 worker。時間性重播會重播工作流程記錄 (事件來源)，並從上次完成的活動繼續執行，不會重複執行已完成的 LLM 呼叫和工具呼叫。

1. 如要爭取時間終止 worker，請開啟 `durable_agent_worker.py`，並暫時取消 `AgentWorkflow`
   `run` 迴圈內的 `await asyncio.sleep(10)` 註解。
2. 重新啟動工作站：

   ```
   python -m durable_agent_worker
   ```
3. 提交會觸發多種工具的查詢：

   ```
   python -m start_workflow "are there any weather alerts where I am?"
   ```
4. 在完成前隨時終止 worker 程序 (在 worker 終端機中按 `Ctrl-C`，或在背景執行時使用 `kill %1`)。
5. 重新啟動工作站：

   ```
   python -m durable_agent_worker
   ```

Temporal 會重播工作流程記錄。系統**不會**重新執行已完成的 LLM 呼叫和工具叫用作業，而是會立即從記錄 (事件記錄) 重新播放結果。工作流程順利完成。

## 其他資源

- [Temporal 說明文件](https://docs.temporal.io/)
- [Temporal Python SDK](https://docs.temporal.io/develop/python)
- [Google GenAI SDK](https://googleapis.github.io/python-genai/)
- [本教學課程的原始碼](https://github.com/temporal-community/durable-react-agent-gemini)

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-09-12 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-09-12 (世界標準時間)。"],[],[]]
