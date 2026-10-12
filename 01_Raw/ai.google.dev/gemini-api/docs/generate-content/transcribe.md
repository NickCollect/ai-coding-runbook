---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/transcribe?hl=he
fetched_at: 2026-10-12T06:52:14.353361+00:00
title: "\u05ea\u05de\u05dc\u05d5\u05dc \u05d0\u05d5\u05d3\u05d9\u05d5 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

‫Google משתמשת בטכנולוגיית AI כדי לתרגם תוכן לשפה המועדפת עליך. בתרגומים כאלו עשויות להיות שגיאות.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs/generate-content?hl=he)

שליחת משוב

# תמלול אודיו

‫Gemini API ממיר דיבור בקובצי אודיו לטקסט באמצעות מודל Gemini 3.5 Transcribe (`gemini-3.5-transcribe`). על סמך יכולות ההבנה של אודיו ב-Gemini, הוא מספק תמלול מדויק עם זיהוי שפה אוטומטי, תיוג דוברים, חותמות זמן ברמת המילה ורמזים לגבי אוצר מילים מותאם אישית. יש גם מצב [תמלול חכם](#transcription-modes) שכולל הסרת גמגום ופורמט חכם.

כדי לתמלל קובץ אודיו, מעלים את האודיו ומעבירים אותו אל `gemini-3.5-transcribe`:

### Python

```
from google import genai

client = genai.Client()

audio_file = client.files.upload(file="path/to/sample.mp3")

response = client.models.generate_content(
    model="gemini-3.5-transcribe",
    contents=[audio_file],
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const audioFile = await ai.files.upload({
  file: "path/to/sample.mp3",
  mimeType: "audio/mp3",
});

const response = await ai.models.generateContent({
  model: "gemini-3.5-transcribe",
  contents: [audioFile],
});

console.log(response.text);
```

### REST

```
# First upload the file via the Files API, then pass its URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-transcribe:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "fileData": {
              "fileUri": "YOUR_FILE_URI",
              "mimeType": "audio/mp3"
            }
          }
        ]
      }
    ]
  }'
```

## סקירה כללית

‫Gemini 3.5 Transcribe עבר אופטימיזציה למשימות של המרת דיבור לטקסט. הוא מתמודד עם מבטאים שונים, רעשי רקע ושיחות בכמה שפות.

היכולות העיקריות:

- **זיהוי אוטומטי של דיבור (ASR):** זיהוי אוטומטי של שפות ב[למעלה מ-85 לוקאלים](#supported-languages). הוא מטפל בערבוב שפות בתוך משפט ובין משפטים בלי הגדרה ידנית.
- **אוצר מילים מותאם אישית:** כדי להטות את הזיהוי למונחים, לראשי תיבות ולשמות פרטיים ספציפיים לדומיין, אפשר להעביר עד 1,000 ביטויים.
- **הפרדה בין דוברים:** מבחינה בין כמה דוברים ומשייכת את הקטעים המדוברים לתוויות שונות.
- **חותמות זמן ברמת המילה:** המערכת יוצרת היסטים מדויקים של שעת ההתחלה ושעת הסיום לכל מילה מזוהה.
- **תמלול חכם:** מוחק מילים מיותרות, חזרות ואי-רציפויות, ומחיל עיצוב מובנה.
- **עיצוב ונורמליזציה:** הפונקציה מוסיפה אותיות רישיות וסימני פיסוק, ומבצעת נורמליזציה הפוכה של טקסט, למשל המרה של "twenty six million dollars" ל-"$26M".

כדי לקבל תשובות לשאלות או נימוקים כלליים לגבי תוכן אודיו, אפשר להשתמש ב[הבנת אודיו](https://ai.google.dev/gemini-api/docs/generate-content/audio?hl=he). כדי לבצע סינתזה של אודיו מהמרת טקסט לדיבור, משתמשים ב[המרת טקסט לדיבור](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=he).

## זיהוי שפה ורמזים

כברירת מחדל, המודל מזהה את השפה המדוברת באופן אוטומטי. הוא עובר בין שפות באופן דינמי כשהדוברים מבצעים החלפת קודים.

כדי להשתמש בזיהוי אוטומטי, משמיטים את `language_codes` או מספקים רשימה ריקה:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-transcribe",
    contents=[audio_file],
    config=types.GenerateContentConfig(
        audio_transcription_config=types.AudioTranscriptionConfig(
            language_codes=[],
        )
    ),
)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.5-transcribe",
  contents: [audioFile],
  config: {
    audioTranscriptionConfig: {
      languageCodes: [],
    },
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-transcribe:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "fileData": {
              "fileUri": "YOUR_FILE_URI",
              "mimeType": "audio/mp3"
            }
          }
        ]
      }
    ],
    "generationConfig": {
      "audioTranscriptionConfig": {
        "languageCodes": []
      }
    }
  }'
