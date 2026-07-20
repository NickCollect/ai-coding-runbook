---
source_url: https://ai.google.dev/gemini-api/docs/computer-use?hl=zh-TW
fetched_at: 2026-07-20T04:40:43.930652+00:00
title: "\u96fb\u8166\u4f7f\u7528 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw) 現已正式發布。建議使用這個 API，存取所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 電腦使用

您可以使用電腦工具建構瀏覽器、行動裝置和電腦控制代理，與這些裝置互動並自動執行工作。模型可以透過螢幕截圖「看到」電腦畫面，並透過產生特定 UI 動作 (例如滑鼠點選和鍵盤輸入)「採取行動」。與函式呼叫類似，您需要實作用戶端執行環境，才能接收及執行電腦使用動作。

Gemini 3.5 Flash 是建議用於電腦用途的模型，並推出多項新功能：

- **支援多種環境：**為[瀏覽器、行動裝置和電腦](#supported-environments)環境建構代理程式。
- **簡化意圖動作：**動作包含 `intent` 欄位，說明模型在每個步驟背後的推理過程。
- **可設定的安全政策：**透過內建政策類別和覆寫功能，微調[安全行為](#safety-policies)。
- **提示詞注入偵測：**選擇啟用[螢幕截圖掃描](#prompt-injection)功能，偵測隱藏的惡意指令。

透過電腦使用功能，您可以建構具備下列功能的代理程式：

- 自動在網站上輸入重複資料或填寫表單。
- 對網頁應用程式和使用者流程執行自動化測試
- 在各種網站上進行研究 (例如從電子商務網站收集產品資訊、價格和評論，做為購買決策的參考依據)

以下是初始化用戶端，並在啟用瀏覽器環境的 `computer_use` 工具後，將提示傳送至模型的最簡單範例：

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Search for 'Gemini API' on Google.",
    tools=[{"type": "computer_use", "environment": "browser"}]
)

print(interaction)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI();

const interaction = await ai.interactions.create({
  model: 'gemini-3.5-flash',
  input: "Search for 'Gemini API' on Google.",
  tools: [{ type: "computer_use", environment: "browser" }]
});

console.log(interaction);
```

## 電腦使用記錄的運作方式

如要使用電腦使用模型建構代理程式，您需要在應用程式和 API 之間設定連續迴圈。以下說明程式碼在每個步驟中的作用：

1. [**向模型傳送要求**](#send-request)
   - 應用程式會傳送 API 要求，其中包含電腦使用工具、設定 (例如目標環境)、使用者提示和目前畫面的螢幕截圖。
2. [**接收模型回應**](#model-response)
   - 模型會分析畫面和提示，然後傳回回應，包括代表 UI 動作的建議 `function_call` (例如點選、捲動或按鍵)。
   - 如果是 **Gemini 3.5 Flash**，回應中也會包含推論 `intent`，說明模型選擇該動作的原因。
   - 回覆內容也可能包含`safety_decision`，這是內部安全系統對動作的分類結果，分為一般/允許、`require_confirmation` (需要使用者核准) 或封鎖。
3. [**執行收到的動作**](#execute-actions)
   - 如果允許執行動作 (或使用者確認)，用戶端程式碼會剖析 `function_call`、調整標準化座標的比例以符合檢視區塊，並使用自動化工具 (例如 Playwright) 在目標環境中執行動作。如果動作遭到封鎖，用戶端應停止執行或處理中斷情形。
4. [**擷取新環境狀態**](#capture-state)
   - 動作執行完畢後，應用程式會擷取新的螢幕截圖，並透過 `function_result` 將其傳回模型，要求執行下一個步驟。

接著，這個程序會從步驟 2 開始重複執行，持續向模型索取下一個動作，直到工作完成或終止為止。

![電腦使用總覽](https://ai.google.dev/static/gemini-api/docs/images/computer_use.png?hl=zh-tw)

## 如何實作電腦使用

使用電腦用途工具建構內容前，請先設定：

- **安全執行環境：**在沙箱 VM 或容器中執行代理程式，與主機系統隔離，並限制潛在影響。[參考實作](https://github.com/google/computer-use-preview/)包含可直接使用的 Docker 型沙箱，方便您踏出第一步。
- **用戶端動作處理常式：**實作用戶端邏輯，執行座標、輸入文字及擷取螢幕截圖。

下列範例使用網頁瀏覽器做為執行環境，並以 [Playwright](https://playwright.dev/) 做為用戶端處理常式。

### 0：設定 Playwright

首先，請安裝必要套件：

```
pip install google-genai playwright
playwright install chromium
```

接著，初始化要用於執行的 Playwright 瀏覽器例項：

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

### 1. 向模型傳送要求

初始化用戶端程式庫，並設定電腦使用工具。請注意，發出要求時不必指定螢幕大小，模型會預測縮放至螢幕高度和寬度的像素座標。

### Gemini 3.5 Flash (建議)

### Python

使用 `google-genai` Python SDK (版本 `2.7.0` 以上) 設定以瀏覽器環境為目標的請求：

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model='gemini-3.5-flash',
    input="Find a flight from SF to Hawaii on Jun 30th, coming back on Jul 6th",
    tools=[
        {
            "type": "computer_use",
            "environment": "browser",
            "enable_prompt_injection_detection": True
        }
    ]
)

print(interaction)
```

### JavaScript

使用 `@google/genai` Node.js SDK 設定以瀏覽器環境為目標的請求：

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI();

const interaction = await ai.interactions.create({
  model: 'gemini-3.5-flash',
  input: "Find a flight from SF to Hawaii on Jun 30th, coming back on Jul 6th",
  tools: [
    {
      type: "computer_use",
      environment: "browser",
      enable_prompt_injection_detection: true
    }
  ]
});

console.log(interaction);
```

### REST

使用 curl 傳送要求：

```
curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Find me a flight from SF to Hawaii on Jun 30th, coming back on Jul 6th. Start by navigating directly to flights.google.com",
    "tools": [
      {
        "type": "computer_use",
        "environment": "browser",
        "enable_prompt_injection_detection": true
      }
    ]
  }'
```

### Gemini 2.5 (舊版)

### Python

```
from google import genai

client = genai.Client()

# Specify predefined functions to exclude (optional)
excluded_functions = ["drag_and_drop"]

interaction = client.interactions.create(
    model='gemini-2.5-computer-use-preview-10-2025',
    input="Search for highly rated smart fridges on Google Shopping.",
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

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI();

// Specify predefined functions to exclude (optional)
const excludedFunctions = ["drag_and_drop"];

const interaction = await ai.interactions.create({
  model: 'gemini-2.5-computer-use-preview-10-2025',
  input: "Search for highly rated smart fridges on Google Shopping.",
  tools: [
    {
      type: "computer_use",
      environment: "browser",
      excluded_predefined_functions: excludedFunctions
    }
  ]
});

console.log(interaction);
```

### 2. 接收模型回覆

回應模型會建議呼叫函式。如果是 **Gemini 3.5 Flash**，回覆內容會包含量身打造的推論意圖和座標。以下範例顯示這兩種回應：

### Gemini 3.5 Flash

```
{
  "steps": [
    {
      "type": "function_call",
      "name": "click",
      "arguments": {
        "x": 450,
        "y": 120,
        "intent": "Click the search box to type the destination."
      }
    }
  ]
}
```

### Gemini 2.5 (舊版)

```
{
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "I will type the search query into the search bar."
        }
      ]
    },
    {
      "type": "function_call",
      "name": "type_text_at",
      "arguments": {
        "x": 371,
        "y": 470,
        "text": "highly rated smart fridges",
        "press_enter": true
      }
    }
  ]
}
```

### 3. 執行收到的動作

應用程式必須剖析回應座標、執行動作，並從標準化的 1000x1000 座標調整大小。

下方程式碼會同時處理舊版工具指令 (`click_at`、`type_text_at`) 和 Gemini 3.5 Flash 簡化指令 (`click`、`type`)。

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

async function executeFunctionCalls(interaction, page, screenWidth, screenHeight) {
    const results = [];
    const functionCalls = interaction.steps.filter(step => step.type === "function_call");

    for (const functionCall of functionCalls) {
        const actionResult = {};
        const fname = functionCall.name;
        const args = functionCall.arguments;
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

### 4. 擷取新環境狀態

執行動作後，將函式執行結果傳回模型，模型就能使用這項資訊生成下一個動作。如果執行多個動作 (平行呼叫)，您必須在後續使用者回合中，針對每個動作傳送 `function_result`。

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

定義如何擷取及格式化環境狀態後，您就可以將所有這些步驟合併為持續執行迴圈。

## 建構代理迴圈

如要啟用多步驟互動，請將「如何實作電腦使用」一節中的四個步驟合併為單一迴圈。這個迴圈會持續要求動作，並將結果回饋給模型，直到工作完成為止。

請務必在每個步驟中，將模型回覆和函式回覆附加至記錄，正確管理對話記錄。

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
        model='gemini-3.5-flash',
        input=[
            {"type": "text", "text": USER_PROMPT},
            {"type": "image", "data": base64.b64encode(initial_screenshot).decode("utf-8"), "mime_type": "image/png"}
        ],
        tools=[{
            "type": "computer_use",
            "environment": "browser",
            "enable_prompt_injection_detection": True
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
            model='gemini-3.5-flash',
            previous_interaction_id=interaction.id,
            input=function_responses,
            tools=[{
                "type": "computer_use",
                "environment": "browser",
                "enable_prompt_injection_detection": True
            }]
        )

finally:
    # Cleanup
    print("\nClosing browser...")
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
    // Go to initial page
    await page.goto("https://ai.google.dev/gemini-api/docs");

    // Take initial screenshot
    const initialScreenshotBuffer = await page.screenshot({ type: 'png' });
    const initialScreenshotBase64 = initialScreenshotBuffer.toString('base64');
    const USER_PROMPT = "Go to ai.google.dev/gemini-api/docs and search for pricing.";
    console.log(`Goal: ${USER_PROMPT}`);

    // First interaction
    let interaction = await ai.interactions.create({
        model: 'gemini-3.5-flash',
        input: [
            { type: 'text', text: USER_PROMPT },
            { type: 'image', data: initialScreenshotBase64, mime_type: 'image/png' }
        ],
        tools: [{
            type: 'computer_use',
            environment: 'browser',
            enable_prompt_injection_detection: true
        }]
    });

    // Agent Loop
    const turnLimit = 5;
    for (let i = 0; i < turnLimit; i++) {
        console.log(`\n--- Turn ${i + 1} ---`);

        const hasFunctionCalls = interaction.steps.some(step => step.type === "function_call");
        if (!hasFunctionCalls) {
            const textResponses = [];
            for (const step of interaction.steps) {
                if (step.type === "model_output") {
                    for (const contentBlock of step.content || []) {
                        if (contentBlock.type === "text") {
                            textResponses.push(contentBlock.text);
                        }
                    }
                }
            }
            console.log("Agent finished:", textResponses.join(" "));
            break;
        }

        console.log("Executing actions...");
        const results = await executeFunctionCalls(interaction, page, SCREEN_WIDTH, SCREEN_HEIGHT);

        console.log("Capturing state...");
        const functionResponses = await getFunctionResponses(page, results);

        // Continue conversation with function responses
        interaction = await ai.interactions.create({
            model: 'gemini-3.5-flash',
            previous_interaction_id: interaction.id,
            input: functionResponses,
            tools: [{
                type: 'computer_use',
                environment: 'browser',
                enable_prompt_injection_detection: true
            }]
        });
    }
} finally {
    // Cleanup
    console.log("\nClosing browser...");
    await browser.close();
}
```

