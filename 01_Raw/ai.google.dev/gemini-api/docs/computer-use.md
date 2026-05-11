---
source_url: https://ai.google.dev/gemini-api/docs/computer-use?hl=zh-CN
fetched_at: 2026-05-11T05:05:27.089366+00:00
title: "Gemini generateContent API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-cn) 现已推出预览版，支持协作规划、可视化、MCP 等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [generateContent API](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 计算机使用

借助计算机使用，您可以构建与任务交互并自动执行任务的浏览器控制代理。通过使用屏幕截图，模型可以“看到”计算机屏幕，并通过生成特定的界面操作（例如鼠标点击和键盘输入）来“执行操作”。与函数调用类似，您需要编写客户端应用代码来接收和执行计算机使用操作。

借助计算机使用，您可以构建能够执行以下操作的代理：

- 自动执行网站上的重复数据输入或表单填写。
- 自动测试 Web 应用和用户流程
- 在各种网站上进行研究（例如，从电子商务网站收集产品信息、价格和评价，以便为购买提供参考）

测试计算机使用功能的最简单方法是通过 [参考
实现](https://github.com/google/computer-use-preview/) 或
[Browserbase 演示环境](http://gemini.browserbase.com)。

## 计算机使用的工作原理

如需使用计算机使用模型构建浏览器控制代理，请实现一个执行以下操作的代理循环：

1. [**向模型发送请求**](#send-request)

   - 将计算机使用工具以及任何可选的自定义用户定义的函数或排除的函数添加到您的 API 请求中。
   - 使用用户的请求提示计算机使用模型。
2. [**接收模型响应**](#model-response)

   - 计算机使用模型会分析用户请求和屏幕截图，并生成一个响应，其中包含一个建议的 `function_call`，表示界面操作（例如“点击坐标 (x,y)”或“输入‘文字’”）。如需了解计算机
     使用模型支持的所有界面操作，请参阅[支持的操作](#supported-actions)。
   - API 响应还可能包含来自内部安全系统的 `safety_decision`，该系统会检查模型建议的操作。此 `safety_decision` 将操作归类为：
     - **常规 / 允许** ：该操作被认为是安全的。这也可以通过不存在 `safety_decision` 来表示。
     - **需要确认 (`require_confirmation`)** ：模型即将执行可能存在风险的操作（例如，点击“接受 Cookie 横幅”）。
3. [**执行收到的操作**](#execute-actions)

   - 您的客户端代码会接收 `function_call` 和任何随附的 `safety_decision`。
     - **常规 / 允许** ：如果 `safety_decision` 指示常规/允许（或者如果不存在 `safety_decision`），您的客户端代码可以在目标环境（例如网络浏览器）中执行指定的 `function_call`。
     - **需要确认** ：如果 `safety_decision` 指示需要确认，您的应用必须先提示最终用户进行确认，然后才能执行 `function_call`。如果用户确认，请继续执行操作。如果用户拒绝，请勿执行该操作。
4. [**捕获新的环境状态**](#capture-state)

   - 如果操作已执行，客户端会捕获 GUI 和当前网址的新屏幕截图，并将其作为 `function_response` 的一部分发送回计算机使用模型。
   - 如果操作被安全系统阻止或用户拒绝确认，您的应用可能会向模型发送不同形式的反馈或结束互动。

此过程从第 2 步开始重复，模型使用新的屏幕截图和正在进行的目标来建议下一步操作。循环会一直持续，直到任务完成、发生错误或进程终止（例如，由于“阻止”安全响应或用户决定）。

![计算机使用概览](https://ai.google.dev/static/gemini-api/docs/images/computer_use.png?hl=zh-cn)

## 如何实现计算机使用

在使用计算机使用工具进行构建之前，您需要设置以下内容：

- **安全执行环境** ：出于安全考虑，您应在安全且受控的环境中运行计算机使用代理（例如，沙盒化虚拟机、容器或具有有限权限的专用浏览器配置文件）。
- **客户端操作处理程序** ：您需要实现客户端逻辑，以执行模型生成的操作并在每次操作后捕获环境的屏幕截图。

本部分中的示例使用浏览器作为执行环境
并使用 [Playwright](https://playwright.dev/) 作为客户端操作处理程序。如需运行这些示例，您必须安装必要的依赖项并初始化 Playwright 浏览器实例。

#### 安装 Playwright

```
    pip install google-genai playwright
    playwright install chromium
```

#### 初始化 Playwright 浏览器实例

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

将扩展到 Android
环境的示例代码包含在[使用自定义用户定义的
函数](#custom-functions)部分中。

### 1. 向模型发送请求

将计算机使用工具添加到您的 API 请求中，并向模型发送包含用户目标的提示。您必须使用计算机使用支持的模型之一，否则会收到错误：

- `gemini-2.5-computer-use-preview-10-2025`
- `gemini-3-flash-preview`

您还可以选择添加以下参数：

- **排除的操作**：如果您不希望模型执行“[支持的
  界面操作](#supported-actions)”列表中的任何操作，请将这些操作指定为 `excluded_predefined_functions`。
- **用户定义的函数** ：除了计算机使用工具之外，您可能还想添加自定义的用户定义的函数。

请注意，发出请求时无需指定显示大小；模型会预测缩放为屏幕高度和宽度的像素坐标。

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

如需查看包含自定义函数的示例，请参阅[使用自定义
用户定义的函数](#custom-functions)。

### 2. 接收模型响应

启用计算机使用工具后，如果模型确定需要界面操作才能完成任务，则会使用一个或多个 `FunctionCalls` 进行响应。
计算机使用支持并行函数调用，这意味着模型可以在一轮中返回多个操作。

以下是模型响应的示例。

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

### 3. 执行收到的操作

您的应用代码需要解析模型响应、执行操作并收集结果。

以下示例代码从计算机使用模型响应中提取函数调用，并将其转换为可以使用 Playwright 执行的操作。
无论输入图片尺寸如何，模型都会输出归一化坐标 (0-999)，因此转换步骤的一部分是将这些归一化坐标转换回实际像素值。

建议与计算机使用模型搭配使用的屏幕尺寸为 (1440, 900)。该模型适用于任何分辨率，但结果的质量可能会受到影响。

请注意，此示例仅包含 3 个最常见的界面操作的实现：`open_web_browser`、`click_at` 和 `type_text_at`。对于
生产用例，您需要实现
[支持的操作](#supported-actions)列表中的所有其他界面操作，除非您明确将其添加为
`excluded_predefined_functions`。

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

### 4. 捕获新的环境状态

执行操作后，将函数执行结果发送回模型，以便模型可以使用此信息生成下一个操作。如果执行了多个操作（并行调用），您必须在后续用户轮次中为每个操作发送一个 `FunctionResponse`。

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

## 构建代理循环

如需启用多步互动，请将[如何
实现计算机使用](#implement-computer-use)部分中的四个步骤组合成一个循环。
请记得通过附加模型响应和函数响应来正确管理对话历史记录。

如需运行此代码示例，您需要：

- 安装[必要的 Playwright
  依赖项](#expandable-1)。
- 定义步骤 [3（执行收到的
  操作](#execute-actions)）和步骤 [4（捕获新的环境
  状态](#capture-state)）中的辅助函数。

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

## 使用自定义用户定义的函数

您可以选择在请求中添加自定义用户定义的函数，以扩展模型的功能。以下示例通过添加 `open_app`、`long_press_at` 和 `go_home` 等自定义用户定义的操作，同时排除特定于浏览器的操作，使计算机使用模型和工具适应移动用例。模型可以智能地调用这些自定义函数以及标准界面操作，以便在非浏览器环境中完成任务。

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

## 支持的界面操作

模型可以通过 `FunctionCall` 请求以下界面操作。您的客户端代码必须实现这些操作的执行逻辑。如需查看示例，请参阅[参考
实现](https://github.com/google/computer-use-preview)。

| 命令名称 | 说明 | 参数（在函数调用中） | 函数调用示例 |
| --- | --- | --- | --- |
| **open\_web\_browser** | 打开网络浏览器。 | 无 | `{"name": "open_web_browser", "args": {}}` |
| **wait\_5\_seconds** | 暂停执行 5 秒，以便加载动态内容或完成动画。 | 无 | `{"name": "wait_5_seconds", "args": {}}` |
| **go\_back** | 前往浏览器历史记录中的上一页。 | 无 | `{"name": "go_back", "args": {}}` |
| **go\_forward** | 前往浏览器历史记录中的下一页。 | 无 | `{"name": "go_forward", "args": {}}` |
| **search** | 前往默认搜索引擎的主页（例如 Google）。适用于开始新的搜索任务。 | 无 | `{"name": "search", "args": {}}` |
| **navigate** | 将浏览器直接导航到指定的网址。 | `url`：str | `{"name": "navigate", "args": {"url": "https://www.wikipedia.org"}}` |
| **click\_at** | 点击网页上的特定坐标。x 和 y 值基于 1000x1000 网格，并缩放为屏幕尺寸。 | `y`：int (0-999)，`x`：int (0-999) | `{"name": "click_at", "args": {"y": 300, "x": 500}}` |
| **hover\_at** | 将鼠标悬停在网页上的特定坐标。适用于显示子菜单。x 和 y 基于 1000x1000 网格。 | `y`：int (0-999)，`x`：int (0-999) | `{"name": "hover_at", "args": {"y": 150, "x": 250}}` |
| **type\_text\_at** | 在特定坐标处输入文字，默认情况下先清除字段，然后在输入后按 Enter 键，但可以停用这些操作。x 和 y 基于 1000x1000 网格。 | `y`：int (0-999)，`x`：int (0-999)，`text`：str，`press_enter`：bool（可选，默认值为 True），`clear_before_typing`：bool（可选，默认值为 True） | `{"name": "type_text_at", "args": {"y": 250, "x": 400, "text": "search query", "press_enter": false}}` |
| **key\_combination** | 按键盘键或组合键，例如“Control+C”或“Enter”。适用于触发操作（例如使用“Enter”提交表单）或剪贴板操作。 | `keys`：str（例如“enter”“control+c”）。 | `{"name": "key_combination", "args": {"keys": "Control+A"}}` |
| **scroll\_document** | 将整个网页“向上”“向下”“向左”或“向右”滚动。 | `direction`：str（“up”“down”“left”或“right”） | `{"name": "scroll_document", "args": {"direction": "down"}}` |
| **scroll\_at** | 按指定方向将坐标 (x, y) 处的特定元素或区域滚动一定的幅度。坐标和幅度（默认值为 800）基于 1000x1000 网格。 | `y`：int (0-999)，`x`：int (0-999)，`direction`：str（“up”“down”“left”“right”），`magnitude`：int (0-999，可选，默认值为 800） | `{"name": "scroll_at", "args": {"y": 500, "x": 500, "direction": "down", "magnitude": 400}}` |
| **drag\_and\_drop** | 从起始坐标 (x, y) 拖动元素，并将其放置在目标坐标 (destination\_x, destination\_y) 处。所有坐标均基于 1000x1000 网格。 | `y`：int (0-999)，`x`：int (0-999)，`destination_y`：int (0-999)，`destination_x`：int (0-999) | `{"name": "drag_and_drop", "args": {"y": 100, "x": 100, "destination_y": 500, "destination_x": 500}}` |

## 安全

### 确认安全决策

根据操作的不同，模型响应还可能包含来自内部安全系统的 `safety_decision`，该系统会检查模型建议的操作。

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

如果 `safety_decision` 为 `require_confirmation`，您必须先要求最终用户确认，然后才能继续执行操作。根据
[服务条款](https://ai.google.dev/gemini-api/terms?hl=zh-cn)，您不得
绕过人工确认请求。

此代码示例会在执行操作之前提示最终用户进行确认。如果用户未确认操作，循环将终止。如果用户确认操作，则会执行该操作，并将 `safety_acknowledgement` 字段标记为 `True`。

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

如果用户确认，您必须在 `FunctionResponse` 中添加安全确认。

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

### 有关安全的最佳实践

计算机使用是一种新颖的工具，会带来新的风险，开发者应注意这些风险：

- **不受信任的内容和欺骗手段** ：当模型尝试实现用户的目标时，可能会依赖于屏幕上不受信任的信息来源和说明。例如，如果用户的目标是购买 Pixel 手机，而模型遇到“完成调查即可免费获得 Pixel”诈骗，则模型有可能会完成调查。
- **偶尔出现意外操作** ：模型可能会误解用户的目标或网页内容，导致其执行错误的操作，例如点击错误的按钮或填写错误的表单。这可能会导致任务失败或数据渗漏。
- **违反政策**：API 的功能可能会有意或无意地指向违反 Google 政策（[《生成式 AI 使用限制政策》](https://policies.google.com/terms/generative-ai/use-policy?hl=zh-cn)和[《Gemini API 附加服务条款》](https://ai.google.dev/gemini-api/terms?hl=zh-cn)）的活动。这包括可能会干扰系统完整性、损害安全性、绕过安全措施、控制医疗设备等的操作。

如需应对这些风险，您可以实现以下安全措施和最佳实践：

1. **人机协同 (HITL)** ：

   - **实现用户确认** ：当安全响应指示 `require_confirmation` 时，您必须先实现用户确认，然后才能执行。如需查看[示例代码](#safety-decisions)，请参阅
     确认安全决策。
   - **提供自定义安全说明**：除了内置的用户
     确认检查之外，开发者还可以选择添加自定义[系统
     说明](https://ai.google.dev/gemini-api/docs/text-generation?hl=zh-cn#system-instructions)
     ，以强制执行自己的安全政策，从而阻止某些模型
     操作或要求用户在模型执行某些
     高风险的不可逆操作之前进行确认。以下是您在与模型互动时可以添加的自定义安全系统说明的示例。

     #### 安全说明示例

     将自定义安全规则设置为系统说明：

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
2. **安全执行环境**：在安全的沙盒化
   环境中运行代理，以限制其潜在影响（例如，沙盒化虚拟机
   (VM)、容器（例如 Docker）或具有有限
   权限的专用浏览器配置文件）。
3. **输入清理** ：清理提示中的所有用户生成文本，以降低意外说明或提示注入的风险。这是一个有用的安全层，但不能替代安全执行环境。
4. **内容护栏**：使用护栏和[内容安全
   API](https://ai.google.dev/gemma/docs/shieldgemma?hl=zh-cn)来评估用户输入、
   工具输入和输出、代理响应的适当性、提示
   注入和越狱检测。
5. **许可名单和屏蔽名单** ：实现过滤机制，以控制模型可以导航到的位置以及可以执行的操作。禁止网站的屏蔽名单是一个不错的起点，而限制性更强的许可名单则更加安全。
6. **可观测性和日志记录** ：维护详细的日志，以进行调试、审核和突发事件响应。您的客户端应记录提示、屏幕截图、模型建议的操作 (function\_call)、安全响应以及客户端最终执行的所有操作。
7. **环境管理** ：确保 GUI 环境一致。
   意外的弹出式窗口、通知或布局更改可能会让模型感到困惑。如果可能，请从每个新任务的已知干净状态开始。

## 模型版本

请注意，`gemini-3-flash-preview` 内置了对计算机使用的支持；您无需单独的模型即可访问该工具。

| 属性 | 说明 |
| --- | --- |
| id\_card模型代码 | **Gemini API**  `gemini-2.5-computer-use-preview-10-2025` |
| save支持的数据类型 | **输入**  图片、文字  **输出**  文字 |
| token\_auto | **输入令牌限制**  128,000  **输出令牌限制**  64,000 |
| 123版本 | 如需了解详情，请参阅[模型版本模式](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-cn#model-versions)。  - 预览版：`gemini-2.5-computer-use-preview-10-2025` |
| calendar\_month上次更新时间 | 2025 年 10 月 |

## 后续步骤

- 在 [Browserbase 演示
  环境](http://gemini.browserbase.com)中试用计算机使用。
- 查看[参考
  实现](https://github.com/google/computer-use-preview)以获取示例
  代码。
- 了解其他 Gemini API 工具：
  - [函数调用](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-cn)
  - [依托 Google 搜索进行接地](https://ai.google.dev/gemini-api/docs/grounding?hl=zh-cn)

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-05-07。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-05-07。"],[],[]]