```

אם אתם יודעים מראש את השפה, כדאי לציין קודי שפה בתקן BCP-47 ב-`language_codes` כדי לשפר את דיוק התמלול (ראו [שפות נתמכות](#supported-languages)):

### Python

```
config = types.GenerateContentConfig(
    audio_transcription_config=types.AudioTranscriptionConfig(
        language_codes=["es-ES"],
    )
)
```

### JavaScript

```
const config = {
  audioTranscriptionConfig: {
    languageCodes: ["es-ES"],
  },
};
```

### REST

```
{
  "generationConfig": {
    "audioTranscriptionConfig": {
      "languageCodes": ["es-ES"]
    }
  }
}
```

## אוצר מילים בהתאמה אישית

אתם יכולים להכווין את מודל הדיבור למילים לא נפוצות, למונחים מקצועיים, לשמות מותגים או לשמות עצם פרטיים. מספקים עד 1,000 מונחים במערך `custom_vocabulary` (בדרך כלל מקבלים את התוצאות הטובות ביותר עם עד 100 מונחים):

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-transcribe",
    contents=[audio_file],
    config=types.GenerateContentConfig(
        audio_transcription_config=types.AudioTranscriptionConfig(
            custom_vocabulary=["Gemini", "Kubernetes", "BigQuery"],
        )
    ),
)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.5-transcribe",
  contents: [audioFile],
  config: {
    audioTranscriptionConfig: {
      customVocabulary: ["Gemini", "Kubernetes", "BigQuery"],
    },
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-transcribe:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "fileData": {
              "fileUri": "YOUR_FILE_URI",
              "mimeType": "audio/mp3"
            }
          }
        ]
      }
    ],
    "generationConfig": {
      "audioTranscriptionConfig": {
        "customVocabulary": ["Gemini", "Kubernetes", "BigQuery"]
      }
    }
  }'
```

## חלוקת קובץ האודיו לפי דוברים

התכונה 'זיהוי דוברים' מזהה קולות שונים בהקלטה ומתייגת כל קטע במזהה דובר כמו `spk_1` או `spk_2`. יש תמיכה בעד 8 דוברים (השיוך ל-3 דוברים או יותר הוא ניסיוני).

כדי להפעיל את החלוקה לפי דוברים, מגדירים את `diarization` ל-`True`:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-transcribe",
    contents=[audio_file],
    config=types.GenerateContentConfig(
        audio_transcription_config=types.AudioTranscriptionConfig(
            diarization=True,
        )
    ),
)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.5-transcribe",
  contents: [audioFile],
  config: {
    audioTranscriptionConfig: {
      diarization: true,
    },
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-transcribe:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "fileData": {
              "fileUri": "YOUR_FILE_URI",
              "mimeType": "audio/mp3"
            }
          }
        ]
      }
    ],
    "generationConfig": {
      "audioTranscriptionConfig": {
        "diarization": true
      }
    }
  }'