## 支援的環境 (Gemini 3.5 Flash)

Gemini 3.5 Flash 支援 `computer_use` 設定中指定的三種環境：

### 瀏覽器環境 (`ENVIRONMENT_BROWSER`)

瀏覽器工具可執行的動作：

| 指令名稱 | 說明 | 引數 (在函式呼叫中) |
| --- | --- | --- |
| **點按** | 在座標處按一下滑鼠左鍵。 | `y`：int (0-999) `x`：int (0-999) `intent`：str |
| **double\_click** | 在座標上按兩下。 | `y`：int (0-999) `x`：int (0-999) `intent`：str |
| **triple\_click** | 在座標上按三下滑鼠。 | `y`：int (0-999) `x`：int (0-999) `intent`：str |
| **middle\_click** | 在座標上按中間鍵。 | `y`：int (0-999) `x`：int (0-999) `intent`：str |
| **right\_click** | 在座標上按一下滑鼠右鍵。 | `y`：int (0-999) `x`：int (0-999) `intent`：str |
| **mouse\_down** | 在座標位置按住滑鼠按鈕。 | `y`：int (0-999) `x`：int (0-999) `intent`：str |
| **mouse\_up** | 在座標處放開滑鼠按鈕。 | `y`：int (0-999) `x`：int (0-999) `intent`：str |
| **移動** | 將游標移至指定位置。 | `y`：int (0-999) `x`：int (0-999) `intent`：str |
| **type** | 輸入文字。 | `text`：str `press_enter`：bool (選用，預設為 `false`) `intent`：str |
| **drag\_and\_drop** | 將項目從起始座標拖曳至結束座標。 | `start_y`：int (0-999) `start_x`：int (0-999) `end_y`：int (0-999) `end_x`：int (0-999) `intent`：str |
| **wait** | 暫停執行指定的秒數。 | `seconds`：int (選用，預設為 `1`) `intent`：str |
| **press\_key** | 按下並放開指定鍵。 | `key`：str `intent`：str |
| **key\_down** | 按下並按住指定鍵。 | `key`：str `intent`：str |
| **key\_up** | 釋放指定鍵。 | `key`：str `intent`：str |
| **快速鍵** | 按下指定的按鍵組合。 | `keys`：`List[str]` `intent`：`str` |
| **take\_screenshot** | 傳回目前畫面的螢幕截圖。 | `intent`：str |
| **scroll** | 以像素距離在座標上下左右捲動。 | `y`：int (0 到 999) `x`：int (0 到 999) `direction`：str (`"up"`、`"down"`、`"left"`、`"right"`) `magnitude_in_pixels`：int (0 到 999，選用，預設為 `300`) `intent`：str |
| **go\_back** | 返回瀏覽器記錄中的上一頁。 | `intent`：str |
| **navigate** | 直接前往指定網址。 | `url`：str `intent`：str |
| **go\_forward** | 前往瀏覽器記錄中的下一個網頁。 | `intent`：str |

