---
source_url: https://ai.google.dev/gemini-api/docs/gemini-3?hl=he
fetched_at: 2026-06-01T05:58:13.260032+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=he) זמין עכשיו בתצוגה מקדימה עם תכונות כמו תכנון שיתופי, ויזואליזציה, תמיכה ב-MCP ועוד.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [generateContent API](https://ai.google.dev/gemini-api/docs/generate-content?hl=he)

שליחת משוב

# מדריך למפתחים של Gemini 3

‫Gemini 3 הוא קבוצת המודלים הכי חכמה שלנו עד היום, שמבוססת על יכולות חשיבה רציונלית מתקדמות. הוא נועד להפוך כל רעיון למציאות באמצעות שליטה בתהליכי עבודה של סוכנים, בקידוד אוטונומי ובמשימות מורכבות מרובות-אופנים.
במדריך הזה נסביר על התכונות העיקריות של משפחת מודלים Gemini 3 ואיך להפיק ממנה את המרב.

[לניסיון Gemini 3.1 Pro בגרסת טרום-השקה](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-pro-preview&hl=he)
[לניסיון Gemini 3 Flash בגרסת טרום-השקה](https://aistudio.google.com/prompts/new_chat?model=gemini-3-flash-preview&hl=he)
[לניסיון Gemini 3.1 Flash-Lite](https://aistudio.google.com/prompts/new_chat?model=gemini-3-flash-lite&hl=he)
[לניסיון Nano Banana 2](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-image-preview&hl=he)

כדאי לעיין [באוסף אפליקציות Gemini 3](https://aistudio.google.com/app/apps?source=showcase&%3BshowcaseTag=gemini-3&hl=he) כדי לראות איך המודל מתמודד עם חשיבה רציונלית משופרת, תכנות אוטונומי ומשימות מורכבות מולטי-מודאליות.

כדי להתחיל, אפשר להשתמש בכמה שורות קוד:

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="Find the race condition in this multi-threaded C++ snippet: [code here]",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "Find the race condition in this multi-threaded C++ snippet: [code here]",
  });

  console.log(response.text);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Find the race condition in this multi-threaded C++ snippet: [code here]"}]
    }]
  }'
```

## הכירו את סדרת Gemini 3

‫Gemini 3.1 Pro הוא המודל הכי טוב למשימות מורכבות שדורשות ידע רחב על העולם וחשיבה רציונלית משופרת במגוון תחומים.

‫Gemini 3 Flash הוא המודל העדכני ביותר בסדרת 3, עם יכולות AI חכמות ברמת Pro, במהירות ובמחיר של Flash.

‫Nano Banana Pro (שנקרא גם Gemini 3 Pro Image) הוא המודל שלנו ליצירת תמונות באיכות הכי גבוהה, ו-Nano Banana 2 (שנקרא גם Gemini 3.1 Flash Image) הוא המודל המקביל ליצירת תמונות בכמויות גדולות, ביעילות גבוהה ובמחיר נמוך יותר.

‫Gemini 3.1 Flash-Lite הוא המודל המתקדם שלנו שנועד לבצע משימות בהיקף גדול בצורה חסכונית.

| מזהה דגם | חלון ההקשר (נכנס / יוצא) | תאריך סף הידע | מחירים (קלט / פלט)\* |
| --- | --- | --- | --- |
| **gemini-3.1-flash-lite** | ‫1M / 64k | ינואר 2025 | ‫0.25$ (טקסט, תמונה, סרטון), 0.50$ (אודיו) / 1.50$ |
| **gemini-3.1-flash-image-preview** | ‫128k / 32k | ינואר 2025 | ‫0.25$ (קלט טקסט) / 0.067$ (פלט תמונה)\*\* |
| **gemini-3.1-pro-preview** | ‫1M / 64k | ינואר 2025 | ‫2$ / 12$ (פחות מ-200k טוקנים)   4$ / 18$ (יותר מ-200k טוקנים) |
| **gemini-3-flash-preview** | ‫1M / 64k | ינואר 2025 | ‫0.50$ / 3$‎ |
| **gemini-3-pro-image-preview** | ‫65,000 / 32,000 | ינואר 2025 | ‫2$ (הזנת טקסט) / 0.134$ (פלט תמונה)\*\* |

*\* המחירים הם למיליון טוקנים, אלא אם צוין אחרת.*
*\*\* המחיר של התמונות משתנה בהתאם לרזולוציה. פרטים נוספים מופיעים ב[דף התמחור](https://ai.google.dev/gemini-api/docs/pricing?hl=he).*

מידע נוסף על מגבלות, תמחור ופרטים נוספים זמין ב[דף המודלים](https://ai.google.dev/gemini-api/docs/models/gemini?hl=he).

## תכונות חדשות ב-Gemini 3 API

‫Gemini 3 כולל פרמטרים חדשים שנועדו לתת למפתחים יותר שליטה בחביון, בעלות ובנאמנות של מודלים מרובי-מוֹדָלִים.

### רמת ההעמקה

מודלים מסדרת Gemini 3 משתמשים כברירת מחדל בחשיבה דינמית כדי להסיק מסקנות מההנחיות. אפשר להשתמש בפרמטר `thinking_level`, ששולט על **העומק המקסימלי** של תהליך החשיבה הרציונלית הפנימי של המודל לפני שהוא מפיק תשובה. ‫Gemini 3 מתייחס לרמות האלה כאל הקצאות יחסיות של משאבים לצורך חשיבה, ולא כאל הבטחות מחמירות לגבי טוקנים.

אם לא מציינים את `thinking_level`, Gemini 3 ישתמש כברירת מחדל ב-`high`. כדי לקבל תשובות מהירות יותר עם חביון נמוך יותר כשלא נדרשת חשיבה רציונלית מורכבת, אפשר להגביל את רמת החשיבה של המודל ל-`low`.

| רמת ההעמקה | ‫Gemini 3.1 Pro | Gemini 3.1 Flash-Lite | Gemini 3 Flash | תיאור |
| --- | --- | --- | --- | --- |
| **`minimal`** | לא נתמך | נתמך (ברירת מחדל) | נתמך | מתאים להגדרה 'ללא חשיבה' ברוב השאילתות. יכול להיות שהמודל יחשוב מעט מאוד כדי לעבוד על משימות מורכבות של כתיבת קוד. מצמצם את זמן האחזור של אפליקציות צ'אט או אפליקציות עם תפוקה גבוהה. הערה: `minimal` לא מבטיח שהחשיבה מושבתת. |
| **`low`** | נתמך | נתמך | נתמך | מצמצם את זמן האחזור ואת העלות. הכי טוב למעקב אחרי הוראות פשוטות, לצ'אט או לאפליקציות עם תפוקה גבוהה. |
| **`medium`** | נתמך | נתמך | נתמך | חשיבה מאוזנת לרוב המשימות. |
| **`high`** | נתמך (ברירת מחדל, דינמי) | נתמך (דינמי) | נתמך (ברירת מחדל, דינמי) | העומק המקסימלי של החשיבה הרציונלית. יכול להיות שיעבור הרבה יותר זמן עד שהמודל יגיע לטוקן הפלט הראשון (שלא קשור לחשיבה), אבל הפלט יהיה מנומק יותר. |

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="How does AI work?",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="low")
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "How does AI work?",
    config: {
      thinkingConfig: {
        thinkingLevel: "low",
      }
    },
  });

console.log(response.text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "How does AI work?"}]
    }],
    "generationConfig": {
      "thinkingConfig": {
        "thinkingLevel": "low"
      }
    }
  }'
```

