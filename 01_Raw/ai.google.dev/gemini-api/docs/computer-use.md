---
source_url: https://ai.google.dev/gemini-api/docs/computer-use?hl=zh-CN
fetched_at: 2026-10-26T05:43:50.925834+00:00
title: "\u4f7f\u7528\u7535\u8111 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon 现已上架。[试试看](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=zh-cn)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 使用电脑

借助 Computer Use 工具，您可以构建浏览器、移动设备和桌面设备控制智能体，以便与任务进行交互并自动执行任务。通过屏幕截图，模型可以“看到”计算机屏幕，并通过生成特定的界面操作（例如鼠标点击和键盘输入）来“执行操作”。与函数调用类似，您需要实现客户端执行环境，以接收和执行“计算机使用”操作。

如需查看支持的模型列表，请参阅[模型版本](#model-versions)。Gemini 4 和 Gemini 3.x 模型支持多项高级功能：

- **多环境支持**：为[浏览器、移动设备和桌面设备](#supported-environments)环境构建智能体。
- **通过 intent 简化操作**：操作包含一个 `intent` 字段，用于解释模型在每个步骤背后的推理。
- **可配置的安全政策**：使用内置政策类别和替换项微调[安全行为](#safety-policies)。
- **提示注入检测**：选择启用[屏幕截图扫描](#prompt-injection)，以检测隐藏的对抗性指令。

借助 Computer Use，您可以构建能够执行以下操作的智能体：

- 自动执行网站上的重复性数据录入或表单填写。
- 对 Web 应用和用户体验流程执行自动化测试
- 在各种网站上进行研究（例如，从电子商务网站收集商品信息、价格和评价，以便做出购买决策）

以下是一个最小示例，展示了如何在浏览器环境中初始化客户端并向启用了 `computer_use` 工具的模型发送提示：

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
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
  model: 'gemini-3.8-flash',
  input: "Search for 'Gemini API' on Google.",
  tools: [{ type: "computer_use", environment: "browser" }]
});

console.log(interaction);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.ComputerUse;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.EnvironmentEnum;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model("gemini-3.8-flash")
        .input(InteractionsInput.of("Search for 'Gemini API' on Google."))
        .tools(
            Arrays.asList(
                ComputerUse.builder().environment(EnvironmentEnum.BROWSER).build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction);
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Search for 'Gemini API' on Google."),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.ComputerUse{
                    Environment: interactions.EnvironmentEnumBrowser.ToPointer(),
                }),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(res.Interaction)
}
```

## “计算机使用”功能的运作方式

如需使用 Computer Use 模型构建智能体，您需要在应用和 API 之间设置一个持续循环。以下是代码在每个步骤中的执行操作：

1. [**向模型发送请求**](#send-request)
   - 您的应用发送一个 API 请求，其中包含计算机使用工具、您的配置设置（例如目标环境）、用户提示以及当前屏幕的屏幕截图。
2. [**接收模型回答**](#model-response)
   - 模型会分析屏幕和提示，并返回一个回答，其中包含表示界面操作（例如点击、滚动或按键）的建议 `function_call`。
   - 对于 **Gemini 4 和 Gemini 3.x 模型**，响应还包含一个推理 `intent`，用于解释模型为何选择该操作。
   - 响应还可能包含来自内部安全系统的 `safety_decision`，该系统会将操作分类为常规/允许、`require_confirmation`（需要用户批准）或已屏蔽。
3. [**执行收到的操作**](#execute-actions)
   - 如果操作被允许（或用户确认了操作），您的客户端代码会解析 `function_call`，缩放归一化坐标以匹配视口，并使用自动化工具（例如 Playwright）在目标环境中执行操作。如果操作被屏蔽，您的客户端应停止执行或处理中断。
4. [**捕获新环境状态**](#capture-state)
   - 操作执行完毕后，应用会截取新的屏幕截图，并在 `function_result` 中将其发送回模型，以请求执行下一步。

然后，此过程会从第 2 步开始重复，不断向模型请求下一个操作，直到任务完成或终止。

![计算机使用概览](https://ai.google.dev/static/gemini-api/docs/images/computer_use.png?hl=zh-cn)

## 如何实现“操作电脑”功能

在使用计算机使用工具进行构建之前，您需要设置：

- **安全执行环境**：在沙盒化虚拟机或容器中运行智能体，使其与主机系统隔离，并限制其潜在影响。[参考实现](https://github.com/google/computer-use-preview/)包含一个基于 Docker 的即用型沙盒，供您参考。
- **客户端操作处理程序**：实现客户端逻辑，以执行坐标、输入文本和截取屏幕截图。

以下示例使用网络浏览器作为执行环境，并使用 [Playwright](https://playwright.dev/) 作为客户端处理程序。

### 0. 设置 Playwright

首先，安装所需的软件包：

```
pip install google-genai playwright
playwright install chromium
```

然后，初始化一个 Playwright 浏览器实例，用于执行：

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

### 1. 向模型发送请求

初始化客户端库并配置“计算机使用”工具。请注意，发出请求时无需指定显示大小；模型会预测按屏幕高度和宽度缩放的像素坐标。

### Python

使用 `google-genai` Python SDK（`2.7.0` 或更高版本）配置针对浏览器环境的请求：

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model='gemini-3.8-flash',
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

使用 `@google/genai` Node.js SDK 配置针对浏览器环境的请求：

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI();

const interaction = await ai.interactions.create({
  model: 'gemini-3.8-flash',
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

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.ComputerUse;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.EnvironmentEnum;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model("gemini-3.8-flash")
        .input(
            InteractionsInput.of(
                "Find a flight from SF to Hawaii on Jun 30th, coming back on Jul 6th"))
        .tools(
            Arrays.asList(
                ComputerUse.builder()
                    .environment(EnvironmentEnum.BROWSER)
                    .enablePromptInjectionDetection(true)
                    .build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction);
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Find a flight from SF to Hawaii on Jun 30th, coming back on Jul 6th"),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.ComputerUse{
                    Environment:                    interactions.EnvironmentEnumBrowser.ToPointer(),
                    EnablePromptInjectionDetection: genai.Ptr(true),
                }),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(res.Interaction)
}
```