### 行動環境 (`ENVIRONMENT_MOBILE`)

Android 最佳化環境動作：

| 指令名稱 | 說明 | 引數 (在函式呼叫中) |
| --- | --- | --- |
| **open\_app** | 依名稱開啟應用程式。 | `app_name`：str `intent`：str |
| **點按** | 在座標處按一下滑鼠左鍵。 | `y`：int (0-999) `x`：int (0-999) `intent`：str |
| **list\_apps** | 列出裝置上可用的應用程式，並傳回應用程式名稱和套件名稱。 | `intent`：str |
| **wait** | 暫停執行指定的秒數。 | `seconds`：int (選用，預設為 `1`) `intent`：str |
| **go\_back** | 返回上一個畫面或網頁。 | `intent`：str |
| **type** | 輸入文字。 | `text`：str `press_enter`：bool (選用，預設為 `false`) `intent`：str |
| **drag\_and\_drop** | 將項目從起始座標拖曳至結束座標。 | `start_y`：int (0-999) `start_x`：int (0-999) `end_y`：int (0-999) `end_x`：int (0-999) `intent`：str |
| **long\_press** | 在螢幕上的座標執行長按操作。 | `y`：int (0 到 999) `x`：int (0 到 999) `seconds`：int (選用，預設為 `2`) `intent`：str |
| **press\_key** | 按下並放開指定鍵。 | `key`：str `intent`：str |
| **take\_screenshot** | 傳回目前畫面的螢幕截圖。 | `intent`：str |