### רזולוציית המדיה

‫Gemini 3 מציג שליטה מפורטת בעיבוד של ראייה מולטימודאלית באמצעות הפרמטר `media_resolution`. רזולוציות גבוהות יותר משפרות את היכולת של המודל לקרוא טקסט קטן או לזהות פרטים קטנים, אבל הן מגדילות את השימוש בטוקנים ואת זמן האחזור.
הפרמטר `media_resolution` קובע את **מספר הטוקנים המקסימלי שהוקצה לכל תמונה או פריים של סרטון קלט.**

עכשיו אפשר להגדיר את הרזולוציה ל-`media_resolution_low`,‏ `media_resolution_medium`,‏ `media_resolution_high` או `media_resolution_ultra_high` לכל קטע מדיה בנפרד או באופן גלובלי (דרך `generation_config`, האפשרות הגלובלית לא זמינה לרזולוציה גבוהה במיוחד). אם לא צוין, המודל משתמש בברירות מחדל אופטימליות על סמך סוג המדיה.

**הגדרות מומלצות**

| סוג מדיה | הגדרה מומלצת | מספר מקסימלי של טוקנים | הנחיות לשימוש |
| --- | --- | --- | --- |
| **תמונות** | `media_resolution_high` | 1120 | מומלץ לרוב משימות ניתוח התמונות כדי להבטיח איכות מקסימלית. |
| **קובצי PDF** | `media_resolution_medium` | 560 | אופטימלי להבנת מסמכים. האיכות מגיעה בדרך כלל לנקודת רוויה ב-`medium`. הגדלה ל-`high` משפרת לעיתים רחוקות את תוצאות ה-OCR במסמכים רגילים. |
| **סרטון** (כללי) | `media_resolution_low` (או `media_resolution_medium`) | ‫70 (לכל פריים) | **הערה:** כשמדובר בסרטונים, ההגדרות `low` ו-`medium` מטופלות באופן זהה (70 טוקנים) כדי לייעל את השימוש בהקשר. זה מספיק לרוב המשימות של זיהוי פעולות ותיאור שלהן. |
| **סרטון** (הרבה טקסט) | `media_resolution_high` | ‫280 (לכל פריים) | נדרש רק אם תרחיש השימוש כולל קריאת טקסט צפוף (OCR) או פרטים קטנים בתוך פריים של סרטון. |

### Python

```
from google import genai
from google.genai import types
import base64

# The media_resolution parameter is currently only available in the v1alpha API version.
client = genai.Client(http_options={'api_version': 'v1alpha'})

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents=[
        types.Content(
            parts=[
                types.Part(text="What is in this image?"),
                types.Part(
                    inline_data=types.Blob(
                        mime_type="image/jpeg",
                        data=base64.b64decode("..."),
                    ),
                    media_resolution={"level": "media_resolution_high"}
                )
            ]
        )
    ]
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

// The media_resolution parameter is currently only available in the v1alpha API version.
const ai = new GoogleGenAI({ apiVersion: "v1alpha" });

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: [
      {
        parts: [
          { text: "What is in this image?" },
          {
            inlineData: {
              mimeType: "image/jpeg",
              data: "...",
            },
            mediaResolution: {
              level: "media_resolution_high"
            }
          }
        ]
      }
    ]
  });

  console.log(response.text);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1alpha/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [
        { "text": "What is in this image?" },
        {
          "inlineData": {
            "mimeType": "image/jpeg",
            "data": "..."
          },
          "mediaResolution": {
            "level": "media_resolution_high"
          }
        }
      ]
    }]
  }'
```

### טמפרטורה

בכל המודלים של Gemini 3, מומלץ מאוד להשאיר את פרמטר רמת האקראיות בערך ברירת המחדל שלו, `1.0`.

במודלים קודמים, כדאי היה לשנות את הגדרת רמת האקראיות כדי לשלוט באיזון בין יצירתיות לבין דטרמיניזם. לעומת זאת, יכולות החשיבה הרציונלית של Gemini 3 מותאמות להגדרת ברירת המחדל. שינוי רמת האקראיות (הגדרה של ערך נמוך מ-1.0) עלול להוביל להתנהגות לא צפויה, כמו לולאה או ביצועים ירודים, במיוחד במשימות מורכבות של מתמטיקה או חשיבה רציונלית.

### חתימות של מחשבות