### REST

使用 curl 发送请求：

```
curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash",
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

### 2. 接收模型回答

模型回答会建议一个函数调用，其中包含坐标和解释该操作的定制推理意图：

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

### 3. 执行收到的操作

应用必须解析响应坐标，将其从归一化的 1000x1000 坐标进行缩放，然后执行操作：

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
            if fname == "open_app":
                pass # Handled / already open
            elif fname in ("click", "double_click", "triple_click", "middle_click", "right_click", "move", "long_press"):
                actual_x = denormalize_x(args["x"], screen_width)
                actual_y = denormalize_y(args["y"], screen_height)

                if fname == "click":
                    page.mouse.click(actual_x, actual_y)
                elif fname == "double_click":
                    page.mouse.dblclick(actual_x, actual_y)
                elif fname == "right_click":
                    page.mouse.click(actual_x, actual_y, button="right")
                elif fname == "middle_click":
                    page.mouse.click(actual_x, actual_y, button="middle")
                elif fname == "move":
                    page.mouse.move(actual_x, actual_y)
            elif fname == "type":
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
            if (fname === "open_app") {
                // Handled / already open
            } else if (["click", "double_click", "triple_click", "middle_click", "right_click", "move", "long_press"].includes(fname)) {
                const actualX = denormalizeX(args.x, screenWidth);
                const actualY = denormalizeY(args.y, screenHeight);

                if (fname === "click") {
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
            } else if (fname === "type") {
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

### Java

```
import com.google.genai.gaos.models.interactions.FunctionCallStep;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.Step;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class ActionExecutor {
  int denormalizeX(int x, int screenWidth) {
    return (int) (x / 1000.0 * screenWidth);
  }

  int denormalizeY(int y, int screenHeight) {
    return (int) (y / 1000.0 * screenHeight);
  }

  List<Map<String, Object>> executeFunctionCalls(
      Interaction interaction, int screenWidth, int screenHeight) {
    List<Map<String, Object>> results = new ArrayList<>();

    for (Step step : interaction.steps().orElse(Collections.emptyList())) {
      if (step instanceof FunctionCallStep) {
        FunctionCallStep functionCall = (FunctionCallStep) step;
        String fname = functionCall.name().orElse("");
        Map<String, Object> args = functionCall.arguments().orElse(Collections.emptyMap());
        Map<String, Object> actionResult = new HashMap<>();

        System.out.println(
            "  -> Executing: " + fname + " (Intent: " + args.getOrDefault("intent", "N/A") + ")");

        try {
          if (fname.equals("click")) {
            int actualX = denormalizeX(((Number) args.get("x")).intValue(), screenWidth);
            int actualY = denormalizeY(((Number) args.get("y")).intValue(), screenHeight);
            // Perform mouse click at (actualX, actualY) using your browser automation library
          } else if (fname.equals("type")) {
            String text = (String) args.get("text");
            // Type text into active element using your browser automation library
          } else if (fname.equals("navigate")) {
            String url = (String) args.get("url");
            // Navigate browser to url
          }
        } catch (Exception e) {
          actionResult.put("error", e.getMessage());
        }

        Map<String, Object> entry = new HashMap<>();
        entry.put("name", fname);
        entry.put("callId", functionCall.id().orElse(""));
        entry.put("result", actionResult);
        results.add(entry);
      }
    }
    return results;
  }
}
```

### Go

```
package main

import (
    "fmt"

    "google.golang.org/genai/interactions/models/interactions"
)

