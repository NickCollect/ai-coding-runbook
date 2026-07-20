---
source_url: https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=he
fetched_at: 2026-07-20T04:37:46.021293+00:00
title: "\u05e0\u05d9\u05d4\u05d5\u05dc \u05e1\u05e9\u05e0\u05d9\u05dd \u05d1\u05d0\u05de\u05e6\u05e2\u05d5\u05ea Live API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# ניהול סשנים באמצעות Live API

ב-Live API, סשן הוא חיבור מתמשך שבו הקלט והפלט מועברים בסטרימינג באופן רציף דרך אותו חיבור ([מידע נוסף על אופן הפעולה](https://ai.google.dev/gemini-api/docs/live?hl=he)).
העיצוב הייחודי של הסשן מאפשר השהיה נמוכה ותומך בתכונות ייחודיות, אבל הוא גם עלול ליצור בעיות, כמו הגבלות על משך הסשן וסיום מוקדם.
במדריך הזה מוסברות אסטרטגיות להתמודדות עם האתגרים בניהול סשנים שיכולים להתעורר כשמשתמשים ב-Live API.

## משך החיים של הסשן

בלי דחיסה, משך הפגישות עם אודיו בלבד מוגבל ל-15 דקות, ומשך הפגישות עם אודיו ווידאו מוגבל ל-2 דקות. חריגה מהמגבלות האלה תגרום לסיום הסשן (ולכן גם של החיבור), אבל אפשר להשתמש ב[דחיסה של חלון ההקשר](#context-window-compression) כדי להאריך את הסשנים לזמן בלתי מוגבל.

גם משך החיים של החיבור מוגבל, לכ-10 דקות. כשהחיבור מסתיים, גם הסשן מסתיים. במקרה כזה, אפשר להגדיר סשן יחיד שיישאר פעיל בכמה חיבורים באמצעות [חידוש סשן](#session-resumption).
בנוסף, תקבלו [הודעת GoAway](#goaway-message) לפני שהחיבור יסתיים, כדי שתוכלו לבצע פעולות נוספות.

## דחיסת חלון ההקשר

כדי להאריך את משך הסשנים ולמנוע ניתוק פתאומי של החיבור, אפשר להפעיל דחיסה של חלון ההקשר על ידי הגדרת השדה [contextWindowCompression](https://ai.google.dev/api/live?hl=he#BidiGenerateContentSetup.FIELDS.ContextWindowCompressionConfig.BidiGenerateContentSetup.context_window_compression) כחלק מהגדרת הסשן.

ב-[ContextWindowCompressionConfig](https://ai.google.dev/api/live?hl=he#contextwindowcompressionconfig), אפשר להגדיר [מנגנון של חלון הזזה](https://ai.google.dev/api/live?hl=he#ContextWindowCompressionConfig.FIELDS.ContextWindowCompressionConfig.SlidingWindow.ContextWindowCompressionConfig.sliding_window) ו[מספר טוקנים](https://ai.google.dev/api/live?hl=he#ContextWindowCompressionConfig.FIELDS.int64.ContextWindowCompressionConfig.trigger_tokens) שמפעיל דחיסה.

### Python

```
from google.genai import types

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    context_window_compression=(
        # Configures compression with default parameters.
        types.ContextWindowCompressionConfig(
            sliding_window=types.SlidingWindow(),
        )
    ),
)
```

### JavaScript

```
const config = {
  responseModalities: [Modality.AUDIO],
  contextWindowCompression: { slidingWindow: {} }
};
```

## המשך הסשן

כדי למנוע את סיום הסשן כשהשרת מאפס מעת לעת את חיבור ה-WebSocket, צריך להגדיר את השדה [sessionResumption](https://ai.google.dev/api/live?hl=he#BidiGenerateContentSetup.FIELDS.SessionResumptionConfig.BidiGenerateContentSetup.session_resumption) ב[הגדרת ההגדרה](https://ai.google.dev/api/live?hl=he#BidiGenerateContentSetup).

העברת ההגדרה הזו גורמת לשרת לשלוח הודעות [SessionResumptionUpdate](https://ai.google.dev/api/live?hl=he#SessionResumptionUpdate), שאפשר להשתמש בהן כדי להמשיך את הסשן. לשם כך צריך להעביר את אסימון ההמשכה האחרון כ-[`SessionResumptionConfig.handle`](https://ai.google.dev/api/live?hl=he#SessionResumptionConfig.FIELDS.string.SessionResumptionConfig.handle) של החיבור הבא.

התוקף של אסימוני חידוש הוא שעתיים אחרי סיום הסשן האחרון.

### Python

```
import asyncio
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.1-flash-live-preview"

async def main():
    print(f"Connecting to the service with handle {previous_session_handle}...")
    async with client.aio.live.connect(
        model=model,
        config=types.LiveConnectConfig(
            response_modalities=["AUDIO"],
            session_resumption=types.SessionResumptionConfig(
                # The handle of the session to resume is passed here,
                # or else None to start a new session.
                handle=previous_session_handle
            ),
        ),
    ) as session:
        while True:
            await session.send_client_content(
                turns=types.Content(
                    role="user", parts=[types.Part(text="Hello world!")]
                )
            )
            async for message in session.receive():
                # Periodically, the server will send update messages that may
                # contain a handle for the current state of the session.
                if message.session_resumption_update:
                    update = message.session_resumption_update
                    if update.resumable and update.new_handle:
                        # The handle should be retained and linked to the session.
                        return update.new_handle

                # For the purposes of this example, placeholder input is continually fed
                # to the model. In non-sample code, the model inputs would come from
                # the user.
                if message.server_content and message.server_content.turn_complete:
                    break

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.1-flash-live-preview';

async function live() {
  const responseQueue = [];

  async function waitMessage() {
    let done = false;
    let message = undefined;
    while (!done) {
      message = responseQueue.shift();
      if (message) {
        done = true;
      } else {
        await new Promise((resolve) => setTimeout(resolve, 100));
      }
    }
    return message;
  }

  async function handleTurn() {
    const turns = [];
    let done = false;
    while (!done) {
      const message = await waitMessage();
      turns.push(message);
      if (message.serverContent && message.serverContent.turnComplete) {
        done = true;
      }
    }
    return turns;
  }

console.debug('Connecting to the service with handle %s...', previousSessionHandle)
const session = await ai.live.connect({
  model: model,
  callbacks: {
    onopen: function () {
      console.debug('Opened');
    },
    onmessage: function (message) {
      responseQueue.push(message);
    },
    onerror: function (e) {
      console.debug('Error:', e.message);
    },
    onclose: function (e) {
      console.debug('Close:', e.reason);
    },
  },
  config: {
    responseModalities: [Modality.AUDIO],
    sessionResumption: { handle: previousSessionHandle }
    // The handle of the session to resume is passed here, or else null to start a new session.
  }
});

const inputTurns = 'Hello how are you?';
session.sendClientContent({ turns: inputTurns });

const turns = await handleTurn();
for (const turn of turns) {
  if (turn.sessionResumptionUpdate) {
    if (turn.sessionResumptionUpdate.resumable && turn.sessionResumptionUpdate.newHandle) {
      let newHandle = turn.sessionResumptionUpdate.newHandle
      // ...Store newHandle and start new session with this handle here
    }
  }
}

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

## קבלת הודעה לפני ניתוק הסשן

השרת שולח הודעת [GoAway](https://ai.google.dev/api/live?hl=he#GoAway) שמציינת שהחיבור הנוכחי יסתיים בקרוב. ההודעה הזו כוללת את [timeLeft](https://ai.google.dev/api/live?hl=he#GoAway.FIELDS.google.protobuf.Duration.GoAway.time_left), שמציין את הזמן שנותר ומאפשר לכם לבצע פעולה נוספת לפני שהחיבור יסתיים כ-ABORTED.

### Python

```
async for response in session.receive():
    if response.go_away is not None:
        # The connection will soon be terminated
        print(response.go_away.time_left)
```

### JavaScript

```
const turns = await handleTurn();

for (const turn of turns) {
  if (turn.goAway) {
    console.debug('Time left: %s\n', turn.goAway.timeLeft);
  }
}
```

## קבלת הודעה כשהיצירה מסתיימת

השרת שולח הודעה מסוג [generationComplete](https://ai.google.dev/api/live?hl=he#BidiGenerateContentServerContent.FIELDS.bool.BidiGenerateContentServerContent.generation_complete)
שמציינת שהמודל סיים ליצור את התשובה.

### Python

```
async for response in session.receive():
    if response.server_content.generation_complete is True:
        # The generation is complete
```

### JavaScript

```
const turns = await handleTurn();

for (const turn of turns) {
  if (turn.serverContent && turn.serverContent.generationComplete) {
    // The generation is complete
  }
}
```

## המאמרים הבאים

אפשר לעיין בדרכים נוספות לעבודה עם Live API במדריך המלא [יכולות](https://ai.google.dev/gemini-api/docs/live?hl=he), בדף [שימוש בכלי](https://ai.google.dev/gemini-api/docs/live-tools?hl=he) או ב[אוסף פתרונות של Live API](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI.ipynb?hl=he).

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-06-01 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-06-01 (שעון UTC)."],[],[]]