### 桌面環境 (`ENVIRONMENT_DESKTOP`)

桌面環境作業系統層級游標指令：

| 指令名稱 | 說明 | 引數 (在函式呼叫中) |
| --- | --- | --- |
| **點按** | 在座標處按一下滑鼠左鍵。 | `y`：int (0-999) `x`：int (0-999) `intent`：str |
| **double\_click** | 在座標上按兩下。 | `y`：int (0-999) `x`：int (0-999) `intent`：str |
| **triple\_click** | 在座標上按三下滑鼠。 | `y`：int (0-999) `x`：int (0-999) `intent`：str |
| **middle\_click** | 在座標上按中間鍵。 | `y`：int (0-999) `x`：int (0-999) `intent`：str |
| **right\_click** | 在座標上按一下滑鼠右鍵。 | `y`：int (0-999) `x`：int (0-999) `intent`：str |
| **mouse\_down** | 在座標位置按住滑鼠按鈕。 | `y`：int (0-999) `x`：int (0-999) `intent`：str |
| **mouse\_up** | 在座標處放開滑鼠按鈕。 | `y`：int (0-999) `x`：int (0-999) `intent`：str |
| **移動** | 將游標移至指定位置。 | `y`：int (0-999) `x`：int (0-999) `intent`：str |
| **type** | 輸入文字。 | `text`：str `press_enter`：bool (選用，預設為 `false`) `intent`：str |
| **drag\_and\_drop** | 將項目從起始座標拖曳至結束座標。 | `start_y`：int (0-999) `start_x`：int (0-999) `end_y`：int (0-999) `end_x`：int (0-999) `intent`：str |
| **wait** | 暫停執行指定的秒數。 | `seconds`：int (選用，預設為 `1`) `intent`：str |
| **press\_key** | 按下並放開指定鍵。 | `key`：str `intent`：str |
| **key\_down** | 按下並按住指定鍵。 | `key`：str `intent`：str |
| **key\_up** | 釋放指定鍵。 | `key`：str `intent`：str |
| **快速鍵** | 按下指定的按鍵組合。 | `keys`：`List[str]` `intent`：`str` |
| **take\_screenshot** | 傳回目前畫面的螢幕截圖。 | `intent`：str |
| **scroll** | 以像素距離在座標上下左右捲動。 | `y`：int (0 到 999) `x`：int (0 到 999) `direction`：str (`"up"`、`"down"`、`"left"`、`"right"`) `magnitude_in_pixels`：int (0 到 999，選用，預設為 `300`) `intent`：str |