func denormalizeX(x, screenWidth int) int {
    return int(float64(x) / 1000.0 * float64(screenWidth))
}

func denormalizeY(y, screenHeight int) int {
    return int(float64(y) / 1000.0 * float64(screenHeight))
}

func executeFunctionCalls(interaction *interactions.Interaction, screenWidth, screenHeight int) []map[string]any {
    var results []map[string]any

    for _, step := range interaction.Steps {
        if functionCall := step.FunctionCallStep; functionCall != nil {
            fname := functionCall.Name
            args := functionCall.Arguments
            actionResult := map[string]any{}

            intent := args["intent"]
            if intent == nil {
                intent = "N/A"
            }
            fmt.Printf("  -> Executing: %s (Intent: %v)\n", fname, intent)

            switch fname {
            case "click":
                xVal, _ := args["x"].(float64)
                yVal, _ := args["y"].(float64)
                actualX := denormalizeX(int(xVal), screenWidth)
                actualY := denormalizeY(int(yVal), screenHeight)
                _ = actualX
                _ = actualY
                // Perform mouse click at (actualX, actualY) using your browser automation library
            case "type":
                text, _ := args["text"].(string)
                _ = text
                // Type text into active element using your browser automation library
            case "navigate":
                url, _ := args["url"].(string)
                _ = url
                // Navigate browser to url
            }

            results = append(results, map[string]any{
                "name":   fname,
                "callId": functionCall.ID,
                "result": actionResult,
            })
        }
    }
    return results
}

func main() {
    // Example helper usage with an Interaction response
}
```

### 4. 捕获新环境状态

执行操作后，将函数执行结果发送回模型，以便模型可以使用此信息生成下一个操作。如果执行了多项操作（并行调用），则必须在后续用户轮次中为每项操作发送一个 `function_result`。

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

### Java

```
import com.google.genai.gaos.models.interactions.FunctionResultStep;
import com.google.genai.gaos.models.interactions.FunctionResultStepResultUnion;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Base64;
import java.util.List;
import java.util.Map;

class StateCapturer {
  List<Step> getFunctionResponses(
      byte[] screenshotBytes, String currentUrl, List<Map<String, Object>> results) {
    List<Step> functionResponses = new ArrayList<>();
    String base64Screenshot = Base64.getEncoder().encodeToString(screenshotBytes);

    for (Map<String, Object> entry : results) {
      String name = (String) entry.get("name");
      String callId = (String) entry.get("callId");
      String jsonResult = String.format("{\"url\": \"%s\"}", currentUrl);

      FunctionResultStep responseStep =
          FunctionResultStep.builder()
              .name(name)
              .callId(callId)
              .result(
                  FunctionResultStepResultUnion.of(
                      Arrays.asList(
                          TextContent.builder().text(jsonResult).build(),
                          ImageContent.builder()
                              .data(base64Screenshot)
                              .mimeType(ImageContentMimeType.IMAGE_PNG)
                              .build())))
              .build();
      functionResponses.add(responseStep);
    }
    return functionResponses;
  }
}
```

### Go

```
package main

import (
    "encoding/base64"
    "fmt"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
)

func getFunctionResponses(screenshotBytes []byte, currentURL string, results []map[string]any) []interactions.Step {
    var functionResponses []interactions.Step
    base64Screenshot := base64.StdEncoding.EncodeToString(screenshotBytes)

    for _, entry := range results {
        name, _ := entry["name"].(string)
        callID, _ := entry["callId"].(string)
        jsonResult := fmt.Sprintf(`{"url": "%s"}`, currentURL)

        responseStep := interactions.NewStep(interactions.FunctionResultStep{
            Name:   genai.Ptr(name),
            CallID: callID,
            Result: interactions.NewFunctionResultStepResultUnion([]interactions.FunctionResultSubcontent{
                interactions.NewFunctionResultSubcontent(interactions.TextContent{
                    Text: jsonResult,
                }),
                interactions.NewFunctionResultSubcontent(interactions.ImageContent{
                    Data:     genai.Ptr(base64Screenshot),
                    MimeType: interactions.ImageContentMimeType("image/png").ToPointer(),
                }),
            }),
        })
        functionResponses = append(functionResponses, responseStep)
    }
    return functionResponses
}

