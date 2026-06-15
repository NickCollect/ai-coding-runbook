---
source_url: https://ai.google.dev/gemini-api/docs/temporal-example?hl=he
fetched_at: 2026-06-15T06:26:18.499795+00:00
title: "\u05e1\u05d5\u05db\u05df AI \u05e2\u05de\u05d9\u05d3 \u05e2\u05dd Gemini \u05d5-Temporal \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=he) זמין עכשיו בתצוגה מקדימה עם תכונות כמו תכנון שיתופי, ויזואליזציה, תמיכה ב-MCP ועוד.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# סוכן AI עמיד עם Gemini ו-Temporal

במדריך הזה נסביר איך ליצור לולאה של סוכן [בסגנון ReAct](https://arxiv.org/abs/2210.03629) שמשתמשת ב-Gemini API לניתוח ול-[Temporal](https://temporal.io/) לעמידות.
קוד המקור המלא של המדריך הזה זמין ב-[GitHub](https://github.com/temporal-community/durable-react-agent-gemini).

הסוכן יכול להשתמש בכלים, כמו חיפוש התראות על מזג האוויר או מיקום של כתובת IP, והוא יחזור על הפעולה עד שיהיה לו מספיק מידע כדי להשיב.

מה שמבדיל את ההדגמה הזו מהדגמה טיפוסית של סוכן הוא **העמידות**. כל קריאה ל-LLM, כל הפעלה של כלי וכל שלב בלולאה של הסוכן נשמרים על ידי Temporal. אם התהליך קורס, הרשת נופלת או שפג הזמן הקצוב לתפוגה של API,‏ Temporal מנסה שוב באופן אוטומטי וממשיך מהשלב האחרון שהושלם. לא תאבדו את היסטוריית השיחות, ולא יהיו חזרות שגויות של קריאות לכלים.

## ארכיטקטורה

הארכיטקטורה מורכבת משלושה חלקים:

- **תהליך עבודה:** הלולאה שמבוססת על סוכנים ומתזמרת את לוגיקת הביצוע.
- **פעילויות:** יחידות עבודה נפרדות (קריאות ל-LLM, קריאות לכלים) ש-Temporal הופך לניתנות להמשכה.
- **Worker:** התהליך שמבצע את תהליכי העבודה והפעילויות.

בדוגמה הזו, כל שלושת החלקים האלה ממוקמים בקובץ אחד (`durable_agent_worker.py`). בהטמעה בעולם האמיתי, כדאי להפריד ביניהם כדי לאפשר יתרונות שונים של פריסה ומדרגיות. תמקמו את הקוד שמספק הנחיה לסוכן בקובץ שני (`start_workflow.py`).

## דרישות מוקדמות

כדי להשלים את ההדרכה הזו, תצטרכו:

- מפתח Gemini API. אפשר ליצור אותו בחינם ב-[Google AI Studio](https://aistudio.google.com/apikey?hl=he).
- ‫[Python](https://www.python.org/downloads/) בגרסה 3.10 ואילך.
- ‫[Temporal CLI](https://docs.temporal.io/cli) להפעלת שרת פיתוח מקומי.

## הגדרה

לפני שמתחילים, מוודאים שיש לכם [שרת פיתוח זמני](https://docs.temporal.io/cli#start-dev-server) שפועל באופן מקומי:

```
temporal server start-dev
```

לאחר מכן, מתקינים את יחסי התלות הנדרשים:

```
pip install temporalio google-genai httpx pydantic python-dotenv
```

יוצרים קובץ `.env` בספריית הפרויקט עם מפתח Gemini API. אפשר לקבל מפתח API מ-[Google AI Studio](https://aistudio.google.com/apikey?hl=he).

```
echo "GOOGLE_API_KEY=your-api-key-here" > .env
```

## הטמעה

בהמשך המדריך הזה נסביר על `durable_agent_worker.py` מלמעלה למטה, וניצור את הסוכן שלב אחר שלב. יוצרים את הקובץ ופועלים לפי ההוראות.

### ייבוא והגדרת ארגז חול

מתחילים עם הייבוא שצריך להגדיר מראש. הבלוק `workflow.unsafe.imports_passed_through()` אומר לארגז החול של תהליך העבודה של Temporal לאפשר למודולים מסוימים לעבור ללא הגבלה. הדבר נחוץ כי כמה ספריות (בעיקר `httpx`, שהיא מחלקת משנה של `urllib.request.Request`) משתמשות בתבניות שארגז החול יחסום אחרת.

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

### הוראות מערכת

בשלב הבא, מגדירים את האישיות של הסוכן. ההוראות למערכת אומרות למודל איך להתנהג. הנציג הזה קיבל הוראה להגיב בשירים קצרים (הייקו) כשאין צורך בכלים.

```
SYSTEM_INSTRUCTIONS = """
You are a helpful agent that can use tools to help the user.
You will be given an input from the user and a list of tools to use.
You may or may not need to use the tools to satisfy the user ask.
If no tools are needed, respond in haikus.
"""
```

### הגדרות של כלים

עכשיו מגדירים את הכלים שבהם הסוכן יכול להשתמש. כל כלי הוא פונקציה אסינכרונית עם מחרוזת docstring תיאורית. כלים שמקבלים פרמטרים משתמשים במודל Pydantic כארגומנט יחיד. זוהי שיטה מומלצת של Temporal ששומרת על יציבות של חתימות פעילות כשמוסיפים שדות אופציונליים לאורך זמן.

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

לאחר מכן, מגדירים כלים למיקום גיאוגרפי של כתובות IP:

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

### מאגר כלים

לאחר מכן, יוצרים מאגר שמתאים בין שמות של כלים לבין פונקציות של מטפלים. הפונקציה
`get_tools()` יוצרת אובייקטים של `FunctionDeclaration` שתואמים ל-Gemini
מתוך הפונקציות שניתנות להפעלה באמצעות `FunctionDeclaration.from_callable_with_api_option()`.

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

### פעילות של LLM

עכשיו מגדירים את הפעילות שקוראת ל-Gemini API. החוזה מוגדר במחלקות הנתונים `GeminiChatRequest` ו-`GeminiChatResponse`.

תשביתו את הקריאה האוטומטית לפונקציות כדי שהפעלת מודל שפה גדול והפעלת כלי יטופלו כמשימות נפרדות, וכך תגדילו את העמידות של הסוכן. תצטרכו גם להשבית את הניסיונות החוזרים המובנים של ה-SDK‏ (`attempts=1`) כי Temporal מטפלת בניסיונות חוזרים בצורה עמידה.

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

### פעילות בכלי הדינמי

בשלב הבא, מגדירים את הפעילות שמפעילה את הכלים. ההגדרה הזו פועלת באמצעות התכונה של Temporal לפעילות דינמית: המטפל בכלי (פונקציה שאפשר להפעיל) מתקבל ממאגר הכלים באמצעות הפונקציה `get_handler`. כך אפשר להגדיר סוכנים שונים פשוט על ידי אספקת מערכת שונה של כלים והוראות מערכת. לא נדרשים שינויים בתהליך העבודה שמיישם את הלולאה של הסוכן.

הפעילות בודקת את החתימה של ה-handler כדי לקבוע איך להעביר את הארגומנטים. אם ה-handler מצפה למודל Pydantic, הוא מטפל בפורמט הפלט המקונן ש-Gemini מייצר (לדוגמה, `{"request": {"state": "CA"}}` במקום `{"state": "CA"}` שטוח).

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

### תהליך העבודה של לולאה סוכנית

עכשיו יש לכם את כל החלקים שצריך כדי לסיים את בניית הסוכן. המחלקה `AgentWorkflow` מיישמת תהליך עבודה המכיל את לולאת הסוכן. בתוך הלולאה הזו, מפעילים את ה-LLM באמצעות פעילות (מה שהופך אותו לעמיד), בודקים את הפלט, ואם ה-LLM בחר כלי, מפעילים אותו באמצעות `dynamic_tool_activity`.

בסוכן הפשוט הזה בסגנון ReAct, ברגע ש-LLM בוחר לא להשתמש בכלי, הלולאה נחשבת להשלמה והתוצאה הסופית של LLM מוחזרת.

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

הלולאה של הסוכן עמידה לחלוטין. אם תהליך העבודה של הסוכן קורס אחרי כמה איטרציות בלולאה, Temporal ימשיך בדיוק מהמקום שבו הוא הפסיק, בלי צורך להפעיל מחדש קריאות שכבר בוצעו ל-LLM או קריאות לכלים.

### הפעלת Worker

לבסוף, מחברים את הכול. הקוד מיישם את הלוגיקה העסקית הנדרשת באופן שגורם לו לפעול בתהליך יחיד, אבל השימוש ב-Temporal הופך אותו למערכת מבוססת-אירועים (במיוחד, מבוססת-מקורות), שבה התקשורת בין תהליך העבודה לבין הפעילויות מתבצעת באמצעות העברת הודעות ש-Temporal מספקת.

ה-Temporal worker מתחבר לשירות Temporal ופועל כמתזמן למשימות של תהליך העבודה והפעילות. העובד רושם את תהליך העבודה ואת שתי הפעילויות, ואז מתחיל להאזין למשימות.

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

## סקריפט הלקוח

יוצרים את סקריפט הלקוח (`start_workflow.py`). הסקריפט שולח שאילתה וממתין לתוצאה. שימו לב שהסקריפט מתחבר לאותו תור משימות שמוזכר ב-agent worker – הסקריפט `start_workflow` שולח משימת תהליך עבודה עם ההנחיה של המשתמש לאותו תור משימות, ומתחיל את ההפעלה של הסוכן.

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

## הפעלת הסוכן

אם עדיין לא עשיתם זאת, מפעילים את שרת הפיתוח של Temporal:

```
temporal server start-dev
```

בחלון טרמינל חדש, מפעילים את תהליך העבודה של הסוכן:

```
python -m durable_agent_worker
```

בחלון מסוף שלישי, שולחים שאילתה לסוכן:

```
python -m start_workflow "are there any weather alerts for where I am?"
```

שימו לב לפלט במסוף של `durable_agent_worker` שבו מוצגות הפעולות שמתבצעות בכל איטרציה של הלולאה של הסוכן. מודל ה-LLM יכול למלא את בקשת המשתמש באמצעות הפעלה של סדרת כלים שעומדים לרשותו. אפשר לראות את השלבים שהופעלו דרך ממשק המשתמש של Temporal בכתובת `http://localhost:8233/namespaces/default/workflows`.

כדאי לנסות כמה הנחיות שונות כדי לראות את הסיבה לפנייה לנציג ואת הכלים לשיחה:

```
python -m start_workflow "are there any weather alerts for New York?"
python -m start_workflow "where am I?"
python -m start_workflow "what is my ip address?"
python -m start_workflow "tell me a joke"
```

ההנחיה האחרונה לא דורשת שימוש בכלים, ולכן הסוכן מגיב בשיר הייקו על סמך `SYSTEM_INSTRUCTIONS`.

## בדיקת העמידות (אופציונלי)

השימוש ב-Temporal מבטיח שהסוכן ימשיך לפעול בצורה חלקה גם אם יתרחשו כשלים. אפשר לבדוק את זה באמצעות שני ניסויים שונים.

### הדמיה של הפסקה זמנית בשירות ברשת

בבדיקה הזו, תשביתו באופן זמני את החיבור לאינטרנט במחשב, תשלחו תהליך עבודה, תצפו בניסיון חוזר אוטומטי של Temporal, ואז תשחזרו את הרשת כדי לראות את השחזור.

1. מנתקים את המחשב מהאינטרנט (לדוגמה, משביתים את ה-Wi-Fi).
2. הגשת תהליך עבודה:

   ```
   python -m start_workflow "tell me a joke"
   ```
3. בודקים את ממשק המשתמש של Temporal ‏ (`http://localhost:8233`). תראו שהפעילות של ה-LLM נכשלת ו-Temporal מנהל אוטומטית את הניסיונות החוזרים ברקע.
4. צריך להתחבר מחדש לאינטרנט.
5. הניסיון האוטומטי הבא יגיע בהצלחה אל Gemini API, והתוצאה הסופית תודפס במסוף.

### איך שורדים קריסה של עובד

בבדיקה הזו, אתם משביתים את העובד באמצע ההרצה ומפעילים אותו מחדש. ‫Temporal מפעיל מחדש את היסטוריית תהליך העבודה (מקור אירועים) וממשיך מהפעילות האחרונה שהושלמה – קריאות ל-LLM וקריאות לכלים שכבר הושלמו לא חוזרות על עצמן.

1. כדי לאפשר לעצמכם זמן להפסיק את ה-worker, פותחים את `durable_agent_worker.py` ומבטלים את ההערה של `await asyncio.sleep(10)` בתוך הלולאה `AgentWorkflow`
   `run` באופן זמני.
2. מפעילים מחדש את העובד:

   ```
   python -m durable_agent_worker
   ```
3. שליחת שאילתה שמפעילה כמה כלים:

   ```
   python -m start_workflow "are there any weather alerts where I am?"
   ```
4. אפשר להפסיק את תהליך העובד בכל שלב לפני ההשלמה (`Ctrl-C` במסוף העובד או באמצעות `kill %1` אם התהליך פועל ברקע).
5. מפעילים מחדש את העובד:

   ```
   python -m durable_agent_worker
   ```

‫Temporal מפעיל מחדש את היסטוריית תהליך העבודה. הקריאות ל-LLM והפעלות הכלים שכבר הושלמו **לא** מופעלות מחדש – התוצאות שלהן מוצגות מחדש באופן מיידי מההיסטוריה (יומן האירועים). תהליך העבודה מסתיים בהצלחה.

## מקורות מידע נוספים

- [תיעוד זמני](https://docs.temporal.io/)
- ‫[Temporal Python SDK](https://docs.temporal.io/develop/python)
- [Google GenAI SDK](https://googleapis.github.io/python-genai/)
- [קוד המקור של המדריך הזה](https://github.com/temporal-community/durable-react-agent-gemini)

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-05-19 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-05-19 (שעון UTC)."],[],[]]