```

## חותמות זמן ברמת המילה

חותמות זמן ברמת המילה מספקות היסטים מדויקים של התחלה וסיום לכל מילה מזוהה בשידור האודיו.

כדי להפעיל חותמות זמן, מגדירים את `word_timestamp` ל-`True`:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-transcribe",
    contents=[audio_file],
    config=types.GenerateContentConfig(
        audio_transcription_config=types.AudioTranscriptionConfig(
            word_timestamp=True,
        )
    ),
)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.5-transcribe",
  contents: [audioFile],
  config: {
    audioTranscriptionConfig: {
      wordTimestamp: true,
    },
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-transcribe:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "fileData": {
              "fileUri": "YOUR_FILE_URI",
              "mimeType": "audio/mp3"
            }
          }
        ]
      }
    ],
    "generationConfig": {
      "audioTranscriptionConfig": {
        "wordTimestamp": true
      }
    }
  }'
```

אפשר לשלב בין `diarization` לבין `word_timestamp` בבקשה אחת כדי לקבל גם תוויות לזיהוי דוברים וגם חותמות זמן של המילים:

### Python

```
config = types.GenerateContentConfig(
    audio_transcription_config=types.AudioTranscriptionConfig(
        diarization=True,
        word_timestamp=True,
    )
)
```

### JavaScript

```
const config = {
  audioTranscriptionConfig: {
    diarization: true,
    wordTimestamp: true,
  },
};
```

### REST

```
{
  "generationConfig": {
    "audioTranscriptionConfig": {
      "diarization": true,
      "wordTimestamp": true
    }
  }
}
```

## מצבי תמלול

‫Gemini 3.5 Transcribe תומך בשני מצבי תמלול באמצעות הפרמטר `mode`:

- ‫**`VERBATIM` (ברירת מחדל)**: מחזיר תמליל מדויק מילה במילה של כל מה שנאמר, כולל מילות מילוי לא ערוכות (כמו 'אה', 'אממ', 'כאילו', 'אתה יודע'), חזרות, הפסקות והתחלות שגויות. חובה כשמשתמשים בחותמות זמן או בהפרדה בין הדוברים.
- ‫**`SMART` (תמלול חכם)**: התמלול עובר אופטימיזציה לקריאה באמצעות עיבוד מתקדם:
  - **הסרת מילים מיותרות**: מסירה מילים מיותרות, גמגום והתחלות שגויות.
  - **תיקונים עצמיים בתוך המשפט**: תיקונים שמתבצעים במהלך הדיבור נפתרים באופן ישיר (לדוגמה, *"בוא ניפגש ביום שלישי, בעצם לא, ביום רביעי בשעה שתיים"* הופך ל-*"בוא ניפגש ביום רביעי בשעה 14:00"*).
  - **עיצוב מובנה אוטומטי**: המערכת מעצבת באופן אוטומטי את המחשבות המדוברות לפסקאות, לרשימות ממוספרות, לתבליטים, לתאריכים, למטבעות ולמספרים מעוצבים.
  - **ניקוי דקדוקי**: הוספת פיסוק טבעי, שימוש באותיות רישיות בתחילת משפטים ושיפור הרצף.

| אודיו של דיבור | פלט `VERBATIM` | פלט של `SMART` (תמלול חכם) |
| --- | --- | --- |
| "אה, אז לפגישה, אני חושב שכדאי לנו, אה, להזמין את אליס ו, רגע, לא, את בוב ואת קרול." | "אממ אז לפגישה אני חושב שכדאי לנו להזמין את אליס, רגע לא, את בוב ואת קרול". | "לפגישה, אני חושב שכדאי להזמין את בוב ואת קרול". |
| ‫"First item review budget second item finalize timeline third item send recap" | ‫"first item review budget second item finalize timeline third item send recap" | "1. בודקים את התקציב 2. סיום העריכה של ציר הזמן 3. שליחת סיכום" |

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-transcribe",
    contents=[audio_file],
    config=types.GenerateContentConfig(
        audio_transcription_config=types.AudioTranscriptionConfig(
            mode="SMART",
        )
    ),
)
print(response.text)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.5-transcribe",
  contents: [audioFile],
  config: {
    audioTranscriptionConfig: {
      mode: "SMART",
    },
  },
});
console.log(response.text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-transcribe:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "fileData": {
              "fileUri": "YOUR_FILE_URI",
              "mimeType": "audio/mp3"
            }
          }
        ]
      }
    ],
    "generationConfig": {
      "audioTranscriptionConfig": {
        "mode": "SMART"
      }
    }
  }'
