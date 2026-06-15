---
source_url: https://ai.google.dev/gemini-api/docs/interactions/computer-use?hl=ar
fetched_at: 2026-06-15T06:25:11.768382+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# استخدام الكمبيوتر

تتيح لك ميزة "استخدام الكمبيوتر" إنشاء وكلاء للتحكّم في المتصفّح يتفاعلون مع المهام وينفّذونها آليًا. باستخدام لقطات الشاشة، يمكن للنموذج "رؤية" شاشة الكمبيوتر و "التصرف" من خلال إنشاء إجراءات معيّنة في واجهة المستخدم، مثل نقرات الماوس وإدخالات لوحة المفاتيح. على غرار ميزة &quot;استدعاء الدالة&quot;، عليك كتابة الرمز البرمجي للتطبيق من جهة العميل لتلقّي إجراءات &quot;استخدام الكمبيوتر&quot; وتنفيذها.

باستخدام "استخدام الكمبيوتر"، يمكنك إنشاء وكلاء تنفيذ يمكنهم:

- أتمتة إدخال البيانات المتكرّر أو ملء النماذج على المواقع الإلكترونية
- إجراء اختبار آلي لتطبيقات الويب وتفاعلات المستخدمين
- إجراء بحث على مواقع إلكترونية مختلفة (مثل جمع معلومات عن المنتجات وأسعارها ومراجعاتها من مواقع التجارة الإلكترونية لاتخاذ قرار بشأن الشراء)

