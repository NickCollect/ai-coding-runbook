---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/computer-use?hl=th
fetched_at: 2026-08-03T04:41:35.366617+00:00
title: "\u0e01\u0e32\u0e23\u0e43\u0e0a\u0e49\u0e04\u0e2d\u0e21\u0e1e\u0e34\u0e27\u0e40\u0e15\u0e2d\u0e23\u0e4c \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

ตอนนี้ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) พร้อมให้บริการแก่ผู้ใช้ทั่วไปแล้ว เราขอแนะนำให้ใช้ API นี้เพื่อเข้าถึงฟีเจอร์และโมเดลล่าสุดทั้งหมด

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# การใช้คอมพิวเตอร์

เครื่องมือการใช้คอมพิวเตอร์ช่วยให้คุณสร้างเอเจนต์ควบคุมเบราว์เซอร์ อุปกรณ์เคลื่อนที่ และเดสก์ท็อป
ที่โต้ตอบและทำงานโดยอัตโนมัติได้ การใช้ภาพหน้าจอทำให้โมเดล "เห็น" หน้าจอคอมพิวเตอร์ และ "ดำเนินการ" โดยสร้างการดำเนินการ UI ที่เฉพาะเจาะจง เช่น การคลิกเมาส์
และการป้อนข้อมูลด้วยแป้นพิมพ์ คุณจะต้องใช้สภาพแวดล้อมการดำเนินการฝั่งไคลเอ็นต์เพื่อรับและดำเนินการกับการดำเนินการด้านการใช้งานคอมพิวเตอร์
เช่นเดียวกับการเรียกใช้ฟังก์ชัน