‫Gemini 3 משתמש ב[חתימות מחשבה](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=he) כדי לשמור על הקשר של ההנמקה בכל קריאות ה-API. החתימות האלה הן ייצוגים מוצפנים של תהליך החשיבה הפנימי של המודל. כדי לוודא שהמודל ישמור על יכולות החשיבה הרציונלית שלו, צריך להחזיר את החתימות האלה למודל בבקשה בדיוק כמו שהן התקבלו:

- **קריאה לפונקציה (מחמירה):** ה-API מבצע אימות מחמיר של 'התור הנוכחי'. אם חתימות חסרות, תוצג שגיאת 400.
- **טקסט/צ'אט:** אין אכיפה קפדנית של אימות, אבל אם לא תציינו חתימות, איכות הנימוקים והתשובות של המודל תרד.
- **יצירה או עריכה של תמונות (מחמיר)**: ה-API מבצע אימות מחמיר של כל חלקי המודל, כולל `thoughtSignature`. אם חתימות חסרות, תוצג שגיאת 400.

#### בקשה להפעלת פונקציה (אימות קפדני)

כש-Gemini יוצר `functionCall`, הוא מסתמך על `thoughtSignature` כדי לעבד את הפלט של הכלי בצורה נכונה בתור הבא. הקטע 'תור נוכחי' כולל את כל השלבים של המודל (`functionCall`) והמשתמש (`functionResponse`) שהתרחשו מאז ההודעה האחרונה של **המשתמש** `text`.

- **קריאה יחידה לפונקציה:** החלק `functionCall` מכיל חתימה. עליך להחזיר את המכשיר.
- **קריאות לפונקציות במקביל:** רק החלק הראשון `functionCall` ברשימה יכיל את החתימה. צריך להחזיר את החלקים בדיוק בסדר שבו הם התקבלו.
- **רב-שלבי (עוקב):** אם המודל מפעיל כלי, מקבל תוצאה ומפעיל *כלי אחר* (באותה תור), **שתי** בקשות להפעלת פונקציה מופעלות עם חתימות. אתם צריכים להחזיר **את כל** החתימות שנצברו בהיסטוריה.

#### טקסט וסטרימינג

בצ'אט רגיל או ביצירת טקסט, לא מובטח שתהיה חתימה.

- **ללא סטרימינג**: החלק האחרון של התשובה עשוי להכיל `thoughtSignature`, אבל הוא לא תמיד מופיע. אם מוחזרת אחת, כדאי לשלוח אותה בחזרה כדי לשמור על הביצועים הטובים ביותר.
- **סטרימינג**: אם נוצרת חתימה, יכול להיות שהיא תגיע בחלק סופי שמכיל חלק טקסט ריק. מוודאים שהכלי לניתוח הזרם בודק חתימות גם אם שדה הטקסט ריק.

#### יצירה ועריכה של תמונות

במקרה של `gemini-3-pro-image-preview` ו-`gemini-3.1-flash-image-preview`, חתימות מחשבה הן קריטיות לעריכה בממשק שיחה. כשמבקשים מהמודל לשנות תמונה, הוא מסתמך על `thoughtSignature` מהתור הקודם כדי להבין את הקומפוזיציה והלוגיקה של התמונה המקורית.

- **עריכה:** החתימות מופיעות בחלק הראשון אחרי המחשבות של התשובה (`text` או `inlineData`) ובכל חלק `inlineData` שבהמשך. כדי למנוע שגיאות, צריך להחזיר את כל החתימות האלה.

#### דוגמאות לקוד

#### בקשות להפעלת פונקציות רבות (עוקבות)

המשתמש שואל שאלה שדורשת שני שלבים נפרדים (בדיקת טיסה -> הזמנת מונית) בתור אחד.   
  
**שלב 1: מפעילים את הכלי 'תחזית תנועה'**  
המודל מחזיר חתימה `<Sig_A>`

```
// Model Response (Turn 1, Step 1)
  {
    "role": "model",
    "parts": [
      {
        "functionCall": { "name": "check_flight", "args": {...} },
        "thoughtSignature": "<Sig_A>" // SAVE THIS
      }
    ]
  }
```

**שלב 2: המשתמש שולח תוצאת חיפוש טיסה**  
אנחנו צריכים להחזיר את `<Sig_A>` כדי לשמור על רצף המחשבה של המודל.

```
// User Request (Turn 1, Step 2)
[
  { "role": "user", "parts": [{ "text": "Check flight AA100..." }] },
  {
    "role": "model",
    "parts": [
      { 
        "functionCall": { "name": "check_flight", "args": {...} },
        "thoughtSignature": "<Sig_A>" // REQUIRED
      }
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": { "name": "check_flight", "response": {...} } }] }
]
```

**שלב 3: המודל מתקשר עם כלי המוניות**  
המודל זוכר את העיכוב בטיסה באמצעות `<Sig_A>` ועכשיו הוא מחליט להזמין מונית. נוצרת חתימה *חדשה* `<Sig_B>`.

```
// Model Response (Turn 1, Step 3)
{
  "role": "model",
  "parts": [
    {
      "functionCall": { "name": "book_taxi", "args": {...} },
      "thoughtSignature": "<Sig_B>" // SAVE THIS
    }
  ]
}
```

**שלב 4: המשתמש שולח תוצאה של מונית**  
כדי להשלים את התור, צריך לשלוח בחזרה את כל השרשרת: `<Sig_A>` וגם `<Sig_B>`.

```
// User Request (Turn 1, Step 4)
[
  // ... previous history ...
  { 
    "role": "model", 
    "parts": [
       { "functionCall": { "name": "check_flight", ... }, "thoughtSignature": "<Sig_A>" }
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": {...} }] },
  { 
    "role": "model", 
    "parts": [
       { "functionCall": { "name": "book_taxi", ... }, "thoughtSignature": "<Sig_B>" }
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": {...} }] }
]
```

#### בקשות להפעלת פונקציות במקביל

