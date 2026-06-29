---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/computer-use?hl=ar
fetched_at: 2026-06-29T05:37:55.027290+00:00
title: "\u0627\u0633\u062a\u062e\u062f\u0627\u0645 \u0627\u0644\u0643\u0645\u0628\u064a\u0648\u062a\u0631 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# استخدام الكمبيوتر

تتيح لك أداة "استخدام الكمبيوتر" إنشاء وكلاء تحكّم في المتصفّح والأجهزة الجوّالة وأجهزة الكمبيوتر المكتبي تتفاعل مع المهام وتنفّذها تلقائيًا. باستخدام لقطات الشاشة، يمكن للنموذج "رؤية" شاشة الكمبيوتر و "التصرف" من خلال إنشاء إجراءات معيّنة في واجهة المستخدم، مثل نقرات الماوس وإدخالات لوحة المفاتيح. على غرار ميزة &quot;استدعاء الدوال&quot;، عليك تنفيذ بيئة التنفيذ من جهة العميل لتلقّي إجراءات &quot;استخدام الكمبيوتر&quot; وتنفيذها.

‫Gemini 3.5 Flash هو النموذج المقترَح للاستخدام على الكمبيوتر، ويتضمّن عدة إمكانات جديدة:

- **التوافق مع بيئات متعددة:** يمكنك إنشاء وكلاء لبيئات [المتصفّح والأجهزة الجوّالة وأجهزة الكمبيوتر](#supported-environments).
- **إجراءات مبسطة مع النوايا:** تتضمّن الإجراءات حقل `intent` يشرح الأساس المنطقي الذي يستند إليه النموذج في كل خطوة.
- **سياسات الأمان القابلة للإعداد:** يمكنك تحسين [سلوك الأمان](#safety-policies) باستخدام فئات السياسات وعناصر التجاوز المضمّنة.
- **رصد عمليات حقن الطلبات:** فعِّل ميزة [فحص لقطات الشاشة](#prompt-injection) لرصد التعليمات الخفية التي تهدف إلى خداع الذكاء الاصطناعي.

باستخدام "استخدام الكمبيوتر"، يمكنك إنشاء وكلاء تنفيذ يمكنهم:

- أتمتة إدخال البيانات المتكرّر أو ملء النماذج على المواقع الإلكترونية
- إجراء اختبار آلي لتطبيقات الويب وتفاعلات المستخدمين
- إجراء بحث على مواقع إلكترونية مختلفة (مثل جمع معلومات عن المنتجات وأسعارها ومراجعاتها من مواقع التجارة الإلكترونية لاتخاذ قرار بشأن الشراء)

في ما يلي مثال بسيط على تفعيل أداة "استخدام الكمبيوتر":

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Search for 'Gemini API' on Google.",
    config=types.GenerateContentConfig(
        tools=[types.Tool(
            computer_use=types.ComputerUse(
                environment=types.Environment.ENVIRONMENT_BROWSER,
            )
        )]
    )
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI();

const response = await ai.models.generateContent({
  model: 'gemini-3.5-flash',
  contents: "Search for 'Gemini API' on Google.",
  config: {
    tools: [{
      computerUse: {
        environment: "ENVIRONMENT_BROWSER",
      }
    }]
  }
});

console.log(response.text);
```

## طريقة عمل ميزة "استخدام الكمبيوتر"

لإنشاء وكيل باستخدام نموذج "استخدام الكمبيوتر"، عليك إعداد حلقة متواصلة بين تطبيقك وواجهة برمجة التطبيقات. في ما يلي ما سيفعله الرمز في كل خطوة:

1. [**إرسال طلب إلى النموذج**](#send-request)
   - يرسل تطبيقك طلبًا إلى واجهة برمجة التطبيقات يتضمّن أداة "استخدام الكمبيوتر"، وإعدادات التهيئة (مثل البيئة المستهدَفة)، وطلب المستخدم، ولقطة شاشة للشاشة الحالية.
2. [**تلقّي ردّ النموذج**](#model-response)
   - يحلّل النموذج الشاشة والطلب، ويعرض ردًا يتضمّن `function_call` مقترَحًا يمثّل إجراءً في واجهة المستخدم (مثل النقر أو التمرير أو ضغط المفاتيح).
   - بالنسبة إلى **Gemini 3.5 Flash**، يتضمّن الرد أيضًا شرحًا `intent`
     يوضّح سبب اختيار النموذج لهذا الإجراء.
   - قد يتضمّن الرد أيضًا `safety_decision` من نظام أمان داخلي يصنّف الإجراء على أنّه عادي/مسموح به، أو `require_confirmation` (يتطلّب موافقة المستخدم)، أو محظور.
3. [**تنفيذ الإجراء الذي تم تلقّيه**](#execute-actions)
   - إذا كان الإجراء مسموحًا به (أو إذا أكّده المستخدم)، سيحلّل الرمز البرمجي من جهة العميل `function_call`، ويغيّر حجم الإحداثيات العادية لتتطابق مع إطار العرض، وينفّذ الإجراء في البيئة المستهدَفة باستخدام أدوات التشغيل الآلي (مثل Playwright). إذا تم حظر الإجراء، على العميل إيقاف التنفيذ أو التعامل مع الانقطاع.
4. [**تسجيل حالة البيئة الجديدة**](#capture-state)
   - بعد انتهاء تنفيذ الإجراء، يلتقط تطبيقك لقطة شاشة جديدة ويرسلها إلى النموذج في `function_result` لطلب الخطوة التالية.

بعد ذلك، تتكرر هذه العملية بدءًا من الخطوة 2، ويتم باستمرار طلب الإجراء التالي من النموذج إلى أن تكتمل المهمة أو يتم إنهاؤها.

![نظرة عامة على استخدام الكمبيوتر](https://ai.google.dev/static/gemini-api/docs/images/computer_use.png?hl=ar)

## كيفية تنفيذ ميزة "استخدام الكمبيوتر"

قبل إنشاء تطبيق باستخدام أداة "استخدام الكمبيوتر"، عليك إعداد ما يلي:

- **بيئة التنفيذ الآمنة:** شغِّل وكيلك في جهاز افتراضي أو حاوية في وضع الحماية لعزله عن نظامك المضيف والحدّ من تأثيره المحتمل.
  يتضمّن [التنفيذ المرجعي](https://github.com/google/computer-use-preview/)
  بيئة اختبارية جاهزة للاستخدام تستند إلى Docker ويمكنك استخدامها كنقطة بداية.
- **معالج الإجراءات من جهة العميل:** نفِّذ منطقًا من جهة العميل لتنفيذ الإحداثيات وكتابة النص وأخذ لقطات شاشة.

تستخدِم الأمثلة أدناه متصفّح ويب كبيئة تنفيذ و[Playwright](https://playwright.dev/) كأداة معالجة من جهة العميل.

### 0. إعداد Playwright

أولاً، ثبِّت الحِزم المطلوبة:

```
pip install google-genai playwright
playwright install chromium
```

بعد ذلك، ابدأ مثيلاً لمتصفّح Playwright لاستخدامه في التنفيذ:

```
from playwright.sync_api import sync_playwright

# 1. Configure screen dimensions for the target environment
SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 900

# 2. Start the Playwright browser
# In production, utilize a sandboxed environment.
playwright = sync_playwright().start()
# Set headless=False to see the actions performed on your screen
browser = playwright.chromium.launch(headless=False)

# 3. Create a context and page with the specified dimensions
context = browser.new_context(
    viewport={"width": SCREEN_WIDTH, "height": SCREEN_HEIGHT}
)
page = context.new_page()

# 4. Navigate to an initial page to start the task
page.goto("https://www.google.com")

# The 'page', 'SCREEN_WIDTH', and 'SCREEN_HEIGHT' variables
# will be used in the steps below.
```

### 1. إرسال طلب إلى النموذج

ابدأ مكتبة البرامج واضبط أداة "استخدام الكمبيوتر". يُرجى العِلم أنّه ليس من الضروري تحديد حجم العرض عند إرسال طلب، إذ يتوقّع النموذج إحداثيات البكسل التي تم تغيير حجمها لتناسب ارتفاع الشاشة وعرضها.

### ‫Gemini 3.5 Flash (يُنصح به)

### Python

استخدِم حزمة تطوير البرامج (SDK) `google-genai` Python (الإصدار `2.7.0` أو إصدار أحدث) لإعداد طلب يستهدف بيئة المتصفّح:

```
from google import genai
from google.genai.types import (
    Content,
    Part,
    GenerateContentConfig,
    Tool,
    ComputerUse,
    Environment,
    ThinkingConfig,
)

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=[
        Content(
            role="user",
            parts=[
                Part(text="Find a flight from SF to Hawaii on Jun 30th, coming back on Jul 6th"),
            ],
        )
    ],
    config=GenerateContentConfig(
        tools=[
            Tool(
                computer_use=ComputerUse(
                    environment=Environment.ENVIRONMENT_BROWSER,
                    enable_prompt_injection_detection=True,
                ),
            ),
        ],
        thinking_config=ThinkingConfig(
            include_thoughts=True
        ),
    )
)

print(response.text)
```

### JavaScript

استخدِم حزمة تطوير البرامج (SDK) الخاصة بـ Node.js في `@google/genai` لإعداد طلب يستهدف بيئة المتصفّح:

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI();

const response = await ai.models.generateContent({
  model: 'gemini-3.5-flash',
  contents: [
    {
      role: 'user',
      parts: [{ text: "Find a flight from SF to Hawaii on Jun 30th, coming back on Jul 6th" }]
    }
  ],
  config: {
    tools: [{
      computerUse: {
        environment: "ENVIRONMENT_BROWSER",
        enable_prompt_injection_detection: true
      }
    }],
    thinkingConfig: {
      includeThoughts: true
    }
  }
});

console.log(response.text);
```

### REST

استخدِم curl لإرسال طلب:

```
curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": {
          "text": "Find me a flight from SF to Hawaii on Jun 30th, coming back on Jul 6th. Start by navigating directly to flights.google.com"
        }
      }
    ],
    "tools": [
      {
        "computer_use": {
          "environment": "ENVIRONMENT_BROWSER",
          "enable_prompt_injection_detection": true
        }
      }
    ]
  }'
```

### الإصدار القديم من Gemini 2.5

### Python

```
from google import genai
from google.genai import types
from google.genai.types import Content, Part

client = genai.Client()

# Specify predefined functions to exclude (optional)
excluded_functions = ["drag_and_drop"]

generate_content_config = genai.types.GenerateContentConfig(
    tools=[
        types.Tool(
            computer_use=types.ComputerUse(
                environment=types.Environment.ENVIRONMENT_BROWSER,
                excluded_predefined_functions=excluded_functions
                )
              ),
          ],
  )

contents=[
    Content(
        role="user",
        parts=[
            Part(text="Search for highly rated smart fridges on Google Shopping."),
        ],
    )
]

response = client.models.generate_content(
    model='gemini-2.5-computer-use-preview-10-2025',
    contents=contents,
    config=generate_content_config,
)

print(response)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI();

// Specify predefined functions to exclude (optional)
const excludedFunctions = ["drag_and_drop"];

const response = await ai.models.generateContent({
  model: 'gemini-2.5-computer-use-preview-10-2025',
  contents: [
    {
      role: 'user',
      parts: [{ text: "Search for highly rated smart fridges on Google Shopping." }]
    }
  ],
  config: {
    tools: [{
      computerUse: {
        environment: "ENVIRONMENT_BROWSER",
        excluded_predefined_functions: excludedFunctions
      }
    }]
  }
});

console.log(response);
```

### 2. تلقّي ردّ النموذج

يقترح نموذج الردّ استدعاء دالة. بالنسبة إلى **Gemini 3.5 Flash**،
يتضمّن الرد نية استدلال مخصّصة بالإضافة إلى الإحداثيات. يوضّح ما يلي أمثلة على كلا الردّين:

### Gemini 3.5 Flash

```
{
  "function_call": {
    "name": "click",
    "args": {
      "x": 450,
      "y": 120,
      "intent": "Click the search box to type the destination."
    }
  }
}
```

### الإصدار القديم من Gemini 2.5

```
{
  "content": {
    "parts": [
      {
        "text": "I will type the search query into the search bar."
      },
      {
        "function_call": {
          "name": "type_text_at",
          "args": {
            "x": 371,
            "y": 470,
            "text": "highly rated smart fridges",
            "press_enter": true
          }
        }
      }
    ]
  }
}
```

### 3- تنفيذ الإجراءات التي تم تلقّيها

يجب أن يحلّل الرمز البرمجي لتطبيقك استجابة النموذج، وينفّذ الإجراءات، ويجمع النتائج.

يتعامل الرمز أدناه مع أوامر الأدوات القديمة (`click_at` و`type_text_at`) وأوامر Gemini 3.5 Flash المبسّطة (`click` و`type`).

### Python

```
from typing import Any, List, Tuple
import time

def denormalize_x(x: int, screen_width: int) -> int:
    """Convert normalized x coordinate (0-1000) to actual pixel coordinate."""
    return int(x / 1000 * screen_width)

def denormalize_y(y: int, screen_height: int) -> int:
    """Convert normalized y coordinate (0-1000) to actual pixel coordinate."""
    return int(y / 1000 * screen_height)

def execute_function_calls(interaction, page, screen_width, screen_height):
    results = []
    function_calls = []

    # Parse content parts (Handling legacy and Gemini 3 response structures)
    parts = candidate.content.parts if hasattr(candidate, 'content') else []
    if not parts and hasattr(candidate, 'function_calls'):
        function_calls = candidate.function_calls
    else:
        for part in parts:
            if part.function_call:
                function_calls.append(part.function_call)

    for function_call in function_calls:
        action_result = {}
        fname = function_call.name
        args = function_call.args
        print(f"  -> Executing: {fname} (Intent: {args.get('intent', 'N/A')})")

        try:
            if fname in ("open_web_browser", "open_app"):
                pass # Handled / already open
            elif fname in ("click", "click_at", "double_click", "triple_click", "middle_click", "right_click", "move", "long_press"):
                actual_x = denormalize_x(args["x"], screen_width)
                actual_y = denormalize_y(args["y"], screen_height)

                if fname in ("click", "click_at"):
                    page.mouse.click(actual_x, actual_y)
                elif fname == "double_click":
                    page.mouse.dblclick(actual_x, actual_y)
                elif fname == "right_click":
                    page.mouse.click(actual_x, actual_y, button="right")
                elif fname == "middle_click":
                    page.mouse.click(actual_x, actual_y, button="middle")
                elif fname == "move":
                    page.mouse.move(actual_x, actual_y)
            elif fname in ("type", "type_text_at"):
                actual_x = denormalize_x(args["x"], screen_width) if "x" in args else None
                actual_y = denormalize_y(args["y"], screen_height) if "y" in args else None
                text = args["text"]
                press_enter = args.get("press_enter", False)

                if actual_x is not None and actual_y is not None:
                    page.mouse.click(actual_x, actual_y)
                # Clear field first
                page.keyboard.press("Meta+A")
                page.keyboard.press("Backspace")
                page.keyboard.type(text)
                if press_enter:
                    page.keyboard.press("Enter")
            elif fname == "navigate":
                page.goto(args["url"])
            elif fname == "go_back":
                page.go_back()
            elif fname == "go_forward":
                page.go_forward()
            elif fname == "wait":
                time.sleep(args.get("seconds", 1))
            else:
                print(f"Warning: Custom or unhandled function {fname}")

            page.wait_for_load_state(timeout=5000)
            time.sleep(1)

        except Exception as e:
            print(f"Error executing {fname}: {e}")
            action_result = {"error": str(e)}

        results.append((fname, function_call.id, action_result))

    return results
```

### JavaScript

```
function denormalizeX(x, screenWidth) {
    // Convert normalized x coordinate (0-1000) to actual pixel coordinate.
    return Math.floor((x / 1000) * screenWidth);
}

function denormalizeY(y, screenHeight) {
    // Convert normalized y coordinate (0-1000) to actual pixel coordinate.
    return Math.floor((y / 1000) * screenHeight);
}

async function executeFunctionCalls(candidate, page, screenWidth, screenHeight) {
    const results = [];
    let functionCalls = [];

    // Parse function calls from candidate response
    const parts = candidate.content?.parts || [];
    if (parts.length === 0 && candidate.functionCalls) {
        functionCalls = candidate.functionCalls;
    } else {
        for (const part of parts) {
            if (part.functionCall) {
                functionCalls.push(part.functionCall);
            }
        }
    }

    for (const functionCall of functionCalls) {
        const actionResult = {};
        const fname = functionCall.name;
        const args = functionCall.args;
        console.log(`  -> Executing: ${fname} (Intent: ${args.intent || 'N/A'})`);

        try {
            if (fname === "open_web_browser" || fname === "open_app") {
                // Handled / already open
            } else if (["click", "click_at", "double_click", "triple_click", "middle_click", "right_click", "move", "long_press"].includes(fname)) {
                const actualX = denormalizeX(args.x, screenWidth);
                const actualY = denormalizeY(args.y, screenHeight);

                if (fname === "click" || fname === "click_at") {
                    await page.mouse.click(actualX, actualY);
                } else if (fname === "double_click") {
                    await page.mouse.dblclick(actualX, actualY);
                } else if (fname === "right_click") {
                    await page.mouse.click(actualX, actualY, { button: "right" });
                } else if (fname === "middle_click") {
                    await page.mouse.click(actualX, actualY, { button: "middle" });
                } else if (fname === "move") {
                    await page.mouse.move(actualX, actualY);
                }
            } else if (fname === "type" || fname === "type_text_at") {
                const actualX = args.x !== undefined ? denormalizeX(args.x, screenWidth) : null;
                const actualY = args.y !== undefined ? denormalizeY(args.y, screenHeight) : null;
                const text = args.text;
                const pressEnter = args.press_enter || false;

                if (actualX !== null && actualY !== null) {
                    await page.mouse.click(actualX, actualY);
                }
                // Clear field first
                await page.keyboard.press("Meta+A");
                await page.keyboard.press("Backspace");
                await page.keyboard.type(text);
                if (pressEnter) {
                    await page.keyboard.press("Enter");
                }
            } else if (fname === "navigate") {
                await page.goto(args.url);
            } else if (fname === "go_back") {
                await page.goBack();
            } else if (fname === "go_forward") {
                await page.goForward();
            } else if (fname === "wait") {
                await new Promise(resolve => setTimeout(resolve, (args.seconds || 1) * 1000));
            } else {
                console.log(`Warning: Custom or unhandled function ${fname}`);
            }

            await page.waitForLoadState('load', { timeout: 5000 }).catch(() => {});
            await new Promise(resolve => setTimeout(resolve, 1000));
        } catch (e) {
            console.log(`Error executing ${fname}: ${e}`);
            actionResult.error = e.message;
        }

        results.push([fname, functionCall.id, actionResult]);
    }

    return results;
}
```

### 4. تسجيل حالة البيئة الجديدة

التقط تمثيلاً للشاشة وأرسِله إلى النموذج.

### Python

```
def get_function_responses(page, results):
    screenshot_bytes = page.screenshot(type="png")
    current_url = page.url
    function_responses = []
    for name, call_id, result in results:
        function_responses.append({
            "type": "function_result",
            "name": name,
            "call_id": call_id,
            "result": [
                {
                    "type": "text",
                    "text": json.dumps({"url": current_url, **result})
                },
                {
                    "type": "image",
                    "data": base64.b64encode(screenshot_bytes).decode("utf-8"),
                    "mime_type": "image/png"
                }
            ]
        })
    return function_responses
```

### JavaScript

```
async function getFunctionResponses(page, results) {
    const screenshotBuffer = await page.screenshot({ type: 'png' });
    const screenshotBase64 = screenshotBuffer.toString('base64');
    const currentUrl = page.url();
    const functionResponses = [];

    for (const [name, callId, result] of results) {
        functionResponses.push({
            type: "function_result",
            name: name,
            call_id: callId,
            result: [
                {
                    type: "text",
                    text: JSON.stringify({ url: currentUrl, ...result })
                },
                {
                    type: "image",
                    data: screenshotBase64,
                    mime_type: "image/png"
                }
            ]
        });
    }
    return functionResponses;
}
```

بعد تحديد كيفية تسجيل حالة البيئة وتنسيقها، يمكنك دمج كل هذه الخطوات في حلقة تنفيذ مستمرة.

## إنشاء حلقة وكيل

لتفعيل التفاعلات المتعدّدة الخطوات، ادمِج الخطوات الأربع من قسم [كيفية تنفيذ ميزة "استخدام الكمبيوتر"](#implement-computer-use) في حلقة واحدة. تستمر هذه الحلقة في طلب تنفيذ إجراءات وإعادة النتائج إلى النموذج إلى أن تكتمل المهمة.

تذكَّر إدارة سجلّ المحادثات بشكل صحيح من خلال إضافة ردود النموذج وردود وظيفتك إلى السجلّ في كل خطوة.

### Python

```
import time
from typing import Any, List, Tuple
from playwright.sync_api import sync_playwright
from google import genai
from google.genai import types

client = genai.Client()

SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 900

print("Initializing browser...")
playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False)
context = browser.new_context(viewport={"width": SCREEN_WIDTH, "height": SCREEN_HEIGHT})
page = context.new_page()

# Paste helper functions execute_function_calls and get_function_responses here

try:
    page.goto("https://ai.google.dev/gemini-api/docs")

    config = types.GenerateContentConfig(
        tools=[types.Tool(computer_use=types.ComputerUse(
            environment=types.Environment.ENVIRONMENT_BROWSER,
            enable_prompt_injection_detection=True
        ))],
        thinking_config=types.ThinkingConfig(include_thoughts=True),
    )

    initial_screenshot = page.screenshot(type="png")
    USER_PROMPT = "Go to ai.google.dev/gemini-api/docs and search for pricing."
    print(f"Goal: {USER_PROMPT}")

    contents = [
        types.Content(role="user", parts=[
            types.Part(text=USER_PROMPT),
            types.Part.from_bytes(data=initial_screenshot, mime_type='image/png')
        ])
    ]

    # Agent Loop
    turn_limit = 5
    for i in range(turn_limit):
        print(f"\n--- Turn {i+1} ---")
        print("Thinking...")
        response = client.models.generate_content(
            model='gemini-3.5-flash',
            contents=contents,
            config=config,
        )

        candidate = response.candidates[0]
        contents.append(candidate.content)

        has_function_calls = any(part.function_call for part in candidate.content.parts)
        if not has_function_calls:
            text_response = " ".join(
                part.text for part in candidate.content.parts if hasattr(part, 'text')
            )
            print("Agent finished:", text_response)
            break

        print("Executing actions...")
        results = execute_function_calls(candidate, page, SCREEN_WIDTH, SCREEN_HEIGHT)

        print("Capturing state...")
        function_responses = get_function_responses(page, results)

        contents.append(
            types.Content(role="user", parts=[types.Part(function_response=fr) for fr in function_responses])
        )

finally:
    print("Closing browser...")
    browser.close()
    playwright.stop()
```

### JavaScript

```
import { chromium } from 'playwright';
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI();

// Constants for screen dimensions
const SCREEN_WIDTH = 1440;
const SCREEN_HEIGHT = 900;

console.log("Initializing browser...");
const browser = await chromium.launch({ headless: false });
const context = await browser.newContext({
    viewport: { width: SCREEN_WIDTH, height: SCREEN_HEIGHT }
});
const page = await context.newPage();

// Define helper functions. Copy/paste from steps 3 and 4:
// function denormalizeX(...)
// function denormalizeY(...)
// async function executeFunctionCalls(...)
// async function getFunctionResponses(...)

try {
    await page.goto("https://ai.google.dev/gemini-api/docs");

    const config = {
        tools: [{
            computerUse: {
                environment: "ENVIRONMENT_BROWSER",
                enable_prompt_injection_detection: true
            }
        }],
        thinkingConfig: { includeThoughts: true }
    };

    const initialScreenshotBuffer = await page.screenshot({ type: 'png' });
    const initialScreenshotBase64 = initialScreenshotBuffer.toString('base64');
    const USER_PROMPT = "Go to ai.google.dev/gemini-api/docs and search for pricing.";
    console.log(`Goal: ${USER_PROMPT}`);

    const contents = [
        {
            role: "user",
            parts: [
                { text: USER_PROMPT },
                {
                    inlineData: {
                        data: initialScreenshotBase64,
                        mimeType: "image/png"
                    }
                }
            ]
        }
    ];

    // Agent Loop
    const turnLimit = 5;
    for (let i = 0; i < turnLimit; i++) {
        console.log(`\n--- Turn ${i + 1} ---`);
        console.log("Thinking...");
        const response = await ai.models.generateContent({
            model: 'gemini-3.5-flash',
            contents: contents,
            config: config
        });

        const candidate = response.candidates[0];
        contents.push(candidate.content);

        const hasFunctionCalls = candidate.content.parts.some(part => part.functionCall);
        if (!hasFunctionCalls) {
            const textResponse = candidate.content.parts
                .filter(part => part.text)
                .map(part => part.text)
                .join(" ");
            console.log("Agent finished:", textResponse);
            break;
        }

        console.log("Executing actions...");
        const results = await executeFunctionCalls(candidate, page, SCREEN_WIDTH, SCREEN_HEIGHT);

        console.log("Capturing state...");
        const functionResponses = await getFunctionResponses(page, results);

        contents.push({
            role: "user",
            parts: functionResponses.map(fr => ({
                ...fr
            }))
        });
    }
} finally {
    console.log("Closing browser...");
    await browser.close();
}
```

## البيئات المتوافقة (Gemini 3.5 Flash)

يتوافق Gemini 3.5 Flash مع ثلاث بيئات محدّدة في إعدادات `computer_use`:

### بيئة المتصفّح (`ENVIRONMENT_BROWSER`)

إجراءات الإجراءات ضمن أداة المتصفّح:

| اسم الأمر | الوصف | الوسيطات (في استدعاء الدالة) |
| --- | --- | --- |
| **click** | انقر بالزر الأيسر للفأرة على الإحداثيات. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **double\_click** | انقر مرّتين على الإحداثيات. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **triple\_click** | النقر ثلاث مرات على الإحداثيات | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **middle\_click** | انقر بزر الماوس الأوسط على الإحداثيات. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **right\_click** | انقر بزر الماوس الأيمن على الإحداثيات. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **mouse\_down** | يضغط مع الاستمرار على زر الماوس عند الإحداثيات. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **mouse\_up** | يرفع إصبعك عن زر الماوس عند الإحداثيات. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **نقل** | تنقل هذه السمة المؤشر إلى الموضع المحدّد. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **type** | كتابة نص | `text`: str `press_enter`: bool (اختياري، القيمة التلقائية `false`) `intent`: str |
| **drag\_and\_drop** | يسحب عنصرًا من إحداثيات البداية إلى إحداثيات النهاية. | `start_y`: int (0-999) `start_x`: int (0-999) `end_y`: int (0-999) `end_x`: int (0-999) `intent`: str |
| **wait** | يوقف التنفيذ مؤقتًا لعدد محدّد من الثواني. | ‫`seconds`: int (اختياري، القيمة التلقائية `1`) `intent`: str |
| **press\_key** | يضغط على المفتاح المحدّد ثم يحرّره. | `key`: str `intent`: str |
| **key\_down** | يضغط مع الاستمرار على المفتاح المحدّد. | `key`: str `intent`: str |
| **key\_up** | تُستخدَم هذه الطريقة لتحرير المفتاح المحدّد. | `key`: str `intent`: str |
| **مفتاح الاختصار** | يضغط على مجموعة المفاتيح المحدّدة. | `keys`: `List[str]` `intent`: `str` |
| **take\_screenshot** | تعرض هذه الدالة لقطة شاشة للشاشة الحالية. | ‫`intent`: str |
| **scroll** | التمرير للأعلى أو للأسفل أو لليسار أو لليمين عند إحداثية معيّنة بمسافة بكسل | `y`: عدد صحيح (0-999) `x`: عدد صحيح (0-999) `direction`: سلسلة (`"up"`، `"down"`، `"left"`، `"right"`) `magnitude_in_pixels`: عدد صحيح (0-999، اختياري، القيمة التلقائية `300`) `intent`: سلسلة |
| **go\_back** | للرجوع إلى صفحة الويب السابقة في سجلّ المتصفّح | ‫`intent`: str |
| **navigate** | ينتقِل مباشرةً إلى عنوان URL محدّد. | `url`: str `intent`: str |
| **go\_forward** | ينتقِل إلى صفحة الويب التالية في سجلّ التصفّح. | ‫`intent`: str |

### بيئة الأجهزة الجوّالة (`ENVIRONMENT_MOBILE`)

إجراءات البيئة المحسّنة على Android:

| اسم الأمر | الوصف | الوسيطات (في استدعاء الدالة) |
| --- | --- | --- |
| **open\_app** | يفتح تطبيقًا باسمه. | `app_name`: str `intent`: str |
| **click** | انقر بالزر الأيسر للفأرة على الإحداثيات. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **list\_apps** | تعرض هذه الطريقة التطبيقات المتاحة على الجهاز، وتعرض أسماءها وأسماء حِزمها. | ‫`intent`: str |
| **wait** | يوقف التنفيذ مؤقتًا لعدد محدّد من الثواني. | ‫`seconds`: int (اختياري، القيمة التلقائية `1`) `intent`: str |
| **go\_back** | للرجوع إلى الشاشة أو صفحة الويب السابقة | ‫`intent`: str |
| **type** | كتابة نص | `text`: str `press_enter`: bool (اختياري، القيمة التلقائية `false`) `intent`: str |
| **drag\_and\_drop** | يسحب عنصرًا من إحداثيات البداية إلى إحداثيات النهاية. | `start_y`: int (0-999) `start_x`: int (0-999) `end_y`: int (0-999) `end_x`: int (0-999) `intent`: str |
| **long\_press** | تنفيذ ضغطة مع الاستمرار على إحداثيات معيّنة على الشاشة | ‫`y`: عدد صحيح (0-999) `x`: عدد صحيح (0-999) `seconds`: عدد صحيح (اختياري، القيمة التلقائية `2`) `intent`: سلسلة |
| **press\_key** | يضغط على المفتاح المحدّد ثم يحرّره. | `key`: str `intent`: str |
| **take\_screenshot** | تعرض هذه الدالة لقطة شاشة للشاشة الحالية. | ‫`intent`: str |

### بيئة الكمبيوتر المكتبي (`ENVIRONMENT_DESKTOP`)

أوامر المؤشر على مستوى نظام التشغيل في بيئات سطح المكتب:

| اسم الأمر | الوصف | الوسيطات (في استدعاء الدالة) |
| --- | --- | --- |
| **click** | انقر بالزر الأيسر للفأرة على الإحداثيات. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **double\_click** | انقر مرّتين على الإحداثيات. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **triple\_click** | النقر ثلاث مرات على الإحداثيات | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **middle\_click** | انقر بزر الماوس الأوسط على الإحداثيات. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **right\_click** | انقر بزر الماوس الأيمن على الإحداثيات. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **mouse\_down** | يضغط مع الاستمرار على زر الماوس عند الإحداثيات. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **mouse\_up** | يرفع إصبعك عن زر الماوس عند الإحداثيات. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **نقل** | تنقل هذه السمة المؤشر إلى الموضع المحدّد. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **type** | كتابة نص | `text`: str `press_enter`: bool (اختياري، القيمة التلقائية `false`) `intent`: str |
| **drag\_and\_drop** | يسحب عنصرًا من إحداثيات البداية إلى إحداثيات النهاية. | `start_y`: int (0-999) `start_x`: int (0-999) `end_y`: int (0-999) `end_x`: int (0-999) `intent`: str |
| **wait** | يوقف التنفيذ مؤقتًا لعدد محدّد من الثواني. | ‫`seconds`: int (اختياري، القيمة التلقائية `1`) `intent`: str |
| **press\_key** | يضغط على المفتاح المحدّد ثم يحرّره. | `key`: str `intent`: str |
| **key\_down** | يضغط مع الاستمرار على المفتاح المحدّد. | `key`: str `intent`: str |
| **key\_up** | تُستخدَم هذه الطريقة لتحرير المفتاح المحدّد. | `key`: str `intent`: str |
| **مفتاح الاختصار** | يضغط على مجموعة المفاتيح المحدّدة. | `keys`: `List[str]` `intent`: `str` |
| **take\_screenshot** | تعرض هذه الدالة لقطة شاشة للشاشة الحالية. | ‫`intent`: str |
| **scroll** | التمرير للأعلى أو للأسفل أو لليسار أو لليمين عند إحداثية معيّنة بمسافة بكسل | `y`: عدد صحيح (0-999) `x`: عدد صحيح (0-999) `direction`: سلسلة (`"up"`، `"down"`، `"left"`، `"right"`) `magnitude_in_pixels`: عدد صحيح (0-999، اختياري، القيمة التلقائية `300`) `intent`: سلسلة |

## إجراءات واجهة المستخدم المتوافقة مع الإصدارات القديمة (Gemini 2.5)

بالنسبة إلى النماذج القديمة (`gemini-2.5-computer-use-preview-10-2025`)، تتوفّر الإجراءات التالية:

| اسم الأمر | الوصف | الوسيطات (في استدعاء الدالة) | مثال على استدعاء الدالة |
| --- | --- | --- | --- |
| **open\_web\_browser** | يفتح متصفّح الويب. | بدون | `{"name": "open_web_browser", "args": {}}` |
| **wait\_5\_seconds** | يوقف التنفيذ مؤقتًا لمدة 5 ثوانٍ. | بدون | `{"name": "wait_5_seconds", "args": {}}` |
| **go\_back** | ينقلك هذا الزر إلى الصفحة السابقة في السجلّ. | بدون | `{"name": "go_back", "args": {}}` |
| **go\_forward** | للانتقال إلى الصفحة التالية في السجلّ | بدون | `{"name": "go_forward", "args": {}}` |
| **search** | ينتقِل إلى محرك البحث التلقائي. | بدون | `{"name": "search", "args": {}}` |
| **navigate** | ينقل المتصفّح مباشرةً إلى عنوان URL المحدّد. | ‫`url`: str | `{"name": "navigate", "args": {"url": "https://www.wikipedia.org"}}` |
| **click\_at** | النقرات في إحداثيات معيّنة | ‫`y`: عدد صحيح (من 0 إلى 999)، `x`: عدد صحيح (من 0 إلى 999) | `{"name": "click_at", "args": {"y": 300, "x": 500}}` |
| **hover\_at** | تحريك مؤشر الماوس إلى إحداثيات معيّنة | ‫`y`: عدد صحيح (من 0 إلى 999)، `x`: عدد صحيح (من 0 إلى 999) | `{"name": "hover_at", "args": {"y": 150, "x": 250}}` |
| **type\_text\_at** | كتابة نص في إحداثية | ‫`y`: عدد صحيح (0-999)، `x`: عدد صحيح (0-999)، `text`: سلسلة، `press_enter`: قيمة منطقية (اختيارية، القيمة التلقائية هي True)، `clear_before_typing`: قيمة منطقية (اختيارية، القيمة التلقائية هي True) | `{"name": "type_text_at", "args": {"y": 250, "x": 400, "text": "search", "press_enter": false}}` |
| **key\_combination** | اضغط على المفاتيح أو المجموعات. | ‫`keys`: str | `{"name": "key_combination", "args": {"keys": "Control+A"}}` |
| **scroll\_document** | تنتقل إلى أسفل صفحة الويب بأكملها. | ‫`direction`: str | `{"name": "scroll_document", "args": {"direction": "down"}}` |
| **scroll\_at** | يتم التمرير في الإحداثيات (x,y). | ‫`y`: int، ‏`x`: int، ‏`direction`: str، ‏`magnitude`: int (اختياري، القيمة التلقائية 800) | `{"name": "scroll_at", "args": {"y": 500, "x": 500, "direction": "down"}}` |
| **drag\_and\_drop** | عمليات السحب بين إحداثيتَين | ‫`y`: int، ‏`x`: int، ‏`destination_y`: int، ‏`destination_x`: int | `{"name": "drag_and_drop", "args": {"y": 100, "destination_y": 500, "destination_x": 500, "x": 100}}` |

## الدوال المخصّصة من تحديد المستخدم

يمكنك توسيع وظائف النموذج من خلال تضمين دوال مخصّصة يحدّدها المستخدم. على سبيل المثال، في سيناريوهات المشاركة البشرية (HITL)، يمكنك استبعاد الإجراءات التلقائية المحدّدة مسبقًا وتسجيل إجراءات مخصّصة.

#### أدوات Gemini 3.5 Flash المخصّصة

### Python

استبعِد إجراءات المتصفّح العادية المحدّدة مسبقًا (مثل `click`) وسجِّل أداة `yield_to_user` مخصّصة:

```
from google import genai
from google.genai import types

client = genai.Client()

yield_to_user_tool = types.FunctionDeclaration(
    name="yield_to_user",
    description="Yields control back to the user for assistance or verification when an automated action is unsafe or ambiguous.",
    parameters=types.Schema(
        type="OBJECT",
        properties={
            "reason": types.Schema(
                type="STRING",
                description="The reason why the agent is yielding control to the human."
            )
        },
        required=["reason"]
    )
)

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Click the submit button. If you need a second factor authentication code, ask me.",
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                computer_use=types.ComputerUse(
                    environment="ENVIRONMENT_MOBILE",
                    excluded_predefined_functions=["click"]
                )
            ),
            yield_to_user_tool
        ]
    )
)
```

#### أدوات مخصّصة (قديمة) في Gemini 2.5

### Python

```
from typing import Optional, Dict, Any
from google import genai
from google.genai import types

client = genai.Client()

# Define custom tools here
custom_functions = [...] # Describe parameters as FunctionDeclaration object

def make_generate_content_config():
    excluded_functions = ["open_web_browser", "wait_5_seconds", "go_back", "go_forward", "search", "navigate", "hover_at", "scroll_document", "key_combination", "drag_and_drop"]
    generate_content_config = types.GenerateContentConfig(
        tools=[
            types.Tool(
                computer_use=types.ComputerUse(
                    environment=types.Environment.ENVIRONMENT_BROWSER,
                    excluded_predefined_functions=excluded_functions
                )
            ),
            types.Tool(function_declarations=custom_functions)
        ]
    )
    return generate_content_config
```

## إدارة مستويات التفكير (Gemini 3.5 Flash)

بالنسبة إلى وكلاء استخدام الكمبيوتر، يمكنك ضبط مستويات تفكير مختلفة لتحقيق التوازن بين جودة الإجراء وسرعة التنفيذ. بشكل عام، تحقق مستويات التفكير المنخفضة توازنًا جيدًا لمهام التشغيل الآلي العادية.

## السلامة والأمان

### ضبط سياسات الأمان (Gemini 3.5 Flash)

يتضمّن نموذج Gemini 3.5 Flash فئات خدمات أمان مُدمَجة تحدّد تلقائيًا ما إذا كان تأكيد المستخدم مطلوبًا.

| فئة سياسة السلامة | الوصف |
| --- | --- |
| `FINANCIAL_TRANSACTIONS` | يحظر أو يشغّل تأكيدًا للإجراءات التي تتضمّن دفعات أو إتمام عملية شراء بالتجزئة أو سلعًا خاضعة للرقابة. |
| `SENSITIVE_DATA_MODIFICATION` | يحمي السجلات الصحية أو المالية أو الحكومية من التعديل غير المصرّح به. |
| `COMMUNICATION_TOOL` | يمنع الوكيل من إرسال رسائل إلكترونية أو رسائل محادثة أو مسودات بشكل مستقل. |
| `ACCOUNT_CREATION` | يمنع هذا الخيار الوكيل من تسجيل حسابات جديدة بشكل مستقل على المواقع الإلكترونية. |
| `DATA_MODIFICATION` | تنظّم هذه السياسة التعديلات العامة على نظام الملفات ومشاركة البيانات وحذف مساحة التخزين. |
| `USER_CONSENT_MANAGEMENT` | يتطلّب ذلك أن يتولّى المستخدم إدارة بانرات قبول ملفات تعريف الارتباط وإشعارات الخصوصية. |
| `LEGAL_TERMS_AND_AGREEMENTS` | يمنع النموذج من قبول بنود الخدمة أو العقود الملزمة قانونًا بشكل مستقل. |

#### تجاهل إعدادات الأمان

يمكنك إلغاء سياسات محدّدة من خلال تمرير عمليات الإلغاء:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Clean up the local folder by archiving old logs.",
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                computer_use=types.ComputerUse(
                    environment=types.Environment.ENVIRONMENT_DESKTOP,
                    disabled_safety_policies=[
                        types.SafetyPolicy.DATA_MODIFICATION
                    ]
                )
            )
        ]
    )
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI();

