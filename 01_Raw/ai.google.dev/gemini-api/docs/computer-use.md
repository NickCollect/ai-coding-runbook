---
source_url: https://ai.google.dev/gemini-api/docs/computer-use?hl=he
fetched_at: 2026-05-05T20:48:40.129315+00:00
title: "\u05e9\u05d9\u05de\u05d5\u05e9 \u05d1\u05de\u05d7\u05e9\u05d1 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=he) זמין עכשיו בתצוגה מקדימה עם תכונות כמו תכנון שיתופי, ויזואליזציה, תמיכה ב-MCP ועוד.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# שימוש במחשב

התכונה 'שימוש במחשב' מאפשרת לכם ליצור סוכנים לשליטה בדפדפן שמבצעים אינטראקציה עם משימות והופכים אותן לאוטומטיות. באמצעות צילומי מסך, המודל יכול 'לראות' מסך מחשב ו'לפעול' על ידי יצירת פעולות ספציפיות בממשק המשתמש, כמו קליקים בעכבר וקלט מהמקלדת. בדומה לקריאה לפונקציה, צריך לכתוב את קוד האפליקציה בצד הלקוח כדי לקבל ולהפעיל את הפעולות של השימוש במחשב.

באמצעות 'שימוש במחשב', אתם יכולים ליצור סוכנים שיכולים:

- להפוך לאוטומטיות משימות חוזרות של הזנת נתונים או מילוי טפסים באתרים.
- ביצוע בדיקות אוטומטיות של אפליקציות אינטרנט ותהליכי משתמש
- עריכת מחקר באתרים שונים (למשל, איסוף מידע על מוצרים, מחירים וביקורות מאתרי מסחר אלקטרוני כדי לקבל החלטה לגבי רכישה)