## 舊版支援的 UI 動作 (Gemini 2.5)

對於舊版模型 (`gemini-2.5-computer-use-preview-10-2025`)，系統支援下列動作：

| 指令名稱 | 說明 | 引數 (在函式呼叫中) | 函式呼叫範例 |
| --- | --- | --- | --- |
| **open\_web\_browser** | 開啟網路瀏覽器。 | 無 | `{"name": "open_web_browser", "arguments": {}}` |
| **wait\_5\_seconds** | 暫停執行 5 秒。 | 無 | `{"name": "wait_5_seconds", "arguments": {}}` |
| **go\_back** | 前往瀏覽記錄中的上一頁。 | 無 | `{"name": "go_back", "arguments": {}}` |
| **go\_forward** | 前往記錄中的下一頁。 | 無 | `{"name": "go_forward", "arguments": {}}` |
| **search** | 前往預設搜尋引擎。 | 無 | `{"name": "search", "arguments": {}}` |
| **navigate** | 直接將瀏覽器導向指定網址。 | `url`：str | `{"name": "navigate", "arguments": {"url": "https://www.wikipedia.org"}}` |
| **click\_at** | 在特定座標點擊。 | `y`：int (0 到 999)，`x`：int (0 到 999) | `{"name": "click_at", "arguments": {"y": 300, "x": 500}}` |
| **hover\_at** | 將滑鼠懸停在特定座標。 | `y`：int (0 到 999)，`x`：int (0 到 999) | `{"name": "hover_at", "arguments": {"y": 150, "x": 250}}` |
| **type\_text\_at** | 在座標位置輸入文字。 | `y`：int (0 到 999)、`x`：int (0 到 999)、`text`：str、`press_enter`：bool (選用，預設為 True)、`clear_before_typing`：bool (選用，預設為 True) | `{"name": "type_text_at", "arguments": {"y": 250, "x": 400, "text": "search", "press_enter": false}}` |
| **key\_combination** | 按下按鍵或組合鍵。 | `keys`：str | `{"name": "key_combination", "arguments": {"keys": "Control+A"}}` |
| **scroll\_document** | 捲動整個網頁。 | `direction`：str | `{"name": "scroll_document", "arguments": {"direction": "down"}}` |
| **scroll\_at** | 在座標 (x,y) 捲動。 | `y`：int、`x`：int、`direction`：str、`magnitude`：int (選用，預設為 800) | `{"name": "scroll_at", "arguments": {"y": 500, "x": 500, "direction": "down"}}` |
| **drag\_and\_drop** | 在兩個座標之間拖曳。 | `y`：int、`x`：int、`destination_y`：int、`destination_x`：int | `{"name": "drag_and_drop", "arguments": {"y": 100, "destination_y": 500, "destination_x": 500, "x": 100}}` |