const response = await ai.models.generateContent({
  model: 'gemini-3.5-flash',
  contents: "Clean up the local folder by archiving old logs.",
  config: {
    tools: [{
      computerUse: {
        environment: "ENVIRONMENT_DESKTOP",
        disabledSafetyPolicies: [
          "DATA_MODIFICATION"
        ]
      }
    }]
  }
});
```

### رصد هجمات حقن الطلبات (Gemini 3.5 Flash)

آلية أمان اختيارية تفحص وحدات البكسل في لقطة الشاشة بحثًا عن تعليمات خفية معادية (مثل "تجاهل الأوامر السابقة") وتحظر التنفيذ عند رصدها.

### تأكيد قرار الأمان

قد يتضمّن الردّ المَعلمة `safety_decision` في وسيطات استدعاء الدالة:

```
{
  "function_call": {
    "name": "click_at",
    "args": {
      "x": 60,
      "y": 100,
      "safety_decision": {
        "explanation": "Must check check-box",
        "decision": "require_confirmation"
      }
    }
  }
}
```

إذا كانت قيمة `safety_decision` هي `require_confirmation`، اطلب من المستخدم النهائي اتّخاذ إجراء. إذا أكّد المستخدم ذلك، اضبط `safety_acknowledgement` في `FunctionResponse`.

### Python

```
def get_safety_confirmation(safety_decision):
    # Prompt user for confirmation
    print(f"Safety confirmation required: {safety_decision.get('explanation', '')}")
    return "CONTINUE" # Or TERMINATE