ดูรายการโมเดลที่รองรับได้ที่[เวอร์ชันโมเดล](#model-versions) โมเดล Gemini 3.x รองรับความสามารถขั้นสูงหลายอย่าง ได้แก่

- **การรองรับหลายสภาพแวดล้อม:** สร้างเอเจนต์สำหรับสภาพแวดล้อมของ[เบราว์เซอร์ อุปกรณ์เคลื่อนที่ และเดสก์ท็อป](#supported-environments)
- **การดำเนินการที่ปรับปรุงแล้วด้วยเจตนา:** การดำเนินการมีฟิลด์ `intent` ที่อธิบายเหตุผลของโมเดลในแต่ละขั้นตอน
- **นโยบายความปลอดภัยที่กำหนดค่าได้:** ปรับ[พฤติกรรมด้านความปลอดภัย](#safety-policies)ให้เหมาะสมด้วยหมวดหมู่นโยบายและการลบล้างที่มีอยู่
- **การตรวจหาการแทรกพรอมต์:** เลือกใช้[การสแกนภาพหน้าจอ](#prompt-injection)เพื่อตรวจหาคำสั่งที่เป็นอันตรายที่ซ่อนอยู่

การใช้คอมพิวเตอร์ช่วยให้คุณสร้างเอเจนต์ที่ทำสิ่งต่อไปนี้ได้

- ป้อนข้อมูลซ้ำๆ หรือกรอกแบบฟอร์มในเว็บไซต์โดยอัตโนมัติ
- ทำการทดสอบเว็บแอปพลิเคชันและโฟลว์ของผู้ใช้โดยอัตโนมัติ
- ทําการวิจัยในเว็บไซต์ต่างๆ (เช่น รวบรวมข้อมูลผลิตภัณฑ์ ราคา และรีวิวจากเว็บไซต์อีคอมเมิร์ซเพื่อประกอบการตัดสินใจซื้อ)

ต่อไปนี้คือตัวอย่างการเปิดใช้เครื่องมือการใช้คอมพิวเตอร์ในรูปแบบที่เรียบง่ายที่สุด

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.6-flash",
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
  model: 'gemini-3.6-flash',
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

## การทำงานของการใช้คอมพิวเตอร์

หากต้องการสร้างเอเจนต์ด้วยโมเดลการใช้คอมพิวเตอร์ คุณต้องตั้งค่า
ลูปต่อเนื่องระหว่างแอปพลิเคชันกับ API โค้ดของคุณจะทำสิ่งต่อไปนี้ในแต่ละขั้นตอน

1. [**ส่งคำขอไปยังโมเดล**](#send-request)
   - แอปพลิเคชันของคุณจะส่งคำขอ API ที่มีเครื่องมือการใช้งานคอมพิวเตอร์
     การตั้งค่าการกำหนดค่า (เช่น สภาพแวดล้อมเป้าหมาย) พรอมต์ของผู้ใช้
     และภาพหน้าจอของหน้าจอปัจจุบัน
2. [**รับคำตอบของโมเดล**](#model-response)
   - โมเดลจะวิเคราะห์หน้าจอและพรอมต์ แล้วส่งคำตอบ
     ซึ่งมี`function_call`ที่แนะนำซึ่งแสดงถึงการดำเนินการใน UI (เช่น
     การคลิก การเลื่อน หรือการกดแป้น)
   - สำหรับ**โมเดล Gemini 3.x** คำตอบจะมีเหตุผล `intent`
     ที่อธิบายว่าทำไมโมเดลจึงเลือกการดำเนินการนั้น
   - การตอบกลับอาจรวมถึง`safety_decision`จากระบบความปลอดภัยภายใน
     ที่จัดประเภทการดำเนินการเป็นปกติ/อนุญาต
     `require_confirmation` (ต้องได้รับการอนุมัติจากผู้ใช้) หรือถูกบล็อก
3. [**ดำเนินการตามการกระทำที่ได้รับ**](#execute-actions)
   - หากได้รับอนุญาตให้ดำเนินการ (หรือผู้ใช้ยืนยัน) โค้ดฝั่งไคลเอ็นต์ จะแยกวิเคราะห์ `function_call` ปรับขนาดพิกัดที่ปรับให้เป็นมาตรฐานให้ตรงกับ วิวพอร์ต และดำเนินการในสภาพแวดล้อมเป้าหมายโดยใช้ เครื่องมือการทำงานอัตโนมัติ (เช่น Playwright) หากการดำเนินการถูกบล็อก ไคลเอ็นต์ควรหยุดการดำเนินการหรือจัดการการหยุดชะงัก
4. [**บันทึกสถานะสภาพแวดล้อมใหม่**](#capture-state)
   - หลังจากดำเนินการเสร็จแล้ว แอปพลิเคชันจะจับภาพหน้าจอใหม่
     และส่งกลับไปยังโมเดลใน `function_result` เพื่อ
     ขอขั้นตอนถัดไป

จากนั้นกระบวนการนี้จะทำซ้ำจากขั้นตอนที่ 2 โดยจะขอการดำเนินการถัดไปจากโมเดลอย่างต่อเนื่องจนกว่าจะทำงานเสร็จหรือสิ้นสุด

![ภาพรวมการใช้คอมพิวเตอร์](https://ai.google.dev/static/gemini-api/docs/images/computer_use.png?hl=th)

## วิธีใช้การใช้คอมพิวเตอร์

ก่อนที่จะสร้างด้วยเครื่องมือการใช้งานคอมพิวเตอร์ คุณจะต้องตั้งค่าสิ่งต่อไปนี้

- **สภาพแวดล้อมการดำเนินการที่ปลอดภัย:** เรียกใช้เอเจนต์ใน VM หรือ
  คอนเทนเนอร์แซนด์บ็อกซ์เพื่อแยกเอเจนต์ออกจากระบบโฮสต์และจำกัดผลกระทบที่อาจเกิดขึ้น
  [การติดตั้งใช้งานอ้างอิง](https://github.com/google/computer-use-preview/)
  มีแซนด์บ็อกซ์ที่ใช้ Docker พร้อมใช้งานซึ่งคุณใช้เป็นจุดเริ่มต้นได้
- **ตัวแฮนเดิลการดำเนินการฝั่งไคลเอ็นต์:** ใช้ตรรกะฝั่งไคลเอ็นต์เพื่อดำเนินการกับพิกัด พิมพ์ข้อความ และถ่ายภาพหน้าจอ

ตัวอย่างด้านล่างใช้เว็บเบราว์เซอร์เป็นสภาพแวดล้อมการดำเนินการและ
[Playwright](https://playwright.dev/) เป็นตัวแฮนเดิลฝั่งไคลเอ็นต์

### 0. ตั้งค่า Playwright

ก่อนอื่น ให้ติดตั้งแพ็กเกจที่จำเป็น

```
pip install google-genai playwright
playwright install chromium
```

จากนั้นเริ่มต้นอินสแตนซ์เบราว์เซอร์ Playwright เพื่อใช้ในการดำเนินการ

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

### 1. ส่งคำขอไปยังโมเดล

เริ่มต้นไลบรารีของไคลเอ็นต์และกำหนดค่าเครื่องมือการใช้งานคอมพิวเตอร์ โปรดทราบว่าไม่จำเป็นต้องระบุขนาดการแสดงผลเมื่อส่งคำขอ เนื่องจากโมเดลจะคาดการณ์พิกัดพิกเซลที่ปรับขนาดตามความสูงและความกว้างของหน้าจอ

### Gemini 3.x

### Python

ใช้ `google-genai` Python SDK (เวอร์ชัน `2.7.0` ขึ้นไป) เพื่อกำหนดค่าคำขอที่กำหนดเป้าหมายไปยังสภาพแวดล้อมของเบราว์เซอร์

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
    model="gemini-3.6-flash",
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

ใช้ `@google/genai` Node.js SDK เพื่อกำหนดค่าคำขอที่กำหนดเป้าหมายไปยังสภาพแวดล้อมของเบราว์เซอร์

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI();

const response = await ai.models.generateContent({
  model: 'gemini-3.6-flash',
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

ใช้ curl เพื่อส่งคำขอ

```
curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key=$GEMINI_API_KEY" \
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

### Gemini 2.5 (เดิม)

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

### 2. รับคำตอบของโมเดล

โมเดลการตอบกลับแนะนำการเรียกใช้ฟังก์ชัน สำหรับ**โมเดล Gemini 3.x** คำตอบ
จะมีความตั้งใจในการให้เหตุผลที่ปรับแต่งแล้วพร้อมกับพิกัด
ต่อไปนี้เป็นตัวอย่างของการตอบกลับทั้ง 2 แบบ

### Gemini 3.x

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

### Gemini 2.5 (เดิม)

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

### 3. ดำเนินการตามการดำเนินการที่ได้รับ

โค้ดของแอปพลิเคชันของคุณต้องแยกวิเคราะห์การตอบกลับของโมเดล ดำเนินการ และรวบรวมผลลัพธ์

โค้ดด้านล่างจะจัดการทั้งคำสั่งเครื่องมือเดิม (`click_at`, `type_text_at`) และคำสั่งที่ปรับปรุงใหม่ (`click`, `type`)

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

### 4. บันทึกสถานะสภาพแวดล้อมใหม่

จับภาพการแสดงหน้าจอและส่งกลับไปยังโมเดล

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

เมื่อกำหนดวิธีบันทึกและจัดรูปแบบสถานะสภาพแวดล้อมแล้ว คุณจะรวมขั้นตอนทั้งหมดเหล่านี้ไว้ในลูปการดำเนินการต่อเนื่องได้

## สร้างลูปของ Agent

หากต้องการเปิดใช้การโต้ตอบแบบหลายขั้นตอน ให้รวม 4 ขั้นตอนจากส่วน[วิธีใช้งานคอมพิวเตอร์](#implement-computer-use)เป็นลูปเดียว ลูปนี้จะขอให้ดำเนินการและป้อนผลลัพธ์กลับไปยังโมเดลต่อไปจนกว่างานจะเสร็จสมบูรณ์

อย่าลืมจัดการประวัติการสนทนาอย่างถูกต้องโดยการต่อท้ายทั้งคำตอบของโมเดลและคำตอบของฟังก์ชันลงในประวัติในแต่ละขั้นตอน

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
            model='gemini-3.6-flash',
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
            model: 'gemini-3.6-flash',
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

## สภาพแวดล้อมที่รองรับ (Gemini 3.x)

โมเดล Gemini 3.x รองรับสภาพแวดล้อม 3 แบบที่ระบุไว้ในการกำหนดค่า `computer_use` ดังนี้

### สภาพแวดล้อมของเบราว์เซอร์ (`ENVIRONMENT_BROWSER`)

การดำเนินการของ Action ในเครื่องมือเบราว์เซอร์

| ชื่อคำสั่ง | คำอธิบาย | อาร์กิวเมนต์ (ในการเรียกใช้ฟังก์ชัน) |
| --- | --- | --- |
| **คลิก** | คลิกซ้ายที่พิกัด | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **double\_click** | ดับเบิลคลิกที่พิกัด | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **triple\_click** | คลิก 3 ครั้งที่พิกัด | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **middle\_click** | คลิกตรงกลางที่พิกัด | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **right\_click** | คลิกขวาที่พิกัด | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **mouse\_down** | กดปุ่มเมาส์ค้างไว้ที่พิกัด | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **mouse\_up** | ปล่อยปุ่มเมาส์ที่พิกัด | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **ย้าย** | ย้ายเคอร์เซอร์ไปยังตำแหน่งที่ระบุ | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **ประเภท** | พิมพ์ข้อความ | `text`: str `press_enter`: bool (ไม่บังคับ ค่าเริ่มต้น `false`) `intent`: str |
| **drag\_and\_drop** | ลากรายการจากพิกัดเริ่มต้นไปยังพิกัดสิ้นสุด | `start_y`: int (0-999) `start_x`: int (0-999) `end_y`: int (0-999) `end_x`: int (0-999) `intent`: str |
| **รอ** | หยุดการดำเนินการชั่วคราวตามจำนวนวินาทีที่ระบุ | `seconds`: int (ไม่บังคับ ค่าเริ่มต้น `1`) `intent`: str |
| **press\_key** | กดแป้นที่ระบุแล้วปล่อย | `key`: str `intent`: str |
| **key\_down** | กดแป้นที่ระบุค้างไว้ | `key`: str `intent`: str |
| **key\_up** | ปล่อยคีย์ที่ระบุ | `key`: str `intent`: str |
| **ฮอตคีย์** | กดชุดแป้นที่ระบุ | `keys`: `List[str]` `intent`: `str` |
| **take\_screenshot** | แสดงผลภาพหน้าจอปัจจุบัน | `intent`: str |
| **เลื่อน** | เลื่อนขึ้น ลง ซ้าย หรือขวาที่พิกัดตามระยะห่างของพิกเซล | `y`: int (0-999) `x`: int (0-999) `direction`: str (`"up"`, `"down"`, `"left"`, `"right"`) `magnitude_in_pixels`: int (0-999, ไม่บังคับ, ค่าเริ่มต้น `300`) `intent`: str |
| **go\_back** | กลับไปยังหน้าเว็บก่อนหน้าในประวัติการท่องเว็บ | `intent`: str |
| **navigate** | ไปยัง URL ที่ระบุโดยตรง | `url`: str `intent`: str |
| **go\_forward** | ไปยังหน้าเว็บถัดไปในประวัติการท่องเว็บ | `intent`: str |

### สภาพแวดล้อมบนอุปกรณ์เคลื่อนที่ (`ENVIRONMENT_MOBILE`)

การดำเนินการในสภาพแวดล้อมที่เพิ่มประสิทธิภาพสำหรับ Android

| ชื่อคำสั่ง | คำอธิบาย | อาร์กิวเมนต์ (ในการเรียกใช้ฟังก์ชัน) |
| --- | --- | --- |
| **open\_app** | เปิดแอปพลิเคชันตามชื่อ | `app_name`: str `intent`: str |
| **คลิก** | คลิกซ้ายที่พิกัด | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **list\_apps** | แสดงรายการแอปพลิเคชันที่พร้อมใช้งานในอุปกรณ์ โดยจะแสดงชื่อและชื่อแพ็กเกจของแอปพลิเคชัน | `intent`: str |
| **รอ** | หยุดการดำเนินการชั่วคราวตามจำนวนวินาทีที่ระบุ | `seconds`: int (ไม่บังคับ ค่าเริ่มต้น `1`) `intent`: str |
| **go\_back** | กลับไปยังหน้าจอก่อนหน้าหรือหน้าเว็บก่อนหน้า | `intent`: str |
| **ประเภท** | พิมพ์ข้อความ | `text`: str `press_enter`: bool (ไม่บังคับ ค่าเริ่มต้น `false`) `intent`: str |
| **drag\_and\_drop** | ลากรายการจากพิกัดเริ่มต้นไปยังพิกัดสิ้นสุด | `start_y`: int (0-999) `start_x`: int (0-999) `end_y`: int (0-999) `end_x`: int (0-999) `intent`: str |
| **long\_press** | กดค้างที่พิกัดบนหน้าจอ | `y`: int (0-999) `x`: int (0-999) `seconds`: int (ไม่บังคับ ค่าเริ่มต้น `2`) `intent`: str |
| **press\_key** | กดแป้นที่ระบุแล้วปล่อย | `key`: str `intent`: str |
| **take\_screenshot** | แสดงผลภาพหน้าจอปัจจุบัน | `intent`: str |

### สภาพแวดล้อมของเดสก์ท็อป (`ENVIRONMENT_DESKTOP`)

คำสั่งเคอร์เซอร์ระดับระบบปฏิบัติการของสภาพแวดล้อมเดสก์ท็อป

| ชื่อคำสั่ง | คำอธิบาย | อาร์กิวเมนต์ (ในการเรียกใช้ฟังก์ชัน) |
| --- | --- | --- |
| **คลิก** | คลิกซ้ายที่พิกัด | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **double\_click** | ดับเบิลคลิกที่พิกัด | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **triple\_click** | คลิก 3 ครั้งที่พิกัด | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **middle\_click** | คลิกตรงกลางที่พิกัด | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **right\_click** | คลิกขวาที่พิกัด | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **mouse\_down** | กดปุ่มเมาส์ค้างไว้ที่พิกัด | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **mouse\_up** | ปล่อยปุ่มเมาส์ที่พิกัด | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **ย้าย** | ย้ายเคอร์เซอร์ไปยังตำแหน่งที่ระบุ | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **ประเภท** | พิมพ์ข้อความ | `text`: str `press_enter`: bool (ไม่บังคับ ค่าเริ่มต้น `false`) `intent`: str |
| **drag\_and\_drop** | ลากรายการจากพิกัดเริ่มต้นไปยังพิกัดสิ้นสุด | `start_y`: int (0-999) `start_x`: int (0-999) `end_y`: int (0-999) `end_x`: int (0-999) `intent`: str |
| **รอ** | หยุดการดำเนินการชั่วคราวตามจำนวนวินาทีที่ระบุ | `seconds`: int (ไม่บังคับ ค่าเริ่มต้น `1`) `intent`: str |
| **press\_key** | กดแป้นที่ระบุแล้วปล่อย | `key`: str `intent`: str |
| **key\_down** | กดแป้นที่ระบุค้างไว้ | `key`: str `intent`: str |
| **key\_up** | ปล่อยคีย์ที่ระบุ | `key`: str `intent`: str |
| **ฮอตคีย์** | กดชุดแป้นที่ระบุ | `keys`: `List[str]` `intent`: `str` |
| **take\_screenshot** | แสดงผลภาพหน้าจอปัจจุบัน | `intent`: str |
| **เลื่อน** | เลื่อนขึ้น ลง ซ้าย หรือขวาที่พิกัดตามระยะห่างของพิกเซล | `y`: int (0-999) `x`: int (0-999) `direction`: str (`"up"`, `"down"`, `"left"`, `"right"`) `magnitude_in_pixels`: int (0-999, ไม่บังคับ, ค่าเริ่มต้น `300`) `intent`: str |

## การดำเนินการใน UI ที่รองรับเวอร์ชันเดิม (Gemini 2.5)

สำหรับโมเดลเดิม (`gemini-2.5-computer-use-preview-10-2025`) ระบบจะรองรับการดำเนินการต่อไปนี้

| ชื่อคำสั่ง | คำอธิบาย | อาร์กิวเมนต์ (ในการเรียกใช้ฟังก์ชัน) | ตัวอย่างการเรียกใช้ฟังก์ชัน |
| --- | --- | --- | --- |
| **open\_web\_browser** | เปิดเว็บเบราว์เซอร์ | ไม่มี | `{"name": "open_web_browser", "args": {}}` |
| **wait\_5\_seconds** | หยุดการดำเนินการชั่วคราวเป็นเวลา 5 วินาที | ไม่มี | `{"name": "wait_5_seconds", "args": {}}` |
| **go\_back** | ไปยังหน้าก่อนหน้าในประวัติการเข้าชม | ไม่มี | `{"name": "go_back", "args": {}}` |
| **go\_forward** | ไปยังหน้าถัดไปในประวัติการเข้าชม | ไม่มี | `{"name": "go_forward", "args": {}}` |
| **search** | ไปยังเครื่องมือค้นหาเริ่มต้น | ไม่มี | `{"name": "search", "args": {}}` |
| **navigate** | นำทางเบราว์เซอร์ไปยัง URL ที่ระบุโดยตรง | `url`: str | `{"name": "navigate", "args": {"url": "https://www.wikipedia.org"}}` |
| **click\_at** | คลิกที่พิกัดที่เฉพาะเจาะจง | `y`: int (0-999), `x`: int (0-999) | `{"name": "click_at", "args": {"y": 300, "x": 500}}` |
| **hover\_at** | วางเมาส์ที่พิกัดที่เฉพาะเจาะจง | `y`: int (0-999), `x`: int (0-999) | `{"name": "hover_at", "args": {"y": 150, "x": 250}}` |
| **type\_text\_at** | พิมพ์ข้อความที่พิกัด | `y`: int (0-999), `x`: int (0-999), `text`: str, `press_enter`: bool (ไม่บังคับ ค่าเริ่มต้นคือ True), `clear_before_typing`: bool (ไม่บังคับ ค่าเริ่มต้นคือ True) | `{"name": "type_text_at", "args": {"y": 250, "x": 400, "text": "search", "press_enter": false}}` |
| **key\_combination** | กดแป้นหรือชุดแป้น | `keys`: str | `{"name": "key_combination", "args": {"keys": "Control+A"}}` |
| **scroll\_document** | เลื่อนทั้งหน้าเว็บ | `direction`: str | `{"name": "scroll_document", "args": {"direction": "down"}}` |
| **scroll\_at** | เลื่อนที่พิกัด (x,y) | `y`: int, `x`: int, `direction`: str, `magnitude`: int (ไม่บังคับ ค่าเริ่มต้นคือ 800) | `{"name": "scroll_at", "args": {"y": 500, "x": 500, "direction": "down"}}` |
| **drag\_and\_drop** | ลากระหว่างพิกัด 2 จุด | `y`: int, `x`: int, `destination_y`: int, `destination_x`: int | `{"name": "drag_and_drop", "args": {"y": 100, "destination_y": 500, "destination_x": 500, "x": 100}}` |

## ฟังก์ชันที่กำหนดเองซึ่งผู้ใช้กำหนด

คุณขยายฟังก์ชันการทำงานของโมเดลได้โดยรวมฟังก์ชันที่กำหนดเองโดยผู้ใช้ เช่น ในสถานการณ์ที่มีการใช้คนในกระบวนการ (HITL) คุณสามารถยกเว้นการดำเนินการเริ่มต้นที่กำหนดไว้ล่วงหน้าและลงทะเบียนการดำเนินการที่กำหนดเองได้

#### เครื่องมือที่กำหนดเองของ Gemini 3.x

### Python

ยกเว้นการดำเนินการในเบราว์เซอร์ที่กำหนดไว้ล่วงหน้ามาตรฐาน (เช่น `click`) และลงทะเบียนเครื่องมือ `yield_to_user` ที่กำหนดเอง

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
    model="gemini-3.6-flash",
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

#### เครื่องมือที่กำหนดเองของ Gemini 2.5 (เดิม)

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

## การจัดการระดับการคิด (Gemini 3.x)

สำหรับเอเจนต์ที่ใช้คอมพิวเตอร์ คุณสามารถกำหนดค่าระดับการคิดต่างๆ เพื่อปรับสมดุลคุณภาพการดำเนินการและความเร็วในการดำเนินการ โดยทั่วไปแล้ว ระดับการคิดที่ต่ำกว่าจะสร้างสมดุลที่ดีสำหรับงานอัตโนมัติมาตรฐาน

## ความปลอดภัย

### การกำหนดค่านโยบายความปลอดภัย (Gemini 3.x)

โมเดล Gemini 3.x มีหมวดหมู่บริการด้านความปลอดภัยในตัวที่จะพิจารณาโดยอัตโนมัติว่าต้องมีการยืนยันจากผู้ใช้หรือไม่

| หมวดหมู่นโยบายด้านความปลอดภัย | คำอธิบาย |
| --- | --- |
| `FINANCIAL_TRANSACTIONS` | บล็อกหรือทริกเกอร์การยืนยันสำหรับการดำเนินการที่เกี่ยวข้องกับการชำระเงิน การชำระเงินที่ร้านค้าปลีก หรือสินค้าควบคุม |
| `SENSITIVE_DATA_MODIFICATION` | ปกป้องบันทึกด้านสุขภาพ การเงิน หรือของรัฐบาลจากการแก้ไขที่ไม่ได้รับอนุญาต |
| `COMMUNICATION_TOOL` | จำกัดไม่ให้ตัวแทนส่งอีเมล ข้อความแชท หรือฉบับร่างโดยอัตโนมัติ |
| `ACCOUNT_CREATION` | จำกัดไม่ให้เอเจนต์ลงทะเบียนบัญชีใหม่บนเว็บไซต์โดยอัตโนมัติ |
| `DATA_MODIFICATION` | ควบคุมการแก้ไขระบบไฟล์โดยรวม การแชร์ข้อมูล และการลบข้อมูลที่จัดเก็บ |
| `USER_CONSENT_MANAGEMENT` | ต้องมีการควบคุมของผู้ใช้สำหรับแบนเนอร์แสดงความยินยอมในการใช้คุกกี้และข้อความแจ้งเกี่ยวกับความเป็นส่วนตัว |
| `LEGAL_TERMS_AND_AGREEMENTS` | ป้องกันไม่ให้โมเดลยอมรับข้อกำหนดในการให้บริการหรือสัญญาที่มีผลผูกพันตามกฎหมายโดยอัตโนมัติ |

#### การลบล้างความปลอดภัย

คุณสามารถลบล้างนโยบายบางอย่างได้โดยส่งการลบล้างดังนี้

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.6-flash",
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
  model: 'gemini-3.6-flash',
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

### การตรวจหาการแทรกพรอมต์ (Gemini 3.x)

กลไกความปลอดภัยแบบเลือกใช้ที่จะสแกนพิกเซลของภาพหน้าจอเพื่อหาคำสั่งพรอมต์ที่เป็นการโจมตีแบบซ่อนเร้น (เช่น "ไม่สนใจคำสั่งก่อนหน้า") และบล็อกการดำเนินการเมื่อ
ตรวจพบ

### รับทราบการตัดสินใจด้านความปลอดภัย

การตอบกลับอาจมีพารามิเตอร์ `safety_decision` ในอาร์กิวเมนต์การเรียกใช้ฟังก์ชัน

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

หาก `safety_decision` เป็น `require_confirmation` ให้แจ้งผู้ใช้ปลายทาง หากผู้ใช้ยืนยัน ให้ตั้งค่า `safety_acknowledgement` ใน `FunctionResponse`

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

### แนวทางปฏิบัติแนะนำด้านความปลอดภัย

การใช้คอมพิวเตอร์มีความเสี่ยงด้านความปลอดภัยและการปฏิบัติงานที่ไม่เหมือนใคร เนื่องจากโมเดลที่ทํางานในนามของผู้ใช้อาจพบเนื้อหาที่ไม่น่าเชื่อถือบนหน้าจอหรือทําผิดพลาดในการดําเนินการ ใช้แนวทางปฏิบัติแนะนำต่อไปนี้เพื่อปกป้องข้อมูลและระบบของผู้ใช้

1. **การมีมนุษย์เป็นผู้ตรวจสอบ (HITL):**

   - **บังคับใช้การยืนยันผู้ใช้:** เมื่อการตอบกลับด้านความปลอดภัยระบุ
     `require_confirmation` (หรือการตัดสินด้านความปลอดภัยเดิมกำหนดไว้) ให้แจ้งให้ผู้ใช้ขออนุมัติ
   - **ระบุวิธีการด้านความปลอดภัยที่กำหนดเอง:** ใช้คำสั่งของระบบที่กำหนดเองเพื่อกำหนดและบังคับใช้ขอบเขตด้านความปลอดภัยของคุณเอง เช่น

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
         model="gemini-3.6-flash",
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
       model: 'gemini-3.6-flash',
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
2. **สภาพแวดล้อมการดำเนินการที่ปลอดภัย:** เรียกใช้เอเจนต์ในสภาพแวดล้อมแซนด์บ็อกซ์ที่ปลอดภัย
   เพื่อจำกัดผลกระทบที่อาจเกิดขึ้น ซึ่งอาจเป็นเครื่องเสมือน (VM) แบบแซนด์บ็อกซ์ คอนเทนเนอร์ (เช่น Docker) หรือโปรไฟล์เบราว์เซอร์เฉพาะที่มีสิทธิ์จำกัด ดูคำแนะนำในการตั้งค่าแซนด์บ็อกซ์โดยใช้ Docker ได้ที่[การใช้งานอ้างอิงของ GitHub](https://github.com/google/computer-use-preview/)
3. **การล้างข้อมูลอินพุต:** ล้างข้อมูลข้อความทั้งหมดที่ผู้ใช้สร้างขึ้นในพรอมต์เพื่อลดความเสี่ยงของวิธีการที่ไม่ต้องการหรือการแทรกพรอมต์ ซึ่งเป็น
   การรักษาความปลอดภัยที่มีประโยชน์ แต่ไม่ใช่การแทนที่สภาพแวดล้อมการดำเนินการที่ปลอดภัย
4. **แนวทางป้องกันเนื้อหา:** ใช้ API แนวทางป้องกันและ API ความปลอดภัยของเนื้อหาเพื่อประเมิน
   อินพุตของผู้ใช้ อินพุตและเอาต์พุตของเครื่องมือ รวมถึงการตอบกลับของเอเจนต์ว่าเหมาะสมหรือไม่
   การแทรกพรอมต์ และการตรวจหาการหลบเลี่ยง
5. **รายการที่อนุญาตและรายการที่บล็อก:** ใช้กลไกการกรองเพื่อควบคุม
   ตำแหน่งที่โมเดลสามารถไปยังได้และสิ่งที่โมเดลทำได้ จุดเริ่มต้นที่ดีคือรายการที่บล็อกเว็บไซต์ที่ห้าม
   ขณะที่รายการที่อนุญาตที่จำกัดมากขึ้นจะปลอดภัยยิ่งกว่า
6. **ความสามารถในการสังเกตและการบันทึก:** จัดเก็บบันทึกโดยละเอียดสำหรับการแก้ไขข้อบกพร่อง การตรวจสอบ และการตอบสนองต่อเหตุการณ์ ลูกค้าควรบันทึกพรอมต์
   ภาพหน้าจอ การดำเนินการที่โมเดลแนะนำ (`function_call`) การตอบกลับด้านความปลอดภัย และ
   การดำเนินการทั้งหมดที่ไคลเอ็นต์ดำเนินการในท้ายที่สุด
7. **การจัดการสภาพแวดล้อม:** ตรวจสอบว่าสภาพแวดล้อม GUI สอดคล้องกัน
   ป๊อปอัป การแจ้งเตือน หรือการเปลี่ยนแปลงเลย์เอาต์ที่ไม่คาดคิดอาจทำให้โมเดลสับสน
   เริ่มต้นจากสถานะที่ทราบและสะอาดสำหรับงานใหม่แต่ละงานหากเป็นไปได้

## เวอร์ชันของโมเดล

คุณใช้การใช้คอมพิวเตอร์กับรุ่นต่อไปนี้ได้

- [**Gemini 3.6 Flash**](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=th) (`gemini-3.6-flash`): โมเดลที่แนะนำสำหรับการใช้งานใน
  คอมพิวเตอร์ ซึ่งมีฟีเจอร์การดำเนินการที่ปรับปรุงแล้วพร้อมเจตนา รองรับ
  สภาพแวดล้อมของเบราว์เซอร์ อุปกรณ์เคลื่อนที่ และเดสก์ท็อป นโยบายความปลอดภัยที่กำหนดค่าได้ และ
  การตรวจหาการแทรกพรอมต์
- [**Gemini 3.5 Flash-Lite**](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=th) (`gemini-3.5-flash-lite`): โมเดลที่มีเวลาในการตอบสนองต่ำและคุ้มค่าที่รองรับการใช้งานคอมพิวเตอร์
- [**Gemini 3.5 Flash**](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=th) (`gemini-3.5-flash`): โมเดลเวอร์ชันเสถียรก่อนหน้าซึ่งรองรับ
  การใช้งานคอมพิวเตอร์
- [**รุ่นตัวอย่าง Gemini 3 Flash**](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=th) (`gemini-3-flash-preview`): โมเดลตัวอย่าง
  ที่รองรับการใช้งานคอมพิวเตอร์
- [**Gemini 2.5 (ตัวอย่างเวอร์ชันเดิม)**](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-computer-use-preview-10-2025?hl=th) (`gemini-2.5-computer-use-preview-10-2025`): โมเดลตัวอย่างเวอร์ชันเดิมที่ได้รับการเพิ่มประสิทธิภาพสำหรับการใช้งานคอมพิวเตอร์ที่ใช้เบราว์เซอร์

## ขั้นตอนถัดไป

- ทดลองใช้คอมพิวเตอร์ใน[สภาพแวดล้อมการสาธิตของ Browserbase](http://gemini.browserbase.com)
- ดูโค้ดตัวอย่างได้ที่[การติดตั้งใช้งานอ้างอิง](https://github.com/google/computer-use-preview)
- ดูข้อมูลเกี่ยวกับเครื่องมืออื่นๆ ของ Gemini API
  - [การเรียกใช้ฟังก์ชัน](https://ai.google.dev/gemini-api/docs/function-calling?hl=th)
  - [การเชื่อมต่อแหล่งข้อมูลกับ Google Search](https://ai.google.dev/gemini-api/docs/grounding?hl=th)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-07-30 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-07-30 UTC"],[],[]]
