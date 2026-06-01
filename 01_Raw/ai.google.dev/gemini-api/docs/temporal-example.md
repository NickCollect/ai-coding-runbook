---
source_url: https://ai.google.dev/gemini-api/docs/temporal-example?hl=vi
fetched_at: 2026-06-01T06:06:46.715949+00:00
title: "T\u00e1c nh\u00e2n AI b\u1ec1n v\u1eefng v\u1edbi Gemini v\u00e0 Temporal \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Tác nhân AI bền vững với Gemini và Temporal

Hướng dẫn này hướng dẫn bạn cách xây dựng một vòng lặp có tác nhân [theo kiểu ReAct](https://arxiv.org/abs/2210.03629) sử dụng Gemini API để suy luận và [Temporal](https://temporal.io/) để duy trì.
Bạn có thể xem toàn bộ mã nguồn của hướng dẫn này trên [GitHub](https://github.com/temporal-community/durable-react-agent-gemini).

Trợ lý có thể gọi các công cụ, chẳng hạn như tra cứu cảnh báo thời tiết hoặc xác định vị trí địa lý của địa chỉ IP và sẽ lặp lại cho đến khi có đủ thông tin để phản hồi.

Điểm khác biệt giữa bản minh hoạ này và bản minh hoạ tác nhân thông thường là **độ bền**. Mọi lệnh gọi LLM, mọi lệnh gọi công cụ và mọi bước của vòng lặp dựa trên tác nhân đều được Temporal duy trì. Nếu quy trình gặp sự cố, mạng bị ngắt hoặc API hết thời gian chờ, Temporal sẽ tự động thử lại và tiếp tục từ bước đã hoàn tất gần đây nhất. Không có nhật ký cuộc trò chuyện nào bị mất và không có lệnh gọi công cụ nào bị lặp lại không chính xác.

## Kiến trúc

Cấu trúc này bao gồm 3 phần:

- **Quy trình công việc:** Vòng lặp có tác nhân điều phối logic thực thi.
- **Hoạt động:** Các đơn vị công việc riêng lẻ (lệnh gọi LLM, lệnh gọi công cụ) mà Temporal duy trì.
- **Worker:** Quy trình thực thi quy trình công việc và hoạt động.

Trong ví dụ này, bạn sẽ đặt cả 3 phần này vào một tệp duy nhất (`durable_agent_worker.py`). Trong quá trình triển khai thực tế, bạn sẽ tách chúng ra để có nhiều lợi thế về việc triển khai và khả năng mở rộng. Bạn sẽ đặt mã cung cấp lời nhắc cho tác nhân trong tệp thứ hai (`start_workflow.py`).

## Điều kiện tiên quyết

Để hoàn tất hướng dẫn này, bạn cần:

- Khoá Gemini API. Bạn có thể tạo một khoá API miễn phí trong [Google AI Studio](https://aistudio.google.com/apikey?hl=vi).
- [Python](https://www.python.org/downloads/) phiên bản 3.10 trở lên.
- [Temporal CLI](https://docs.temporal.io/cli) để chạy máy chủ phát triển cục bộ.

## Thiết lập

Trước khi bắt đầu, hãy đảm bảo bạn có một [máy chủ phát triển Temporal](https://docs.temporal.io/cli#start-dev-server) đang chạy cục bộ:

```
temporal server start-dev
```

Tiếp theo, hãy cài đặt các phần phụ thuộc bắt buộc:

```
pip install temporalio google-genai httpx pydantic python-dotenv
```

Tạo một tệp `.env` trong thư mục dự án bằng khoá Gemini API của bạn. Bạn có thể lấy khoá API từ [Google AI Studio](https://aistudio.google.com/apikey?hl=vi).

```
echo "GOOGLE_API_KEY=your-api-key-here" > .env
```

## Triển khai

Phần còn lại của hướng dẫn này sẽ trình bày về `durable_agent_worker.py` từ trên xuống dưới, từng bước xây dựng tác nhân. Tạo tệp và làm theo.

### Nhập và thiết lập hộp cát

Bắt đầu bằng những nội dung nhập phải được xác định trước. Khối `workflow.unsafe.imports_passed_through()` cho biết hộp cát quy trình công việc của Temporal cho phép một số mô-đun nhất định đi qua mà không bị hạn chế. Điều này là cần thiết vì một số thư viện (đáng chú ý là `httpx`, phân lớp con `urllib.request.Request`) sử dụng các mẫu mà hộp cát sẽ chặn.

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

### Hướng dẫn về hệ thống

Tiếp theo, hãy xác định tính cách của trợ lý. Các chỉ dẫn hệ thống cho mô hình biết cách hoạt động. Nhân viên hỗ trợ này được hướng dẫn phản hồi bằng thơ hai câu khi không cần dùng công cụ.

```
SYSTEM_INSTRUCTIONS = """
You are a helpful agent that can use tools to help the user.
You will be given an input from the user and a list of tools to use.
You may or may not need to use the tools to satisfy the user ask.
If no tools are needed, respond in haikus.
"""
```

### Định nghĩa về công cụ

Bây giờ, hãy xác định những công cụ mà tác nhân có thể sử dụng. Mỗi công cụ là một hàm không đồng bộ có chuỗi tài liệu mô tả. Các công cụ nhận tham số sẽ sử dụng một mô hình Pydantic làm đối số duy nhất. Đây là phương pháp hay nhất của Temporal giúp chữ ký hoạt động ổn định khi bạn thêm các trường không bắt buộc theo thời gian.

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

Tiếp theo, hãy xác định các công cụ để xác định vị trí địa lý theo địa chỉ IP:

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

### Sổ đăng ký công cụ

Tiếp theo, hãy tạo một sổ đăng ký ánh xạ tên công cụ đến các hàm trình xử lý. Hàm `get_tools()` tạo các đối tượng `FunctionDeclaration` tương thích với Gemini từ các lệnh gọi bằng cách sử dụng `FunctionDeclaration.from_callable_with_api_option()`.

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

### Hoạt động của LLM

Bây giờ, hãy xác định hoạt động gọi Gemini API. Các lớp dữ liệu `GeminiChatRequest` và `GeminiChatResponse` xác định hợp đồng.

Bạn sẽ tắt tính năng tự động gọi hàm để lời gọi LLM và lời gọi công cụ được xử lý dưới dạng các tác vụ riêng biệt, giúp tăng độ bền cho tác nhân của bạn. Bạn cũng sẽ tắt các lần thử lại tích hợp của SDK (`attempts=1`) vì Temporal xử lý các lần thử lại một cách bền bỉ.

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

### Hoạt động của công cụ động

Tiếp theo, hãy xác định hoạt động thực thi các công cụ. Thao tác này sử dụng tính năng hoạt động động của Temporal: trình xử lý công cụ (một đối tượng có thể gọi) được lấy từ sổ đăng ký công cụ thông qua hàm `get_handler`. Nhờ đó, bạn có thể xác định nhiều tác nhân chỉ bằng cách cung cấp một bộ công cụ và hướng dẫn hệ thống khác; quy trình triển khai vòng lặp dựa trên tác nhân không cần thay đổi.

Hoạt động này kiểm tra chữ ký của trình xử lý để xác định cách truyền đối số. Nếu trình xử lý dự kiến nhận một mô hình Pydantic, thì trình xử lý đó sẽ xử lý định dạng đầu ra lồng nhau mà Gemini tạo ra (ví dụ: `{"request": {"state": "CA"}}` thay vì `{"state": "CA"}` đơn giản).

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

### Quy trình công việc của vòng lặp AI tác nhân

Giờ đây, bạn đã có tất cả các thành phần để hoàn tất việc tạo tác nhân. Lớp `AgentWorkflow` triển khai một quy trình công việc chứa vòng lặp của tác nhân. Trong vòng lặp đó, LLM được gọi thông qua hoạt động (giúp hoạt động này bền vững), đầu ra được kiểm tra và nếu LLM đã chọn một công cụ, thì công cụ đó sẽ được gọi thông qua `dynamic_tool_activity`.

Trong tác nhân kiểu ReAct đơn giản này, sau khi LLM chọn không sử dụng một công cụ, vòng lặp sẽ được coi là hoàn tất và kết quả LLM cuối cùng sẽ được trả về.

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

Vòng lặp có tác nhân hoàn toàn bền vững. Nếu worker của tác nhân gặp sự cố sau một số lần lặp lại trong vòng lặp, Temporal sẽ tiếp tục chính xác từ nơi worker dừng lại mà không cần gọi lại các lệnh gọi LLM hoặc lệnh gọi công cụ đã thực thi.

### Khởi động worker

Cuối cùng, hãy kết nối mọi thứ với nhau. Mặc dù mã này triển khai logic nghiệp vụ cần thiết theo cách khiến mã có vẻ đang chạy trong một quy trình duy nhất, nhưng việc sử dụng Temporal sẽ biến mã này thành một hệ thống dựa trên sự kiện (cụ thể là dựa trên nguồn sự kiện) trong đó hoạt động giao tiếp giữa quy trình công việc và các hoạt động diễn ra thông qua tính năng nhắn tin do Temporal cung cấp.

Worker Temporal kết nối với dịch vụ Temporal và đóng vai trò là trình lập lịch biểu cho các tác vụ quy trình làm việc và hoạt động. Worker đăng ký quy trình và cả hai hoạt động, sau đó bắt đầu nghe các tác vụ.

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

## Tập lệnh phía máy khách

Tạo tập lệnh máy khách (`start_workflow.py`). Tập lệnh này gửi một truy vấn và chờ kết quả. Lưu ý rằng nó kết nối với cùng một hàng đợi tác vụ được tham chiếu trong worker của tác nhân – tập lệnh `start_workflow` sẽ gửi một tác vụ quy trình làm việc có lời nhắc của người dùng đến hàng đợi tác vụ đó, bắt đầu quá trình thực thi tác nhân.

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

## Chạy tác nhân

Nếu bạn chưa làm, hãy khởi động máy chủ phát triển Temporal:

```
temporal server start-dev
```

Trong một cửa sổ dòng lệnh mới, hãy bắt đầu trình chạy tác nhân:

```
python -m durable_agent_worker
```

Trong cửa sổ dòng lệnh thứ ba, hãy gửi một truy vấn đến tác nhân của bạn:

```
python -m start_workflow "are there any weather alerts for where I am?"
```

Lưu ý đầu ra trong thiết bị đầu cuối của `durable_agent_worker` cho biết các hành động xảy ra trong mỗi lần lặp của vòng lặp dựa trên tác nhân. LLM có thể đáp ứng yêu cầu của người dùng bằng cách gọi một loạt công cụ theo ý mình. Bạn có thể xem các bước đã thực hiện thông qua giao diện người dùng Temporal tại `http://localhost:8233/namespaces/default/workflows`.

Hãy thử một vài câu lệnh khác nhau để xem lý do của nhân viên và các công cụ gọi:

```
python -m start_workflow "are there any weather alerts for New York?"
python -m start_workflow "where am I?"
python -m start_workflow "what is my ip address?"
python -m start_workflow "tell me a joke"
```

Câu lệnh cuối cùng không yêu cầu bất kỳ công cụ nào, vì vậy, tác nhân sẽ phản hồi bằng một bài thơ haiku dựa trên `SYSTEM_INSTRUCTIONS`.

## Kiểm tra độ bền (Không bắt buộc)

Việc xây dựng trên Temporal đảm bảo tác nhân của bạn hoạt động liền mạch khi gặp sự cố. Bạn có thể kiểm thử việc này bằng hai thử nghiệm riêng biệt.

### Mô phỏng tình trạng mất mạng

Trong thử nghiệm này, bạn sẽ tạm thời tắt kết nối Internet của máy tính, gửi một quy trình làm việc, xem Temporal tự động thử lại, sau đó khôi phục mạng để xem quy trình này khôi phục.

1. Ngắt kết nối máy tính với Internet (ví dụ: tắt Wi-Fi).
2. Gửi quy trình công việc:

   ```
   python -m start_workflow "tell me a joke"
   ```
3. Kiểm tra giao diện người dùng Temporal (`http://localhost:8233`). Bạn sẽ thấy hoạt động LLM không thành công và Temporal tự động quản lý các lần thử lại ở chế độ nền.
4. Kết nối lại với Internet.
5. Lần thử lại tự động tiếp theo sẽ kết nối thành công với Gemini API và thiết bị đầu cuối của bạn sẽ in kết quả cuối cùng.

### Sống sót sau sự cố của worker

Trong kiểm thử này, bạn sẽ huỷ worker khi đang thực thi và khởi động lại worker đó. Phát lại tạm thời nhật ký quy trình làm việc (nguồn sự kiện) và tiếp tục từ hoạt động đã hoàn thành gần đây nhất – các lệnh gọi LLM và lệnh gọi công cụ đã hoàn thành sẽ không được lặp lại.

1. Để có thời gian dừng worker, hãy mở `durable_agent_worker.py` và tạm thời bỏ chú thích `await asyncio.sleep(10)` bên trong vòng lặp `AgentWorkflow`
   `run`.
2. Khởi động lại worker:

   ```
   python -m durable_agent_worker
   ```
3. Gửi một cụm từ tìm kiếm kích hoạt nhiều công cụ:

   ```
   python -m start_workflow "are there any weather alerts where I am?"
   ```
4. Huỷ quy trình worker bất cứ lúc nào trước khi hoàn tất (`Ctrl-C` trong thiết bị đầu cuối worker hoặc sử dụng `kill %1` nếu đang chạy ở chế độ nền).
5. Khởi động lại worker:

   ```
   python -m durable_agent_worker
   ```

Temporal phát lại nhật ký quy trình làm việc. Các lệnh gọi LLM và lệnh gọi công cụ đã hoàn tất sẽ **không** được thực thi lại – kết quả của các lệnh gọi này sẽ được phát lại ngay lập tức từ nhật ký (nhật ký sự kiện). Quy trình công việc hoàn tất thành công.

## Tài nguyên khác

- [Tài liệu về Temporal](https://docs.temporal.io/)
- [Temporal Python SDK](https://docs.temporal.io/develop/python)
- [SDK AI tạo sinh của Google](https://googleapis.github.io/python-genai/)
- [Mã nguồn cho hướng dẫn này](https://github.com/temporal-community/durable-react-agent-gemini)

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-05-19 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-05-19 UTC."],[],[]]