أسهل طريقة لاختبار إمكانية "استخدام الكمبيوتر" هي من خلال [التنفيذ المرجعي](https://github.com/google/computer-use-preview/) أو [بيئة العرض التوضيحي في Browserbase](http://gemini.browserbase.com).

## طريقة عمل ميزة "استخدام الكمبيوتر"

لإنشاء وكيل للتحكّم في المتصفّح باستخدام نموذج "استخدام الكمبيوتر"، عليك تنفيذ حلقة وكيل تنفّذ ما يلي:

1. [**إرسال طلب إلى النموذج**](#send-request)

   - أضِف أداة &quot;استخدام الكمبيوتر&quot; وأي وظائف مخصّصة يحدّدها المستخدم أو وظائف مستبعَدة إلى طلب بيانات من واجهة برمجة التطبيقات (اختياري).
   - قدِّم طلب المستخدم إلى نموذج "استخدام الكمبيوتر".
2. [**تلقّي ردّ النموذج**](#model-response)

   - يحلّل نموذج "استخدام الكمبيوتر" طلب المستخدم ولقطة الشاشة، وينشئ ردًا يتضمّن `function_call` مقترحًا يمثّل إجراءً في واجهة المستخدم (مثل "النقر على الإحداثية (س، ص)" أو "كتابة النص"). للاطّلاع على وصف لجميع إجراءات واجهة المستخدم التي يتيحها نموذج استخدام الكمبيوتر، يُرجى الانتقال إلى [الإجراءات المتاحة](#supported-actions).
   - قد يتضمّن ردّ واجهة برمجة التطبيقات أيضًا `safety_decision` من نظام أمان داخلي يتحقّق من الإجراء المقترَح من النموذج. يصنّف هذا `safety_decision` الإجراء على النحو التالي:
     - **عادي / مسموح به:** يُعتبر الإجراء آمنًا، وقد لا يظهر الرمز `safety_decision` في هذه الحالة.
     - **يتطلّب تأكيدًا (`require_confirmation`):** يعني ذلك أنّ النموذج على وشك تنفيذ إجراء قد يكون محفوفًا بالمخاطر (مثل النقر على "بانر ملفات تعريف الارتباط").
3. [**تنفيذ الإجراء الذي تم تلقّيه**](#execute-actions)

   - يتلقّى الرمز البرمجي من جهة العميل `function_call` وأي `safety_decision` مصاحب.
     - **عادي / مسموح به:** إذا كان `safety_decision` يشير إلى عادي/مسموح به (أو إذا لم يكن `safety_decision` متوفّرًا)، يمكن أن ينفّذ الرمز البرمجي من جهة العميل `function_call` المحدّد في بيئتك المستهدَفة (مثل متصفّح الويب).
     - **يتطلّب تأكيدًا:** إذا كان `safety_decision` يشير إلى أنّه
       يتطلّب تأكيدًا، يجب أن يطلب تطبيقك من المستخدم النهائي
       تأكيدًا قبل تنفيذ `function_call`. إذا أكّد المستخدم، يمكنك المتابعة لتنفيذ الإجراء. إذا رفض المستخدم، لا تنفِّذ الإجراء.
4. [**تسجيل حالة البيئة الجديدة**](#capture-state)

   - إذا تم تنفيذ الإجراء، يلتقط تطبيقك لقطة شاشة جديدة لواجهة المستخدم الرسومية وعنوان URL الحالي لإرسالهما مرة أخرى إلى نموذج &quot;استخدام الكمبيوتر&quot; كجزء من `function_result`.
   - إذا حظر نظام الأمان إجراءً أو رفض المستخدم تأكيده، قد يرسل تطبيقك نوعًا مختلفًا من الملاحظات إلى النموذج أو ينهي التفاعل.

وتتكرّر هذه العملية بدءًا من الخطوة 2، حيث يستخدم النموذج لقطة الشاشة الجديدة والهدف المستمر لاقتراح الإجراء التالي. تستمر الحلقة إلى أن يتم إكمال المهمة أو يحدث خطأ أو يتم إنهاء العملية (على سبيل المثال، بسبب استجابة أمان "حظر" أو قرار المستخدم).

![نظرة عامة حول استخدام الكمبيوتر](https://ai.google.dev/static/gemini-api/docs/images/computer_use.png?hl=ar)

## كيفية تنفيذ ميزة "استخدام الكمبيوتر"

قبل استخدام أداة &quot;استخدام الكمبيوتر&quot;، عليك إعداد ما يلي:

- **بيئة التنفيذ الآمنة:** لأسباب تتعلق بالأمان، يجب تشغيل وكيل &quot;استخدام الكمبيوتر&quot; في بيئة آمنة ومراقَبة (مثل جهاز افتراضي في وضع الحماية أو حاوية أو ملف شخصي مخصّص للمتصفّح مع أذونات محدودة).
- **معالج الإجراءات من جهة العميل:** عليك تنفيذ منطق من جهة العميل لتنفيذ الإجراءات التي ينشئها النموذج والتقاط لقطات شاشة للبيئة بعد كل إجراء.

تستخدِم الأمثلة الواردة في هذا القسم متصفّحًا كبيئة تنفيذ، وتستخدِم [Playwright](https://playwright.dev/) كأداة معالجة الإجراءات من جهة العميل. لتشغيل هذه النماذج، عليك تثبيت التبعيات اللازمة وتهيئة مثيل متصفّح Playwright:

### ‫0. تثبيت Playwright

```
pip install google-genai playwright
playwright install chromium
```

### ‫0. تهيئة مثيل متصفّح Playwright

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

يتم تضمين نموذج رمز برمجي للتوسيع إلى بيئة Android في قسم [استخدام الدوال المخصّصة التي يحدّدها المستخدم](#custom-functions).

### 1. إرسال طلب إلى النموذج

أضِف أداة "استخدام الكمبيوتر" إلى طلب بيانات من واجهة برمجة التطبيقات وأرسِل طلبًا إلى النموذج يتضمّن هدف المستخدم. يجب استخدام أحد الطُرز المتوافقة مع ميزة "استخدام الكمبيوتر"، وإلا سيظهر لك خطأ:

- `gemini-2.5-computer-use-preview-10-2025`
- `gemini-3-flash-preview`

يمكنك أيضًا إضافة المَعلمات الاختيارية التالية:

- **الإجراءات المستبعَدة:** إذا كانت هناك أي إجراءات من قائمة [إجراءات واجهة المستخدم المتوافقة](#supported-actions) لا تريد أن يتّخذها النموذج، حدِّد هذه الإجراءات على أنّها `excluded_predefined_functions`.
- **الدوال المعرَّفة من قِبل المستخدم:** بالإضافة إلى أداة "استخدام الكمبيوتر"، قد تحتاج إلى تضمين دوال مخصّصة معرَّفة من قِبل المستخدم.

يُرجى العِلم أنّه ليس من الضروري تحديد حجم العرض عند إرسال طلب،
إذ يتوقّع النموذج إحداثيات البكسل التي تم تغيير حجمها لتناسب ارتفاع الشاشة وعرضها.

### Python

```
from google import genai

client = genai.Client()

# Specify predefined functions to exclude (optional)
excluded_functions = ["drag_and_drop"]

interaction = client.interactions.create(
    model='gemini-2.5-computer-use-preview-10-2025',
    input="Search for highly rated smart fridges with touchscreen, 2 doors, around 25 cu ft, priced below 4000 dollars on Google Shopping. Create a bulleted list of the 3 cheapest options in the format of name, description, price in an easy-to-read layout.",
    tools=[
        {
            "type": "computer_use",
            "environment": "browser",
            "excluded_predefined_functions": excluded_functions
        }
    ]
)

print(interaction)
```

للاطّلاع على مثال يتضمّن دوال مخصّصة، راجِع [استخدام دوال مخصّصة](#custom-functions).

### 2. تلقّي ردّ النموذج

عند تفعيل أداة &quot;استخدام الكمبيوتر&quot;، سيستجيب النموذج بخطوة واحدة أو أكثر من `function_call` إذا حدّد أنّ إكمال المهمة يتطلّب اتّخاذ إجراءات في واجهة المستخدم.
تتيح أداة "استخدام الكمبيوتر" تنفيذ عدة وظائف بالتوازي، ما يعني أنّ النموذج يمكنه عرض إجراءات متعددة في رد واحد.

في ما يلي مثال على ردّ النموذج.

```
{
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "I will type the search query into the search bar. The search bar is in the center of the page."
        }
      ]
    },
    {
      "type": "function_call",
      "name": "type_text_at",
      "arguments": {
        "x": 371,
        "y": 470,
        "text": "highly rated smart fridges with touchscreen, 2 doors, around 25 cu ft, priced below 4000 dollars on Google Shopping",
        "press_enter": true
      }
    }
  ]
}
```

### 3- تنفيذ الإجراءات التي تم تلقّيها

يجب أن يحلّل الرمز البرمجي لتطبيقك استجابة النموذج، وينفّذ الإجراءات، ويجمع النتائج.

يستخرج نموذج التعليمات البرمجية التالي طلبات الدوال من استجابة نموذج "استخدام الكمبيوتر"، ويحوّلها إلى إجراءات يمكن تنفيذها باستخدام Playwright.
يُخرج النموذج إحداثيات عادية (0-999) بغض النظر عن أبعاد الصورة المدخلة، لذا فإنّ جزءًا من خطوة الترجمة هو تحويل هذه الإحداثيات العادية مرة أخرى إلى قيم البكسل الفعلية.

حجم الشاشة المقترَح للاستخدام مع نموذج &quot;استخدام الكمبيوتر&quot; هو (1440, 900)، وسيعمل النموذج مع أي دقة، ولكن قد تتأثر جودة النتائج.

يُرجى العِلم أنّ هذا المثال يتضمّن فقط عملية التنفيذ الخاصة بإجراءات واجهة المستخدم الثلاثة الأكثر شيوعًا: `open_web_browser` و`click_at` و`type_text_at`. بالنسبة إلى حالات الاستخدام في مرحلة الإنتاج، عليك تنفيذ جميع إجراءات واجهة المستخدم الأخرى من قائمة [الإجراءات المتوافقة](#supported-actions) ما لم تُضِفها بشكل صريح كـ `excluded_predefined_functions`.

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
    function_calls = [
        step for step in interaction.steps if step.type == "function_call"
    ]

    for function_call in function_calls:
        action_result = {}
        fname = function_call.name
        args = function_call.arguments
        print(f"  -> Executing: {fname}")

        try:
            if fname == "open_web_browser":
                pass # Already open
            elif fname == "click_at":
                actual_x = denormalize_x(args["x"], screen_width)
                actual_y = denormalize_y(args["y"], screen_height)
                page.mouse.click(actual_x, actual_y)
            elif fname == "type_text_at":
                actual_x = denormalize_x(args["x"], screen_width)
                actual_y = denormalize_y(args["y"], screen_height)
                text = args["text"]
                press_enter = args.get("press_enter", False)

                page.mouse.click(actual_x, actual_y)
                # Simple clear (Command+A, Backspace for Mac)
                page.keyboard.press("Meta+A")
                page.keyboard.press("Backspace")
                page.keyboard.type(text)
                if press_enter:
                    page.keyboard.press("Enter")
            else:
                print(f"Warning: Unimplemented or custom function {fname}")

            # Wait for potential navigations/renders
            page.wait_for_load_state(timeout=5000)
            time.sleep(1)

        except Exception as e:
            print(f"Error executing {fname}: {e}")
            action_result = {"error": str(e)}

        results.append((fname, function_call.id, action_result))

    return results
```

### 4. تسجيل حالة البيئة الجديدة

بعد تنفيذ الإجراءات، أرسِل نتيجة تنفيذ الدالة إلى النموذج ليتمكّن من استخدام هذه المعلومات لإنشاء الإجراء التالي. في حال تنفيذ إجراءات متعدّدة (طلبات متوازية)، عليك إرسال `function_result` لكل إجراء في رد المستخدم التالي.

### Python

```
import json
import base64

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

## إنشاء حلقة وكيل

لتفعيل التفاعلات المتعدّدة الخطوات، ادمِج الخطوات الأربع من قسم [كيفية تنفيذ استخدام الكمبيوتر](#implement-computer-use) في حلقة.
تذكَّر إدارة سجلّ المحادثات بشكل صحيح من خلال إضافة ردود النموذج وردود الوظيفة.

لتشغيل عينة التعليمات البرمجية هذه، عليك إجراء ما يلي:

- ثبِّت [التبعيات اللازمة في Playwright](#implement-computer-use).
- حدِّد الدوال المساعدة من الخطوتَين [(3) تنفيذ الإجراءات المستلَمة](#execute-actions) و[(4) تسجيل حالة البيئة الجديدة](#capture-state).

### Python

```
import time
from typing import Any, List, Tuple
from playwright.sync_api import sync_playwright

from google import genai

client = genai.Client()

# Constants for screen dimensions
SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 900

# Setup Playwright
print("Initializing browser...")
playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False)
context = browser.new_context(viewport={"width": SCREEN_WIDTH, "height": SCREEN_HEIGHT})
page = context.new_page()

# Define helper functions. Copy/paste from steps 3 and 4
# def denormalize_x(...)
# def denormalize_y(...)
# def execute_function_calls(...)
# def get_function_responses(...)

try:
    # Go to initial page
    page.goto("https://ai.google.dev/gemini-api/docs")

    # Take initial screenshot
    initial_screenshot = page.screenshot(type="png")
    USER_PROMPT = "Go to ai.google.dev/gemini-api/docs and search for pricing."
    print(f"Goal: {USER_PROMPT}")

    # First interaction
    interaction = client.interactions.create(
        model='gemini-2.5-computer-use-preview-10-2025',
        input=[
            {"type": "text", "text": USER_PROMPT},
            {"type": "image", "data": base64.b64encode(initial_screenshot).decode("utf-8"), "mime_type": "image/png"}
        ],
        tools=[{
            "type": "computer_use",
            "environment": "browser"
        }]
    )

    # Agent Loop
    turn_limit = 5
    for i in range(turn_limit):
        print(f"\n--- Turn {i+1} ---")

        has_function_calls = any(
            step.type == "function_call"
            for step in interaction.steps
        )
        if not has_function_calls:
            text_response = " ".join([
                content_block.text for step in interaction.steps if step.type == "model_output"
                for content_block in step.content if content_block.type == "text"
            ])
            print("Agent finished:", text_response)
            break

        print("Executing actions...")
        results = execute_function_calls(interaction, page, SCREEN_WIDTH, SCREEN_HEIGHT)

        print("Capturing state...")
        function_responses = get_function_responses(page, results)

        # Continue conversation with function responses
        interaction = client.interactions.create(
            model='gemini-2.5-computer-use-preview-10-2025',
            previous_interaction_id=interaction.id,
            input=function_responses,
            tools=[{
                "type": "computer_use",
                "environment": "browser"
            }]
        )

finally:
    # Cleanup
    print("\nClosing browser...")
    browser.close()
    playwright.stop()
```

## استخدام دوال مخصّصة من تحديد المستخدم

يمكنك اختياريًا تضمين دوال مخصّصة يحدّدها المستخدم في طلبك لتوسيع وظائف النموذج. يعدّل المثال التالي نموذج استخدام الكمبيوتر وأدواته ليناسب حالات الاستخدام على الأجهزة الجوّالة من خلال تضمين إجراءات مخصّصة يحدّدها المستخدم، مثل `open_app` و`long_press_at` و`go_home`، مع استبعاد الإجراءات الخاصة بالمتصفح. يمكن للنموذج استدعاء هذه الدوال المخصّصة بذكاء إلى جانب إجراءات واجهة المستخدم العادية لإكمال المهام في بيئات غير المتصفّح.

### Python

```
from typing import Optional, Dict, Any

from google import genai

client = genai.Client()

SYSTEM_PROMPT = """You are operating an Android phone. Today's date is October 15, 2023, so ignore any other date provided.
* To provide an answer to the user, *do not use any tools* and output your answer on a separate line. IMPORTANT: Do not add any formatting or additional punctuation/text, just output the answer by itself after two empty lines.
* Make sure you scroll down to see everything before deciding something isn't available.
* You can open an app from anywhere. The icon doesn't have to currently be on screen.
* Unless explicitly told otherwise, make sure to save any changes you make.
* If text is cut off or incomplete, scroll or click into the element to get the full text before providing an answer.
* IMPORTANT: Complete the given task EXACTLY as stated. DO NOT make any assumptions that completing a similar task is correct.  If you can't find what you're looking for, SCROLL to find it.
* If you want to edit some text, ONLY USE THE `type` tool. Do not use the onscreen keyboard.
* Quick settings shouldn't be used to change settings. Use the Settings app instead.
* The given task may already be completed. If so, there is no need to do anything.
"""

# Custom function definitions for mobile
custom_functions = [
    {
        "type": "function",
        "name": "open_app",
        "description": "Opens an app by name.",
        "parameters": {
            "type": "object",
            "properties": {
                "app_name": {"type": "string", "description": "Name of the app to open"},
                "intent": {"type": "string", "description": "Optional deep-link or action"}
            },
            "required": ["app_name"]
        }
    },
    {
        "type": "function",
        "name": "long_press_at",
        "description": "Long-press at a specific screen coordinate.",
        "parameters": {
            "type": "object",
            "properties": {
                "x": {"type": "integer", "description": "X coordinate"},
                "y": {"type": "integer", "description": "Y coordinate"}
            },
            "required": ["x", "y"]
        }
    },
    {
        "type": "function",
        "name": "go_home",
        "description": "Navigates to the device home screen.",
        "parameters": {"type": "object", "properties": {}}
    }
]

# Exclude browser-specific functions
excluded_functions = [
    "open_web_browser",
    "search",
    "navigate",
    "hover_at",
    "scroll_document",
    "go_forward",
    "key_combination",
    "drag_and_drop",
]

interaction = client.interactions.create(
    model='gemini-2.5-computer-use-preview-10-2025',
    system_instruction=SYSTEM_PROMPT,
    input="Open Chrome, then long-press at 200,400.",
    tools=[
        {
            "type": "computer_use",
            "environment": "browser",
            "excluded_predefined_functions": excluded_functions
        },
        *custom_functions
    ]
)

print(interaction)
```

## إجراءات واجهة المستخدم المتوافقة

يمكن للنموذج طلب تنفيذ إجراءات واجهة المستخدم التالية باستخدام
`function_call`. يجب أن ينفّذ الرمز البرمجي من جهة العميل منطق التنفيذ لهذه الإجراءات. يمكنك الاطّلاع على [التنفيذ المرجعي](https://github.com/google/computer-use-preview) للحصول على أمثلة.

| اسم الأمر | الوصف | الوسيطات (في استدعاء الدالة) | مثال على استدعاء الدالة |
| --- | --- | --- | --- |
| **open\_web\_browser** | يفتح متصفّح الويب. | بدون | `{"name": "open_web_browser", "arguments": {}}` |
| **wait\_5\_seconds** | توقف التنفيذ مؤقتًا لمدة 5 ثوانٍ للسماح بتحميل المحتوى الديناميكي أو إكمال الصور المتحركة. | بدون | `{"name": "wait_5_seconds", "arguments": {}}` |
| **go\_back** | للانتقال إلى الصفحة السابقة في سجلّ المتصفّح | بدون | `{"name": "go_back", "arguments": {}}` |
| **go\_forward** | ينتقِل إلى الصفحة التالية في سجلّ المتصفّح. | بدون | `{"name": "go_forward", "arguments": {}}` |
| **search** | ينتقِل إلى الصفحة الرئيسية لمحرّك البحث التلقائي (مثل Google)، وهو مفيد لبدء مهمة بحث جديدة. | بدون | `{"name": "search", "arguments": {}}` |
| **navigate** | ينقل المتصفّح مباشرةً إلى عنوان URL المحدّد. | ‫`url`: str | `{"name": "navigate", "arguments": {"url": "https://www.wikipedia.org"}}` |
| **click\_at** | تنقر هذه السمة على إحداثيات معيّنة في صفحة الويب. وتستند قيمتا x وy إلى شبكة 1000x1000 ويتم تغيير حجمهما ليناسب أبعاد الشاشة. | ‫`y`: عدد صحيح (من 0 إلى 999)، `x`: عدد صحيح (من 0 إلى 999) | `{"name": "click_at", "arguments": {"y": 300, "x": 500}}` |
| **hover\_at** | يحرك مؤشر الماوس إلى إحداثيات معيّنة على صفحة الويب. مفيدة لعرض القوائم الفرعية، ويستند المحوران x وy إلى شبكة 1000x1000. | `y`: عدد صحيح (0-999) `x`: عدد صحيح (0-999) | `{"name": "hover_at", "arguments": {"y": 150, "x": 250}}` |
| **type\_text\_at** | يكتب نصًا في إحداثيات معيّنة، ويتم تلقائيًا محو الحقل أولاً والضغط على مفتاح ENTER بعد الكتابة، ولكن يمكن إيقاف هذه الإعدادات. تستند الإحداثيات x وy إلى شبكة 1000x1000. | ‫`y`: عدد صحيح (0-999)، `x`: عدد صحيح (0-999)، `text`: سلسلة، `press_enter`: قيمة منطقية (اختيارية، القيمة التلقائية هي True)، `clear_before_typing`: قيمة منطقية (اختيارية، القيمة التلقائية هي True) | `{"name": "type_text_at", "arguments": {"y": 250, "x": 400, "text": "search query", "press_enter": false}}` |
| **key\_combination** | اضغط على مفاتيح لوحة المفاتيح أو مجموعات المفاتيح، مثل "Control+C" أو "Enter". مفيد لتنفيذ إجراءات (مثل إرسال نموذج باستخدام مفتاح Enter) أو عمليات الحافظة. | ‫`keys`: str (مثلاً 'enter' أو 'control+c'). | `{"name": "key_combination", "arguments": {"keys": "Control+A"}}` |
| **scroll\_document** | تؤدي إلى تمرير صفحة الويب بأكملها "للأعلى" أو "للأسفل" أو "لليسار" أو "لليمين". | `direction`: str ("up" أو "down" أو "left" أو "right") | `{"name": "scroll_document", "arguments": {"direction": "down"}}` |
| **scroll\_at** | تؤدي هذه السمة إلى تمرير عنصر أو مساحة معيّنة في الإحداثيات (x, y) في الاتجاه المحدّد بمقدار معيّن. تستند الإحداثيات والمقدار (القيمة التلقائية هي 800) إلى شبكة 1000x1000. | `y`: عدد صحيح (0-999)، `x`: عدد صحيح (0-999)، `direction`: سلسلة (up أو down أو left أو right)، `magnitude`: عدد صحيح (0-999، اختياري، القيمة التلقائية 800) | `{"name": "scroll_at", "arguments": {"y": 500, "x": 500, "direction": "down", "magnitude": 400}}` |
| **drag\_and\_drop** | يسحب عنصرًا من إحداثيات البداية (x, y) ويسقطه في إحداثيات الوجهة (destination\_x, destination\_y). تستند جميع الإحداثيات إلى شبكة 1000x1000. | `y`: عدد صحيح (0-999)، `x`: عدد صحيح (0-999)، `destination_y`: عدد صحيح (0-999)، `destination_x`: عدد صحيح (0-999) | `{"name": "drag_and_drop", "arguments": {"y": 100, "x": 100, "destination_y": 500, "destination_x": 500}}` |

## السلامة والأمان

### تأكيد قرار الأمان

استنادًا إلى الإجراء، قد يتضمّن ردّ النموذج أيضًا
`safety_decision` من نظام أمان داخلي يتحقّق من الإجراء المقترَح الذي سيتّخذه النموذج.

```
{
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "I have evaluated step 2. It seems Google detected unusual traffic and is asking me to verify I'm not a robot. I need to click the 'I'm not a robot' checkbox located near the top left (y=98, x=95)."
        }
      ]
    },
    {
      "type": "function_call",
      "name": "click_at",
      "arguments": {
        "x": 60,
        "y": 100,
        "safety_decision": {
          "explanation": "I have encountered a CAPTCHA challenge that requires interaction. I need you to complete the challenge by clicking the 'I'm not a robot' checkbox and any subsequent verification steps.",
          "decision": "require_confirmation"
        }
      }
    }
  ]
}
```

إذا كانت قيمة `safety_decision` هي `require_confirmation`، عليك أن تطلب من المستخدم النهائي تأكيد الإجراء قبل تنفيذه، إذ لا تسمح لك [بنود الخدمة](https://ai.google.dev/gemini-api/terms?hl=ar) بتجاوز طلبات التأكيد من المستخدم.

يطلب نموذج الرمز هذا من المستخدم النهائي تأكيد الإجراء قبل تنفيذه. وإذا لم يؤكّد المستخدم الإجراء، سيتم إنهاء الحلقة. أما إذا أكّده، فسيتم تنفيذ الإجراء وسيتم وضع علامة `True` على الحقل `safety_acknowledgement`.

### Python

```
import termcolor

def get_safety_confirmation(safety_decision):
    """Prompt user for confirmation when safety check is triggered."""
    termcolor.cprint("Safety service requires explicit confirmation!", color="red")
    print(safety_decision["explanation"])

    decision = ""
    while decision.lower() not in ("y", "n", "ye", "yes", "no"):
        decision = input("Do you wish to proceed? [Y]es/[N]o\n")

    if decision.lower() in ("n", "no"):
        return "TERMINATE"
    return "CONTINUE"

def execute_function_calls(interaction, page, screen_width, screen_height):

    # ... Extract function calls from response ...

    for function_call in function_calls:
        extra_fr_fields = {}

        # Check for safety decision
        if 'safety_decision' in function_call.arguments:
            decision = get_safety_confirmation(function_call.arguments['safety_decision'])
            if decision == "TERMINATE":
                print("Terminating agent loop")
                break
            extra_fr_fields["safety_acknowledgement"] = True # Safety acknowledgement

        # ... Execute function call and append to results ...
```

إذا أكّد المستخدم ذلك، عليك تضمين إقرار السلامة في `function_result`.

```
```python
function_responses.append({
    "type": "function_result",
    "name": name,
    "call_id": function_call.id,
    "result": [
        {
            "type": "text",
            "text": json.dumps({
                "url": current_url,
                "safety_acknowledgement": True,
                **extra_fr_fields
            })
        },
        {
            "type": "image",
            "data": base64.b64encode(screenshot_bytes).decode("utf-8"),
            "mime_type": "image/png"
        }
    ]
})
```
```

### أفضل الممارسات المتعلّقة بالأمان

&quot;استخدام الكمبيوتر&quot; هي أداة جديدة تنطوي على مخاطر جديدة يجب أن ينتبه إليها المطوّرون:

- **المحتوى غير الموثوق به وعمليات الخداع:** أثناء محاولة النموذج تحقيق هدف المستخدم، قد يعتمد على مصادر غير موثوق بها للحصول على المعلومات والتعليمات من الشاشة. على سبيل المثال، إذا كان هدف المستخدم هو شراء هاتف Pixel
  وواجه النموذج عملية احتيال بعنوان "احصل على هاتف Pixel مجانًا إذا أكملت استطلاعًا"،
  هناك احتمال أن يكمل النموذج الاستطلاع.
- **إجراءات غير مقصودة في بعض الأحيان:** قد يسيء النموذج فهم هدف المستخدم أو محتوى صفحة الويب، ما يؤدي إلى اتخاذ إجراءات غير صحيحة، مثل النقر على الزر الخطأ أو ملء النموذج الخطأ، ويمكن أن يؤدي ذلك إلى فشل المهام أو استخراج البيانات.
- **انتهاكات السياسة:** يمكن توجيه إمكانات واجهة برمجة التطبيقات، سواء عن قصد أو عن غير قصد، نحو أنشطة تنتهك سياسات Google ([سياسة الاستخدام المحظور للذكاء الاصطناعي التوليدي](https://policies.google.com/terms/generative-ai/use-policy?hl=ar) و[بنود الخدمة الإضافية لواجهة Gemini API](https://ai.google.dev/gemini-api/terms?hl=ar)). ويشمل ذلك الإجراءات التي قد تتداخل مع سلامة النظام أو تعرّض الأمان للخطر أو تتجاوز إجراءات الأمان أو تتحكّم في الأجهزة الطبية وما إلى ذلك.

لمعالجة هذه المخاطر، يمكنك اتّخاذ إجراءات السلامة التالية واتّباع أفضل الممارسات:

1. **المشاركة البشرية (HITL):**

   - **تنفيذ تأكيد المستخدم:** عندما تشير استجابة السلامة إلى
     `require_confirmation`، عليك تنفيذ تأكيد المستخدم قبل
     التنفيذ. راجِع [الإقرار بقرار السلامة](#safety-decisions) للاطّلاع على نموذج الرمز.
   - **تقديم تعليمات أمان مخصّصة:** بالإضافة إلى عمليات التحقّق المضمّنة التي تتطلّب تأكيدًا من المستخدم، يمكن للمطوّرين اختياريًا إضافة [تعليمات نظام](https://ai.google.dev/gemini-api/docs/text-generation?hl=ar#system-instructions) مخصّصة تفرض سياسات الأمان الخاصة بهم، إما لحظر إجراءات معيّنة يتّخذها النموذج أو لطلب تأكيد من المستخدم قبل أن يتّخذ النموذج إجراءات معيّنة لا يمكن التراجع عنها. في ما يلي مثال على تعليمات نظام الأمان المخصّصة التي يمكنك تضمينها عند التفاعل مع النموذج.

     **أمثلة على تعليمات السلامة:**

     اضبط قواعد الأمان المخصّصة كتعليمات نظام:

     ```
     ## **RULE 1: Seek User Confirmation (USER_CONFIRMATION)**

     This is your first and most important check. If the next required action falls
     into any of the following categories, you MUST stop immediately, and seek the
     user's explicit permission.

     **Procedure for Seeking Confirmation:**  * **For Consequential Actions:**
     Perform all preparatory steps (e.g., navigating, filling out forms, typing a
     message). You will ask for confirmation **AFTER** all necessary information is
     entered on the screen, but **BEFORE** you perform the final, irreversible action
     (e.g., before clicking "Send", "Submit", "Confirm Purchase", "Share").  * **For
     Prohibited Actions:** If the action is strictly forbidden (e.g., accepting legal
     terms, solving a CAPTCHA), you must first inform the user about the required
     action and ask for their confirmation to proceed.

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
     ```
2. **بيئة التنفيذ الآمنة:** شغِّل الوكيل في بيئة آمنة ومحمية
   للحدّ من تأثيره المحتمل (مثل جهاز افتراضي (VM) محمي، أو حاوية (مثل Docker)، أو ملف شخصي مخصّص للمتصفّح مع أذونات محدودة).
3. **تنقية الإدخالات:** يجب تنقية جميع النصوص التي ينشئها المستخدمون في الطلبات للحد من خطر التعليمات غير المقصودة أو هجمات حقن الطلبات. هذه الطبقة مفيدة للأمان، ولكنّها لا تحلّ محل بيئة التنفيذ الآمنة.
4. **ضوابط المحتوى:** استخدِم الضوابط و[واجهات برمجة التطبيقات الخاصة بأمان المحتوى](https://ai.google.dev/gemma/docs/shieldgemma?hl=ar) لتقييم مدخلات المستخدمين ومدخلات الأدوات ومخرجاتها، وردّات الوكيل من حيث الملاءمة، وعمليات حقن الطلبات، ورصد عمليات تجاوز القيود.
5. **القوائم المسموح بها والقوائم المحظورة:** استخدِم آليات فلترة للتحكّم في الأماكن التي يمكن للنموذج الانتقال إليها والإجراءات التي يمكنه اتّخاذها. تُعدّ القائمة المحظورة التي تتضمّن المواقع الإلكترونية المحظورة نقطة بداية جيدة، بينما تكون القائمة المسموح بها الأكثر تقييدًا أكثر أمانًا.
6. **إمكانية تتبّع البيانات وتسجيل البيانات:** احتفِظ بسجلات مفصّلة لتصحيح الأخطاء والتدقيق والاستجابة للحوادث. على العميل تسجيل الطلبات، ولقطات الشاشة، والإجراءات التي تقترحها النماذج (function\_call)، وردود الأمان، وجميع الإجراءات التي ينفّذها العميل في النهاية.
7. **إدارة البيئة:** تأكَّد من اتساق بيئة واجهة المستخدم الرسومية.
   قد تؤدي النوافذ المنبثقة أو الإشعارات أو التغييرات غير المتوقّعة في التنسيق إلى إرباك النموذج. ابدأ من حالة معروفة ونظيفة لكل مهمة جديدة إذا أمكن ذلك.

## إصدارات النموذج

يُرجى العِلم أنّ `gemini-3-flash-preview` يتضمّن ميزة مدمجة
للاستخدام على الكمبيوتر، ولن تحتاج إلى نموذج منفصل للوصول إلى الأداة.

| الموقع | الوصف |
| --- | --- |
| id\_cardرمز النموذج | **Gemini API**  `gemini-2.5-computer-use-preview-10-2025` |
| saveأنواع البيانات المتوافقة | **الإدخال**  صورة، نص  **الناتج**  نص |
| token\_autoحدود الرموز المميزة[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=ar) | **الحدّ الأقصى لعدد الرموز المميزة التي يمكن إدخالها**  128,000  **الحد الأقصى لعدد الرموز المميزة في الناتج**  64,000 |
| 123الإصدارات | يمكنك الاطّلاع على [أنماط إصدارات النماذج](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ar#model-versions) لمزيد من التفاصيل.  - معاينة: `gemini-2.5-computer-use-preview-10-2025` |
| calendar\_monthآخر تعديل | أكتوبر 2025 |

## الخطوات التالية

- جرِّب استخدام الكمبيوتر في [بيئة العرض التوضيحي Browserbase](http://gemini.browserbase.com).
- يمكنك الاطّلاع على [التنفيذ المرجعي](https://github.com/google/computer-use-preview) للحصول على مثال على الرمز.
- مزيد من المعلومات حول أدوات Gemini API الأخرى:
  - [استدعاء الدوال](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=ar)
  - [تحديد المصدر من خلال "بحث Google"](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=ar)

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-06-05 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-06-05 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