## 自訂使用者定義函式

您可以納入自訂的 user-defined function，擴充模型的函式。舉例來說，在人機迴圈 (HITL) 情境中，您可以排除預先定義的預設動作，並註冊自訂動作。

#### Gemini 3.5 Flash Custom Tooling

### Python

排除標準預先定義的瀏覽器動作 (例如 `click`)，並註冊自訂 `yield_to_user` 工具：

```
from google import genai

client = genai.Client()

yield_to_user_tool = {
    "type": "function",
    "name": "yield_to_user",
    "description": "Yields control back to the user for assistance or verification when an automated action is unsafe or ambiguous.",
    "parameters": {
        "type": "object",
        "properties": {
            "reason": {
                "type": "string",
                "description": "The reason why the agent is yielding control to the human."
            }
        },
        "required": ["reason"]
    }
}

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Click the submit button. If you need a second factor authentication code, ask me.",
    tools=[
        {
            "type": "computer_use",
            "environment": "mobile",
            "excluded_predefined_functions": ["click"]
        },
        yield_to_user_tool
    ]
)
```

### JavaScript

排除標準預先定義的瀏覽器動作 (例如 `click`)，並註冊自訂 `yield_to_user` 工具：

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI();

const yieldToUserTool = {
    type: "function",
    name: "yield_to_user",
    description: "Yields control back to the user for assistance or verification when an automated action is unsafe or ambiguous.",
    parameters: {
        type: "object",
        properties: {
            reason: {
                type: "string",
                description: "The reason why the agent is yielding control to the human."
            }
        },
        required: ["reason"]
    }
};

const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Click the submit button. If you need a second factor authentication code, ask me.",
    tools: [
        {
            type: "computer_use",
            environment: "mobile",
            excluded_predefined_functions: ["click"]
        },
        yieldToUserTool
    ]
});
```

#### Gemini 2.5 (Legacy) Custom Tooling

### Python

```
from google import genai

client = genai.Client()

# Define custom tools here
custom_functions = [...]  # Describe parameters as function declarations

excluded_functions = [
    "open_web_browser",
    "wait_5_seconds",
    "go_back",
    "go_forward",
    "search",
    "navigate",
    "hover_at",
    "scroll_document",
    "key_combination",
    "drag_and_drop",
]