func main() {
    // Example helper usage to build FunctionResultStep responses
}
```

定义如何捕获环境状态并设置其格式后，您可以将所有这些步骤组合成一个持续执行循环。

## 构建智能体循环

如需实现多步互动，请将[如何实现 Computer Use](#implement-computer-use) 部分中的四个步骤合并为一个循环。此循环会持续请求操作并将结果反馈给模型，直到任务完成。

请务必在每个步骤中将模型回答和函数回答都附加到对话记录中，以便正确管理对话记录。

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
        model='gemini-3.8-flash',
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
            model='gemini-3.8-flash',
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
        model: 'gemini-3.8-flash',
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
            model: 'gemini-3.8-flash',
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

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.ComputerUse;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.EnvironmentEnum;
import com.google.genai.gaos.models.interactions.FunctionCallStep;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Base64;
import java.util.Collections;
import java.util.List;

Client client = new Client();

// Constants for screen dimensions
int screenWidth = 1440;
int screenHeight = 900;

// Capture initial screenshot from browser driver (e.g. Playwright)
byte[] initialScreenshot = new byte[0];
String base64Screenshot = Base64.getEncoder().encodeToString(initialScreenshot);
String userPrompt = "Go to ai.google.dev/gemini-api/docs and search for pricing.";
System.out.println("Goal: " + userPrompt);

ComputerUse computerUseTool =
    ComputerUse.builder()
        .environment(EnvironmentEnum.BROWSER)
        .enablePromptInjectionDetection(true)
        .build();

CreateModelInteraction initialParams =
    CreateModelInteraction.builder()
        .model("gemini-3.8-flash")
        .input(
            InteractionsInput.ofContent(
                Arrays.asList(
                    TextContent.builder().text(userPrompt).build(),
                    ImageContent.builder()
                        .data(base64Screenshot)
                        .mimeType(ImageContentMimeType.IMAGE_PNG)
                        .build())))
        .tools(Arrays.asList(computerUseTool))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(initialParams)).interaction().get();

int turnLimit = 5;
for (int i = 0; i < turnLimit; i++) {
  System.out.println("\n--- Turn " + (i + 1) + " ---");

  boolean hasFunctionCalls =
      interaction.steps().orElse(Collections.emptyList()).stream()
          .anyMatch(step -> step instanceof FunctionCallStep);

  if (!hasFunctionCalls) {
    StringBuilder textResponse = new StringBuilder();
    for (Step step : interaction.steps().orElse(Collections.emptyList())) {
      if (step instanceof ModelOutputStep) {
        for (Content contentBlock :
            ((ModelOutputStep) step).content().orElse(Collections.emptyList())) {
          if (contentBlock instanceof TextContent) {
            textResponse.append(((TextContent) contentBlock).text().orElse("")).append(" ");
          }
        }
      }
    }
    System.out.println("Agent finished: " + textResponse.toString().trim());
    break;
  }

  System.out.println("Executing actions and capturing state...");
  // Execute function calls against browser driver and capture List<Step> functionResponses
  List<Step> functionResponses = new ArrayList<>();

  CreateModelInteraction nextParams =
      CreateModelInteraction.builder()
          .model("gemini-3.8-flash")
          .previousInteractionId(interaction.id().get())
          .input(InteractionsInput.ofStep(functionResponses))
          .tools(Arrays.asList(computerUseTool))
          .build();

  interaction =
      client.interactions.create(CreateInteractionRequestBody.of(nextParams)).interaction().get();
}
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
    "fmt"
    "log"
    "strings"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    // Constants for screen dimensions
    screenWidth := 1440
    screenHeight := 900
    _ = screenWidth
    _ = screenHeight

    // Capture initial screenshot from browser driver (e.g. Playwright)
    initialScreenshot := []byte{}
    base64Screenshot := base64.StdEncoding.EncodeToString(initialScreenshot)
    userPrompt := "Go to ai.google.dev/gemini-api/docs and search for pricing."
    fmt.Println("Goal:", userPrompt)

    computerUseTool := interactions.NewTool(interactions.ComputerUse{
        Environment:                    interactions.EnvironmentEnumBrowser.ToPointer(),
        EnablePromptInjectionDetection: genai.Ptr(true),
    })

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.TextContent{Text: userPrompt}),
                interactions.NewContent(interactions.ImageContent{
                    Data:     genai.Ptr(base64Screenshot),
                    MimeType: interactions.ImageContentMimeType("image/png").ToPointer(),
                }),
            }),
            Tools: []interactions.Tool{computerUseTool},
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    interaction := res.Interaction

    turnLimit := 5
    for i := 0; i < turnLimit; i++ {
        fmt.Printf("\n--- Turn %d ---\n", i+1)

        hasFunctionCalls := false
        for _, step := range interaction.Steps {
            if step.FunctionCallStep != nil {
                hasFunctionCalls = true
                break
            }
        }

        if !hasFunctionCalls {
            var parts []string
            for _, step := range interaction.Steps {
                if outStep := step.ModelOutputStep; outStep != nil {
                    for _, contentBlock := range outStep.Content {
                        if textContent := contentBlock.TextContent; textContent != nil {
                            parts = append(parts, textContent.GetText())
                        }
                    }
                }
            }
            fmt.Println("Agent finished:", strings.TrimSpace(strings.Join(parts, " ")))
            break
        }

        fmt.Println("Executing actions and capturing state...")
        // Execute function calls against browser driver and capture []interactions.Step functionResponses
        var functionResponses []interactions.Step

        nextRes, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
            Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
                Model:                 interactions.Model("gemini-3.8-flash"),
                PreviousInteractionID: interaction.ID,
                Input:                 interactions.NewInteractionsInput(functionResponses),
                Tools:                 []interactions.Tool{computerUseTool},
            }),
        })
        if err != nil {
            log.Fatal(err)
        }
        interaction = nextRes.Interaction
    }
}
```

