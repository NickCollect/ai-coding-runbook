---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/computer-use?hl=bn
fetched_at: 2026-10-12T06:55:03.974503+00:00
title: "\u0995\u09ae\u09cd\u09aa\u09bf\u0989\u099f\u09be\u09b0\u09c7\u09b0 \u09ac\u09cd\u09af\u09ac\u09b9\u09be\u09b0 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

জেমিনি ৩.৮ ফ্ল্যাশ এখন পাওয়া যাচ্ছে। [ব্যবহার করে দেখুন](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=bn) ।

![](https://ai.google.dev/_static/images/translated.svg?hl=bn)

আপনার পছন্দের ভাষায় কন্টেন্ট অনুবাদ করতে Google তার AI প্রযুক্তি ব্যবহার করে। AI-এর মাধ্যমে করা অনুবাদে ভুল থাকতে পারে।

- [হোম](https://ai.google.dev/?hl=bn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=bn)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=bn)
- [দস্তাবেজ](https://ai.google.dev/gemini-api/docs/generate-content?hl=bn)

মতামত জানান

# কম্পিউটারের ব্যবহার

কম্পিউটার ব্যবহার টুল আপনাকে ব্রাউজার, মোবাইল ও ডেস্কটপ কন্ট্রোল এজেন্ট তৈরি করতে দেয়
যা টাস্কের সাথে ইন্টার‍্যাক্ট করে ও অটোমেট করে। স্ক্রিনশট ব্যবহার করে, মডেলটি একটি
কম্পিউটার স্ক্রিন "দেখতে" এবং মাউস ক্লিক
ও কীবোর্ড ইনপুটের মতো নির্দিষ্ট UI অ্যাকশন জেনারেট করে "কাজ করতে" পারে। ফাংশন কলিংয়ের মতোই, কম্পিউটার ব্যবহার সংক্রান্ত
অ্যাকশন পেতে ও এক্সিকিউট করতে আপনাকে ক্লায়েন্ট-সাইড এক্সিকিউশন এনভায়রনমেন্ট
ইমপ্লিমেন্ট করতে হবে।

কোন কোন মডেল কাজ করে তার তালিকা দেখতে, [মডেলের ভার্সন](#model-versions) দেখুন। Gemini 3.x মডেলে একাধিক উন্নত ফিচার কাজ করে:

- **একাধিক এনভায়রনমেন্টে কাজ করে:** [ব্রাউজার, মোবাইল ও ডেস্কটপ](#supported-environments) এনভায়রনমেন্টের জন্য বিল্ড এজেন্ট।
- **ইন্টেন্ট সহ স্ট্রিমলাইন করা অ্যাকশন:** অ্যাকশনে একটি `intent` ফিল্ড থাকে যা প্রতিটি ধাপের পিছনে মডেলের যুক্তি ব্যাখ্যা করে।
- **কনফিগার করা যায় এমন নিরাপত্তা নীতি:** বিল্ট-ইন নীতি বিভাগ ও ওভাররাইড ব্যবহার করে [নিরাপত্তা সংক্রান্ত আচরণ](#safety-policies) ফাইন-টিউন করুন।
- **প্রম্পট ইঞ্জেকশন শনাক্তকরণ:** লুকানো ক্ষতিকর নির্দেশাবলী শনাক্ত করতে [স্ক্রিনশট স্ক্যানিং](#prompt-injection) অপ্ট-ইন করুন।

কম্পিউটার ব্যবহারের মাধ্যমে, আপনি এমন এজেন্ট তৈরি করতে পারবেন যা:

- ওয়েবসাইটে বারবার ডেটা এন্ট্রি করা বা ফর্ম পূরণ করার কাজ অটোমেট করা।
- ওয়েব অ্যাপ্লিকেশন ও ইউজার ফ্লোয়ের অটোমেটেড টেস্টিং করা
- বিভিন্ন ওয়েবসাইট জুড়ে রিসার্চ করা (যেমন, কেনাকাটা করার ব্যাপারে জানানোর জন্য
  ই-কমার্স সাইট থেকে প্রোডাক্ট সংক্রান্ত তথ্য, দাম ও রিভিউ সংগ্রহ করা)

কম্পিউটার ব্যবহার টুল চালু করার একটি সংক্ষিপ্ত উদাহরণ এখানে দেওয়া হল:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash",
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

### জাভাস্ক্রিপ্ট

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI();

const response = await ai.models.generateContent({
  model: 'gemini-3.8-flash',
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

## কম্পিউটার ব্যবহার কীভাবে কাজ করে

কম্পিউটার ব্যবহার মডেলের সাহায্যে এজেন্ট তৈরি করতে, আপনার অ্যাপ্লিকেশন ও API-এর মধ্যে
একটি নিরবচ্ছিন্ন লুপ সেট-আপ করতে হবে। প্রতিটি ধাপে আপনার কোড
কী করবে তা এখানে দেওয়া হল:

1. [**মডেলকে অনুরোধ পাঠান**](#send-request)
   - আপনার অ্যাপ্লিকেশন, কম্পিউটার ব্যবহার করার টুল,
     আপনার কনফিগারেশন সেটিংস (যেমন, টার্গেট এনভায়রনমেন্ট), ব্যবহারকারীর
     প্রম্পট এবং বর্তমান স্ক্রিনের একটি স্ক্রিনশট সহ একটি API অনুরোধ পাঠায়।
2. [**মডেলের উত্তর পান**](#model-response)
   - মডেলটি স্ক্রিন ও প্রম্পট বিশ্লেষণ করে একটি উত্তর দেয়
     যেখানে UI অ্যাকশন (যেমন
     ক্লিক, স্ক্রল বা কীস্ট্রোক) বোঝানোর জন্য একটি সাজেস্ট করা `function_call` থাকে।
   - **Gemini 3.x মডেলের** ক্ষেত্রে, উত্তরে একটি যুক্তিও `intent`
     ব্যাখ্যা করা হয় যে কেন মডেলটি সেই অ্যাকশন বেছে নিয়েছে।
   - এছাড়াও, উত্তরে ইন্টার্নাল নিরাপত্তা
     সিস্টেম থেকে পাওয়া `safety_decision` থাকতে পারে যা অ্যাকশনকে সাধারণ/অনুমোদিত,
     `require_confirmation` (ব্যবহারকারীর অনুমোদন প্রয়োজন) বা ব্লক করা হিসেবে শ্রেণীবদ্ধ করে।
3. [**প্রাপ্ত অ্যাকশন এক্সিকিউট করা**](#execute-actions)
   - অ্যাকশনটি অনুমোদিত হলে (বা ব্যবহারকারী এটি কনফার্ম করলে), আপনার ক্লায়েন্ট-সাইড
     কোড `function_call` পার্স করে, আপনার ভিউপোর্ট
     ম্যাচ করার জন্য স্বাভাবিক কোঅর্ডিনেট স্কেল করে এবং অটোমেশন টুল (যেমন, Playwright)
     ব্যবহার করে আপনার টার্গেট এনভায়রনমেন্টে অ্যাকশনটি এক্সিকিউট করে। অ্যাকশন ব্লক করা হলে, আপনার
     ক্লায়েন্টকে এক্সিকিউশন বন্ধ করতে হবে বা বাধা সামলাতে হবে।
4. [**নতুন এনভায়রনমেন্ট স্টেট ক্যাপচার করুন**](#capture-state)
   - অ্যাকশন এক্সিকিউট করা হয়ে গেলে, আপনার অ্যাপ্লিকেশন একটি নতুন
     স্ক্রিনশট ক্যাপচার করে এবং পরবর্তী ধাপের জন্য অনুরোধ করতে `function_result`-এর মাধ্যমে
     মডেলকে সেটি ফেরত পাঠায়।

এই প্রসেসটি তারপর ধাপ ২ থেকে পুনরাবৃত্তি হয়, টাস্ক সম্পূর্ণ বা বাতিল না হওয়া পর্যন্ত মডেলের থেকে ক্রমাগত পরবর্তী অ্যাকশন
চাওয়ার মাধ্যমে এটি করা হয়।

![কম্পিউটার ব্যবহার সংক্রান্ত ওভারভিউ](https://ai.google.dev/static/gemini-api/docs/images/computer_use.png?hl=bn)

## কম্পিউটার ব্যবহার কীভাবে প্রয়োগ করতে হয়

কম্পিউটার ব্যবহার টুল ব্যবহার করে বিল্ড করার আগে আপনাকে এগুলি সেট-আপ করতে হবে:

- **নিরাপদ এক্সিকিউশন এনভায়রনমেন্ট:** আপনার হোস্ট সিস্টেম থেকে এটিকে আলাদা করতে এবং এর সম্ভাব্য প্রভাব সীমিত করতে, আপনার এজেন্টকে স্যান্ডবক্স করা VM বা
  কন্টেনারে চালান।
  [রেফারেন্স ইমপ্লিমেন্টেশনে](https://github.com/google/computer-use-preview/)
  ব্যবহার করার জন্য রেডি-টু-ইউজ ডকার-ভিত্তিক স্যান্ডবক্স অন্তর্ভুক্ত থাকে যা আপনি প্রাথমিক পয়েন্ট হিসেবে ব্যবহার করতে পারেন।
- **ক্লায়েন্ট-সাইড অ্যাকশন হ্যান্ডলার:** কোঅর্ডিনেট এক্সিকিউট করা, টেক্সট টাইপ করা এবং স্ক্রিনশট নেওয়ার জন্য ক্লায়েন্ট-সাইড লজিক প্রয়োগ করুন।

নিচে দেওয়া উদাহরণগুলি এক্সিকিউশন এনভায়রনমেন্ট হিসেবে ওয়েব ব্রাউজার এবং
ক্লায়েন্ট-সাইড হ্যান্ডলার হিসেবে [Playwright](https://playwright.dev/) ব্যবহার করে।

### ০. Playwright সেট-আপ করা

প্রথমে, প্রয়োজনীয় প্যাকেজ ইনস্টল করুন:

```
pip install google-genai playwright
playwright install chromium
```

তারপরে, এক্সিকিউশনের জন্য Playwright ব্রাউজার ইনস্ট্যান্স ইনিশিয়ালাইজ করুন:

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

### ১. মডেলের কাছে অনুরোধ পাঠান

ক্লায়েন্ট লাইব্রেরি ইনিশিয়ালাইজ করুন এবং কম্পিউটার ব্যবহার টুল কনফিগার করুন। মনে রাখবেন, অনুরোধ করার সময় ডিসপ্লে সাইজ উল্লেখ করার প্রয়োজন নেই; মডেলটি স্ক্রিনের দৈর্ঘ্য ও প্রস্থ অনুযায়ী স্কেল করা পিক্সেল কোঅর্ডিনেট অনুমান করে।

### Python

ব্রাউজার এনভায়রনমেন্টকে টার্গেট করে কোনও অনুরোধ কনফিগার করতে `google-genai` Python SDK (ভার্সন `2.7.0` বা তার পরবর্তী যেকোনও ভার্সন) ব্যবহার করুন:

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
    model="gemini-3.8-flash",
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

### জাভাস্ক্রিপ্ট

ব্রাউজার এনভায়রনমেন্টকে টার্গেট করে কোনও অনুরোধ কনফিগার করতে `@google/genai` Node.js SDK ব্যবহার করুন:

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI();

const response = await ai.models.generateContent({
  model: 'gemini-3.8-flash',
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

অনুরোধ পাঠাতে curl ব্যবহার করুন:

```
curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key=$GEMINI_API_KEY" \
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

### ২. মডেলের উত্তর পান

মডেলের উত্তরে কোঅর্ডিনেট ও একটি
কাস্টমাইজ করা যুক্তিপূর্ণ উদ্দেশ্য সহ ফাংশন কলের কথা বলা হয়েছে যা অ্যাকশন ব্যাখ্যা করে:

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

### ৩. প্রাপ্ত অ্যাকশন প্রয়োগ করা

আপনার অ্যাপ্লিকেশন কোডকে মডেলের উত্তর পার্স করতে হবে, অ্যাকশন এক্সিকিউট করতে হবে
এবং ফলাফল সংগ্রহ করতে হবে।

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

    # Parse function calls from candidate response
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

### জাভাস্ক্রিপ্ট

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

### ৪. নতুন এনভায়রনমেন্ট স্টেট ক্যাপচার করা

স্ক্রিনের একটি ছবি ক্যাপচার করে মডেলে ফেরত দিন।

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

### জাভাস্ক্রিপ্ট

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

পরিবেশের অবস্থা কীভাবে ক্যাপচার ও ফর্ম্যাট করতে হবে তা নির্ধারণ করার পরে, আপনি এই সমস্ত ধাপকে একটি অবিচ্ছিন্ন এক্সিকিউশন লুপে একত্রিত করতে পারবেন।

## এজেন্ট লুপ তৈরি করা

মাল্টি-স্টেপ ইন্ট্যার‍্যাকশন চালু করতে, [কম্পিউটার ব্যবহার কীভাবে প্রয়োগ করতে হয়](#implement-computer-use) বিভাগ থেকে চারটি ধাপকে একটি লুপে একত্রিত করুন। টাস্ক সম্পূর্ণ না হওয়া পর্যন্ত এই লুপ অ্যাকশনের অনুরোধ করা এবং মডেলকে ফলাফল ফিড করা চালিয়ে যায়।

প্রতিটি ধাপে মডেলের উত্তর ও আপনার ফাংশনের উত্তর, দুটিই কথোপকথনের ইতিহাসে যোগ করে কথোপকথনের ইতিহাস সঠিকভাবে ম্যানেজ করতে ভুলবেন না।

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
            model='gemini-3.8-flash',
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

### জাভাস্ক্রিপ্ট

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
            model: 'gemini-3.8-flash',
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

## মানানসই এনভায়রনমেন্ট

Gemini 3.x মডেলে `computer_use` কনফিগারেশনে উল্লেখ করা তিনটি এনভায়র্নমেন্ট কাজ করে:

### ব্রাউজার এনভায়রনমেন্ট (`ENVIRONMENT_BROWSER`)

ব্রাউজার টুলের অধীনে অ্যাকশন অ্যাকশন:

| কমান্ডের নাম | বিবরণ | আর্গুমেন্ট (ফাংশন কলে) |
| --- | --- | --- |
| **ক্লিক করুন** | স্থানাঙ্কে মাউসের বাঁদিকের বোতামে ক্লিক করুন। | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **double\_click** | স্থানাঙ্কে ডবল ক্লিক করুন। | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **triple\_click** | কোঅর্ডিনেটে ট্রিপল ক্লিক করুন। | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **middle\_click** | স্থানাঙ্কে মিডল ক্লিক করুন। | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **right\_click** | কোঅর্ডিনেটে রাইট ক্লিক করে। | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **mouse\_down** | কোঅর্ডিনেটে মাউস বোতাম প্রেস করে ধরে রাখে। | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **mouse\_up** | কোঅর্ডিনেটে মাউস বোতাম রিলিজ করে। | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **সরানো** | নির্দিষ্ট পজিশনে কার্সর নিয়ে যায়। | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **type** | টেক্সট টাইপ করে। | `text`: str `press_enter`: bool (ঐচ্ছিক, ডিফল্ট `false`) `intent`: str |
| **drag\_and\_drop** | শুরু কোঅর্ডিনেট থেকে শেষ কোঅর্ডিনেটে কোনও আইটেম ড্র্যাগ করে। | `start_y`: int (0-999) `start_x`: int (0-999) `end_y`: int (0-999) `end_x`: int (0-999) `intent`: str |
| **অপেক্ষা করুন** | নির্দিষ্ট সংখ্যক সেকেন্ডের জন্য এক্সিকিউশন পজ করে। | `seconds`: int (ঐচ্ছিক, ডিফল্ট `1`) `intent`: str |
| **press\_key** | নির্দিষ্ট কী প্রেস করে ছেড়ে দেয়। | `key`: str `intent`: str |
| **key\_down** | নির্দিষ্ট কী প্রেস করে ধরে রাখে। | `key`: str `intent`: str |
| **key\_up** | নির্দিষ্ট কী রিলিজ করে। | `key`: str `intent`: str |
| **হটকী** | নির্দিষ্ট কী কম্বিনেশন প্রেস করে। | `keys`: `List[str]` `intent`: `str` |
| **take\_screenshot** | বর্তমান স্ক্রিনের একটি স্ক্রিনশট রিটার্ন করে। | `intent`: str |
| **স্ক্রল করুন** | পিক্সেল দূরত্ব অনুযায়ী কোঅর্ডিনেটে উপরে, নিচে, বাঁদিকে বা ডানদিকে স্ক্রল করে। | `y`: int (০-৯৯৯) `x`: int (০-৯৯৯) `direction`: str (`"up"`, `"down"`, `"left"`, `"right"`) `magnitude_in_pixels`: int (০-৯৯৯, ঐচ্ছিক, ডিফল্ট `300`) `intent`: str |
| **go\_back** | ব্রাউজার ইতিহাসে আগের ওয়েবপেজে ফিরে যায়। | `intent`: str |
| **নেভিগেট করা** | নির্দিষ্ট URL-এ সরাসরি নেভিগেট করে। | `url`: str `intent`: str |
| **go\_forward** | ব্রাউজার ইতিহাসে পরবর্তী ওয়েবপেজে নেভিগেট করে। | `intent`: str |

### মোবাইল এনভায়রনমেন্ট (`ENVIRONMENT_MOBILE`)

Android-এর জন্য অপ্টিমাইজ করা এনভায়রনমেন্ট অ্যাকশন:

| কমান্ডের নাম | বিবরণ | আর্গুমেন্ট (ফাংশন কলে) |
| --- | --- | --- |
| **open\_app** | নাম ধরে কোনও অ্যাপ্লিকেশন খোলে। | `app_name`: str `intent`: str |
| **ক্লিক করুন** | স্থানাঙ্কে মাউসের বাঁদিকের বোতামে ক্লিক করুন। | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **list\_apps** | ডিভাইসে উপলভ্য অ্যাপ্লিকেশনগুলির তালিকা তৈরি করে, তাদের নাম এবং প্যাকেজের নাম রিটার্ন করে। | `intent`: str |
| **অপেক্ষা করুন** | নির্দিষ্ট সংখ্যক সেকেন্ডের জন্য এক্সিকিউশন পজ করে। | `seconds`: int (ঐচ্ছিক, ডিফল্ট `1`) `intent`: str |
| **go\_back** | আগের স্ক্রিন বা ওয়েবপেজে ফিরে যায়। | `intent`: str |
| **type** | টেক্সট টাইপ করে। | `text`: str `press_enter`: bool (ঐচ্ছিক, ডিফল্ট `false`) `intent`: str |
| **drag\_and\_drop** | শুরু কোঅর্ডিনেট থেকে শেষ কোঅর্ডিনেটে কোনও আইটেম ড্র্যাগ করে। | `start_y`: int (0-999) `start_x`: int (0-999) `end_y`: int (0-999) `end_x`: int (0-999) `intent`: str |
| **long\_press** | স্ক্রিনের কোনও কোঅর্ডিনেটে বেশিক্ষণ প্রেস করে। | `y`: int (০-৯৯৯) `x`: int (০-৯৯৯) `seconds`: int (ঐচ্ছিক, ডিফল্ট `2`) `intent`: str |
| **press\_key** | নির্দিষ্ট কী প্রেস করে ছেড়ে দেয়। | `key`: str `intent`: str |
| **take\_screenshot** | বর্তমান স্ক্রিনের একটি স্ক্রিনশট রিটার্ন করে। | `intent`: str |

### ডেস্কটপ এনভায়রনমেন্ট (`ENVIRONMENT_DESKTOP`)

ডেস্কটপ এনভায়রনমেন্ট OS-লেভেল কার্সর কমান্ড:

| কমান্ডের নাম | বিবরণ | আর্গুমেন্ট (ফাংশন কলে) |
| --- | --- | --- |
| **ক্লিক করুন** | স্থানাঙ্কে মাউসের বাঁদিকের বোতামে ক্লিক করুন। | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **double\_click** | স্থানাঙ্কে ডবল ক্লিক করুন। | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **triple\_click** | কোঅর্ডিনেটে ট্রিপল ক্লিক করুন। | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **middle\_click** | স্থানাঙ্কে মিডল ক্লিক করুন। | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **right\_click** | কোঅর্ডিনেটে রাইট ক্লিক করে। | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **mouse\_down** | কোঅর্ডিনেটে মাউস বোতাম প্রেস করে ধরে রাখে। | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **mouse\_up** | কোঅর্ডিনেটে মাউস বোতাম রিলিজ করে। | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **সরানো** | নির্দিষ্ট পজিশনে কার্সর নিয়ে যায়। | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **type** | টেক্সট টাইপ করে। | `text`: str `press_enter`: bool (ঐচ্ছিক, ডিফল্ট `false`) `intent`: str |
| **drag\_and\_drop** | শুরু কোঅর্ডিনেট থেকে শেষ কোঅর্ডিনেটে কোনও আইটেম ড্র্যাগ করে। | `start_y`: int (0-999) `start_x`: int (0-999) `end_y`: int (0-999) `end_x`: int (0-999) `intent`: str |
| **অপেক্ষা করুন** | নির্দিষ্ট সংখ্যক সেকেন্ডের জন্য এক্সিকিউশন পজ করে। | `seconds`: int (ঐচ্ছিক, ডিফল্ট `1`) `intent`: str |
| **press\_key** | নির্দিষ্ট কী প্রেস করে ছেড়ে দেয়। | `key`: str `intent`: str |
| **key\_down** | নির্দিষ্ট কী প্রেস করে ধরে রাখে। | `key`: str `intent`: str |
| **key\_up** | নির্দিষ্ট কী রিলিজ করে। | `key`: str `intent`: str |
| **হটকী** | নির্দিষ্ট কী কম্বিনেশন প্রেস করে। | `keys`: `List[str]` `intent`: `str` |
| **take\_screenshot** | বর্তমান স্ক্রিনের একটি স্ক্রিনশট রিটার্ন করে। | `intent`: str |
| **স্ক্রল করুন** | পিক্সেল দূরত্ব অনুযায়ী কোঅর্ডিনেটে উপরে, নিচে, বাঁদিকে বা ডানদিকে স্ক্রল করে। | `y`: int (০-৯৯৯) `x`: int (০-৯৯৯) `direction`: str (`"up"`, `"down"`, `"left"`, `"right"`) `magnitude_in_pixels`: int (০-৯৯৯, ঐচ্ছিক, ডিফল্ট `300`) `intent`: str |

## ব্যবহারকারীর নির্দিষ্ট করা কাস্টম ফাংশন

কাস্টম ব্যবহারকারী-সংজ্ঞায়িত ফাংশন অন্তর্ভুক্ত করে আপনি মডেলের কার্যকারিতা বাড়াতে পারেন। যেমন, হিউম্যান-ইন-দ্য-লুপ (HITL) পরিস্থিতিতে আপনি আগে থেকে নির্ধারণ করা ডিফল্ট অ্যাকশন বাদ দিতে এবং কাস্টম অ্যাকশন রেজিস্টার করতে পারবেন।

### Python

আগে থেকে সংজ্ঞায়িত স্ট্যান্ডার্ড ব্রাউজার অ্যাকশন (যেমন `click`) বাদ দিন এবং কাস্টম `yield_to_user` টুল রেজিস্টার করুন:

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
    model="gemini-3.8-flash",
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

## থিঙ্কিং লেভেল ম্যানেজ করা

কম্পিউটার ব্যবহারকারী এজেন্টের ক্ষেত্রে, অ্যাকশনের কোয়ালিটি ও এক্সিকিউশন স্পিডের মধ্যে ব্যালেন্স বজায় রাখতে আপনি বিভিন্ন থিঙ্কিং লেভেল কনফিগার করতে পারবেন। সাধারণত, স্ট্যান্ডার্ড অটোমেশন টাস্কের জন্য কম লেভেলের থিঙ্কিং ভালো ব্যালেন্স বজায় রাখে।

## নিরাপত্তা ও সুরক্ষা

### নিরাপত্তা নীতি কনফিগার করা

Gemini 3.x মডেলে বিল্ট-ইন নিরাপত্তা পরিষেবা বিভাগ অন্তর্ভুক্ত থাকে যা
ব্যবহারকারীর কনফার্মেশন প্রয়োজন কিনা তা নির্ধারণ করতে সাহায্য করে।

| নিরাপত্তা নীতি বিভাগ | বিবরণ |
| --- | --- |
| `FINANCIAL_TRANSACTIONS` | পেমেন্ট, রিটেল চেক-আউট বা রেগুলেটেড প্রোডাক্ট সংক্রান্ত অ্যাকশনের জন্য কনফার্মেশন ব্লক বা ট্রিগার করে। |
| `SENSITIVE_DATA_MODIFICATION` | অননুমোদিত পরিবর্তন থেকে স্বাস্থ্য, আর্থিক বা সরকারি রেকর্ড রক্ষা করে। |
| `COMMUNICATION_TOOL` | এজেন্টকে নিজে থেকে ইমেল, চ্যাট মেসেজ বা ড্রাফ্ট পাঠানোর ব্যাপারে বিধিনিষেধ আরোপ করে। |
| `ACCOUNT_CREATION` | ওয়েবসাইটে এজেন্টকে নতুন অ্যাকাউন্ট অটোমেটিক রেজিস্টার করা থেকে সীমাবদ্ধ করে। |
| `DATA_MODIFICATION` | সামগ্রিক ফাইল সিস্টেমের পরিবর্তন, ডেটা শেয়ারিং ও স্টোরেজ মুছে দেওয়া নিয়ন্ত্রণ করে। |
| `USER_CONSENT_MANAGEMENT` | কুকি সংক্রান্ত সম্মতি ব্যানার ও গোপনীয়তা প্রম্পটের জন্য ব্যবহারকারীর টেকওভার প্রয়োজন। |
| `LEGAL_TERMS_AND_AGREEMENTS` | মডেলকে পরিষেবার শর্তাবলী বা আইনগতভাবে বাধ্যতামূলক চুক্তি নিজে থেকে গ্রহণ করা থেকে বাধা দেয়। |

#### নিরাপত্তা সংক্রান্ত ওভাররাইড

আপনি ওভাররাইড পাস করে বেছে নেওয়া নীতি ওভাররাইড করতে পারবেন:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash",
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

### জাভাস্ক্রিপ্ট

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI();

const response = await ai.models.generateContent({
  model: 'gemini-3.8-flash',
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

### প্রম্পট ইঞ্জেকশন শনাক্তকরণ

Gemini 3.5 Flash-Lite বা এর পরের যেকোনও ভার্সনের জন্য কম্পিউটার ব্যবহার, প্রম্পট ইনজেকশন অ্যাটাক শনাক্ত করতে উন্নত নিরাপত্তা
মেকানিজমকে সমর্থন করে। চালু করা হলে, এই ফিচার
চেক করে দেখে যে যোগ করা স্ক্রিনশটে লুকানো অ্যাডভার্সারিয়াল
নির্দেশাবলী (যেমন, "আগের কমান্ড উপেক্ষা করো") আছে কিনা এবং শনাক্ত করা হলে
সেগুলি প্রয়োগ করা ব্লক করে দেয়।

প্রম্পট ইঞ্জেকশন শনাক্তকরণ হল একটি অপ্ট-ইন ফিচার। ডিফল্ট হল `false`।

আপনার কম্পিউটার ব্যবহার টুল কনফিগারেশনে কীভাবে প্রম্পট ইনজেকশন শনাক্তকরণ
চালু করবেন তা নিম্নলিখিত উদাহরণ থেকে জানতে পারবেন:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Search for flight deals and summarize top results.",
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                computer_use=types.ComputerUse(
                    environment="ENVIRONMENT_DESKTOP",
                    enable_prompt_injection_detection=True,
                )
            )
        ]
    ),
)
```

### জাভাস্ক্রিপ্ট

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI();

const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "Search for flight deals and summarize top results.",
    config: {
        tools: [{
            computerUse: {
                environment: "ENVIRONMENT_DESKTOP",
                enablePromptInjectionDetection: true,
            }
        }]
    }
});
```

### cURL

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key=${GEMINI_API_KEY}" \
-H 'Content-Type: application/json' \
-d '{
  "contents": [{
    "parts": [{"text": "Search for flight deals and summarize top results."}]
  }],
  "tools": [{
    "computer_use": {
      "environment": "ENVIRONMENT_DESKTOP",
      "enable_prompt_injection_detection": true
    }
  }]
}'
```

### নিরাপত্তা সংক্রান্ত সিদ্ধান্ত সম্পর্কে সম্মতি জানানো

উত্তরে ফাংশন কল আর্গুমেন্টে `safety_decision` প্যারামিটার থাকতে পারে:

```
{
  "function_call": {
    "name": "click",
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

`safety_decision` `require_confirmation` হলে, ব্যবহারকারীকে প্রম্পট দেখান। ব্যবহারকারী কনফার্ম করলে, `FunctionResponse`-এ `safety_acknowledgement` সেট করুন।

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

### নিরাপত্তা সংক্রান্ত পেশাদার পদ্ধতি

কম্পিউটার ব্যবহার করার ক্ষেত্রে অনন্য নিরাপত্তা ও অপারেশনাল ঝুঁকি থাকে, কারণ কোনও মডেল ব্যবহারকারীর হয়ে কাজ করার
সময় স্ক্রিনে বিশ্বাসযোগ্য নয় এমন কন্টেন্ট দেখতে পেতে পারে অথবা অ্যাকশন এক্সিকিউট করার সময়
ভুল করতে পারে। ব্যবহারকারীর
ডেটা ও সিস্টেম সুরক্ষিত রাখতে, নিম্নলিখিত পেশাদার পদ্ধতি প্রয়োগ করুন:

1. **হিউম্যান-ইন-দ্য-লুপ (HITL):**

   - **ব্যবহারকারীর কনফার্মেশন এনফোর্স করা:** নিরাপত্তা সংক্রান্ত উত্তরে
     `require_confirmation` থাকলে, ব্যবহারকারীকে অনুমোদনের জন্য প্রম্পট করো।
   - **নিরাপত্তা সংক্রান্ত কাস্টম নির্দেশাবলী প্রদান করুন:** আপনার নিজস্ব নিরাপত্তা সংক্রান্ত সীমা নির্ধারণ ও প্রয়োগ করতে কাস্টম সিস্টেম নির্দেশাবলী প্রয়োগ করুন। যেমন:

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
         model="gemini-3.8-flash",
         contents="Prepare a draft but do not send.",
         config=types.GenerateContentConfig(
             system_instruction=system_instruction,
             tools=[types.Tool(computer_use=types.ComputerUse(environment="ENVIRONMENT_BROWSER"))]
         )
     )
     ```

     ### জাভাস্ক্রিপ্ট

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

     const response = await ai.models.generateContent({
       model: 'gemini-3.8-flash',
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
2. **নিরাপদ এক্সিকিউশন এনভায়রনমেন্ট:** আপনার এজেন্টের সম্ভাব্য প্রভাব সীমিত করতে, এটি একটি নিরাপদ, স্যান্ডবক্সড
   এনভায়রনমেন্টে চালান। এটি স্যান্ডবক্স করা ভার্চুয়াল
   মেশিন (VM), কন্টেনার (যেমন, Docker) বা সীমিত অনুমতি সহ ডেডিকেটেড ব্রাউজার প্রোফাইল
   হতে পারে। Docker ব্যবহার করে স্যান্ডবক্স সেট-আপ করার নির্দেশিকা পেতে
   [GitHub রেফারেন্স ইমপ্লিমেন্টেশন](https://github.com/google/computer-use-preview/)
   দেখুন।
3. **ইনপুট স্যানিটাইজেশন:** প্রম্পটে ব্যবহারকারীর তৈরি করা সব টেক্সট স্যানিটাইজ করে
   অনিচ্ছাকৃত নির্দেশাবলী বা প্রম্পট ইনজেকশনের ঝুঁকি কমান। এটি
   সুরক্ষার একটি সহায়ক স্তর, তবে এটি নিরাপদ এক্সিকিউশন
   এনভায়রনমেন্টের বিকল্প নয়।
4. **কন্টেন্ট গার্ডরেল:** উপযুক্ততা,
   প্রম্পট ইনজেকশন ও জেলব্রেক শনাক্তকরণের জন্য
   ব্যবহারকারীর ইনপুট, টুলের ইনপুট ও আউটপুট এবং এজেন্টের উত্তর মূল্যায়ন করতে গার্ডরেল ও কন্টেন্ট সুরক্ষা API ব্যবহার করুন।
5. **সাদা তালিকা ও কালো তালিকা:** মডেল কোথায় নেভিগেট করতে পারবে এবং কী করতে পারবে তা নিয়ন্ত্রণ করতে
   ফিল্টার করার পদ্ধতি প্রয়োগ করুন। নিষিদ্ধ
   ওয়েবসাইটের কালো তালিকা একটি ভালো সূচনা হতে পারে, তবে আরও বেশি বিধিনিষেধমূলক সাদা তালিকা
   আরও বেশি সুরক্ষিত।
6. **পর্যবেক্ষণযোগ্যতা ও লগিং:** ডিবাগিং,
   অডিটিং ও ঘটনার প্রতিক্রিয়া জানানোর জন্য বিস্তারিত লগ বজায় রাখুন। আপনার ক্লায়েন্টকে প্রম্পট,
   স্ক্রিনশট, মডেলের সাজেস্ট করা অ্যাকশন (`function_call`), নিরাপত্তা সংক্রান্ত উত্তর এবং
   ক্লায়েন্টের দ্বারা চূড়ান্তভাবে এক্সিকিউট করা সব অ্যাকশন লগ করতে হবে।
7. **পরিবেশ ম্যানেজমেন্ট:** GUI পরিবেশ যেন সামঞ্জস্যপূর্ণ হয় তা নিশ্চিত করুন।
   অপ্রত্যাশিত পপ-আপ, বিজ্ঞপ্তি বা লেআউটে পরিবর্তন হলে, মডেল বিভ্রান্ত
   হয়ে যেতে পারে। সম্ভব হলে, প্রতিটি নতুন টাস্কের জন্য পরিচিত, পরিষ্কার স্টেট থেকে শুরু করুন।

## মডেলের ভার্সন

আপনি নিম্নলিখিত মডেলের সাথে কম্পিউটার ব্যবহার করতে পারবেন:

- [**Gemini 3.8 Flash**](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=bn) (`gemini-3.8-flash`): কম্পিউটারে ব্যবহারের জন্য সাজেস্ট করা মডেল, এতে রয়েছে অত্যন্ত নিখুঁত UI ইন্টার‍্যাকশন ও নির্ভরযোগ্য টুল কলিং।
- [**Gemini 3.5 Flash-Lite**](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=bn) (`gemini-3.5-flash-lite`): কম লেটেন্সি ও কম খরচে কাজ করে এমন মডেল যা
  কম্পিউটার ব্যবহারের ক্ষেত্রে সহায়ক।
- [**Gemini 3 Flash প্রিভিউ**](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=bn) (`gemini-3-flash-preview`): কম্পিউটার ব্যবহারের জন্য উপযুক্ত
  মডেলের প্রিভিউ।

## এর পরে কী করতে হবে

- [Browserbase ডেমো এনভায়রনমেন্টে](http://gemini.browserbase.com) কম্পিউটার ব্যবহারের মাধ্যমে এক্সপেরিমেন্ট করুন।
- কোডের উদাহরণের জন্য [রেফারেন্স প্রয়োগ](https://github.com/google/computer-use-preview) দেখুন।
- অন্যান্য Gemini API টুল সম্পর্কে জানুন:
  - [ফাংশন কলিং](https://ai.google.dev/gemini-api/docs/function-calling?hl=bn)
  - [Google Search-এর মাধ্যমে গ্রাউন্ডিং](https://ai.google.dev/gemini-api/docs/grounding?hl=bn)

মতামত জানান

অন্য কিছু উল্লেখ না করা থাকলে, এই পৃষ্ঠার কন্টেন্ট [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)-এর অধীনে এবং কোডের নমুনাগুলি [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)-এর অধীনে লাইসেন্স প্রাপ্ত। আরও জানতে, [Google Developers সাইট নীতি](https://developers.google.com/site-policies?hl=bn) দেখুন। Java হল Oracle এবং/অথবা তার অ্যাফিলিয়েট সংস্থার রেজিস্টার্ড ট্রেডমার্ক।

2026-10-09 UTC-তে শেষবার আপডেট করা হয়েছে।

আমাদের আরও কিছু জানাতে চান?

[[["সহজে বোঝা যায়","easyToUnderstand","thumb-up"],["আমার সমস্যার সমাধান হয়েছে","solvedMyProblem","thumb-up"],["অন্যান্য","otherUp","thumb-up"]],[["এতে আমার প্রয়োজনীয় তথ্য নেই","missingTheInformationINeed","thumb-down"],["খুব জটিল / অনেক ধাপ","tooComplicatedTooManySteps","thumb-down"],["পুরনো","outOfDate","thumb-down"],["অনুবাদ সংক্রান্ত সমস্যা","translationIssue","thumb-down"],["নমুনা / কোড সংক্রান্ত সমস্যা","samplesCodeIssue","thumb-down"],["অন্যান্য","otherDown","thumb-down"]],["2026-10-09 UTC-তে শেষবার আপডেট করা হয়েছে।"],[],[]]