interaction = client.interactions.create(
    model='gemini-2.5-computer-use-preview-10-2025',
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

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI();

// Define custom tools here
const customFunctions = [...]; // Describe parameters as function declarations

const excludedFunctions = [
    "open_web_browser",
    "wait_5_seconds",
    "go_back",
    "go_forward",
    "search",
    "navigate",
    "hover_at",
    "scroll_document",
    "key_combination",
    "drag_and_drop",
];

const interaction = await ai.interactions.create({
    model: 'gemini-2.5-computer-use-preview-10-2025',
    input: "Open Chrome, then long-press at 200,400.",
    tools: [
        {
            type: "computer_use",
            environment: "browser",
            excluded_predefined_functions: excludedFunctions
        },
        ...customFunctions
    ]
});

console.log(interaction);
```

## 管理思考程度 (Gemini 3.5 Flash)

對於電腦使用代理程式，您可以設定不同的思考層級，以平衡動作品質和執行速度。較低的思考層級通常能為標準自動化工作取得良好平衡。

## 安全與安全性

### 設定安全政策 (Gemini 3.5 Flash)

Gemini 3.5 Flash 模型內建安全服務類別，可自動判斷是否需要使用者確認。

| 安全政策類別 | 說明 |
| --- | --- |
| `FINANCIAL_TRANSACTIONS` | 封鎖或觸發涉及付款、零售結帳或管制商品的動作確認。 |
| `SENSITIVE_DATA_MODIFICATION` | 保護健康、財務或政府記錄，避免未經授權的修改。 |
| `COMMUNICATION_TOOL` | 禁止代理程式自主傳送電子郵件、即時通訊訊息或草稿。 |
| `ACCOUNT_CREATION` | 禁止代理程式在網站上自主註冊新帳戶。 |
| `DATA_MODIFICATION` | 控管整體檔案系統修改、資料共用和儲存空間刪除作業。 |
| `USER_CONSENT_MANAGEMENT` | 需要使用者接管 Cookie 同意橫幅和隱私權提示。 |
| `LEGAL_TERMS_AND_AGREEMENTS` | 避免模型自主接受《服務條款》或具有法律約束力的合約。 |

#### 安全覆寫

您可以傳遞覆寫項目，藉此覆寫特定政策：

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Clean up the local folder by archiving old logs.",
    tools=[
        {
            "type": "computer_use",
            "environment": "desktop",
            "disabled_safety_policies": [
                "data_modification"
            ]
        }
    ]
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI();

const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Clean up the local folder by archiving old logs.",
    tools: [
        {
            type: "computer_use",
            environment: "desktop",
            disabled_safety_policies: [
                "data_modification"
            ]
        }
    ]
});
```

### 提示插入偵測 (Gemini 3.5 Flash)

這項安全機制可掃描螢幕截圖中的像素，找出隱藏的對抗性提示指令 (例如「忽略先前的指令」)，並在偵測到時封鎖執行。

### 確認安全裁決

回覆內容可能包含函式呼叫引數中的 `safety_decision` 參數：

```
{
  "steps": [
    {
      "type": "function_call",
      "name": "click_at",
      "arguments": {
        "x": 60,
        "y": 100,
        "safety_decision": {
          "explanation": "Must check check-box",
          "decision": "require_confirmation"
        }
      }
    }
  ]
}
```

如果 `safety_decision` 為 `require_confirmation`，請提示使用者。如果使用者確認，請在 `function_result` 中設定 `safety_acknowledgement`。

### Python

```
def get_safety_confirmation(safety_decision):
    # Prompt user for confirmation
    print(f"Safety confirmation required: {safety_decision.get('explanation', '')}")
    return "CONTINUE" # Or TERMINATE

# Inside execute_function_calls, check for safety_decision:
if 'safety_decision' in function_call.arguments:
    decision = get_safety_confirmation(function_call.arguments['safety_decision'])
    if decision == "TERMINATE":
        break
    # Include safety_acknowledgement inside the action result
    action_result["safety_acknowledgement"] = True
```

### 安全性最佳做法

電腦使用功能會帶來獨特的安全性與作業風險，因為模型代表使用者執行動作時，可能會在畫面上遇到不受信任的內容，或在執行動作時發生錯誤。請實作下列最佳做法，保護使用者資料和系統：

1. **人機迴圈 (HITL)：**

   - **強制使用者確認：**當安全回應指出 `require_confirmation` (或舊版安全決策要求)，提示使用者核准。
   - **提供自訂安全指示：**實作自訂系統指令，定義及強制執行專屬安全界線。例如：

     ### Python

     ```
     from google import genai

     client = genai.Client()

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

     interaction = client.interactions.create(
         model="gemini-3.5-flash",
         system_instruction=system_instruction,
         input="Prepare a draft but do not send.",
         tools=[{
             "type": "computer_use",
             "environment": "browser"
         }]
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
     `;

     const interaction = await ai.interactions.create({
         model: "gemini-3.5-flash",
         system_instruction: systemInstruction,
         input: "Prepare a draft but do not send.",
         tools: [{
             type: "computer_use",
             environment: "browser"
         }]
     });
     ```
2. **安全執行環境：**在安全的沙箱環境中執行代理程式，以限制潛在影響。可以是沙箱虛擬機器 (VM)、容器 (例如 Docker)，或權限受限的專用瀏覽器設定檔。如需使用 Docker 設定沙箱的指南，請參閱 [GitHub 參考實作](https://github.com/google/computer-use-preview/)。
3. **輸入內容清除：**清除提示詞中所有使用者產生的文字，降低出現非預期指令或提示詞注入的風險。這層安全防護很有幫助，但無法取代安全執行環境。
4. **內容防護機制：**使用防護機制和內容安全 API 評估使用者輸入內容、工具輸入內容和輸出內容，以及代理程式的回覆是否適當，並偵測提示詞注入和越獄活動。
5. **許可清單和封鎖清單：**導入篩選機制，控管模型可前往的位置和可執行的動作。禁止存取的網站封鎖清單是不錯的起點，而限制更嚴格的許可清單則更加安全。
6. **可觀測性和記錄：**維護詳細記錄以進行偵錯、稽核和事件應對。用戶端應記錄提示、螢幕截圖、模型建議的動作 (`function_call`)、安全回應，以及用戶端最終執行的所有動作。
7. **環境管理：**確保 GUI 環境一致。如果出現非預期的彈出式視窗、通知或版面配置變更，模型可能會感到困惑。盡可能從已知的乾淨狀態開始執行每個新工作。

## 模型版本

您可以在下列機型上使用電腦模式：

- [**Gemini 3.5 Flash**](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=zh-tw) (`gemini-3.5-flash`)：建議用於電腦，可簡化意圖相關動作、支援瀏覽器、行動裝置和電腦環境、設定安全防護政策，以及偵測提示注入攻擊。
- [**Gemini 3 Flash 預先發布版**](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=zh-tw) (`gemini-3-flash-preview`)：支援電腦使用的預先發布模型。
- [**Gemini 2.5 (舊版預先發布版)**](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-computer-use-preview-10-2025?hl=zh-tw) (`gemini-2.5-computer-use-preview-10-2025`)：舊版預先發布模型，專為瀏覽器型電腦使用而設計。

## 後續步驟

- 在 [Browserbase 示範環境](http://gemini.browserbase.com)中試用電腦。
- 如需程式碼範例，請參閱[參考實作](https://github.com/google/computer-use-preview)。
- 瞭解其他 Gemini API 工具：
  - [函式呼叫](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-tw)
  - [以 Google 搜尋強化事實基礎](https://ai.google.dev/gemini-api/docs/google-search?hl=zh-tw)

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-07-06 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-07-06 (世界標準時間)。"],[],[]]