## 受支持的环境

Gemini 4 和 Gemini 3.x 模型支持 `computer_use` 配置中指定的三个环境：

### 浏览器环境 (`ENVIRONMENT_BROWSER`)

浏览器工具下的可用操作：

| 命令名称 | 说明 | 参数（在函数调用中） |
| --- | --- | --- |
| **click** | 在坐标处左键点击。 | `y`：int (0-999) `x`：int (0-999) `intent`：str |
| **double\_click** | 双击坐标。 | `y`：int (0-999) `x`：int (0-999) `intent`：str |
| **triple\_click** | 在坐标处三击。 | `y`：int (0-999) `x`：int (0-999) `intent`：str |
| **middle\_click** | 在坐标处点击鼠标中键。 | `y`：int (0-999) `x`：int (0-999) `intent`：str |
| **right\_click** | 右键点击坐标。 | `y`：int (0-999) `x`：int (0-999) `intent`：str |
| **mouse\_down** | 在相应坐标处按住鼠标按键。 | `y`：int (0-999) `x`：int (0-999) `intent`：str |
| **mouse\_up** | 在指定坐标处松开鼠标按键。 | `y`：int (0-999) `x`：int (0-999) `intent`：str |
| **move** | 将光标移至指定位置。 | `y`：int (0-999) `x`：int (0-999) `intent`：str |
| **type** | 输入文字。 | `text`：str `press_enter`：bool（可选，默认值为 `false`） `intent`：str |
| **drag\_and\_drop** | 将某个项从起始坐标拖动到结束坐标。 | `start_y`：int (0-999) `start_x`：int (0-999) `end_y`：int (0-999) `end_x`：int (0-999) `intent`：str |
| **wait** | 暂停执行指定的秒数。 | `seconds`：int（可选，默认值为 `1`） `intent`：str |
| **press\_key** | 按下并松开指定按键。 | `key`：str `intent`：str |
| **key\_down** | 按住指定键。 | `key`：str `intent`：str |
| **key\_up** | 释放指定的键。 | `key`：str `intent`：str |
| **hotkey** | 按下指定的组合键。 | `keys`：`List[str]` `intent`：`str` |
| **take\_screenshot** | 返回当前屏幕的屏幕截图。 | `intent`：str |
| **scroll** | 在某个坐标处向上、向下、向左或向右滚动一定像素距离。 | `y`：int (0-999) `x`：int (0-999) `direction`：str（`"up"`、`"down"`、`"left"`、`"right"`） `magnitude_in_pixels`：int（0-999，可选，默认值为 `300`） `intent`：str |
| **go\_back** | 返回浏览器历史记录中的上一个网页。 | `intent`：str |
| **navigate** | 直接导航到指定网址。 | `url`：str `intent`：str |
| **go\_forward** | 在浏览器历史记录中前进到下一个网页。 | `intent`：str |

### 移动环境 (`ENVIRONMENT_MOBILE`)

针对 Android 优化的环境操作：

| 命令名称 | 说明 | 参数（在函数调用中） |
| --- | --- | --- |
| **open\_app** | 按名称打开应用。 | `app_name`：str `intent`：str |
| **click** | 在坐标处左键点击。 | `y`：int (0-999) `x`：int (0-999) `intent`：str |
| **list\_apps** | 列出设备上的可用应用，并返回其名称和软件包名称。 | `intent`：str |
| **wait** | 暂停执行指定的秒数。 | `seconds`：int（可选，默认值为 `1`） `intent`：str |
| **go\_back** | 返回上一个屏幕或网页。 | `intent`：str |
| **type** | 输入文字。 | `text`：str `press_enter`：bool（可选，默认值为 `false`） `intent`：str |
| **drag\_and\_drop** | 将某个项从起始坐标拖动到结束坐标。 | `start_y`：int (0-999) `start_x`：int (0-999) `end_y`：int (0-999) `end_x`：int (0-999) `intent`：str |
| **long\_press** | 在屏幕上的某个坐标处执行长按操作。 | `y`：int (0-999) `x`：int (0-999) `seconds`：int（可选，默认值为 `2`） `intent`：str |
| **press\_key** | 按下并松开指定按键。 | `key`：str `intent`：str |
| **take\_screenshot** | 返回当前屏幕的屏幕截图。 | `intent`：str |

### 桌面环境 (`ENVIRONMENT_DESKTOP`)

桌面环境操作系统级光标命令：