```

## ניתוח פלט התמלול

הטקסט המלא של התמליל מוחזר ב-`response.text`.

כשמפעילים את `word_timestamp` או את `diarization`, ה-API מחזיר גם הערות מפורטות ברמת המילה ותוויות לזיהוי דוברים שמצורפות לחלקים הרלוונטיים.

כך מחלצים את חותמות הזמן של המילים ואת תור הדיבור של הדוברים וחוזרים עליהם שוב ושוב:

### Python

```
def extract_word_transcriptions(response):
    words = []
    for candidate in getattr(response, "candidates", []) or []:
        content = getattr(candidate, "content", None)
        for part in getattr(content, "parts", []) or []:
            transcription = getattr(part, "audio_transcription", None)
            if transcription:
                speaker = getattr(transcription, "speaker_label", "")
                for word_info in getattr(transcription, "words", []) or []:
                    word = getattr(word_info, "word", "")
                    start = getattr(word_info, "start_offset", "")
                    end = getattr(word_info, "end_offset", "")
                    words.append({
                        "word": word,
                        "speaker": speaker,
                        "start_offset": start,
                        "end_offset": end,
                    })
    return words

words = extract_word_transcriptions(response)

for w in words:
    speaker = f"[{w['speaker']}] " if w["speaker"] else ""
    timing = f"({w['start_offset']} -> {w['end_offset']}) " if w["start_offset"] and w["end_offset"] else ""
    print(f"{speaker}{timing}{w['word']}")
```

### JavaScript

```
function extractWordTranscriptions(response) {
  const words = [];
  for (const candidate of response.candidates ?? []) {
    for (const part of candidate.content?.parts ?? []) {
      const transcription = part.audioTranscription;
      if (transcription) {
        const speaker = transcription.speakerLabel ?? "";
        for (const wordInfo of transcription.words ?? []) {
          words.push({
            word: wordInfo.word ?? "",
            speaker: speaker,
            startOffset: wordInfo.startOffset ?? "",
            endOffset: wordInfo.endOffset ?? "",
          });
        }
      }
    }
  }
  return words;
}

const words = extractWordTranscriptions(response);

for (const w of words) {
  const speaker = w.speaker ? `[${w.speaker}] ` : "";
  const timing = (w.startOffset && w.endOffset) ? `(${w.startOffset} -> ${w.endOffset}) ` : "";
  console.log(`${speaker}${timing}${w.word}`);
}
```

### REST

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "audioTranscription": {
              "speakerLabel": "spk_1",
              "words": [
                {
                  "word": "Hello",
                  "startOffset": "0.100s",
                  "endOffset": "0.450s"
                },
                {
                  "word": "world",
                  "startOffset": "0.500s",
                  "endOffset": "0.850s"
                }
              ]
            }
          }
        ],
        "role": "model"
      },
      "finishReason": "STOP"
    }
  ]
}
```

## שפות נתמכות

השפות הבאות וקודי השפה שלהן בתקן BCP-47 נתמכות ב-Gemini 3.5 Transcribe:

