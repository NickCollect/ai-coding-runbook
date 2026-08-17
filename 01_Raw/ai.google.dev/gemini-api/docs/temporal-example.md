---
source_url: https://ai.google.dev/gemini-api/docs/temporal-example?hl=th
fetched_at: 2026-08-17T02:32:59.311564+00:00
title: "\u0e40\u0e2d\u0e40\u0e08\u0e19\u0e15\u0e4c AI \u0e17\u0e35\u0e48\u0e17\u0e19\u0e17\u0e32\u0e19\u0e14\u0e49\u0e27\u0e22 Gemini \u0e41\u0e25\u0e30 Temporal \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

ตอนนี้ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) พร้อมให้บริการแก่ผู้ใช้ทั่วไปแล้ว เราขอแนะนำให้ใช้ API นี้เพื่อเข้าถึงฟีเจอร์และโมเดลล่าสุดทั้งหมด

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# เอเจนต์ AI ที่ทนทานด้วย Gemini และ Temporal

บทแนะนำนี้จะอธิบายขั้นตอนการสร้างลูปของ Agent ในสไตล์
[ReAct](https://arxiv.org/abs/2210.03629) ที่ใช้
Gemini API สำหรับการให้เหตุผลและ [Temporal](https://temporal.io/) สำหรับความทนทาน
ซอร์สโค้ดฉบับสมบูรณ์สำหรับบทแนะนำนี้พร้อมให้บริการบน
[GitHub](https://github.com/temporal-community/durable-react-agent-gemini)

Agent สามารถเรียกใช้เครื่องมือต่างๆ ได้ เช่น การค้นหาการแจ้งเตือนสภาพอากาศหรือการระบุตำแหน่งทางภูมิศาสตร์ของที่อยู่ IP และจะวนซ้ำจนกว่าจะมีข้อมูลเพียงพอที่จะตอบกลับ

สิ่งที่ทำให้ Agent นี้แตกต่างจากการสาธิต Agent ทั่วไปคือ**ความทนทาน** Temporal จะเก็บรักษาการเรียกใช้ LLM, การเรียกใช้เครื่องมือ และทุกขั้นตอนของลูปของ Agent หากกระบวนการขัดข้อง เครือข่ายขาดการเชื่อมต่อ หรือ API หมดเวลา Temporal จะลองอีกครั้งโดยอัตโนมัติและดำเนินการต่อจากขั้นตอนสุดท้ายที่เสร็จสมบูรณ์ ระบบจะไม่สูญเสียประวัติการสนทนาและจะไม่เรียกใช้เครื่องมือซ้ำอย่างไม่ถูกต้อง

## สถาปัตยกรรม

สถาปัตยกรรมประกอบด้วย 3 ส่วนดังนี้

- **เวิร์กโฟลว์:** ลูปของ Agent ที่จัดระเบียบตรรกะการดำเนินการ
- **กิจกรรม:** หน่วยงานแต่ละหน่วย (การเรียกใช้ LLM, การเรียกใช้เครื่องมือ) ที่ Temporal ทำให้ทนทาน
- **Worker:** กระบวนการที่ดำเนินการเวิร์กโฟลว์และกิจกรรม

ในตัวอย่างนี้ คุณจะวางทั้ง 3 ส่วนนี้ไว้ในไฟล์เดียว (`durable_agent_worker.py`) แต่ในการใช้งานจริง คุณควรแยกส่วนต่างๆ ออกจากกันเพื่อให้ได้รับประโยชน์ต่างๆ ในด้านการติดตั้งใช้งานและความสามารถในการปรับขนาด คุณจะวางโค้ดที่ส่งพรอมต์ไปยัง Agent ไว้ในไฟล์ที่ 2 (`start_workflow.py`)

## ข้อกำหนดเบื้องต้น

สิ่งที่ต้องมีเพื่อให้ทำตามคำแนะนำนี้ได้

- คีย์ Gemini API คุณสร้างคีย์ได้ฟรีใน
  [Google AI Studio](https://aistudio.google.com/apikey?hl=th)
- [Python](https://www.python.org/downloads/) เวอร์ชัน 3.10 ขึ้นไป
- [Temporal CLI](https://docs.temporal.io/cli) สำหรับเรียกใช้เซิร์ฟเวอร์การพัฒนาซอฟต์แวร์ภายใน

## ตั้งค่า

ก่อนเริ่มต้น ให้ตรวจสอบว่าคุณมี
[เซิร์ฟเวอร์การพัฒนาซอฟต์แวร์ Temporal](https://docs.temporal.io/cli#start-dev-server)
ที่ทำงานภายในเครื่อง

```
temporal server start-dev
```

จากนั้นติดตั้งการอ้างอิงที่จำเป็น

```
pip install temporalio google-genai httpx pydantic python-dotenv
```

สร้างไฟล์ `.env` ในไดเรกทอรีโปรเจ็กต์ด้วยคีย์ Gemini API คุณ
รับคีย์ API ได้จาก
[Google AI Studio](https://aistudio.google.com/apikey?hl=th)

```
echo "GOOGLE_API_KEY=your-api-key-here" > .env
```

## การใช้งาน

ส่วนที่เหลือของบทแนะนำนี้จะอธิบาย `durable_agent_worker.py` ตั้งแต่ต้นจนจบ โดยสร้าง Agent ขึ้นทีละส่วน สร้างไฟล์แล้วทำตาม

### การนำเข้าและการตั้งค่าแซนด์บ็อกซ์

เริ่มต้นด้วยการนำเข้าที่ต้องกำหนดไว้ล่วงหน้า บล็อก `workflow.unsafe.imports_passed_through()` จะบอกให้แซนด์บ็อกซ์เวิร์กโฟลว์ของ Temporal อนุญาตให้โมดูลบางโมดูลผ่านได้โดยไม่มีข้อจำกัด ซึ่งจำเป็นเนื่องจากไลบรารีหลายรายการ (โดยเฉพาะ `httpx` ซึ่งเป็นคลาสย่อยของ `urllib.request.Request`) ใช้รูปแบบที่แซนด์บ็อกซ์จะบล็อก

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

### วิธีการของระบบ

จากนั้นกำหนดบุคลิกของ Agent วิธีการของระบบจะบอกให้โมเดลทราบถึงวิธีแสดงพฤติกรรม Agent นี้ได้รับคำสั่งให้ตอบกลับเป็นไฮกุเมื่อไม่จำเป็นต้องใช้เครื่องมือ

```
SYSTEM_INSTRUCTIONS = """
You are a helpful agent that can use tools to help the user.
You will be given an input from the user and a list of tools to use.
You may or may not need to use the tools to satisfy the user ask.
If no tools are needed, respond in haikus.
"""
```

### คำจำกัดความของเครื่องมือ

ตอนนี้ให้กำหนดเครื่องมือที่ Agent ใช้ได้ เครื่องมือแต่ละอย่างเป็นฟังก์ชันแบบไม่พร้อมกันที่มีสตริงเอกสารอธิบาย เครื่องมือที่ใช้พารามิเตอร์จะใช้โมเดล Pydantic เป็นอาร์กิวเมนต์เดียว นี่เป็นแนวทางปฏิบัติแนะนำของ Temporal ที่ช่วยให้ลายเซ็นของกิจกรรมมีเสถียรภาพเมื่อคุณเพิ่มช่องที่ไม่บังคับเมื่อเวลาผ่านไป

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

จากนั้นกำหนดเครื่องมือสำหรับการระบุตำแหน่งทางภูมิศาสตร์ของที่อยู่ IP

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

### รีจิสทรีเครื่องมือ

จากนั้นสร้างรีจิสทรีที่แมปชื่อเครื่องมือกับฟังก์ชันตัวแฮนเดิล ฟังก์ชัน
`get_tools()` จะสร้างออบเจ็กต์ที่เข้ากันได้กับ Gemini `FunctionDeclaration` จากฟังก์ชันที่เรียกใช้ได้โดยใช้ `FunctionDeclaration.from_callable_with_api_option()`

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

### กิจกรรม LLM

ตอนนี้ให้กำหนดกิจกรรมที่เรียกใช้ Gemini API คลาสข้อมูล `GeminiChatRequest` และ `GeminiChatResponse` จะกำหนดสัญญา

คุณจะปิดใช้การเรียกใช้ฟังก์ชันอัตโนมัติเพื่อให้ระบบจัดการการเรียกใช้ LLM และการเรียกใช้เครื่องมือเป็นงานแยกกัน ซึ่งจะช่วยเพิ่มความทนทานให้กับ Agent นอกจากนี้ คุณยังจะปิดใช้การลองอีกครั้งในตัวของ SDK (`attempts=1`) เนื่องจาก Temporal จัดการการลองอีกครั้งได้อย่างทนทาน

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

### กิจกรรมเครื่องมือแบบไดนามิก

จากนั้นกำหนดกิจกรรมที่ดำเนินการเครื่องมือ ซึ่งใช้ฟีเจอร์กิจกรรมแบบไดนามิกของ Temporal โดยระบบจะรับตัวแฮนเดิลเครื่องมือ (ฟังก์ชันที่เรียกใช้ได้) จากรีจิสทรีเครื่องมือผ่านฟังก์ชัน `get_handler` วิธีนี้ช่วยให้กำหนด Agent ต่างๆ ได้ง่ายๆ เพียงแค่ระบุชุดเครื่องมือและวิธีการของระบบที่แตกต่างกัน โดยเวิร์กโฟลว์ที่ใช้ลูปของ Agent ไม่จำเป็นต้องมีการเปลี่ยนแปลง

กิจกรรมจะตรวจสอบลายเซ็นของตัวจัดการเพื่อกำหนดวิธีส่งอาร์กิวเมนต์ หากตัวจัดการคาดหวังโมเดล Pydantic ระบบจะจัดการรูปแบบเอาต์พุตที่ซ้อนกันซึ่ง Gemini สร้างขึ้น (เช่น `{"request": {"state": "CA"}}` แทนที่จะเป็น `{"state": "CA"}` แบบแบน)

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

### เวิร์กโฟลว์ลูปของ Agent

ตอนนี้คุณมีทุกส่วนที่จำเป็นในการสร้าง Agent ให้เสร็จสมบูรณ์แล้ว คลาส `AgentWorkflow` ใช้เวิร์กโฟลว์ที่มีลูปของ Agent ภายในลูปนั้น ระบบจะเรียกใช้ LLM ผ่านกิจกรรม (ทำให้ทนทาน) ตรวจสอบเอาต์พุต และหาก LLM เลือกเครื่องมือ ระบบจะเรียกใช้เครื่องมือผ่าน `dynamic_tool_activity`

ใน Agent สไตล์ ReAct อย่างง่ายนี้ เมื่อ LLM เลือกที่จะไม่ใช้เครื่องมือ ระบบจะถือว่าลูปเสร็จสมบูรณ์และส่งคืนผลลัพธ์สุดท้ายของ LLM

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

ลูปของ Agent มีความทนทานอย่างเต็มที่ หาก Worker ของ Agent ขัดข้องหลังจากวนซ้ำหลายครั้ง Temporal จะดำเนินการต่อจากจุดที่หยุดไว้โดยไม่ต้องเรียกใช้การเรียกใช้ LLM หรือการเรียกใช้เครื่องมือที่ดำเนินการไปแล้วอีกครั้ง

### การเริ่มต้น Worker

สุดท้ายให้เชื่อมต่อทุกอย่างเข้าด้วยกัน แม้ว่าโค้ดจะใช้ตรรกะทางธุรกิจที่จำเป็นในลักษณะที่ทำให้ดูเหมือนว่ากำลังทำงานในกระบวนการเดียว แต่การใช้ Temporal จะทำให้ระบบเป็นระบบที่ขับเคลื่อนด้วยเหตุการณ์ (โดยเฉพาะอย่างยิ่งระบบที่ใช้การจัดเก็บข้อมูลเหตุการณ์) ซึ่งการสื่อสารระหว่างเวิร์กโฟลว์และกิจกรรมจะเกิดขึ้นผ่านการรับส่งข้อความที่ Temporal จัดเตรียมไว้

Worker ของ Temporal จะเชื่อมต่อกับบริการ Temporal และทำหน้าที่เป็นตัวจัดตารางเวลาสำหรับเวิร์กโฟลว์และงานกิจกรรม Worker จะลงทะเบียนเวิร์กโฟลว์และกิจกรรมทั้ง 2 อย่าง จากนั้นจะเริ่มรอรับงาน

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

## สคริปต์ไคลเอ็นต์

สร้างสคริปต์ไคลเอ็นต์ (`start_workflow.py`) ซึ่งจะส่งคำค้นหาและรอผลลัพธ์ โปรดทราบว่าสคริปต์นี้จะเชื่อมต่อกับคิวงานเดียวกันกับที่อ้างอิงไว้ใน Worker ของ Agent โดยสคริปต์ `start_workflow` จะส่งงานเวิร์กโฟลว์พร้อมพรอมต์ของผู้ใช้ไปยังคิวงานนั้น ซึ่งจะเริ่มการดำเนินการของ Agent

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

## เรียกใช้ Agent

หากยังไม่ได้ดำเนินการ ให้เริ่มเซิร์ฟเวอร์การพัฒนาซอฟต์แวร์ Temporal โดยทำดังนี้

```
temporal server start-dev
```

เริ่ม Worker ของ Agent ในหน้าต่างเทอร์มินัลใหม่โดยทำดังนี้

```
python -m durable_agent_worker
```

ส่งคำค้นหาไปยัง Agent ในหน้าต่างเทอร์มินัลที่ 3 โดยทำดังนี้

```
python -m start_workflow "are there any weather alerts for where I am?"
```

สังเกตเอาต์พุตในเทอร์มินัลของ `durable_agent_worker` ซึ่งแสดงการดำเนินการที่เกิดขึ้นในแต่ละการวนซ้ำของลูปของ Agent LLM สามารถตอบสนองคำขอของผู้ใช้ได้โดยการเรียกใช้เครื่องมือต่างๆ ที่มี คุณดูขั้นตอนที่ดำเนินการได้ผ่าน UI ของ Temporal ที่ `http://localhost:8233/namespaces/default/workflows`

ลองใช้พรอมต์ต่างๆ เพื่อดูเหตุผลและการเรียกใช้เครื่องมือของ Agent โดยทำดังนี้

```
python -m start_workflow "are there any weather alerts for New York?"
python -m start_workflow "where am I?"
python -m start_workflow "what is my ip address?"
python -m start_workflow "tell me a joke"
```

พรอมต์สุดท้ายไม่จำเป็นต้องใช้เครื่องมือใดๆ ดังนั้น Agent จะตอบกลับเป็นไฮกุตาม `SYSTEM_INSTRUCTIONS`

## ทดสอบความทนทาน (ไม่บังคับ)

การสร้าง Agent บน Temporal จะช่วยให้ Agent ทำงานต่อไปได้อย่างราบรื่นเมื่อเกิดข้อผิดพลาด คุณทดสอบได้โดยใช้การทดลอง 2 อย่างที่แตกต่างกัน

### จำลองเครือข่ายขัดข้อง

ในการทดสอบนี้ คุณจะปิดใช้การเชื่อมต่ออินเทอร์เน็ตของคอมพิวเตอร์ชั่วคราว ส่งเวิร์กโฟลว์ ดู Temporal ลองอีกครั้งโดยอัตโนมัติ จากนั้นกู้คืนเครือข่ายเพื่อดูว่าระบบกู้คืนได้หรือไม่

1. ยกเลิกการเชื่อมต่อเครื่องกับอินเทอร์เน็ต (เช่น ปิด Wi-Fi)
2. ส่งเวิร์กโฟลว์โดยทำดังนี้

   ```
   python -m start_workflow "tell me a joke"
   ```
3. ตรวจสอบ UI ของ Temporal (`http://localhost:8233`) คุณจะเห็นว่ากิจกรรม LLM ล้มเหลวและ Temporal จัดการการลองอีกครั้งโดยอัตโนมัติในเบื้องหลัง
4. เชื่อมต่ออินเทอร์เน็ตอีกครั้ง
5. การลองอีกครั้งโดยอัตโนมัติครั้งถัดไปจะเข้าถึง Gemini API ได้สำเร็จ และเทอร์มินัลจะพิมพ์ผลลัพธ์สุดท้าย

### การทำงานต่อไปได้เมื่อ Worker ขัดข้อง

ในการทดสอบนี้ คุณจะหยุดกระบวนการ Worker กลางคันและรีสตาร์ท Temporal จะเล่นประวัติเวิร์กโฟลว์ซ้ำ (การจัดเก็บข้อมูลเหตุการณ์) และดำเนินการต่อจากกิจกรรมสุดท้ายที่เสร็จสมบูรณ์ โดยจะไม่เรียกใช้ LLM และการเรียกใช้เครื่องมือที่เสร็จสมบูรณ์ไปแล้วอีกครั้ง

1. หากต้องการให้มีเวลาหยุด Worker ให้เปิด `durable_agent_worker.py` และยกเลิกการแสดงความคิดเห็น `await asyncio.sleep(10)` ชั่วคราวภายในลูป `run` ของ `AgentWorkflow`
2. รีสตาร์ท Worker โดยทำดังนี้

   ```
   python -m durable_agent_worker
   ```
3. ส่งคำค้นหาที่ทริกเกอร์เครื่องมือหลายอย่างโดยทำดังนี้

   ```
   python -m start_workflow "are there any weather alerts where I am?"
   ```
4. หยุดกระบวนการ Worker ได้ทุกเมื่อก่อนที่จะเสร็จสมบูรณ์ (`Ctrl-C` ในเทอร์มินัลของ Worker หรือใช้ `kill %1` หากทำงานในเบื้องหลัง)
5. รีสตาร์ท Worker โดยทำดังนี้

   ```
   python -m durable_agent_worker
   ```

Temporal จะเล่นประวัติเวิร์กโฟลว์ซ้ำ ระบบจะ**ไม่** เรียกใช้การเรียกใช้ LLM และการเรียกใช้เครื่องมือที่เสร็จสมบูรณ์ไปแล้วอีกครั้ง แต่จะเล่นผลลัพธ์ซ้ำจากประวัติ (บันทึกเหตุการณ์) ทันที เวิร์กโฟลว์จะเสร็จสมบูรณ์

## แหล่งข้อมูลเพิ่มเติม

- [เอกสารประกอบของ Temporal](https://docs.temporal.io/)
- [Temporal Python SDK](https://docs.temporal.io/develop/python)
- [Google GenAI SDK](https://googleapis.github.io/python-genai/)
- [ซอร์สโค้ดสำหรับบทแนะนำนี้](https://github.com/temporal-community/durable-react-agent-gemini)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-06-22 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-06-22 UTC"],[],[]]