הדרך הקלה ביותר לבדוק את היכולת 'שימוש במחשב' היא באמצעות [הטמעה לדוגמה](https://github.com/google/computer-use-preview/) או [סביבת הדגמה של Browserbase](http://gemini.browserbase.com).

## איך פועלת התכונה 'שימוש במחשב'

כדי ליצור סוכן לשליטה בדפדפן באמצעות מודל השימוש במחשב, צריך להטמיע לולאת סוכן שמבצעת את הפעולות הבאות:

1. [**שליחת בקשה למודל**](#send-request)

   - מוסיפים את הכלי Computer Use (שימוש במחשב) ואם רוצים, גם פונקציות מותאמות אישית שהוגדרו על ידי המשתמש או פונקציות שהוחרגו לבקשת ה-API.
   - מזינים את הבקשה של המשתמש למודל Computer Use.
2. [**קבלת התשובה של המודל**](#model-response)

   - מודל השימוש במחשב מנתח את בקשת המשתמש ואת צילום המסך, ומפיק תשובה שכוללת הצעה ל`function_call` שמייצגת פעולת ממשק משתמש (למשל, 'לחיצה על הקואורדינטות (x,y)' או 'הקלדת הטקסט'). תיאור של כל הפעולות בממשק המשתמש שנתמכות על ידי מודל השימוש במחשב מופיע במאמר [פעולות נתמכות](#supported-actions).
   - תשובת ה-API עשויה לכלול גם `safety_decision` ממערכת בטיחות פנימית שבודקת את הפעולה המוצעת של המודל. התג הזה
     `safety_decision` מסווג את הפעולה כ:
     - **רגילה / מותרת:** הפעולה נחשבת בטוחה. יכול להיות גם שלא יופיע `safety_decision`.
     - **נדרש אישור (`require_confirmation`):** המודל עומד לבצע פעולה שיכולה להיות מסוכנת (למשל, לחיצה על 'הודעה על שימוש בקובצי Cookie').
3. [**ביצוע הפעולה שהתקבלה**](#execute-actions)

   - הקוד בצד הלקוח מקבל את הערך `function_call` ואת כל הערכים הנלווים `safety_decision`.
     - **רגיל / מותר:** אם `safety_decision` מציין רגיל / מותר (או אם לא מופיע `safety_decision`), קוד בצד הלקוח יכול להפעיל את `function_call` שצוין בסביבת היעד (למשל, דפדפן אינטרנט).
     - **נדרש אישור:** אם ב-`safety_decision` מצוין שנדרש אישור, האפליקציה צריכה לבקש מהמשתמש אישור לפני שהיא מבצעת את `function_call`. אם המשתמש מאשר, ממשיכים לבצע את הפעולה. אם המשתמש מסרב, אל תבצע את הפעולה.
4. [**תיעוד המצב של הסביבה החדשה**](#capture-state)

   - אם הפעולה בוצעה, הלקוח מצלם צילום מסך חדש של ממשק המשתמש הגרפי ושל כתובת ה-URL הנוכחית כדי לשלוח אותם בחזרה למודל Computer Use כחלק מ`function_response`.
   - אם פעולה נחסמה על ידי מערכת הבטיחות או שהמשתמש סירב לאשר אותה, יכול להיות שהאפליקציה תשלח למודל סוג אחר של משוב או תסיים את האינטראקציה.

התהליך הזה חוזר על עצמו משלב 2, כשהמודל משתמש בצילום המסך החדש וביעד המתמשך כדי להציע את הפעולה הבאה. הלולאה ממשיכה עד שהמשימה מסתיימת, מתרחשת שגיאה או שהתהליך מסתיים (למשל, בגלל תגובת בטיחות של 'חסימה' או החלטה של המשתמש).

![סקירה כללית על שימוש במחשב](https://ai.google.dev/static/gemini-api/docs/images/computer_use.png?hl=he)

## איך מטמיעים את התכונה 'שימוש במחשב'

לפני שמתחילים לפתח באמצעות הכלי לשימוש במחשב, צריך להגדיר את הדברים הבאים:

- **סביבת ביצוע מאובטחת:** מטעמי בטיחות, מומלץ להריץ את סוכן השימוש במחשב בסביבה מאובטחת ומבוקרת (למשל, מכונה וירטואלית בארגז חול, קונטיינר או פרופיל דפדפן ייעודי עם הרשאות מוגבלות).
- **מטפל בפעולות בצד הלקוח:** תצטרכו להטמיע לוגיקה בצד הלקוח כדי לבצע את הפעולות שהמודל יצר ולצלם צילומי מסך של הסביבה אחרי כל פעולה.

בדוגמאות שבקטע הזה נעשה שימוש בדפדפן כסביבת ההפעלה וב-[Playwright](https://playwright.dev/) כ-handler של פעולות בצד הלקוח. כדי להריץ את הדוגמאות האלה, צריך להתקין את הרכיבים התלויים הנדרשים ולהפעיל מופע של דפדפן Playwright.

#### התקנה של Playwright

```
    pip install google-genai playwright
    playwright install chromium
```

#### אתחול של מופע דפדפן Playwright

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

קוד לדוגמה להרחבה לסביבת Android מופיע בקטע [שימוש בפונקציות מותאמות אישית שהוגדרו על ידי המשתמש](#custom-functions).

### 1. שליחת בקשה למודל

מוסיפים את הכלי Computer Use לבקשת ה-API ושולחים הנחיה למודל שכוללת את המטרה של המשתמש. אתם צריכים להשתמש באחד מהמודלים הנתמכים לשימוש במחשב, אחרת תוצג לכם שגיאה:

- `gemini-2.5-computer-use-preview-10-2025`
- `gemini-3-flash-preview`

אפשר גם להוסיף את הפרמטרים הבאים:

- **פעולות מוחרגות:** אם יש פעולות מתוך רשימת [הפעולות הנתמכות בממשק המשתמש](#supported-actions) שאתם לא רוצים שהמודל יבצע, צריך לציין את הפעולות האלה כ-`excluded_predefined_functions`.
- **פונקציות בהגדרת המשתמש:** בנוסף לכלי 'שימוש במחשב', יכול להיות שתרצו לכלול פונקציות מותאמות אישית בהגדרת המשתמש.

שימו לב: אין צורך לציין את גודל התצוגה כשמגישים בקשה. המודל מנבא קואורדינטות של פיקסלים שמותאמות לגובה ולרוחב של המסך.

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

דוגמה לשימוש בפונקציות בהתאמה אישית מופיעה במאמר [שימוש בפונקציות מותאמות אישית שהוגדרו על ידי המשתמש](#custom-functions).

### 2. קבלת התשובה מהמודל

כשהכלי 'שימוש במחשב' מופעל, המודל יגיב עם `FunctionCalls` אחד או יותר אם הוא יקבע שצריך לבצע פעולות בממשק המשתמש כדי להשלים את המשימה.
השימוש במחשב תומך בהפעלת פונקציות מקבילית, כלומר המודל יכול להחזיר כמה פעולות בתור אחד.

זוהי דוגמה לתשובה של מודל.

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

### 3. ביצוע הפעולות שהתקבלו

קוד האפליקציה צריך לנתח את תשובת המודל, לבצע את הפעולות ולאסוף את התוצאות.

קוד הדוגמה שבהמשך מחלץ קריאות לפונקציות מהתגובה של מודל Computer Use, ומתרגם אותן לפעולות שאפשר לבצע באמצעות Playwright.
המודל מוציא קואורדינטות מנורמלות (0-999) בלי קשר לממדים של תמונת הקלט, ולכן חלק משלב התרגום הוא המרה של הקואורדינטות המנורמלות האלה בחזרה לערכי פיקסלים בפועל.

גודל המסך המומלץ לשימוש במודל 'שימוש במחשב' הוא (1440, 900). המודל יפעל בכל רזולוציה, אבל יכול להיות שהאיכות של התוצאות תיפגע.

שימו לב שהדוגמה הזו כוללת רק את ההטמעה של 3 פעולות הממשק הנפוצות ביותר: `open_web_browser`, `click_at` ו-`type_text_at`. בתרחישי שימוש בסביבת ייצור, תצטרכו להטמיע את כל פעולות ממשק המשתמש האחרות מהרשימה [פעולות נתמכות](#supported-actions), אלא אם תוסיפו אותן באופן מפורש כ-`excluded_predefined_functions`.

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

### 4. תיעוד של מצב הסביבה החדש

אחרי שמבצעים את הפעולות, שולחים את התוצאה של הפעלת הפונקציה בחזרה למודל כדי שהוא יוכל להשתמש במידע הזה כדי ליצור את הפעולה הבאה. אם בוצעו כמה פעולות (קריאות מקבילות), צריך לשלוח `FunctionResponse` לכל אחת מהן בתור הבא של המשתמש.

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

## יצירת לופ של סוכן

כדי להפעיל אינטראקציות מרובות שלבים, משלבים את ארבעת השלבים מהקטע [איך מטמיעים את התכונה 'שימוש במחשב'](#implement-computer-use) בלולאה.
חשוב לזכור לנהל את היסטוריית השיחות בצורה נכונה על ידי הוספה של תשובות המודל ותשובות הפונקציה.

כדי להריץ את דוגמת הקוד הזו, צריך:

- מתקינים את [יחסי התלות הנדרשים של Playwright](#expandable-1).
- מגדירים את פונקציות העזר משלבים [(3) ביצוע הפעולות שהתקבלו](#execute-actions) ו[(4) תיעוד מצב הסביבה החדש](#capture-state).

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

## שימוש בפונקציות מותאמות אישית בהגדרת המשתמש

אפשר לכלול בבקשה פונקציות מותאמות אישית בהגדרת המשתמש כדי להרחיב את הפונקציונליות של המודל. בדוגמה שלמטה מותאם המודל והכלי Computer Use (שימוש במחשב) לתרחישי שימוש בנייד, על ידי הכללה של פעולות מותאמות אישית שהוגדרו על ידי המשתמש, כמו `open_app`, `long_press_at` ו-`go_home`, והחרגה של פעולות ספציפיות לדפדפן. המודל יכול להפעיל בצורה חכמה את הפונקציות המותאמות אישית האלה לצד פעולות סטנדרטיות בממשק המשתמש כדי להשלים משימות בסביבות שאינן דפדפן.

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

## פעולות נתמכות בממשק המשתמש

המודל יכול לבקש את פעולות ממשק המשתמש הבאות באמצעות `FunctionCall`. בקוד בצד הלקוח צריך להטמיע את לוגיקת הביצוע של הפעולות האלה. דוגמאות מופיעות ב[הטמעה לדוגמה](https://github.com/google/computer-use-preview).

| שם הפקודה | תיאור | ארגומנטים (בבקשה להפעלת פונקציה) | בקשה להפעלת פונקציה לדוגמה |
| --- | --- | --- | --- |
| **open\_web\_browser** | הדפדפן ייפתח. | ללא | `{"name": "open_web_browser", "args": {}}` |
| **wait\_5\_seconds** | הפונקציה מפסיקה את ההפעלה למשך 5 שניות כדי לאפשר לתוכן דינמי להיטען או לאנימציות להסתיים. | ללא | `{"name": "wait_5_seconds", "args": {}}` |
| **go\_back** | מעבר לדף הקודם בהיסטוריית הדפדפן. | ללא | `{"name": "go_back", "args": {}}` |
| **go\_forward** | מעבר לדף הבא בהיסטוריה של הדפדפן. | ללא | `{"name": "go_forward", "args": {}}` |
| **search** | ניווט לדף הבית של מנוע החיפוש שמוגדר כברירת מחדל (למשל, Google). האפשרות הזו שימושית כשרוצים להתחיל משימת חיפוש חדשה. | ללא | `{"name": "search", "args": {}}` |
| **navigate** | הדפדפן עובר ישירות לכתובת ה-URL שצוינה. | `url`: str | `{"name": "navigate", "args": {"url": "https://www.wikipedia.org"}}` |
| **click\_at** | קליקים בקואורדינטה ספציפית בדף האינטרנט. הערכים של x ו-y מבוססים על רשת של 1,000x1,000 ומוגדרים בהתאם למידות המסך. | ‫`y`: int (0-999), `x`: int (0-999) | `{"name": "click_at", "args": {"y": 300, "x": 500}}` |
| **hover\_at** | מציב את סמן העכבר בקואורדינטה ספציפית בדף האינטרנט. הערכים האלה שימושיים להצגת תפריטי משנה. הערכים x ו-y מבוססים על רשת של 1,000x1,000. | ‫`y`: int (0-999) `x`: int (0-999) | `{"name": "hover_at", "args": {"y": 150, "x": 250}}` |
| **type\_text\_at** | מקליד טקסט בקואורדינטה ספציפית. כברירת מחדל, הפעולה מוחקת קודם את השדה ומקישה על ENTER אחרי ההקלדה, אבל אפשר להשבית את הפעולות האלה. הערכים של x ו-y מבוססים על רשת של 1,000x1,000. | ‫`y`: int (0-999), `x`: int (0-999), `text`: str, `press_enter`: bool (אופציונלי, ברירת המחדל היא True), `clear_before_typing`: bool (אופציונלי, ברירת המחדל היא True) | `{"name": "type_text_at", "args": {"y": 250, "x": 400, "text": "search query", "press_enter": false}}` |
| **key\_combination** | מקישים על מקשים או על שילובים של מקשים במקלדת, כמו Control+C או Enter. האפשרות הזו שימושית להפעלת פעולות (כמו שליחת טופס באמצעות Enter) או פעולות בלוח העריכה. | ‫`keys`: מחרוזת (למשל 'enter',‏ 'control+c'). | `{"name": "key_combination", "args": {"keys": "Control+A"}}` |
| **scroll\_document** | גלילה של כל דף האינטרנט למעלה, למטה, שמאלה או ימינה. | ‫`direction`: str ("up",‏ "down",‏ "left" או "right") | `{"name": "scroll_document", "args": {"direction": "down"}}` |
| **scroll\_at** | מגלגלת רכיב או אזור ספציפיים בנקודה (x, y) בכיוון שצוין, במידה מסוימת. הקואורדינטות והגודל (ברירת מחדל 800) מבוססים על רשת של 1,000x1,000. | ‫`y`: int (0-999), `x`: int (0-999), `direction`: str ("up", "down", "left", "right"), `magnitude`: int (0-999, Optional, default 800) | `{"name": "scroll_at", "args": {"y": 500, "x": 500, "direction": "down", "magnitude": 400}}` |
| **drag\_and\_drop** | גורר רכיב מקואורדינטת התחלה (x, y) ומשחרר אותו בקואורדינטת יעד (destination\_x, destination\_y). כל הקואורדינטות מבוססות על רשת בגודל 1,000x1,000. | ‫`y`: int (0-999), `x`: int (0-999), `destination_y`: int (0-999), `destination_x`: int (0-999) | `{"name": "drag_and_drop", "args": {"y": 100, "x": 100, "destination_y": 500, "destination_x": 500}}` |

## בטיחות ואבטחה

### אישור החלטה בנושא בטיחות

בהתאם לפעולה, התשובה של המודל עשויה לכלול גם `safety_decision` ממערכת בטיחות פנימית שבודקת את הפעולה המוצעת של המודל.

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

אם הערך של `safety_decision` הוא `require_confirmation`, צריך לבקש אישור ממשתמש הקצה לפני שממשיכים בהפעלת הפעולה. בהתאם [לתנאים ולהגבלות](https://ai.google.dev/gemini-api/terms?hl=he), אסור לך לעקוף בקשות לאימות שאתה אדם.

בדוגמת הקוד הזו, המשתמש מתבקש לאשר את הפעולה לפני שהיא מבוצעת. אם המשתמש לא מאשר את הפעולה, הלולאה מסתיימת. אם המשתמש מאשר את הפעולה, הפעולה מבוצעת והשדה `safety_acknowledgement` מסומן כ-`True`.

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

אם המשתמש מאשר, צריך לכלול את אישור הבטיחות ב`FunctionResponse`.

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

### שיטות מומלצות לשמירה על האבטחה

השימוש במחשב הוא כלי חדש שמציג סיכונים חדשים שמפתחים צריכים להיות מודעים להם:

- **תוכן לא מהימן ותרמיות:** כדי להשיג את המטרה של המשתמש, המודל עשוי להסתמך על מקורות מידע לא מהימנים ועל הוראות מהמסך. לדוגמה, אם המטרה של המשתמש היא לרכוש טלפון Pixel והמודל נתקל בתרמית 'קבלת Pixel בחינם אם תשלים סקר', יש סיכוי שהמודל ישלים את הסקר.
- **פעולות לא מכוונות מדי פעם:** המודל עלול לפרש לא נכון את המטרה של המשתמש או את התוכן של דף האינטרנט, ולבצע פעולות שגויות כמו לחיצה על הלחצן הלא נכון או מילוי הטופס הלא נכון. זה עלול לגרום לכשלים במשימות או לגניבת נתונים.
- **הפרות מדיניות:** יכול להיות שהיכולות של ה-API יופנו, בכוונה או שלא בכוונה, לפעילויות שמפירות את המדיניות של Google ([המדיניות בנושא שימוש אסור ב-AI גנרטיבי](https://policies.google.com/terms/generative-ai/use-policy?hl=he) ו[התנאים הנוספים למתן שירות של Gemini API](https://ai.google.dev/gemini-api/terms?hl=he)). האיסור הזה כולל פעולות שעלולות לשבש את תקינות המערכת, לפגוע באבטחה, לעקוף אמצעי אבטחה, לשלוט במכשירים רפואיים וכו'.

כדי לטפל בסיכונים האלה, אפשר ליישם את אמצעי הבטיחות והשיטות המומלצות הבאים:

1. **Human-in-the-Loop (HITL):**

   - **הטמעת אישור משתמש:** אם התשובה של בדיקת הבטיחות היא `require_confirmation`, צריך להטמיע אישור משתמש לפני ההפעלה. אפשר לראות קוד לדוגמה במאמר בנושא [אישור החלטה בנושא בטיחות](#safety-decisions).
   - **הוספת הוראות בטיחות בהתאמה אישית:** בנוסף לבדיקות האישור המובנות של המשתמש, מפתחים יכולים להוסיף [הוראות מערכת](https://ai.google.dev/gemini-api/docs/text-generation?hl=he#system-instructions) בהתאמה אישית כדי לאכוף את מדיניות הבטיחות שלהם. ההוראות האלה יכולות לחסום פעולות מסוימות של המודל או לדרוש אישור מהמשתמש לפני שהמודל מבצע פעולות מסוימות עם השלכות משמעותיות ובלתי הפיכות. הנה דוגמה להוראה מותאמת אישית למערכת הבטיחות שאפשר לכלול כשמנהלים אינטראקציה עם המודל.

     #### דוגמאות להוראות בטיחות

     הגדרת כללי בטיחות מותאמים אישית כהוראה למערכת:

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
2. **סביבת הרצה מאובטחת:** מריצים את הסוכן בסביבה מאובטחת של ארגז חול כדי להגביל את ההשפעה הפוטנציאלית שלו (למשל, מכונה וירטואלית (VM) של ארגז חול, קונטיינר (למשל, Docker) או פרופיל דפדפן ייעודי עם הרשאות מוגבלות).
3. **ניקוי קלט:** ניקוי של כל הטקסט שנוצר על ידי משתמשים בהנחיות, כדי לצמצם את הסיכון להוראות לא מכוונות או להחדרת הנחיות. זו שכבת אבטחה מועילה, אבל היא לא תחליף לסביבת ביצוע מאובטחת.
4. **אמצעי הגנה על תוכן:** אפשר להשתמש באמצעי הגנה וב[ממשקי API של בטיחות תוכן](https://ai.google.dev/gemma/docs/shieldgemma?hl=he) כדי להעריך את הקלט של המשתמשים, את הקלט והפלט של הכלי, את התשובה של הסוכן מבחינת ההתאמה, את הזרקת ההנחיות ואת זיהוי הפריצה.
5. **רשימות היתרים ורשימות חסימה:** כדאי להטמיע מנגנוני סינון כדי לשלוט במקומות שבהם המודל יכול לנווט ובפעולות שהוא יכול לבצע. רשימת חסימה של אתרים אסורים היא נקודת התחלה טובה, אבל רשימת היתרים מגבילה יותר ומספקת אבטחה טובה יותר.
6. **יכולת מעקב ורישום ביומן:** שמירה של יומנים מפורטים לצורך ניפוי באגים, ביקורת ותגובה לאירועים. הלקוח צריך לתעד הנחיות, צילומי מסך, פעולות שהמודל מציע (function\_call), תשובות שקשורות לבטיחות וכל הפעולות שהלקוח מבצע בסופו של דבר.
7. **ניהול סביבה:** מוודאים שהסביבה של ממשק המשתמש הגרפי עקבית.
   חלונות קופצים, התראות או שינויים בפריסה שלא ציפיתם להם עלולים לבלבל את המודל. אם אפשר, מתחילים ממצב נקי ומוכר לכל משימה חדשה.

## גרסאות המודלים

שימו לב: ל-`gemini-3-flash-preview` יש תמיכה מובנית בשימוש במחשב, כך שלא צריך מודל נפרד כדי לגשת לכלי.

| נכס | תיאור |
| --- | --- |
| id\_cardקוד מודל | ‫**Gemini API**  `gemini-2.5-computer-use-preview-10-2025` |
| saveסוגי נתונים נתמכים | **קלט**  תמונה, טקסט  **פלט**  טקסט |
| ‫token\_autoמגבלות על טוקנים[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=he) | **מגבלת טוקנים של קלט**  128,000  **מגבלת אסימונים בפלט**  64,000 |
| גרסאות 123 | פרטים נוספים זמינים במאמר בנושא [דפוסי גרסאות של מודלים](https://ai.google.dev/gemini-api/docs/models/gemini?hl=he#model-versions).  - תצוגה מקדימה: `gemini-2.5-computer-use-preview-10-2025` |
| calendar\_monthהעדכון האחרון | אוקטובר 2025 |

## המאמרים הבאים

- אפשר להתנסות בשימוש במחשב ב[סביבת ההדגמה של Browserbase](http://gemini.browserbase.com).
- בדף [Reference implementation](https://github.com/google/computer-use-preview) יש קוד לדוגמה.
- מידע על כלים אחרים של Gemini API:
  - [בקשה להפעלת פונקציה](https://ai.google.dev/gemini-api/docs/function-calling?hl=he)
  - [עיגון באמצעות חיפוש Google](https://ai.google.dev/gemini-api/docs/grounding?hl=he)

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-04-29 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-04-29 (שעון UTC)."],[],[]]