| 命令名称 | 说明 | 参数（在函数调用中） |
| --- | --- | --- |
| **click** | 在坐标处左键点击。 | `y`：int (0-999) `x`：int (0-999) `intent`：str |
| **double\_click** | 双击坐标。 | `y`：int (0-999) `x`：int (0-999) `intent`：str |
| **triple\_click** | 在坐标处三击。 | `y`：int (0-999) `x`：int (0-999) `intent`：str |
| **middle\_click** | 在坐标处点击鼠标中键。 | `y`：int (0-999) `x`：int (0-999) `intent`：str |
| **right\_click** | 右键点击坐标。 | `y`：int (0-999) `x`：int (0-999) `intent`：str |
| **mouse\_down** | 在相应坐标处按住鼠标按键。 | `y`：int (0-999) `x`：int (0-999) `intent`：str |
| **mouse\_up** | 在指定坐标处松开鼠标按键。 | `y`：int (0-999) `x`：int (0-999) `intent`：str |
| **move** | 将光标移至指定位置。 | `y`：int (0-999) `x`：int (0-999) `intent`：str |
| **type** | 输入文字。 | `text`：str `press_enter`：bool（可选，默认值为 `false`） `intent`：str |
| **drag\_and\_drop** | 将某个项从起始坐标拖动到结束坐标。 | `start_y`：int (0-999) `start_x`：int (0-999) `end_y`：int (0-999) `end_x`：int (0-999) `intent`：str |
| **wait** | 暂停执行指定的秒数。 | `seconds`：int（可选，默认值为 `1`） `intent`：str |
| **press\_key** | 按下并松开指定按键。 | `key`：str `intent`：str |
| **key\_down** | 按住指定键。 | `key`：str `intent`：str |
| **key\_up** | 释放指定的键。 | `key`：str `intent`：str |
| **hotkey** | 按下指定的组合键。 | `keys`：`List[str]` `intent`：`str` |
| **take\_screenshot** | 返回当前屏幕的屏幕截图。 | `intent`：str |
| **scroll** | 在某个坐标处向上、向下、向左或向右滚动一定像素距离。 | `y`：int (0-999) `x`：int (0-999) `direction`：str（`"up"`、`"down"`、`"left"`、`"right"`） `magnitude_in_pixels`：int（0-999，可选，默认值为 `300`） `intent`：str |

## 自定义用户定义的函数

您可以通过添加自定义的用户定义的函数来扩展模型的功能。例如，在人机协同 (HITL) 场景中，您可以排除默认的预定义操作并注册自定义操作。

### Python

排除标准预定义浏览器操作（例如 `click`），并注册自定义 `yield_to_user` 工具：

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
    model="gemini-3.8-flash",
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

排除标准预定义浏览器操作（例如 `click`），并注册自定义 `yield_to_user` 工具：

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
    model: "gemini-3.8-flash",
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

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.ComputerUse;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.EnvironmentEnum;
import com.google.genai.gaos.models.interactions.Function;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

Client client = new Client();

Map<String, Object> reasonProp = new HashMap<>();
reasonProp.put("type", "string");
reasonProp.put("description", "The reason why the agent is yielding control to the human.");

Map<String, Object> properties = new HashMap<>();
properties.put("reason", reasonProp);

Map<String, Object> parameters = new HashMap<>();
parameters.put("type", "object");
parameters.put("properties", properties);
parameters.put("required", Collections.singletonList("reason"));

Function yieldToUserTool =
    Function.builder()
        .name("yield_to_user")
        .description(
            "Yields control back to the user for assistance or verification when an automated action is unsafe or ambiguous.")
        .parameters(parameters)
        .build();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model("gemini-3.8-flash")
        .input(
            InteractionsInput.of(
                "Click the submit button. If you need a second factor authentication code, ask me."))
        .tools(
            Arrays.asList(
                ComputerUse.builder()
                    .environment(EnvironmentEnum.MOBILE)
                    .excludedPredefinedFunctions(Arrays.asList("click"))
                    .build(),
                yieldToUserTool))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### Go

```
package main

import (
    "context"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    yieldToUserTool := interactions.NewTool(interactions.Function{
        Name:        genai.Ptr("yield_to_user"),
        Description: genai.Ptr("Yields control back to the user for assistance or verification when an automated action is unsafe or ambiguous."),
        Parameters: map[string]any{
            "type": "object",
            "properties": map[string]any{
                "reason": map[string]any{
                    "type":        "string",
                    "description": "The reason why the agent is yielding control to the human.",
                },
            },
            "required": []string{"reason"},
        },
    })

    _, err = client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Click the submit button. If you need a second factor authentication code, ask me."),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.ComputerUse{
                    Environment:                 interactions.EnvironmentEnumMobile.ToPointer(),
                    ExcludedPredefinedFunctions: []string{"click"},
                }),
                yieldToUserTool,
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
}
```

