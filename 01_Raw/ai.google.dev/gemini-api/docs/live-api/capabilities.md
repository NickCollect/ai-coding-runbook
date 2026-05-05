---
source_url: https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=he
fetched_at: 2026-05-05T19:52:15.096837+00:00
title: "Live API capabilities guide \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=he) זמין עכשיו בתצוגה מקדימה עם תכונות כמו תכנון שיתופי, ויזואליזציה, תמיכה ב-MCP ועוד.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# Live API capabilities guide

זהו מדריך מקיף שכולל את היכולות וההגדרות שזמינות ב-API בזמן אמת.
במאמר [תחילת העבודה עם Live API](https://ai.google.dev/gemini-api/docs/live?hl=he) מופיע סקירה כללית וקוד לדוגמה לתרחישי שימוש נפוצים.

## לפני שמתחילים

- **כדאי להכיר את המושגים העיקריים:** אם עדיין לא עשיתם את זה, קודם כדאי לקרוא את המאמר [תחילת העבודה עם Live API](https://ai.google.dev/gemini-api/docs/live?hl=he) .
  במאמר הזה נסביר על העקרונות הבסיסיים של Live API, איך הוא פועל ועל [גישות שונות להטמעה](https://ai.google.dev/gemini-api/docs/live?hl=he#implementation-approach).
- **התנסות ב-Live API ב-AI Studio:** מומלץ להתנסות ב-Live API ב-[Google AI Studio](https://aistudio.google.com/app/live?hl=he) לפני שמתחילים לפתח. כדי להשתמש ב-Live API ב-Google AI Studio, בוחרים באפשרות **Stream** (שידור).

## השוואה בין מודלים

בטבלה הבאה מפורטים ההבדלים העיקריים בין המודלים של [Gemini 3.1 Flash בגרסת טרום-השקה (Preview)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview?hl=he) לבין [Gemini 2.5 Flash בגרסת טרום-השקה (Preview)](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-native-audio-preview-12-2025?hl=he):

| תכונה | ‫Gemini 3.1 Flash Live Preview | גרסת טרום-השקה של Gemini ‎2.5 Flash Live |
| --- | --- | --- |
| **[תהליך החשיבה](#native-audio-output-thinking)** | משתמש ב-`thinkingLevel` כדי לשלוט בעומק החשיבה באמצעות הגדרות כמו `minimal`,‏ `low`,‏ `medium` ו-`high`. ברירת המחדל היא `minimal` כדי לבצע אופטימיזציה לזמן האחזור הנמוך ביותר. [מידע נוסף על תקציבים ורמות חשיבה](https://ai.google.dev/gemini-api/docs/thinking?hl=he#levels-budgets) | משתמשים ב-`thinkingBudget` כדי להגדיר את מספר הטוקנים של החשיבה. התכונה 'חשיבה דינמית' מופעלת כברירת מחדל. כדי להשבית, מגדירים את `thinkingBudget` להיות `0`. [מידע נוסף על תקציבים ורמות חשיבה](https://ai.google.dev/gemini-api/docs/thinking?hl=he#levels-budgets) |
| **[קבלת תשובה](https://ai.google.dev/api/live?hl=he#bidigeneratecontentservercontent)** | אירוע יחיד בשרת יכול להכיל כמה חלקי תוכן בו-זמנית (לדוגמה, `inlineData` ותמליל). כדי שלא יחסר תוכן, חשוב לוודא שהקוד מעבד את כל החלקים בכל אירוע. | כל אירוע שרת מכיל רק חלק תוכן אחד. החלקים מועברים באירועים נפרדים. |
| **[תוכן של לקוחות](#incremental-updates)** | ‫`send_client_content` נתמך רק לאכלוס היסטוריית ההקשר הראשוני (נדרשת הגדרה של `initial_history_in_client_content` בהגדרת הסשן). כדי לשלוח עדכוני טקסט במהלך השיחה, משתמשים באפשרות `send_realtime_input`. | `send_client_content` נתמך לאורך השיחה כדי לשלוח עדכוני תוכן מצטברים וליצור הקשר. |
| **[הפעלת כיסוי](https://ai.google.dev/api/live?hl=he#turncoverage)** | ברירת המחדל היא `TURN_INCLUDES_AUDIO_ACTIVITY_AND_ALL_VIDEO`. התור של המודל כולל פעילות אודיו שזוהתה וכל פריים של הווידאו. | ברירת המחדל היא `TURN_INCLUDES_ONLY_ACTIVITY`. התור של המודל כולל רק את הפעילות שזוהתה. |
| **[Custom VAD](#disable-automatic-vad)** (`activity_start`/`activity_end`) | נתמך. משביתים את ה-VAD האוטומטי ושולחים הודעות `activityStart` ו-`activityEnd` באופן ידני כדי לשלוט בהגדרת הגבולות של תורות הדיבור. | נתמך. משביתים את ה-VAD האוטומטי ושולחים הודעות `activityStart` ו-`activityEnd` באופן ידני כדי לשלוט בהגדרת הגבולות של תורות הדיבור. |
| **[הגדרה אוטומטית של VAD](#configure-automatic-vad)** | נתמך. מגדירים פרמטרים כמו `start_of_speech_sensitivity`, `end_of_speech_sensitivity`, `prefix_padding_ms` ו-`silence_duration_ms`. | נתמך. מגדירים פרמטרים כמו `start_of_speech_sensitivity`, `end_of_speech_sensitivity`, `prefix_padding_ms` ו-`silence_duration_ms`. |
| **[קריאות אסינכרוניות לפונקציות](https://ai.google.dev/gemini-api/docs/live-tools?hl=he#async-function-calling)** (`behavior: NON_BLOCKING`) | לא נתמך. הפעלת פונקציות היא רציפה בלבד. המודל לא יתחיל להגיב עד שתשלחו את התשובה של הכלי. | נתמך. כדי שהמודל ימשיך באינטראקציה בזמן שהפונקציה פועלת, צריך להגדיר את `behavior` לערך `NON_BLOCKING` בהצהרת הפונקציה. אפשר לשלוט באופן שבו המודל מטפל בתשובות באמצעות הפרמטר `scheduling` (`INTERRUPT`,‏ `WHEN_IDLE` או `SILENT`). |
| **[אודיו יזום](#proactive-audio)** | לא נתמך | נתמך. כשההגדרה הזו מופעלת, המודל יכול להחליט באופן יזום לא להגיב אם תוכן הקלט לא רלוונטי. מגדירים את `proactive_audio` ל-`true` בתצורה `proactivity` (נדרש `v1alpha`). |
| **[שיחה מותאמת-רגש](#affective-dialog)** | לא נתמך | נתמך. סגנון התשובה של המודל מותאם לסגנון הביטוי ולטון של הקלט. מגדירים את `enable_affective_dialog` ל-`true` בהגדרות הסשן (נדרש `v1alpha`). |

כדי לעבור מ-Gemini 2.5 Flash Live ל-Gemini 3.1 Flash Live, אפשר לעיין ב[מדריך להעברת נתונים](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview?hl=he#migrating).

## יצירת חיבור

בדוגמה הבאה מוצג אופן היצירה של חיבור באמצעות מפתח API:

### Python

```
import asyncio
from google import genai

client = genai.Client()

model = "gemini-3.1-flash-live-preview"
config = {"response_modalities": ["AUDIO"]}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        print("Session started")
        # Send content...

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.1-flash-live-preview';
const config = { responseModalities: [Modality.AUDIO] };

async function main() {

  const session = await ai.live.connect({
    model: model,
    callbacks: {
      onopen: function () {
        console.debug('Opened');
      },
      onmessage: function (message) {
        console.debug(message);
      },
      onerror: function (e) {
        console.debug('Error:', e.message);
      },
      onclose: function (e) {
        console.debug('Close:', e.reason);
      },
    },
    config: config,
  });

  console.debug("Session started");
  // Send content...

  session.close();
}

main();
```

## אופני אינטראקציה

בקטעים הבאים מופיעות דוגמאות והסבר על ההקשר של אמצעי הקלט והפלט השונים שזמינים ב-Live API.

### האודיו בתהליכי שליחה…

צריך לשלוח את האודיו כנתוני PCM גולמיים (אודיו PCM גולמי של 16 ביט, 16kHz, little-endian).

### Python

```
# Assuming 'chunk' is your raw PCM audio bytes
await session.send_realtime_input(
    audio=types.Blob(
        data=chunk,
        mime_type="audio/pcm;rate=16000"
    )
)
```

### JavaScript

```
// Assuming 'chunk' is a Buffer of raw PCM audio
session.sendRealtimeInput({
  audio: {
    data: chunk.toString('base64'),
    mimeType: 'audio/pcm;rate=16000'
  }
});
```

### פורמטים של אודיו

נתוני האודיו ב-Live API הם תמיד גולמיים, בפורמט little-endian,
PCM של 16 ביט. תמיד נעשה שימוש בתדירות דגימה של 24kHz בפלט האודיו. השמע שמוזן הוא בדרך כלל 16kHz, אבל Live API ידגום מחדש אם צריך, כך שאפשר לשלוח כל תדירות דגימה. כדי להעביר את תדירות הדגימה של אודיו מהקלט, צריך להגדיר את סוג ה-MIME של כל [Blob](https://ai.google.dev/api/caching?hl=he#Blob) שמכיל אודיו לערך כמו `audio/pcm;rate=16000`.

### קבלת אודיו

התשובות הקוליות של המודל מתקבלות כמקטעי נתונים.

### Python

```
async for response in session.receive():
    if response.server_content and response.server_content.model_turn:
        for part in response.server_content.model_turn.parts:
            if part.inline_data:
                audio_data = part.inline_data.data
                # Process or play the audio data
```

### JavaScript

```
// Inside the onmessage callback
const content = response.serverContent;
if (content?.modelTurn?.parts) {
  for (const part of content.modelTurn.parts) {
    if (part.inlineData) {
      const audioData = part.inlineData.data;
      // Process or play audioData (base64 encoded string)
    }
  }
}
```

### נשלחת הודעת טקסט

אפשר לשלוח טקסט באמצעות `send_realtime_input` (Python) או `sendRealtimeInput` (JavaScript).

### Python

```
await session.send_realtime_input(text="Hello, how are you?")
```

### JavaScript

```
session.sendRealtimeInput({
  text: 'Hello, how are you?'
});
```

### שליחת הסרטון מתבצעת

פריימים של סרטונים נשלחים כתמונות נפרדות (למשל, JPEG או PNG) בקצב פריימים ספציפי (עד פריים אחד לשנייה).

### Python

```
# Assuming 'frame' is your JPEG-encoded image bytes
await session.send_realtime_input(
    video=types.Blob(
        data=frame,
        mime_type="image/jpeg"
    )
)
```

### JavaScript

```
// Assuming 'frame' is a Buffer of JPEG-encoded image data
session.sendRealtimeInput({
  video: {
    data: frame.toString('base64'),
    mimeType: 'image/jpeg'
  }
});
```

#### עדכונים מצטברים של תוכן

אפשר להשתמש בעדכונים מצטברים כדי לשלוח קלט טקסט, ליצור הקשר של סשן או לשחזר את ההקשר של סשן. בהקשרים קצרים אפשר לשלוח אינטראקציות שלב אחר שלב כדי לייצג את רצף האירועים המדויק:

### Python

```
turns = [
    {"role": "user", "parts": [{"text": "What is the capital of France?"}]},
    {"role": "model", "parts": [{"text": "Paris"}]},
]

await session.send_client_content(turns=turns, turn_complete=False)

turns = [{"role": "user", "parts": [{"text": "What is the capital of Germany?"}]}]

await session.send_client_content(turns=turns, turn_complete=True)
```

### JavaScript

```
let inputTurns = [
  { "role": "user", "parts": [{ "text": "What is the capital of France?" }] },
  { "role": "model", "parts": [{ "text": "Paris" }] },
]

session.sendClientContent({ turns: inputTurns, turnComplete: false })

inputTurns = [{ "role": "user", "parts": [{ "text": "What is the capital of Germany?" }] }]

session.sendClientContent({ turns: inputTurns, turnComplete: true })
```

בהקשרים ארוכים יותר, מומלץ לספק סיכום של ההודעה כדי לפנות מקום בחלון ההקשר לאינטראקציות הבאות. במאמר בנושא [המשכת סשן](https://ai.google.dev/gemini-api/docs/live-session?hl=he#session-resumption) מוסבר על שיטה נוספת לטעינת הקשר של הסשן.

### תמלולי אודיו

בנוסף לתשובה של המודל, אפשר גם לקבל תמלילים של פלט האודיו ושל קלט האודיו.

כדי להפעיל תמלול של פלט האודיו של המודל, שולחים את המחרוזת
`output_audio_transcription` בהגדרות. שפת התמלול נקבעת לפי התשובה של המודל.

### Python

```
import asyncio
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.1-flash-live-preview"

config = {
    "response_modalities": ["AUDIO"],
    "output_audio_transcription": {}
}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        message = "Hello? Gemini are you there?"

        await session.send_client_content(
            turns={"role": "user", "parts": [{"text": message}]}, turn_complete=True
        )

        async for response in session.receive():
            if response.server_content.model_turn:
                print("Model turn:", response.server_content.model_turn)
            if response.server_content.output_transcription:
                print("Transcript:", response.server_content.output_transcription.text)

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.1-flash-live-preview';

const config = {
  responseModalities: [Modality.AUDIO],
  outputAudioTranscription: {}
};

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
    config: config,
  });

  const inputTurns = 'Hello how are you?';
  session.sendClientContent({ turns: inputTurns });

  const turns = await handleTurn();

  for (const turn of turns) {
    if (turn.serverContent && turn.serverContent.outputTranscription) {
      console.debug('Received output transcription: %s\n', turn.serverContent.outputTranscription.text);
    }
  }

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

כדי להפעיל תמלול של קלט האודיו של המודל, שולחים את הפקודה
`input_audio_transcription` בהגדרות.

### Python

```
import asyncio
from pathlib import Path
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.1-flash-live-preview"

config = {
    "response_modalities": ["AUDIO"],
    "input_audio_transcription": {},
}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        audio_data = Path("16000.pcm").read_bytes()

        await session.send_realtime_input(
            audio=types.Blob(data=audio_data, mime_type='audio/pcm;rate=16000')
        )

        async for msg in session.receive():
            if msg.server_content.input_transcription:
                print('Transcript:', msg.server_content.input_transcription.text)

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';
import * as fs from "node:fs";
import pkg from 'wavefile';
const { WaveFile } = pkg;

const ai = new GoogleGenAI({});
const model = 'gemini-3.1-flash-live-preview';

const config = {
  responseModalities: [Modality.AUDIO],
  inputAudioTranscription: {}
};

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
    config: config,
  });

  // Send Audio Chunk
  const fileBuffer = fs.readFileSync("16000.wav");

  // Ensure audio conforms to API requirements (16-bit PCM, 16kHz, mono)
  const wav = new WaveFile();
  wav.fromBuffer(fileBuffer);
  wav.toSampleRate(16000);
  wav.toBitDepth("16");
  const base64Audio = wav.toBase64();

  // If already in correct format, you can use this:
  // const fileBuffer = fs.readFileSync("sample.pcm");
  // const base64Audio = Buffer.from(fileBuffer).toString('base64');

  session.sendRealtimeInput(
    {
      audio: {
        data: base64Audio,
        mimeType: "audio/pcm;rate=16000"
      }
    }
  );

  const turns = await handleTurn();
  for (const turn of turns) {
    if (turn.text) {
      console.debug('Received text: %s\n', turn.text);
    }
    else if (turn.data) {
      console.debug('Received inline data: %s\n', turn.data);
    }
    else if (turn.serverContent && turn.serverContent.inputTranscription) {
      console.debug('Received input transcription: %s\n', turn.serverContent.inputTranscription.text);
    }
  }

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

### שינוי הקול והשפה

מודלים של [פלט אודיו מקורי](#native-audio-output) תומכים בכל הקולות שזמינים במודלים של [המרת טקסט לדיבור (TTS)](https://ai.google.dev/gemini-api/docs/speech-generation?hl=he#voices). אפשר להאזין לכל הקולות ב-[AI Studio](https://aistudio.google.com/app/live?hl=he).

כדי לציין קול, מגדירים את שם הקול באובייקט `speechConfig` כחלק מהגדרת הסשן:

### Python

```
config = {
    "response_modalities": ["AUDIO"],
    "speech_config": {
        "voice_config": {"prebuilt_voice_config": {"voice_name": "Kore"}}
    },
}
```

### JavaScript

```
const config = {
  responseModalities: [Modality.AUDIO],
  speechConfig: { voiceConfig: { prebuiltVoiceConfig: { voiceName: "Kore" } } }
};
```

‫Live API תומך ב[כמה שפות](#supported-languages).
מודלים של [פלט אודיו בשפה המקורית](#native-audio-output) בוחרים באופן אוטומטי את השפה המתאימה ולא תומכים בהגדרה מפורשת של קוד השפה.

## יכולות אודיו מובנות

המודלים הכי חדשים שלנו כוללים [פלט אודיו מקורי](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview?hl=he), שמספק דיבור טבעי וריאליסטי ומשפר את הביצועים בריבוי שפות.

### העמקה

מודלים של Gemini 3.1 משתמשים ב-`thinkingLevel` כדי לשלוט בעומק החשיבה, עם הגדרות כמו `minimal`,‏ `low`,‏ `medium` ו-`high`. ברירת המחדל היא `minimal` כדי לבצע אופטימיזציה לזמן האחזור הנמוך ביותר. במקום זאת, במודלים של Gemini 2.5 נעשה שימוש ב-`thinkingBudget` כדי להגדיר את מספר טוקני החשיבה. [מידע נוסף על רמות לעומת תקציבים](https://ai.google.dev/gemini-api/docs/thinking?hl=he#levels-budgets)

### Python

```
model = "gemini-3.1-flash-live-preview"

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"]
    thinking_config=types.ThinkingConfig(
        thinking_level="low",
    )
)

async with client.aio.live.connect(model=model, config=config) as session:
    # Send audio input and receive audio
```

### JavaScript

```
const model = 'gemini-3.1-flash-live-preview';
const config = {
  responseModalities: [Modality.AUDIO],
  thinkingConfig: {
    thinkingLevel: 'low',
  },
};

async function main() {

  const session = await ai.live.connect({
    model: model,
    config: config,
    callbacks: ...,
  });

  // Send audio input and receive audio

  session.close();
}

main();
```

בנוסף, אפשר להפעיל סיכומי מחשבות על ידי הגדרת `includeThoughts` לערך `true` בהגדרות. מידע נוסף זמין במאמר בנושא [סיכומי מחשבות](https://ai.google.dev/gemini-api/docs/thinking?hl=he#summaries).

### Python

```
model = "gemini-3.1-flash-live-preview"

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"]
    thinking_config=types.ThinkingConfig(
        thinking_level="low",
        include_thoughts=True
    )
)
```

### JavaScript

```
const model = 'gemini-3.1-flash-live-preview';
const config = {
  responseModalities: [Modality.AUDIO],
  thinkingConfig: {
    thinkingLevel: 'low',
    includeThoughts: true,
  },
};
```

### שיחה מותאמת-רגש

התכונה הזו מאפשרת ל-Gemini להתאים את סגנון התשובה שלו לניסוח ולטון של הקלט.

כדי להשתמש בשיחה מותאמת-רגש, צריך להגדיר את גרסת ה-API ל-`v1alpha` ולהגדיר את `enable_affective_dialog` ל-`true` בהודעת ההגדרה:

### Python

```
client = genai.Client(http_options={"api_version": "v1alpha"})

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    enable_affective_dialog=True
)
```

### JavaScript

```
const ai = new GoogleGenAI({ httpOptions: {"apiVersion": "v1alpha"} });

const config = {
  responseModalities: [Modality.AUDIO],
  enableAffectiveDialog: true
};
```

### אודיו פרואקטיבי

כשהתכונה הזו מופעלת, Gemini יכול להחליט מראש לא להגיב אם התוכן לא רלוונטי.

כדי להשתמש בו, צריך להגדיר את גרסת ה-API ל-`v1alpha`, להגדיר את השדה `proactivity` בהודעת ההגדרה ולהגדיר את הערך `proactive_audio` ל-`true`:

### Python

```
client = genai.Client(http_options={"api_version": "v1alpha"})

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    proactivity={'proactive_audio': True}
)
```

### JavaScript

```
const ai = new GoogleGenAI({ httpOptions: {"apiVersion": "v1alpha"} });

const config = {
  responseModalities: [Modality.AUDIO],
  proactivity: { proactiveAudio: true }
}
```

## זיהוי פעילות קולית (VAD)

זיהוי פעילות קולית (VAD) מאפשר למודל לזהות מתי אדם מדבר. היכולת הזו חיונית ליצירת שיחות טבעיות, כי היא מאפשרת למשתמש לקטוע את המודל בכל שלב.

כש-VAD מזהה הפרעה, היצירה המתמשכת מבוטלת ומושלכת. רק המידע שכבר נשלח ללקוח נשמר בהיסטוריית הסשנים. השרת שולח הודעת [`BidiGenerateContentServerContent`](https://ai.google.dev/api/live?hl=he#bidigeneratecontentservercontent) כדי לדווח על ההפרעה.

שרת Gemini מוחק את כל הקריאות לפונקציות שממתינות ושולח הודעת `BidiGenerateContentServerContent` עם מזהי השיחות שבוטלו.

### Python

```
async for response in session.receive():
    if response.server_content.interrupted is True:
        # The generation was interrupted

        # If realtime playback is implemented in your application,
        # you should stop playing audio and clear queued playback here.
```

### JavaScript

```
const turns = await handleTurn();

for (const turn of turns) {
  if (turn.serverContent && turn.serverContent.interrupted) {
    // The generation was interrupted

    // If realtime playback is implemented in your application,
    // you should stop playing audio and clear queued playback here.
  }
}
```

### זיהוי אוטומטי של פעילות קולית (VAD)

כברירת מחדל, המודל מבצע VAD באופן אוטומטי על זרם קלט רציף של אודיו. אפשר להגדיר את ה-VAD באמצעות השדה [`realtimeInputConfig.automaticActivityDetection`](https://ai.google.dev/api/live?hl=he#RealtimeInputConfig.AutomaticActivityDetection) של [הגדרת ההגדרה](https://ai.google.dev/api/live?hl=he#BidiGenerateContentSetup).

אם זרם האודיו מושהה למשך יותר משנייה (לדוגמה, כי המשתמש כיבה את המיקרופון), צריך לשלוח אירוע [`audioStreamEnd`](https://ai.google.dev/api/live?hl=he#BidiGenerateContentRealtimeInput.FIELDS.bool.BidiGenerateContentRealtimeInput.audio_stream_end) כדי לנקות את האודיו שנשמר במטמון. הלקוח יכול להמשיך לשלוח נתוני אודיו בכל שלב.

### Python

```
# example audio file to try:
# URL = "https://storage.googleapis.com/generativeai-downloads/data/hello_are_you_there.pcm"
# !wget -q $URL -O sample.pcm
import asyncio
from pathlib import Path
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.1-flash-live-preview"

config = {"response_modalities": ["AUDIO"]}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        audio_bytes = Path("sample.pcm").read_bytes()

        await session.send_realtime_input(
            audio=types.Blob(data=audio_bytes, mime_type="audio/pcm;rate=16000")
        )

        # if stream gets paused, send:
        # await session.send_realtime_input(audio_stream_end=True)

        async for response in session.receive():
            if response.text is not None:
                print(response.text)

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
// example audio file to try:
// URL = "https://storage.googleapis.com/generativeai-downloads/data/hello_are_you_there.pcm"
// !wget -q $URL -O sample.pcm
import { GoogleGenAI, Modality } from '@google/genai';
import * as fs from "node:fs";

const ai = new GoogleGenAI({});
const model = 'gemini-3.1-flash-live-preview';
const config = { responseModalities: [Modality.AUDIO] };

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
    config: config,
  });

  // Send Audio Chunk
  const fileBuffer = fs.readFileSync("sample.pcm");
  const base64Audio = Buffer.from(fileBuffer).toString('base64');

  session.sendRealtimeInput(
    {
      audio: {
        data: base64Audio,
        mimeType: "audio/pcm;rate=16000"
      }
    }

  );

  // if stream gets paused, send:
  // session.sendRealtimeInput({ audioStreamEnd: true })

  const turns = await handleTurn();
  for (const turn of turns) {
    if (turn.text) {
      console.debug('Received text: %s\n', turn.text);
    }
    else if (turn.data) {
      console.debug('Received inline data: %s\n', turn.data);
    }
  }

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

אם משתמשים ב-`send_realtime_input`, ה-API יגיב לאודיו באופן אוטומטי על סמך VAD. המודל `send_client_content` מוסיף הודעות להקשר של המודל לפי הסדר, אבל המודל `send_realtime_input` עובר אופטימיזציה לתגובה מהירה על חשבון סדר דטרמיניסטי.

### הגדרה אוטומטית של VAD

כדי לקבל שליטה רבה יותר בפעילות של זיהוי דיבור, אפשר להגדיר את הפרמטרים הבאים. מידע נוסף זמין במאמר בנושא [הפניית API](https://ai.google.dev/api/live?hl=he#automaticactivitydetection).

### Python

```
from google.genai import types

config = {
    "response_modalities": ["AUDIO"],
    "realtime_input_config": {
        "automatic_activity_detection": {
            "disabled": False, # default
            "start_of_speech_sensitivity": types.StartSensitivity.START_SENSITIVITY_LOW,
            "end_of_speech_sensitivity": types.EndSensitivity.END_SENSITIVITY_LOW,
            "prefix_padding_ms": 20,
            "silence_duration_ms": 100,
        }
    }
}
```

### JavaScript

```
import { GoogleGenAI, Modality, StartSensitivity, EndSensitivity } from '@google/genai';

const config = {
  responseModalities: [Modality.AUDIO],
  realtimeInputConfig: {
    automaticActivityDetection: {
      disabled: false, // default
      startOfSpeechSensitivity: StartSensitivity.START_SENSITIVITY_LOW,
      endOfSpeechSensitivity: EndSensitivity.END_SENSITIVITY_LOW,
      prefixPaddingMs: 20,
      silenceDurationMs: 100,
    }
  }
};
```

### השבתה של זיהוי דיבור אוטומטי

לחלופין, אפשר להשבית את ה-VAD האוטומטי על ידי הגדרת הערך `realtimeInputConfig.automaticActivityDetection.disabled` ל-`true` בהודעת ההגדרה. בהגדרה הזו, הלקוח אחראי לזיהוי הדיבור של המשתמש ולשליחת ההודעות [`activityStart`](https://ai.google.dev/api/live?hl=he#BidiGenerateContentRealtimeInput.FIELDS.BidiGenerateContentRealtimeInput.ActivityStart.BidiGenerateContentRealtimeInput.activity_start) ו-[`activityEnd`](https://ai.google.dev/api/live?hl=he#BidiGenerateContentRealtimeInput.FIELDS.BidiGenerateContentRealtimeInput.ActivityEnd.BidiGenerateContentRealtimeInput.activity_end) בזמנים המתאימים. לא נשלח `audioStreamEnd` בהגדרה הזו. במקום זאת, כל הפרעה לשידור מסומנת בהודעה `activityEnd`.

### Python

```
config = {
    "response_modalities": ["AUDIO"],
    "realtime_input_config": {"automatic_activity_detection": {"disabled": True}},
}

async with client.aio.live.connect(model=model, config=config) as session:
    # ...
    await session.send_realtime_input(activity_start=types.ActivityStart())
    await session.send_realtime_input(
        audio=types.Blob(data=audio_bytes, mime_type="audio/pcm;rate=16000")
    )
    await session.send_realtime_input(activity_end=types.ActivityEnd())
    # ...
```

### JavaScript

```
const config = {
  responseModalities: [Modality.AUDIO],
  realtimeInputConfig: {
    automaticActivityDetection: {
      disabled: true,
    }
  }
};

session.sendRealtimeInput({ activityStart: {} })

session.sendRealtimeInput(
  {
    audio: {
      data: base64Audio,
      mimeType: "audio/pcm;rate=16000"
    }
  }

);

session.sendRealtimeInput({ activityEnd: {} })
```

## ספירת הטוקנים

אפשר למצוא את המספר הכולל של הטוקנים שנצרכו בשדה [usageMetadata](https://ai.google.dev/api/live?hl=he#usagemetadata) של הודעת השרת שמוחזרת.

### Python

```
async for message in session.receive():
    # The server will periodically send messages that include UsageMetadata.
    if message.usage_metadata:
        usage = message.usage_metadata
        print(
            f"Used {usage.total_token_count} tokens in total. Response token breakdown:"
        )
        for detail in usage.response_tokens_details:
            match detail:
                case types.ModalityTokenCount(modality=modality, token_count=count):
                    print(f"{modality}: {count}")
```

### JavaScript

```
const turns = await handleTurn();

for (const turn of turns) {
  if (turn.usageMetadata) {
    console.debug('Used %s tokens in total. Response token breakdown:\n', turn.usageMetadata.totalTokenCount);

    for (const detail of turn.usageMetadata.responseTokensDetails) {
      console.debug('%s\n', detail);
    }
  }
}
```

## רזולוציית המדיה

אתם יכולים לציין את רזולוציית המדיה של מדיה הקלט על ידי הגדרת השדה `mediaResolution` כחלק מהגדרת הסשן:

### Python

```
from google.genai import types

config = {
    "response_modalities": ["AUDIO"],
    "media_resolution": types.MediaResolution.MEDIA_RESOLUTION_LOW,
}
```

### JavaScript

```
import { GoogleGenAI, Modality, MediaResolution } from '@google/genai';

const config = {
    responseModalities: [Modality.AUDIO],
    mediaResolution: MediaResolution.MEDIA_RESOLUTION_LOW,
};
```

## מגבלות

כדאי להביא בחשבון את המגבלות הבאות של Live API כשמתכננים את הפרויקט.

### אופני תגובה

מודלים מקוריים של אודיו תומכים רק ב-`AUDIO response modality. אם אתם צריכים את התשובה של המודל כטקסט, אתם יכולים להשתמש בתכונה [תמלול אודיו של הפלט](#audio-transcription).

### אימות לקוח

כברירת מחדל, Live API מספק רק אימות משרת לשרת. אם אתם מטמיעים את אפליקציית Live API באמצעות [גישה של לקוח לשרת](https://ai.google.dev/gemini-api/docs/live?hl=he#implementation-approach), אתם צריכים להשתמש ב[טוקנים זמניים](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=he) כדי לצמצם את הסיכונים לאבטחה.

### משך הביקור

משך הפגישות עם אודיו בלבד מוגבל ל-15 דקות, ומשך הפגישות עם אודיו ווידאו מוגבל ל-2 דקות.
עם זאת, אתם יכולים להגדיר [טכניקות שונות לניהול סשנים](https://ai.google.dev/gemini-api/docs/live-session?hl=he) כדי להאריך את משך הסשן ללא הגבלה.

### חלון ההקשר

לסשן יש מגבלה של חלון הקשר:

- ‫128,000 טוקנים למודלים של [פלט אודיו מקורי](#native-audio-output)
- ‫32,000 טוקנים בדגמים אחרים של Live API

## שפות נתמכות

ה-API של שידורים חיים תומך ב-97 השפות הבאות.

| שפה | קוד BCP-47 | שפה | קוד BCP-47 |
| --- | --- | --- | --- |
| אפריקאנס | `af` | לטבית | `lv` |
| אקאן | `ak` | ליטאית | `lt` |
| אלבנית | `sq` | מקדונית | `mk` |
| אמהרית | `am` | מלאית | `ms` |
| ערבית | `ar` | מליאלאם | `ml` |
| ארמנית | `hy` | מלטית | `mt` |
| אסאמית | `as` | מאורית | `mi` |
| אזרית | `az` | מראטהית | `mr` |
| בסקית | `eu` | מונגולית | `mn` |
| בלארוסית | `be` | נפאלית | `ne` |
| בנגלית | `bn` | נורווגית | `no` |
| בוסנית | `bs` | אודיה | `or` |
| בולגרית | `bg` | אורומו | `om` |
| בורמזית | `my` | פשטו | `ps` |
| קטלאנית | `ca` | פרסית | `fa` |
| סבואנו | `ceb` | פולנית | `pl` |
| סינית | `zh` | פורטוגזית | `pt` |
| קרואטית | `hr` | פנג'אבי | `pa` |
| צ'כית | `cs` | קצ'ואה | `qu` |
| דנית | `da` | רומנית | `ro` |
| הולנדית | `nl` | רומאנש | `rm` |
| אנגלית | `en` | רוסית | `ru` |
| אסטונית | `et` | סרבית | `sr` |
| פארואזית | `fo` | סינדהית | `sd` |
| פיליפינית | `fil` | סינהאלה | `si` |
| פינית | `fi` | סלובקית | `sk` |
| צרפתית | `fr` | סלובנית | `sl` |
| גליציאנית | `gl` | סומלית | `so` |
| גאורגית | `ka` | ססוטו | `st` |
| גרמנית | `de` | ספרדית | `es` |
| יוונית | `el` | סווהילי | `sw` |
| גוג'ראטי | `gu` | שוודית | `sv` |
| האוסה | `ha` | טג'יקית | `tg` |
| עברית | `iw` | טמילית | `ta` |
| הינדי | `hi` | טלוגו | `te` |
| הונגרית | `hu` | תאית | `th` |
| איסלנדית | `is` | טסוואנה | `tn` |
| אינדונזית | `id` | טורקית | `tr` |
| אירית | `ga` | טורקמנית | `tk` |
| איטלקית | `it` | אוקראינית | `uk` |
| יפנית | `ja` | אורדו | `ur` |
| קנאדה | `kn` | אוזבקית | `uz` |
| קזחית | `kk` | וייטנאמית | `vi` |
| חמרית | `km` | וולשית | `cy` |
| קינירואנדה | `rw` | פריזית מערבית | `fy` |
| קוריאנית | `ko` | וולוף | `wo` |
| כורדית | `ku` | יורובה | `yo` |
| קירגיזית | `ky` | זולו | `zu` |
| לאו | `lo` |  |  |

## המאמרים הבאים

- כדאי לקרוא את המדריכים [שימוש בכלי](https://ai.google.dev/gemini-api/docs/live-tools?hl=he) ו[ניהול סשנים](https://ai.google.dev/gemini-api/docs/live-session?hl=he) כדי לקבל מידע חשוב על שימוש יעיל ב-Live API.
- אפשר לנסות את ממשק ה-API של Live ב-[Google AI Studio](https://aistudio.google.com/app/live?hl=he).
- מידע נוסף על מודלים של Live API זמין במאמר [Gemini 2.5 Flash Native Audio](https://ai.google.dev/gemini-api/docs/models?hl=he#gemini-2.5-flash-native-audio) בדף Models.
- אפשר לנסות דוגמאות נוספות ב[ספר המתכונים של Live API](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI.ipynb?hl=he), ב[ספר המתכונים של Live API Tools](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI_tools.ipynb?hl=he) וב[סקריפט Live API Get Started](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI.py).

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-04-29 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-04-29 (שעון UTC)."],[],[]]