המשתמש שואל: "תבדוק את מזג האוויר בפריז ובלונדון". המודל מחזיר שתי קריאות לפונקציות בתשובה אחת.

```
// User Request (Sending Parallel Results)
[
  {
    "role": "user",
    "parts": [
      { "text": "Check the weather in Paris and London." }
    ]
  },
  {
    "role": "model",
    "parts": [
      // 1. First Function Call has the signature
      {
        "functionCall": { "name": "check_weather", "args": { "city": "Paris" } },
        "thoughtSignature": "<Signature_A>" 
      },
      // 2. Subsequent parallel calls DO NOT have signatures
      {
        "functionCall": { "name": "check_weather", "args": { "city": "London" } }
      } 
    ]
  },
  {
    "role": "user",
    "parts": [
      // 3. Function Responses are grouped together in the next block
      {
        "functionResponse": { "name": "check_weather", "response": { "temp": "15C" } }
      },
      {
        "functionResponse": { "name": "check_weather", "response": { "temp": "12C" } }
      }
    ]
  }
]
```

#### טקסט/הסקה בהקשר (ללא אימות)

המשתמש שואל שאלה שדורשת חשיבה רציונלית בהקשר ללא שימוש בכלים חיצוניים. המודל לא מאמת את החתימה באופן מוחלט, אבל הוספת החתימה עוזרת לו לשמור על שרשרת ההיגיון לשאלות המשך.

```
// User Request (Follow-up question)
[
  {
    "role": "user",
    "parts": [{ "text": "What are the risks of this investment?" }]
  },
  {
    "role": "model",
    "parts": [
      {
        "text": "I need to calculate the risk step-by-step. First, I'll look at volatility...",
        "thoughtSignature": "<Signature_C>" // Recommended to include
      }
    ]
  },
  {
    "role": "user",
    "parts": [{ "text": "Summarize that in one sentence." }]
  }
]
```

#### יצירה ועריכה של תמונות

ליצירת תמונות, החתימות עוברות אימות קפדני. הן מופיעות ב**חלק הראשון** (טקסט או תמונה) וב**כל חלקי התמונה הבאים**. צריך להחזיר את כולם בתור הבא.

```
// Model Response (Turn 1)
{
  "role": "model",
  "parts": [
    // 1. First part ALWAYS has a signature (even if text)
    {
      "text": "I will generate a cyberpunk city...",
      "thoughtSignature": "<Signature_D>"
    },
    // 2. ALL InlineData (Image) parts ALWAYS have signatures
    {
      "inlineData": { ... }, 
      "thoughtSignature": "<Signature_E>"
    },
  ]
}

// User Request (Turn 2 - Requesting an Edit)
{
  "contents": [
    // History must include ALL signatures received
    {
      "role": "user",
      "parts": [{ "text": "Generate a cyberpunk city" }]
    },
    {
      "role": "model",
      "parts": [
         { "text": "...", "thoughtSignature": "<Signature_D>" },
         { "inlineData": "...", "thoughtSignature": "<Signature_E>" },
      ]
    },
    // New User Prompt
    {
      "role": "user",
      "parts": [{ "text": "Make it daytime." }]
    }
  ]
}
```

#### העברה ממודלים אחרים

אם אתם מעבירים נתוני מעקב של שיחה ממודל אחר (למשל, Gemini 2.5) או מוסיפים בקשה להפעלת פונקציה בהתאמה אישית שלא נוצרה על ידי Gemini 3, לא תהיה לכם חתימה תקינה.

כדי לעקוף את האימות המחמיר בתרחישים הספציפיים האלה, מאכלסים את השדה במחרוזת ה-placeholder הספציפית הזו: `"thoughtSignature": "context_engineering_is_the_way
to_go"`

### פלט מובנה עם כלים