# Inside execute_function_calls, check for safety_decision:
if 'safety_decision' in function_call.args:
    decision = get_safety_confirmation(function_call.args['safety_decision'])
    if decision == "TERMINATE":
        break
    # Include safety_acknowledgement inside the action result
    action_result["safety_acknowledgement"] = True
```

### أفضل الممارسات المتعلّقة بالأمان

تتضمّن ميزة "استخدام الكمبيوتر" مخاطر فريدة تتعلّق بالأمان والتشغيل، إذ قد يواجه النموذج محتوًى غير موثوق به على الشاشات أو يرتكب أخطاءً في تنفيذ الإجراءات نيابةً عن المستخدم. اتّبِع أفضل الممارسات التالية لحماية بيانات المستخدمين وأنظمتهم:

1. **المشاركة البشرية (HITL):**

   - **فرض تأكيد المستخدم:** عندما يشير الرد المتعلّق بالسلامة إلى
     `require_confirmation` (أو عندما يتطلّب قرار السلامة القديم ذلك)، اطلب من المستخدم الموافقة.
   - **تقديم تعليمات أمان مخصّصة:** يمكنك تنفيذ تعليمات نظام مخصّصة لتحديد حدود الأمان الخاصة بك وفرضها. على سبيل المثال:

     ### Python

     ```
     from google import genai
     from google.genai import types

     system_instruction = """
     ## **RULE 1: Seek User Confirmation (USER_CONFIRMATION)**

     This is your first and most important check. If the next required action falls
     into any of the following categories, you MUST stop immediately, and seek the
     user's explicit permission.

     **Procedure for Seeking Confirmation:**
     * **For Consequential Actions:** Perform all preparatory steps (e.g., navigating,
       filling out forms, typing a message). You will ask for confirmation **AFTER**
       all necessary information is entered on the screen, but **BEFORE** you perform
       the final, irreversible action (e.g., before clicking "Send", "Submit",
       "Confirm Purchase", "Share").
     * **For Prohibited Actions:** If the action is strictly forbidden (e.g., accepting
       legal terms, solving a CAPTCHA), you must first inform the user about the
       required action and ask for their confirmation to proceed.

     **USER_CONFIRMATION Categories:**

     *   **Consent and Agreements:** You are FORBIDDEN from accepting, selecting, or
         agreeing to any of the following on the user's behalf. You must ask the
         user to confirm before performing these actions.
         *   Terms of Service
         *   Privacy Policies
         *   Cookie consent banners
         *   End User License Agreements (EULAs)
         *   Any other legally significant contracts or agreements.
     *   **Robot Detection:** You MUST NEVER attempt to solve or bypass the
         following. You must ask the user to confirm before performing these actions.
         *   CAPTCHAs (of any kind)
         *   Any other anti-robot or human-verification mechanisms, even if you are
             capable.
     *   **Financial Transactions:**
         *   Completing any purchase.
         *   Managing or moving money (e.g., transfers, payments).
         *   Purchasing regulated goods or participating in gambling.
     *   **Sending Communications:**
         *   Sending emails.
         *   Sending messages on any platform (e.g., social media, chat apps).
         *   Posting content on social media or forums.
     *   **Accessing or Modifying Sensitive Information:**
         *   Health, financial, or government records (e.g., medical history, tax
             forms, passport status).
         *   Revealing or modifying sensitive personal identifiers (e.g., SSN, bank
             account number, credit card number).
     *   **User Data Management:**
         *   Accessing, downloading, or saving files from the web.
         *   Sharing or sending files/data to any third party.
         *   Transferring user data between systems.
     *   **Browser Data Usage:**
         *   Accessing or managing Chrome browsing history, bookmarks, autofill data,
             or saved passwords.
     *   **Security and Identity:**
         *   Logging into any user account.
         *   Any action that involves misrepresentation or impersonation (e.g.,
             creating a fan account, posting as someone else).
     *   **Insurmountable Obstacles:** If you are technically unable to interact with
         a user interface element or are stuck in a loop you cannot resolve, ask the
         user to take over.
     ---

     ## **RULE 2: Default Behavior (ACTUATE)**

     If an action does **NOT** fall under the conditions for `USER_CONFIRMATION`,
     your default behavior is to **Actuate**.

     **Actuation Means:**  You MUST proactively perform all necessary steps to move
     the user's request forward. Continue to actuate until you either complete the
     non-consequential task or encounter a condition defined in Rule 1.

     *   **Example 1:** If asked to send money, you will navigate to the payment
         portal, enter the recipient's details, and enter the amount. You will then
         **STOP** as per Rule 1 and ask for confirmation before clicking the final
         "Send" button.
     *   **Example 2:** If asked to post a message, you will navigate to the site,
         open the post composition window, and write the full message. You will then
         **STOP** as per Rule 1 and ask for confirmation before clicking the final
         "Post" button.

         After the user has confirmed, remember to get the user's latest screen
         before continuing to perform actions.

     # Final Response Guidelines:
     Write final response to the user in the following cases:
     - User confirmation
     - When the task is complete or you have enough information to respond to the user
     """

     client = genai.Client()
     response = client.models.generate_content(
         model="gemini-3.5-flash",
         contents="Prepare a draft but do not send.",
         config=types.GenerateContentConfig(
             system_instruction=system_instruction,
             tools=[types.Tool(computer_use=types.ComputerUse(environment="ENVIRONMENT_BROWSER"))]
         )
     )
     ```

     ### JavaScript

     ```
     import { GoogleGenAI } from '@google/genai';

     const ai = new GoogleGenAI();

     const systemInstruction = `
     ## **RULE 1: Seek User Confirmation (USER_CONFIRMATION)**

     This is your first and most important check. If the next required action falls
     into any of the following categories, you MUST stop immediately, and seek the
     user's explicit permission.

     **Procedure for Seeking Confirmation:**
     * **For Consequential Actions:** Perform all preparatory steps (e.g., navigating,
       filling out forms, typing a message). You will ask for confirmation **AFTER**
       all necessary information is entered on the screen, but **BEFORE** you perform
       the final, irreversible action (e.g., before clicking "Send", "Submit",
       "Confirm Purchase", "Share").
     * **For Prohibited Actions:** If the action is strictly forbidden (e.g., accepting
       legal terms, solving a CAPTCHA), you must first inform the user about the
       required action and ask for their confirmation to proceed.

     **USER_CONFIRMATION Categories:**

     *   **Consent and Agreements:** You are FORBIDDEN from accepting, selecting, or
         agreeing to any of the following on the user's behalf. You must ask the
         user to confirm before performing these actions.
         *   Terms of Service
         *   Privacy Policies
         *   Cookie consent banners
         *   End User License Agreements (EULAs)
         *   Any other legally significant contracts or agreements.
     *   **Robot Detection:** You MUST NEVER attempt to solve or bypass the
         following. You must ask the user to confirm before performing these actions.
         *   CAPTCHAs (of any kind)
         *   Any other anti-robot or human-verification mechanisms, even if you are
             capable.
     *   **Financial Transactions:**
         *   Compleying any purchase.
         *   Managing or moving money (e.g., transfers, payments).
         *   Purchasing regulated goods or participating in gambling.
     *   **Sending Communications:**
         *   Sending emails.
         *   Sending messages on any platform (e.g., social media, chat apps).
         *   Posting content on social media or forums.
     *   **Accessing or Modifying Sensitive Information:**
         *   Health, financial, or government records (e.g., medical history, tax
             forms, passport status).
         *   Revealing or modifying sensitive personal identifiers (e.g., SSN, bank
             account number, credit card number).
     *   **User Data Management:**
         *   Accessing, downloading, or saving files from the web.
         *   Sharing or sending files/data to any third party.
         *   Transferring user data between systems.
     *   **Browser Data Usage:**
         *   Accessing or managing Chrome browsing history, bookmarks, autofill data,
             or saved passwords.
     *   **Security and Identity:**
         *   Logging into any user account.
         *   Any action that involves misrepresentation or impersonation (e.g.,
             creating a fan account, posting as someone else).
     *   **Insurmountable Obstacles:** If you are technically unable to interact with
         a user interface element or are stuck in a loop you cannot resolve, ask the
         user to take over.
     ---

     ## **RULE 2: Default Behavior (ACTUATE)**

     If an action does **NOT** fall under the conditions for `USER_CONFIRMATION`,
     your default behavior is to **Actuate**.

     **Actuation Means:**  You MUST proactively perform all necessary steps to move
     the user's request forward. Continue to actuate until you either complete the
     non-consequential task or encounter a condition defined in Rule 1.

     *   **Example 1:** If asked to send money, you will navigate to the payment
         portal, enter the recipient's details, and enter the amount. You will then
         **STOP** as per Rule 1 and ask for confirmation before clicking the final
         "Send" button.
     *   **Example 2:** If asked to post a message, you will navigate to the site,
         open the post composition window, and write the full message. You will then
         **STOP** as per Rule 1 and ask for confirmation before clicking the final
         "Post" button.

         After the user has confirmed, remember to get the user's latest screen
         before continuing to perform actions.

     # Final Response Guidelines:
     Write final response to the user in the following cases:
     - User confirmation
     - When the task is complete or you have enough information to respond to the user
     `;

     const response = await ai.models.generateContent({
       model: 'gemini-3.5-flash',
       contents: "Prepare a draft but do not send.",
       config: {
         systemInstruction: systemInstruction,
         tools: [{
           computerUse: {
             environment: "ENVIRONMENT_BROWSER"
           }
         }]
       }
     });
     ```
2. **بيئة التنفيذ الآمنة:** شغِّل الوكيل في بيئة آمنة ومحمية
   للحدّ من تأثيره المحتمَل. يمكن أن يكون ذلك عبارة عن آلة افتراضية (VM) في بيئة معزولة أو حاوية (مثل Docker) أو ملف شخصي مخصّص للمتصفّح مع أذونات محدودة. يمكنك الاطّلاع على [التنفيذ المرجعي على GitHub](https://github.com/google/computer-use-preview/) للحصول على إرشادات حول إعداد وضع الحماية باستخدام Docker.
3. **تنقية المدخلات:** يجب تنقية كل النص الذي ينشئه المستخدمون في الطلبات للحد من خطر التعليمات غير المقصودة أو هجمات حقن الطلبات. هذه الطبقة مفيدة للأمان، ولكنّها لا تحلّ محل بيئة التنفيذ الآمنة.
4. **ضوابط المحتوى:** استخدِم ضوابط المحتوى وواجهات برمجة التطبيقات الخاصة بسلامة المحتوى لتقييم مدى ملاءمة مدخلات المستخدمين ومدخلات الأدوات ومخرجاتها وردود الوكيل، بالإضافة إلى رصد عمليات حقن التعليمات البرمجية وعمليات تجاوز القيود.
5. **القوائم المسموح بها والقوائم المحظورة:** استخدِم آليات فلترة للتحكّم في الأماكن التي يمكن للنموذج الانتقال إليها والإجراءات التي يمكنه اتّخاذها. تُعدّ القائمة المحظورة التي تتضمّن المواقع الإلكترونية المحظورة نقطة بداية جيدة، بينما تكون القائمة المسموح بها الأكثر تقييدًا أكثر أمانًا.
6. **إمكانية تتبّع البيانات وتسجيل البيانات:** احتفِظ بسجلات مفصّلة لتصحيح الأخطاء والتدقيق والاستجابة للحوادث. على البرنامج تسجيل الطلبات، ولقطات الشاشة، والإجراءات التي تقترحها النماذج (`function_call`)، والردود الآمنة، وجميع الإجراءات التي ينفّذها البرنامج في النهاية.
7. **إدارة البيئة:** تأكَّد من اتساق بيئة واجهة المستخدم الرسومية.
   قد تؤدي النوافذ المنبثقة أو الإشعارات أو التغييرات غير المتوقّعة في التنسيق إلى إرباك النموذج. ابدأ من حالة معروفة ونظيفة لكل مهمة جديدة إذا أمكن ذلك.

## إصدارات النموذج

يمكنك استخدام ميزة "استخدام الكمبيوتر" مع الطُرز التالية:

- [**‫Gemini 3.5 Flash**](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=ar) (`gemini-3.5-flash`): النموذج المقترَح للاستخدام على الكمبيوتر، ويتميّز بإجراءات مبسطة مع نوايا، ويتوافق مع بيئات المتصفح والأجهزة الجوّالة وأجهزة الكمبيوتر، ويتضمّن سياسات أمان قابلة للضبط، ويتيح رصد عمليات حقن الطلبات.
- [**معاينة Gemini 3 Flash**](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=ar) (`gemini-3-flash-preview`): نموذج معاينة
  متوافق مع أجهزة الكمبيوتر
- [**‫Gemini 2.5 (إصدار تجريبي قديم)**](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-computer-use-preview-10-2025?hl=ar) (`gemini-2.5-computer-use-preview-10-2025`): نموذج إصدار تجريبي قديم محسّن للاستخدام على أجهزة الكمبيوتر المستندة إلى المتصفّح

## الخطوات التالية

- جرِّب استخدام الكمبيوتر في [بيئة العرض التوضيحي Browserbase](http://gemini.browserbase.com).
- اطّلِع على [التنفيذ المرجعي](https://github.com/google/computer-use-preview) للحصول على مثال على الرمز البرمجي.
- مزيد من المعلومات حول أدوات Gemini API الأخرى:
  - [استدعاء الدوال](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar)
  - [تحديد المصدر من خلال "بحث Google"](https://ai.google.dev/gemini-api/docs/grounding?hl=ar)

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-06-25 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-06-25 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
