---
source_url: https://ai.google.dev/gemini-api/docs/temporal-example?hl=ar
fetched_at: 2026-07-20T04:42:51.819635+00:00
title: "\u0648\u0643\u064a\u0644 \u0627\u0644\u0630\u0643\u0627\u0621 \u0627\u0644\u0627\u0635\u0637\u0646\u0627\u0639\u064a \u0627\u0644\u062f\u0627\u0626\u0645 \u0645\u0639 Gemini \u0648Temporal \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# وكيل الذكاء الاصطناعي الدائم مع Gemini وTemporal

يرشدك هذا البرنامج التعليمي خلال عملية إنشاء حلقة وكيل بأسلوب
[ReAct](https://arxiv.org/abs/2210.03629) تستخدِم
Gemini API للاستدلال و[Temporal](https://temporal.io/) لضمان استمراريتها.
يتوفّر الرمز المصدر الكامل لهذا البرنامج التعليمي على
[GitHub](https://github.com/temporal-community/durable-react-agent-gemini).

يمكن للوكيل استدعاء الأدوات، مثل البحث عن تنبيهات الأحوال الجوية أو تحديد الموقع الجغرافي لعنوان IP، وسيستمر في التكرار إلى أن يحصل على معلومات كافية للردّ.

ما يميّز هذا البرنامج التعليمي عن العرض التوضيحي العادي للوكيل هو **الاستمرارية**. تحتفظ Temporal بكل استدعاء للنموذج اللغوي الكبير وكل استدعاء للأداة وكل خطوة من خطوات حلقة الوكيل. إذا تعطّلت العملية أو انقطع الاتصال بالشبكة أو انتهت مهلة واجهة برمجة التطبيقات، تعيد Temporal المحاولة تلقائيًا وتستأنف من آخر خطوة مكتملة. لا يتم فقدان سجلّ المحادثات ولا يتم تكرار استدعاءات الأدوات بشكل غير صحيح.

## هندسة معمارية

تتألف الهندسة المعمارية من ثلاثة أجزاء:

- **سير العمل:** حلقة الوكيل التي تنظّم منطق التنفيذ.
- **الأنشطة:** وحدات العمل الفردية (استدعاءات النموذج اللغوي الكبير واستدعاءات الأدوات) التي تجعلها Temporal مستمرة.
- **العامل:** العملية التي تنفّذ مهام سير العمل والأنشطة.

في هذا المثال، ستضع كل هذه الأجزاء الثلاثة في ملف واحد (`durable_agent_worker.py`). في عملية التنفيذ الواقعية، يمكنك فصلها للاستفادة من مزايا النشر وقابلية التوسّع المختلفة. ستضع الرمز الذي يقدّم طلبًا إلى الوكيل في ملف ثانٍ (`start_workflow.py`).

## المتطلبات الأساسية

لإكمال هذا الدليل، ستحتاج إلى:

- مفتاح Gemini API يمكنك إنشاء مفتاح مجانًا في
  [Google AI Studio](https://aistudio.google.com/apikey?hl=ar).
- الإصدار 3.10 من [Python](https://www.python.org/downloads/) أو إصدار أحدث
- واجهة سطر الأوامر [Temporal](https://docs.temporal.io/cli) لتشغيل خادم تطوير محلي

## الإعداد

قبل البدء، تأكَّد من تشغيل خادم تطوير
[Temporal](https://docs.temporal.io/cli#start-dev-server)
محليًا:

```
temporal server start-dev
```

بعد ذلك، ثبِّت التبعيات المطلوبة:

```
pip install temporalio google-genai httpx pydantic python-dotenv
```

أنشِئ ملف `.env` في دليل مشروعك باستخدام مفتاح Gemini API. يمكنك الحصول على مفتاح واجهة برمجة التطبيقات من
[Google AI Studio](https://aistudio.google.com/apikey?hl=ar).

```
echo "GOOGLE_API_KEY=your-api-key-here" > .env
```

## التنفيذ

يرشدك الجزء المتبقي من هذا البرنامج التعليمي خلال عملية إنشاء `durable_agent_worker.py` من أعلى إلى أسفل، وتجميع الوكيل جزءًا جزءًا. أنشِئ الملف واتّبِع الخطوات.

### عمليات الاستيراد وإعداد وضع الحماية

ابدأ بعمليات الاستيراد التي يجب تحديدها مسبقًا. تخبر الكتلة `workflow.unsafe.imports_passed_through()` وضع حماية سير عمل Temporal بالسماح بمرور وحدات معيّنة بدون قيود. هذا ضروري لأنّ العديد من المكتبات (أبرزها `httpx`، التي تنتمي إلى الفئة الفرعية `urllib.request.Request`) تستخدِم أنماطًا سيحظرها وضع الحماية بخلاف ذلك.

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

### تعليمات النظام

بعد ذلك، حدِّد شخصية الوكيل. تخبر تعليمات النظام النموذج بكيفية التصرّف. تمت توجيه هذا الوكيل للردّ في قصائد هايكو عندما لا تكون هناك حاجة إلى استخدام أي أدوات.

```
SYSTEM_INSTRUCTIONS = """
You are a helpful agent that can use tools to help the user.
You will be given an input from the user and a list of tools to use.
You may or may not need to use the tools to satisfy the user ask.
If no tools are needed, respond in haikus.
"""
```

### تعريفات الأدوات

الآن، حدِّد الأدوات التي يمكن للوكيل استخدامها. كل أداة هي دالة غير متزامنة تتضمّن سلسلة مستندات وصفية. تستخدِم الأدوات التي تأخذ مَعلمات نموذج Pydantic كمعلَمة واحدة. هذه أفضل ممارسة في Temporal تحافظ على ثبات تواقيع النشاط أثناء إضافة حقول اختيارية بمرور الوقت.

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

بعد ذلك، حدِّد أدوات تحديد الموقع الجغرافي لعنوان IP:

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

### سجلّ الأدوات

بعد ذلك، أنشِئ قاعدة بيانات المسجّلين التي تربط أسماء الأدوات بدوال المعالجة. تنشئ الدالة
`get_tools()` كائنات `FunctionDeclaration` متوافقة مع Gemini
من الدوال القابلة للاستدعاء باستخدام `FunctionDeclaration.from_callable_with_api_option()`.

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

### نشاط النموذج اللغوي الكبير

الآن، حدِّد النشاط الذي يستدعي Gemini API. تحدِّد فئتا البيانات `GeminiChatRequest` و`GeminiChatResponse` العقد.

ستوقف ميزة استدعاء الدوال التلقائي حتى يتم التعامل مع استدعاء النموذج اللغوي الكبير واستدعاء الأداة كمهام منفصلة، ما يمنح وكيلك مزيدًا من الاستمرارية. ستوقف أيضًا عمليات إعادة المحاولة المضمّنة في حزمة SDK (`attempts=1`) لأنّ Temporal تتعامل مع عمليات إعادة المحاولة بشكل مستمر.

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

### نشاط الأداة الديناميكية

بعد ذلك، حدِّد النشاط الذي ينفّذ الأدوات. يستخدِم هذا ميزة النشاط الديناميكي في Temporal: يتم الحصول على معالج الأداة (دالة قابلة للاستدعاء) من سجلّ الأدوات من خلال الدالة `get_handler`. يتيح ذلك تحديد وكلاء مختلفين ببساطة من خلال تقديم مجموعة مختلفة من الأدوات وتعليمات النظام، ولا يتطلّب سير العمل الذي ينفّذ حلقة الوكيل أي تغييرات.

يفحص النشاط توقيع المعالج لتحديد كيفية تمرير الوسيطات. إذا كان المعالج يتوقّع نموذج Pydantic، فإنّه يتعامل مع تنسيق الإخراج المتداخل
الذي ينتجه Gemini (على سبيل المثال، `{"request": {"state": "CA"}}` بدلاً
من `{"state": "CA"}`).

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

### سير عمل حلقة الوكيل

الآن، لديك كل الأجزاء اللازمة لإنهاء إنشاء الوكيل. تنفّذ الفئة `AgentWorkflow` سير عمل يحتوي على حلقة الوكيل. ضمن هذه الحلقة، يتم استدعاء النموذج اللغوي الكبير من خلال النشاط (ما يجعله مستمرًا)، ويتم فحص الناتج، وإذا اختار النموذج اللغوي الكبير أداة، يتم استدعاؤها من خلال `dynamic_tool_activity`.

في هذا الوكيل البسيط بأسلوب ReAct، بمجرد أن يختار النموذج اللغوي الكبير عدم استخدام أداة، تُعتبر الحلقة مكتملة ويتم عرض النتيجة النهائية للنموذج اللغوي الكبير.

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

حلقة الوكيل مستمرة بالكامل. إذا تعطّل عامل الوكيل بعد عدة تكرارات خلال الحلقة، ستستأنف Temporal من المكان الذي توقّفت عنده بالضبط بدون الحاجة إلى إعادة استدعاء استدعاءات النموذج اللغوي الكبير أو استدعاءات الأدوات التي تم تنفيذها من قبل.

### بدء تشغيل العامل

أخيرًا، اربط كل شيء معًا. على الرغم من أنّ الرمز ينفّذ منطق النشاط التجاري الضروري بطريقة تجعله يبدو وكأنّه يتم تشغيله في عملية واحدة، فإنّ استخدام Temporal يجعله نظامًا يستند إلى الأحداث (على وجه التحديد، يستند إلى مصدر الأحداث) حيث يحدث التواصل بين سير العمل والأنشطة من خلال المراسلة التي توفّرها Temporal.

يتصل عامل Temporal بخدمة Temporal ويعمل كنظام جدولة مهام لمهام سير العمل والأنشطة. يسجِّل العامل سير العمل وكلا النشاطَين، ثم يبدأ في الاستماع إلى المهام.

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

## النص البرمجي للعميل

أنشِئ النص البرمجي للعميل (`start_workflow.py`). يرسِل هذا النص استعلامًا وينتظر النتيجة. لاحظ أنّه يتصل بقائمة انتظار المهام نفسها المشار إليها في عامل الوكيل، إذ يرسِل النص البرمجي `start_workflow` مهمة سير عمل تتضمّن طلب المستخدم إلى قائمة انتظار المهام هذه، ما يؤدي إلى بدء تنفيذ الوكيل.

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

## تشغيل الوكيل

إذا لم يسبق لك ذلك، ابدأ خادم تطوير Temporal:

```
temporal server start-dev
```

في نافذة طرفية جديدة، ابدأ عامل الوكيل:

```
python -m durable_agent_worker
```

في نافذة طرفية ثالثة، أرسِل استعلامًا إلى وكيلك:

```
python -m start_workflow "are there any weather alerts for where I am?"
```

لاحظ الناتج في النافذة الطرفية لـ `durable_agent_worker` الذي يعرض الإجراءات التي تحدث في كل تكرار من حلقة الوكيل. يستطيع النموذج اللغوي الكبير تلبية طلب المستخدم من خلال استدعاء سلسلة من الأدوات المتاحة له. يمكنك الاطّلاع على الخطوات التي تم تنفيذها من خلال واجهة مستخدم Temporal على `http://localhost:8233/namespaces/default/workflows`.

جرِّب توجيه بضعة طلبات مختلفة للاطّلاع على طريقة استدلال الوكيل واستدعائه للأدوات:

```
python -m start_workflow "are there any weather alerts for New York?"
python -m start_workflow "where am I?"
python -m start_workflow "what is my ip address?"
python -m start_workflow "tell me a joke"
```

لا يتطلّب الطلب الأخير أي أدوات، لذا يردّ الوكيل في قصيدة هايكو استنادًا إلى `SYSTEM_INSTRUCTIONS`.

## اختبار الاستمرارية (اختياري)

يضمن إنشاء وكيلك استنادًا إلى Temporal أنّه سيستمر في العمل بسلاسة في حال حدوث أعطال. يمكنك اختبار ذلك باستخدام تجربتَين مختلفتَين.

### محاكاة انقطاع الشبكة

في هذا الاختبار، ستوقف مؤقتًا الاتصال بالإنترنت على جهاز الكمبيوتر، وترسِل سير عمل، وتراقب إعادة المحاولة التلقائية في Temporal، ثم تعيد الاتصال بالشبكة للاطّلاع على عملية الاسترداد.

1. افصل جهازك عن الإنترنت (على سبيل المثال، أوقِف شبكة Wi-Fi).
2. أرسِل سير عمل:

   ```
   python -m start_workflow "tell me a joke"
   ```
3. تحقَّق من واجهة مستخدم Temporal (`http://localhost:8233`). ستلاحظ تعذُّر نشاط النموذج اللغوي الكبير وإدارة Temporal تلقائيًا لعمليات إعادة المحاولة في الخلفية.
4. أعِد الاتصال بالإنترنت.
5. ستصل عملية إعادة المحاولة التلقائية التالية بنجاح إلى Gemini API، وستعرض النافذة الطرفية النتيجة النهائية.

### الاستمرار في العمل بعد تعطُّل العامل

في هذا الاختبار، ستوقف العامل في منتصف التنفيذ ثم تعيد تشغيله. تعيد Temporal تشغيل سجلّ سير العمل (مصدر الأحداث) وتستأنف من آخر نشاط مكتمل، ولا يتم تكرار استدعاءات النموذج اللغوي الكبير واستدعاءات الأدوات التي تم إكمالها من قبل.

1. لمنح نفسك وقتًا لإيقاف العامل، افتح `durable_agent_worker.py` وأزِل مؤقتًا علامة التعليق عن `await asyncio.sleep(10)` داخل حلقة `run` في `AgentWorkflow`.
2. أعِد تشغيل العامل:

   ```
   python -m durable_agent_worker
   ```
3. أرسِل استعلامًا يؤدي إلى استدعاء عدة أدوات:

   ```
   python -m start_workflow "are there any weather alerts where I am?"
   ```
4. أوقِف عملية العامل في أي وقت قبل الإكمال (`Ctrl-C` في النافذة الطرفية للعامل، أو باستخدام `kill %1` إذا كان يتم تشغيلها في الخلفية).
5. أعِد تشغيل العامل:

   ```
   python -m durable_agent_worker
   ```

تعيد Temporal تشغيل سجلّ سير العمل. **لا** تتم إعادة تنفيذ استدعاءات النموذج اللغوي الكبير واستدعاءات الأدوات التي تم إكمالها من قبل، بل تتم إعادة تشغيل نتائجها على الفور من السجلّ (سجلّ الأحداث). يكتمل سير العمل بنجاح.

## موارد أخرى

- [مستندات Temporal](https://docs.temporal.io/)
- [حزمة Temporal Python SDK](https://docs.temporal.io/develop/python)
- [حزمة Google GenAI SDK](https://googleapis.github.io/python-genai/)
- [الرمز المصدر لهذا البرنامج التعليمي](https://github.com/temporal-community/durable-react-agent-gemini)

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-06-22 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-06-22 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