## 管理思考等级

对于计算机使用代理，您可以配置不同的思考级别，以平衡操作质量和执行速度。较低的思考级别通常可以在标准自动化任务中实现良好的平衡。

## 安全

### 配置安全政策

Gemini 4 和 Gemini 3.x 模型包含内置的安全服务类别，有助于确定是否需要用户确认。

| 安全政策类别 | 说明 |
| --- | --- |
| `FINANCIAL_TRANSACTIONS` | 屏蔽或触发涉及付款、零售结账或管制商品的操作的确认。 |
| `SENSITIVE_DATA_MODIFICATION` | 保护健康、财务或政府记录免遭未经授权的修改。 |
| `COMMUNICATION_TOOL` | 限制代理自主发送邮件、聊天消息或草稿。 |
| `ACCOUNT_CREATION` | 限制代理在网站上自主注册新账号。 |
| `DATA_MODIFICATION` | 管理整体文件系统修改、数据共享和存储空间删除。 |
| `USER_CONSENT_MANAGEMENT` | 需要用户接管 Cookie 意见征求横幅和隐私权提示。 |
| `LEGAL_TERMS_AND_AGREEMENTS` | 防止模型自主接受服务条款或具有法律约束力的合同。 |

#### 安全替换

您可以通过传递替换项来替换所选政策：

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
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
    model: "gemini-3.8-flash",
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

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.ComputerUse;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.DisabledSafetyPolicy;
import com.google.genai.gaos.models.interactions.EnvironmentEnum;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model("gemini-3.8-flash")
        .input(InteractionsInput.of("Clean up the local folder by archiving old logs."))
        .tools(
            Arrays.asList(
                ComputerUse.builder()
                    .environment(EnvironmentEnum.DESKTOP)
                    .disabledSafetyPolicies(
                        Arrays.asList(DisabledSafetyPolicy.DATA_MODIFICATION))
                    .build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### Go

```
package main

import (
    "context"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    _, err = client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Clean up the local folder by archiving old logs."),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.ComputerUse{
                    Environment: interactions.EnvironmentEnumDesktop.ToPointer(),
                    DisabledSafetyPolicies: []interactions.DisabledSafetyPolicy{
                        interactions.DisabledSafetyPolicyDataModification,
                    },
                }),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
}
```

### 提示注入检测

Gemini 3.5 Flash-Lite 或更高版本的 Computer Use 支持高级安全机制，可检测提示注入攻击。启用后，此功能会检查添加的屏幕截图是否包含隐藏的对抗性指令（例如“忽略之前的命令”），并在检测到此类指令时阻止执行。

提示注入检测是一项由用户自主选择启用的功能。默认值为 `false`。

以下示例演示了如何在“计算机使用”工具配置中启用提示注入检测：

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Search for flight deals and summarize top results.",
    tools=[
        {
            "type": "computer_use",
            "environment": "desktop",
            "enable_prompt_injection_detection": True,
        }
    ],
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI();

const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: "Search for flight deals and summarize top results.",
    tools: [
        {
            type: "computer_use",
            environment: "desktop",
            enablePromptInjectionDetection: true,
        }
    ]
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.ComputerUse;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.EnvironmentEnum;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model("gemini-3.8-flash")
        .input(InteractionsInput.of("Search for flight deals and summarize top results."))
        .tools(
            Arrays.asList(
                ComputerUse.builder()
                    .environment(EnvironmentEnum.DESKTOP)
                    .enablePromptInjectionDetection(true)
                    .build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### Go

```
package main

import (
    "context"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    _, err = client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Search for flight deals and summarize top results."),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.ComputerUse{
                    Environment:                    interactions.EnvironmentEnumDesktop.ToPointer(),
                    EnablePromptInjectionDetection: genai.Ptr(true),
                }),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
}
```

### cURL

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions?key=${GEMINI_API_KEY}" \
-H 'Content-Type: application/json' \
-d '{
  "model": "gemini-3.8-flash",
  "input": "Search for flight deals and summarize top results.",
  "tools": [
    {
      "type": "computer_use",
      "environment": "desktop",
      "enable_prompt_injection_detection": true
    }
  ]
}'
```

### 确认安全决策

回答可能在函数调用参数中包含 `safety_decision` 参数：

```
{
  "steps": [
    {
      "type": "function_call",
      "name": "click",
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

如果 `safety_decision` 为 `require_confirmation`，则提示最终用户。如果用户确认，请在 `function_result` 中设置 `safety_acknowledgement`。

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

### 有关安全的最佳实践

Computer Use 会带来独特的安全和运营风险，因为代表用户执行操作的模型可能会在屏幕上遇到不可信的内容，或在执行操作时出错。实施以下最佳实践，保护用户数据和系统：

1. **人机协同 (HITL)**：
   - **强制执行用户确认**：当安全响应指示 `require_confirmation` 时，提示用户批准。
   - **提供自定义安全指令**：实施自定义系统指令，以定义和强制执行您自己的安全边界。例如：

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
         model="gemini-3.8-flash",
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

     If an action does **NOT** fall under the conditions for \`USER_CONFIRMATION\`,
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
         model: "gemini-3.8-flash",
         system_instruction: systemInstruction,
         input: "Prepare a draft but do not send.",
         tools: [{
             type: "computer_use",
             environment: "browser"
         }]
     });
     ```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.ComputerUse;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.EnvironmentEnum;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

String systemInstruction =
    "## **RULE 1: Seek User Confirmation (USER_CONFIRMATION)**\n\n"
        + "This is your first and most important check. If the next required action falls "
        + "into any of the following categories, you MUST stop immediately, and seek the "
        + "user's explicit permission.\n\n"
        + "## **RULE 2: Default Behavior (ACTUATE)**\n\n"
        + "If an action does **NOT** fall under the conditions for `USER_CONFIRMATION`, "
        + "your default behavior is to **Actuate**.";

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model("gemini-3.8-flash")
        .systemInstruction(systemInstruction)
        .input(InteractionsInput.of("Prepare a draft but do not send."))
        .tools(
            Arrays.asList(
                ComputerUse.builder().environment(EnvironmentEnum.BROWSER).build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### Go

```
package main

import (
    "context"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    systemInstruction := "## **RULE 1: Seek User Confirmation (USER_CONFIRMATION)**\n\n" +
        "This is your first and most important check. If the next required action falls " +
        "into any of the following categories, you MUST stop immediately, and seek the " +
        "user's explicit permission.\n\n" +
        "## **RULE 2: Default Behavior (ACTUATE)**\n\n" +
        "If an action does **NOT** fall under the conditions for `USER_CONFIRMATION`, " +
        "your default behavior is to **Actuate**."

    _, err = client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model:             interactions.Model("gemini-3.8-flash"),
            SystemInstruction: genai.Ptr(systemInstruction),
            Input:             interactions.NewInteractionsInput("Prepare a draft but do not send."),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.ComputerUse{
                    Environment: interactions.EnvironmentEnumBrowser.ToPointer(),
                }),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
}
```

1. **安全的执行环境**：在安全的沙盒环境中运行智能体，以限制其潜在影响。这可以是沙盒化虚拟机 (VM)、容器（例如 Docker）或权限受限的专用浏览器配置文件。如需了解如何使用 Docker 设置沙盒，请参阅 [GitHub 参考实现](https://github.com/google/computer-use-preview/)。
2. **输入净化**：净化提示中所有用户生成的文本，以降低意外指令或提示注入的风险。这是一种有用的安全层，但不能替代安全执行环境。
3. **内容护栏**：使用护栏和 Content Safety API 评估用户输入、工具输入和输出以及智能体的回答，以检测其是否适当、是否存在提示词注入和越狱。
4. **许可清单和屏蔽清单**：实施过滤机制，以控制模型可以导航到哪些位置以及可以执行哪些操作。禁止网站的屏蔽清单是一个很好的起点，而更严格的许可清单则更安全。
5. **可观测性和日志记录**：维护详细日志，以便进行调试、审核和突发事件响应。您的客户端应记录提示、屏幕截图、模型建议的操作 (`function_call`)、安全响应以及客户端最终执行的所有操作。
6. **环境管理**：确保 GUI 环境一致。意外的弹出式窗口、通知或布局变化可能会让模型感到困惑。如果可能，请从每个新任务的已知干净状态开始。

## 模型版本

您可以将“计算机使用”功能与以下模型搭配使用：

- [**Gemini 4 Argon**](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=zh-cn) (`gemini-4-argon`)：我们最强大的模型，支持通过计算机使用功能执行复杂的推理和代理界面工作流。
- [**Gemini 3.8 Flash**](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=zh-cn) (`gemini-3.8-flash`)：推荐用于计算机使用的模型，具有高准确度的界面交互和可靠的工具调用功能。
- [**Gemini 3.5 Flash-Lite**](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=zh-cn) (`gemini-3.5-flash-lite`)：一种低延迟、高性价比的模型，支持计算机使用。
- [**Gemini 3 Flash 预览版**](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=zh-cn) (`gemini-3-flash-preview`)：支持计算机使用的预览版模型。

## 后续步骤

- 在 [Browserbase 演示环境](http://gemini.browserbase.com)中试用 Computer Use。
- 如需查看示例代码，请参阅[参考实现](https://github.com/google/computer-use-preview)。
- 了解其他 Gemini API 工具：
  - [函数调用](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-cn)
  - [使用 Google 搜索建立依据](https://ai.google.dev/gemini-api/docs/google-search?hl=zh-cn)

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-10-22。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-10-22。"],[],[]]
