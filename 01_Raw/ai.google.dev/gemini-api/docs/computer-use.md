---
source_url: https://ai.google.dev/gemini-api/docs/computer-use?hl=th
fetched_at: 2026-05-25T05:19:17.542122+00:00
title: "Gemini generateContent API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=th) พร้อมให้บริการในเวอร์ชันพรีวิวแล้วตอนนี้ โดยมีฟีเจอร์การวางแผนร่วมกัน การแสดงภาพข้อมูล การรองรับ MCP และอื่นๆ

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [generateContent API](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# การใช้คอมพิวเตอร์

การใช้คอมพิวเตอร์ช่วยให้คุณสร้างเอเจนต์ควบคุมเบราว์เซอร์ที่โต้ตอบและทำงานโดยอัตโนมัติได้ การใช้ภาพหน้าจอช่วยให้โมเดล "เห็น" หน้าจอคอมพิวเตอร์และ "ดำเนินการ" โดยสร้างการดำเนินการ UI ที่เฉพาะเจาะจง เช่น การคลิกเมาส์และอินพุตจากแป้นพิมพ์ คุณต้องเขียนโค้ดของแอปพลิเคชันฝั่งไคลเอ็นต์เพื่อรับและดำเนินการกับการดำเนินการเกี่ยวกับการใช้คอมพิวเตอร์ ซึ่งคล้ายกับการเรียกใช้ฟังก์ชัน

การใช้คอมพิวเตอร์ช่วยให้คุณสร้างเอเจนต์ที่ทำสิ่งต่อไปนี้ได้

- ทำให้การกรอกข้อมูลซ้ำๆ หรือการกรอกแบบฟอร์มในเว็บไซต์เป็นแบบอัตโนมัติ
- ทำการทดสอบเว็บแอปพลิเคชันและโฟลว์ของผู้ใช้โดยอัตโนมัติ
- ทําการวิจัยในเว็บไซต์ต่างๆ (เช่น รวบรวมข้อมูลผลิตภัณฑ์ ราคา และรีวิวจากเว็บไซต์อีคอมเมิร์ซเพื่อประกอบการตัดสินใจซื้อ)

วิธีที่ง่ายที่สุดในการทดสอบความสามารถในการใช้งานคอมพิวเตอร์คือการทดสอบผ่าน[การติดตั้งใช้งานอ้างอิง](https://github.com/google/computer-use-preview/)หรือ[สภาพแวดล้อมเดโมของ Browserbase](http://gemini.browserbase.com)

## การทำงานของการใช้คอมพิวเตอร์

หากต้องการสร้างเอเจนต์ควบคุมเบราว์เซอร์ด้วยโมเดลการใช้คอมพิวเตอร์ ให้ใช้ลูปเอเจนต์ที่ทำสิ่งต่อไปนี้

1. [**ส่งคำขอไปยังโมเดล**](#send-request)

   - เพิ่มเครื่องมือการใช้คอมพิวเตอร์และฟังก์ชันที่ผู้ใช้กำหนดเองหรือฟังก์ชันที่ยกเว้น (ไม่บังคับ) ลงในคำขอ API
   - แจ้งโมเดลการใช้คอมพิวเตอร์ด้วยคำขอของผู้ใช้
2. [**รับคำตอบของโมเดล**](#model-response)

   - โมเดลการใช้งานคอมพิวเตอร์จะวิเคราะห์คำขอและภาพหน้าจอของผู้ใช้ แล้วสร้างคำตอบซึ่งมี`function_call`ที่แนะนำ
     ซึ่งแสดงถึงการดำเนินการใน UI (เช่น "คลิกที่พิกัด (x,y)" หรือ "พิมพ์
     'ข้อความ'") ดูคำอธิบายการดำเนินการทั้งหมดใน UI ที่โมเดล Computer
     Use รองรับได้ที่[การดำเนินการที่รองรับ](#supported-actions)
   - การตอบกลับจาก API อาจมี `safety_decision` จากระบบความปลอดภัยภายใน
     ที่ตรวจสอบการดำเนินการที่โมเดลเสนอด้วย ซึ่ง
     `safety_decision`จะจัดประเภทการดำเนินการเป็น
     - **ปกติ / อนุญาต:** ระบบจะถือว่าการดำเนินการปลอดภัย นอกจากนี้ ยังอาจ
       แสดงด้วยการไม่มี`safety_decision`
     - **ต้องมีการยืนยัน (`require_confirmation`):** โมเดลกำลังจะดำเนินการที่อาจมีความเสี่ยง (เช่น การคลิก "แบนเนอร์คุกกี้ที่ยอมรับ")
3. [**ดำเนินการตามการกระทำที่ได้รับ**](#execute-actions)

   - โค้ดฝั่งไคลเอ็นต์จะได้รับ `function_call` และ `safety_decision` ที่เกี่ยวข้อง
     - **ปกติ / อนุญาต:** หาก `safety_decision` ระบุว่าปกติ/อนุญาต (หรือหากไม่มี `safety_decision`) โค้ดฝั่งไคลเอ็นต์จะเรียกใช้ `function_call` ที่ระบุในสภาพแวดล้อมเป้าหมายได้ (เช่น เว็บเบราว์เซอร์)
     - **ต้องมีการยืนยัน:** หาก `safety_decision` ระบุว่า
       ต้องมีการยืนยัน แอปพลิเคชันของคุณต้องแจ้งให้ผู้ใช้ปลายทาง
       ยืนยันก่อนที่จะดำเนินการ `function_call` หากผู้ใช้
       ยืนยัน ให้ดำเนินการตามที่ขอ หากผู้ใช้ปฏิเสธ ให้
       อย่าดำเนินการ
4. [**บันทึกสถานะสภาพแวดล้อมใหม่**](#capture-state)

   - หากดำเนินการแล้ว ไคลเอ็นต์จะจับภาพหน้าจอใหม่ของ GUI และ URL ปัจจุบันเพื่อส่งกลับไปยังโมเดลการใช้งานคอมพิวเตอร์เป็นส่วนหนึ่งของ `function_response`
   - หากระบบความปลอดภัยบล็อกการดำเนินการหรือผู้ใช้ปฏิเสธการยืนยัน แอปพลิเคชันของคุณอาจส่งความคิดเห็นในรูปแบบอื่นไปยังโมเดลหรือสิ้นสุดการโต้ตอบ

กระบวนการนี้จะทำซ้ำจากขั้นตอนที่ 2 โดยโมเดลจะใช้
ภาพหน้าจอใหม่และเป้าหมายที่กำลังดำเนินการเพื่อแนะนำการดำเนินการถัดไป ลูปจะทำงานต่อไป
จนกว่าจะทำงานเสร็จ เกิดข้อผิดพลาด หรือกระบวนการสิ้นสุดลง
(เช่น เนื่องจากมีการตอบสนองด้านความปลอดภัยแบบ "บล็อก" หรือผู้ใช้ตัดสินใจ)

![ภาพรวม
การใช้คอมพิวเตอร์](https://ai.google.dev/static/gemini-api/docs/images/computer_use.png?hl=th)

## วิธีใช้งานการใช้คอมพิวเตอร์

ก่อนที่จะสร้างด้วยเครื่องมือการใช้งานคอมพิวเตอร์ คุณจะต้องตั้งค่าสิ่งต่อไปนี้

- **สภาพแวดล้อมการดำเนินการที่ปลอดภัย:** เพื่อความปลอดภัย คุณควรเรียกใช้เอเจนต์การใช้งานคอมพิวเตอร์ในสภาพแวดล้อมที่ปลอดภัยและมีการควบคุม (เช่น เครื่องเสมือนแบบแซนด์บ็อกซ์ คอนเทนเนอร์ หรือโปรไฟล์เบราว์เซอร์เฉพาะที่มีสิทธิ์จำกัด)
- **ตัวแฮนเดิลการดำเนินการฝั่งไคลเอ็นต์:** คุณจะต้องใช้ตรรกะฝั่งไคลเอ็นต์
  เพื่อดำเนินการกับการดำเนินการที่โมเดลสร้างขึ้น และ
  บันทึกภาพหน้าจอของสภาพแวดล้อมหลังจากการดำเนินการแต่ละครั้ง

ตัวอย่างในส่วนนี้ใช้เบราว์เซอร์เป็นสภาพแวดล้อมการดำเนินการ
และ [Playwright](https://playwright.dev/) เป็นตัวแฮนเดิลการดำเนินการฝั่งไคลเอ็นต์ หากต้องการ
เรียกใช้ตัวอย่างเหล่านี้ คุณต้องติดตั้งการอ้างอิงที่จำเป็นและเริ่มต้นอินสแตนซ์เบราว์เซอร์
Playwright

#### ติดตั้ง Playwright

```
    pip install google-genai playwright
    playwright install chromium
```

#### เริ่มต้นอินสแตนซ์เบราว์เซอร์ Playwright

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

โค้ดตัวอย่างสำหรับการขยายไปยังสภาพแวดล้อม Android จะรวมอยู่ในส่วน[การใช้ฟังก์ชันที่ผู้ใช้กำหนด](#custom-functions)

### 1. ส่งคำขอไปยังโมเดล

เพิ่มเครื่องมือการใช้คอมพิวเตอร์ลงในคำขอ API แล้วส่งพรอมต์ไปยังโมเดล
ซึ่งมีเป้าหมายของผู้ใช้ คุณต้องใช้โมเดลที่รองรับการใช้งานคอมพิวเตอร์
หรือจะได้รับข้อผิดพลาด

- `gemini-2.5-computer-use-preview-10-2025`
- `gemini-3-flash-preview`

นอกจากนี้ คุณยังเพิ่มพารามิเตอร์ต่อไปนี้ได้ด้วย (ไม่บังคับ)

- **การดำเนินการที่ยกเว้น:** หากมีการดำเนินการใดๆ จากรายการ[การดำเนินการ UI ที่รองรับ](#supported-actions)ที่คุณไม่ต้องการให้โมเดลดำเนินการ
  ให้ระบุการดำเนินการเหล่านี้เป็น `excluded_predefined_functions`
- **ฟังก์ชันที่ผู้ใช้กำหนด:** นอกเหนือจากเครื่องมือการใช้งานคอมพิวเตอร์แล้ว คุณอาจ
  ต้องการรวมฟังก์ชันที่ผู้ใช้กำหนดเองด้วย

โปรดทราบว่าไม่จำเป็นต้องระบุขนาดการแสดงผลเมื่อส่งคำขอ
เนื่องจากโมเดลจะคาดการณ์พิกัดพิกเซลที่ปรับขนาดตามความสูงและความกว้างของ
หน้าจอ

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
        # 1. Computer Use tool with browser environment
        types.Tool(
            computer_use=types.ComputerUse(
                environment=types.Environment.ENVIRONMENT_BROWSER,
                # Optional: Exclude specific predefined functions
                excluded_predefined_functions=excluded_functions
                )
              ),
        # 2. Optional: Custom user-defined functions
        #types.Tool(
          # function_declarations=custom_functions
          #   )
          ],
  )

# Create the content with user message
contents=[
    Content(
        role="user",
        parts=[
            Part(text="Search for highly rated smart fridges with touchscreen, 2 doors, around 25 cu ft, priced below 4000 dollars on Google Shopping. Create a bulleted list of the 3 cheapest options in the format of name, description, price in an easy-to-read layout."),
        ],
    )
]

# Generate content with the configured settings
response = client.models.generate_content(
    model='gemini-2.5-computer-use-preview-10-2025',
    contents=contents,
    config=generate_content_config,
)

# Print the response output
print(response)
```

ดูตัวอย่างฟังก์ชันที่กำหนดเองได้ที่[การใช้ฟังก์ชันที่ผู้ใช้กำหนดเอง](#custom-functions)

### 2. รับคำตอบของโมเดล

เมื่อเปิดใช้เครื่องมือการใช้คอมพิวเตอร์ โมเดลจะตอบกลับด้วย`FunctionCalls`อย่างน้อย 1 รายการ หากพิจารณาว่าต้องมีการดำเนินการใน UI เพื่อทํางานให้เสร็จสมบูรณ์
การใช้คอมพิวเตอร์รองรับการเรียกใช้ฟังก์ชันแบบขนาน ซึ่งหมายความว่าโมเดลสามารถแสดงผลการดำเนินการหลายอย่างในเทิร์นเดียวได้

ตัวอย่างคำตอบของโมเดลมีดังนี้

```
{
  "content": {
    "parts": [
      {
        "text": "I will type the search query into the search bar. The search bar is in the center of the page."
      },
      {
        "function_call": {
          "name": "type_text_at",
          "args": {
            "x": 371,
            "y": 470,
            "text": "highly rated smart fridges with touchscreen, 2 doors, around 25 cu ft, priced below 4000 dollars on Google Shopping",
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

โค้ดตัวอย่างด้านล่างจะดึงข้อมูลการเรียกใช้ฟังก์ชันจากคำตอบของโมเดลการใช้งานคอมพิวเตอร์
และแปลเป็นคำสั่งที่เรียกใช้ได้ด้วย Playwright
โมเดลจะแสดงผลพิกัดที่ปรับให้เป็นมาตรฐาน (0-999) โดยไม่คำนึงถึงขนาดของรูปภาพที่ป้อน
ดังนั้นขั้นตอนการแปลบางส่วนจึงเป็นการแปลงพิกัดที่ปรับให้เป็นมาตรฐานเหล่านี้
กลับเป็นค่าพิกเซลจริง

ขนาดหน้าจอที่แนะนำสำหรับการใช้
กับโมเดลการใช้คอมพิวเตอร์คือ (1440, 900) โมเดลจะทำงานกับความละเอียดใดก็ได้
แม้ว่าคุณภาพของผลลัพธ์อาจได้รับผลกระทบ

โปรดทราบว่าตัวอย่างนี้รวมเฉพาะการติดตั้งใช้งานสำหรับการดำเนินการ UI ที่พบบ่อยที่สุด 3 รายการ ได้แก่ `open_web_browser`, `click_at` และ `type_text_at` สำหรับ Use Case ในการใช้งานจริง คุณจะต้องใช้การดำเนินการใน UI อื่นๆ ทั้งหมดจากรายการ[การดำเนินการที่รองรับ](#supported-actions) เว้นแต่คุณจะเพิ่มการดำเนินการเหล่านั้นเป็น`excluded_predefined_functions`อย่างชัดแจ้ง

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

def execute_function_calls(candidate, page, screen_width, screen_height):
    results = []
    function_calls = []
    for part in candidate.content.parts:
        if part.function_call:
            function_calls.append(part.function_call)

    for function_call in function_calls:
        action_result = {}
        fname = function_call.name
        args = function_call.args
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

        results.append((fname, action_result))

    return results
```

### 4. บันทึกสถานะสภาพแวดล้อมใหม่

หลังจากดำเนินการแล้ว ให้ส่งผลลัพธ์ของการเรียกใช้ฟังก์ชันกลับไปยังโมเดล เพื่อให้โมเดลใช้ข้อมูลนี้ในการสร้างการดำเนินการถัดไปได้ หากมีการดำเนินการหลายอย่าง (การเรียกแบบขนาน) คุณต้องส่ง `FunctionResponse` สำหรับแต่ละรายการในเทิร์นของผู้ใช้ถัดไป

### Python

```
def get_function_responses(page, results):
    screenshot_bytes = page.screenshot(type="png")
    current_url = page.url
    function_responses = []
    for name, result in results:
        response_data = {"url": current_url}
        response_data.update(result)
        function_responses.append(
            types.FunctionResponse(
                name=name,
                response=response_data,
                parts=[types.FunctionResponsePart(
                        inline_data=types.FunctionResponseBlob(
                            mime_type="image/png",
                            data=screenshot_bytes))
                ]
            )
        )
    return function_responses
```

## สร้างลูปของเอเจนต์

หากต้องการเปิดใช้การโต้ตอบแบบหลายขั้นตอน ให้รวม 4 ขั้นตอนจากส่วน[วิธี
ใช้คอมพิวเตอร์](#implement-computer-use)เป็นลูป
อย่าลืมจัดการประวัติการสนทนาอย่างถูกต้องโดยการต่อท้ายทั้งคำตอบของโมเดลและคำตอบของฟังก์ชัน

หากต้องการเรียกใช้ตัวอย่างโค้ดนี้ คุณต้องทำดังนี้

- ติดตั้ง[การอ้างอิง Playwright
  ที่จำเป็น](#expandable-1)
- กำหนดฟังก์ชันตัวช่วยจากขั้นตอน [(3) ดำเนินการกับ
  การดำเนินการที่ได้รับ](#execute-actions)และ [(4) บันทึกสถานะ
  สภาพแวดล้อมใหม่](#capture-state)

### Python

```
import time
from typing import Any, List, Tuple
from playwright.sync_api import sync_playwright

from google import genai
from google.genai import types
from google.genai.types import Content, Part

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

    # Configure the model (From Step 1)
    config = types.GenerateContentConfig(
        tools=[types.Tool(computer_use=types.ComputerUse(
            environment=types.Environment.ENVIRONMENT_BROWSER
        ))],
        thinking_config=types.ThinkingConfig(include_thoughts=True),
    )

    # Initialize history
    initial_screenshot = page.screenshot(type="png")
    USER_PROMPT = "Go to ai.google.dev/gemini-api/docs and search for pricing."
    print(f"Goal: {USER_PROMPT}")

    contents = [
        Content(role="user", parts=[
            Part(text=USER_PROMPT),
            Part.from_bytes(data=initial_screenshot, mime_type='image/png')
        ])
    ]

    # Agent Loop
    turn_limit = 5
    for i in range(turn_limit):
        print(f"\n--- Turn {i+1} ---")
        print("Thinking...")
        response = client.models.generate_content(
            model='gemini-2.5-computer-use-preview-10-2025',
            contents=contents,
            config=config,
        )

        candidate = response.candidates[0]
        contents.append(candidate.content)

        has_function_calls = any(part.function_call for part in candidate.content.parts)
        if not has_function_calls:
            text_response = " ".join([part.text for part in candidate.content.parts if part.text])
            print("Agent finished:", text_response)
            break

        print("Executing actions...")
        results = execute_function_calls(candidate, page, SCREEN_WIDTH, SCREEN_HEIGHT)

        print("Capturing state...")
        function_responses = get_function_responses(page, results)

        contents.append(
            Content(role="user", parts=[Part(function_response=fr) for fr in function_responses])
        )

finally:
    # Cleanup
    print("\nClosing browser...")
    browser.close()
    playwright.stop()
```

## การใช้ฟังก์ชันที่ผู้ใช้กำหนดเอง

คุณอาจรวมฟังก์ชันที่ผู้ใช้กำหนดเองไว้ในคำขอเพื่อขยายฟังก์ชันการทำงานของโมเดลได้ (ไม่บังคับ) ตัวอย่างด้านล่างนี้ปรับรูปแบบการใช้งานคอมพิวเตอร์
และเครื่องมือสำหรับกรณีการใช้งานบนอุปกรณ์เคลื่อนที่โดยรวมการดำเนินการที่ผู้ใช้กำหนดเอง
เช่น `open_app`, `long_press_at` และ `go_home` ขณะที่ยกเว้น
การดำเนินการเฉพาะเบราว์เซอร์ โมเดลสามารถเรียกฟังก์ชันที่กำหนดเองเหล่านี้อย่างชาญฉลาดควบคู่ไปกับการดำเนินการ UI มาตรฐานเพื่อทำงานให้เสร็จสมบูรณ์ในสภาพแวดล้อมที่ไม่ใช่เบราว์เซอร์

### Python

```
from typing import Optional, Dict, Any

from google import genai
from google.genai import types
from google.genai.types import Content, Part

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

def open_app(app_name: str, intent: Optional[str] = None) -> Dict[str, Any]:
    """Opens an app by name.

    Args:
        app_name: Name of the app to open (any string).
        intent: Optional deep-link or action to pass when launching, if the app supports it.

    Returns:
        JSON payload acknowledging the request (app name and optional intent).
    """
    return {"status": "requested_open", "app_name": app_name, "intent": intent}

def long_press_at(x: int, y: int) -> Dict[str, int]:
    """Long-press at a specific screen coordinate.

    Args:
        x: X coordinate (absolute), scaled to the device screen width (pixels).
        y: Y coordinate (absolute), scaled to the device screen height (pixels).

    Returns:
        Object with the coordinates pressed and the duration used.
    """
    return {"x": x, "y": y}

def go_home() -> Dict[str, str]:
    """Navigates to the device home screen.

    Returns:
        A small acknowledgment payload.
    """
    return {"status": "home_requested"}

#  Build function declarations
CUSTOM_FUNCTION_DECLARATIONS = [
    types.FunctionDeclaration.from_callable(client=client, callable=open_app),
    types.FunctionDeclaration.from_callable(client=client, callable=long_press_at),
    types.FunctionDeclaration.from_callable(client=client, callable=go_home),
]

#Exclude browser functions
EXCLUDED_PREDEFINED_FUNCTIONS = [
    "open_web_browser",
    "search",
    "navigate",
    "hover_at",
    "scroll_document",
    "go_forward",
    "key_combination",
    "drag_and_drop",
]

#Utility function to construct a GenerateContentConfig
def make_generate_content_config() -> genai.types.GenerateContentConfig:
    """Return a fixed GenerateContentConfig with Computer Use + custom functions."""
    return genai.types.GenerateContentConfig(
        system_instruction=SYSTEM_PROMPT,
        tools=[
            types.Tool(
                computer_use=types.ComputerUse(
                    environment=types.Environment.ENVIRONMENT_BROWSER,
                    excluded_predefined_functions=EXCLUDED_PREDEFINED_FUNCTIONS,
                )
            ),
            types.Tool(function_declarations=CUSTOM_FUNCTION_DECLARATIONS),
        ],
    )

# Create the content with user message
contents: list[Content] = [
    Content(
        role="user",
        parts=[
            # text instruction
            Part(text="Open Chrome, then long-press at 200,400."),
        ],
    )
]

# Build your fixed config (from helper)
config = make_generate_content_config()

# Generate content with the configured settings
response = client.models.generate_content(
        model='gemini-2.5-computer-use-preview-10-2025',
        contents=contents,
        config=config,
    )

print(response)
```

## การดำเนินการใน UI ที่รองรับ

โมเดลสามารถขอการดำเนินการใน UI ต่อไปนี้ผ่าน
`FunctionCall` โค้ดฝั่งไคลเอ็นต์ต้องใช้ตรรกะการดำเนินการสำหรับ
การดำเนินการเหล่านี้ ดูตัวอย่างได้ที่[การติดตั้งใช้งาน
อ้างอิง](https://github.com/google/computer-use-preview)

| ชื่อคำสั่ง | คำอธิบาย | อาร์กิวเมนต์ (ใน Function Call) | ตัวอย่างการเรียกใช้ฟังก์ชัน |
| --- | --- | --- | --- |
| **open\_web\_browser** | เปิดเว็บเบราว์เซอร์ | ไม่มี | `{"name": "open_web_browser", "args": {}}` |
| **wait\_5\_seconds** | หยุดการดำเนินการชั่วคราวเป็นเวลา 5 วินาทีเพื่อให้เนื้อหาแบบไดนามิกโหลดหรือภาพเคลื่อนไหวเสร็จสมบูรณ์ | ไม่มี | `{"name": "wait_5_seconds", "args": {}}` |
| **go\_back** | ไปยังหน้าก่อนหน้าในประวัติของเบราว์เซอร์ | ไม่มี | `{"name": "go_back", "args": {}}` |
| **go\_forward** | ไปยังหน้าถัดไปในประวัติของเบราว์เซอร์ | ไม่มี | `{"name": "go_forward", "args": {}}` |
| **search** | ไปยังหน้าแรกของเครื่องมือค้นหาเริ่มต้น (เช่น Google) มีประโยชน์ในการเริ่มงานการค้นหาใหม่ | ไม่มี | `{"name": "search", "args": {}}` |
| **navigate** | นำทางเบราว์เซอร์ไปยัง URL ที่ระบุโดยตรง | `url`: str | `{"name": "navigate", "args": {"url": "https://www.wikipedia.org"}}` |
| **click\_at** | การคลิกที่พิกัดที่เฉพาะเจาะจงในหน้าเว็บ ค่า x และ y อิงตามตารางกริดขนาด 1000x1000 และปรับขนาดให้ตรงกับขนาดหน้าจอ | `y`: int (0-999), `x`: int (0-999) | `{"name": "click_at", "args": {"y": 300, "x": 500}}` |
| **hover\_at** | วางเมาส์ที่พิกัดที่เฉพาะเจาะจงในหน้าเว็บ มีประโยชน์ในการแสดงเมนูย่อย โดย x และ y จะอิงตามตารางกริดขนาด 1000x1000 | `y`: int (0-999) `x`: int (0-999) | `{"name": "hover_at", "args": {"y": 150, "x": 250}}` |
| **type\_text\_at** | พิมพ์ข้อความที่พิกัดที่เฉพาะเจาะจง โดยค่าเริ่มต้นคือล้างช่องก่อนแล้วกด ENTER หลังจากพิมพ์ แต่สามารถปิดใช้ได้ x และ y จะอิงตามตารางกริด 1000x1000 | `y`: int (0-999), `x`: int (0-999), `text`: str, `press_enter`: bool (ไม่บังคับ ค่าเริ่มต้นคือ True), `clear_before_typing`: bool (ไม่บังคับ ค่าเริ่มต้นคือ True) | `{"name": "type_text_at", "args": {"y": 250, "x": 400, "text": "search query", "press_enter": false}}` |
| **key\_combination** | กดแป้นหรือชุดแป้นบนแป้นพิมพ์ เช่น "Control+C" หรือ "Enter" มีประโยชน์ในการเรียกใช้การดำเนินการ (เช่น การส่งแบบฟอร์มด้วย "Enter") หรือการดำเนินการในคลิปบอร์ด | `keys`: สตริง (เช่น "enter", "control+c") | `{"name": "key_combination", "args": {"keys": "Control+A"}}` |
| **scroll\_document** | เลื่อนทั้งหน้าเว็บ "ขึ้น" "ลง" "ซ้าย" หรือ "ขวา" | `direction`: str ("up", "down", "left" หรือ "right") | `{"name": "scroll_document", "args": {"direction": "down"}}` |
| **scroll\_at** | เลื่อนองค์ประกอบหรือพื้นที่ที่เฉพาะเจาะจงที่พิกัด (x, y) ในทิศทางที่ระบุตามขนาดที่กำหนด พิกัดและขนาด (ค่าเริ่มต้นคือ 800) จะอิงตามตารางกริดขนาด 1000x1000 | `y`: int (0-999), `x`: int (0-999), `direction`: str ("up", "down", "left", "right"), `magnitude`: int (0-999, ไม่บังคับ, ค่าเริ่มต้นคือ 800) | `{"name": "scroll_at", "args": {"y": 500, "x": 500, "direction": "down", "magnitude": 400}}` |
| **drag\_and\_drop** | ลากองค์ประกอบจากพิกัดเริ่มต้น (x, y) และวางที่พิกัดปลายทาง (destination\_x, destination\_y) พิกัดทั้งหมดอิงตามตารางขนาด 1000x1000 | `y`: int (0-999), `x`: int (0-999), `destination_y`: int (0-999), `destination_x`: int (0-999) | `{"name": "drag_and_drop", "args": {"y": 100, "x": 100, "destination_y": 500, "destination_x": 500}}` |

## ความปลอดภัย

### รับทราบการตัดสินใจด้านความปลอดภัย

การตอบกลับของโมเดลอาจมี`safety_decision`จากระบบความปลอดภัยภายในที่ตรวจสอบการดำเนินการที่โมเดลเสนอด้วย ทั้งนี้ขึ้นอยู่กับการดำเนินการ

```
{
  "content": {
    "parts": [
      {
        "text": "I have evaluated step 2. It seems Google detected unusual traffic and is asking me to verify I'm not a robot. I need to click the 'I'm not a robot' checkbox located near the top left (y=98, x=95).",
      },
      {
        "function_call": {
          "name": "click_at",
          "args": {
            "x": 60,
            "y": 100,
            "safety_decision": {
              "explanation": "I have encountered a CAPTCHA challenge that requires interaction. I need you to complete the challenge by clicking the 'I'm not a robot' checkbox and any subsequent verification steps.",
              "decision": "require_confirmation"
            }
          }
        }
      }
    ]
  }
}
```

หาก `safety_decision` เป็น `require_confirmation` คุณต้อง
ขอให้ผู้ใช้ปลายทางยืนยันก่อนดำเนินการต่อเพื่อดำเนินการ ตาม[ข้อกำหนดในการให้บริการ](https://ai.google.dev/gemini-api/terms?hl=th) คุณไม่ได้รับอนุญาต
ให้หลีกเลี่ยงคำขอการยืนยันจากมนุษย์

ตัวอย่างโค้ดนี้จะแจ้งให้ผู้ใช้ปลายทางยืนยันก่อนดำเนินการ
การดำเนินการ หากผู้ใช้ไม่ยืนยันการดำเนินการ ลูปจะสิ้นสุด หากผู้ใช้ยืนยันการดำเนินการ ระบบจะดำเนินการดังกล่าวและทำเครื่องหมายช่อง
`safety_acknowledgement`เป็น `True`

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

def execute_function_calls(candidate, page, screen_width, screen_height):

    # ... Extract function calls from response ...

    for function_call in function_calls:
        extra_fr_fields = {}

        # Check for safety decision
        if 'safety_decision' in function_call.args:
            decision = get_safety_confirmation(function_call.args['safety_decision'])
            if decision == "TERMINATE":
                print("Terminating agent loop")
                break
            extra_fr_fields["safety_acknowledgement"] = "true" # Safety acknowledgement

        # ... Execute function call and append to results ...
```

หากผู้ใช้ยืนยัน คุณต้องใส่การรับทราบเรื่องความปลอดภัยใน`FunctionResponse`

### Python

```
function_response_parts.append(
    FunctionResponse(
        name=name,
        response={"url": current_url,
                  **extra_fr_fields},  # Include safety acknowledgement
        parts=[
            types.FunctionResponsePart(
                inline_data=types.FunctionResponseBlob(
                    mime_type="image/png", data=screenshot
                )
             )
           ]
         )
       )
```

### แนวทางปฏิบัติแนะนำด้านความปลอดภัย

การใช้คอมพิวเตอร์เป็นเครื่องมือใหม่ที่นำมาซึ่งความเสี่ยงใหม่ๆ ที่นักพัฒนาซอฟต์แวร์ควรตระหนักถึง

- **เนื้อหาที่ไม่น่าเชื่อถือและการหลอกลวง:** ขณะที่โมเดลพยายามบรรลุเป้าหมายของผู้ใช้
  โมเดลอาจอาศัยแหล่งข้อมูลและวิธีการที่ไม่น่าเชื่อถือ
  จากหน้าจอ ตัวอย่างเช่น หากเป้าหมายของผู้ใช้คือการซื้อโทรศัพท์ Pixel
  และโมเดลพบกลโกง "รับ Pixel ฟรีหากทำแบบสำรวจเสร็จ"
  ก็มีโอกาสที่โมเดลจะทำแบบสำรวจให้เสร็จ
- **การดำเนินการที่ไม่ตั้งใจเป็นครั้งคราว:** โมเดลอาจตีความเป้าหมายของผู้ใช้
  หรือเนื้อหาหน้าเว็บผิด ซึ่งทําให้โมเดลทําการดําเนินการที่ไม่ถูกต้อง เช่น คลิก
  ปุ่มที่ไม่ถูกต้องหรือกรอกแบบฟอร์มที่ไม่ถูกต้อง ซึ่งอาจทำให้งานล้มเหลวหรือ
  การขโมยข้อมูล
- **การละเมิดนโยบาย:** ความสามารถของ API อาจถูกนำไปใช้ (ทั้งโดยตั้งใจและไม่ตั้งใจ) ในกิจกรรมที่ละเมิดนโยบายของ Google ([นโยบายการใช้งานที่ไม่อนุญาตสำหรับ Gen AI](https://policies.google.com/terms/generative-ai/use-policy?hl=th) และ[ข้อกำหนดในการให้บริการเพิ่มเติมของ Gemini API](https://ai.google.dev/gemini-api/terms?hl=th)) ซึ่งรวมถึงการดำเนินการที่
  อาจรบกวนความสมบูรณ์ของระบบ บุกรุกความปลอดภัย
  หลีกเลี่ยงมาตรการรักษาความปลอดภัย
  ควบคุมอุปกรณ์ทางการแพทย์ ฯลฯ

หากต้องการจัดการความเสี่ยงเหล่านี้ คุณสามารถใช้มาตรการด้านความปลอดภัยและแนวทางปฏิบัติแนะนำต่อไปนี้

1. **การมีมนุษย์เป็นผู้ควบคุม (HITL):**

   - **ใช้การยืนยันผู้ใช้:** เมื่อการตอบกลับด้านความปลอดภัยระบุว่า
     `require_confirmation` คุณต้องใช้การยืนยันผู้ใช้ก่อน
     การดำเนินการ ดูโค้ดตัวอย่างได้ที่[รับทราบการตัดสินด้านความปลอดภัย](#safety-decisions)
   - **ระบุวิธีการด้านความปลอดภัยที่กำหนดเอง:** นอกเหนือจากการตรวจสอบการยืนยันผู้ใช้ในตัวแล้ว นักพัฒนาแอปอาจเลือกเพิ่ม[คำสั่งของระบบ](https://ai.google.dev/gemini-api/docs/text-generation?hl=th#system-instructions)ที่กำหนดเอง
     ซึ่งบังคับใช้นโยบายด้านความปลอดภัยของตนเอง ไม่ว่าจะเพื่อบล็อกการดำเนินการบางอย่างของโมเดล
     หรือกำหนดให้ผู้ใช้ยืนยันก่อนที่โมเดลจะดำเนินการบางอย่าง
     ที่มีความเสี่ยงสูงและย้อนกลับไม่ได้ ตัวอย่างคำสั่งระบบความปลอดภัยที่กำหนดเองที่คุณอาจรวมไว้เมื่อโต้ตอบกับโมเดลมีดังนี้

     #### ตัวอย่างวิธีการด้านความปลอดภัย

     ตั้งกฎความปลอดภัยที่กำหนดเองเป็นคำสั่งของระบบ

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
2. **สภาพแวดล้อมการดำเนินการที่ปลอดภัย:** เรียกใช้เอเจนต์ในสภาพแวดล้อมแซนด์บ็อกซ์ที่ปลอดภัย
   เพื่อจำกัดผลกระทบที่อาจเกิดขึ้น (เช่น เครื่องเสมือน (VM) ที่อยู่ในแซนด์บ็อกซ์
   คอนเทนเนอร์ (เช่น Docker) หรือโปรไฟล์เบราว์เซอร์เฉพาะที่มีสิทธิ์แบบจำกัด
   )
3. **การล้างข้อมูลอินพุต:** ล้างข้อความทั้งหมดที่ผู้ใช้สร้างขึ้นในพรอมต์เพื่อลดความเสี่ยงของวิธีการที่ไม่ต้องการหรือการแทรกพรอมต์ ซึ่งเป็น
   เลเยอร์ความปลอดภัยที่มีประโยชน์ แต่ไม่สามารถใช้แทนสภาพแวดล้อมการดำเนินการที่ปลอดภัยได้
4. **แนวทางป้องกันเนื้อหา:** ใช้แนวทางป้องกันและ[API ความปลอดภัยของเนื้อหา](https://ai.google.dev/gemma/docs/shieldgemma?hl=th)เพื่อประเมินอินพุตของผู้ใช้
   อินพุตและเอาต์พุตของเครื่องมือ คำตอบของเอเจนต์เพื่อความเหมาะสม การแทรกพรอมต์
   และการตรวจหาการหลบเลี่ยง
5. **รายการที่อนุญาตและรายการที่บล็อก:** ใช้กลไกการกรองเพื่อควบคุม
   ตำแหน่งที่โมเดลสามารถไปยังได้และสิ่งที่โมเดลทำได้ รายการที่บล็อกเว็บไซต์ที่ห้าม
   เป็นจุดเริ่มต้นที่ดี ในขณะที่รายการที่อนุญาตที่เข้มงวดมากขึ้นจะ
   ปลอดภัยยิ่งกว่า
6. **ความสามารถในการสังเกตและการบันทึก:** จัดเก็บบันทึกโดยละเอียดสำหรับการแก้ไขข้อบกพร่อง การตรวจสอบ และการตอบสนองต่อเหตุการณ์ ลูกค้าของคุณควรบันทึกพรอมต์
   ภาพหน้าจอ การดำเนินการที่โมเดลแนะนำ (function\_call) การตอบกลับด้านความปลอดภัย และ
   การดำเนินการทั้งหมดที่ไคลเอ็นต์ดำเนินการในท้ายที่สุด
7. **การจัดการสภาพแวดล้อม:** ตรวจสอบว่าสภาพแวดล้อม GUI สอดคล้องกัน
   ป๊อปอัป การแจ้งเตือน หรือการเปลี่ยนแปลงเลย์เอาต์ที่ไม่คาดคิดอาจทำให้โมเดลสับสน
   เริ่มต้นจากสถานะที่ทราบและสะอาดสำหรับงานใหม่แต่ละงานหากเป็นไปได้

## เวอร์ชันของโมเดล

โปรดทราบว่า `gemini-3-flash-preview` มีการรองรับการใช้คอมพิวเตอร์ในตัว
คุณจึงไม่จำเป็นต้องมีโมเดลแยกต่างหากเพื่อเข้าถึงเครื่องมือนี้

| พร็อพเพอร์ตี้ | คำอธิบาย |
| --- | --- |
| รหัสโมเดล id\_card | **Gemini API**  `gemini-2.5-computer-use-preview-10-2025` |
| บันทึกประเภทข้อมูลที่รองรับ | **อินพุต**  รูปภาพ ข้อความ  **เอาต์พุต**  ข้อความ |
| token\_autoขีดจำกัดของโทเค็น[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=th) | **ขีดจำกัดโทเค็นอินพุต**  128,000  **ขีดจำกัดโทเค็นเอาต์พุต**  64,000 |
| 123เวอร์ชัน | อ่านรายละเอียดเพิ่มเติมได้ใน[รูปแบบเวอร์ชันของโมเดล](https://ai.google.dev/gemini-api/docs/models/gemini?hl=th#model-versions)  - ตัวอย่าง: `gemini-2.5-computer-use-preview-10-2025` |
| calendar\_monthการอัปเดตล่าสุด | ตุลาคม 2025 |

## ขั้นตอนถัดไป

- ทดลองใช้คอมพิวเตอร์ใน[สภาพแวดล้อมของเดโม Browserbase](http://gemini.browserbase.com)
- ดูโค้ดตัวอย่างได้ที่[การติดตั้งใช้งาน
  อ้างอิง](https://github.com/google/computer-use-preview)
- ดูข้อมูลเกี่ยวกับเครื่องมืออื่นๆ ของ Gemini API
  - [การเรียกใช้ฟังก์ชัน](https://ai.google.dev/gemini-api/docs/function-calling?hl=th)
  - [การเชื่อมต่อแหล่งข้อมูลกับ Google Search](https://ai.google.dev/gemini-api/docs/grounding?hl=th)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-05-19 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-05-19 UTC"],[],[]]