מודלים של Gemini 3 מאפשרים לכם לשלב [פלט מובנה](https://ai.google.dev/gemini-api/docs/structured-output?hl=he) עם כלים מובנים, כולל [עיגון באמצעות חיפוש Google](https://ai.google.dev/gemini-api/docs/google-search?hl=he), [הקשר של כתובת URL](https://ai.google.dev/gemini-api/docs/url-context?hl=he), [הרצת קוד](https://ai.google.dev/gemini-api/docs/code-execution?hl=he) ו[קריאה לפונקציה](https://ai.google.dev/gemini-api/docs/function-calling?hl=he).

### Python

```
from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from typing import List

class MatchResult(BaseModel):
    winner: str = Field(description="The name of the winner.")
    final_match_score: str = Field(description="The final match score.")
    scorers: List[str] = Field(description="The name of the scorer.")

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="Search for all details for the latest Euro.",
    config={
        "tools": [
            {"google_search": {}},
            {"url_context": {}}
        ],
        "response_format": {"text": {"mime_type": "application/json", "schema": MatchResult.model_json_schema()}},
    },  
)

result = MatchResult.model_validate_json(response.text)
print(result)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";

const ai = new GoogleGenAI({});

const matchSchema = z.object({
  winner: z.string().describe("The name of the winner."),
  final_match_score: z.string().describe("The final score."),
  scorers: z.array(z.string()).describe("The name of the scorer.")
});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "Search for all details for the latest Euro.",
    config: {
      tools: [
        { googleSearch: {} },
        { urlContext: {} }
      ],
      responseFormat: { text: { mimeType: "application/json", schema: zodToJsonSchema(matchSchema) } },
    },
  });

  const match = matchSchema.parse(JSON.parse(response.text));
  console.log(match);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Search for all details for the latest Euro."}]
    }],
    "tools": [
      {"googleSearch": {}},
      {"urlContext": {}}
    ],
    "generationConfig": {
"responseFormat": {
  "text": {
    "mimeType": "application/json",
    "schema": {
            "type": "object",
            "properties": {
                "winner": {"type": "string", "description": "The name of the winner."},
                "final_match_score": {"type": "string", "description": "The final score."},
                "scorers": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The name of the scorer."
                }
  }
}
},
            "required": ["winner", "final_match_score", "scorers"]
        }
    }
  }'
```

### יצירת תמונות

‫Gemini 3.1 Flash Image ו-Gemini 3 Pro Image מאפשרים ליצור ולערוך תמונות על סמך הנחיות טקסט. הוא משתמש בחשיבה רציונלית כדי 'לחשוב' על הנחיה, ויכול לאחזר נתונים בזמן אמת – כמו תחזיות מזג אוויר או תרשימי מניות – לפני שהוא משתמש בעיגון של [חיפוש Google](https://ai.google.dev/gemini-api/docs/google-search?hl=he) כדי ליצור תמונות ברמת דיוק גבוהה.

**יכולות חדשות ומשופרות:**

- **רזולוציית 4K ועיבוד טקסט:** אפשר ליצור טקסט ותרשימים חדים וקריאים ברזולוציות של עד 2K ו-4K.
- **יצירה מבוססת-קרקע:** אפשר להשתמש בכלי `google_search` כדי לאמת עובדות וליצור תמונות על סמך מידע מהעולם האמיתי. ‫Grounding עם חיפוש *תמונות* ב-Google זמין ב-Gemini 3.1 Flash Image.
- **עריכה בממשק שיחה:** עריכת תמונות בכמה שלבים באמצעות הנחיות פשוטות (למשל, "הפוך את הרקע לשקיעה"). תהליך העבודה הזה מסתמך על **חתימות מחשבה** כדי לשמור על ההקשר החזותי בין התורות.

פרטים מלאים על יחסי גובה-רוחב, תהליכי עריכה ואפשרויות הגדרה זמינים [במדריך ליצירת תמונות](https://ai.google.dev/gemini-api/docs/image-generation?hl=he).

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-pro-image-preview",
    contents="Generate an infographic of the current weather in Tokyo.",
    config=types.GenerateContentConfig(
        tools=[{"google_search": {}}],
        response_format={"image": {"aspect_ratio": "16:9", "image_size": "4K"}}
    )
)

image_parts = [part for part in response.parts if part.inline_data]

if image_parts:
    image = image_parts[0].as_image()
    image.save('weather_tokyo.png')
    image.show()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3-pro-image-preview",
    contents: "Generate a visualization of the current weather in Tokyo.",
    config: {
      tools: [{ googleSearch: {} }],
      responseFormat: {
    image: {
        aspectRatio: "16:9",
        imageSize: "4K"
      }
  }
    }
  });

  for (const part of response.candidates[0].content.parts) {
    if (part.inlineData) {
      const imageData = part.inlineData.data;
      const buffer = Buffer.from(imageData, "base64");
      fs.writeFileSync("weather_tokyo.png", buffer);
    }
  }
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Generate a visualization of the current weather in Tokyo."}]
    }],
    "tools": [{"googleSearch": {}}],
    "generationConfig": {
        "responseFormat": {
    "image": {
          "aspectRatio": "16:9",
          "imageSize": "4K"
      }
  }
    }
  }'
```

**דוגמה לתשובה**

![מזג האוויר בטוקיו](https://ai.google.dev/static/gemini-api/docs/images/weather-tokyo.jpg?hl=he)

### ביצוע קוד עם תמונות

‫Gemini 3 Flash יכול להתייחס לראייה כאל חקירה פעילה, ולא רק כאל מבט סטטי. באמצעות שילוב של חשיבה רציונלית עם [הרצת קוד](https://ai.google.dev/gemini-api/docs/code-execution?hl=he), המודל מגבש תוכנית, ואז כותב ומריץ קוד Python כדי לבצע הגדלה, חיתוך, הוספת הערות או פעולות אחרות על תמונות, שלב אחר שלב, כדי לעגן את התשובות שלו באופן ויזואלי.

**תרחישים לדוגמה:**

- **זום ובדיקה:** המודל מזהה באופן מובנה מתי הפרטים קטנים מדי (למשל, קריאת מד או מספר סידורי מרחוק) וכותב קוד לחיתוך ולבדיקה מחדש של האזור ברזולוציה גבוהה יותר.
- **מתמטיקה והצגה גרפית:** המודל יכול להריץ חישובים מרובי-שלבים באמצעות קוד (למשל, סיכום פריטים בחשבונית או יצירת תרשים Matplotlib מנתונים שחולצו).
- **הערות לתמונות:** המודל יכול לצייר חצים, תיבות תוחמות או הערות אחרות ישירות על תמונות כדי לענות על שאלות שקשורות למיקום, כמו 'איפה צריך למקם את הפריט הזה?'.

כדי להפעיל חשיבה ויזואלית, צריך להגדיר את [הפעלת קוד](https://ai.google.dev/gemini-api/docs/code-execution?hl=he) ככלי. המודל ישתמש אוטומטית בקוד כדי לערוך תמונות כשצריך.

### Python

```
from google import genai
from google.genai import types
import requests
from PIL import Image
import io

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image = types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg")

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[
        image,
        "Zoom into the expression pedals and tell me how many pedals are there?"
    ],
    config=types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)]
    ),
)

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    if part.executable_code is not None:
        print(part.executable_code.code)
    if part.code_execution_result is not None:
        print(part.code_execution_result.output)
    if part.as_image() is not None:
        display(Image.open(io.BytesIO(part.as_image().image_bytes)))
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const imageUrl = "https://goo.gle/instrument-img";
  const response = await fetch(imageUrl);
  const imageArrayBuffer = await response.arrayBuffer();
  const base64ImageData = Buffer.from(imageArrayBuffer).toString("base64");

  const result = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: [
      {
        inlineData: {
          mimeType: "image/jpeg",
          data: base64ImageData,
        },
      },
      {
        text: "Zoom into the expression pedals and tell me how many pedals are there?",
      },
    ],
    config: {
      tools: [{ codeExecution: {} }],
    },
  });

  for (const part of result.candidates[0].content.parts) {
    if (part.text) {
      console.log("Text:", part.text);
    }
    if (part.executableCode) {
      console.log("Code:", part.executableCode.code);
    }
    if (part.codeExecutionResult) {
      console.log("Output:", part.codeExecutionResult.output);
    }
  }
}