| שפה | קוד BCP-47 | שפה | קוד BCP-47 |
| --- | --- | --- | --- |
| אפריקאנס | `af-ZA` | יפנית | `ja-JP` |
| אמהרית | `am-ET` | ג'אווה | `jv-ID` |
| ערבית (מצרים) | `ar-EG` | קאבוורדיאנו | `kea-CV` |
| ארמנית | `hy-AM` | קנאדה | `kn-IN` |
| אסאמית | `as-IN` | קזחית | `kk-KZ` |
| אזרית | `az-AZ` | קוריאנית | `ko-KR` |
| בלארוסית | `be-BY` | קירגיזית | `ky-KG` |
| בנגלית (בנגלדש) | `bn-BD` | לטבית | `lv-LV` |
| בנגלית (הודו) | `bn-IN` | לינגלה | `ln-CD` |
| בוסנית | `bs-BA` | ליטאית | `lt-LT` |
| בולגרית | `bg-BG` | מקדונית | `mk-MK` |
| בולגרית (ארומנית) | `rup-BG` | מלאית | `ms-MY` |
| בורמזית | `my-MM` | מליאלאם | `ml-IN` |
| קנטונזית (מסורתית) | `yue-Hant-HK` | מלטית | `mt-MT` |
| קטלאנית | `ca-ES` | סינית מנדרינית (פשוטה) | `cmn-Hans-CN` |
| סבואנו | `ceb` | מראטהית | `mr-IN` |
| חמר מרכזית | `km-KH` | מונגולית | `mn-MN` |
| קרואטית | `hr-HR` | נפאלית | `ne-NP` |
| צ'כית | `cs-CZ` | נורווגית | `nb-NO` |
| דנית | `da-DK` | אורייה | `or-IN` |
| הולנדית | `nl-NL` | פולנית | `pl-PL` |
| אנגלית (בריטניה) | `en-GB` | פורטוגזית (ברזיל) | `pt-BR` |
| אנגלית (הודו) | `en-IN` | פורטוגזית (פורטוגל) | `pt-PT` |
| אנגלית (ארצות הברית) | `en-US` | פנג'אבי | `pa-IN` |
| אסטונית | `et-EE` | פנג'אבי (כתב גורמוקי) | `pa-Guru-IN` |
| פרסית | `fa-IR` | רומנית | `ro-RO` |
| פיליפינית | `fil-PH` | רוסית | `ru-RU` |
| פינית | `fi-FI` | סרבית | `sr-RS` |
| צרפתית | `fr-FR` | סינדהי (כתב ערבי) | `sd-Arab-IN` |
| גליציאנית | `gl-ES` | סלובקית | `sk-SK` |
| גאורגית | `ka-GE` | סלובנית | `sl-SI` |
| גרמנית | `de-DE` | ספרדית (אמריקה הלטינית) | `es-419` |
| יוונית | `el-GR` | ספרדית (ארצות הברית) | `es-US` |
| גוג'ראטי | `gu-IN` | סוואהילית (קניה) | `sw-KE` |
| האוסה | `ha-NG` | שוודית | `sv-SE` |
| עברית | `he-IL` | טג'יקית | `tg-TJ` |
| הינדי | `hi-IN` | טלוגו | `te-IN` |
| הונגרית | `hu-HU` | תאית | `th-TH` |
| איסלנדית | `is-IS` | טורקית | `tr-TR` |
| אנגלית הודית | `en-IN` | אוקראינית | `uk-UA` |
| אינדונזית | `id-ID` | אוזבקית | `uz-UZ` |
| איטלקית | `it-IT` | וייטנאמית | `vi-VN` |

## פורמטים נתמכים של אודיו

‫Gemini 3.5 Transcribe תומך בסוגי ה-MIME הבאים של פורמט אודיו:

- ‫WAV – `audio/wav`
- MP3 - `audio/mp3`
- AIFF - `audio/aiff`
- ‫AAC – `audio/aac`
- ‫OGG – `audio/ogg`
- ‫FLAC – `audio/flac`
- MPEG - `audio/mpeg`
- M4A - `audio/m4a`
- L16 - `audio/l16`
- Opus – `audio/opus`
- ALAW - `audio/alaw`
- MULAW - `audio/mulaw`
- ‫WebM – `audio/webm`

