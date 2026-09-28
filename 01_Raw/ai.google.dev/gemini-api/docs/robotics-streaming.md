---
source_url: https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=he
fetched_at: 2026-09-28T06:31:01.601187+00:00
title: "\u05e8\u05d5\u05d1\u05d5\u05d8\u05d9\u05e7\u05d4 \u05e2\u05dd \u05e1\u05d8\u05e8\u05d9\u05de\u05d9\u05e0\u05d2 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

‫Google משתמשת בטכנולוגיית AI כדי לתרגם תוכן לשפה המועדפת עליך. בתרגומים כאלו עשויות להיות שגיאות.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# רובוטיקה עם סטרימינג

נקודת הקצה של מודל `gemini-robotics-er-2-streaming-preview` חושפת נקודת קצה ייעודית לסטרימינג שמשולבת עם [Live API](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=he), ומאפשרת אינטראקציה דו-כיוונית בזמן אמת בין האפליקציה לבין הרובוט. התכונה הזו מתאימה לסוכנים שצריכים לולאות משוב מהירות ותגובות מהירות לסביבה.

[אפשר לנסות ב-Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-2-streaming-preview&hl=he)
[שיבוט של אפליקציות לדוגמה מ-GitHub](https://github.com/google-gemini/robotics-samples/tree/main/live-api)

## תרחישים לדוגמה

- **תיאום בין כמה רובוטים**: כמה רובוטים שמתקשרים ביניהם לגבי סטטוס המשימה ומעבירים משימות משנה באמצעות סשן משותף.
- **מעקב רציף**: רובוטים שצופים בסצנה ומפעילים פעולות כשמתרחשים אירועים ספציפיים, כמו מיכל שמגיע לרמת מילוי מסוימת.
- **מחסן ולוגיסטיקה**: סוכני ליקוט ואריזה שמאמתים פריטים באופן ויזואלי, עוקבים אחרי התקדמות האריזה ומתקנים שגיאות.

## מפרטים טכניים

בטבלה הבאה מפורטות המפרטים הטכניים של Live API:

| קטגוריה | פרטים |
| --- | --- |
| אופני קלט | אודיו (אודיו PCM גולמי של 16 ביט, 16kHz, little-endian), תמונות (JPEG <= 1FPS), טקסט |
| אופנויות פלט | טקסט |
| פרוטוקול | חיבור WebSocket עם שמירת מצב (WSS) |

## איך יוצרים הגדרה סוכנית

כל סוכן רובוטיקה שמבוסס על Live API פועל לפי שלושה שלבים:

1. **הצהרה על יכולות הרובוט ככלים.** כל פעולה שהרובוט יכול לבצע – ניווט, אחיזה, דיבור – הופכת להצהרת פונקציה עם שם, תיאור וסכימת פרמטרים. בפעולות פיזיות צריך להשתמש ב-`"behavior": "BLOCKING"` כדי שהמודל ימתין לסיום הפעולה של הרובוט לפני שיבחר את השלב הבא.
2. **הזרמת קלט מרובה מצבים לסשן מתמשך.** פותחים סשן `live.connect`
   ומשאירים אותו פתוח למשך כל זמן ביצוע המשימה. לשלוח פריים של סרטון, אודיו או טקסט כשהם מגיעים מהחיישנים של הרובוט.
3. **טיפול בקריאות לכלים בלולאת קבלה.** בכל פעם שהמודל בוחר פעולה, הוא שולח הודעה מסוג `tool_call`. לולאת הקבלה מפעילה את הפונקציה מול ה-SDK של הרובוט ושולחת בחזרה את הערך `tool_response`. הסשן נשאר פתוח, והמודל בוחר את הפעולה הבאה על סמך התוצאה.

בקטעים הבאים מוסבר איך להשתמש בשלבים האלה בשלושה תרחישים נפוצים:
לולאת סוכן בסיסית, מעקב פרואקטיבי אחרי סצנות באמצעות אות פעימה וניתוב
של דיבור דרך TTS ככלי.

## תיאום פעולות של רובוט באמצעות הפעלת פונקציות

בדוגמה הבאה מוצגים שלושת השלבים שמחוברים יחד בסקריפט Python יחיד.

שלב 1 – הגדרות כלי – מגדיר את היכולות של הרובוט כהצהרות פונקציה. הפונקציה `navigate` משתמשת ב-`"behavior": "BLOCKING"`, ולכן המודל מחכה שהרובוט יגיע לנקודת הציון לפני שהוא קורא לכלי אחר.
כדי לחשוף יכולות נוספות של הרובוט, אפשר להוסיף עוד הצהרות על פונקציות באותה רשימה.

שלב 2 – עזרה בהזנת קלט – מוצגות שלוש פונקציות שמעבירות קלט של אופנויות שונות לשיחה: `send_text` לפקודות, `send_image` לפריימים של המצלמה עם פרומפט טקסטואלי אופציונלי, ו-`send_audio` לאודיו גולמי בפורמט PCM ממיקרופון.

שלב 3 – לולאת הקבלה – פועל במקביל ומטפל בשני סוגים של הודעות:
הודעות `server_content` (פלט הטקסט של המודל) והודעות `tool_call` (המודל מבקש פעולה של רובוט). כשמתקבלת קריאה לכלי, הלולאה קוראת ל-`execute_tool` – קובץ stub שצריך להחליף ב-SDK הרובוט האמיתי – ואז שולחת בחזרה `tool_response` כדי שהמודל יוכל לבחור את הפעולה הבאה.

```
import asyncio
from google import genai
from google.genai import types

MODEL = "gemini-robotics-er-2-streaming-preview"

# ── Tool definitions ─────────────────────────────────────────────────────────
tools = [
   {
       "function_declarations": [
           {
               "name": "navigate",
               "description": "Navigate the robot to a named waypoint.",
               "behavior": "BLOCKING",
               "parameters": {
                   "type": "OBJECT",
                   "properties": {"name": {"type": "STRING"}},
                   "required": ["name"],
               },
           },
           # Add more function definitions here
       ]
   }
]

# ── Stub tool executor (replace with real robot SDK calls) ───────────────────
def execute_tool(name: str, args: dict) -> dict:
   print(f"  [Tool] {name}({args})")
   return {"status": "success"}

# ── Input helpers ────────────────────────────────────────────────────────────
def send_text(session, text: str):
   """Send a text turn."""
   return session.send_client_content(
       turns=types.Content(role="user", parts=[types.Part(text=text)]),
       turn_complete=True,
   )

def send_image(session, image_bytes: bytes, prompt: str = ""):
   """Send a JPEG image with an optional text prompt."""
   parts = [
       types.Part(
           inline_data=types.Blob(data=image_bytes, mime_type="image/jpeg")
       )
   ]
   if prompt:
       parts.append(types.Part(text=prompt))
   return session.send_client_content(
       turns=types.Content(role="user", parts=parts),
       turn_complete=True,
   )

def send_audio(session, audio_chunk: bytes):
   """Stream a chunk of raw PCM audio (16-bit, 16 kHz, mono)."""
   return session.send_realtime_input(
       media=types.Blob(data=audio_chunk, mime_type="audio/pcm;rate=16000")
   )

# ── Receive loop ─────────────────────────────────────────────────────────────
async def receive_loop(session):
   """Print model text and handle tool calls until the session ends."""
   async for message in session.receive():
       if message.server_content:
           sc = message.server_content
           if sc.model_turn and sc.model_turn.parts:
               for part in sc.model_turn.parts:
                   if part.text:
                       print(f"Model: {part.text}", end="", flush=True)
           if sc.turn_complete:
               print("\n[Turn Complete]")
       elif message.tool_call:
           responses = []
           for call in message.tool_call.function_calls:
               print(f"\n[Tool Call] {call.name}({call.args})")
               result = execute_tool(call.name, call.args)
               responses.append(
                   types.FunctionResponse(
                       name=call.name,
                       response=result,
                       id=call.id,
                   )
               )
           await session.send_tool_response(function_responses=responses)

# ── Main ─────────────────────────────────────────────────────────────────────
async def main():
   client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
   config = types.LiveConnectConfig(
       response_modalities=["TEXT"],
       tools=tools,
       system_instruction=types.Content(
           parts=[types.Part(text="You are a robot controller. Use tools to execute commands.")]
       ),
   )
   async with client.aio.live.connect(model=MODEL, config=config) as session:
       recv_task = asyncio.create_task(receive_loop(session))
       # Connect robot perception callbacks and user inputs to the helpers above.
       recv_task.cancel()

asyncio.run(main())
```

לולאת הקבלה נשארת פעילה אחרי כל תשובה של הכלי. המודל בונה ומשנה תוכנית לטווח ארוך בלי שתצטרכו לקודד מראש את כל רצף הפעולות.

## חשיבה מרחבית-זמנית פרואקטיבית

ה-Live API מעביר את הווידאו בסטרימינג, אבל פריימים של וידאו לבד לא מפעילים תור חדש של ניתוח. כדי להפעיל את התגובה של המודל, צריך לצרף למסגרות של הסרטון הנחיה בטקסט או באודיו. פרטים נוספים זמינים במאמר בנושא [יכולות של API פעיל](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=he).

כדי להפעיל חשיבה רציונלית, צריך להטמיע **פעימת לב**: לשלוח מעת לעת את הפריים האחרון מהמצלמה, ואחריו פרומפט טקסטואלי קצר שמאלץ את המודל לבדוק את הסצנה ולקבל החלטה מפורשת. קצב הפריימים של קלט הווידאו מוגבל לפרים אחד לשנייה.

### הטמעה של פעימת הלב

קורוטינת הדופק פועלת כמשימת `asyncio` נפרדת באותו סשן.
הוא מכוון באופן אופטימלי לקצב של 1 הרץ (בהתאם למגבלת קצב קלט הווידאו) בזמן ההמתנה להשלמת כל תור (`er_turn_done`) כדי למנוע שיבוש של תהליך ההסקה:

```
async def heartbeat(session, camera, er_turn_done: asyncio.Event):
    TARGET_INTERVAL_SEC = 1.0

    while True:
        start_time = asyncio.get_running_loop().time()

        frame = await camera.latest_jpeg()
        await session.send_realtime_input(
            video=types.Blob(data=frame, mime_type="image/jpeg")
        )
        await session.send_realtime_input(
            text=(
                "[HEARTBEAT] If no task is active, call 'ack' and wait for user"
                " input. If a task is active: observe the scene. If the current"
                " step is progressing correctly, call 'ack'. If the current step"
                " is complete, call 'run_instruction' with the next step. If the"
                " overall goal is achieved, call 'reset' and inform the user."
            )
        )

        # Wait for the model to finish responding before sending the next heartbeat
        await er_turn_done.wait()
        er_turn_done.clear()

        # Sleep only the remaining time to maintain ~1 Hz cadence
        elapsed = asyncio.get_running_loop().time() - start_time
        remaining = TARGET_INTERVAL_SEC - elapsed
        if remaining > 0:
            await asyncio.sleep(remaining)
```

### עדכון לולאת הקבלה

כדי לציין מתי המודל סיים את התור שלו, צריך לעדכן את `receive_loop`
כדי להגדיר את `er_turn_done`:

```
# In receive_loop: signal when the model finishes its turn
if sc.turn_complete:
    er_turn_done.set()
```

## פלט אודיו דרך TTS חיצוני

‫Gemini Robotics ER 2 מחזיר טקסט. האפליקציה שלכם מעבירה תשובות מלאות לספק TTS נפרד (כמו [Gemini TTS](https://ai.google.dev/gemini-api/docs/speech-generation?hl=he)) באמצעות קריאה חוזרת (callback) שמוזרקת.
כך תוכלו לשלוט בהשהיה של הדיבור, בבחירת הקול ובהתנהגות של ההפרעה, ולהחליף את מערכות ה-TTS בלי לשנות את הלוגיקה של הסוכן.

אפשר גם להגדיר את ה-TTS ככלי, כדי שהמודל יתייחס ל "say something" באותו אופן כמו "move the arm". מוסיפים את הצהרת הפונקציה הבאה לרשימת `tools` מהקטע הראשון:

```
TOOLS = [
    {
        "name": "send_message",
        "description": (
            "Speak a message aloud via TTS, then deliver it to the"
            " specified target. Use target='user' to speak directly"
            " to the user, or a peer agent name (e.g., 'duo') to"
            " communicate with another robot."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "target": {
                    "type": "string",
                    "description": "Recipient: 'user' or a peer agent name.",
                },
                "message": {
                    "type": "string",
                    "description": "The message to speak and deliver.",
                },
            },
            "required": ["target", "message"],
        },
    },
]
```

כשעוטפים את ה-TTS בהצהרת פונקציה, המודל מטפל בדיבור דרך אותו נתיב של קריאה לכלי כמו כל פעולה אחרת של הרובוט. האפליקציה ממלאת את הקריאה באמצעות קריאה חוזרת (callback) מוזרקת.

## דוגמאות ב-GitHub

דוגמאות מלאות שעובדות, כולל הדגמה של רובוט Spot שמביא חטיפים ו-Tinybot pan-tilt hello world, זמינות במאמר [דוגמאות ל-API של Robotics Live](https://github.com/google-gemini/robotics-samples/tree/main/live-api).

## המאמרים הבאים

- [הבנת סרטונים](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=he) – איתור רגעים וסיווג התקדמות.
- [תזמור משימות](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=he) – משימות ארוכות טווח ללא סטרימינג.
- [סקירה כללית של Live API](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=he) – תיעוד מלא של Live API.

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-09-16 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-09-16 (שעון UTC)."],[],[]]