main();
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"
MODEL="gemini-3-flash-preview"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/$MODEL:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {
              "inline_data": {
                "mime_type":"'"$MIME_TYPE"'",
                "data": "'"$IMAGE_B64"'"
              }
            },
            {"text": "Zoom into the expression pedals and tell me how many pedals are there?"}
        ]
      }],
      "tools": [{"code_execution": {}}]
    }'
```

מידע נוסף על הרצת קוד עם תמונות זמין במאמר בנושא [הרצת קוד](https://ai.google.dev/gemini-api/docs/code-execution?hl=he#images).

### תשובות של פונקציות רב-אופניות

[בקשות להפעלת פונקציות מולטי-מודאליות](https://ai.google.dev/gemini-api/docs/function-calling?hl=he#multimodal)
מאפשרות למשתמשים לקבל תשובות לפונקציות שמכילות
אובייקטים מולטי-מודאליים, וכך לשפר את השימוש ביכולות של המודל להפעלת פונקציות. קריאה רגילה לפונקציה תומכת רק בתשובות לפונקציה שמבוססות על טקסט:

### Python

```
from google import genai
from google.genai import types

import requests

client = genai.Client()

# This is a manual, two turn multimodal function calling workflow:

# 1. Define the function tool
get_image_declaration = types.FunctionDeclaration(
  name="get_image",
  description="Retrieves the image file reference for a specific order item.",
  parameters={
      "type": "object",
      "properties": {
          "item_name": {
              "type": "string",
              "description": "The name or description of the item ordered (e.g., 'instrument')."
          }
      },
      "required": ["item_name"],
  },
)
tool_config = types.Tool(function_declarations=[get_image_declaration])

# 2. Send a message that triggers the tool
prompt = "Show me the instrument I ordered last month."
response_1 = client.models.generate_content(
  model="gemini-3-flash-preview",
  contents=[prompt],
  config=types.GenerateContentConfig(
      tools=[tool_config],
  )
)

# 3. Handle the function call
function_call = response_1.function_calls[0]
requested_item = function_call.args["item_name"]
print(f"Model wants to call: {function_call.name}")

# Execute your tool (e.g., call an API)
# (This is a mock response for the example)
print(f"Calling external tool for: {requested_item}")

function_response_data = {
  "image_ref": {"$ref": "instrument.jpg"},
}
image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
function_response_multimodal_data = types.FunctionResponsePart(
  inline_data=types.FunctionResponseBlob(
    mime_type="image/jpeg",
    display_name="instrument.jpg",
    data=image_bytes,
  )
)

# 4. Send the tool's result back
# Append this turn's messages to history for a final response.
history = [
  types.Content(role="user", parts=[types.Part(text=prompt)]),
  response_1.candidates[0].content,
  types.Content(
    role="user",
    parts=[
        types.Part.from_function_response(
          name=function_call.name,
          response=function_response_data,
          parts=[function_response_multimodal_data]
        )
    ],
  )
]

response_2 = client.models.generate_content(
  model="gemini-3-flash-preview",
  contents=history,
  config=types.GenerateContentConfig(
      tools=[tool_config],
      thinking_config=types.ThinkingConfig(include_thoughts=True)
  ),
)

print(f"\nFinal model response: {response_2.text}")
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

// This is a manual, two turn multimodal function calling workflow:
// 1. Define the function tool
const getImageDeclaration = {
  name: 'get_image',
  description: 'Retrieves the image file reference for a specific order item.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      item_name: {
        type: Type.STRING,
        description: "The name or description of the item ordered (e.g., 'instrument').",
      },
    },
    required: ['item_name'],
  },
};

const toolConfig = {
  functionDeclarations: [getImageDeclaration],
};

// 2. Send a message that triggers the tool
const prompt = 'Show me the instrument I ordered last month.';
const response1 = await client.models.generateContent({
  model: 'gemini-3-flash-preview',
  contents: prompt,
  config: {
    tools: [toolConfig],
  },
});

// 3. Handle the function call
const functionCall = response1.functionCalls[0];
const requestedItem = functionCall.args.item_name;
console.log(`Model wants to call: ${functionCall.name}`);

// Execute your tool (e.g., call an API)
// (This is a mock response for the example)
console.log(`Calling external tool for: ${requestedItem}`);

const functionResponseData = {
  image_ref: { $ref: 'instrument.jpg' },
};

const imageUrl = "https://goo.gle/instrument-img";
const response = await fetch(imageUrl);
const imageArrayBuffer = await response.arrayBuffer();
const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

const functionResponseMultimodalData = {
  inlineData: {
    mimeType: 'image/jpeg',
    displayName: 'instrument.jpg',
    data: base64ImageData,
  },
};

// 4. Send the tool's result back
// Append this turn's messages to history for a final response.
const history = [
  { role: 'user', parts: [{ text: prompt }] },
  response1.candidates[0].content,
  {
    role: 'tool',
    parts: [
      {
        functionResponse: {
          name: functionCall.name,
          response: functionResponseData,
          parts: [functionResponseMultimodalData],
        },
      },
    ],
  },
];

const response2 = await client.models.generateContent({
  model: 'gemini-3-flash-preview',
  contents: history,
  config: {
    tools: [toolConfig],
    thinkingConfig: { includeThoughts: true },
  },
});

console.log(`\nFinal model response: ${response2.text}`);
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

# Check for macOS
if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      ...,
      {
        "role": "user",
        "parts": [
        {
            "functionResponse": {
              "name": "get_image",
              "response": {
                "image_ref": {
                  "$ref": "instrument.jpg"
                }
              },
              "parts": [
                {
                  "inlineData": {
                    "displayName": "instrument.jpg",
                    "mimeType":"'"$MIME_TYPE"'",
                    "data": "'"$IMAGE_B64"'"
                  }
                }
              ]
            }
          }
        ]
      }
    ]
  }'