רשימה מלאה של סוגי ה-MIME הנתמכים וסכימות הפרמטרים מופיעה [במאמר בנושא Interactions API](https://ai.google.dev/api/interactions-api?hl=he#Resource:Content).

## הפניה לפרמטר

כדי להגדיר תמלול, צריך להגדיר שדות באובייקט `audio_transcription_config` ב-`GenerateContentConfig`:

| שדה | סוג | תיאור |
| --- | --- | --- |
| `language_codes` | מערך של מחרוזות | קודי שפה בתקן BCP-47 (למשל, `["en-US"]`). אם לא מציינים קוד או אם הקוד ריק (`[]`), המודל מזהה את השפה באופן אוטומטי ומטפל בהחלפת קודים. |
| `custom_vocabulary` | מערך של מחרוזות | עד 1,000 מונחים מותאמים אישית, ראשי תיבות או שמות עצם כדי להטות את זיהוי הדיבור. האפשרות לא תואמת לסימון דוברים ולחותמות זמן ברמת המילה. |
| `word_timestamp` | בוליאני | מגדירים את הערך `True` כדי לכלול את ההיסטים של תחילת המילה וסוף המילה. אם משמיטים את הפרמטר או מציינים את הערך `False`, לא מוחזרות חותמות זמן של מילים. לא תואם לאוצר מילים מותאם אישית. |
| `diarization` | בוליאני | מגדירים את האפשרות `True` כדי לזהות דוברים שונים ולהוסיף להם תוויות. לא תואם לאוצר מילים מותאם אישית. |
| `mode` | מחרוזת | מצב תמלול. ערכים נתמכים: `"VERBATIM"` (ברירת מחדל) ו-`"SMART"`. לא תואם לחותמות זמן ולזיהוי דוברים. |

## שיטות מומלצות

- **הקלטת אודיו ברור:** חשוב לוודא שההקלטות של האודיו כוללות הפרדה ברורה של הקולות, ולהימנע מקטיעת אודיו חמורה.
- **הוספת רמזים לגבי השפה כשמכירים אותה:** אם אתם יודעים מראש מה השפה של האודיו, כדאי לציין את `language_codes` כדי לשפר את הדיוק.
- **אוצר מילים מותאם אישית ליעד:** כדאי לכלול ב-`custom_vocabulary` רק מונחים ייחודיים שקשורים לדומיין, שמות של מותגים או שמות עצם, ולא מילים נפוצות שמשמשות בחיי היום-יום.
- **שימוש ב-Files API להקלטות ארוכות:** לקבצים שאורכם כמה שניות או יותר, מעלים את הקובץ באמצעות `client.files.upload` ומעבירים את הקובץ שמוחזר לתוכן המודל.

## מגבלות

- **משך האודיו:** בקשות סטנדרטיות של unary תומכות בקובצי אודיו באורך של עד שעה. כשמפעילים תכונות כמו זיהוי דוברים או חותמות זמן ברמת המילה, עיבוד האודיו מוגבל ל-30 דקות.
- **חותמות זמן ברמת המילה:** הפעלת חותמות זמן ברמת המילה עלולה לפגוע בדיוק הכולל של התמלול.
- **חלוקת קובץ האודיו לפי דוברים:** חלוקת קובץ האודיו לפי דוברים תומכת בעד 8 דוברים. השיוך של דוברים בשיחות עם 3 דוברים או יותר הוא ניסיוני.
- **אוצר מילים מותאם אישית:** אפשר לספק עד 1,000 מונחים ב-`custom_vocabulary`, אבל בדרך כלל התוצאות הכי טובות מתקבלות עם עד 100 מונחים. אי אפשר לשלב את `custom_vocabulary` עם תיוג דוברים או עם חותמות זמן ברמת המילה. ה-API דוחה בקשות שמציינות את `custom_vocabulary` לצד אחת מהתכונות האלה.
- **תאימות למצבים:** אי אפשר לשלב תמלול חכם (`mode: "SMART"`) עם `word_timestamp` או `diarization`.

## המאמרים הבאים

- אתם יכולים להזרים אודיו בזמן אמת באמצעות [המדריך לתמלול בזמן אמת](https://ai.google.dev/gemini-api/docs/live-api/live-transcribe?hl=he) באמצעות Live API.
- אפשר להשתמש ב[הבנת אודיו](https://ai.google.dev/gemini-api/docs/generate-content/audio?hl=he) כדי לנתח, לסכם או לשאול שאלות לגבי תוכן אודיו.
- [איך מסנתזים אודיו מטקסט באמצעות המרת טקסט לדיבור](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=he)
- [בדף התמחור](https://ai.google.dev/gemini-api/docs/pricing?hl=he#gemini-3.5-transcribe) מפורטים המחירים של המודלים ומגבלות הטוקנים.
- במדריך [Files API](https://ai.google.dev/gemini-api/docs/files?hl=he) מוסבר איך להעלות ולנהל קובצי מדיה.

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-09-08 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-09-08 (שעון UTC)."],[],[]]
