---
source_url: https://ai.google.dev/gemini-api/docs/computer-use?hl=he
fetched_at: 2026-07-27T04:46:49.397639+00:00
title: "\u05e9\u05d9\u05de\u05d5\u05e9 \u05d1\u05de\u05d7\u05e9\u05d1 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# שימוש במחשב

הכלי 'שימוש במחשב' מאפשר לכם לבנות סוכני בקרה לדפדפן, לנייד ולמחשב, שמבצעים אינטראקציות ומשימות אוטומטיות. באמצעות צילומי מסך, המודל יכול "לראות" מסך מחשב ו "לפעול" על ידי יצירת פעולות ספציפיות בממשק המשתמש, כמו קליקים בעכבר וקלט מהמקלדת. בדומה לקריאה לפונקציה, תצטרכו להטמיע את סביבת ההפעלה בצד הלקוח כדי לקבל ולהפעיל את הפעולות של השימוש במחשב.

רשימת המודלים הנתמכים מופיעה במאמר [גרסאות של מודלים](#model-versions). מודלים של Gemini 3.x תומכים בכמה יכולות מתקדמות:

- **תמיכה בסביבות מרובות:** אפשר ליצור סוכנים לסביבות [דפדפן, נייד ומחשב](#supported-environments).
- **פעולות יעילות עם כוונות:** הפעולות כוללות שדה `intent` שמסביר את ההיגיון של המודל מאחורי כל שלב.
- **מדיניות בטיחות שאפשר להגדיר:** אפשר לשנות את [התנהגות הבטיחות](#safety-policies) באמצעות קטגוריות מדיניות מובנות ושינויים בהגדרות ברירת המחדל.
- **זיהוי הזרקת הנחיות:** הפעלה של [סריקת צילומי מסך](#prompt-injection) כדי לזהות הוראות נסתרות של יריבים.

באמצעות 'שימוש במחשב', אפשר ליצור סוכנים ש:

- להפוך לאוטומטית משימות חוזרות של הזנת נתונים או מילוי טפסים באתרים.
- ביצוע בדיקות אוטומטיות של אפליקציות אינטרנט ותהליכי משתמש
- ביצוע מחקר באתרים שונים (למשל, איסוף מידע על מוצרים, מחירים וביקורות מאתרי מסחר אלקטרוני כדי לקבל החלטה לגבי רכישה)

הנה דוגמה מינימלית לאתחול הלקוח ושליחת הנחיה למודל עם הכלי `computer_use` שמופעל בסביבת דפדפן:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
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
  model: 'gemini-3.6-flash',
  input: "Search for 'Gemini API' on Google.",
  tools: [{ type: "computer_use", environment: "browser" }]
});

console.log(interaction);
```

## איך פועלת התכונה 'שימוש במחשב'

כדי ליצור סוכן באמצעות מודל השימוש במחשב, צריך להגדיר לולאה רציפה בין האפליקציה לבין ה-API. מה הקוד יעשה בכל שלב:

1. [**שליחת בקשה למודל**](#send-request)
   - האפליקציה שולחת בקשת API שמכילה את הכלי לשימוש במחשב, את הגדרות התצורה (כמו סביבת היעד), את ההנחיה של המשתמש וצילום מסך של המסך הנוכחי.
2. [**קבלת התשובה של המודל**](#model-response)
   - המודל מנתח את המסך ואת ההנחיה ומחזיר תשובה שכוללת `function_call` שמייצג פעולה בממשק המשתמש (כמו לחיצה, גלילה או הקשה על מקש).
   - ב**מודלים של Gemini 3.x**, התשובה כוללת גם הסבר `intent`
     למה המודל בחר בפעולה הזו.
   - התגובה עשויה לכלול גם `safety_decision` ממערכת בטיחות פנימית שמסווגת את הפעולה כרגילה/מותרת, `require_confirmation` (נדרש אישור משתמש) או חסומה.
3. [**מבצעים את הפעולה שהתקבלה**](#execute-actions)
   - אם הפעולה מותרת (או שהמשתמש מאשר אותה), הקוד בצד הלקוח מנתח את `function_call`, משנה את קנה המידה של הקואורדינטות המנורמלות כך שיתאימו לאזור התצוגה, ומבצע את הפעולה בסביבת היעד באמצעות כלי אוטומציה (כמו Playwright). אם הפעולה חסומה, הלקוח צריך להפסיק את ההפעלה או לטפל בהפרעה.
4. [**תיעוד המצב של הסביבה החדשה**](#capture-state)
   - אחרי שהפעולה מסתיימת, האפליקציה מצלמת צילום מסך חדש ושולחת אותו בחזרה למודל ב-`function_result` כדי לבקש את השלב הבא.

התהליך הזה חוזר על עצמו משלב 2, והמודל מתבקש שוב ושוב לבצע את הפעולה הבאה עד שהמשימה מסתיימת או שהתהליך מופסק.

![סקירה כללית על שימוש במחשב](https://ai.google.dev/static/gemini-api/docs/images/computer_use.png?hl=he)

## איך מטמיעים את התכונה 'שימוש במחשב'

לפני שמתחילים להשתמש בכלי 'שימוש במחשב', צריך להגדיר:

- **סביבת ביצוע מאובטחת:** מריצים את הסוכן במכונה וירטואלית או במאגר מבודד כדי לבודד אותו ממערכת המארח ולהגביל את ההשפעה הפוטנציאלית שלו.
  [הטמעה לדוגמה](https://github.com/google/computer-use-preview/) כוללת ארגז חול מבוסס Docker שמוכן לשימוש, ואפשר להשתמש בו כנקודת התחלה.
- **הנדלר של פעולות מצד הלקוח:** הטמעת לוגיקה מצד הלקוח כדי להפעיל קואורדינטות, להקליד טקסט ולצלם צילומי מסך.

בדוגמאות שבהמשך נעשה שימוש בדפדפן אינטרנט כסביבת ההפעלה וב-[Playwright](https://playwright.dev/) כמטפל בצד הלקוח.

### ‫0. הגדרת Playwright

קודם כול, מתקינים את החבילות הנדרשות:

```
pip install google-genai playwright
playwright install chromium
```

לאחר מכן, מאתחלים מופע של דפדפן Playwright לשימוש בהרצה:

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

### 1. שליחת בקשה למודל

מאתחלים את ספריית הלקוח ומגדירים את הכלי 'שימוש במחשב'. שימו לב: אין צורך לציין את גודל התצוגה כששולחים בקשה. המודל חוזה את קואורדינטות הפיקסלים שמותאמות לגובה ולרוחב של המסך.

### ‫Gemini 3.x

### Python

משתמשים ב-`google-genai` Python SDK (גרסה `2.7.0` ואילך) כדי להגדיר בקשה לטירגוט סביבת הדפדפן:

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model='gemini-3.6-flash',
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

משתמשים ב-Node.js SDK‏ `@google/genai` כדי להגדיר בקשה שמטרגטת את סביבת הדפדפן:

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI();

const interaction = await ai.interactions.create({
  model: 'gemini-3.6-flash',
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

משתמשים ב-curl כדי לשלוח בקשה:

```
curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.6-flash",
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

### ‫Gemini 2.5 (גרסה מדור קודם)

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

### 2. קבלת התשובה מהמודל

מודל התגובה מציע קריאה לפונקציה. ב**מודלים של Gemini 3.x**, התשובה מכילה כוונת חשיבה רציונלית מותאמת אישית לצד קואורדינטות. בדוגמאות הבאות אפשר לראות את שתי התגובות:

### ‫Gemini 3.x

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

### ‫Gemini 2.5 (גרסה מדור קודם)

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

### 3. ביצוע הפעולות שהתקבלו

האפליקציה צריכה לנתח את קואורדינטות התגובה, לבצע את הפעולה ולשנות את קנה המידה שלהן מקואורדינטות נורמליות של 1,000x1,000.

הקוד שלמטה מטפל גם בפקודות של כלי מדור קודם (`click_at`, `type_text_at`) וגם בפקודות מודרניות יעילות (`click`, `type`).

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

### 4. תיעוד מצב הסביבה החדש

אחרי שמבצעים את הפעולות, שולחים את התוצאה של הפעלת הפונקציה בחזרה למודל כדי שהוא יוכל להשתמש במידע הזה כדי ליצור את הפעולה הבאה. אם בוצעו כמה פעולות (קריאות מקבילות), צריך לשלוח `function_result` לכל אחת מהן בתור הבא של המשתמש.

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

אחרי שמגדירים איך ללכוד ולעצב את מצב הסביבה, אפשר לשלב את כל השלבים האלה בלולאת ביצוע רציפה.

## יצירת לופ של סוכן

כדי להפעיל אינטראקציות מרובות שלבים, משלבים את ארבעת השלבים מהקטע [איך מטמיעים את התכונה 'שימוש במחשב'](#implement-computer-use) בלולאה אחת.
הלולאה הזו ממשיכה לבקש פעולות ולהעביר את התוצאות בחזרה למודל עד שהמשימה מסתיימת.

חשוב לזכור לנהל את היסטוריית השיחות בצורה נכונה על ידי הוספת התשובות של המודל והתשובות של הפונקציה להיסטוריה בכל שלב.

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
        model='gemini-3.6-flash',
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
            model='gemini-3.6-flash',
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
        model: 'gemini-3.6-flash',
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
            model: 'gemini-3.6-flash',
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

## סביבות נתמכות (Gemini 3.x)

מודלים של Gemini 3.x תומכים בשלוש סביבות שמוגדרות ב`computer_use`הגדרות:

### סביבת הדפדפן (`ENVIRONMENT_BROWSER`)

הפעולות הזמינות בכלי הדפדפן:

| שם הפקודה | תיאור | ארגומנטים (בבקשה להפעלת פונקציה) |
| --- | --- | --- |
| **קליק** | קליקים שמאליים בקואורדינטה. | ‫`y`: int (0-999) `x`: int (0-999) `intent`: str |
| **double\_click** | לחיצות כפולות על הקואורדינטה. | ‫`y`: int (0-999) `x`: int (0-999) `intent`: str |
| **triple\_click** | שלוש לחיצות על הקואורדינטה. | ‫`y`: int (0-999) `x`: int (0-999) `intent`: str |
| **middle\_click** | לחיצה אמצעית על הקואורדינטה. | ‫`y`: int (0-999) `x`: int (0-999) `intent`: str |
| **right\_click** | לחיצות ימניות בקואורדינטה. | ‫`y`: int (0-999) `x`: int (0-999) `intent`: str |
| **mouse\_down** | לחיצה ארוכה על כפתור העכבר בקואורדינטה. | ‫`y`: int (0-999) `x`: int (0-999) `intent`: str |
| **mouse\_up** | משחרר את כפתור העכבר בקואורדינטה. | ‫`y`: int (0-999) `x`: int (0-999) `intent`: str |
| **העברה** | העברת הסמן למיקום שצוין. | ‫`y`: int (0-999) `x`: int (0-999) `intent`: str |
| **type** | הקלדת טקסט. | `text`: str `press_enter`: bool (Optional, default `false`) `intent`: str |
| **drag\_and\_drop** | גורר פריט מקואורדינטת ההתחלה לקואורדינטת הסיום. | ‫`start_y`: int (0-999) `start_x`: int (0-999) `end_y`: int (0-999) `end_x`: int (0-999) `intent`: str |
| **wait** | הפסקת ההרצה למספר שניות שצוין. | ‫`seconds`: int (אופציונלי, ברירת מחדל `1`) `intent`: str |
| **press\_key** | לחיצה על המקש שצוין ושחרור שלו. | ‫`key`: str `intent`: str |
| **key\_down** | לחיצה ארוכה על המקש שצוין. | ‫`key`: str `intent`: str |
| **key\_up** | משחרר את המקש שצוין. | ‫`key`: str `intent`: str |
| **מקש קיצור** | לחיצה על שילוב המקשים שצוין. | `keys`: `List[str]` `intent`: `str` |
| **take\_screenshot** | מחזירה צילום מסך של המסך הנוכחי. | `intent`: str |
| **scroll** | גלילה למעלה, למטה, שמאלה או ימינה בנקודה מסוימת בפיקסל אחד. | ‫`y`: int (0-999) `x`: int (0-999) `direction`: str (`"up"`, `"down"`, `"left"`, `"right"`) `magnitude_in_pixels`: int (0-999, Optional, default `300`) `intent`: str |
| **go\_back** | חזרה לדף האינטרנט הקודם בהיסטוריית הדפדפן. | `intent`: str |
| **navigate** | ניווט ישירות לכתובת URL ספציפית. | ‫`url`: str `intent`: str |
| **go\_forward** | מעבר קדימה לדף האינטרנט הבא בהיסטוריית הגלישה. | `intent`: str |

### סביבה לנייד (`ENVIRONMENT_MOBILE`)

פעולות בסביבה שעברה אופטימיזציה ל-Android:

| שם הפקודה | תיאור | ארגומנטים (בבקשה להפעלת פונקציה) |
| --- | --- | --- |
| **open\_app** | פותח אפליקציה לפי השם שלה. | ‫`app_name`: str `intent`: str |
| **קליק** | קליקים שמאליים בקואורדינטה. | ‫`y`: int (0-999) `x`: int (0-999) `intent`: str |
| **list\_apps** | מציג את האפליקציות שזמינות במכשיר ומחזיר את השמות ושמות החבילות שלהן. | `intent`: str |
| **wait** | הפסקת ההרצה למספר שניות שצוין. | ‫`seconds`: int (אופציונלי, ברירת מחדל `1`) `intent`: str |
| **go\_back** | חזרה למסך הקודם או לדף האינטרנט הקודם. | `intent`: str |
| **type** | הקלדת טקסט. | `text`: str `press_enter`: bool (Optional, default `false`) `intent`: str |
| **drag\_and\_drop** | גורר פריט מקואורדינטת ההתחלה לקואורדינטת הסיום. | ‫`start_y`: int (0-999) `start_x`: int (0-999) `end_y`: int (0-999) `end_x`: int (0-999) `intent`: str |
| **long\_press** | מבצע לחיצה ארוכה בקואורדינטה במסך. | ‫`y`: int (0-999) `x`: int (0-999) `seconds`: int (אופציונלי, ברירת מחדל `2`) `intent`: str |
| **press\_key** | לחיצה על המקש שצוין ושחרור שלו. | ‫`key`: str `intent`: str |
| **take\_screenshot** | מחזירה צילום מסך של המסך הנוכחי. | `intent`: str |

### סביבת שולחן עבודה (`ENVIRONMENT_DESKTOP`)

פקודות של סמן ברמת מערכת ההפעלה בסביבות שולחן עבודה:

| שם הפקודה | תיאור | ארגומנטים (בבקשה להפעלת פונקציה) |
| --- | --- | --- |
| **קליק** | קליקים שמאליים בקואורדינטה. | ‫`y`: int (0-999) `x`: int (0-999) `intent`: str |
| **double\_click** | לחיצות כפולות על הקואורדינטה. | ‫`y`: int (0-999) `x`: int (0-999) `intent`: str |
| **triple\_click** | שלוש לחיצות על הקואורדינטה. | ‫`y`: int (0-999) `x`: int (0-999) `intent`: str |
| **middle\_click** | לחיצה אמצעית על הקואורדינטה. | ‫`y`: int (0-999) `x`: int (0-999) `intent`: str |
| **right\_click** | לחיצות ימניות בקואורדינטה. | ‫`y`: int (0-999) `x`: int (0-999) `intent`: str |
| **mouse\_down** | לחיצה ארוכה על כפתור העכבר בקואורדינטה. | ‫`y`: int (0-999) `x`: int (0-999) `intent`: str |
| **mouse\_up** | משחרר את כפתור העכבר בקואורדינטה. | ‫`y`: int (0-999) `x`: int (0-999) `intent`: str |
| **העברה** | העברת הסמן למיקום שצוין. | ‫`y`: int (0-999) `x`: int (0-999) `intent`: str |
| **type** | הקלדת טקסט. | `text`: str `press_enter`: bool (Optional, default `false`) `intent`: str |
| **drag\_and\_drop** | גורר פריט מקואורדינטת ההתחלה לקואורדינטת הסיום. | ‫`start_y`: int (0-999) `start_x`: int (0-999) `end_y`: int (0-999) `end_x`: int (0-999) `intent`: str |
| **wait** | הפסקת ההרצה למספר שניות שצוין. | ‫`seconds`: int (אופציונלי, ברירת מחדל `1`) `intent`: str |
| **press\_key** | לחיצה על המקש שצוין ושחרור שלו. | ‫`key`: str `intent`: str |
| **key\_down** | לחיצה ארוכה על המקש שצוין. | ‫`key`: str `intent`: str |
| **key\_up** | משחרר את המקש שצוין. | ‫`key`: str `intent`: str |
| **מקש קיצור** | לחיצה על שילוב המקשים שצוין. | `keys`: `List[str]` `intent`: `str` |
| **take\_screenshot** | מחזירה צילום מסך של המסך הנוכחי. | `intent`: str |
| **scroll** | גלילה למעלה, למטה, שמאלה או ימינה בנקודה מסוימת בפיקסל אחד. | ‫`y`: int (0-999) `x`: int (0-999) `direction`: str (`"up"`, `"down"`, `"left"`, `"right"`) `magnitude_in_pixels`: int (0-999, Optional, default `300`) `intent`: str |

## פעולות נתמכות בממשק המשתמש מדור קודם (Gemini 2.5)

במודלים מדור קודם (`gemini-2.5-computer-use-preview-10-2025`), הפעולות הבאות נתמכות:

| שם הפקודה | תיאור | ארגומנטים (בבקשה להפעלת פונקציה) | דוגמה לבקשה להפעלת פונקציה |
| --- | --- | --- | --- |
| **open\_web\_browser** | הפעולה הזו תפתח את דפדפן האינטרנט. | ללא | `{"name": "open_web_browser", "arguments": {}}` |
| **wait\_5\_seconds** | ההרצה מושהית למשך 5 שניות. | ללא | `{"name": "wait_5_seconds", "arguments": {}}` |
| **go\_back** | מעבר לדף הקודם בהיסטוריה. | ללא | `{"name": "go_back", "arguments": {}}` |
| **go\_forward** | מעבר לדף הבא בהיסטוריה. | ללא | `{"name": "go_forward", "arguments": {}}` |
| **search** | עוברים למנוע החיפוש שמוגדר כברירת מחדל. | ללא | `{"name": "search", "arguments": {}}` |
| **navigate** | הדפדפן עובר ישירות לכתובת ה-URL שצוינה. | `url`: str | `{"name": "navigate", "arguments": {"url": "https://www.wikipedia.org"}}` |
| **click\_at** | קליקים בקואורדינטה ספציפית. | ‫`y`: int (0-999), `x`: int (0-999) | `{"name": "click_at", "arguments": {"y": 300, "x": 500}}` |
| **hover\_at** | העכבר מרחף בקואורדינטה ספציפית. | ‫`y`: int (0-999), `x`: int (0-999) | `{"name": "hover_at", "arguments": {"y": 150, "x": 250}}` |
| **type\_text\_at** | הקלדת טקסט בקואורדינטה. | ‫`y`: int (0-999), `x`: int (0-999), `text`: str, `press_enter`: bool (אופציונלי, ברירת המחדל היא True), `clear_before_typing`: bool (אופציונלי, ברירת המחדל היא True) | `{"name": "type_text_at", "arguments": {"y": 250, "x": 400, "text": "search", "press_enter": false}}` |
| **key\_combination** | לוחצים על מקשים או על שילובים של מקשים. | `keys`: str | `{"name": "key_combination", "arguments": {"keys": "Control+A"}}` |
| **scroll\_document** | גלילה בכל דף האינטרנט. | `direction`: str | `{"name": "scroll_document", "arguments": {"direction": "down"}}` |
| **scroll\_at** | גלילה בקואורדינטות (x,y). | ‫`y`: int, `x`: int, `direction`: str, `magnitude`: int (אופציונלי, ברירת מחדל 800) | `{"name": "scroll_at", "arguments": {"y": 500, "x": 500, "direction": "down"}}` |
| **drag\_and\_drop** | גרירה בין שתי קואורדינטות. | ‫`y`: int, `x`: int, `destination_y`: int, `destination_x`: int | `{"name": "drag_and_drop", "arguments": {"y": 100, "destination_y": 500, "destination_x": 500, "x": 100}}` |

## פונקציות מותאמות אישית בהגדרת המשתמש

אפשר להרחיב את הפונקציונליות של המודל באמצעות פונקציות מותאמות אישית בהגדרת המשתמש. לדוגמה, בתרחישים של התערבות אנושית (HITL), אפשר להחריג פעולות מוגדרות מראש ולרשום פעולות בהתאמה אישית.

#### כלים מותאמים אישית של Gemini 3.x

### Python

להחריג פעולות סטנדרטיות שהוגדרו מראש בדפדפן (כמו `click`) ולרשום כלי מותאם אישית `yield_to_user`:

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
    model="gemini-3.6-flash",
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

להחריג פעולות סטנדרטיות שהוגדרו מראש בדפדפן (כמו `click`) ולרשום כלי מותאם אישית `yield_to_user`:

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
    model: "gemini-3.6-flash",
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

#### כלים מותאמים אישית של Gemini 2.5 (גרסה מדור קודם)

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

## ניהול רמות ההעמקה (Gemini 3.x)

בסוכנים לשימוש במחשב, אפשר להגדיר רמות חשיבה שונות כדי ליצור איזון בין איכות הפעולה למהירות הביצוע. בדרך כלל, רמות חשיבה נמוכות יותר מאפשרות להשיג איזון טוב במשימות אוטומציה רגילות.

## בטיחות ואבטחה

### הגדרת מדיניות בנושא בטיחות (Gemini 3.x)

מודלים של Gemini 3.x כוללים קטגוריות מובנות של שירותי בטיחות שקובעות באופן אוטומטי אם נדרש אישור מהמשתמש.

| קטגוריית מדיניות בנושא בטיחות | תיאור |
| --- | --- |
| `FINANCIAL_TRANSACTIONS` | חסימה או הפעלה של אישור לפעולות שקשורות לתשלומים, לתהליך התשלום בקמעונאות או למוצרים מפוקחים. |
| `SENSITIVE_DATA_MODIFICATION` | הגנה על רשומות בריאותיות, פיננסיות או ממשלתיות מפני שינויים לא מורשים. |
| `COMMUNICATION_TOOL` | הגבלה של הסוכן כך שלא יוכל לשלוח אימיילים, הודעות צ'אט או טיוטות באופן אוטונומי. |
| `ACCOUNT_CREATION` | ההגדרה הזו מגבילה את היכולת של הסוכן לרשום באופן אוטונומי חשבונות חדשים באתרים. |
| `DATA_MODIFICATION` | ההרשאה הזו מסדירה שינויים במערכת הקבצים, שיתוף נתונים ומחיקת אחסון. |
| `USER_CONSENT_MANAGEMENT` | נדרשת השתלטות על המשתמשים כדי להציג באנרים לבקשת הסכמה לשימוש בקובצי Cookie והודעות בנושא פרטיות. |
| `LEGAL_TERMS_AND_AGREEMENTS` | מונעת מהמודל לאשר באופן אוטונומי תנאים והגבלות או חוזים מחייבים מבחינה משפטית. |

#### שינויים בהגדרות האבטחה

אפשר לשנות מדיניות ספציפית על ידי העברת שינויים:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
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
    model: "gemini-3.6-flash",
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

### זיהוי החדרת פרומפטים (Gemini 3.x)

מנגנון בטיחות אופציונלי שסורק פיקסלים בצילומי מסך כדי לזהות הוראות פרומפט זדוני נסתרות (למשל, 'התעלם מהפקודות הקודמות') וחוסם את הביצוע שלהן אם הן מזוהות.

### אישור החלטה בנושא בטיחות

התשובה יכולה לכלול את הפרמטר `safety_decision` בארגומנטים של קריאת הפונקציה:

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

אם הערך של `safety_decision` הוא `require_confirmation`, מציגים למשתמש הקצה הנחיה. אם המשתמש מאשר, מגדירים את `safety_acknowledgement` ב-`function_result`.

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

### שיטות מומלצות לשמירה על האבטחה

שימוש במחשב מציב סיכוני אבטחה ותפעול ייחודיים, כי מודל שפועל בשם משתמש עלול להיתקל בתוכן לא מהימן במסכים או לבצע שגיאות בהפעלת פעולות. כדי להגן על נתוני המשתמשים ועל המערכות, מומלץ להטמיע את השיטות המומלצות הבאות:

1. **Human-in-the-Loop (HITL):**

   - **אכיפת אישור המשתמש:** אם התגובה בנושא בטיחות מציינת
     `require_confirmation` (או אם נדרש אישור לפי החלטת הבטיחות הקודמת), המשתמש יתבקש לאשר.
   - **הוספת הוראות בטיחות בהתאמה אישית:** אפשר להטמיע הוראות מערכת בהתאמה אישית כדי להגדיר ולאכוף את גבולות הבטיחות שלכם. לדוגמה:

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
         model="gemini-3.6-flash",
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
         model: "gemini-3.6-flash",
         system_instruction: systemInstruction,
         input: "Prepare a draft but do not send.",
         tools: [{
             type: "computer_use",
             environment: "browser"
         }]
     });
     ```
2. **סביבת ביצוע מאובטחת:** הפעלת הסוכן בסביבה מאובטחת של ארגז חול כדי להגביל את ההשפעה הפוטנציאלית שלו. יכול להיות שמדובר במכונה וירטואלית (VM) בסביבת ארגז חול, בקונטיינר (למשל, Docker) או בפרופיל דפדפן ייעודי עם הרשאות מוגבלות. הוראות להגדרת ארגז חול באמצעות Docker מופיעות ב[הטמעה לדוגמה ב-GitHub](https://github.com/google/computer-use-preview/).
3. **ניקוי קלט:** ניקוי של כל הטקסט שנוצר על ידי משתמשים בהנחיות, כדי לצמצם את הסיכון להוראות לא מכוונות או להחדרת פרומפטים. זו שכבת אבטחה מועילה, אבל היא לא תחליף לסביבת ביצוע מאובטחת.
4. **אמצעי הגנה על תוכן:** אפשר להשתמש באמצעי הגנה ובממשקי API של בטיחות תוכן כדי להעריך את הקלט של המשתמשים, את הקלט והפלט של כלי העזר ואת התשובות של הסוכן, ולבדוק אם הם מתאימים, אם יש בהם הזרקת הנחיות ואם הם מאפשרים עקיפת הגבלות.
5. **רשימות היתרים ורשימות חסימה:** כדאי להטמיע מנגנוני סינון כדי לשלוט במקומות שבהם המודל יכול לנווט ובפעולות שהוא יכול לבצע. רשימת חסימה של אתרים אסורים היא נקודת התחלה טובה, אבל רשימת היתרים מגבילה יותר היא מאובטחת עוד יותר.
6. **יכולת מעקב ורישום ביומן:** שמירה של יומנים מפורטים לצורך ניפוי באגים, ביקורת ותגובה לאירועים. הלקוח צריך לתעד הנחיות, צילומי מסך, פעולות שהמודל מציע (`function_call`), תשובות שקשורות לבטיחות וכל הפעולות שהלקוח מבצע בסופו של דבר.
7. **ניהול סביבה:** מוודאים שהסביבה של ממשק המשתמש הגרפי עקבית.
   חלונות קופצים, התראות או שינויים בפריסה שלא ציפיתם להם עלולים לבלבל את המודל. אם אפשר, מתחילים ממצב נקי ומוכר לכל משימה חדשה.

## גרסאות המודלים

אפשר להשתמש ב'שימוש במחשב' עם הדגמים הבאים:

- ‫[**Gemini 3.6 Flash**](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=he) (`gemini-3.6-flash`): המודל המומלץ לשימוש במחשב, עם פעולות יעילות באמצעות כוונות, תמיכה בסביבות דפדפן, נייד ומחשב, מדיניות אבטחה שניתנת להגדרה וזיהוי של הזרקת הנחיות.
- ‫[**Gemini 3.5 Flash-Lite**](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=he) (`gemini-3.5-flash-lite`): מודל חסכוני עם זמן אחזור נמוך, שתומך בשימוש במחשב.
- ‫[**Gemini 3.5 Flash**](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=he) (`gemini-3.5-flash`): מודל יציב קודם שתומך בשימוש במחשב.
- ‫[**Gemini 3 Flash Preview**](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=he) (`gemini-3-flash-preview`): מודל בתצוגה מקדימה
  עם תמיכה בשימוש במחשב.
- ‫[**Gemini 2.5 (גרסת טרום-השקה מדור קודם)**](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-computer-use-preview-10-2025?hl=he) (`gemini-2.5-computer-use-preview-10-2025`): מודל טרום-השקה מדור קודם שעבר אופטימיזציה לשימוש במחשב מבוסס-דפדפן.

## המאמרים הבאים

- אפשר להתנסות בשימוש במחשב ב[סביבת ההדגמה של Browserbase](http://gemini.browserbase.com).
- בדף [Reference implementation](https://github.com/google/computer-use-preview) יש דוגמאות לקוד.
- מידע על כלים אחרים של Gemini API:
  - [בקשה להפעלת פונקציה](https://ai.google.dev/gemini-api/docs/function-calling?hl=he)
  - [עיגון באמצעות חיפוש Google](https://ai.google.dev/gemini-api/docs/google-search?hl=he)

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-07-23 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-07-23 (שעון UTC)."],[],[]]