```

### שילוב של כלים מובנים וקריאה לפונקציות

‫Gemini 3 מאפשר שימוש בכלים מובנים (כמו חיפוש Google, הקשר של כתובת URL ו[עוד](https://ai.google.dev/gemini-api/docs/tools?hl=he)) ובכלים מותאמים אישית של [קריאות לפונקציות](https://ai.google.dev/gemini-api/docs/function-calling?hl=he) באותה קריאה ל-API, וכך מאפשר תהליכי עבודה מורכבים יותר. מידע נוסף זמין בדף [שילובים של כלים](https://ai.google.dev/gemini-api/docs/tool-combination?hl=he).

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

getWeather = {
    "name": "getWeather",
    "description": "Gets the weather for a requested city.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The city and state, e.g. Utqiaġvik, Alaska",
            },
        },
        "required": ["city"],
    },
}

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="What is the northernmost city in the United States? What's the weather like there today?",
    config=types.GenerateContentConfig(
      tools=[
        types.Tool(
          google_search=types.ToolGoogleSearch(),  # Built-in tool
          function_declarations=[getWeather]       # Custom tool
        ),
      ],
      include_server_side_tool_invocations=True
    ),
)

history = [
    types.Content(
        role="user",
        parts=[types.Part(text="What is the northernmost city in the United States? What's the weather like there today?")]
    ),
    response.candidates[0].content,
    types.Content(
        role="user",
        parts=[types.Part(
            function_response=types.FunctionResponse(
                name="getWeather",
                response={"response": "Very cold. 22 degrees Fahrenheit."},
                id=response.candidates[0].content.parts[2].function_call.id
            )
        )]
    )
]

response_2 = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=history,
    config=types.GenerateContentConfig(
      tools=[
        types.Tool(
          google_search=types.ToolGoogleSearch(),
          function_declarations=[getWeather]
        ),
      ],
      include_server_side_tool_invocations=True
    ),
)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({});

const getWeather = {
    name: "getWeather",
    description: "Get the weather in a given location",
    parameters: {
        type: "OBJECT",
        properties: {
            location: {
                type: "STRING",
                description: "The city and state, e.g. San Francisco, CA"
            }
        },
        required: ["location"]
    }
};

async function run() {
    const model = client.models.generateContent({
        model: "gemini-3-flash-preview",
    });

    const tools = [
      { googleSearch: {} },
      { functionDeclarations: [getWeather] }
    ];
    const toolConfig = { includeServerSideToolInvocations: true };

    const result1 = await model.generateContent({
        contents: [{role: "user", parts: [{text: "What is the northernmost city in the United States? What's the weather like there today?"}]}],
        tools: tools,
        toolConfig: toolConfig,
    });

    const response1 = result1.response;
    const functionCallId = response1.candidates[0].content.parts.find(p => p.functionCall)?.functionCall?.id;

    const history = [
        {
            role: "user",
            parts:[{text: "What is the northernmost city in the United States? What's the weather like there today?"}]
        },
        response1.candidates[0].content,
        {
            role: "user",
            parts: [{
                functionResponse: {
                    name: "getWeather",
                    response: {response: "Very cold. 22 degrees Fahrenheit."},
                    id: functionCallId
                }
            }]
        }
    ];

    const result2 = await model.generateContent({
        contents: history,
        tools: tools,
        toolConfig: toolConfig,
    });
}

run();
```

## העברה מ-Gemini 2.5

‫Gemini 3 היא משפחת המודלים הכי מתקדמת שלנו עד היום, והיא מציעה שיפור הדרגתי בהשוואה ל-Gemini 2.5. כשמבצעים העברה, חשוב לקחת בחשבון את הנקודות הבאות:

- **מצב 'מעמיק':** אם השתמשתם בעבר בהנדסת הנחיות מורכבת (כמו שרשרת מחשבות) כדי לגרום ל-Gemini 2.5 להסיק מסקנות, נסו להשתמש ב-Gemini 3 עם `thinking_level: "high"` והנחיות פשוטות יותר.
- **הגדרות רמת אקראיות:** אם הקוד הקיים מגדיר במפורש את רמת האקראיות (במיוחד לערכים נמוכים של פלט דטרמיניסטי), מומלץ להסיר את הפרמטר הזה ולהשתמש בערך ברירת המחדל של Gemini 3, שהוא 1.0, כדי למנוע בעיות פוטנציאליות של לולאות או ירידה בביצועים במשימות מורכבות.
- **הבנה של מסמכי PDF:**
  אם הסתמכתם על התנהגות ספציפית של ניתוח מסמכים צפופים, כדאי לבדוק את ההגדרה החדשה `media_resolution_high` כדי לוודא שהדיוק נשמר.
- **צריכת טוקנים:** המעבר לברירות המחדל של Gemini 3 עשוי **להגדיל** את השימוש בטוקנים בקובצי PDF, אבל **להקטין** את השימוש בטוקנים בסרטונים. אם הבקשות חורגות עכשיו מחלון ההקשר בגלל רזולוציות ברירת מחדל גבוהות יותר, מומלץ להקטין באופן מפורש את רזולוציית המדיה.
- **חלוקת תמונות למקטעים:** אין תמיכה ביכולות חלוקת תמונות למקטעים (החזרת מסכות של אובייקטים ברמת הפיקסל) ב-Gemini 3 Pro או ב-Gemini 3 Flash. לגבי עומסי עבודה שדורשים חלוקת תמונות למקטעים מקורי, מומלץ להמשיך להשתמש ב-Gemini 2.5 Flash עם השבתת המצב 'חשיבה' או ב-[Gemini Robotics-ER 1.6](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=he).
- **שימוש במחשב:** מודלים Gemini 3 Pro ו-Gemini 3 Flash תומכים ב[שימוש במחשב](https://ai.google.dev/gemini-api/docs/computer-use?hl=he). בשונה מסדרת 2.5, לא צריך להשתמש במודל נפרד כדי לגשת לכלי 'שימוש במחשב'.
- **תמיכה בכלי עזר**: [שילוב של כלי עזר מובנים עם בקשות להפעלת פונקציות](https://ai.google.dev/gemini-api/docs/tool-combination?hl=he) נתמך עכשיו במודלים של Gemini 3. ‫[Maps grounding](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=he) נתמך עכשיו גם במודלים של Gemini 3.

## תאימות ל-OpenAI

משתמשים ב-[OpenAI compatibility layer](https://ai.google.dev/gemini-api/docs/openai?hl=he)? פרמטרים רגילים (`reasoning_effort` של OpenAI) ממופים אוטומטית למקבילים ב-Gemini (`thinking_level`).

## שיטות מומלצות לכתיבת הנחיות

‫Gemini 3 הוא מודל חשיבה רציונלית, ולכן צריך לשנות את ההנחיות שנותנים לו.

- **הוראות מדויקות:** כדאי לנסח את ההנחיות בצורה תמציתית. כדי לקבל את התשובות הכי טובות מ-Gemini 3, מומלץ לתת לו הוראות ברורות וישירות. יכול להיות שהיא תנתח יתר על המידה טכניקות מפורטות או מורכבות מדי של הנדסת הנחיות ששימשו ליצירת מודלים ישנים יותר.
- **פירוט הפלט:** כברירת מחדל, Gemini 3 פחות מפורט ומעדיף לספק תשובות ישירות ויעילות. אם התרחיש לדוגמה שלכם מחייב אישיות יותר שיחתית או "פטפטנית", אתם צריכים להנחות את המודל באופן מפורש בהנחיה (למשל, "תסביר את זה בתור עוזר ידידותי ופטפטן").
- **ניהול הקשר:** כשעובדים עם מערכי נתונים גדולים (למשל, ספרים שלמים, בסיסי קוד או סרטונים ארוכים), כדאי למקם את ההוראות או השאלות הספציפיות בסוף ההנחיה, אחרי הקשר של הנתונים. כדי להבסס את הנימוקים של המודל על הנתונים שסיפקתם, כדאי להתחיל את השאלה בניסוח כמו "בהתבסס על המידע שלמעלה...".

מידע נוסף על אסטרטגיות לעיצוב הנחיות זמין ב[מדריך להנדסת הנחיות](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=he).

## שאלות נפוצות

1. **מהו תאריך סף הידע של Gemini 3?** למודלים של Gemini 3 יש תאריך סף ידע של ינואר 2025. כדי לקבל מידע עדכני יותר, אפשר להשתמש בכלי [הארקה של חיפוש](https://ai.google.dev/gemini-api/docs/google-search?hl=he).
2. **מהן המגבלות של חלון ההקשר?** מודלים של Gemini 3 תומכים בחלון הקשר של מיליון טוקנים של קלט ועד 64,000 טוקנים של פלט.
3. **יש תוכנית בחינם ל-Gemini 3?** ל-Gemini 3 Flash‏`gemini-3-flash-preview` ול-3.1 Flash-Lite‏ `gemini-3.1-flash-lite` יש רמות שימוש חינמיות ב-Gemini API. אתם יכולים לנסות את Gemini 3.1 Pro ו-3 Flash בחינם ב-Google AI Studio, אבל אין רמת שימוש חינמית ל-`gemini-3.1-pro-preview` ב-Gemini API.
4. **האם הקוד הישן שלי של `thinking_budget` עדיין יעבוד?** כן, `thinking_budget` עדיין נתמך לצורך תאימות לאחור, אבל מומלץ לעבור ל-`thinking_level` כדי לקבל ביצועים צפויים יותר. אין להשתמש בשניהם באותה בקשה.
5. **האם Gemini 3 תומך ב-Batch API?** כן, Gemini 3 תומך ב-[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=he).
6. **האם יש תמיכה בשמירת נתונים במטמון לפי הקשר?** כן, [שמירת ההקשר במטמון](https://ai.google.dev/gemini-api/docs/caching?hl=he) נתמכת ב-Gemini 3.
7. **אילו כלים נתמכים ב-Gemini 3?** ‫Gemini 3 תומך ב[חיפוש Google](https://ai.google.dev/gemini-api/docs/google-search?hl=he), ב[עיגון באמצעות מפות Google](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=he), ב[חיפוש קבצים](https://ai.google.dev/gemini-api/docs/file-search?hl=he), ב[הרצת קוד](https://ai.google.dev/gemini-api/docs/code-execution?hl=he) וב[הקשר של כתובת URL](https://ai.google.dev/gemini-api/docs/url-context?hl=he). הוא גם תומך ב[קריאה לפונקציות](https://ai.google.dev/gemini-api/docs/function-calling?hl=he) רגילות עבור כלים מותאמים אישית משלכם, ו[בשילוב עם כלים מובנים](https://ai.google.dev/gemini-api/docs/tool-combination?hl=he).
8. **מה זה `gemini-3.1-pro-preview-customtools`?** אם אתם משתמשים ב-`gemini-3.1-pro-preview` והמודל מתעלם מהכלים המותאמים אישית שלכם ומעדיף פקודות bash, נסו להשתמש במודל `gemini-3.1-pro-preview-customtools`. [מידע נוסף](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=he#gemini-31-pro-preview-customtools)

## השלבים הבאים

- [איך מתחילים להשתמש ב-Gemini 3 Cookbook](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started.ipynb?hl=he#templateParams=%7B%22MODEL_ID%22:+%22gemini-3-pro-preview%22%7D)
- כדאי לעיין במדריך הייעודי בנושא [רמות חשיבה](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_thinking_REST.ipynb?hl=he#gemini3) ובנושא המעבר מתקציב חשיבה לרמות חשיבה.

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-05-29 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-05-29 (שעון UTC)."],[],[]]
